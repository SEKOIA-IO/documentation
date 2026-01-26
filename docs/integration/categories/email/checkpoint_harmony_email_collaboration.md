uuid: 71bd28dc-163d-4262-9d50-84ec4a9cef65
name: Checkpoint Harmony Email and Collaboration
type: intake

## Overview

Check Point Harmony Email & Collaboration Suite Security delivers unified protection for email, cloud storage and collaboration apps (Office 365, Google Workspace, Teams, Slack).
Advanced anti-phishing, zero-day malware sandboxing, URL defense and data loss prevention stop BEC, ransomware and data leaks.
Centrally managed with granular policies, threat intelligence and real-time insights for seamless workspace security.

- **Vendor**: Check Point
- **Supported environment**: SaaS
- **Detection based on**: Telemetry, Alert
- **Supported application or feature**: Email gateway, Cloud security

### Supported events

This integration supports the following event types:

- `phishing`
- `malware`
- `suspicious malware`
- `dlp`
- `anomaly`
- `shadow_it`
- `malicious_url_click`
- `malicious_url`
- `alert`

## Configure

#### How To Set Up The Forwarding

1. Log in to the Checkpoint Harmony portal

2. Go to the Checkpoint Harmony Email & Collaboration interface

3. On the left panel, navigate to `Security Settings` > `Security Engines`

    ![Step 01](/assets/integration/checkpoint_hec/step_01.png)

4. Scroll down to the `SIEM Integration` section

5. Click `Configure`

    ![Step 02](/assets/integration/checkpoint_hec/step_02.png)

6. Select `HTTP Collector` as **Transport**

7. Type `https://intake.sekoia.io/plain` as **HTTP Collector URL**

    ![Step 03](/assets/integration/checkpoint_hec/step_03.png)

8. Select `JSON` as **Format**

9. Enable `Add custom header`

10. Type `X-SEKOIAIO-INTAKE-KEY` as the **Custom header name**

11. Type your intake key as the **Custom header value**

12. Click `Save`

    ![Step 04](/assets/integration/checkpoint_hec/step_04.png)

#### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Checkpoint Harmony Email & Collaboration`.
2. Copy the intake key that was generated.
3. Use this intake key in the Checkpoint Harmony configuration as described above.

{!_shared_content/operations_center/integrations/generated/71bd28dc-163d-4262-9d50-84ec4a9cef65_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_71bd28dc-163d-4262-9d50-84ec4a9cef65_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/71bd28dc-163d-4262-9d50-84ec4a9cef65.md!}
