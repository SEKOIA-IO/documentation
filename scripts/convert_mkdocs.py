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
  {!_shared_content/x.md!} -> {% include "../.gitbook/includes/x.md" %} (option --gitbook-includes :
                              contenu réutilisable GitBook, les inclusions générées restent telles quelles)
  ++ctrl+c++               -> `Ctrl+C`
  code  # (1)              -> code                     (marqueurs d'annotation retirés, la liste reste)

Les fins de ligne (LF ou CRLF) de chaque fichier sont conservées.

Ce qui reste à reprendre à la main (HTML avec style, <br>, <table>, <iframe>/<video>,
attributs hors liens) est signalé dans le rapport, fichier par fichier, sans être modifié.

Usage :
  python scripts/convert_mkdocs.py docs/ --exclude integration            # simulation
  python scripts/convert_mkdocs.py docs/ --exclude integration --write
  python scripts/convert_mkdocs.py docs/ --since gitbook-last-sync --write  # fichiers modifiés seulement

  # Integration team usage :
  python scripts/convert_mkdocs.py docs/ --only integration --exclude integration/action_library
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
    "information": "info", "prerequisites": "info",
    "warning": "warning", "important": "warning", "caution": "warning", "attention": "warning",
    "warn": "warning", "disclaimer": "warning",
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
# Raccourcis clavier pymdownx.keys : ++ctrl+alt+del++
KEYS_RE = re.compile(r'\+\+([A-Za-z0-9]+(?:\+[A-Za-z0-9]+)*)\+\+')
# Annotations de code (content.code.annotate) : marqueur « # (1) » ou « // (1)! » en fin de ligne,
# retiré seulement si le bloc est suivi de sa liste d'annotations (« 1. ... »), pour ne pas
# toucher du code ordinaire comme « count // (2) »
ANNOT_RE = re.compile(r'\s*(?:#|//)\s*\(\d+\)!?\s*$')
ANNOT_LIST_RE = re.compile(r'\s*1\.\s+\S')
# Code en ligne `...` (ou ``...``), laissé tel quel par convert_keys
CODE_SPAN_RE = re.compile(r'(`+).*?\1')
# Syntaxe non convertie automatiquement, signalée pour reprise à la main (hors blocs de code)
TO_REVIEW = {
    "HTML avec style": re.compile(r'<[a-z][\w-]*\b[^>]*\bstyle=', re.I),
    "balises <br>": re.compile(r'<br\s*/?>', re.I),
    "tableaux HTML": re.compile(r'<table\b', re.I),
    "<iframe>/<video>": re.compile(r'<(?:iframe|video)\b', re.I),
    "attributs {: ...} / {#...} hors liens": re.compile(r'\{:[^}\n]*\}|\{\s*[#.][\w-][^}\n%]*\}\s*$'),
}

# Inclusions produites par les générateurs (intakes : SekoiaLab/integration#1839, connecteurs d'actifs : #1840)
GENERATED_INCLUDE_RE = re.compile(r'generated|do_not_edit')

stats = Counter()
REUSABLE = {}  # contenu réutilisable à écrire (chemin -> texte), option --gitbook-includes
CURRENT = [""]  # fichier en cours, pour les messages
ANNOTATED = set()  # fichiers déjà signalés pour les annotations de code


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
                annotated = has_annotation_list(lines, i, fence)
                line = re.sub(r'\s*\{\s*\.annotate\s*\}', '', line)
            elif mk[0] == fence[0] and len(mk) >= fence[1]:
                fence = None
            out.append(line)
            i += 1
            continue
        if fence:
            out.append(strip_annotation(line) if annotated else line)
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

        out.append(convert_keys(line))
        i += 1
    return out


def has_annotation_list(lines, opening_fence_index, fence):
    fence_char, fence_len = fence

    def closes_fence(line):
        match = FENCE_RE.match(line)
        return bool(match) and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_len

    closing_fence_index = opening_fence_index + 1
    while closing_fence_index < len(lines) and not closes_fence(lines[closing_fence_index]):
        closing_fence_index += 1

    next_text_index = closing_fence_index + 1
    while next_text_index < len(lines) and lines[next_text_index].strip() == "":
        next_text_index += 1

    return next_text_index < len(lines) and bool(ANNOT_LIST_RE.match(lines[next_text_index]))


def strip_annotation(line):
    """Retire un marqueur d'annotation de code ; la liste d'annotations sous le bloc est conservée."""
    new = ANNOT_RE.sub("", line)
    if new != line:
        stats["annotations de code retirées (liste sous le bloc à relire)"] += 1
        if CURRENT[0] not in ANNOTATED:
            ANNOTATED.add(CURRENT[0])
            print(f"  ! {CURRENT[0]}: annotations de code retirées, relire la liste sous le bloc", file=sys.stderr)
    return new


def convert_keys(line):
    def keys(m):
        stats["raccourcis ++touches++"] += 1
        return "`" + "+".join(k.capitalize() for k in m.group(1).split("+")) + "`"
    parts, pos = [], 0
    for m in CODE_SPAN_RE.finditer(line):
        parts += [KEYS_RE.sub(keys, line[pos:m.start()]), m.group(0)]
        pos = m.end()
    parts.append(KEYS_RE.sub(keys, line[pos:]))
    return "".join(parts)


def report_to_review(text):
    """Signale (sans modifier) la syntaxe que le script ne sait pas convertir, hors blocs de code."""
    fence = None
    for n, line in enumerate(text.split("\n"), 1):
        m_f = FENCE_RE.match(line)
        if m_f:
            mk = m_f.group(1)
            if fence is None:
                fence = (mk[0], len(mk))
            elif mk[0] == fence[0] and len(mk) >= fence[1]:
                fence = None
            continue
        if fence:
            continue
        for label, rx in TO_REVIEW.items():
            if rx.search(line):
                stats[f"à reprendre à la main : {label}"] += 1
                print(f"  ! {CURRENT[0]}:{n}: à reprendre à la main ({label}) : {line.strip()[:100]}", file=sys.stderr)


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


def gitbook_includes(text, path, docs_root, repo_root):
    """{!_shared_content/x.md!} -> {% include "<relatif>/.gitbook/includes/x.md" %}.

    Le fichier inclus (écrit à la main) est converti et déposé dans le dossier .gitbook/includes/ de la
    section GitBook (premier dossier sous docs_root), où GitBook le lit comme contenu réutilisable.
    Une inclusion imbriquée est copiée dans le contenu réutilisable. Les inclusions générées sont laissées.
    """
    rel = path.relative_to(docs_root)
    section = docs_root / rel.parts[0] if len(rel.parts) > 1 else docs_root
    includes_dir = section / ".gitbook" / "includes"

    def repl(m):
        src = m.group(1)
        if GENERATED_INCLUDE_RE.search(src):
            stats["inclusions générées laissées telles quelles (générateurs à adapter)"] += 1
            return m.group(0)
        if not (repo_root / src).exists():
            stats["inclusions introuvables"] += 1
            print(f"  ! {CURRENT[0]}: inclusion introuvable : {src}", file=sys.stderr)
            return m.group(0)
        target = includes_dir / Path(src).name
        if target not in REUSABLE:
            page, CURRENT[0] = CURRENT[0], target.relative_to(docs_root).as_posix()
            content = (repo_root / src).read_text(encoding="utf-8").rstrip("\n")
            content = inline_includes(content, repo_root, depth=1)
            content = "\n".join(convert_blocks(content.split("\n")))
            REUSABLE[target] = convert_inline(content, target, docs_root) + "\n"
            CURRENT[0] = page
        stats["inclusions -> contenu réutilisable GitBook {% include %}"] += 1
        link = os.path.relpath(target, path.parent).replace(os.sep, "/")
        return f'{{% include "{link}" %}}'
    return INCLUDE_RE.sub(repl, text)


def convert(text, path, docs_root, repo_root, do_includes, do_gitbook_includes=False):
    if do_includes:
        text = inline_includes(text, repo_root)
    if do_gitbook_includes:
        text = gitbook_includes(text, path, docs_root, repo_root)
    text = "\n".join(convert_blocks(text.split("\n")))
    return convert_inline(text, path, docs_root)


def changed_files(ref, root):
    top = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                              text=True, check=True).stdout.strip())
    out = subprocess.run(["git", "diff", "--name-only", "-M", "--diff-filter=ACMR", ref, "HEAD", "--", str(root)],
                         capture_output=True, text=True, check=True).stdout
    return [(top / f).absolute() for f in out.splitlines() if f.endswith(".md") and (top / f).exists()]


def in_scope(rel, prefix):
    """Un dossier (et tout son contenu) ou un fichier précis."""
    prefix = prefix.strip("/")
    return rel == prefix or rel.startswith(prefix + "/")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docs_root", type=Path)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true", help="code 1 si des fichiers restent à convertir (CI)")
    ap.add_argument("--since", metavar="REF", help="seulement les fichiers modifiés depuis ce tag/commit")
    ap.add_argument("--exclude", action="append", default=[], help="sous-dossier à ignorer (répétable)")
    ap.add_argument("--only", action="append", default=[], help="ne traiter que ce sous-dossier (répétable)")
    ap.add_argument("--inline-includes", action="store_true", help="remplacer {!...!} par le contenu inclus")
    ap.add_argument("--gitbook-includes", action="store_true",
                    help="remplacer les {!...!} écrits à la main par un {%% include %%} GitBook "
                         "(fichier converti dans .gitbook/includes/ de la section) ; les inclusions générées restent")
    ap.add_argument("--repo-root", type=Path, default=Path("."), help="base des chemins {!...!} (défaut : .)")
    ap.add_argument("--report", action="store_true",
                    help="signaler, fichier par fichier, la syntaxe à reprendre à la main (HTML, embeds...)")
    args = ap.parse_args(argv)
    if args.inline_includes and args.gitbook_includes:
        ap.error("--inline-includes et --gitbook-includes sont exclusifs")

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
        if any(in_scope(rel, e) for e in args.exclude):
            continue
        if args.only and not any(in_scope(rel, o) for o in args.only):
            continue
        if path.is_symlink():
            stats["liens symboliques (à remplacer par de vrais fichiers, non suivis)"] += 1
            print(f"  ! lien symbolique : {rel} -> {os.readlink(path)}", file=sys.stderr)
            continue
        CURRENT[0] = rel
        # Lecture sans normalisation des fins de ligne, pour conserver le CRLF des fichiers qui en ont
        original = path.read_bytes().decode("utf-8")
        crlf = "\r\n" in original
        new = convert(original.replace("\r\n", "\n"), path, docs_root, args.repo_root.resolve(),
                      args.inline_includes, args.gitbook_includes)
        if args.report:
            report_to_review(new)
        if crlf:
            new = new.replace("\n", "\r\n")
        if new != original:
            changed.append(rel)
            if args.write:
                path.write_bytes(new.encode("utf-8"))

    for target, content in sorted(REUSABLE.items()):
        rel = target.relative_to(docs_root).as_posix()
        CURRENT[0] = rel
        if args.report:
            report_to_review(content)
        if target.exists() and target.read_text(encoding="utf-8") == content:
            continue
        changed.append(rel)
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

    print(f"{len(changed)} fichier(s) {'convertis' if args.write else 'à convertir'}")
    for k, v in sorted(stats.items()):
        print(f"  {v:5}  {k}")
    if args.check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
