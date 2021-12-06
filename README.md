# SEKOIA.IO Documentation

The documentation service exposes both the user and the developper documentation to the public. The content is managed by SEKOIA.IO teams but the community is invited to participate in its improvements.

## Contributing to the docs

You can click the **Fork** button in the upper-right area of the screen to create a copy of this repository in your GitHub account. This copy is called a *fork*. Make any changes you want in your fork, and when you are ready to send those changes to us, go to your fork and create a new pull request to let us know about it.

Once your pull request is created, a SEKOIA.IO reviewer will take responsibility for providing clear, actionable feedback.

## Test locally

The service relies on the [MkDocs](https://www.mkdocs.org/) Python framework helped by a customized [Material theme](https://squidfunk.github.io/mkdocs-material/). To serve the documentation on the port `8000` of your computer, you should create a Python virtual environment, install the few requirements detailed in `requirements.txt` and trigger the execution of the MkDocs server:

```shell
$ poetry install
$ mkdir -p docs/stylesheets/ && sassc src/sekoiaio.scss docs/stylesheets/sekoiaio.css
$ poetry run mkdocs serve
```
