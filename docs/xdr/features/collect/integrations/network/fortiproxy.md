uuid: d971c8c7-b7d0-4de1-9b5c-b58235c1d7e4
name: FortiProxy
type: intake

## Overview

FortiProxy is a web proxy that protects clients against internet threats.
In this documentation we will explain one way to collect and send FortiProxy logs to SEKOIA.IO.
- From the FortiProxy server to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

{!xdr/features/collect/integrations/generated/fortiproxy_do_not_edit_manually.md!}


## Configure

On FortiProxy appliances, differents type of logs are available. This intake currently supports :

- Traffic: Records traffic flow information, such as HTTP/HTTPS requests and responses.
- HTTP Transaction: Records HTTP transaction-related traffic log.
- DLP: Records data leak prevention events.

### Transport to the concentrator

The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator rights on FortiProxy
- Traffic towards the Rsyslog must be open on `UDP 514`

#### Configure logging to a RSYSLOG server

1. Go to `Log > Log Settings > Remote Logging and Archiving`
2. Tick the box `Send Logs to Syslog`
3. In `IP Address/FQDN`, enter the IP address or the domain name of the remote Syslog server.
4. In `Log Settings` you can customize what types of events you want to send to SEKOIA.IO. By default :
   - `Event Logging` : `All`
   - `Local Traffic Log` : `All`

5. Click `Apply`

For more information please refer to the official documentation of [FortiProxy](https://docs.fortinet.com/document/fortiproxy/7.0.0/administration-guide/707542/log-settings#Log_Settings)

### Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
