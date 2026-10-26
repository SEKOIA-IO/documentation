# Troubleshoot asset connectors

This article explains how to identify and resolve issues with asset connectors using error indicators and connector logs.

## Before you begin

To access the asset connector list, navigate to **Configure > Assets > Asset connectors**.

## Step 1: Identify a defective connector

Review the connector list. A connector with an issue displays an error message in the upper right corner of its tile.

!!! note "Zero assets warning"
    If a connector tile shows 0 assets, this may indicate a synchronization issue even if no error message is visible. Inspect the logs to confirm.

![!Defective connector with message Error during data collection](/assets/connector_error_mesg.png){: style="width: 100%; max-width: 100%"}

## Step 2: Open the connector logs

1. On the defective connector tile, select **...**.
2. Select **View logs**.

The full log list opens.

![!Asset connector log list with error entries](/assets/connector_logs.png){: style="width: 100%; max-width: 100%"}

## Step 3: Diagnose the issue

Review the log entries to identify the root cause. Common issues include:

| Symptom | Likely cause |
|---|---|
| Authentication error | Invalid or expired credentials |
| Permission denied | Insufficient rights on the external system |
| No assets retrieved | The account cannot see any asset on the external system (wrong tenant or missing permissions) |
| Timeout | Network connectivity issue or external system unavailable |

!!! note "Connector running on a local runner"

    If the connector runs on a local runner, check the runner before changing the connector configuration.

    1. Navigate to **Configure > Assets > Local runners**.
    2. Confirm that the selected runner is **Online**.
    3. Check the runner's last activity, hostname, and version.
    4. If the runner is offline or cannot reach Sekoia, check the host connectivity, proxy configuration, Docker service, and Endpoint Agent logs.

    For runner configuration and connectivity checks, see [Local runners](/xdr/features/automate/playbooks-on-premises.md). For Endpoint Agent logs, see [Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md).

## Step 4: Edit the connector configuration

If the issue is caused by a misconfiguration or expired credentials:

1. Close the logs panel.
2. On the connector tile, select **...**.
3. Select **Edit**.
4. Update the relevant fields such as the API key or client ID.
5. Select **Test connector** to validate the updated credentials.
6. When the test is conclusive, select **Edit asset connector**.

The connector resumes synchronization with the updated configuration.

!!! note "What the test checks"
    The test validates credentials only. It does not retrieve assets. Verify asset retrieval from the **Assets** page after saving.

## Related links

- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md) — How to configure a new asset connector from the integration catalog.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md) — Which data sources are required for each Reveal capability.
- [Security controls](/xdr/features/modules/reveal_security_controls.md) — How to verify connector coverage and identify visibility gaps from the asset context panel.
- [Troubleshoot Reveal](/xdr/features/modules/reveal_troubleshoot.md) — General Reveal troubleshooting for missing data across capabilities.
- [Local runners](/xdr/features/automate/playbooks-on-premises.md): How to check runner status and troubleshoot local execution.
- [Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to collect Endpoint Agent logs and diagnose connectivity issues.
