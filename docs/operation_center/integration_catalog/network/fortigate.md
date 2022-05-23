uuid: 5702ae4e-7d8a-455f-a47b-ef64dd87c981
name: fortigate
type: intake

## Overview

The range of Fortigate firewalls is a complete appliance solution whose security functions are highly developed. The firewalls run on the FortiOS operating system.

{!operation_center/integration_catalog/generated/fortigate_do_not_edit_manually.md!}


## Configure

In this documentation we explain one way to collect and send Fortigate logs to SEKOIA.IO.

- From the Fortigate machine to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

## Fortigate logs

On Fortigate appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Local out traffic, Denied traffic, Allowed traffic
- Web
- Url-Filtering
- VPN

## Transport to the concentrator

### Prerequisites

The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator writes on the Fortigate
- Traffic towards the Rsyslog must be open on `TCP/514`

### Configure Fortigate

The first step is to configure Fortigate to log the awaited traffic.
You can configure FortiOS to send log messages to remote syslog servers in standard, CSV or CEF (Common Event Format) format. These three formats are accepted by the SEKOIA.IO intake.
To enable syslog, log into the CLI and enter the following commands:

```bash
config log syslogd setting
set status enable
set port 514
set mode reliable
set server [IP address of syslog server]
set facility user
set format rfc5424
end
```

Most FortiGate features are enabled for logging by default. Ensure they are enabled by executing the following command:

```bash
show full-configuration
```

Make sure the Traffic, Web and URL Filtering features are enabled for logging with the following commands:

```bash
config log syslogd filter
set forward-traffic enable
set local-traffic enable
set multicast-traffic enable
....
set vpn enable
set web enable
set url-filter enable
end
```

With some Fortigate appliance, it may not be possible to do the above configuration through the command line. An alternative method is to use the graphical interface and go to the `Log Settings` menu. From there you can choose every logging options within `Event Logging` and `Local Traffic Log` except for the `Denied` options.

Then in order to use CEF format, use the following commands :

```bash
config log syslogd setting
set format cef
end
```

## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
