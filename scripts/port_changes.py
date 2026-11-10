#!/usr/bin/env python3
"""
Reporte sur la branche GitBook les modifications faites sur une branche source (main, ou la
branche de l'équipe Intégrations) depuis la dernière synchronisation, SANS fusion Git.

Pour chaque fichier modifié côté source :
  base   = version source lors de la dernière synchro, convertie en syntaxe GitBook
  source = version source actuelle, convertie en syntaxe GitBook
  ours   = version actuelle sur la branche GitBook, à son emplacement actuel
           (renommages faits dans GitBook suivis automatiquement, ex. xdr -> defend)
puis fusion à trois voies (git merge-file) : seule la modification du rédacteur est
appliquée, déjà convertie. Les conflits restent marqués <<<<<<< dans le fichier.

Usage : python scripts/port_changes.py --source origin/main [--write]
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import convert_mkdocs as cm  # noqa: E402

BASELINE = "gitbook-baseline"   # fin de la préparation : point de départ des renommages GitBook
MANIFEST = Path("migration/materialized.tsv")
LINK_RE = re.compile(r'(\]\()([^)\s#:]+\.md)(#[^)\s]*)?(\))')


def git(*a, check=True):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=check).stdout


def show(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def sync_tag(source):
    return "sync/" + source.split("/", 1)[-1]


def build_rename_map():
    files, dirs = {}, {}
    for line in git("diff", "-M", "--name-status", BASELINE, "HEAD").splitlines():
        p = line.split("\t")
        if p[0].startswith("R"):
            files[p[1]] = p[2]
            a, b = p[1].split("/"), p[2].split("/")
            while a and b and a[-1] == b[-1]:
                a.pop(), b.pop()
            if a and b:
                dirs["/".join(a)] = "/".join(b)
    return files, dirs


def map_path(path, files, dirs):
    if path in files:
        return files[path]
    for old in sorted(dirs, key=len, reverse=True):
        if path.startswith(old + "/"):
            return dirs[old] + path[len(old):]
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="ex. origin/main")
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--exclude", action="append", default=[], help="sous-dossier de docs non converti")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    tag = sync_tag(args.source)
    base_ref = git("rev-parse", "-q", "--verify", f"refs/tags/{tag}", check=False).strip() \
        or git("merge-base", args.source, "pre-migration").strip()
    src_ref = git("rev-parse", args.source).strip()
    Path(".git/port_source_ref").unlink(missing_ok=True)
    if base_ref == src_ref:
        print("Rien de nouveau.")
        return
    files_map, dirs_map = build_rename_map()
    manifest = [l.split("\t") for l in MANIFEST.read_text().splitlines() if l.strip()] if MANIFEST.exists() else []

    # Arbre de la source pour résoudre liens et inclusions comme MkDocs le ferait
    wt = Path(tempfile.mkdtemp(prefix="port-src-"))
    git("worktree", "add", "--detach", "-f", str(wt), src_ref)
    report = {"appliqué": [], "conflit": [], "nouveau": [], "supprimé côté source": [], "copié brut": []}
    try:
        diff = git("diff", "-M", "--name-status", base_ref, src_ref, "--", args.docs, "_shared_content")
        for line in diff.splitlines():
            st, *paths = line.split("\t")
            old_src, new_src = (paths[0], paths[-1])
            if new_src.startswith("_shared_content/"):
                # Miroir brut (pour les inclusions), puis report dans la copie éventuelle
                if args.write and st[0] != "D":
                    Path(new_src).parent.mkdir(parents=True, exist_ok=True)
                    Path(new_src).write_text(show(src_ref, new_src) or "", encoding="utf-8")
                report["copié brut"].append(new_src)
                docs_path = next((d + new_src[len(s):] for d, s in manifest
                                  if new_src == s or new_src.startswith(s + "/")), None)
                if not docs_path:
                    continue
            else:
                docs_path = new_src
            if st[0] == "D":
                report["supprimé côté source"].append(map_path(docs_path, files_map, dirs_map))
                continue
            if not new_src.endswith(".md"):
                dest = map_path(docs_path, files_map, dirs_map)
                if args.write:
                    Path(dest).parent.mkdir(parents=True, exist_ok=True)
                    Path(dest).write_bytes(subprocess.run(["git", "show", f"{src_ref}:{new_src}"],
                                                          capture_output=True).stdout)
                report["appliqué"].append(dest)
                continue

            rel = docs_path[len(args.docs) + 1:]
            excluded = any(rel.startswith(e.strip("/") + "/") for e in args.exclude)

            def conv(text):
                if text is None or excluded:
                    return text
                return cm.convert(text, wt / docs_path, wt / args.docs, wt, True)

            base_txt = conv(show(base_ref, old_src))
            src_txt = conv(show(src_ref, new_src))
            dest = map_path(docs_path, files_map, dirs_map)
            ours = Path(dest).read_text(encoding="utf-8") if Path(dest).exists() else None

            if ours is None or base_txt is None:
                result, conflicts = src_txt, 0
                report["nouveau"].append(dest)
            else:
                with tempfile.TemporaryDirectory() as td:
                    o, b, s = (Path(td) / n for n in ("ours", "base", "src"))
                    o.write_text(ours), b.write_text(base_txt), s.write_text(src_txt)
                    r = subprocess.run(["git", "merge-file", "-p", "-L", "GitBook", "-L", "base",
                                        "-L", args.source, str(o), str(b), str(s)],
                                       capture_output=True, text=True)
                    result, conflicts = r.stdout, r.returncode
                report["conflit" if conflicts else "appliqué"].append(dest)

            # Liens écrits vers d'anciens emplacements : on suit les renommages GitBook
            def fix(m):
                tgt = os.path.normpath(os.path.join(os.path.dirname(docs_path), m.group(2)))
                if Path(os.path.normpath(os.path.join(os.path.dirname(dest), m.group(2)))).exists():
                    return m.group(0)
                new_t = map_path(tgt, files_map, dirs_map)
                return f"{m.group(1)}{os.path.relpath(new_t, os.path.dirname(dest))}{m.group(3) or ''}{m.group(4)}"
            result = LINK_RE.sub(fix, result)

            if args.write:
                Path(dest).parent.mkdir(parents=True, exist_ok=True)
                Path(dest).write_text(result, encoding="utf-8")
    finally:
        git("worktree", "remove", "--force", str(wt), check=False)

    print(f"Report de {args.source} ({base_ref[:8]}..{src_ref[:8]})")
    for k, v in report.items():
        if v and k != "copié brut":
            print(f"  {k} : {len(v)}")
            for p in v:
                print(f"    {'!' if k in ('conflit', 'supprimé côté source') else '-'} {p}")
    if args.write:
        Path(".git/port_source_ref").write_text(src_ref)
    sys.exit(2 if report["conflit"] else 0)


if __name__ == "__main__":
    main()
