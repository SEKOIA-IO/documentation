#!/usr/bin/env python3
"""
Réorganise la branche GitBook en un dossier autonome par onglet (= un espace GitBook =
une section du site), d'après les sections de premier niveau de la nav de mkdocs.yml.

Pour chaque section, dans docs/<dossier>/ :
  - les pages de la section (git mv, donc renommages suivis par la synchro) ;
  - SUMMARY.md : sous-sections de premier niveau en groupes (## ...), le reste imbriqué ;
  - .gitbook.yaml (page d'accueil = première page de la section) ;
  - assets/ : copie des seules images utilisées par la section ;
  - liens réécrits : relatifs dans la section, absolus (URL du site) vers les autres sections.

Étape 1 : python scripts/split_sections.py --init    -> écrit migration/sections.yaml (à relire)
Étape 2 : python scripts/split_sections.py           -> simulation
Étape 3 : python scripts/split_sections.py --write   -> applique (un commit à faire ensuite)
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent))
from build_summary import Loader, slug, title_of  # noqa: E402

CONFIG = Path("migration/sections.yaml")
DOCS = Path("docs")
LINK_RE = re.compile(r'(\]\(|src=")([^<)"\s#?][^)"\s#?]*)((?:#[^)"\s]*)?)(\)|")')
ANGLE_RE = re.compile(r'(\]\(<)([^>#]+)((?:#[^>]*)?)(>)')   # ](<chemin avec espaces>)


def nav_pages(v, acc):
    if isinstance(v, str):
        if v.endswith(".md"):
            acc.append(v)
    elif isinstance(v, list):
        for e in v:
            nav_pages(e, acc)
    elif isinstance(v, dict):
        for x in v.values():
            nav_pages(x, acc)
    return acc


def load_nav():
    import section_links as SL
    return yaml.load(SL.mkdocs_text(), Loader=Loader)["nav"]


def common_prefix(paths):
    dirs = [p.split("/")[:-1] for p in paths]
    pre = []
    for parts in zip(*dirs):
        if len(set(parts)) != 1:
            break
        pre.append(parts[0])
    return "/".join(pre)


def init():
    sections, nav = [], load_nav()
    all_pages = {next(iter(e))[0] if False else next(iter(e.keys())): nav_pages(next(iter(e.values())), [])
                 for e in nav}
    for title, pages in all_pages.items():
        pre = common_prefix(pages)
        others = [p for t, ps in all_pages.items() if t != title for p in ps]
        # Un dossier existant qui contient toute la section, et rien d'autre, n'est pas déplacé
        exclusive = pre and "/" not in pre and not any(p.startswith(pre + "/") for p in others)
        folder = pre if exclusive else slug(title)
        sections.append({"title": title, "dir": folder, "url": slug(title)})
    CONFIG.parent.mkdir(exist_ok=True)
    CONFIG.write_text(
        "# Une entrée par onglet GitBook. title = titre de premier niveau dans la nav de mkdocs.yml\n"
        "# dir = dossier sous docs/ (= Project directory de l'espace : ./docs/<dir>)\n"
        "# url = chemin de la section sur le site GitBook (sert aux liens entre sections)\n"
        + yaml.safe_dump({"site_url": "https://docs.sekoia.com", "sections": sections},
                         allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"{CONFIG} écrit : relisez dir et url, puis relancez sans --init")


def emit(items, depth, out, mp):
    """Comme build_summary.emit, avec les chemins convertis par mp (ancien -> relatif section)."""
    from build_summary import is_page, used, stubs  # noqa: F401
    pad = "  " * depth
    for e in items:
        if isinstance(e, str):
            if not e.endswith(".md"):
                continue
            e = {title_of(DOCS, e): e}
        title, v = next(iter(e.items()))
        if isinstance(v, str):
            if v.startswith("http"):
                out.append(f"{pad}* [{title}]({v})")
            elif v in mp and mp[v] not in used:
                used.add(mp[v])
                out.append(f"{pad}* [{title}]({mp[v]})")
        elif isinstance(v, list):
            idx = next((x for x in v if isinstance(x, str) and x.endswith("index.md")), None)
            if idx is None:
                for x in v:
                    page = list(x.values())[0] if isinstance(x, dict) else x
                    if isinstance(page, str) and page.endswith(".md") and slug(Path(page).stem) == slug(title):
                        idx = x
                        break
            children = [x for x in v if x is not idx]
            idx_path = list(idx.values())[0] if isinstance(idx, dict) else idx
            if idx_path and idx_path in mp:
                target = mp[idx_path]
            else:
                first = next((mp[p] for p in nav_pages(children, []) if p in mp), "")
                folder = os.path.dirname(first)
                base = f"{folder}/{slug(title)}".lstrip("/")
                target, n = f"{base}.md", 2
                while target in used or target in mp.values():
                    target, n = f"{base}-{n}.md", n + 1
                stubs.append((target, title))
            used.add(target)
            out.append(f"{pad}* [{title}]({target})")
            emit(children, depth + 1, out, mp)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--no-rewrite", action="append", default=["integration"],
                    help="dossier de section dont les pages ne sont pas modifiées (défaut : integration)")
    args = ap.parse_args()
    if args.init:
        return init()

    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    site = cfg["site_url"].rstrip("/")
    by_title = {s["title"]: s for s in cfg["sections"]}
    nav = load_nav()

    # 1. Page -> section et sous-section de nav (première apparition dans la nav)
    section_of, navpath = {}, {}

    def walk(items, stack, title):
        for e in items:
            if isinstance(e, str):
                if e.endswith(".md"):
                    section_of.setdefault(e, title)
                    navpath.setdefault(e, tuple(stack))
                continue
            t, v = next(iter(e.items()))
            if isinstance(v, list):
                walk(v, stack + [t], title)
            elif isinstance(v, str) and v.endswith(".md"):
                section_of.setdefault(v, title)
                navpath.setdefault(v, tuple(stack))

    for e in nav:
        title, v = next(iter(e.items()))
        if title in by_title:
            walk(v if isinstance(v, list) else [v], [], title)

    tracked = subprocess.run(["git", "ls-files", str(DOCS)], capture_output=True, text=True).stdout.split()
    tracked_rel = [f[len("docs/"):] for f in tracked]
    orphans, old_stubs = [], []
    nav_set = set(section_of)
    for rel in tracked_rel:
        if rel.endswith(".md") and rel not in nav_set and (DOCS / rel).exists():
            body = (DOCS / rel).read_text(encoding="utf-8").strip()
            if body.startswith("# ") and "\n" not in body:   # page de section vide d'un ancien SUMMARY
                old_stubs.append(rel)

    # 2. Chemin cible : dossier = sous-section de nav la plus précise déclarée dans `folders`,
    #    tout ce qui est plus profond est mis à plat dans ce dossier.
    taken, new_of = set(), {}

    def place(folder_path, old):
        name = os.path.basename(old)
        cand = f"{folder_path}/{name}".replace("//", "/")
        if cand in taken:
            parent = os.path.basename(os.path.dirname(old)) or "page"
            cand = f"{folder_path}/{parent}-{name}".replace("//", "/")
        n = 2
        base = cand[:-3] if cand.endswith(".md") else cand
        while cand in taken:
            cand, n = f"{base}-{n}{Path(old).suffix}", n + 1
        taken.add(cand)
        return cand

    def keeps_paths(s):
        return s.get("keep_paths") or s.get("skip") or "folders" not in s

    folder_votes = defaultdict(Counter)
    for old, t in section_of.items():
        s = by_title[t]
        if keeps_paths(s):
            new_of[old] = old if old.startswith(s["dir"] + "/") else f"{s['dir']}/{old}"
            taken.add(new_of[old])
            continue
        stack, folder, depth = navpath[old], "", 0
        for k in range(len(stack), 0, -1):
            key = " > ".join(stack[:k])
            if key in s["folders"]:
                folder, depth = s["folders"][key], k
                break
        target_dir = f"{s['dir']}/{folder}".rstrip("/")
        if os.path.basename(old) in ("index.md", "README.md") and len(stack) > depth:
            # page d'accueil d'une sous-section mise à plat : nommée d'après son ancien dossier
            new_of[old] = place(target_dir, os.path.dirname(old) + ".md")
        else:
            new_of[old] = place(target_dir, old)
        folder_votes[os.path.dirname(old)][(t, target_dir)] += 1

    # Fichiers hors nav (images locales, pages orphelines) : dossier majoritaire de leurs voisins
    for rel in tracked_rel:
        if rel in new_of or rel in old_stubs or rel.startswith("assets/") or "/" not in rel:
            continue
        top = rel.split("/", 1)[0]
        keep = next((s for s in by_title.values() if keeps_paths(s) and s["dir"] == top), None)
        if keep:
            section_of[rel], new_of[rel] = keep["title"], rel
            continue
        d = os.path.dirname(rel)
        while d and d not in folder_votes:
            d = os.path.dirname(d)
        if d:
            (t, target_dir), _ = folder_votes[d].most_common(1)[0]
            sub = os.path.dirname(rel)[len(d):].strip("/")   # ex. library/ sous automate/
            section_of[rel], new_of[rel] = t, place(f"{target_dir}/{sub}".rstrip("/"), rel)
        elif rel.endswith(".md"):
            orphans.append(rel)

    moves = {o: n for o, n in new_of.items() if o != n and (DOCS / o).exists()}
    old_of = {n: o for o, n in new_of.items()}

    print(f"{len(old_stubs)} anciennes pages de section vides supprimées (régénérées par section)")
    print(f"{len(section_of)} fichiers répartis en {len(by_title)} sections, {len(moves)} déplacements")
    for t, sec in by_title.items():
        n = sum(1 for p in section_of.values() if p == t)
        mode = " (ignorée : aucun fichier modifié)" if sec.get("skip") else ""
        print(f"  {sec['dir']:26} {n:5} fichiers   <- « {t} »{mode}")
    for o in orphans:
        print(f"  ! page hors nav et hors dossier connu, laissée en place : docs/{o}")
    if not args.write:
        print("Simulation terminée. Relancez avec --write pour appliquer.")
        return

    for rel in old_stubs:
        subprocess.run(["git", "rm", "-q", "-f", str(DOCS / rel)], check=True)

    # 2. Déplacements (git mv : la synchro suit ces renommages)
    for o, n in sorted(moves.items()):
        (DOCS / n).parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", "-k", str(DOCS / o), str(DOCS / n)], check=True)

    # 3. Liens et images
    sec_dir = {t: s["dir"] for t, s in by_title.items()}
    dir_sec = {v: k for k, v in sec_dir.items()}
    copied, cross = 0, 0
    for new, old in old_of.items():
        f = DOCS / new
        if not f.suffix == ".md" or not f.exists():
            continue
        here_sec = sec_dir[section_of[old]]
        if here_sec in args.no_rewrite or by_title[section_of[old]].get("skip"):
            continue
        text = f.read_text(encoding="utf-8")

        def fix(m):
            nonlocal copied, cross
            target = unquote(m.group(2))
            if re.match(r"^[a-z]+:", target) or target.startswith(("/", "#")):
                return m.group(0)
            tgt_old = os.path.normpath(os.path.join(os.path.dirname(old), target))
            if tgt_old.startswith("assets/"):
                dest = f"{here_sec}/{tgt_old}"
                if not (DOCS / dest).exists() and (DOCS / tgt_old).exists():
                    (DOCS / dest).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(DOCS / tgt_old, DOCS / dest)
                    copied += 1
                new_t = dest
            elif tgt_old in new_of:
                new_t = new_of[tgt_old]
            elif (DOCS / tgt_old).exists():      # fichier resté en place (hors nav, autre section)
                new_t = tgt_old
            else:
                return m.group(0)
            if new_t.split("/")[0] != here_sec and new_t.endswith(".md"):
                cross += 1
                import section_links as SL
                url = SL.url_of(new_t)
                return f"{m.group(1)}{url}{m.group(3)}{m.group(4)}"
            rel = os.path.relpath(new_t, os.path.dirname(new))
            return f"{m.group(1)}{rel}{m.group(3)}{m.group(4)}"
        new_text = ANGLE_RE.sub(fix, LINK_RE.sub(fix, text))
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")

    # 4. SUMMARY.md, .gitbook.yaml et pages de groupe par section
    import build_summary as bs
    for sec in cfg["sections"]:       # sections nouvelles, sans contenu dans la nav MkDocs
        if sec.get("new"):
            d = DOCS / sec["dir"]
            d.mkdir(parents=True, exist_ok=True)
            if not (d / "README.md").exists():
                (d / "README.md").write_text(f"# {sec['title']}\n", encoding="utf-8")
            (d / "SUMMARY.md").write_text(f"# Table of contents\n\n* [{sec['title']}](README.md)\n", encoding="utf-8")
            (d / ".gitbook.yaml").write_text("root: ./\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n",
                                             encoding="utf-8")
            print(f"  docs/{sec['dir']}/ : nouvelle section vide créée")
    for e in nav:
        title, v = next(iter(e.items()))
        if title not in by_title or by_title[title].get("skip"):
            continue
        d = sec_dir[title]
        mp = {o: n[len(d) + 1:] for o, n in new_of.items() if n.startswith(d + "/")}
        bs.used, bs.stubs = set(), []
        out = ["# Table of contents", ""]
        first = None
        for item in v if isinstance(v, list) else [v]:
            if isinstance(item, dict) and isinstance(next(iter(item.values())), list):
                sub_title, sub = next(iter(item.items()))
                out += ["", f"## {sub_title}", ""]
                emit(sub, 0, out, mp)
            else:
                emit([item], 0, out, mp)
        for line in out:
            m = re.search(r"\]\(([^)]+\.md)\)", line)
            if m:
                first = first or m.group(1)
        for p, t in bs.stubs:
            (DOCS / d / p).parent.mkdir(parents=True, exist_ok=True)
            if not (DOCS / d / p).exists():
                (DOCS / d / p).write_text(f"# {t}\n", encoding="utf-8")
        (DOCS / d / "SUMMARY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
        (DOCS / d / ".gitbook.yaml").write_text(
            f"root: ./\n\nstructure:\n  readme: {first}\n  summary: SUMMARY.md\n", encoding="utf-8")
        print(f"  docs/{d}/SUMMARY.md : {sum(1 for l in out if l.lstrip().startswith('*'))} entrées, accueil = {first}")

    for stale in (DOCS / "SUMMARY.md", Path(".gitbook.yaml")):
        if stale.exists():
            subprocess.run(["git", "rm", "-q", str(stale)], check=False)
    subprocess.run(["find", str(DOCS), "-type", "d", "-empty", "-delete"], check=False)
    print(f"{copied} images copiées dans les sections, {cross} liens entre sections passés en URL absolue")
    here = Path(__file__).parent
    subprocess.run(["git", "add", "-A", "docs", "migration"], check=True)
    subprocess.run(["find", str(DOCS), "-type", "d", "-empty", "-delete"], check=False)
    print("\n== Doublons et pages hors SUMMARY")
    subprocess.run([sys.executable, str(here / "tidy_sections.py"), "--write"], check=True)
    print("\n== Repasse de conversion (règles de liens par section)")
    excl = sum((["--exclude", d] for d in args.no_rewrite), [])
    subprocess.run([sys.executable, str(here / "convert_mkdocs.py"), "docs", *excl, "--write"], check=True)
    print("\n== Table des redirections MkDocs -> GitBook")
    subprocess.run([sys.executable, str(here / "export_redirects.py")], check=False)
    print("\n== Contrôle d'autonomie des sections")
    subprocess.run([sys.executable, str(here / "check_links.py")], check=False)
    print("\nRelisez puis : git add -A docs migration && git commit -m 'Découpage en sections GitBook'")


if __name__ == "__main__":
    main()
