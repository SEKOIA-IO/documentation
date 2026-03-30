# cyberwatch\_detection

uuid: c6a43439-7b9d-4678-804b-ebda6756db60 name: Cyberwatch Detection type: intake

### Overview

Cyberwatch is a vulnerability detection and monitoring solution.

This integration encompasses the detection logs from Cyberwatch Vulnerability Manager.

* **Vendor**: Cyberwatch
* **Supported environment**: On Premise
* **Detection based on**: Alert
* **Supported application or feature**: Vulnerability report

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
  * Administrator or Root access to the Cyberwatch Vulnerability Manager
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](cyberwatch_detection.md#overview)
* **Supported verbosity level**: Alert / Informational
* **Supported type(s) of structure**: Key-Value

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

**Forward Cyberwatch Detection Logs to Sekoia.io**

This setup guide will show you how to forward your Cyberwatch logs to Sekoia.io by means of a syslog transport channel.

**Detailed Procedure:**

1. **Prerequisites:**
   * Have an internal log concentrator.
2. **Enable Syslog Forwarding for Cyberwatch:**
   * Once configured, Cyberwatch will send hourly the latest CVEs detected to the remote Syslog server:
     1. Click `Administration`.
     2. Click `External tools`.
     3. Click `Remote Syslog server`.
   * In the Remote Syslog server configuration, provide the address, the port, and the transport to the syslog concentrator.

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/c6a43439-7b9d-4678-804b-ebda6756db60\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_c6a43439-7b9d-4678-804b-ebda6756db60\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/c6a43439-7b9d-4678-804b-ebda6756db60.md!}

### Further readings

* [Configure a remote Syslog server](https://docs.cyberwatch.fr/help/en/administration/remote_syslog_configuration/)
