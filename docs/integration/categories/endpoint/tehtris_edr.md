uuid: 8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd
name: TEHTRIS Endpoint Detection & Response
type: intake

## Overview

TEHTRIS EDR is a security product to monitor, detect and mitigate threats on endpoints. It reduces the attack surface and prevents attacks.

This setup guide shows how to forward events produced by TEHTRIS EDR to Sekoia.io.

- **Vendor**: TEHTRIS
- **Supported environment**: On Cloud
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: File monitoring, Process monitoring and Anti-virus


## Configure

### Prerequisites

TEHTRIS EDR supports two collection modes:

- API polling, which remains supported
- Syslog push mode, which is recommended by TEHTRIS for high-volume environments

To forward events produced by TEHTRIS EDR to Sekoia.io with the API mode, you have to:

1. Contact your TEHTRIS referent to activate the XDR Platform APIs for your tenant and ask to add the [Sekoia.io IP address](https://api.sekoia.io/outgoing-ips) to the allowlist

2. Log on the TEHTRIS XDR platform and navigate to `SOAR > Key Management`

3. Click on the button `Add`, enter the label of the API Key and select, at least, the API `Fetch Events`. You are required to create a filter (this filter may be left empty if desired).

4. At the end, click on `Create` to generate the API Key

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `TEHTRIS Endpoint Detection & Response`.
2. Choose the collection mode that matches your deployment:

#### API mode

Set up the intake configuration with your API key and your tenant ID (most of time, your tenant ID is the subdomain of your TEHTRIS instance; eg: `https://{tenant_id}.tehtris.net`).

#### Syslog push mode

For large environments, TEHTRIS recommends enabling syslog push mode through their Level 3 support team.

1. Copy the intake key of the newly created intake.
2. Open a Customer Service Request on the TEHTRIS support portal.
3. Ask TEHTRIS Level 3 support to enable syslog sending messages for your tenant.
4. Provide the following values:
   - Destination address: `intake.sekoia.io`
   - Destination port: `10514`
   - Transport: `TCP with TLS`
   - Root certificate: `https://letsencrypt.org/certs/isrgrootx1.pem`
   - Intake key: the intake key copied from Sekoia.io
   - Filter for the logs to send, for example `Severity 4 to 9`
   - Product to forward: `EDR`

This intake is designed for TEHTRIS EDR events. If you need to ingest other TEHTRIS product logs, configure a dedicated intake that supports those event types.

Use the following message template:

```text
1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"] RAW_MESSAGE
```

The current parser expects the following elements to be present in syslog push messages:

- the RFC5424 prefix starting with version `1`
- the literal `LOG`
- the structured data block `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
- the JSON event appended after the structured data block

Only replace `YOUR_INTAKE_KEY` with your Sekoia.io intake key. The `LOG`, `SEKOIA@53288` and `intake_key` tokens must stay unchanged for the parser to detect the syslog envelope correctly.

!!! note
   If the TEHTRIS environment produces a large volume of events, prefer syslog push mode over API polling to avoid recurring API timeouts.

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd.md!}

### Verify event ingestion

1. In Sekoia.io, open the intake and confirm that events are being received.
2. Check that parsed events contain expected fields such as `event.module`, `event.reason`, `agent.id`, and `host.hostname`.
3. If no events are received in syslog mode, verify that the syslog template is unchanged and still contains:
   - `LOG`
   - `[SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"]`
   - the TEHTRIS JSON payload appended after the structured data block