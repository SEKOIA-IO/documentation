uuid: 2259adc3-9d93-4150-9c1c-46804e636084
name: FortiWeb
type: intake

## Overview

This documentation details one way to collect and send FortiWeb logs to Sekoia.io: from the FortiWeb machine to an internal syslog concentrator, then forwarded to Sekoia.io


{!_shared_content/operations_center/detection/generated/suggested_rules_2259adc3-9d93-4150-9c1c-46804e636084_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2259adc3-9d93-4150-9c1c-46804e636084.md!}

## Configure

On FortiWeb appliances, most of the important hardware and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Displays traffic flow information, such as HTTP/HTTPS requests and responses.
- Event: Displays administrative events, such as downloading a backup copy of the configuration, and hardware failures.
- Attack: Displays attack and intrusion attempt events.

### Transport to the concentrator

The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator writes on the FortiWeb (read & write permission)
- Traffic towards the syslog concentrator must be open on `UDP 514`

#### Configure FortiWeb

**Enable logging via trigger mechanism**

1. Go to `Log&Report > Log Config > Other Log Settings`
2. Tick the boxes : Enable Attack Log / Enable Traffic Log / Enable Event Log

**Configure Syslog policies**

1. Go to `Log&Report > Log Policy > Syslog Policy`.

> To access this part of the web UI, your administrator’s account access profile must have Read and Write permission to items in the Log & Report category. For details, see Permissions.

2. Click `Create New`.

> If the policy is new, in Policy Name, type the name of the policy as it will be referenced in the configuration.

3. Click Create New.
4. In `IP Address`, enter the address of the remote Syslog server.
5. In `Port`, enter the listening port number of the Syslog server. The default is 514.
6. Click `OK`.

**Configure log destinations**

1. Go to `Log&Report > Log Config > Global Log Settings`
2. Tick the syslog box
3. Select the relevant Syslog Policy, Log Level and Facility
4. Click `Apply`

For more information please refer to the official documentation of [FortiWeb](https://docs.fortinet.com/document/fortiweb/6.1.1/administration-guide/303842/logging)

### Forward logs to Sekoia.io

The reader is invited to consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
