"""
Règles de liens communes après le découpage en sections (un dossier = un espace GitBook) :
  - image de docs/assets/ -> copie dans <section>/assets/, lien relatif ;
  - page de la même section -> lien relatif ;
  - page d'une autre section -> URL absolue du site (un espace ne voit pas les autres) ;
  - ancien chemin (avant découpage ou renommage GitBook) -> suivi via l'historique Git.
"""
import os
import re
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path

import yaml

CONFIG = Path("migration/sections.yaml")
BASELINE = "gitbook-baseline"


@lru_cache(maxsize=1)
def mkdocs_text():
    """mkdocs.yml de origin/main (nav à jour) ; à défaut, celui de la branche courante."""
    r = subprocess.run(["git", "show", "origin/main:mkdocs.yml"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 and r.stdout else Path("mkdocs.yml").read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def config():
    if not CONFIG.exists():
        return None
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8"))


def section_of(docs_rel):
    cfg = config()
    if not cfg:
        return None
    top = docs_rel.split("/", 1)[0]
    return next((s for s in cfg["sections"] if s["dir"] == top), None)


def is_stub(path):
    """Page de groupe générée (« # Titre » seul) : Git les apparie au hasard, on les ignore."""
    if not str(path).endswith(".md"):
        return False
    try:
        body = Path(path).read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError):
        return False
    return body.startswith("# ") and "\n" not in body


@lru_cache(maxsize=1)
def rename_map():
    files = {}
    # --cached : compare à l'index, donc inclut aussi les déplacements pas encore commités
    r = subprocess.run(["git", "-c", "diff.renameLimit=0", "diff", "-M", "--cached", "--name-status", BASELINE],
                       capture_output=True, text=True)
    for line in r.stdout.splitlines():
        p = line.split("\t")
        if p[0].startswith("R") and not is_stub(p[2]):
            files[p[1]] = p[2]
    return files, {}


@lru_cache(maxsize=1)
def _present():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
    targets = set(rename_map()[0].values())
    return [f for f in out if f not in targets]


@lru_cache(maxsize=None)
def _dir_destination(d):
    """Où sont partis les fichiers du dossier d ? Vote des fichiers déplacés et restés en place."""
    files, _ = rename_map()
    votes = {}
    for old, new in files.items():
        if old.startswith(d + "/"):
            rest = old[len(d):]
            if new.endswith(rest):
                votes[new[: -len(rest)]] = votes.get(new[: -len(rest)], 0) + 1
    stayed = sum(1 for f in _present() if f.startswith(d + "/"))
    if stayed:
        votes[d] = votes.get(d, 0) + stayed
    return max(votes, key=votes.get) if votes else None


def map_path(path):
    files, _ = rename_map()
    if path in files:
        return files[path]
    d = os.path.dirname(path)
    while d:
        dest = _dir_destination(d)
        if dest is not None:
            return dest + path[len(d):]
        d = os.path.dirname(d)
    return path


def link_for(target_rel, from_rel, docs_root, copy_from=None):
    """target_rel, from_rel : chemins relatifs à docs/ (emplacements actuels)."""
    here = section_of(from_rel)
    if here and target_rel.startswith("assets/"):
        dest = f"{here['dir']}/{target_rel}"
        if not (docs_root / dest).exists():
            for src_root in (copy_from, docs_root):
                if src_root and (src_root / target_rel).exists():
                    (docs_root / dest).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_root / target_rel, docs_root / dest)
                    break
        target_rel = dest
    there = section_of(target_rel)
    if here and there and there is not here and target_rel.endswith(".md"):
        inner = re.sub(r"(^|/)(README|index)$", "", target_rel.split("/", 1)[1][:-3])
        return f"{config()['site_url'].rstrip('/')}/{there['url']}/{inner}".rstrip("/")
    return os.path.relpath(target_rel, os.path.dirname(from_rel)).replace(os.sep, "/")
