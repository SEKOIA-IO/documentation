# Validate or override an Elevate verdict

This article explains how to confirm the AI verdict on an alert or replace it with your own judgment.

## Prerequisites

- The alert has an AI-generated verdict. AI verdicts are marked with a sparkle icon in the **Verdict** column of the alert list.
- You have reviewed the investigation report. See [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md).

## Set a verdict

To validate or override the AI verdict, select your verdict from the **Select a verdict** dropdown in the alert header.

- To **validate** the AI conclusion, select the same verdict the agent produced.
- To **override** the AI conclusion, select a different verdict.

> 📸 [SCREENSHOT SUGGESTION: Alert detail view header showing the "Select a verdict" dropdown open with True Positive and False Positive options visible. | ALT TEXT: Alert header with the verdict dropdown open showing available verdict options.]

!!! note "Your verdict always takes precedence"
    Once you select a verdict, the sparkle icon disappears from the alert list. The alert reflects your analyst verdict, not the AI attribution. The original AI verdict and its reasoning remain accessible in the **AI Investigation** tab for reference.

## Result

The alert verdict is updated immediately. The **Verdict** column in the alert list displays your selection without the sparkle icon, indicating an analyst-confirmed verdict.

## Related links

- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read the AI investigation report before setting a verdict.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
