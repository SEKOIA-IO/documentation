uuid: 255764ef-eaf6-4964-958e-81b9418e6584
name: Kaspersky Endpoint Security
type: intake

## Overview

**Kaspersky Endpoint Security** is an advanced security solution designed to safeguard businesses, their networks, and data against a wide array of cyber threats. Employing a multi-layered approach, it integrates various protection technologies including signature-based detection, heuristic analysis, machine learning, and real-time monitoring to detect and thwart malware, ransomware, zero-day attacks, and other threats effectively.

- **Vendor**: Kaspersky
- **Plan**: Defend Prime
- **Supported environment**: On Premise
- **Version compatibility, if applicable**:
- **Detection based on**: Endpoint Telemetry
- **Supported application or feature**: Endpoint Security

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![kaspersky_endpoint_security_architecture](/assets/integration/kaspersky_endpoint_security_architecture.png)

## Specification

### Prerequisites

- **Licence level**:
    - Proprietary
- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator rights on the Kaspersky Security Center Cloud
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: syslog
- **Supported verbosity level**: Emergency / Alert / Critical / Error / Warning / Notice / Informational / Debug

!!! Note
    Log levels are based on the taxonomy of [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Kaspersky Endpoint Security Logs to Sekoia.io

This setup guide describes how to forward events produced by **Kaspersky Endpoint Security** to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Login to Kaspersky Security Center Cloud Center:**
   - Log in to the Kaspersky Security Center Cloud Center available at `https://ksc.kaspersky.com`

2. **Enable SIEM Configuration:**

   - In the console, on the left panel, click on the spanner at the right of **Administration server**:

     ![SIEM1.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/SIEM1.png)

   - In the **General** tab, click on **SIEM** on the menu:

     ![SIEM2.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/SIEM2.png)

   - Click on **settings** to configure the forwarding (point 1):

     ![SIEM3.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/SIEM3.png)

   - Configure the forwarding:
     a. Type the address of your log concentrator in the **SIEM system server address**
     b. Type the port in **SIEM system port**
     c. Select **TLS over TCP** as the protocol
     d. Select the way to authenticate the concentrator’s certificate
     e. Click on OK

     !!! warning
         If you need to generate a custom certificate:

         ```bash
         $ openssl req -new -x509 -keyout server.key -out server.crt -nodes
         $ cat server.key server.crt > server.pem
         $ openssl x509 -in cert.crt -noout -fingerprint # copy the output
         ```

     ![SIEM4.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/SIEM4.png)

   - Check **Automatically export event to SIEM system database** (point 2):

     ![SIEM3.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/SIEM3.png)

3. **Apply Log Export Configuration on Devices:**

   - In the console, on the left menu, click on **Devices** > **Policies & profiles**:

     ![Event1.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/Event1.png)

   - For each policy **Kaspersky Endpoint Security for X**, click on the policy:

     ![Event2.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/Event2.png)

   - In the policy, select the **Event configuration** tab:

     ![Event3.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/Event3.png)

   - On the left panel, select the section **Critical**. Select all event types and click on **Mark for export to SIEM system by using Syslog**:

     ![Event4.png](/assets/operation_center/integration_catalog/endpoint/kaspersky-edr/Event4.png)

   - Select the section **Warning** and select all event types and click on **Mark for export to SIEM system by using Syslog**.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/255764ef-eaf6-4964-958e-81b9418e6584_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_255764ef-eaf6-4964-958e-81b9418e6584_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/255764ef-eaf6-4964-958e-81b9418e6584.md!}

## Further readings

- [Kaspersky Security Center Documentation](https://support.kaspersky.com/)