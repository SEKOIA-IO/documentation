# Troubleshooting

This document will help you fix the most common issues when developing intake-formats.

## Linting issues

This section provides ways to fix most linting issues.

### On the parser

For linting issues on the parser, execute the following command:

```bash
> npx prettier --write '<module_name>/<format_name>/ingest/parser.yml'
```

### On test files, smart-descriptions, ...

To fix linting issues on test files, smart-descriptions, metadata, ..., execute this command:

```bash
> uv run utils/linter.py --changes
```

## Compliance issues

### Logo

Logos for the module and for the format must respect the following criteria:

  - The logo must be a PNG image
  - The logo must be named `logo.png`
  - The background must be transparent
  - The image must be square, i.e. the width is equal to the height
  - The size of the logo must be less than 50 KB

To meet these criteria, execute the following script:

```bash
> uv run utils/normalize_image.py normalize_image "<path_to_the_original_logo>" "<path_to_the_logo>"
```

### Changelog

#### Missing Changelog

If a changelog is missing from our format, please create a CHANGELOG.md file, under the root directory of the format, using this template:

```bash
> cat > CHANGELOG.md <<EOF
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
EOF
```

### Manifest

#### Missing Manifest

Under the `_meta` directory, create the `manifest.yml` file with the following information:

```bash
> cat > _meta/manifest.yml <<EOF
uuid: <unique identifier in the repository (format: uuid)>
name: <the name>
slug: <the slug (format: '^[a-z]([a-z]|-|\d)*$')>

description: >-
  <a description>
EOF
```

For a manifest for a format, add a list of datasources (see [`Missing or invalid datasources`](#missing-or-invalid-datasources))

#### Missing or invalid datasources

The manifest for a format requires a list of datasources, under the `data_sources` field:

```yaml
...

data_sources:
    <data source 1>: <description>
    <data source 2>: <description>
```

The list of expected datasources is available in [Datasources](datasources.md)

### Taxonomy

#### Missing fields.yml

A format expects having a `_meta/fields.yml` file. Please create it even if it's empty.

```bash
> touch _meta/fields.yml
```

#### Invalid or missing custom field

Any custom field, used in the parser, must be declared in `_meta/fields.yml`:

```yaml

<custom field name>:
    name: <custom field name>
    description: <a description explaining what the value of the custom field represents>
    type: <the type of the custom field>
```

See [Custom field](taxonomy.md#custom-field) for the recommendations about the naming and the typing of a custom field.

### Tests

#### Missing or invalid tests

In order to validate developments and prevent regressions on changes, tests are required.

Provide a test covering its use case for the format. See [Create a test](create_a_format.md#create-a-test).

#### Event type or category incorrect

The parsers of a format aim to generate standard JSON documents relying on the [Elastic Common Schema](https://www.elastic.co/docs/reference/ecs) specification.

These generated documents must provide an `event.category` and an `event.type` fields, and the type of the event must match the category of the event.

See [ECS categorization](https://www.elastic.co/docs/reference/ecs/ecs-allowed-values-event-category) to set the correct category with one of its expected type.

#### Incorrect timestamp

Any generated document must provide a `@timestamp` with a [RFC3339-formatted](https://www.rfc-editor.org/rfc/rfc3339.html) datetime.

#### Anonymization

As a public repository, tests inside `intake-formats` must not contain any information that identifies a person, an organization or a machine, as well as any sensitive data.

Redact the following information:

- IP addresses
- domain names
- usernames
- emails
- uuid
- MAC addresses
- Phone number
- Account id
- Identifying information in paths
- API Key
- session token

See [Anonymization guide for test data](https://github.com/SEKOIA-IO/intake-formats/blob/develop/.github/SECURITY_ANONYMIZATION_GUIDE.md) for more details
