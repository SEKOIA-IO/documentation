#!/usr/bin/env python3
"""
Table complète des redirections docs.sekoia.com (MkDocs) -> site GitBook, à importer dans
les redirections de site GitBook :

  1. chaque page publiée par MkDocs avant la migration (tag pre-migration), vers son
     emplacement actuel sur la branche GitBook (découpage en sections, renommages GitBook) ;
  2. les redirections déjà déclarées dans mkdocs.yml (plugin mkdocs-redirects), dont la
     destination est elle aussi ramenée à son emplacement actuel ;
  3. les pages supprimées ou dédoublonnées au découpage (migration/redirects_dedup.csv).

Sortie : migration/redirects.csv (source = chemin MkDocs, destination = URL GitBook).
Usage  : python scripts/export_redirects.py
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import section_links as SL  # noqa: E402
from build_summary import Loader  # noqa: E402

OUT = Path("migration/redirects.csv")


def mkdocs_url(docs_rel):
    p = re.sub(r"(^|/)index$", "", docs_rel[:-3])
    return "/" + (p + "/" if p else "")


def gitbook_url(current, site):
    """URL GitBook d'un fichier docs/<section>/... ; None si hors section."""
    return SL.url_of(current[len("docs/"):])


def main():
    site = SL.config()["site_url"].rstrip("/")
    rows, missing = {}, []

    # 1. Toutes les pages d'avant la migration
    before = subprocess.run(["git", "ls-tree", "-r", "--name-only", "pre-migration", "docs"],
                            capture_output=True, text=True, check=True).stdout.split()
    excluded = set()
    cfg_mk = yaml.load(SL.mkdocs_text(), Loader=Loader)
    for line in str(cfg_mk.get("exclude_docs") or "").splitlines():
        if line.strip():
            excluded.add("docs/" + line.strip())
    # Pages créées sur main depuis la préparation (reportées par la synchro)
    after = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main", "docs"],
                           capture_output=True, text=True).stdout.split()
    before += [f for f in after if f not in set(before)]
    # Pages servies par MkDocs à travers un lien symbolique (dossiers matérialisés)
    manifest = Path("migration/materialized.tsv")
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            dest_dir, src = line.split("\t")
            src_files = [Path(src)] if Path(src).is_file() else sorted(Path(src).rglob("*.md"))
            for sf in src_files:
                before.append(dest_dir + sf.as_posix()[len(src):])
    before = sorted(set(before))
    dropped_file = Path("migration/dropped_copies.txt")
    dropped = dropped_file.read_text(encoding="utf-8").split() if dropped_file.exists() else []
    for f in before:
        if not f.endswith(".md") or f in excluded or f.startswith("docs/integration/") \
                or f.startswith("docs/developer/"):
            continue
        if any(f == d or f.startswith(d + "/") for d in dropped):
            continue   # supprimée volontairement : redirection fournie par redirects_dedup.csv
        cur = SL.map_path(f)
        url = gitbook_url(cur, site) if Path(cur).exists() else None
        if url:
            rows[mkdocs_url(f[len("docs/"):])] = url
        else:
            missing.append(f)

    # 2. Redirections existantes de mkdocs.yml, destination ramenée à l'emplacement actuel
    maps = {}
    for p in cfg_mk.get("plugins", []):
        if isinstance(p, dict) and "redirects" in p:
            maps = p["redirects"].get("redirect_maps", {})
    for old, new in maps.items():
        if str(new).startswith("http"):
            rows[mkdocs_url(old)] = new
            continue
        url = gitbook_url(SL.map_path("docs/" + new), site)
        if url is None:  # destination hors de toute section connue
            url = f"{site}{mkdocs_url(new)}"
        rows[mkdocs_url(old)] = url

    # 3. Doublons et pages supprimées au découpage
    dedup = Path("migration/redirects_dedup.csv")
    if dedup.exists():
        with dedup.open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                rows[r["source"]] = r["destination"]

    # On retire les lignes qui ne changent rien (même chemin)
    rows = {s: d for s, d in rows.items() if d.rstrip("/") != f"{site}{s}".rstrip("/")}
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["source", "destination"])
        w.writerows(sorted(rows.items()))
    print(f"{OUT} : {len(rows)} redirection(s)")
    for m in missing:
        if mkdocs_url(m[len("docs/"):]) not in rows:
            print(f"  ! sans destination : {m}")


if __name__ == "__main__":
    main()
