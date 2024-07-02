uuid: 02a74ceb-a9b0-467c-97d1-588319e39d71
name: Citrix NetScaler / ADC
type: intake

## Overview

Citrix NetScaler / ADC (formely Citrix NetScaler) is a delivery controller and load-balancing tool that offers enhanced security and application performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_02a74ceb-a9b0-467c-97d1-588319e39d71_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/02a74ceb-a9b0-467c-97d1-588319e39d71.md!}

## Configure

### Prerequisites

- Have an internal log concentrator
- Have a NSLog server with the syslog protocol
- Have an auditing module which runs on the NetScaler appliance.

### Forward audit logs

Follow this [guide](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html) to enable syslog forwarding for audit logs.

**IMPORTANT:** please make sure `-dateFormat MMDDYYYY` is set and date is present in logs

### Forward Application Firewall logs

To enable application firewall logs forwarding, see this [guide](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server) and apply the following command to convert Application Firewall logs into CEF events:

```
set appfw settings CEFLogging on
```

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Citrix ADC.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further readings

- [Audit log forwarding](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/audit-logging/configuring-audit-logging.html)
- [Application firewall forwarding](https://support.citrix.com/article/CTX138973/how-to-send-application-firewall-messages-to-a-separate-syslog-server)
