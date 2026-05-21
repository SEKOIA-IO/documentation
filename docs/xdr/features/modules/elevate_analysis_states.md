# Elevate analysis states

The **Verdict** column in the alert list displays the current state of the Elevate AI investigation for each alert. This article describes every possible state and what it means.

> 📸 [SCREENSHOT SUGGESTION: Alert list view with the Verdict column highlighted, showing a variety of AI analysis states including "In progress", "Confirmed Attack", "AI analysis failed", "AI analysis timeout", and "AI limit reached". | ALT TEXT: Alert list showing different Elevate verdict states in the Verdict column.]

## States reference

| State | Description |
|---|---|
| **In progress** | The AI agent is currently analyzing the alert. Results will be available shortly. |
| **True Positive** | The agent concluded the alert represents a real threat. A confidence score and explanation are available in the AI Investigation tab. |
| **False Positive** | The agent concluded the alert is benign. A confidence score and explanation are available in the AI Investigation tab. |
| **AI analysis failed** | The analysis could not be completed due to an internal error. You can retry by reassigning the alert to Roy. |
| **AI analysis timeout** | The analysis request timed out before completing. You can retry by reassigning the alert to Roy. |
| **AI limit reached** | Your monthly investigation quota is exhausted. No new alerts will be analyzed until the next billing cycle or until your administrator upgrades your plan. |

## AI-generated vs. analyst-set verdicts

Verdicts set by the Elevate agent display a sparkle icon in the alert list. When an analyst validates or overrides the AI verdict manually, the sparkle icon disappears and the verdict reflects the analyst's choice.

## Related links

- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
- [Validate or override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md): How to confirm or change the AI verdict on an alert.
- [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md): How to analyze an alert that was not processed automatically.
- [Manage your Elevate investigation quota](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly investigation quota.
