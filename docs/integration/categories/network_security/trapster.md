# trapster

uuid: 517e223d-07a1-4d61-b508-c4c5587146d6 name: Trapster type: intake

### Overview

Trapster deploys honeypots across your network to detect lateral movements, malicious scans, and insider threats. These digital decoys have no legitimate use, so any interaction immediately signals suspicious activity. With near-zero false positives and instant alerts, security teams can quickly identify and investigate potential intrusions. You also receive alerts for any attempted connection to the honeypots as well as the use of honeytokens or breadcrumbs, helping reduce overall detection time.

!!! Warning Important note - This format is currently in beta. We highly value your feedback to improve its performance.

* **Vendor**: Ballpoint
* **Supported environment**: SaaS
* **Detection based on**: Alert
* **Supported application or feature**: Honeypot alerts (lateral movement, scans, honeytokens, breadcrumbs, threats)

### Configure

This setup guide describes how to forward events from Trapster to Sekoia.io via webhook.

#### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes).
2. Click **+ New Intake**.
3. Select the format **Trapster**.
4. Copy the **intake key** created(you will need it in the next step).

#### Configure Trapster

1. Log in to your **Trapster console**.
2. Navigate to **Settings**.
3. Select **Webhooks**.
4. Click **+ Add** to create a new webhook.
5. Choose **Sekoia** as the webhook type.
6. Enter a name for the webhook.
7. Paste the **Intake Key** (Token) copied from Sekoia.io.
8. Click save to apply the configuration.
9. Test the integration by clicking on the three-dot menu next to the webhook you created and then **Send test**.

Your events will then be available on the [Events page](https://app.sekoia.io/operations/events).

{!\_shared\_content/operations\_center/integrations/generated/517e223d-07a1-4d61-b508-c4c5587146d6\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_517e223d-07a1-4d61-b508-c4c5587146d6\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/517e223d-07a1-4d61-b508-c4c5587146d6.md!}
