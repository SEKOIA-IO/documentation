# trellix\_atd

uuid: ff575606-1cec-4d9f-8e08-d02dd9100af8 name: Trellix Advanced Threat Defense type: intake

### Overview

The Advanced Threat Defense Appliances are purpose-built, scalable, and flexible high-performance servers designed to analyze suspicious files for malware.

* **Vendor**: Trellix
* **Supported environment**: On Premise
* **Detection based on**: Telemetry
* **Supported application or feature**: Application logs

### High-Level Architecture Diagram

* **Type of integration**: Outbound (PUSH to Sekoia.io)
* **Schema** {: style="max-width:100%"}

### Specification

#### Prerequisites

* **Resource**:
  * Self-managed syslog forwarder
* **Network**:
  * Outbound traffic allowed
* **Permissions**:
  * Root access to the Trellix ATD web interface
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](trellix_atd.md#overview)
* **Supported type(s) of structure**: Syslog
* **Supported verbosity level**: Informational

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the vendor.

### Step-by-Step Quick Configuration Procedure

1. Log on to the Advanced Threat Defense web interface.
2. Click **Manage** → **ATD Configuration** → **Syslog**, then select **Enable Logging**
3. In the Statistic to Log section, select the entries that suits your needs.

> Note: When HTTPS Session Log is enabled, Advanced Threat Defense web performance is impacted.

4. From the drop-down menu, select TCP

> Note, if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder, modify the configuration accordingly

5. Click **Enable Syslog**
6. Type in the IP and port of the forwarder you want the logs sent to.
7. Click **Test Connection** and expect a "Test connection successful" message.
8. Click **Submit**

!!! Note If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your vendor. We also welcome any suggestions for improving our documentation to better serve your needs.

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/ff575606-1cec-4d9f-8e08-d02dd9100af8\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_ff575606-1cec-4d9f-8e08-d02dd9100af8\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/ff575606-1cec-4d9f-8e08-d02dd9100af8.md!}
