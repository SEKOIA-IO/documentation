# Reduce alert fatigue with Sekoia Elevate

Sekoia Elevate automatically investigates incoming alerts and returns a verdict with supporting evidence and a confidence score. In this tutorial, you activate Elevate, scope the alerts it analyzes, review its reasoning, and keep the final decision with your analysts.

## When the queue fills faster than your team can work

Monday morning, the alert queue is already growing. The detection rules are doing their job, but analysts are spending too much time checking the same benign patterns and too little time on the alerts that may require action. Turning off noisy rules would remove visibility, so you need another way to separate useful signals from routine noise.

## Do it in Sekoia

Use Sekoia Elevate to investigate relevant alerts before an analyst opens them. In this tutorial, you activate automatic analysis, limit it to the alerts that matter, review the evidence behind each verdict, and keep the final decision with your analysts.

## Before you start

- Your subscription includes the Elevate module.
- You have administrator access to the workspace.
- At least one intake is configured and sending events to Sekoia.
- Your detection rules and alert sources are producing the alerts you want Elevate to analyze.
- You have reviewed [Sekoia Elevate](/xdr/features/modules/elevate_overview.md) and understand that each analysis consumes one run from your monthly run pack.

!!! warning "Run consumption starts when you enable auto-analysis"

    Enabling **Auto-analyze alerts** starts analysis for new incoming alerts across the workspace. Review your available runs before you activate the agent.

## Activate automatic alert analysis

The agent is disabled by default, so you can choose when to start consuming runs.

1. Go to **Settings > Subscriptions**.
2. Confirm that your subscription includes **Elevate**.
3. Go to **Settings > AI agents**.
4. Select **Alert/Case Investigation** in the **Workspace** section.
5. Select the **Settings** tab.
6. Enable **Auto-analyze alerts**.

New incoming alerts are now sent to the Elevate investigation agent. The **Verdict** column in the alert list is updated when each investigation completes.

For the complete activation procedure, see [Activate Sekoia Elevate on a workspace](/xdr/features/modules/elevate_activate.md).

## Limit which alerts Elevate analyzes

If your workspace receives a high volume of alerts, use filters to reserve runs for alerts that need investigation. You can combine filters based on the detection rule, rule effort level, alert severity, or alert urgency.

1. Go to **Settings > AI agents**.
2. Select **Alert/Case Investigation**.
3. Select the **Settings** tab.
4. Open **Filters**.
5. Select the rules or thresholds that match your triage policy.
6. Save the configuration.

Filters are evaluated when the alert is raised. An alert that does not match the configured filters does not consume a run.

!!! note "Filters combine"

    When you configure several filters, an alert must match all of them before Elevate analyzes it. With no filter configured, Elevate analyzes every new alert.

For the available filters and their behavior, see [Scope auto-analysis with filters](/xdr/features/modules/elevate_rule_filter.md).

## Add context from your environment

Elevate uses detection-specific runbooks to investigate alerts. You can also provide workspace context, such as legitimate administrative activity, known service accounts, or investigation priorities.

1. Go to **Settings > AI agents**.
2. Select **Alert/Case Investigation**.
3. Open the **Instructions** field.
4. Enter environment-specific context that can help the agent distinguish expected activity from suspicious activity.
5. Save the instructions.

Keep instructions specific and verifiable. Describe the behavior, account, host group, or operating window that analysts should consider during triage.

For examples and writing guidance, see [Add custom instructions for an Elevate agent](/xdr/features/modules/elevate_custom_instructions.md) and [Write effective instructions for Elevate](/xdr/features/modules/elevate_instructions_best_practices.md).

## Review an automated investigation

After Elevate completes an analysis, use the alert details page to decide which alerts need analyst action.

1. Go to **Investigate > Alerts**.
2. Select an alert with a completed Elevate analysis.
3. Read the **Verdict** section in the alert header.
4. Check the classification, confidence score, and plain-language explanation.
5. Open the **Findings** view.
6. Review the evidence collected by the agent.
7. Open the **Reasoning questions** section.
8. Compare the questions and answers with the evidence in your environment.

Each finding is a discrete observation drawn from your telemetry. The alert details page also lets you inspect the query or action that produced a finding. This gives analysts a way to verify the result instead of treating the verdict as an unexplained label.

The investigation follows a runbook associated with the detection rule. The runbook contains the detection rationale, legitimate scenarios, and investigation questions. To understand how these parts produce a verdict, see [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md).

For the alert review procedure, see [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md).

> 📸 [SCREENSHOT SUGGESTION: Alert details page showing the Elevate verdict, confidence score, findings, and reasoning questions. | ALT TEXT: Alert details page with an Elevate verdict and investigation evidence.]

## Keep or override the verdict

If the evidence supports the Elevate verdict, leave it unchanged. If your investigation reaches a different conclusion, set the analyst verdict yourself.

1. Open the alert details page.
2. Select a different verdict from the **Select a verdict** dropdown in the alert header.
3. Choose the verdict that matches your investigation.

Your verdict takes precedence over the AI verdict. The alert list then displays the analyst-set verdict without the AI attribution icon.

For more information, see [Override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md).

## Result

Elevate now investigates the alert types that match your policy and provides analysts with a verdict, evidence, and reasoning before they start a manual review. Your team can focus on alerts that require a decision while keeping noisy detection rules active and preserving analyst oversight.

## Related articles

- [Sekoia Elevate](/xdr/features/modules/elevate_overview.md): Overview of the Elevate investigation agent, runbooks, findings, verdicts, and run packs.
- [Activate Sekoia Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable automatic alert analysis.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read the verdict, findings, and reasoning questions.
- [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md): Overview of how runbooks and evidence produce a verdict.
- [Override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md): How to replace an AI verdict with an analyst verdict.
- [Manage your Elevate runs](/xdr/features/modules/elevate_quota.md): How to monitor run consumption and optimize the monthly run pack.
