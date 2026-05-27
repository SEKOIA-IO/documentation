# Add custom instructions for Elevate agents

Elevate investigation results can be refined by adding custom instructions to the agent. This article explains how to provide contextual instructions at the workspace or community level, and how to customize the reasoning questions embedded in a detection rule's runbook.

## Prerequisites

- Elevate is activated on your workspace or community. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).

## Add contextual instructions

Contextual instructions tell the agent what is normal or expected in your environment. The agent takes them into account when analyzing alerts and producing its verdict.

To add instructions for a specific community:

1. Navigate to **Settings > AI agent**.
2. Select the community where you want the instructions to apply.
3. Select **Agent/Alert case investigation**.
4. Select the **Instructions** tab.
5. Enter your custom instructions.
6. Select **Save**.

!!! note "Applying instructions to all communities"
    To apply instructions across all communities, select your workspace instead of a specific community in step 2.

> 📸 [SCREENSHOT SUGGESTION: AI agent settings panel with the Instructions tab open, showing a free-text field containing example instructions. | ALT TEXT: Instructions tab in the AI agent settings panel with a text input field.]

## Customize the reasoning questions of a detection rule

The reasoning questions are the structured questions the agent answers during its investigation of an alert. They are defined in the rule's runbook and drive the findings the agent collects.

!!! tip "Custom rules vs. Sekoia rules"
    You can edit the reasoning questions of any detection rule you created. If the triggering rule was built by Sekoia, you can duplicate it and edit the runbook on the copy, but the duplicated rule will not receive automatic updates from Sekoia.

To modify the reasoning questions of a detection rule:

1. Open an alert triggered by the rule you want to customize.
2. In the **Triggered rule** section, select **Runbook**.
3. At the bottom of the runbook panel, select **Edit runbook**.
4. Modify the reasoning questions according to your needs.
5. Select **Save runbook**.

> 📸 [SCREENSHOT SUGGESTION: Runbook panel open from an alert's Triggered rule section, showing the Edit runbook button at the bottom and the Reasoning questions section visible above it. | ALT TEXT: Runbook panel showing the Edit runbook button and the Reasoning questions section.]

From the next alert triggered by this rule, the agent applies your updated reasoning questions.

!!! note "Scope of runbook changes"
    Runbook modifications apply to all communities in your workspace.

## Related links

- [Write effective instructions for Elevate](/xdr/usecases/elevate_instructions_best_practices.md): Use case guidance and examples for writing instructions that improve investigation quality.
- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent and configure auto-analysis.
- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
