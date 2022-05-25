uuid: 162064f0-c594-455e-ac24-2d7129137688
name: Azure Linux
type: intake

## Overview

Azure Virtual Machines service is developed and managed by Microsoft Corp.

{!xdr/features/collect/integrations/generated/azure-linux_do_not_edit_manually.md!}

## Configure

This setup guide will show you how to forward events produced by a Linux Virtual Machine hosted on Azure platform to SEKOIA.IO.

Theses changes have to be made from the [Azure Web Portal](https://portal.azure.com).

### Azure Event Hubs

As a prerequisite, you need to choose an existing “resource group”, or create a new one (e.g. `company-resource-group`).

#### Retrieve your Subscription ID

You also need your “Subscription ID” if you don't have a default one. In Azure Web Portal, navigate to: “Home”, “Cost Management + Billing”, ”Subscriptions”. From there, copy the relevant “Subscription ID” that will be used in the command line (e.g. `uuid`)

#### Create the Event Hubs

Use Azure PowerShell (within Cloud Shell interface for example) to create a namespace (e.g. `company-eventhub`) and a specific `Event Hub` (e.g. `linux-event`) within your “resource group” (e.g. `company-resource-group`)

```powershell
PS Azure:\> az eventhubs namespace create --name company-eventhub --resource-group company-resource-group --enable-kafka true --subscription uuid
```

```powershell
PS Azure:\> az eventhubs eventhub create --resource-group company-resource-group --namespace-name company-eventhub --name linux-event --message-retention 3 --partition-count 4 --subscription uuid
```

!!! info
    Please replace :

    - `company-resource-group` with the name of your “resource group”.
    - `uuid` with your subscription ID retrieved previously (see below).

#### Create “Shared Access Policies”

1. Navigate to “Home”, “Event Hubs”, “company-eventhub - Shared access policies”. From there, you can create a policy (e.g. `RootManageSharedAccessKey`) with the claims `Manage`, `Send` and `Listen`, and note the `Primary Key` that will be used as the `SharedAccessKey`.
2. Navigate to “Home”, “Event Hubs”, “company-eventhub”, “linux-event - Shared access policies”. From there, you can create a policy (e.g. `sekoiaio`) with the claims `Listen`. Once created, click on the policy and save the `Connection string-primary key`, to be sent to SEKOIA.IO.
3. Navigate to “Home”, “Event Hubs”, “company-eventhub”, ”linux-event - Consumer groups”. From there, you can create a consumer group (e.g. `sekoiaio`).

#### Create a Blob Storage for Checkpointing

In order to allow SEKOIA.IO keep track of the consumed events, the next step consists in creating a dedicated Azure Blob Storage.

To proceed, you can use Azure PowerShell:

```powershell
PS Azure:\> az storage account create --name "sekoiaiocheckpoint" --resource-group "company-resource-group"
```

```powershell
PS Azure:\> az storage container create --name "linux-event" --account-name "sekoiaiocheckpoint"
```

!!! info
    The container name, here `linux-event` should be the same as the Event Hub’s one.
    You also need to replace `company-resource-group` with the name of your “resource group”.

Finally, you have to retrieve the connection string from Azure Web Portal by going in “Storage Accounts”, then in the created storage (`sekoiaiocheckpoint`) and finally in the “Access Keys” section. After clicking on “Show keys”, you can copy the first of the two connection strings.

### Linux Virtual Machine

You need to activate and configure the diagnostic extension `LinuxDiagnostic`.

1. Navigate to “Home”, “Virtual machines”, “virtual machine name (e.g. company-linux)”, “Settings” and “Extensions”. Install it and note the new `StorageAccount` name created (e.g. `company-storage-account`).
2. Navigate to “Home”, “Storage accounts”, “company-storage-account”, “Access keys”. From there you can note the key value later used as the `storageAccountKey`.
3. Navigate to “Home”, “Storage accounts”, “company-storage-account”, “Shared access signature”. From there set the expiration date with caution, then click on “Generate SAS and connection string”. You should note the `SAS token` value later used (starting with `sv?=`).

Navigate to “Home”, “All resources”. From there you can note the `resourceId` associated to your linux virtual machine.

You need to create two configuration files `public_settings.json` and `protected_settings.json`.

Once again you need Azure PowerShell to do it using your favorite text editor:

```powershell
PS Azure:\> vim public_settings.json
```

Adapt the public settings configuration file with the value of theses variables: `StorageAccount`, `resourceId` and `sinks` and the syslog configuration.

```json
{
  "StorageAccount": "company-storage-account",
  "ladCfg": {
    "diagnosticMonitorConfiguration": {
      "eventVolume": "Medium",
      "metrics": {
        "metricAggregation": [
          {
            "scheduledTransferPeriod": "PT1H"
          },
          {
            "scheduledTransferPeriod": "PT1M"
          }
        ],
        "resourceId": "/subscriptions/128ed5ce-4f50-4b5f-a3b0-08233b5a86b6/resourceGroups/company-resource-group/providers/Microsoft.Compute/virtualMachines/company-linux"
      },
      "performanceCounters": {
        "performanceCounterConfiguration": []
      },
      "syslogEvents": {
        "sinks": "linux-event",
        "syslogEventConfiguration": {
          "LOG_AUTH": "LOG_INFO",
          "LOG_AUTHPRIV": "LOG_INFO",
          "LOG_CRON": "LOG_INFO",
          "LOG_DAEMON": "LOG_INFO",
          "LOG_FTP": "LOG_INFO",
          "LOG_KERN": "LOG_INFO",
          "LOG_LOCAL0": "LOG_INFO",
          "LOG_LOCAL1": "LOG_INFO",
          "LOG_LOCAL2": "LOG_INFO",
          "LOG_LOCAL3": "LOG_INFO",
          "LOG_LOCAL4": "LOG_INFO",
          "LOG_LOCAL5": "LOG_INFO",
          "LOG_LOCAL6": "LOG_INFO",
          "LOG_LOCAL7": "LOG_INFO",
          "LOG_LPR": "LOG_INFO",
          "LOG_MAIL": "LOG_INFO",
          "LOG_NEWS": "LOG_INFO",
          "LOG_SYSLOG": "LOG_INFO",
          "LOG_USER": "LOG_INFO",
          "LOG_UUCP": "LOG_INFO"
        }
      }
    },
    "sampleRateInSeconds": 15
  }
}
```

You need to generate an authentication token for the access to the `linux-event` hub.
First we'll convert the expiration date we set before into a unix timestamp. Extract the `se=` value from `storageAccountSasTokenv`and use it as a parameter to this command:

```powershell
PS Azure:\> date -d '2021-07-09T23:09:19' +%s
1625872159
```

Then you could create this python script:

```powershell
PS Azure:\> vim get_token.py
```

Adapt theses variables: `sb_name`, `eh_name`, `Url`, `sas_name`, `sas_value`, and `expiry`:

```python
from urllib.parse import quote_plus, quote
import hmac
import hashlib
import base64

def get_auth_token(sb_name, eh_name, sas_name, sas_value, expiry):
    """
    Returns an authorization token dictionary
    for making calls to Event Hubs REST API.
    """
    uri = quote_plus("https://{}.servicebus.windows.net/{}" \
                                  .format(sb_name, eh_name))
    sas = sas_value.encode('utf-8')
    string_to_sign = (uri + '\n' + expiry).encode('utf-8')
    signed_hmac_sha256 = hmac.HMAC(sas, string_to_sign, hashlib.sha256)
    signature = quote(base64.b64encode(signed_hmac_sha256.digest()))
    return  {"sb_name": sb_name,
             "eh_name": eh_name,
             "token":'SharedAccessSignature sr={}&sig={}&se={}&skn={}' \
                     .format(uri, signature, expiry, sas_name)
            }

print(get_auth_token(sb_name="company-eventhub", eh_name="linux-event", sas_name="RootManageSharedAccessKey", sas_value="base64string", expiry="unix_timestamp"))
```

Execute this python script and note the `token` variable value only from the `sr=`.

```powershell
PS Azure:\> python get_token.py
{'token': 'SharedAccessSignature sr=https%3A%2F%2Fcompany-eventhub.servicebus.windows.net%2Flinux-event&sig=9%2BOwFlfqBVEcVg2c5G1wztIjG22GtsMZN5g4NYEu6p0%3D&se=1561569146&skn=RootManageSharedAccessKey', 'eh_name': 'linux-event', 'sb_name': 'company-eventhub'}
```

Then edit the protected settings configuration file:

```powershell
PS Azure:\> vim protected_settings.json
```

Adapt the public protected settings configuration file with the value of theses variables: `storageAccountName`, `storageAccountSasToken` (starting with sv= and previously refered as `SAS token`), `sasURL` (replace the different values, company-eventhub, linux-event, sr=, and RootManageSharedAccessKey), and `SharedAccessKeyName`:

```json
{
    "storageAccountName": "company-storage-account",
    "storageAccountSasToken": "sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-06-21T15:52:44Z&st=2019-06-21T07:52:44Z&spr=https&sig=Dewc7mP63E4xrwqttVcOrChgDIpm6Trp%2FR4dfvSo4vg%3D",
    "sinksConfig": {
        "sink": [
            {
                "name": "SyslogJsonBlob",
                "type": "JsonBlob"
            },
            {
                "name": "linux-event",
                "type": "EventHub",
                "sasURL": "https://company-eventhub.servicebus.windows.net/linux-event?sr=https%3A%2F%2Fcompany-eventhub.servicebus.windows.net%2Flinux-event&sig=W86ldfWlPKW0sutGWM7shYGlg%2BbwnbtyVJ7eMsBs840%3D&se=1561137701&skn=RootManageSharedAccessKey"
            }
        ]
    }
}
```

Finally you could push the change of the diagnostic extension configuration (adapt the parameters resource-group, vm-name):

```powershell
PS Azure:\> az vm extension set --publisher Microsoft.Azure.Diagnostics --name LinuxDiagnostic --version 3.0 --resource-group company-resource-group --vm-name company-linux --protected-settings protected_settings.json --settings public_settings.json --subscription uuid
```

### Forward the Connection Keys to SEKOIA.IO

Finally, please send to SEKOIA.IO the following information:

- Azure Event Hub’s “Connection string-primary key” (e.g. `"Endpoint=sb://company-eventhub.servicebus.windows.net/;SharedAccessKeyName=sekoiaio;SharedAccessKey=XXXXXX;EntityPath=linux-event"`).
- Azure Event Hub’s consumer group name (e.g. `sekoiaio`).
- Azure Blob Storage’s connection string (e.g. `"DefaultEndpointsProtocol=https;AccountName=sekoiaiocheckpoint;AccountKey=XXXXX"`).

## Further Readings

- [Microsoft Github linux diagnostic extension documentation](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/virtual-machines/extensions/diagnostics-linux.md)
- [Linkedin post](https://www.linkedin.com/pulse/how-send-syslog-messages-from-azure-linux-vms-eventhub-adrian-corona/)
