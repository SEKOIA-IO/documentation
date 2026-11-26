# GitBook Intake Documentation

Run from the repository root, with an intake-formats checkout next to this repository:

```shell
uv run --project scripts/update_mkdocs python scripts/update_mkdocs/update_gitbook.py ../intake-formats .
uv run --project scripts/update_mkdocs python -m unittest discover -s scripts/update_mkdocs/tests -v
```

The generator writes reusable Markdown to `docs/.gitbook/includes/intakes/`.
By default, the script reads `root` from `.gitbook.yaml` when available; if not,
it falls back to `docs/`. Use `--section-root` to override this value and adjust
page include paths accordingly.

Integration pages use `{% include "../../../.gitbook/includes/intakes/<uuid>.md" %}`
with paths relative to each page. `<uuid>_sample.md` contains raw examples.
Edit the intake source or templates rather than the generated files.
The intake workflow regenerates GitBook includes, runs tests, and
opens a pull request.

Only generated intake fragments are migrated here. Other MkDocs-specific syntax
and shared content belong to the broader migration. Final rendering still needs
to be verified in GitBook.