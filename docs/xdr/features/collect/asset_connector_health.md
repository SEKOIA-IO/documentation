# Asset connector health status and logs

**[Reveal module](reveal_index.md)** — This feature requires the Reveal add-on module.

The asset connectors panel provides visibility into whether a connector is experiencing errors and what happened during its recent activity. Use it to confirm successful synchronizations, identify issues preventing asset collection, and gather precise error details for troubleshooting or escalation.

## Access the asset connectors panel

1. Navigate to **Configure > Assets**.
2. Open the **Asset Connectors** panel.

From this panel, you can review connector error states and open detailed logs for a specific connector.

## View connector error states

The asset connectors panel displays error states when issues affect a connector. If no error is affecting a connector, no error state is displayed.

**Possible error states**

| State | Condition | Description |
|---|---|---|
| Error during data collection | More than 5 error logs in the last 24 hours | The connector is still functional and running but has encountered repeated errors during data collection. |
| Stopped by critical error | Critical errors have forced the connector to stop | The connector is no longer running and requires intervention. |

> 📸 [SCREENSHOT SUGGESTION: Asset connectors panel showing a connector with an error state badge such as "Error during data collection" next to its name. | ALT TEXT: Asset connectors panel with a connector entry displaying an error state indicator.]

## View connector logs

Connector logs help you understand what happened during a connector run. Use them to confirm whether a synchronization completed successfully, check when the last synchronization occurred, and investigate authentication, API quota, or connectivity issues.

### Open connector logs

1. Navigate to **Configure > Assets**.
2. Open the **Asset Connectors** panel.
3. Open the **...** menu for the connector you want to inspect.
4. Select **View logs**.

!!! tip "Review recent runs first"
    Start by reviewing the most recent runs to determine whether the issue is ongoing or limited to a single execution.

> 📸 [SCREENSHOT SUGGESTION: Asset connectors panel with the ... menu open for a connector, showing the View logs option highlighted. | ALT TEXT: Asset connectors panel showing the options menu for a connector with the View logs item visible.]

### What the logs show

For each connector run, the logs can include the following information.

**Run status**

A high-level indication of log severity, such as:

| Status | Description |
|---|---|
| Info | Normal operational information |
| Debug | Detailed diagnostic output |
| Error | Issues encountered during the run |

**Timestamps**

| Field | Description |
|---|---|
| Start time | When the connector run began |
| End time | When the connector run completed |
| Duration | Total time elapsed for the run |

**Execution details**

Useful information about what happened during the run, including:

- connection attempts made to the source system
- authentication steps and outcomes
- requests sent to the source system
- objects or records processed
- import, update, or skip actions applied to assets

> 📸 [SCREENSHOT SUGGESTION: Connector log view showing a list of log entries with status badges (Info, Error), timestamps, and execution detail messages. | ALT TEXT: Connector log view with run entries showing status, timestamps, and execution detail lines.]

## Related links

- [Asset context panel](asset_context_panel.md) — Full reference for the asset context panel, which displays data enriched by asset connectors including security controls, vulnerabilities, and hygiene information.
- [Attack path visualization](attack_path_visualization.md) — How attack path graph enrichment depends on asset connectors providing relationship and exposure data.
- [Integration — Asset categories](https://docs.sekoia.io/integration/assets_categories/overview/) — Reference documentation for asset connector categories and integration setup.
- [Collect — Assets](https://docs.sekoia.io/xdr/features/collect/assets/) — How assets are configured and discovered in Sekoia, including the role of asset connectors in the collection pipeline.
