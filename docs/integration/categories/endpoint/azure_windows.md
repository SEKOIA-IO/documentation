uuid: 2815eaab-2425-4eff-8038-3f7d5a3b8b11
name: Azure Windows
type: intake

## Overview
Azure Virtual Machines service is developed and managed by Microsoft Corp.

- **Vendor**: Microsoft Azure
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Access tokens,Authentication logs, File monitoring, PowerShell logs, Process command-line parameters, Process monitoring, Process use of network, Windows event logs, Windows Registry	

## Configure
This setup guide will show you how to forward events produced by a Windows Virtual Machine hosted on Azure platform to Sekoia.io.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Azure Event Hubs

As a prerequisite, you need to choose an existing **resource group**, or create a new one (e.g. `company-resource-group`).

#### Retrieve your Subscription ID

You also need your **Subscription ID** if you don't have a default one. 

In Azure Web Portal:

1. Navigate to: `Home` > `Cost Management + Billing` > `Subscriptions`
2. From there, copy the relevant **Subscription ID** that will be used in the command line (e.g. `uuid`)

#### Create the Event Hubs

Use Azure PowerShell (within Cloud Shell interface for example) to create a **namespace** (e.g. `company-eventhub`) and a specific **Event Hub** (e.g. `windows-event`) within your **resource group** (e.g. `company-resource-group`)

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid
```

```powershell
PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name windows-event --message-retention 3 --partition-count 4 --subscription uuid
```

!!! info
    Please replace the following:

    - `company-resource-group` with the name of your **resource group**.
    - `uuid` with your **subscription ID** retrieved previously (see below).

#### Create “Shared Access Policies”

1. Navigate to `Home` > `Event Hubs`> `company-eventhub - Shared access policies`
    - From there, you can create a **policy** (e.g. `RootManageSharedAccessKey`) with the claims `Manage`, `Send` and `Listen` and note the **Primary Key** that will be used as the **SharedAccessKey**

2. Navigate to `Home` > `Event Hubs` > `company-eventhub` > `mysql-event - Shared access policies`
    -  From there, you can create a **policy** (e.g. `sekoiaio`) with the claims `Listen`
    - Once created, click on the policy and save the **Connection string-primary key**, to be sent to Sekoia.io

5. Navigate to `Home`> `Event Hubs`> `company-eventhub`> `mysql-event - Consumer groups`
    - From there, you can create a **consumer group** (e.g. `sekoiaio`)

#### Create a Blob Storage for Checkpointing

In order to allow Sekoia.io keep track of the consumed events, the next step consists in creating a dedicated Azure Blob Storage.

To proceed, you can use Azure PowerShell:

```powershell
PS Azure:\> az storage account create --name "sekoiaiocheckpoint" --resource-group "company-resource-group"
```

```powershell
PS Azure:\> az storage container create --name "windows-event" --account-name "sekoiaiocheckpoint"
```

!!! info
    The container name, here `windows-event` should be the same as the Event Hub’s one.
    You also need to replace `company-resource-group` with the name of your **resource group**.

Finally, you have to retrieve the connection string from Azure Web Portal by going in **Storage Accounts**, then in the created storage (`sekoiaiocheckpoint`) and finally in the **Access Keys** section. After clicking on **Show keys**, you can copy the first of the two connection strings.

### Windows Virtual Machine

You need to activate and configure the diagnostic extension `Microsoft.Insights.VMDiagnosticsSettings`.

1. Navigate to `Home` > `Virtual machines` > `virtual machine name` (e.g. `company-windows`) > `Settings` > `Extensions`. 
    Install it and note the new **StorageAccount** name created (e.g. `company-storage-account`).

3. Navigate to `Home` > `Storage accounts` > `company-storage-account` > `Access keys`.
    From there you can note the key value later used as the **storageAccountKey**.

5. You need to create two configuration files `public_settings.json` and `protected_settings.json`.

Once again you need Azure powershell to do it using your favorite text editor:

```powershell
PS Azure:\> vim public_settings.json
```

Adapt the public settings configuration file with the value oh theses variables: `Url`, `SharedAccessKeyName`, `StorageAccount`.

```json
{
"WadCfg": {
        "DiagnosticMonitorConfiguration": {
            "overallQuotaInMB": 4096,
            "sinks": "applicationInsights.errors",
            "DiagnosticInfrastructureLogs": {
                "scheduledTransferLogLevelFilter": "Error"
            },
            "WindowsEventLog": {
                "scheduledTransferPeriod": "PT1M",
                "DataSource": [
                    {
                      "name": "Application!*"
                    },
                    {
                      "name": "System!*"
                    },
                    {
                      "name": "Security!*"
                    }
                ],
                "sinks": "HotPath"
            },
            "Logs": {
                "scheduledTransferPeriod": "PT1M",
                "scheduledTransferLogLevelFilter": "Error",
                "sinks": "HotPath"
            }
        },
        "SinksConfig": {
            "Sink": [
                {
                    "name": "HotPath",
                    "type": "JsonBlob",
                    "EventHub": {
                        "Url": "https://company-eventhub.servicebus.windows.net/windows-event",
                        "SharedAccessKeyName": "RootManageSharedAccessKey"
                    }
                },
                {
                    "name": "applicationInsights",
                    "ApplicationInsights": "",
                    "Channels": {
                        "Channel": [
                            {
                                "logLevel": "Error",
                                "name": "errors"
                            }
                        ]
                    }
                }
            ]
        }
    },
    "StorageAccount": "company-storage-account"
}
```

A more specific windows event log can be added by specifying the event log filename (e.g for Sysmon: `"name": "Microsoft-Windows-Sysmon/Operational!*"`).


Then edit the protected settings configuration file:

```powershell
PS Azure:\> vim protected_settings.json
```

Adapt the public protected settings configuration file with the value of theses variables: `storageAccountName`, `storageAccountKey`, `Url`, `SharedAccessKeyName`, `SharedAccessKey`:

```json
{
    "storageAccountName": "company-storage-account",
    "storageAccountKey": "base64-string",
    "storageAccountEndPoint": "https://core.windows.net",
    "EventHub": {
        "Url": "https://company-eventhub.servicebus.windows.net/windows-event",
        "SharedAccessKeyName": "RootManageSharedAccessKey",
        "SharedAccessKey": "base64-string"
    }
}
```

Finally you could push the change of the diagnostic extension configuration (adapt the parameters resource-group, vm-name):

```powershell
PS Azure:\> az vm extension set --publisher Microsoft.Azure.Diagnostics --name IaaSDiagnostics --version 1.5 --resource-group company-resource-group --vm-name company-windows --protected-settings protected_settings.json --settings public_settings.json --subscription uuid
```

### Sysmon

Sysmon tool from Microsoft could improve the detection on Windows computers.
You could download the tool on [Microsoft website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
If you do not know how to use and configure it, please check [SwiftOnSecurity github](https://github.com/SwiftOnSecurity/sysmon-config).

### Forward the Connection Keys to Sekoia.io

Finally, please send to Sekoia.io the following information:

- Azure Event Hub’s **Connection string-primary key** (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=windows-event"`).
- Azure Event Hub’s **consumer group name** (e.g. `sekoiaio`).
- Azure Blob Storage’s **connection string** (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`).

{!_shared_content/operations_center/integrations/generated/2815eaab-2425-4eff-8038-3f7d5a3b8b11_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_2815eaab-2425-4eff-8038-3f7d5a3b8b11_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2815eaab-2425-4eff-8038-3f7d5a3b8b11.md!}

## Further Readings

- [Microsoft Github windows diagnostic extension documentation](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/azure-monitor/platform/diagnostics-extension-stream-event-hubs.md)
