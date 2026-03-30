# cisco\_ios

uuid: 700f332f-d515-4bc5-8a62-49fa5f2c9206 name: Cisco IOS type: intake

### Overview

Cisco IOS is a network operating system for Cisco ASR routers and Cisco Catalyst switches.

* **Vendor**: Cisco
* **Supported environment**: On Premise
* **Version compatibility**: 15.5 (Latest version as of now)
* **Detection based on**: Telemetry
* **Supported application or feature**: Network management and operation

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
  * Administrator or Root access to the Cisco IOS device
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](cisco_ios.md#overview)
* **Supported type(s) of structure**: Plain text
* **Supported verbosity level**: Informational

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

**Forward Cisco IOS Logs to Sekoia.io**

This setup guide will show you how to provide an integration between Cisco IOS events and Sekoia.io.

**Enable Syslog Forwarding:**

* Log on your Cisco appliance.
* Follow [this guide](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html#wp1055038) to enable syslog forwarding to a managed syslog forwarder.

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/700f332f-d515-4bc5-8a62-49fa5f2c9206\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_700f332f-d515-4bc5-8a62-49fa5f2c9206\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/700f332f-d515-4bc5-8a62-49fa5f2c9206.md!}

### Further readings

* [Cisco System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html)
