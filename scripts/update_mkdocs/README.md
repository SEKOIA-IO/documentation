# GitBook Asset Connector Documentation

Run from the repository root, with an automation-library checkout next to this repository:

```shell
uv run --project scripts/update_mkdocs python scripts/update_mkdocs/update_gitbook_asset_connectors.py ../automation-library .
uv run --project scripts/update_mkdocs python -m unittest discover -s scripts/update_mkdocs/tests -v
```

The generator writes one GitBook reusable content block per asset connector to
`docs/.gitbook/includes/asset_connectors/<slug>_<type>.md` and removes the blocks
of connectors that no longer exist. `docs/` is the root of the GitBook space
(see `.gitbook.yaml`). Use `--section-root` to select another root, for example
`--section-root docs/integration` for a space rooted at `docs/integration`.

It also rewrites the legacy MkDocs includes in the pages of that space
(`{!_shared_content/.../generated_assets_documentation/<slug>_<type>.md!}`,
including the form escaped by GitBook) to
`{% include "<relative path>/.gitbook/includes/asset_connectors/<slug>_<type>.md" %}`.

Generated blocks are overwritten on every run: edit the mapping files in
automation-library or `templates/asset_connector_gitbook.md.jinja`, not the blocks
in GitBook. The `update-asset-connectors-documentation` workflow still runs the
MkDocs generator; switching it is a separate task.
