# Sekoia Elevate

**Empower your analysts. Accelerate every investigation.**

Sekoia Elevate is the agentic AI layer of the Sekoia AI SOC platform. It brings together autonomous investigation and human validation to help security teams triage faster, investigate deeper, and respond with confidence.

## How Elevate works

When a new alert arrives in Sekoia, the Elevate investigation agent runs a full investigation autonomously without waiting for an analyst to open the alert. It is driven by detection-specific AI runbooks, one per detection rule, that define the exact logic, questions, and false-positive scenarios relevant to that alert type.

For each alert, the agent:

- Assesses the relevance of the alert and the likelihood of a false positive
- Collects and correlates evidence across all available data sources
- Enriches findings with threat intelligence and contextual signals
- Produces a complete, audit-ready investigation report with a verdict and a confidence score

Elevate also investigates cases. Assign a case to Roy, the Elevate investigation agent, and it produces the same verdict, findings and reasoning questions at the case level.

## What makes Elevate different

**Detection-specific AI runbooks** embed expert investigation logic directly at the rule level. Rather than applying generic playbooks across all alert types, the agent follows tailored guidance for each detection.

**Human-in-the-loop by design** keeps analysts in full control. Every finding is reviewable, every verdict is overridable, and every automated decision is fully traceable. There are no black boxes.

**Private by architecture** keeps all AI computation on Sekoia-hosted infrastructure. No data is sent to external LLM providers, which makes Elevate suitable for regulated environments and sensitive data contexts.

## Use cases

Elevate supports a range of SOC scenarios: enabling noisy detection rules instead of muting them, maintaining investigation coverage outside business hours, focusing analysts on real incidents, and helping MSSPs grow without adding headcount, among others. 

## Key concepts

### Verdict

The verdict is the outcome of the AI investigation, accompanied by a confidence score and a plain-language explanation of the reasoning. Analysts can override any verdict at any time. For how Elevate selects a verdict, see [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md).

### Findings

Findings are the individual evidence items the agent collected during its investigation. Each finding is a discrete, verifiable observation drawn from your telemetry, and for each one the analyst can see the exact query or action the agent executed to reach it. 

### Runbooks and reasoning questions

A runbook defines how the agent reasons and investigates a given detection rule, and the reasoning questions show every line of investigation the agent explored for an alert. Together they make the agent's method transparent and tunable. See [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md).

### Runs

Elevate operates on a monthly run pack. Each investigation the agent runs, whether automatic or manually triggered, consumes one run. Runs reset at the start of each month and do not roll over. When the run pack is exhausted, the agent stops analyzing new alerts until your run pack resets the following month.

## Related articles

- [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md): How runbooks, reasoning questions, findings and verdicts work together.
- [Elevate use cases](/xdr/features/modules/elevate_use_cases.md): Common scenarios where Elevate adds value and the features that support them.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent and configure auto-analysis.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read an AI investigation report and interpret findings.
- [Investigate a case with Elevate](/xdr/features/modules/elevate_investigate_case.md): How to trigger an Elevate investigation on a case by assigning it to Roy.
- [Audit an Elevate investigation with Traces](/xdr/features/modules/elevate_traces.md): How to review the full timeline of actions the agent performed.
