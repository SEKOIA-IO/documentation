# Add custom instructions for an Elevate agent

Custom instructions give the Elevate agent environment-specific context it cannot infer from telemetry alone. This article explains how to provide contextual instructions at the workspace or community level so the agent produces more relevant verdicts.

## Prerequisites

- Elevate is activated on your workspace or community. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).

## Add contextual instructions

Contextual instructions tell the agent what is normal or expected in your environment. The agent takes them into account when analyzing alerts and producing its verdict.

To add instructions for a specific community:

1. Navigate to **Settings > AI agents**.
2. Select the community where you want the instructions to apply.
3. Select **Alert/Case Investigation** agent.
4. Select the **Instructions** tab.
5. Enter your custom instructions.
6. Select **Save**.

!!! note "Applying instructions to all communities"
    To apply instructions across all communities, select your workspace instead of a specific community in step 2.

> 📸 [SCREENSHOT SUGGESTION: AI agent settings panel with the Instructions tab open, showing a free-text field containing example instructions. | ALT TEXT: Instructions tab in the AI agent settings panel with a text input field.]

To customize how the agent reasons for a specific detection rule rather than for your environment as a whole, edit the rule's runbook instead. See [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md).

## Related articles

- [Write effective instructions for Elevate](/xdr/features/modules/elevate_instructions_best_practices.md): Guidance and examples for writing instructions that improve investigation quality.
- [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md): How to edit the Detection Rational, legitimate scenarios and investigation questions of a runbook.
- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent and configure auto-analysis.
- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
