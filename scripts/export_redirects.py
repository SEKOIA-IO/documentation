#!/usr/bin/env python3
"""
Reprend les redirections existantes du plugin mkdocs-redirects (mkdocs.yml) et
les exporte pour GitBook, en appliquant les renommages de dossiers prévus.

Sorties :
  migration/redirects_mkdocs.csv     source,destination (chemins d'URL, pour les redirections de site)
  migration/gitbook_redirects.yaml   bloc `redirects:` au format .gitbook.yaml

Usage :
  python scripts/export_redirects.py --mkdocs mkdocs.yml --rename xdr=defend
"""
import argparse
import csv
from pathlib import Path

import yaml


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("", lambda loader, suffix, node: None)


def url_path(md):
    p = md[:-3] if md.endswith(".md") else md
    if p == "index" or p.endswith("/index"):
        p = p[: -len("index")]
    return p.strip("/")


def apply_renames(path, renames):
    for old, new in renames:
        if path == old or path.startswith(old + "/"):
            return new + path[len(old):]
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mkdocs", type=Path, default=Path("mkdocs.yml"))
    ap.add_argument("--rename", action="append", default=[], help="ancien=nouveau (ex. xdr=defend)")
    ap.add_argument("--out", type=Path, default=Path("migration"))
    args = ap.parse_args()
    renames = [tuple(r.split("=", 1)) for r in args.rename]

    cfg = yaml.load(args.mkdocs.read_text(encoding="utf-8"), Loader=Loader)
    maps = {}
    for p in cfg.get("plugins", []):
        if isinstance(p, dict) and "redirects" in p:
            maps = p["redirects"].get("redirect_maps", {})

    args.out.mkdir(exist_ok=True)
    rows = []
    for old, new in maps.items():
        if str(new).startswith("http"):
            rows.append((url_path(old), new, new))
            continue
        new_file = apply_renames(new, renames)
        rows.append((url_path(old), apply_renames(url_path(new), renames), new_file))

    with (args.out / "redirects_mkdocs.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "destination"])
        for src, dst, _ in rows:
            w.writerow([f"/{src}", dst if dst.startswith("http") else f"/{dst}"])
    with (args.out / "gitbook_redirects.yaml").open("w", encoding="utf-8") as f:
        f.write("redirects:\n")
        for src, _, dst_file in rows:
            if not dst_file.startswith("http"):
                f.write(f"  {src}: {dst_file}\n")
    print(f"{len(rows)} redirection(s) exportées dans {args.out}/")


if __name__ == "__main__":
    main()
