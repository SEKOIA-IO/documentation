uuid: 270777d7-0c5a-42fb-b901-b7fadfb0ba48
name: FortiProxy
type: intake

## Overview

FortiProxy is a web proxy that protects clients against internet threats.
In this documentation we will explain one way to collect and send FortiProxy logs to Sekoia.io.
- From the FortiProxy server to an internal syslog concentrator, then forwarded to Sekoia.io


{!_shared_content/operations_center/detection/generated/suggested_rules_270777d7-0c5a-42fb-b901-b7fadfb0ba48_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/270777d7-0c5a-42fb-b901-b7fadfb0ba48.md!}


## Configure

On FortiProxy appliances, differents type of logs are available. This intake currently supports :

- Traffic: Records traffic flow information, such as HTTP/HTTPS requests and responses.
- HTTP Transaction: Records HTTP transaction-related traffic log.
- DLP: Records data leak prevention events.

### Transport to the concentrator

The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator rights on FortiProxy
- Traffic towards the syslog concentrator must be open on `UDP 514`

#### Configure logging to a RSYSLOG server

1. Go to `Log > Log Settings > Remote Logging and Archiving`
2. Tick the box `Send Logs to Syslog`
3. In `IP Address/FQDN`, enter the IP address or the domain name of the remote Syslog server.
4. In `Log Settings` you can customize what types of events you want to send to Sekoia.io. By default :
   - `Event Logging` : `All`
   - `Local Traffic Log` : `All`

5. Click `Apply`

For more information please refer to the official documentation of [FortiProxy](https://docs.fortinet.com/document/fortiproxy/7.0.0/administration-guide/707542/log-settings#Log_Settings)

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
