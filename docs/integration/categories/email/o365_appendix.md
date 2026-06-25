## Collect Office365 events through Azure EventHub

This is the alternative way to collect Office365 events. It is recommended when:

- The Management API approach is not suitable for your environment
- You are using **China tenants** (operated by 21Vianet)

!!! note "China tenants"
    If you are using a China tenant (21Vianet), replace portal URLs as follows:

    - Azure Portal: `https://portal.azure.cn`
    - Microsoft Purview compliance portal: `https://compliance.microsoft.cn`

### Prerequisites

This setup guide will show you how to generate, store and forward events produced by Office 365 service to Sekoia.io.
These changes have to be made from the Azure web portal ([https://portal.azure.com](https://portal.azure.com)).

### A. Event Hubs

As a prerequisite you need an `Event Hub` (e.g. company-eventhub) and to choose an existing `resourceGroup` or create a new one (e.g. company-resource-group).
You also need your `Subscription ID` if you don't have a default one.

Navigate to: `Home > Cost Management + Billing > Subscriptions`. From there, copy the relevant `Subscription ID` that will be used in the command line (e.g. uuid).
Then use Azure PowerShell (within the Cloud Shell interface for example): you will create a global `Event Hubs` namespace, then a specific `Event Hub` (e.g. o365-event).
```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid

PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name o365-event --message-retention 3 --partition-count 4 --subscription uuid
```

Navigate to: `Home > Event Hubs > company-eventhub - Shared access policies`. From there, you can create a policy (e.g. RootManageSharedAccessKey) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.

Navigate to: `Home > Event Hubs > company-eventhub > o365-event - Shared access policies`. From there, you can create a policy (e.g. sekoiaio) with the claim `Listen`.
> Once created, click on the policy and save the `Connection string-primary key` — it will be used when configuring the Sekoia.io playbook.

Navigate to: `Home > Event Hubs > company-eventhub > o365-event - Consumer groups`. From there, create a consumer group (e.g. sekoiaio).

### B. Stream M365 Unified Audit logs (Exchange, SharePoint, General)

Exchange, SharePoint and General audit events are part of the **M365 Unified Audit Log**. They are **not** configured in the Azure Portal but in the **Microsoft Purview compliance portal**.

!!! note
    A single streaming configuration in Microsoft Purview covers all audit log categories (Exchange, SharePoint, Teams, OneDrive, General, etc.) at once. No separate configuration per category is required.

1. Go to the [Microsoft Purview compliance portal](https://compliance.microsoft.com) (`https://compliance.microsoft.cn` for China tenants)
2. Navigate to `Audit > Audit log streaming`
3. Click `Turn on streaming` (if not already enabled)
4. Select `Stream to Azure Event Hubs` as the destination
5. Enter the Event Hub namespace connection string and the Event Hub name created in section A
6. Save the configuration

> If audit logging is not yet enabled for your organization, refer to [Turn auditing on or off](https://docs.microsoft.com/en-us/microsoft-365/compliance/turn-audit-log-search-on-or-off).

### Create the intake

1. Go to the Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes)
2. Click `+ Intake`
3. Search for **`Office 365`** and select the **Office 365** format
4. Give it a name and assign it to the relevant Entity
5. When prompted for the configuration mode, select **`Manual`** — this skips the OAuth/Management API flow and provides a raw Intake Key
6. Copy the **Intake Key** — it will be used in the playbook below

### Pull events

1. Go to the [Playbooks page](https://app.sekoia.io/operations/playbooks)
2. Create a new playbook using the **`Consume Eventhub messages`** trigger
3. Configure the trigger with the following fields:

    | Field | Value |
    |---|---|
    | **Configuration Name** | A name for this configuration |
    | **categories** | Leave empty to collect all event categories, or specify a subset |
    | **Chunk Size** | `1000` (default) |
    | **Hub Connection String** | The `Connection string-primary key` from the `Listen` policy on your Event Hub |
    | **Hub Consumer Group** | `sekoiaio` (or the consumer group created in section A) |
    | **Hub Name** | The name of your Event Hub (e.g. `o365-event`) |
    | **Intake Key** | The Intake Key copied from the intake created above |
    | **Intake Server** | `https://intake.sekoia.io` (default) |
    | **Storage Connection String** | The `Connection string-primary key` of your Azure Storage account |
    | **Storage Container Name** | The name of the Azure Storage blob container |

4. Start the playbook and verify events flow into your [Events page](https://app.sekoia.io/operations/events)

!!! note "Multiple clients"
    For each client, create a dedicated Event Hub (or separate Event Hubs within the same namespace), a dedicated Sekoia intake, and a dedicated playbook. This ensures log isolation between tenants.

## Further Readings
- [Microsoft: Stream Azure monitoring data to an event hub](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/stream-monitoring-data-event-hubs)
- [Microsoft: Audit log streaming in Microsoft Purview](https://learn.microsoft.com/en-us/purview/audit-streaming)
- [Microsoft: Turn auditing on or off](https://docs.microsoft.com/en-us/microsoft-365/compliance/turn-audit-log-search-on-or-off)