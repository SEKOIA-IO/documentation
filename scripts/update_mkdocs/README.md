# GitBook Asset Connector Documentation

Run from the repository root, with an automation-library checkout next to this repository:

```shell
uv run --project scripts/update_mkdocs python scripts/update_mkdocs/update_gitbook_asset_connectors.py ../automation-library .
uv run --project scripts/update_mkdocs python -m unittest discover -s scripts/update_mkdocs/tests -v
```

The generator writes one GitBook reusable content block per asset connector to
`docs/.gitbook/includes/asset_connectors/<slug>_<type>.md` and removes the blocks
of connectors that no longer exist. The generator owns this folder: any other
Markdown file in it is deleted, so keep hand-written reusable content elsewhere
in `.gitbook/includes/`. `docs/` is the root of the GitBook space
(see `.gitbook.yaml` on the `gitbook` branch). Use `--section-root` to select another root, for example
`--section-root docs/integration` for a space rooted at `docs/integration`.

It also rewrites the legacy MkDocs includes in the pages of that space
(`{!_shared_content/.../generated_assets_documentation/<slug>_<type>.md!}`,
including the form escaped by GitBook) to
`{% include "<relative path>/.gitbook/includes/asset_connectors/<slug>_<type>.md" %}`.

The script exits with code 1 when a module has two connectors with the same
`<slug>_<type>` (the second one is skipped, the rest is still written), or when
a page would include a block under `asset_connectors/` that this run does not
produce, for example after a connector was removed or a page was moved. In that
case nothing is written, so the tree stays as it was.

Generated blocks are overwritten on every run: edit the mapping files in
automation-library or `templates/asset_connector_gitbook.md.jinja`, not the blocks
in GitBook. The `update-asset-connectors-documentation` workflow still runs the
MkDocs generator; switching it is a separate task.
