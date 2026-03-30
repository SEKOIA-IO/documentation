# checkpoint

uuid: f0a10c21-37d1-419f-8671-77903dc8de69 name: Check Point type: intake

### Overview

Check Point’s Next Generation Firewalls (NGFWs) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth-generation cyber-attacks. Check Point’s NGFW includes 23 Firewall models optimized for running all threat prevention technologies simultaneously, including full SSL traffic inspection, without compromising on security or performance.

* **Vendor**: Check Point
* **Supported environment**: On Premise
* **Version compatibility**: R81.10
* **Detection based on**: Telemetry, Alert
* **Supported application or feature**: Firewall and threat prevention

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
  * Administrator or Root access to the Check Point device
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](checkpoint.md#overview)
* **Supported type(s) of structure**: CEF
* **Supported verbosity level**: Informational

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

The solution to collect Check Point logs leverages the [Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=\&solutionid=sk122323) method and Syslog forwarding.

**Configure Log Exporter**

* Set up the Log Exporter to send logs in the **CEF format** by following [this guide](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=\&solutionid=sk122323).

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/f0a10c21-37d1-419f-8671-77903dc8de69\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_f0a10c21-37d1-419f-8671-77903dc8de69\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/f0a10c21-37d1-419f-8671-77903dc8de69.md!}

### Further readings

* The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Check_Point).
* [Log Exporter Configuration](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=\&solutionid=sk122323)
