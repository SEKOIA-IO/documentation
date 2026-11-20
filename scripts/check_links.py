#!/usr/bin/env python3
"""
Vérifie que chaque espace (docs/<section>/) est autonome : tout lien relatif et toute image
doivent pointer vers un fichier existant DANS la même section. Signale aussi les références
restantes à _shared_content et les pages présentes dans le dossier mais absentes du SUMMARY.md.

Usage : python scripts/check_links.py [--section getting-started]
"""
import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent))
import section_links as SL  # noqa: E402

LINK_RE = re.compile(r'(?:\]\(<([^>#]+)[^>]*>|\]\(|src=")([^)"\s#?<]*)')
MARK_RE = re.compile(r'<!-- (?:end)?include:[^>]*-->')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", action="append")
    args = ap.parse_args()
    cfg = SL.config()
    total = 0
    for s in cfg["sections"]:
        if (args.section and s["dir"] not in args.section) or s.get("skip"):
            continue
        root = Path("docs") / s["dir"]
        summary = (root / "SUMMARY.md").read_text(encoding="utf-8") if (root / "SUMMARY.md").exists() else ""
        broken, outside, shared, unlisted = [], [], [], []
        for f in sorted(root.rglob("*.md")):
            rel_f = f.relative_to(root).as_posix()
            if rel_f == "SUMMARY.md":
                continue
            if f"]({rel_f})" not in summary:
                unlisted.append(rel_f)
            text = MARK_RE.sub("", f.read_text(encoding="utf-8"))
            if "_shared_content" in text:
                shared.append(rel_f)
            for m in LINK_RE.finditer(text):
                t = unquote(m.group(1) or m.group(2))
                if not t:
                    continue
                if re.match(r"^[a-z]+:", t) or t.startswith(("/", "#")):
                    continue
                target = Path(os.path.normpath(f.parent / t))
                if not target.is_relative_to(root.absolute()) and not target.is_relative_to(root):
                    outside.append(f"{rel_f} -> {t}")
                elif not target.exists():
                    broken.append(f"{rel_f} -> {t}")
        n = len(broken) + len(outside) + len(shared)
        total += n
        print(f"{s['dir']:26} liens cassés {len(broken):4} | hors section {len(outside):4} | "
              f"mention _shared_content {len(shared):3} | pages hors SUMMARY {len(unlisted):3}")
        for x in (broken + outside)[:5]:
            print(f"    ! {x}")
        for x in shared[:3]:
            print(f"    ! _shared_content : {x}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
