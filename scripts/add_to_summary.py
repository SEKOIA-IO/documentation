#!/usr/bin/env python3
"""
Ajoute dans SUMMARY.md les nouvelles pages reportées depuis la source, à la position
qu'elles occupent dans la navigation MkDocs (mkdocs.yml de la source) : juste après la
page qui les précède, ou comme premier enfant de leur section. Les renommages faits
dans GitBook sont pris en compte. Appelé par sync_from_branch.sh.

Usage : python scripts/add_to_summary.py --source origin/main [--docs docs]
"""
import argparse
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from port_changes import build_rename_map, map_path  # noqa: E402

NEW = Path(".git/port_new_pages.tsv")


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("", lambda loader, suffix, node: None)


def flatten(items, depth=0, out=None):
    out = [] if out is None else out
    for e in items or []:
        if isinstance(e, str):
            out.append((depth, None, e))
            continue
        title, v = next(iter(e.items()))
        if isinstance(v, list):
            out.append((depth, title, None))          # section
            flatten(v, depth + 1, out)
        else:
            out.append((depth, title, v))
    return out


def h1(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(path).stem.replace("_", " ").capitalize()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--docs", default="docs")
    args = ap.parse_args()
    if not NEW.exists() or not NEW.read_text().strip():
        return
    cfg = subprocess.run(["git", "show", f"{args.source}:mkdocs.yml"], capture_output=True, text=True).stdout
    nav = flatten(yaml.load(cfg, Loader=Loader).get("nav", []))
    files_map, dirs_map = build_rename_map()
    docs_prefix = args.docs.rstrip("/") + "/"
    for src_path, dest in (l.split("\t") for l in NEW.read_text().splitlines() if l.strip()):
        # SUMMARY.md le plus proche : celui de la section (ou celui de docs/ avant découpage)
        summary_path = next((p / "SUMMARY.md" for p in Path(dest).parents if (p / "SUMMARY.md").exists()), None)
        if summary_path is None:
            print(f"  ! {dest} : aucun SUMMARY.md trouvé")
            continue
        lines = summary_path.read_text(encoding="utf-8").split("\n")
        prefix = summary_path.parent.as_posix() + "/"

        def summary_target(nav_path):
            t = map_path(docs_prefix + nav_path, files_map, dirs_map)
            return t[len(prefix):] if t.startswith(prefix) else None

        def find_line(target):
            return next((i for i, l in enumerate(lines) if target and f"]({target})" in l), None)

        rel_src, rel_dest = src_path[len(docs_prefix):], dest[len(prefix):]
        if not rel_dest.endswith(".md") or find_line(rel_dest) is not None:
            continue
        idx = next((i for i, (_, _, p) in enumerate(nav) if p == rel_src), None)
        if idx is None:
            print(f"  ! {rel_dest} : absente de la nav de mkdocs.yml, à placer à la main dans GitBook")
            continue
        depth, title = nav[idx][0], nav[idx][1] or h1(dest)
        pos = None
        for j in range(idx - 1, -1, -1):
            d, _, p = nav[j]
            if p is None:
                continue
            k = find_line(summary_target(p))
            if k is None:
                continue
            indent = len(lines[k]) - len(lines[k].lstrip())
            if d < depth:                 # page parente : on devient son premier enfant
                pos, indent = k + 1, indent + 2
            else:                         # page sœur : on se place après elle et ses enfants
                pos = k + 1
                while pos < len(lines) and lines[pos].strip() and \
                        len(lines[pos]) - len(lines[pos].lstrip()) > indent:
                    pos += 1
            break
        if pos is None:
            print(f"  ! {rel_dest} : aucune page voisine trouvée dans SUMMARY.md, à placer à la main")
            continue
        lines.insert(pos, " " * indent + f"* [{title}]({rel_dest})")
        print(f"  + {rel_dest} ajoutée à {summary_path} (ligne {pos + 1})")
        summary_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
