#!/usr/bin/env python3
"""
Après le découpage en sections, rend chaque espace complet et sans doublon :

1. Doublons issus de _shared_content : un même fichier source peut avoir été copié à
   plusieurs endroits (anciens liens symboliques). On garde la ou les copies présentes dans
   un SUMMARY.md, on supprime les autres et on note la redirection de leur ancienne URL
   publique vers la copie gardée (migration/redirects_dedup.csv).
2. Pages hors SUMMARY.md (publiques dans MkDocs même sans figurer dans la nav, invisibles
   dans GitBook) : rattachées comme sous-page de la page de la section qui renvoie vers elles.

Usage : python scripts/tidy_sections.py            # simulation
        python scripts/tidy_sections.py --write
"""
import argparse
import csv
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent))
import section_links as SL  # noqa: E402

DOCS = Path("docs")
LINK_RE = re.compile(r'\]\(<?([^)\s#>]+\.md)')


def summary_entries(sec_dir):
    s = DOCS / sec_dir / "SUMMARY.md"
    return set(re.findall(r"\]\(([^)]+\.md)\)", s.read_text(encoding="utf-8"))) if s.exists() else set()


def sources_of_copies():
    """Chemin actuel d'une copie -> (fichier source, chemin MkDocs d'origine)."""
    out = {}
    manifest = Path("migration/materialized.tsv")
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            dest_dir, src = line.split("\t")
            files = [Path(src)] if Path(src).is_file() else list(Path(src).rglob("*.md"))
            for f in files:
                rest = f.as_posix()[len(src):]
                original = dest_dir + rest
                out[SL.map_path(original)] = (f.as_posix(), original)
    # Liens symboliques encore présents (dossiers non matérialisés, ex. integration/)
    for link in subprocess.run(["find", str(DOCS), "-type", "l"], capture_output=True, text=True).stdout.split():
        target = Path(os.path.relpath(os.path.realpath(link)))
        files = [target] if target.is_file() else list(target.rglob("*.md"))
        for f in files:
            cur = link + f.as_posix()[len(target.as_posix()):]
            out[cur] = (f.as_posix(), cur)
    return out


def mkdocs_url(original):
    p = original[len("docs/"):-3]
    p = re.sub(r"(^|/)index$", "", p)
    return "/" + (p + "/" if p else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cfg = SL.config()
    site = cfg["site_url"].rstrip("/")
    listed = {s["dir"]: summary_entries(s["dir"]) for s in cfg["sections"]}
    skipped = {s["dir"] for s in cfg["sections"] if s.get("skip")}
    # Sections non touchées (sans SUMMARY.md ici) : on se fie à la nav de mkdocs.yml
    import yaml
    from build_summary import Loader
    nav_files = set()

    def walk(v):
        if isinstance(v, str):
            nav_files.add(v)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif isinstance(v, dict):
            for x in v.values():
                walk(x)
    walk(yaml.load(SL.mkdocs_text(), Loader=Loader)["nav"])

    def is_listed(path):
        sec = path.split("/")[1]
        if sec in skipped:
            return path[len("docs/"):] in nav_files
        return path.split("/", 2)[2] in listed.get(sec, set())

    # 1. Doublons
    replaced_by = {}
    copies = defaultdict(list)
    def under_symlink(path):
        return any(p.is_symlink() for p in [Path(path), *Path(path).parents])

    for cur, (src, original) in sources_of_copies().items():
        # Une copie sous lien symbolique n'existe pas pour GitBook : jamais gardée à la place d'un vrai fichier
        if Path(cur).exists() and not under_symlink(cur):
            copies[src].append((cur, original))
    removed, redirects, unlisted_home = [], [], []
    # Section « d'accueil » de chaque dossier source : celle où ses fichiers sont dans la nav
    home_votes = defaultdict(lambda: defaultdict(int))
    for src, cps in copies.items():
        for cur, _ in cps:
            if is_listed(cur):
                home_votes[os.path.dirname(src)][os.path.dirname(cur)] += 1
    for src, cps in copies.items():
        if len(cps) < 2:
            continue
        keep = [c for c in cps if is_listed(c[0])]
        if not keep:   # aucune copie dans la nav : on garde celle du dossier où vivent ses voisines
            votes = home_votes.get(os.path.dirname(src))
            if not votes:
                continue
            home = max(votes, key=votes.get)
            keep = [c for c in cps if os.path.dirname(c[0]) == home]
            if not keep:
                continue
            unlisted_home.append(keep[0][0])
        kept = keep[0][0]
        for cur, original in cps:
            if is_listed(cur) or Path(cur).is_symlink() or any(Path(cur).parents[i].is_symlink() for i in range(3)):
                continue
            removed.append(cur)
            replaced_by[cur] = kept
            redirects.append((mkdocs_url(original), SL.url_of(kept[len("docs/"):])))

    # 2. Pages orphelines : rattachées sous la page qui les cite
    attach, unplaced = defaultdict(list), []
    for s in cfg["sections"]:
        if s.get("skip"):
            continue
        root = DOCS / s["dir"]
        backlinks = defaultdict(list)
        for f in root.rglob("*.md"):
            rel_f = f.relative_to(root).as_posix()
            if rel_f not in listed[s["dir"]] or f.is_symlink():
                continue
            for m in LINK_RE.finditer(f.read_text(encoding="utf-8")):
                t = os.path.normpath(os.path.join(os.path.dirname(rel_f), unquote(m.group(1))))
                backlinks[t].append(rel_f)
        for f in sorted(root.rglob("*.md")):
            rel_f = f.relative_to(root).as_posix()
            if rel_f == "SUMMARY.md" or rel_f in listed[s["dir"]] or str(f) in removed:
                continue
            if any(p.is_symlink() for p in [f, *f.parents]):
                continue
            parents = backlinks.get(rel_f)
            if parents:
                attach[s["dir"]].append((sorted(parents, key=len)[0], rel_f))
            else:
                unplaced.append(str(f))

    # Décisions explicites (migration/sections.yaml > orphans), chemins MkDocs d'origine
    decisions = cfg.get("orphans") or {}
    to_delete, to_keep, dropped_dirs = {}, {}, set()
    for orig, target in (decisions.get("delete") or {}).items():
        if orig.endswith("/"):   # dossier entier -> page de même nom dans le dossier cible
            cur_dir = os.path.dirname(SL.map_path("docs/" + orig + "__probe__.md"))
            dropped_dirs.add("docs/" + orig.rstrip("/"))
            for f in sorted(Path(cur_dir).glob("*.md")) if Path(cur_dir).is_dir() else []:
                name = f.name
                dest = f"{target.rstrip('/')}/{name}" if target and not str(target).startswith("http") else target
                to_delete[f.as_posix()] = (orig + name, dest)
                replaced_by[f.as_posix()] = "docs/" + dest if dest and not str(dest).startswith("http") else None
            continue
        cur = SL.map_path("docs/" + orig)
        if Path(cur).exists():
            to_delete[cur] = (orig, target)
    keep_under = {}   # dossier entier rattaché sous une page : {dossier actuel: page parente actuelle}
    for orig, opts in (decisions.get("keep") or {}).items():
        opts = opts or {}
        if orig.endswith("/"):
            cur_dir = os.path.dirname(SL.map_path("docs/" + orig + "__probe__.md"))
            if cur_dir and Path(cur_dir).is_dir() and opts.get("under"):
                keep_under[cur_dir] = SL.map_path("docs/" + opts["under"])
            continue
        cur = SL.map_path("docs/" + orig)
        after = SL.map_path("docs/" + opts["after"]) if opts.get("after") else None
        if Path(cur).exists():
            to_keep[cur] = after
    in_kept_dir = lambda u: any(u.startswith(d + "/") for d in keep_under)  # noqa: E731
    unplaced = [u for u in unplaced if u not in to_delete and u not in to_keep and not in_kept_dir(u)]
    for sec_dir_, sec_items in attach.items():
        sec_items[:] = [(p, pg) for p, pg in sec_items
                        if not any(k.endswith("/" + pg) for k in list(to_delete) + list(to_keep))
                        and not in_kept_dir(f"docs/{sec_dir_}/{pg}")]

    print(f"{len(removed)} doublon(s) à supprimer (copies hors navigation), avec redirection")
    for r in removed[:5]:
        print(f"  - {r}")
    if len(removed) > 5:
        print(f"  ... et {len(removed) - 5} autres")
    if unlisted_home:
        print(f"  ! {len(unlisted_home)} copie(s) gardée(s) mais absente(s) de toute nav (à signaler à la section concernée) :")
        for u in unlisted_home[:5]:
            print(f"      {u}")
    print(f"{sum(len(v) for v in attach.values())} page(s) hors SUMMARY rattachées sous la page qui les cite")
    for sec, items in attach.items():
        for parent, page in items:
            print(f"  + {sec}/{page}  (sous {parent})")
    for cur, (orig, target) in to_delete.items():
        print(f"  x {cur} : supprimée (décision), redirection -> {target}")
    for cur, after in to_keep.items():
        print(f"  + {cur} : gardée (décision), placée après {after}")
    for d, parent in keep_under.items():
        n = len(list(Path(d).glob("*.md")))
        print(f"  + {d}/ : {n} page(s) gardées (décision), rattachées sous {parent}")
    for u in unplaced:
        print(f"  ! {u} : citée par aucune page de la section, à placer à la main ou supprimer")
    if not args.write:
        print("Simulation terminée. Relancez avec --write pour appliquer.")
        return

    for cur, (orig, target) in to_delete.items():
        if target:
            if not str(target).startswith("http"):
                target = SL.url_of(SL.map_path("docs/" + target)[len("docs/"):]) or target
            redirects.append((mkdocs_url("docs/" + orig), target))
        removed.append(cur)
    for cur, after in to_keep.items():
        sec_dir = cur.split("/")[1]
        sp = DOCS / sec_dir / "SUMMARY.md"
        rel = cur.split("/", 2)[2]
        lines = sp.read_text(encoding="utf-8").split("\n")
        if any(f"]({rel})" in l for l in lines):
            continue
        k = next((i for i, l in enumerate(lines) if after and f"]({after.split('/', 2)[2]})" in l), None)
        if k is None:
            print(f"  ! {cur} : page « after » introuvable dans {sp}, à placer à la main")
            continue
        indent = len(lines[k]) - len(lines[k].lstrip())
        title = next((l[2:].strip() for l in Path(cur).read_text(encoding="utf-8").splitlines()
                      if l.startswith("# ")), Path(cur).stem)
        lines.insert(k + 1, " " * indent + f"* [{title}]({rel})")
        sp.write_text("\n".join(lines), encoding="utf-8")
    for d, parent in keep_under.items():
        sec_dir = d.split("/")[1]
        sp = DOCS / sec_dir / "SUMMARY.md"
        lines = sp.read_text(encoding="utf-8").split("\n")
        k = next((i for i, l in enumerate(lines) if f"]({parent.split('/', 2)[2]})" in l), None)
        if k is None:
            print(f"  ! {d}/ : page parente {parent} introuvable dans {sp}")
            continue
        indent = len(lines[k]) - len(lines[k].lstrip()) + 2
        pos = k + 1
        while pos < len(lines) and lines[pos].strip() and len(lines[pos]) - len(lines[pos].lstrip()) >= indent:
            pos += 1
        entries = []
        for f in sorted(Path(d).glob("*.md"), key=lambda f: f.name.lower()):
            rel = f.as_posix().split("/", 2)[2]
            if any(f"]({rel})" in l for l in lines):
                continue
            title = next((l[2:].strip() for l in f.read_text(encoding="utf-8").splitlines()
                          if l.startswith("# ")), f.stem)
            entries.append(" " * indent + f"* [{title}]({rel})")
        lines[pos:pos] = entries
        sp.write_text("\n".join(lines), encoding="utf-8")
    for r in removed:
        subprocess.run(["git", "rm", "-q", "-f", r], check=True)
    # Dossiers d'origine dont la copie a été supprimée : la synchro ne doit pas les recréer
    if removed:
        dropped = Path("migration/dropped_copies.txt")
        old = set(dropped.read_text(encoding="utf-8").split()) if dropped.exists() else set()
        originals = {os.path.dirname(o) for src, cps in copies.items() for cur, o in cps if cur in removed}
        originals |= {"docs/" + orig for orig, _ in to_delete.values()} | dropped_dirs
        dropped.write_text("\n".join(sorted(old | originals)) + "\n", encoding="utf-8")
    # Liens qui visaient une copie supprimée -> copie gardée (URL absolue si autre section)
    fixed = 0
    rel_removed = {k[len("docs/"):]: v[len("docs/"):] for k, v in replaced_by.items() if v}
    for f in DOCS.glob("*/**/*.md"):
        if f.is_symlink() or any(p.is_symlink() for p in f.parents):
            continue
        rel_f = f.relative_to(DOCS).as_posix()
        text = f.read_text(encoding="utf-8")

        def fix(m):
            nonlocal fixed
            t = os.path.normpath(os.path.join(os.path.dirname(rel_f), unquote(m.group(2))))
            if t not in rel_removed:
                return m.group(0)
            fixed += 1
            return m.group(1) + SL.link_for(rel_removed[t], rel_f, DOCS) + m.group(3)
        new = re.sub(r'(\]\(<?)([^)\s#>:]+\.md)((?:#[^)\s>]*)?>?\))', fix, text)
        if new != text:
            f.write_text(new, encoding="utf-8")
    print(f"{fixed} lien(s) redirigé(s) vers la copie gardée")
    if redirects:
        out = Path("migration/redirects_dedup.csv")
        with out.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["source", "destination"])
            w.writerows(sorted(set(redirects)))
        print(f"{out} : {len(set(redirects))} redirection(s)")
    for sec, items in attach.items():
        sp = DOCS / sec / "SUMMARY.md"
        lines = sp.read_text(encoding="utf-8").split("\n")
        for parent, page in items:
            k = next((i for i, l in enumerate(lines) if f"]({parent})" in l), None)
            if k is None:
                continue
            indent = len(lines[k]) - len(lines[k].lstrip()) + 2
            title = next((l[2:].strip() for l in (DOCS / sec / page).read_text(encoding="utf-8").splitlines()
                          if l.startswith("# ")), Path(page).stem.replace("_", " ").capitalize())
            pos = k + 1   # après les enfants déjà présents : l'ordre est conservé
            while pos < len(lines) and lines[pos].strip() and len(lines[pos]) - len(lines[pos].lstrip()) >= indent:
                pos += 1
            lines.insert(pos, " " * indent + f"* [{title}]({page})")
        sp.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
