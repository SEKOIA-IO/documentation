# cisco\_meraki\_mx

uuid: 995d7daf-4e4a-42ec-b90d-9af2f7be7019 name: Cisco Meraki MX type: intake

### Overview

Cisco Meraki MX is a multifunctional security and SD-WAN enterprise appliance with a wide set of capabilities.

* **Vendor**: Cisco
* **Supported environment**: On Premise
* **Detection based on**: Telemetry
* **Supported application or feature**: Security and SD-WAN

### High-Level Architecture Diagram

* **Type of integration**: Outbound (PUSH to Sekoia.io)
* **Schema**

{: style="max-width:100%"}

### Specification

#### Prerequisites

* **Resource**:
  * Self-managed syslog forwarder
* **Network**:
  * Outbound traffic allowed
* **Permissions**:
  * Administrator or Root access to the Cisco Meraki MX device
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](cisco_meraki_mx.md#overview)
* **Supported type(s) of structure**: Plain text
* **Supported verbosity level**: Informational

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

**Forward Cisco Meraki MX Logs to Sekoia.io**

This setup guide will show you how to provide an integration between Cisco Meraki MX events and Sekoia.io.

**Enable Syslog Forwarding:**

* Log on your Cisco Meraki MX appliance.
* Follow [this guide](https://documentation.meraki.com/General_Administration/Monitoring_and_Reporting/Syslog_Server_Overview_and_Configuration#Configure_Dashboard) to enable syslog forwarding to a syslog forwarder.

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/995d7daf-4e4a-42ec-b90d-9af2f7be7019\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_995d7daf-4e4a-42ec-b90d-9af2f7be7019\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/995d7daf-4e4a-42ec-b90d-9af2f7be7019.md!}

### Further readings

* [Cisco Meraki MX documentation](https://documentation.meraki.com/MX)
