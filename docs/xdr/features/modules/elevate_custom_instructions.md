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

![Instructions tab in the AI agent settings panel with a text input field](/assets/elevate/custom-instructions.png){: style="max-width:100%"}

## Choose the language of investigation text

Elevate does not use the platform interface language as a deterministic selector for the language of an investigation. The language of the verdict explanation, findings, and reasoning answers can be influenced by the context provided to the agent, including custom instructions and runbook content.

To request a consistent language, state it explicitly in the instructions. For example:

!!! example "Request investigations in French"
    Write all investigation explanations, verdicts, findings, and reasoning answers in French. Keep product names, detection names, query syntax, and field names unchanged.

![Community-level Elevate instructions requesting French verdict explanations and findings](/assets/elevate/custom-instructions-language.png){: style="max-width:100%"}

![Elevate investigation showing a verdict and findings written in French](/assets/elevate/french-investigation-example.png){: style="max-width:100%"}

Use a workspace-level instruction when all communities should use the same language. To use a different language for each tenant or customer, add the instruction at community level instead.

!!! note "Language applies when the investigation is generated"
    Elevate saves the generated investigation text with the alert. It does not translate the text dynamically according to each viewer's interface language. An English interface can therefore display an investigation generated in French. Updated language instructions apply to investigations generated afterward.

Using French or another language in the surrounding context may influence the agent, but it does not guarantee a specific output language. An explicit language instruction is the recommended way to make the expected language clear.

To customize how the agent reasons for a specific detection rule rather than for your environment as a whole, edit the rule's runbook instead. See [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md).

## Related articles

- [Write effective instructions for Elevate](/xdr/features/modules/elevate_instructions_best_practices.md): Guidance and examples for writing instructions that improve investigation quality.
- [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md): How to edit the Detection Rational, legitimate scenarios and investigation questions of a runbook.
- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent and configure auto-analysis.
- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
