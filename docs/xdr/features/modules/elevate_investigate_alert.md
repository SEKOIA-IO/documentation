# Investigate an alert with Elevate

This article explains how to access and read the AI investigation report produced by Elevate for an alert, including the verdict, confidence score, and findings.

## Prerequisites

- Elevate is activated on your workspace or community. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- The alert has been analyzed by the Elevate agent. Check the **Verdict** column in the alert list to confirm the analysis is complete. If the state is **In progress** or shows an error, see [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md).

## Open the AI investigation report

1. Navigate to **Investigate > Alerts**.
2. Select the alert you want to review.

> 📸 [SCREENSHOT SUGGESTION: Alert detail view with the AI Investigation tab selected, showing the Verdict section at the top and the Findings section below. | ALT TEXT: AI Investigation tab of an alert showing the verdict and findings sections.]

## Read the verdict

The **Verdict** section at the top of the AI Investigation tab contains:

- The **classification**: True Positive or False Positive
- The **confidence score**: a percentage expressing the agent's certainty in its conclusion
- A **plain-language explanation** summarizing the key evidence and reasoning behind the classification

??? example "Example verdict: False Positive at 85% confidence"
    The spike involved four distinct hosts and included an external source IP, but there were no authentication failures, new processes, data exfiltration, privileged account usage, IoC matches, or corroborating alerts from other sensors. The lack of any malicious indicators suggests the activity is benign and therefore a false positive.

## Read the findings

Findings are the individual evidence items the agent collected and evaluated. Each finding is a discrete, verifiable observation drawn from your telemetry.

To review the findings from the AI Investigation tab:

1. Scroll to the **Findings** section below the verdict.
2. Select the expand arrow on any finding card to view the underlying data that supports it.

Findings tagged **Global** apply to the alert as a whole rather than to a specific asset or event.

> 📸 [SCREENSHOT SUGGESTION: Findings section of the AI Investigation tab with several finding cards expanded, each displaying a "Global" tag and a plain-language observation. | ALT TEXT: Findings section showing expandable evidence cards with Global tags.]

### Access findings from the alert timeline

A summary of findings is also available directly from the alert detail view without opening the AI Investigation tab.

1. In the alert detail view, locate the timeline panel.
2. Select the **Findings** tab.

The Findings tab lists all evidence items the agent collected, allowing you to review them alongside the alert timeline.

> 📸 [SCREENSHOT SUGGESTION: Alert detail view with the Findings tab selected in the timeline panel, showing a bulleted list of evidence items collected by the Elevate agent. | ALT TEXT: Findings tab in the alert timeline panel showing AI-collected evidence items.]

## Discover Reasoning questions

To go further in your understanding of the verdict and findings methodology, scroll down to **Reasoning questions** sections. 

Most of the Reasoning questions comes from our Runbooks, but Elevate agent add its own relevant investigation questions. 


## Related links

- [Validate or override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md): How to confirm or change the AI verdict once you have reviewed the investigation.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
- [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md): How to analyze an alert that was not processed automatically.
