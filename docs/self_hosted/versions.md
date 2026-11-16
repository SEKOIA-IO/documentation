# Documentation versions

Sekoia Self-Hosted documentation is published per minor version, such as 1.0 or 1.1. Each version is a frozen snapshot: it describes the configuration keys, CLI commands, and behavior of that release only. Patch releases, such as 1.0.1 and 1.0.2, only fix issues within a minor version: they are covered by the documentation of that version, and its release notes list the fixes of each patch.

!!! warning "Check your version before following any procedure"
    Configuration keys and CLI commands change between releases. Running a procedure from the wrong version can break your deployment.

## Available versions

| Version | Latest patch | Status | Documentation |
| :--- | :--- | :--- | :--- |
| 1.0 | 1.0.2 | Current | [Read the documentation](/self_hosted/1.0/index.md) |

The current version is the one shown in the navigation menu. Superseded versions stay published and reachable from this page, but they are no longer updated and are excluded from the site search.

## Release notes

| Version | Release notes |
| :--- | :--- |
| 1.0 | [Release notes v1.0](/self_hosted/1.0/release_notes.md), with the fixes of each patch release in [Patch releases](/self_hosted/1.0/release_notes.md#patch-releases) |

## Upgrading

Sekoia Self-Hosted 1.0.1 is the first generally available release: you deploy it with a fresh installation. Sekoia Self-Hosted 1.0.2 is a patch release of 1.0: see [Patch releases](/self_hosted/1.0/release_notes.md#patch-releases).

<!-- TODO: upgrade path from 1.0.1 to 1.0.2. -->

A fresh installation deploys a release on servers that do not run the platform. An upgrade moves a running deployment to a later release and keeps its data. The release notes of each later version describe its upgrade path and the breaking changes to handle before you upgrade.
