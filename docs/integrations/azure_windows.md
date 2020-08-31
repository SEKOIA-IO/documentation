uuid: 2815eaab-2425-4eff-8038-3f7d5a3b8b11
name: Azure Windows

## Overview
Azure Virtual Machines service is developed and managed by Microsoft Corp.

## Setup
This setup guide will show you how to forward events produced by a Windows Virtual Machine hosted on Azure platform to SEKOIA.IO.

Theses changes have to be made from the Azure web portal (https://portal.azure.com).

### 1. Event hubs
As a prerequisite you need an `Event Hubs` (e.g. company-eventhub) and to choose an existing `resourceGroup` or create a new one (e.g. company-resource-group).
You also need your `Subscription ID` if you don't have a default one.

Navigate to: `Home > Cost Management + Billing > Subscriptions`. From there, copy the relevant `Subscription ID` that will be used in the command line (e.g. uuid)

Then you use Azure powershell (within Cloud Shell interface for example): you will a create a global `Event Hubs`, then specific `Event Hub` (e.g. active-directory-event).

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid

PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name windows-event --message-retention 3 --partition-count 4 --subscription uuid
```

Navigate to: `Home > Event Hubs > company-eventhub - Shared access policies`. From there, you can create a policy (e.g. RootManageSharedAccessKey) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.

Navigate to: `Home > Event Hubs > company-eventhub > windows-event - Shared access policies`. From there, you can create a policy (e.g. sekoiaio-nifi) with the claims `Listen`. Once created, click on the policy and save the `Connection string-primary key`, to be sent to SEKOIA.IO.

Navigate to: `Home > Event Hubs > company-eventhub > windows-event - Consumer groups`. From there, you can create a consumer group (e.g. sekoiaio-nifi).

### 2. Windows Virtual Machine
You need to activate and configure the diagnostic extension `Microsoft.Insights.VMDiagnosticsSettings`.
Navigate to: `Home > Virtual machines > virtual machine name (e.g. company-windows) > Settings > Extensions`. Install it and note the new `StorageAccount` name created (e.g. company-storage-account).

Navigate to: `Home > Storage accounts > company-storage-account - Access keys`. From there you can note the key value later used as the `storageAccountKey`.

You need to create two configuration files `public_settings.json` and `protected_settings.json`.
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

### 3. Sysmon

Sysmon tool from Microsoft could improve the detection on Windows computers.
You could download the tool on [Microsoft website](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).
If you do not know how to use and configure it, please check [SwiftOnSecurity github](https://github.com/SwiftOnSecurity/sysmon-config).

### 4. Enjoy your events
You can send to Sekoia the `Connection string-primary key` previously mentioned.

Once the configuration has been done on Sekoia side, you can go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.

## Further Readings

- [Microsoft Github windows diagnostic extension documentation](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/azure-monitor/platform/diagnostics-extension-stream-event-hubs.md)
