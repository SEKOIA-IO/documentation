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

Two methods are available to forward TEHTRIS EDR events to Sekoia.io:

- **Method 1 – API Pull**: Sekoia.io polls the TEHTRIS API to collect events. This is the standard method.
- **Method 2 – Syslog Push**: TEHTRIS pushes events directly to Sekoia.io via syslog over TLS. This method is recommended for high-volume environments where the TEHTRIS API may experience timeouts.

### Create the intake

For both methods, start by creating the intake in Sekoia.io:

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `TEHTRIS Endpoint Detection & Response`.
2. Note the **Intake key** that is generated — you will need it in the configuration steps below.

---

### Method 1: API Pull

#### Prerequisites

To forward events produced by TEHTRIS EDR to Sekoia.io, you have to:

1. Contact your TEHTRIS referent to activate the XDR Platform APIs for your tenant and ask to add the [Sekoia.io IP address](https://api.sekoia.io/outgoing-ips) to the allowlist

2. Log on the TEHTRIS XDR platform and navigate to `SOAR > Key Management`

3. Click on the button `Add`, enter the label of the API Key and select, at least, the API `Fetch Events`. You are required to create a filter (this filter may be left empty if desired).

4. At the end, click on `Create` to generate the API Key

#### Configure the intake

In the intake you created, set up the configuration with your API key and your tenant ID (most of the time, your tenant ID is the subdomain of your TEHTRIS instance; e.g. `https://{tenant_id}.tehtris.net`).

---

### Method 2: Syslog Push

In this method, TEHTRIS Level 3 support configures their platform to push logs directly to Sekoia.io's intake endpoint over syslog with TLS. No intermediate log forwarder is required.

!!! note
    This method is recommended when the volume of logs is important and the TEHTRIS API experiences regular timeouts.

#### Request syslog activation from TEHTRIS

1. Open a **Customer Service Request** on the [TEHTRIS support portal](https://support.tehtris.com) to contact the TEHTRIS Level 3 support team.
2. Ask them to enable **syslog message sending** and provide the following information:

    - **Intake key**: the intake key generated when you created your intake in Sekoia.io
    - **Address**: `intake.sekoia.io`
    - **Listen port**: TCP `10514` (with TLS)
    - **Root certificate**: `https://letsencrypt.org/certs/isrgrootx1.pem`
    - **Message format**:
      ```
      <%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"] RAW_MESSAGE
      ```
      Replace `YOUR_INTAKE_KEY` with the intake key you noted earlier.
    - **Log filter**: define the severity levels and the products to send (e.g. `Severity 4 to 9`, `Products: EDR`)

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd.md!}