uuid: aa41faca-ae2c-487a-b8a0-7035e5dc1441
name: Control D DNS
type: intake

## Overview

Control D is a cloud DNS service that filters, blocks, and redirects DNS traffic for devices, networks, and organizations. Control D can stream the DNS queries it handles for an Organization to Sekoia.io as DNS query events. In this documentation you will learn how to receive Control D DNS query logs in Sekoia.io.

- **Vendor**: Control D
- **Supported environment**: Cloud service (SaaS)
- **Detection based on**: Telemetry
- **Supported application or feature**: DNS records

Each event is one DNS query handled by Control D. The Control D DNS format normalizes the query name and type, the response code and answered IP addresses, the client source IP, the DNS protocol, the Control D Organization, and the Control D action (`pass`, `block`, `redirect_ip`, `redirect_loc`, `fail`) together with the trigger that caused it.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**: Control D managed streaming → HTTPS → Sekoia.io Control D DNS intake

Control D operates the streaming service and pushes events directly to the Sekoia.io HTTPS intake endpoint. No customer-hosted receiver, forwarder, or Sekoia.io connector is required.

## Specification

### Prerequisites

- **Resource**:
    - A Control D Organization account eligible for SIEM log streaming
    - Full Analytics enabled on every Control D Endpoint whose DNS queries should be streamed. Control D then processes and stores detailed query data for those Endpoints, so enable it only where streaming is intended.
    - The IDs of the Control D Organization and of any Sub-Organizations to include, and the Organization's Analytics Storage Region
- **Network**:
    - None on the customer side. Control D initiates the outbound HTTPS connection to Sekoia.io.
- **Permissions**:
    - Permission to create an intake in a Sekoia.io **FRA1** workspace

!!! Note
    The Control D Analytics Storage Region is where Control D stores your DNS analytics. It is independent from the Sekoia.io region of your workspace. The Control D streaming service currently delivers to the FRA1 Sekoia.io region only.

### Transport Protocol/Method

- **Direct HTTP(S)** — Control D pushes events to Sekoia.io

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON Lines (one JSON event per line)

Control D sends `POST` requests to `https://intake.sekoia.io/plain/batch`, authenticated with the `X-SEKOIAIO-INTAKE-KEY` header and delivered over TLS with certificate verification. Each request body is JSON Lines: one JSON object per line, not a JSON array.

!!! warning
    Only the FRA1 endpoint is currently supported by the Control D streaming service. Workspaces in other Sekoia.io regions cannot receive Control D DNS events yet.

## Step-by-Step Configuration Procedure

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

Select **Control D DNS** as the intake format. Keep the intake key at hand: it is required for the activation request below.

### Instructions on the 3rd party solution

Control D activates the stream for you. There is no self-service setting to enable in the Control D dashboard.

1. [Contact Control D Support](https://controld.com/contact) while signed in to the Organization account and request **Sekoia.io SIEM log streaming**.
2. Provide the Control D Organization ID, the IDs of any Sub-Organizations to include, the Organization's Analytics Storage Region, and confirmation that the Sekoia.io workspace is in FRA1.
3. Share the intake key only through the secure exchange method agreed with Control D Support. Do not send it in a public issue, chat room, or email thread.
4. Wait for Control D Support to confirm that the stream is active.

!!! Note
    Treat the intake key as a secret. Anyone who holds it can submit events to your intake.

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

After Control D confirms activation:

1. Generate a fresh DNS query from a Control D Endpoint that has Full Analytics enabled.
2. Confirm that the query appears in the Control D Activity Log.
3. On the Sekoia.io Events page, filter on the Control D DNS intake you created and confirm that the event is present.
4. Check the event timestamp, `dns.question.name`, `observer.vendor: Control D`, and the expected Control D action in `event.action` and `controld.action`.

Raw messages arriving on the intake are not sufficient proof: the fields above must be populated, which shows that the event was parsed by the Control D DNS format.

{!_shared_content/operations_center/integrations/generated/aa41faca-ae2c-487a-b8a0-7035e5dc1441_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_aa41faca-ae2c-487a-b8a0-7035e5dc1441_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/aa41faca-ae2c-487a-b8a0-7035e5dc1441.md!}

## Troubleshooting

If no events arrive, or events stop arriving:

- Confirm that Full Analytics is still enabled on the affected Control D Endpoints.
- Confirm that the Organization and Sub-Organization IDs given to Control D Support are correct and still cover the Endpoints in question.
- Confirm that the Sekoia.io workspace is in the FRA1 region.
- Confirm that the intake is enabled in Sekoia.io and that its key has not been changed.
- If the intake key was rotated or replaced, send the new key to Control D Support through the agreed secure method, then confirm that delivery resumes with a fresh DNS query.
- If the stream still produces no events, contact Control D Support.

## Further readings

- [Control D Support](https://controld.com/contact)
- [Control D SIEM streaming overview](https://docs.controld.com/docs/siem-streaming)
- [Control D log field reference](https://docs.controld.com/docs/log-field-reference)
- The code of the Intake format is available [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Control%20D).
