uuid: 255764ef-eaf6-4964-958e-81b9418e6584
name: Kaspersky Endpoint Security
type: intake

## Overview

**Kaspersky Endpoint Security** is an advanced security solution designed to safeguard businesses, their networks, and data against a wide array of cyber threats. Employing a multi-layered approach, it integrates various protection technologies including signature-based detection, heuristic analysis, machine learning, and real-time monitoring to detect and thwart malware, ransomware, zero-day attacks, and other threats effectively.

{!_shared_content/operations_center/detection/generated/suggested_rules_255764ef-eaf6-4964-958e-81b9418e6584_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/255764ef-eaf6-4964-958e-81b9418e6584.md!}

## Configure

This setup guide describe how to forward events produced by **Kaspersky Endpoint Security** to Sekoia.io.

### Prerequisites

- Have an internal log concentrator (Syslog)

### Enable Syslog forwarding

**Kaspersky** can send network security event and audit logs to a Syslog server. To configure forwarding of event logs to a Syslog server please follow this [guide](https://support.kaspersky.com/IoTSecureGateway/2.0/en-US/194359.htm)

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Kaspersky Endpoint Security**.
