# SEKOIA.IO Documentation

The documentation service exposes both the user and the developper documentation to the public. The content is managed by SEKOIA.IO teams but the community is invited to participate in its improvements.

## Contributing to the docs

You can click the **Fork** button in the upper-right area of the screen to create a copy of this repository in your GitHub account. This copy is called a *fork*. Make any changes you want in your fork, and when you are ready to send those changes to us, go to your fork and create a new pull request to let us know about it.

Once your pull request is created, a SEKOIA.IO reviewer will take responsibility for providing clear, actionable feedback.

## Test locally

The service relies on the [MkDocs](https://www.mkdocs.org/) Python framework helped by a customized [Material theme](https://squidfunk.github.io/mkdocs-material/). To serve the documentation on the port `8000` of your computer, you should create a Python virtual environment, install the few requirements detailed in `pyproject.toml` and trigger the execution of the MkDocs server:

```shell
$ pip install poetry
$ poetry install
$ poetry run mkdocs serve --strict
```

## Guidelines

* You may use absolute links and images such as `[caption](/folder/page.md#anchor)` or `![!someimage](/folder/image.png)`, they will be interpreted as relative to the `docs/` folder. So the example link would point to `docs/folder/page.md` which must exist in the repo. `mkdocs serve --strict` will help you catching any broken link
* When you want to point to the developer documentation, please use full URLs, such as `[delete_playbook_endpoint](https://docs.sekoia.io/xdr/develop/rest_api/playbooks/#tag/Playbooks/operation/delete_playbook_resource)`, because the API documentation is rendered client-side via ReDoc out of OpenAPI specs retrieved from app.sekoia.io platform's API
* Always include the `.md` extension when linking to markdown files in the repo: `[link](/integration/example/index.md)` is okay, whereas `[link](/integration/example/)` or `[link](/integration/example/index)` won't work.
* All links to internal pages and anchors are strictly validated by the CI (via `mkdocs build --strict`) to spot any broken link. Therefore, please refrain as much as possible from using full URLs to point to internal pages, as they won't be covered by automated broken link verification.
