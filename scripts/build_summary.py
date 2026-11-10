#!/usr/bin/env python3
"""
Génère SUMMARY.md (la navigation GitBook) à partir de la section `nav` de mkdocs.yml,
pour retrouver dans GitBook exactement l'arborescence et les titres du site actuel.

Usage :
  python scripts/build_summary.py --mkdocs mkdocs.yml --docs docs --exclude-section Integrations
"""
import argparse
import os
import re
import unicodedata
from pathlib import Path

import yaml


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("", lambda loader, suffix, node: None)  # ignore les !!python/...

stubs, missing, used = [], [], set()


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "section"


def is_page(v):
    return isinstance(v, str) and (v.endswith(".md") or v.startswith("http"))


def title_of(docs, path):
    try:
        for line in (docs / path).read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return Path(path).stem.replace("_", " ").capitalize()


def common_dir(items):
    paths = []
    def walk(it):
        for e in it:
            v = list(e.values())[0] if isinstance(e, dict) else e
            if isinstance(v, list):
                walk(v)
            elif is_page(v) and not v.startswith("http"):
                paths.append(os.path.dirname(v))
    walk(items)
    return os.path.commonpath(paths) if paths else ""


def emit(items, docs, depth, out):
    pad = "  " * depth
    for e in items:
        if isinstance(e, str):
            e = {title_of(docs, e): e} if is_page(e) else None
            if e is None:
                continue
        title, v = next(iter(e.items()))
        if is_page(v):
            if not v.startswith("http") and not (docs / v).exists():
                missing.append(v)
            used.add(v)
            out.append(f"{pad}* [{title}]({v})")
        elif isinstance(v, list):
            index = next((x for x in v if is_page(x) and x.endswith("index.md")), None)
            if index is None:  # une page enfant qui porte le nom de la section devient la page parente
                for x in v:
                    page = list(x.values())[0] if isinstance(x, dict) else x
                    if is_page(page) and slug(Path(page).stem) == slug(title):
                        index = x
                        break
            children = [x for x in v if x is not index]
            if isinstance(index, dict):
                index = list(index.values())[0]
            if index is None:  # section sans page : GitBook exige une page parente, unique
                base = f"{common_dir(v)}/{slug(title)}".lstrip("/")
                index, n = f"{base}.md", 2
                while index in used or (docs / index).exists():
                    index, n = f"{base}-{n}.md", n + 1
                if not (docs / index).exists():
                    stubs.append((index, title))
            used.add(index)
            out.append(f"{pad}* [{title}]({index})")
            emit(children, docs, depth + 1, out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mkdocs", type=Path, default=Path("mkdocs.yml"))
    ap.add_argument("--docs", type=Path, default=Path("docs"))
    ap.add_argument("--exclude-section", action="append", default=[])
    ap.add_argument("--create-stubs", action="store_true", help="créer les pages parentes manquantes")
    args = ap.parse_args()

    nav = yaml.load(args.mkdocs.read_text(encoding="utf-8"), Loader=Loader)["nav"]
    out = ["# Table of contents", ""]
    for entry in nav:
        if isinstance(entry, dict):
            title, v = next(iter(entry.items()))
            if title in args.exclude_section:
                continue
            if isinstance(v, list):
                out += ["", f"## {title}", ""]
                emit(v, args.docs, 0, out)
                continue
        emit([entry], args.docs, 0, out)

    (args.docs / "SUMMARY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{args.docs / 'SUMMARY.md'} : {sum(1 for l in out if l.lstrip().startswith('*'))} entrées")
    dup = [l for l in out if l.lstrip().startswith("*")]
    targets = [l.rsplit("(", 1)[1].rstrip(")") for l in dup]
    for t in sorted({t for t in targets if targets.count(t) > 1 and not t.startswith("http")}):
        print(f"  ! fichier référencé plusieurs fois (interdit dans GitBook) : {t}")
    if stubs and not args.create_stubs:
        print(f"  ! {len(stubs)} page(s) parente(s) à créer pour les sections sans page — relancer avec --create-stubs")
    for p in missing:
        print(f"  ! fichier de la nav introuvable : {p}")
    for p, t in stubs:
        if args.create_stubs:
            (args.docs / p).parent.mkdir(parents=True, exist_ok=True)
            (args.docs / p).write_text(f"# {t}\n", encoding="utf-8")
            print(f"  + page parente créée : {p}")



if __name__ == "__main__":
    main()
