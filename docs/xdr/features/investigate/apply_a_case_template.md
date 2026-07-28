# Apply a case template to a case

Apply a case template to structure a case with predefined custom fields, tasks, and a notebook template. You can do this at the moment you create a case or at any point during an existing investigation.

## Apply a template at case creation

1. Open the case creation modal.
2. In the **Case template** dropdown, search for and select the template that matches the incident type.
3. Fill in the remaining case details and select **Create**.

The case opens with the template's custom fields, tasks, and notebook template already in place.

!!! tip "No template needed at creation"
    Selecting a template at creation is optional. You can always apply one to the case later.

## Apply a template to an existing case

1. Open the case you want to structure.
2. In the top-right corner of the case, select **Case template**.
3. In the modal, search for and select the template to apply.
4. Confirm the selection.

The case is updated with the template's custom fields, tasks, and notebook template.

> 📸 [SCREENSHOT SUGGESTION: A case detail page with the "Case template" button visible in the top-right corner. | ALT TEXT: Case detail page showing the "Case template" button.]

## What happens when you apply multiple templates

Templates are additive. Applying a second template to a case that already has one does not reset the existing structure:

- **Custom fields:** fields from the new template are added. If a field already exists and has a value, that value is kept.
- **Tasks:** tasks from the new template are appended to the existing list.
- **Notebook template:** the new notebook is added alongside any existing one.

!!! note "Review tasks after applying multiple templates"
    Because tasks accumulate with each template applied, check the task list afterward to remove any unintended duplicates.

## Related articles

- [Case templates](/xdr/features/investigate/case_templates.md): Overview of what case templates are and how they work.
- [Create a case template](/xdr/features/investigate/create_a_case_template.md): How to build and configure a template in Settings.
