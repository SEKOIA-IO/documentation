#!/usr/bin/env python3
"""
Vérifie que TOUTES les URL publiques actuelles répondent sur le nouveau site GitBook
(directement ou via une redirection). C'est le filet de sécurité final avant la bascule.

Sources d'URL : le sitemap du site actuel (+ les sources des redirections MkDocs).
Usage :
  python scripts/check_urls.py --sitemap https://docs.sekoia.com/sitemap.xml \\
      --new-base https://preview.example.gitbook.io/docs \\
      --extra migration/redirects_mkdocs.csv
Sortie : migration/url_check.csv (toutes les URL) ; liste des échecs à l'écran.
"""
import argparse
import csv
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse


def fetch(url, headers):
    req = urllib.request.Request(url, headers={"User-Agent": "doc-migration-check", **headers})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")


def check(path, base, headers):
    url = base.rstrip("/") + "/" + path.lstrip("/")
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "doc-migration-check", **headers})
        with urllib.request.urlopen(req, timeout=30) as r:
            return path, r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return path, e.code, ""
    except Exception as e:  # noqa: BLE001
        return path, 0, str(e)[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sitemap", required=True)
    ap.add_argument("--new-base", required=True)
    ap.add_argument("--extra", type=Path, help="CSV avec une colonne source (ex. redirects_mkdocs.csv)")
    ap.add_argument("--header", action="append", default=[], help="en-tête HTTP 'Nom: valeur' (accès privé)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    headers = dict(h.split(": ", 1) for h in args.header)

    paths = {urlparse(u).path for u in re.findall(r"<loc>([^<]+)</loc>", fetch(args.sitemap, {}))}
    if args.extra:
        with args.extra.open(encoding="utf-8") as f:
            paths |= {r["source"] for r in csv.DictReader(f)}
    paths = sorted(paths)
    print(f"{len(paths)} URL à vérifier sur {args.new_base}")

    with ThreadPoolExecutor(args.workers) as ex:
        results = list(ex.map(lambda p: check(p, args.new_base, headers), paths))

    Path("migration").mkdir(exist_ok=True)
    with open("migration/url_check.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ancienne_url", "statut", "url_finale"])
        w.writerows(results)
    ko = [r for r in results if r[1] != 200]
    print(f"{len(results) - len(ko)} OK, {len(ko)} en échec (détail dans migration/url_check.csv)")
    for p, s, final in ko[:50]:
        print(f"  {s}  {p}  {final}")


if __name__ == "__main__":
    main()
