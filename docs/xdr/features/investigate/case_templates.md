# Case templates

A case template is a reusable configuration bundle that structures a case with predefined custom fields, tasks, and a notebook template. Apply one at case creation or at any point during an investigation to ensure every case of the same incident type follows a consistent, repeatable process.

## Why use case templates

Without a shared structure, analysts build each case from scratch. Over time, this creates drift: fields go unfilled, investigation notes lack a common shape, and triage steps get skipped under pressure. Case quality depends on the individual analyst rather than on a defined process.

Case templates address this by encoding your team's best practices directly into the platform. When a phishing case opens from a template, it already carries the right custom fields, the right investigation notebook, and the right task checklist. Junior analysts follow the same process as senior ones, and every closed case is auditable by construction.

For MSSPs (Managed Security Service Providers), templates also support multi-community governance: each community can maintain its own set of templates, ensuring consistent, auditable delivery across a rotating analyst pool.

## What a template contains

A case template is made up of three optional components:

| Component | Description |
|---|---|
| **Custom fields** | Data fields attached to the template. When applied, those fields appear in the case for analysts to fill in. |
| **Tasks** | A checklist of investigation steps. Tasks become active once the template is linked to a case. |
| **Notebook template** | A structured investigation notebook that guides the analyst's documentation and findings. |

## How to apply a template

You can apply a template in two ways:

- **At case creation:** select a template from the **Case template** dropdown in the case creation modal. The case opens fully structured.
- **On an existing case:** click the **Case template** button in the top-right corner of a case at any point during the investigation.

## Behavior when applying multiple templates

Applying a second template to a case that already has one does not replace the existing structure. Templates stack additively:

- **Custom fields:** fields from the new template are added to the case. If a field already exists and contains a value, that value is preserved.
- **Tasks:** tasks from the new template are appended to the existing task list.
- **Notebook template:** the new notebook template is added alongside any existing one.

!!! note "Task accumulation"
    Because tasks accumulate when multiple templates are applied, review the task list after each application to avoid unintended duplicates.

## Related articles

- [Create a case template](/xdr/features/investigate/create_a_case_template.md): How to create and configure a template in Settings.
- [Apply a case template to a case](/xdr/features/investigate/apply_a_case_template.md): How to apply a template at case creation or on an existing case.
