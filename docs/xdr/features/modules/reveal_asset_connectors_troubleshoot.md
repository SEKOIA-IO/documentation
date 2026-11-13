# Troubleshoot asset connectors

This article applies to built-in and custom asset connectors. It explains how to identify connector failures, inspect logs, interpret push errors, and update a connector configuration.

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
| HTTP error on push | The push was refused or partly rejected: see [Diagnose push errors](#diagnose-push-errors) |

### Diagnose push errors

A push error appears in the connector logs with its response code and error code. Errors apply to built-in and custom asset connectors, unless the scope says otherwise.

| Response | Error code | Cause | Action | Scope |
|---|---|---|---|---|
| 200 with `rejected` | - | Some items have an invalid or fully-qualified `device.hostname`. The other items are accepted. `rejected` lists up to 50 rejected items with the reason. | Send the short hostname in `hostname` and the rest in `domain`. | Built-in and custom |
| 422 | - | Every item of the push was rejected, for the same reason. | Same as above. | Built-in and custom |
| 403 | `INSUFFICIENT_PERMISSIONS` | The API key cannot push assets to the community of the configuration. | Use an API key of that community with the permission to push assets. | Built-in and custom |
| 404 | `ASSET_CONNECTOR_NOT_FOUND` | The asset connector configuration was deleted or does not exist. | Check the configuration the connector runs for. | Built-in and custom |
| 413 | `ASSET_CONNECTOR_PUSH_TOO_LARGE` | An item is larger than the item-size limit. | Send fewer interfaces, groups or accounts in the item. | Built-in and custom |
| 429 | `ASSET_CONNECTOR_RATE_LIMIT_EXCEEDED` | The configuration reached the push rate limit. `details.limit` is `items per day` for the daily quota. | Per minute: send larger batches less often. Per day: send fewer items, or wait for the quota to reset 24 hours after the first counted push. | Built-in and custom |
| 429 | `ASSET_CONNECTOR_LIMIT_REACHED` | The configuration or its community reached a storage limit. `details.limits` lists the reached limits. | See [Storage limits for custom asset connectors](/xdr/features/modules/reveal_asset_connectors_limits.md#storage-limits-for-custom-asset-connectors). | Custom only |
| 503 | `ASSET_CONNECTOR_PUSH_UNAVAILABLE` | Sekoia could not confirm the delivery. Some items may have been accepted. | The connector does not retry the batch. See the note below. | Built-in and custom |

After a 429, the connector pauses for an hour by default, then fetches again from its last checkpoint.

After any other error, the connector does not retry the batch. It logs the error and continues with the next batch. The items of that batch reach Sekoia only when a later run fetches them again:

- A connector that sends its whole inventory at every run sends them again at its next run.
- A connector that only sends what changed since its checkpoint may not send them again.

Sending an item again is safe. A device, a user or a finding is matched on its hostname, username or email, or CVEs, so it updates the same asset as long as these fields do not change. If a 503 persists, contact Sekoia support. A 403 or 404 persists until the configuration is fixed.

The logs show the error code of a 429 from version TBD of `sekoia-automation-sdk`.

The values of the limits are in [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md).

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

## Related articles

- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure a new asset connector from the integration catalog.
- [Build a custom asset connector](/xdr/features/modules/build_a_custom_asset_connector.md): How to send valid data and avoid duplicate assets.
- [Asset connector limits](/xdr/features/modules/reveal_asset_connectors_limits.md): Rate limits, caps and storage limits of asset connectors.
- [Reveal feature enablement matrix](/xdr/features/modules/reveal_feature_enablement.md): Which data sources are required for each Reveal capability.
- [Security controls](/xdr/features/modules/reveal_security_controls.md): How to verify connector coverage and identify visibility gaps from the asset context panel.
- [Troubleshoot Reveal](/xdr/features/modules/reveal_troubleshoot.md): General Reveal troubleshooting for missing data across capabilities.
