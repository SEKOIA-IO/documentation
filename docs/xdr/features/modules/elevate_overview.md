# Elevate

Elevate is the AI investigation layer of Sekoia, built to automatically triage and investigate alerts end-to-end. It deploys a specialized AI agent that analyzes every incoming alert, correlates evidence across your data sources, and produces a structured investigation report so your analysts focus on decisions, response, and strategy rather than manual triage.

## How Elevate works

When a new alert arrives in Sekoia, the Elevate investigation agent runs a full investigation autonomously without waiting for an analyst to open the alert. It is driven by detection-specific AI runbooks curated by Sekoia's research team, one per detection rule, that define the exact logic, questions, and false-positive scenarios relevant to that alert type.

For each alert, the agent:

- Assesses the relevance of the alert and the likelihood of a false positive
- Collects and correlates evidence across all available data sources
- Enriches findings with threat intelligence and contextual signals
- Produces a complete, audit-ready investigation report with a verdict and a confidence score

## What makes Elevate different

**Detection-specific AI runbooks** embed expert investigation logic directly at the rule level. Rather than applying generic playbooks across all alert types, the agent follows tailored guidance for each detection.

**Human-in-the-loop by design** keeps analysts in full control. Every finding is reviewable, every verdict is overridable, and every automated decision is fully traceable. There are no black boxes.

**Sovereign AI by architecture** ensures all AI computation runs on Sekoia-hosted infrastructure. No data is sent to external LLM providers, which makes Elevate suitable for regulated environments and sensitive data contexts.

## Key concepts

### Verdict

The verdict is the outcome of the AI investigation. It classifies the alert as a **True Positive** or a **False Positive**, accompanied by a confidence score and a plain-language explanation of the reasoning. Analysts can validate or override any verdict at any time.

### Findings

Findings are the individual evidence items the agent collected during its investigation. Each finding is a discrete, verifiable observation drawn from your telemetry. They are visible in the **AI Investigation** tab and in the **Findings** panel of the alert timeline.

### Investigation quota

Elevate operates on a monthly investigation quota. Each alert analyzed by the agent consumes one unit. When the quota is exhausted, the agent stops analyzing new alerts until the next billing cycle.

## Related links

- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent and configure auto-analysis.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read an AI investigation report and interpret findings.
