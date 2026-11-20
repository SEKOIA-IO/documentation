# GitBook Intake Documentation

Run from the repository root, with an intake-formats checkout next to this repository:

```shell
uv run --project scripts/update_mkdocs python scripts/update_mkdocs/update_gitbook.py ../intake-formats .
uv run --project scripts/update_mkdocs python -m unittest discover -s scripts/update_mkdocs/tests -v
```

The generator writes reusable Markdown to `docs/.gitbook/includes/intakes/`.
This assumes `docs/` is the root of the GitBook-synced section. Confirm the
section root in GitBook before enabling Git Sync. Use `--section-root` to
select another root, and adjust the page include paths accordingly.

Integration pages use `{% include "../../../.gitbook/includes/intakes/<uuid>.md" %}`
with paths relative to each page. `<uuid>_sample.md` contains raw examples.
Edit the intake source or templates rather than the generated files.
The intake workflow regenerates the includes and opens a pull request.

Only generated intake fragments are migrated here. Other MkDocs-specific syntax
and shared content belong to the broader migration. Final rendering still needs
to be verified in GitBook.