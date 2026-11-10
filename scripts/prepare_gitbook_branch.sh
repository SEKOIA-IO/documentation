#!/usr/bin/env bash
# Première conversion : à lancer UNE fois sur la branche qui sera connectée à GitBook.
# Chaque étape fait son propre commit, pour garder un historique lisible et réversible.
#
# Usage : scripts/prepare_gitbook_branch.sh
# Variables : DOCS_ROOT (défaut docs), EXCLUDE (défaut integration : périmètre de l'autre équipe)
set -euo pipefail
ROOT="${DOCS_ROOT:-docs}"
EXCLUDE="${EXCLUDE:-integration}"
HERE="$(cd "$(dirname "$0")" && pwd)"

git diff --quiet && git diff --cached --quiet || { echo "Arbre de travail non propre. Abandon."; exit 1; }
git tag -f pre-migration

echo "== 1/4 Remplacement des liens symboliques par de vrais fichiers (hors $EXCLUDE)"
bash "$HERE/materialize_symlinks.sh" "$ROOT" $EXCLUDE
git add -A "$ROOT" migration && git commit -qm "GitBook : remplacement des liens symboliques" || true
git tag -f gitbook-materialized

echo "== 2/4 Conversion de la syntaxe MkDocs (hors $EXCLUDE)"
EXARGS=(); for e in $EXCLUDE; do EXARGS+=(--exclude "$e"); done
python3 "$HERE/convert_mkdocs.py" "$ROOT" "${EXARGS[@]}" --inline-includes --write
git commit -qam "GitBook : conversion de la syntaxe MkDocs" || true

echo "== 3/4 Navigation (SUMMARY.md) depuis mkdocs.yml"
python3 "$HERE/build_summary.py" --docs "$ROOT" --exclude-section Integrations --create-stubs | grep -v '^  +' || true
python3 "$HERE/export_redirects.py"

echo "== 4/4 Configuration Git Sync"
cat > .gitbook.yaml << YAML
root: ./$ROOT/

structure:
  readme: index.md
  summary: SUMMARY.md
YAML
git add -A "$ROOT" .gitbook.yaml migration && git commit -qm "GitBook : SUMMARY.md, pages de section, .gitbook.yaml, export des redirections" || true

git tag -f gitbook-last-sync
git tag -f gitbook-baseline
git tag -f "sync/main" pre-migration
echo
echo "Terminé. Relisez (git log -p pre-migration..HEAD), puis poussez la branche et les tags :"
echo "  git push -u origin HEAD && git push -f origin pre-migration gitbook-materialized gitbook-baseline gitbook-last-sync sync/main"
