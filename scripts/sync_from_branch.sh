#!/usr/bin/env bash
# Synchronise la branche GitBook avec une branche source, sans fusion Git :
# les modifications de la source sont converties PUIS appliquées (voir port_changes.py),
# en suivant les renommages faits dans GitBook.
#
# Usage :
#   scripts/sync_from_branch.sh main                         # doc en production (rédacteurs)
#   scripts/sync_from_branch.sh gitbook-migration-tooling    # équipe Intégrations
#   PUSH=1 scripts/sync_from_branch.sh main                  # pousse à la fin
# Variables : GB_BRANCH (défaut gitbook), DOCS_ROOT (défaut docs), EXCLUDE (défaut integration)
set -euo pipefail
SRC="${1:-main}"; GB="${GB_BRANCH:-gitbook}"; ROOT="${DOCS_ROOT:-docs}"
TAG="gitbook-last-sync"; SYNC_TAG="sync/$SRC"
EXARGS=(); for e in ${EXCLUDE-integration}; do EXARGS+=(--exclude "$e"); done

finish() {
  echo "== Rafraîchissement des contenus inclus depuis _shared_content"
  python3 scripts/convert_mkdocs.py "$ROOT" --since "$TAG" "${EXARGS[@]}" --inline-includes --write | grep -v '^ ' || true
  git add -A "$ROOT" && git commit -qm "Sync depuis $SRC : contenus inclus" || true

  echo "== Nouveaux fichiers absents de SUMMARY.md"
  git diff --name-only --diff-filter=A "$TAG" HEAD -- "$ROOT" | grep '\.md$' | grep -v "^$ROOT/integration/" \
    | while read -r f; do grep -qF "(${f#"$ROOT"/}" "$ROOT/SUMMARY.md" || echo "  ! ${f#"$ROOT"/}"; done || true

  git tag -f "$SYNC_TAG" "$(cat .git/port_source_ref)" >/dev/null
  git tag -f "$TAG" >/dev/null
  if [ "${PUSH:-0}" = "1" ]; then
    git push -q origin "$GB" && git push -q -f origin "$SYNC_TAG" "$TAG"; echo "Poussé."
  else
    echo "Vérifiez (git log -p origin/$GB..HEAD), puis : git push origin $GB && git push -f origin $SYNC_TAG $TAG"
  fi
}

# Après résolution manuelle des conflits : FINISH=1 scripts/sync_from_branch.sh <source>
if [ "${FINISH:-0}" = "1" ]; then
  git add -A "$ROOT" _shared_content && git commit -qm "Sync depuis $SRC (conflits résolus)" || true
  finish; exit 0
fi

git diff --quiet && git diff --cached --quiet || { echo "Modifications locales non commitées. Abandon."; exit 1; }
git fetch -q origin   # pas --force sur les tags : les tags locaux non poussés restent intacts
git checkout -q "$GB"
git pull -q --ff-only origin "$GB"     # commits faits par GitBook (renommages, éditions)

echo "== Report converti des modifications de origin/$SRC"
set +e
python3 scripts/port_changes.py --source "origin/$SRC" --docs "$ROOT" "${EXARGS[@]}" --write
status=$?
set -e
[ $status -eq 0 ] || [ $status -eq 2 ] || exit $status
[ -f .git/port_source_ref ] || exit 0

if [ $status -eq 2 ]; then
  echo
  echo "Conflits marqués <<<<<<< dans les fichiers « conflit » ci-dessus. Résolvez-les puis :"
  echo "  FINISH=1 scripts/sync_from_branch.sh $SRC"
  exit 2
fi
git add -A "$ROOT" _shared_content && git commit -qm "Sync depuis $SRC (converti)" || true
finish
