# Trigger a manual Elevate analysis

This article explains how to trigger an Elevate investigation on an alert that was not analyzed automatically, for example because it was created before Elevate was activated or because it was excluded by a rule filter.

## Prerequisites

- Elevate is activated on your workspace or community. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- The alert has not yet been analyzed. The **Verdict** column shows no AI state, or the alert was excluded by the rule filter.

## Assign the alert to Roy

Roy is the Elevate investigation agent. Assigning an alert to Roy triggers an immediate analysis.

1. Navigate to **Investigate > Alerts**.
2. Select the alert you want to analyze.
3. Select the **Assignee** field in the alert header.
4. Select **Roy**.

> 📸 [SCREENSHOT SUGGESTION: Alert detail view showing the Assignee dropdown open with Roy listed as an available option. | ALT TEXT: Alert assignee dropdown with Roy as a selectable option to trigger a manual Elevate analysis.]

## Result

The agent begins analyzing the alert. The **Verdict** column updates to **In progress** while the analysis runs. Once complete, the verdict and findings are available in the **AI Investigation** tab.

!!! note "Quota consumption"
    A manually triggered analysis consumes one unit of your monthly investigation quota, the same as an automatic analysis.

## Related links

- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read the AI investigation report once the analysis is complete.
- [Elevate analysis states](/xdr/features/modules/elevate_analysis_states.md): Reference table of all possible AI analysis states and their meaning.
- [Manage your Elevate investigation quota](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly investigation quota.
