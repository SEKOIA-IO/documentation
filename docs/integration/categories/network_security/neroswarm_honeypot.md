# neroswarm\_honeypot

uuid: daa275af-af18-42e5-9c8d-e3191c4ac7fa name: NeroSwarm Honeypot type: intake

### Overview

[NeroSwarm Honeypot](https://neroswarm.com/) is a Deception-as-a-Service platform designed to deploy decoy systems across networks. By detecting and monitoring malicious activity at the earliest stages of an attack, NeroSwarm lures adversaries into revealing tactics and techniques before critical assets are reached. This approach significantly reduces false positives and alert fatigue, providing security teams with real-time, high-fidelity insights into internal threats.

* **Vendor:** NeroSwarm Honeypot
* **Supported environment:** SaaS
* **Detection based on:** Alerts
* **Supported feature:** Events associated with incidents

### Step-by-Step Configuration Procedure

#### Create an Intake

1. Navigate to the [Intake page](https://app.sekoia.io/operations/intakes) in Sekoia.io.
2. Click **Create Intake** and select **NeroSwarm** from the dropdown.
3. Copy the generated **Intake Key** (this key is required in the next section).

***

#### Configure NeroSwarm to Forward Logs

1. [Log in](https://neroswarm.com/auth/login) to the NeroSwarm Honeypot dashboard.
2. From the Honeypot List, click **Logs** for the honeypot to integrate.
3. In the Log List, click **Log Management**.
4.  In the **Log Management** modal:

    1. Select **Sekoia.io** from the integration options.
    2. Paste the **Intake Key** obtained earlier.
    3. Click **Confirm** to save changes.

    > **Note:** It takes around 2 minutes for the changes to be reflected.

#### Verify Inbound Events

Once the configuration has propagated (about 2 minutes later), navigate to the [Events page](https://app.sekoia.io/events) in Sekoia.io. Incoming events from NeroSwarm will appear here, ready for investigation and advanced threat correlation.

{!\_shared\_content/operations\_center/integrations/generated/daa275af-af18-42e5-9c8d-e3191c4ac7fa\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_daa275af-af18-42e5-9c8d-e3191c4ac7fa\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/daa275af-af18-42e5-9c8d-e3191c4ac7fa.md!}
