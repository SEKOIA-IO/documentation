# Migration docs.sekoia.com : MkDocs Material -> GitBook

## Contexte

- Source actuelle : MkDocs Material (`mkdocs.yml`, nav, plugin mkdocs-redirects, inclusions
  `{!_shared_content/...!}`, liens symboliques vers `_shared_content`).
- `main` continue d'alimenter le site MkDocs en production jusqu'à la bascule.
- L'équipe Intégrations travaille sur `gitbook-migration-tooling`, périmètre `docs/integration/`.
  Ne JAMAIS modifier `docs/integration/` ni `_shared_content/integration/` sans me le demander.
- Branche `gitbook` : connectée à GitBook via Git Sync. La structure (renommages, ordre des pages,
  SUMMARY.md) se pilote DEPUIS GITBOOK. Exemple prévu : `xdr` renommé en `defend`.

## Règles impératives

- Toujours `git pull` la branche `gitbook` avant d'agir : GitBook y pousse ses propres commits.
- Ne jamais déplacer ni renommer de fichier en local sur `gitbook` : on le fait dans GitBook.
- Ne jamais convertir la syntaxe à la main : `scripts/convert_mkdocs.py`.
- Ne pas modifier le contenu situé entre `<!-- include:... -->` et `<!-- endinclude:... -->` :
  il est régénéré depuis `_shared_content` à chaque synchronisation.
- Toujours lancer sans `--write` d'abord, me montrer le résultat, attendre ma validation.

## Commandes

- Première conversion (une seule fois) : `scripts/prepare_gitbook_branch.sh`
- Synchro régulière : `scripts/sync_from_branch.sh main` puis `scripts/sync_from_branch.sh gitbook-migration-tooling`
  (pas de `git merge` : les modifications sont converties puis appliquées par `scripts/port_changes.py`).
  En cas de conflit (code 2) : résoudre les marqueurs `<<<<<<<`, puis `FINISH=1 scripts/sync_from_branch.sh <source>`.
  Ne JAMAIS relancer la synchro normale avant d'avoir fait le FINISH.
- Vérification des URL avant bascule :
  `python scripts/check_urls.py --sitemap https://docs.sekoia.com/sitemap.xml --new-base <URL GitBook> --extra migration/redirects_mkdocs.csv`

En cas de conflit lors d'une synchro : m'expliquer chaque conflit fichier par fichier et proposer
une résolution. Règle par défaut : structure et emplacement = version `gitbook` ; texte = version source.

## Contenus générés (ne jamais éditer dans GitBook ni à la main)

- `docs/integration/` (intakes, depuis SEKOIA-IO/intake-formats)
- Connecteurs d'actifs (depuis SEKOIA-IO/automation-module)
- `<defend|xdr>/features/automate/library/` (bibliothèque de playbooks, ~100 pages)
- Le bloc inclus dans `built_in_detection_rules.md` (règles de détection)
Toute modification de ces pages doit passer par les générateurs de l'équipe Intégrations.

## Syntaxe GitBook produite

- `!!!` -> `{% hint style="info|success|warning|danger" %}` ... `{% endhint %}`
- `???` -> `<details><summary>...</summary>` ... `</details>`
- `===` -> `{% tabs %}{% tab title="..." %}` ... `{% endtab %}{% endtabs %}`
- Liens internes : relatifs, vers le fichier `.md`.
