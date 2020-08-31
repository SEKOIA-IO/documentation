# SEKOIA.IO Documentation

The documentation service exposes both the user and the developper documentation to the public. The content is managed by SEKOIA.IO teams but the community is invited to participate in its improvements.

## Test locally

The service relies on the [MkDocs](https://www.mkdocs.org/) Python framework helped by a customized [Material theme](https://squidfunk.github.io/mkdocs-material/). To serve the documentation on the port `8000` of your computer, you should create a Python virtual environment, install the few requirements detailed in `requirements.txt` and trigger the execution of the MkDocs server:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
(venv) $ mkdir -p docs/stylesheets/ && sassc src/sekoiaio.scss docs/stylesheets/sekoiaio.css
(venv) $ mkdocs serve
```
