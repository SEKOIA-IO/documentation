# Investigate an incident from alert to verdict

Sekoia gives you a structured path from an alert to an analyst-owned verdict. In this tutorial, you review an alert with Elevate, verify the evidence, group the alert in a case, and record the conclusion for the rest of your team.

## One suspicious command, no time to waste

A workstation has launched a PowerShell command that does not fit the user's usual activity. It could be a legitimate administrative task, or the first visible sign of an intrusion. The alert is already in the queue, and the next analyst needs to decide whether to dismiss it, escalate it, or connect it to a wider incident.

The detection rule and data sources depend on your environment. Use an alert that has completed an Elevate analysis, or follow the same workflow with a manually investigated alert.

## Do it in Sekoia

Start with the alert, test the initial hypothesis against the evidence, then turn the investigation into a case that others can review. In this tutorial, you read the Elevate verdict, verify its findings, attach the alert to a case, and record the analyst-owned conclusion.

## Before you start

- You have access to the **Investigate** module.
- The alert has been created in Sekoia.
- Elevate is activated if you want to use the AI investigation. See [Activate Sekoia Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- The alert has a completed Elevate analysis if you want to review an AI verdict.
- You can create and update cases in your community.

!!! note "Use the AI verdict as an investigation input"

    Elevate provides a verdict, confidence score, findings, and reasoning questions. Analysts remain responsible for reviewing the evidence and changing the verdict when the evidence does not support it.

## Open the alert

Start with the alert that triggered the investigation.

1. Go to **Investigate > Alerts**.
2. Select the alert for the suspicious PowerShell activity.
3. Confirm that the alert details page has loaded.

Record the basic context before you start your review. Note the detection name, affected entity, time range, severity, and urgency when those fields are available in your alert.

## Review the Elevate verdict

Use the investigation summary to form an initial hypothesis.

1. Read the **Verdict** section in the alert header.
2. Note the classification selected by Elevate.
3. Note the confidence score.
4. Read the plain-language explanation.
5. Compare the explanation with the alert context.

The verdict is not a replacement for evidence review. It tells you how the agent interpreted the available data and gives you a starting point for the investigation.

For the complete alert review procedure, see [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md).

## Verify the findings

Findings are the evidence items collected by the agent. Review them one by one and check whether they support or weaken the initial hypothesis.

1. Switch to the **Findings** view in the alert details.
2. Open each finding that relates to the affected workstation, user, process, or network connection.
3. Review the observation recorded by the agent.
4. Open the related query or action when you need to verify the underlying data.
5. Compare the result with the original alert.

Use the **Reasoning questions** section to understand the investigation path.

1. Scroll to **Reasoning questions**.
2. Read the questions that came from the detection rule's runbook.
3. Review the agent's answer to each question.
4. Identify unanswered questions or evidence that needs a manual check.

Detection-specific runbooks define the investigation questions, legitimate scenarios, and detection rationale used by Elevate. For more detail, see [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md).

> 📸 [SCREENSHOT SUGGESTION: Alert details page with the Findings view and Reasoning questions section expanded. | ALT TEXT: Alert investigation showing evidence items and the questions used to reach the verdict.]

## Create the incident case

Create a case when the alert needs collaboration, additional evidence, or a record that can be shared with other analysts.

1. Go to **Cases**.
2. Click **+ Case**.
3. Enter a title that identifies the incident, such as `Suspicious PowerShell activity on workstation`.
4. Enter a description that summarizes the initial hypothesis and the scope of the investigation.
5. Select an **Assignee**.
6. Set a **Priority**.
7. Add tags that match your incident workflow.
8. Select a **Case template** if your team uses one.
9. Click **Create**.

The case opens immediately. It provides a workspace for alerts, events, tasks, comments, custom fields, graph investigation, and a notebook.

For details about case structure and templates, see [Cases](/xdr/features/investigate/cases.md) and [Create a case](/xdr/features/investigate/create_a_case.md).

## Attach the alert to the case

Add the alert that started your investigation to the new case.

1. Return to the alert details page.
2. Click **Add to case**.
3. Search for the case you created.
4. Select the case.
5. Confirm the association.

The alert is now part of the incident record. You can add related alerts as the investigation develops.

## Record the investigation

Use the case to make your reasoning available to the next analyst.

1. Add a comment that states the evidence you reviewed.
2. Record the affected entities and relevant time range.
3. Add tasks for evidence that still requires collection or validation.
4. Add related alerts and events when they belong to the same incident.
5. Record the conclusion in the notebook or the fields provided by your case template.

Keep the conclusion specific. State what happened, which evidence supports it, and what action the team must take next.

!!! tip "Separate evidence from interpretation"

    Write the observed event first, then explain what it means. This makes the investigation easier to review and helps other analysts challenge or confirm the conclusion.

## Set the analyst verdict

If the Elevate verdict matches your review, you can leave it unchanged. If your review reaches a different conclusion, replace it with your analyst verdict.

1. Open the alert details page.
2. Select a different verdict from the **Select a verdict** dropdown in the alert header.
3. Choose the verdict that matches the evidence.

The analyst verdict takes precedence over the AI verdict. The alert list no longer displays the AI attribution icon after you override the verdict.

For the complete procedure, see [Override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md).

## Result

You have moved from an initial alert to a documented incident decision. The case contains the alert and the investigation record, while the alert shows the verdict selected by the analyst. Other analysts can review the evidence, continue the investigation, and follow the next actions without rebuilding the context.

## Related articles

- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read an AI verdict, findings, and reasoning questions.
- [The Elevate investigation method](/xdr/features/modules/elevate_investigation_method.md): Overview of runbooks, reasoning questions, findings, and verdicts.
- [Cases](/xdr/features/investigate/cases.md): Overview of the case workspace and its investigation content.
- [Create a case](/xdr/features/investigate/create_a_case.md): How to create a case and attach alerts.
- [Case details](/xdr/features/investigate/case_details.md): Reference for the tabs and fields available in a case.
- [Custom verdicts](/xdr/features/investigate/custom_verdicts.md): How to standardize alert and case outcomes.
- [Override an Elevate verdict](/xdr/features/modules/elevate_validate_verdict.md): How to replace an AI verdict with an analyst verdict.
