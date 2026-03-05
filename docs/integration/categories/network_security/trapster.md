uuid: ead80c4a-9305-4e31-9a1b-9a5dd1978d2d
name: Trapster
type: intake

## Overview

Trapster deploys honeypots across your network to detect lateral movements, malicious scans, and insider threats. These digital decoys have no legitimate use, so any interaction immediately signals suspicious activity. With near-zero false positives and instant alerts, security teams can quickly identify and investigate potential intrusions. You also receive alerts for any attempted connection to the honeypots as well as the use of honeytokens or breadcrumbs, helping reduce overall detection time.

- **Vendor**: Ballpoint
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Honeypot alerts (lateral movement, scans, honeytokens, breadcrumbs, threats)

## Configure

This setup guide describes how to forward events from Trapster to Sekoia.io via webhook.

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes).
2. Click  **+ New Intake**.
3. Select the format **Trapster**.
4. Copy the **intake key** created(you will need it in the next step).

### Configure Trapster

1. Log in to your **Trapster console**.
2. Navigate to **Settings**.
3. Select **Webhooks**.
4. Click **+ Add** to create a new webhook.
5. Choose **Sekoia** as the webhook type.
6. Enter a name for the webhook.
7. Paste the **Intake Key** (Token) copied from Sekoia.io.
8. Click save to apply the configuration.

![Save your configuration](/assets/operation_center/integration_catalog/network_security/trapster/trapster_step01.png)

9. Test the integration by clicking on the three-dot menu next to the webhook you created and then **Send test**.

![Test your webhook](/assets/operation_center/integration_catalog/network_security/trapster/trapster_step02.png)

Your events will then be available on the [Events page](https://app.sekoia.io/operations/events).

{!_shared_content/operations_center/integrations/generated/ead80c4a-9305-4e31-9a1b-9a5dd1978d2d_sample.md!}

{!_shared_content/operations_center/integrations/generated/ead80c4a-9305-4e31-9a1b-9a5dd1978d2d.md!}