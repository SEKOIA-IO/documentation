#!/usr/bin/env bash
# GitBook ne suit pas les liens symboliques : on les remplace par de vraies copies.
# Chaque copie est notée dans migration/materialized.tsv (copie -> source) pour que
# sync_from_branch.sh puisse y reporter les modifications faites ensuite sur main.
# Usage : scripts/materialize_symlinks.sh docs [dossier_exclu ...]
set -euo pipefail
ROOT="${1:-docs}"; shift || true
TOP="$(git rev-parse --show-toplevel)"
mkdir -p migration
find "$ROOT" -type l | sort | while read -r link; do
  for ex in "$@"; do [[ "$link" == "$ROOT/$ex/"* ]] && continue 2; done
  target="$(readlink -f "$link")"
  echo "copie : $link  <-  $target"
  rm "$link"
  printf '%s\t%s\n' "$link" "${target#"$TOP"/}" >> migration/materialized.tsv
  cp -RL "$target" "$link"   # -L : suit aussi les liens symboliques imbriqués
done
