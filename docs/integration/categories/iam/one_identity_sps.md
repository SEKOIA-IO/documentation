uuid: 94d4ef59-638c-4230-b38d-e4a1381db8ed
name: One Identity Safeguard for Privileged Sessions
type: intake

## Overview

One Identity Safeguard for Privileged Sessions (SPS) is a core module of the One Identity Safeguard suite that focuses on securing, monitoring, and auditing privileged access to critical systems. It acts as a transparent gateway between administrators and target systems, enabling organizations to control who accesses sensitive resources, record all activity, and detect suspicious behavior in real time.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: One Identity
- **Supported environment**: On prem
- **Version compatibility**: 7.4 and later
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs


## Configure

This setup guide will show you how to forward your One Identity SPS logs to Sekoia.io.

### Prerequisites

- Have an internal log concentrator (e.g., Sekoia.io forwarder,  Rsyslog, Syslog-NG, etc.) to receive the logs from One Identity SPS and forward them to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `One Identity SPS`.

### Configure One Identity SPS to forward logs

1. Log in to the One Identity Safeguard for Privileged Sessions console.
2. Go to `Basic Settings` > `Management`.

![Step 1](/assets/integration/iam/oneidentity_sps/Step 01.webp){: style="max-width:100%"}

3. Click the `Universal SIEM Forwarding` panel to expand it.

![Step 2](/assets/integration/iam/oneidentity_sps/Step 02.webp){: style="max-width:100%"}

4. Select the `Enable` checkbox.

![Step 3](/assets/integration/iam/oneidentity_sps/Step 03.webp){: style="max-width:100%"}

5. Click `+` to add a new SIEM destination.

![Step 4](/assets/integration/iam/oneidentity_sps/Step 04.webp){: style="max-width:100%"}

6. Name the destination (e.g., `Sekoia.io`).
7, In the `Address` field, enter the IP address or hostname of your internal log concentrator.
8. In the `Port` field, enter the port number for the intake
9. Select `CEF` as the `Format`.
10. Click `Commit` to apply the changes.

![Step 5](/assets/integration/iam/oneidentity_sps/Step 05.webp){: style="max-width:100%"}

{!_shared_content/operations_center/integrations/generated/94d4ef59-638c-4230-b38d-e4a1381db8ed.md!}

{!_shared_content/integration/detection_section.md!}


{!_shared_content/operations_center/detection/generated/suggested_rules_94d4ef59-638c-4230-b38d-e4a1381db8ed_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/94d4ef59-638c-4230-b38d-e4a1381db8ed.md!}

## Further readings

- [One Identity Safeguard for Privileged Sessions - Forwarding data to third-party systems](https://support.oneidentity.com/fr-fr/technical-documents/one-identity-safeguard-for-privileged-sessions/7.4/administration-guide/30#TOPIC-2065507)
