#!/usr/bin/env python3
"""
Convertit la syntaxe MkDocs Material de la doc Sekoia en syntaxe GitBook.

Idempotent : relançable sans risque (ce qui est déjà converti n'est plus détecté).

Conversions :
  !!! type "Titre"         -> {% hint style="..." %}   (titre conservé en gras)
  ??? type "Titre"         -> <details><summary>Titre</summary> ... </details>
  === "Onglet"             -> {% tabs %}{% tab title="Onglet" %} ... {% endtabs %}
  ![img](x){: style=...}   -> ![img](x)                (attributs MkDocs supprimés)
  ](/xdr/page.md)          -> ](../../xdr/page.md)     (liens absolus -> relatifs)
  {!_shared_content/x.md!} -> contenu du fichier inclus (option --inline-includes)

Usage :
  python scripts/convert_mkdocs.py docs/ --exclude integration            # simulation
  python scripts/convert_mkdocs.py docs/ --exclude integration --write
  python scripts/convert_mkdocs.py docs/ --since gitbook-last-sync --write  # fichiers modifiés seulement
"""
import argparse
import os
import re
import subprocess
import sys
from urllib.parse import quote, unquote
from collections import Counter
from pathlib import Path

HINT_STYLE = {
    "note": "info", "info": "info", "abstract": "info", "summary": "info", "example": "info",
    "quote": "info", "question": "info", "alternative": "info",
    "tip": "success", "tips": "success", "success": "success", "check": "success", "done": "success",
    "warning": "warning", "important": "warning", "caution": "warning", "attention": "warning",
    "danger": "danger", "error": "danger", "failure": "danger", "bug": "danger",
}
ADMON_RE = re.compile(r'^(?P<ind>[ \t]*)(?P<mark>!!!|\?\?\?\+?)\s*(?P<type>[\w-]+)?\s*(?:"(?P<title>[^"]*)")?\s*$')
TAB_RE = re.compile(r'^(?P<ind>[ \t]*)===\+?\s+"(?P<title>[^"]*)"\s*$')
FENCE_RE = re.compile(r'^\s*(`{3,}|~{3,})')
ATTR_RE = re.compile(r'(\]\([^)]*\))\{[^}\n]*\}')
LINK_RE = re.compile(r'(\]\()(/[^)\s#]*)(#[^)\s]*)?(\))')
INCLUDE_RE = re.compile(r'\{!\s*([^!\s]+)\s*!\}')
# Les contenus inclus sont encadrés de balises pour pouvoir être rafraîchis
# quand le fichier source de _shared_content change (contenus générés notamment).
MARKED_RE = re.compile(r'<!-- include:(?P<p>[^ ]+) -->\n.*?\n<!-- endinclude:(?P=p) -->', re.S)

stats = Counter()
CURRENT = [""]  # fichier en cours, pour les messages


def indent_width(s):
    return len(s.expandtabs(4)) - len(s.expandtabs(4).lstrip(" "))


def take_block(lines, i, base):
    """Récupère les lignes indentées (corps d'une admonition ou d'un onglet)."""
    body = []
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            body.append("")
            i += 1
            continue
        if indent_width(line) > base:
            body.append(line.expandtabs(4)[base + 4:] if indent_width(line) >= base + 4 else line.lstrip())
            i += 1
            continue
        break
    while body and body[-1] == "":
        body.pop()
        i -= 1
    return body, i


def convert_blocks(lines):
    out, i, fence = [], 0, None
    while i < len(lines):
        line = lines[i]
        m_f = FENCE_RE.match(line)
        if m_f:
            mk = m_f.group(1)
            if fence is None:
                fence = (mk[0], len(mk))
            elif mk[0] == fence[0] and len(mk) >= fence[1]:
                fence = None
            out.append(line)
            i += 1
            continue
        if fence:
            out.append(line)
            i += 1
            continue

        m = ADMON_RE.match(line)
        if m:
            ind, base = m.group("ind"), indent_width(line)
            kind = (m.group("type") or "note").lower()
            title = m.group("title")
            body, i = take_block(lines, i + 1, base)
            if not any(b.strip() for b in body):
                stats["encadrés vides dans la source (texte non indenté : à corriger à la main)"] += 1
                print(f"  ! {CURRENT[0]}: encadré vide : « {line.strip()} » (le texte qui suit n'est pas indenté)", file=sys.stderr)
            body = [ind + b if b else "" for b in convert_blocks(body)]
            if m.group("mark").startswith("???"):
                summary = title or kind.capitalize()
                out += [f"{ind}<details>", f"{ind}<summary>{summary}</summary>", ""] + body + ["", f"{ind}</details>"]
                stats["dépliables ???"] += 1
            else:
                style = HINT_STYLE.get(kind, "info")
                if kind not in HINT_STYLE:
                    stats[f"type d'encadré inconnu « {kind} » -> info"] += 1
                head = [f"{ind}**{title}**", ""] if title else []
                out += [f'{ind}{{% hint style="{style}" %}}'] + head + body + [f"{ind}{{% endhint %}}"]
                stats["encadrés !!!"] += 1
            continue

        m = TAB_RE.match(line)
        if m:
            ind, base = m.group("ind"), indent_width(line)
            out.append(f"{ind}{{% tabs %}}")
            while True:
                body, i = take_block(lines, i + 1, base)
                body = [ind + b if b else "" for b in convert_blocks(body)]
                out += [f'{ind}{{% tab title="{m.group("title")}" %}}'] + body + [f"{ind}{{% endtab %}}"]
                stats["onglets ==="] += 1
                j = i
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                m = TAB_RE.match(lines[j]) if j < len(lines) else None
                if not m or indent_width(lines[j]) != base:
                    break
                i = j
            out.append(f"{ind}{{% endtabs %}}")
            continue

        out.append(line)
        i += 1
    return out


def convert_inline(text, path, docs_root):
    def attr(m):
        stats["attributs {: ...} supprimés"] += 1
        return m.group(1)
    text = ATTR_RE.sub(attr, text)

    def link(m):
        target = unquote(m.group(2))
        abs_target = docs_root / target.lstrip("/")
        if not abs_target.exists() and not Path(target).suffix:
            abs_target = docs_root / (target.strip("/") + ".md")
        if not abs_target.exists():
            stats["liens absolus vers une cible introuvable (laissés tels quels)"] += 1
            print(f"  ! lien introuvable : {path}: {target}", file=sys.stderr)
            return m.group(0)
        rel = quote(os.path.relpath(abs_target, path.parent).replace(os.sep, "/"))
        stats["liens absolus -> relatifs"] += 1
        return f"{m.group(1)}{rel}{m.group(3) or ''}{m.group(4)}"
    return LINK_RE.sub(link, text)


def inline_includes(text, repo_root, depth=0):
    def raw(rel):
        content = (repo_root / rel).read_text(encoding="utf-8").rstrip("\n")
        return inline_includes(content, repo_root, depth + 1) if depth < 5 else content

    def repl(m):
        rel = m.group(1)
        if not (repo_root / rel).exists():
            stats["inclusions introuvables"] += 1
            print(f"  ! {CURRENT[0]}: inclusion introuvable : {rel}", file=sys.stderr)
            return m.group(0)
        stats["inclusions {!...!} remplacées"] += 1
        if depth:  # inclusion imbriquée : pas de balises
            return raw(rel)
        return f"<!-- include:{rel} -->\n{raw(rel)}\n<!-- endinclude:{rel} -->"

    def refresh(m):
        rel = m.group("p")
        if not (repo_root / rel).exists():
            return m.group(0)
        return f"<!-- include:{rel} -->\n{raw(rel)}\n<!-- endinclude:{rel} -->"

    if depth == 0:
        text = MARKED_RE.sub(refresh, text)
    return INCLUDE_RE.sub(repl, text)


def convert(text, path, docs_root, repo_root, do_includes):
    if do_includes:
        text = inline_includes(text, repo_root)
    text = "\n".join(convert_blocks(text.split("\n")))
    return convert_inline(text, path, docs_root)


def changed_files(ref, root):
    top = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                              text=True, check=True).stdout.strip())
    out = subprocess.run(["git", "diff", "--name-only", "-M", "--diff-filter=ACMR", ref, "HEAD", "--", str(root)],
                         capture_output=True, text=True, check=True).stdout
    return [(top / f).absolute() for f in out.splitlines() if f.endswith(".md") and (top / f).exists()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docs_root", type=Path)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true", help="code 1 si des fichiers restent à convertir (CI)")
    ap.add_argument("--since", metavar="REF", help="seulement les fichiers modifiés depuis ce tag/commit")
    ap.add_argument("--exclude", action="append", default=[], help="sous-dossier à ignorer (répétable)")
    ap.add_argument("--only", action="append", default=[], help="ne traiter que ce sous-dossier (répétable)")
    ap.add_argument("--inline-includes", action="store_true", help="remplacer {!...!} par le contenu inclus")
    ap.add_argument("--repo-root", type=Path, default=Path("."), help="base des chemins {!...!} (défaut : .)")
    args = ap.parse_args()

    docs_root = args.docs_root.absolute()
    files = changed_files(args.since, args.docs_root) if args.since else sorted(docs_root.rglob("*.md"))
    if args.since and args.inline_includes:
        # Pages dont un contenu inclus a changé dans _shared_content depuis REF
        repo = args.repo_root.absolute()
        shared = {p.relative_to(repo).as_posix() for p in changed_files(args.since, repo / "_shared_content")}
        if shared:
            for p in docs_root.rglob("*.md"):
                if not p.is_symlink() and any(f"<!-- include:{r} -->" in p.read_text(encoding="utf-8") for r in shared):
                    files.append(p.absolute())
            files = sorted(set(files))
    changed = []
    for path in files:
        path = path.absolute()
        rel = path.relative_to(docs_root).as_posix()
        if any(rel.startswith(e.strip("/") + "/") for e in args.exclude):
            continue
        if args.only and not any(rel.startswith(o.strip("/") + "/") for o in args.only):
            continue
        if path.is_symlink():
            stats["liens symboliques (à remplacer par de vrais fichiers, non suivis)"] += 1
            print(f"  ! lien symbolique : {rel} -> {os.readlink(path)}", file=sys.stderr)
            continue
        CURRENT[0] = rel
        original = path.read_text(encoding="utf-8")
        new = convert(original, path, docs_root, args.repo_root.resolve(), args.inline_includes)
        if new != original:
            changed.append(rel)
            if args.write:
                path.write_text(new, encoding="utf-8")

    print(f"{len(changed)} fichier(s) {'convertis' if args.write else 'à convertir'}")
    for k, v in sorted(stats.items()):
        print(f"  {v:5}  {k}")
    if args.check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
