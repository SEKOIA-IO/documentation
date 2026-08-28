# Override an Elevate verdict

This article explains how to override an Elevate verdict when it is incorrect or inaccurate, and what happens to the alert when you do.

## Prerequisites

- The alert has an AI-generated verdict. AI verdicts are marked with a sparkle icon in the **Verdict** column of the alert list.
- You have reviewed the investigation. See [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md).

## When to override

There is no separate step to validate an Elevate verdict. If the verdict is correct, leave it as is: the alert keeps the AI verdict and its sparkle icon. If the verdict is incorrect or inaccurate, override it with your own judgment.

## Override a verdict

To override the verdict, select a different verdict from the **Select a verdict** dropdown in the alert header.

![Alert header with the verdict dropdown open showing the available verdicts grouped by category](/assets/elevate/alert-override-verdict.png){: style="max-width:100%"}

!!! note "Your verdict always takes precedence"
    Once you select a verdict, the sparkle icon disappears from the alert list. The alert reflects your analyst verdict, not the AI attribution. The AI verdict is not retained after you override it.

## Result

The alert verdict is updated immediately. The **Verdict** column in the alert list displays your selection without the sparkle icon, indicating an analyst-set verdict.

## Related articles

- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read the AI investigation report before setting a verdict.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
