# The Elevate investigation method

Every Elevate investigation follows a structured method built on detection-specific runbooks, reasoning questions, findings and a final verdict. This article explains how those pieces fit together so you can read an AI investigation with confidence and know where to intervene to improve it.

## How an investigation runs

When an alert arrives, the Elevate agent runs a detailed analysis workflow to determine whether the alert is a real incident and how severe it is. The agent does not wait for an analyst to open the alert: it investigates autonomously, then produces a summary that states the outcome and the confidence behind it.

The investigation is driven by a **runbook** tied to the detection rule that raised the alert. The runbook tells the agent what the detection is meant to catch, which legitimate situations could explain it, and which questions to answer. The agent works through those questions, gathers evidence as **findings**, and consolidates everything into a **verdict**.

!!! note "Investigating cases"
    Elevate can also investigate a case when you assign it to Roy. The investigation is performed at the case level: it produces a single case-level verdict, findings and reasoning questions, not separate verdicts for the individual alerts in the case. See [Investigate a case with Elevate](/xdr/features/modules/elevate_investigate_case.md).

## Runbooks

Runbooks define the way agents reason and carry out their investigations. Sekoia Elevate generates a runbook **automatically for every detection rule**, including your custom rules, and analysts can edit it at any time for fine tuning.

Each runbook has three sections:

- **Detection Rational**: context for the agent about why the alert exists and what the detection is aiming to identify.
- **Legitimate scenarios**: the benign situations that could trigger this detection. Describing them helps the agent recognize likely false positives.
- **Investigation questions**: the questions the agent works through during the investigation. They are closely tied to the reasoning questions seen on the alert, and the agent may add its own questions while processing an alert.

To edit a runbook, see [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md).

## Reasoning questions

The reasoning questions show every line of investigation the Elevate agents explored for an alert. They give the agent a structured investigation method for alert triage: the agent analyzes each question and answers it using the data and tools available in the platform.

Each answer contributes to forging the verdict. Most reasoning questions come from the runbook's investigation questions, and the agent adds its own questions when an alert calls for it.

## Findings

Findings are the discrete evidence items the agent collected and evaluated during the investigation. Each finding is a verifiable observation drawn from your telemetry.

For every finding, the analyst can see the **exact query or action the agent executed** to reach it. Consulting the query behind a finding lets you immediately understand and confirm the information, and it doubles as a learning tool: analysts can draw on the way agents carry out their triage. To review every action the agent took during the investigation, with its duration, open the Traces panel. See [Audit an Elevate investigation with Traces](/xdr/features/modules/elevate_traces.md).

## How the agent searches your data

To investigate, the agent runs search queries over your events. When it builds those queries, it takes into account the [intakes](/xdr/features/collect/intakes.md) (the log sources) configured in your community, so it searches the data you have actually ingested, targets the relevant fields, and pivots accurately across your datasets instead of querying sources you do not collect. This keeps the agent's searches grounded in your environment and improves the relevance of its findings.

## Verdict

The verdict is the outcome of the investigation, with a confidence score and a plain-language explanation of the reasoning.

Rather than applying a fixed label, Elevate selects the most appropriate verdict for the alert from those available in your workspace, including the **custom verdicts** your SOC defines in **Settings > Custom Statuses**. Each custom verdict has a name and a description, and the agent reads them to decide which one fits. The clearer and more specific your descriptions, the more accurately Elevate adapts to and applies your own verdicts. You can override the verdict at any time. See [Override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md).

## How detection rules and intelligence feed the investigation

Two sources of expert knowledge shape every investigation:

- **The detection rule.** Alerts are raised by detection rules authored by the Sekoia Threat Detection & Research (TDR) team, or by detection engineers in the platform with the support of generative AI. The rule defines what triggered the alert and anchors the runbook.
- **Threat intelligence.** Related intelligence, including ATT&CK mappings, adds context and helps classify the alert. This intelligence comes from the Sekoia TDR team. It is useful for human analysts, and it is also taken into account by Elevate agents when they perform their investigations.

!!! note "Private by architecture"
    All AI computation runs on Sekoia infrastructure. No customer data is sent to external LLM providers, which makes Elevate suitable for regulated environments and sensitive data contexts.

## Related articles

- [Elevate](/xdr/features/modules/elevate_overview.md): Overview of how Elevate works and its key concepts.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read an AI investigation report and interpret findings.
- [Investigate a case with Elevate](/xdr/features/modules/elevate_investigate_case.md): How to trigger a case investigation by assigning the case to Roy.
- [Audit an Elevate investigation with Traces](/xdr/features/modules/elevate_traces.md): How to review the full timeline of actions the agent performed.
- [Customize a detection rule's runbook](/xdr/features/modules/elevate_customize_runbook.md): How to edit the Detection Rational, legitimate scenarios and investigation questions of a runbook.
- [Add custom instructions for an Elevate agent](/xdr/features/modules/elevate_custom_instructions.md): How to give the agent environment-specific context.
