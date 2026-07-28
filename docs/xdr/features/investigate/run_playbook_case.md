# Run a playbook from a case

You can trigger a SOAR playbook directly from within a case, without leaving the investigation screen. Any playbook configured with a **Case manual trigger** appears in the case's playbook panel and runs against the case context with a single click.

## Before you begin

- The playbook you want to run must be configured with the **Case manual trigger** trigger type. Playbooks using other trigger types do not appear in the case panel.[PLACEHOLDER: How???? ]
- [PLACEHOLDER: Confirm the required permission level (e.g., Analyst role or above.)]

## Run a playbook from a case

1. Open the case from which you want to trigger a playbook.
2. Click the **Available playbooks for this case** icon in the top-right corner of the case view.

   > 📸 [SCREENSHOT SUGGESTION: The case header with the "Available playbooks for this case" icon highlighted in the top-right corner. | ALT TEXT: Case header showing the Available playbooks icon.]

   The **Available playbooks for this case** panel opens on the right side of the screen, listing all playbooks configured with a Case manual trigger.

3. Find the playbook you want to run in the panel.
4. Click the **▶** button next to the playbook name. Hover over it to confirm the tooltip reads **Run this playbook**.

   > 📸 [SCREENSHOT SUGGESTION: The Available playbooks panel with the "Run this playbook" tooltip visible on the ▶ button. | ALT TEXT: Available playbooks panel showing the Run this playbook tooltip on the run button.]

   The icon next to the playbook name changes to a loading spinner while the execution is in progress.

5. Wait for the run to complete. Once finished, the status updates in the **View last runs performed** section.

## View previous runs

To check the history of executions for a playbook, click **View last runs performed** below the playbook name. Each entry shows:

- A **status badge**: In progress, Succeeded, or Failed — the same statuses as standard playbook executions.
- The **time elapsed** since the run was triggered (e.g. "less than a minute ago").
- The **execution duration** (e.g. "Performed in less than a minute").

!!! note "Case activity feed"
    Entries in the case activity feed reflect the actions performed by the playbook itself (for example, adding a comment, updating a field, or closing an alert). The trigger does not generate a dedicated activity entry.

## Related articles

- [Cases overview](/xdr/features/investigate/cases.md): Overview of the Cases feature and the investigation workflow.
- [Playbooks overview](/xdr/features/automate/playbooks.md): Overview of playbooks and how the SOAR engine works.
- [Create a playbook](/xdr/features/automate/create_playbook.md): How to create and configure a playbook.
