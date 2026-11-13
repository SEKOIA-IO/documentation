uuid: 3960e1fc-1b9b-435e-bc5d-7a3c888a6b03
name: Nextron THOR Cloud
type: intake

## Overview

[THOR](https://www.nextron-systems.com/thor/) is Nextron Systems' APT scanner. It hunts for hacking activity, malware and other threats on endpoints with thousands of YARA and Sigma rules, anomaly checks and IOC matching. THOR Cloud and THOR Cloud Lite run THOR scans on your endpoints and keep their results.

This integration collects the results of finished THOR Cloud scans. A connector polls the THOR Cloud API, downloads the JSON log of every finished scan once, and sends each log line to the intake, which parses the THOR JSON log format v2.

- **Vendor**: Nextron Systems
- **Supported environment**: SaaS
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: THOR scan results: YARA and Sigma matches, IOC matches, files, processes, network connections, registry, services, event logs

## Configure

### Create an API key in THOR Cloud

Use an account API key: it isn't tied to a person, can be created without an expiration date, and only gets the permissions you give it.

1. Log in to THOR Cloud or THOR Cloud Lite and open **Settings → Account API Keys**.
2. Click **+ Create**, give the key a name, and leave **Allow CIDRs**, **Deny CIDRs** and **Roles** empty. The connector runs on Sekoia's infrastructure, so an IP allow list would block it.

    ![Create an account API key](/assets/instructions/nextron_thor_cloud/step01-create-account-api-key.png)

3. Leave **Administrator** unchecked. The connector only needs **List Scans** and **Read Logs**:

    - To collect scans from every campaign, including campaigns created later, check both under **Access to all campaigns**.

        ![Permissions on all campaigns](/assets/instructions/nextron_thor_cloud/step02-api-key-all-campaigns.png)

    - To collect scans from specific campaigns only, add each campaign under **Per-campaign Permissions** and check both permissions in its row. Enter the same campaign UUIDs in the **Campaigns** setting of the connector.

        ![Permissions on a single campaign](/assets/instructions/nextron_thor_cloud/step03-api-key-single-campaign.png)

4. Click **Create** and copy the key.

!!! note
    The playbook action **Generate THOR Cloud launcher** needs more permissions: **Run Scans**, and **Create Campaigns** under **Administrative** to create campaigns. See the [THOR Cloud action library](/integration/action_library/thor-cloud.md).

### Connect the account

1. In Sekoia, open **Configure → Integrations**, search for **THOR Cloud** and open it.
2. Click **Connect an account**, give the account a name, paste the API key into **Api Key** and click **Save**. Sekoia checks the key against THOR Cloud and THOR Cloud Lite.

    ![Connect the THOR Cloud account](/assets/instructions/nextron_thor_cloud/step04-connect-account.png)

For more information, see [Manage accounts](/xdr/features/automate/manage-accounts.md).

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format **Nextron THOR v2**.
2. Choose the community and entity, then select the account you connected and set the connector options:

    | Setting | Default | Description |
    |---|---|---|
    | **Product** | `thor_cloud_lite` | `thor_cloud` for THOR Cloud, `thor_cloud_lite` for THOR Cloud Lite. It must match the service of the API key. |
    | **Campaigns** | empty | Comma-separated campaign UUIDs to collect. Leave it empty to collect all campaigns the key can access. |
    | **Days Back** | `7` | Only scans created within this many days are collected. Use a larger value once to import older scans. |
    | **Polling Interval** | `60` | Minutes between two polls. |

    ![Connector configuration](/assets/instructions/nextron_thor_cloud/step05-connector-configuration.png)

3. Save the intake and make sure it's switched on.

The connector only collects scans that have finished (status *successful* or *failed*) and sends each scan only once, also across restarts and when **Days Back** is raised. Scans whose logs are encrypted with the account's public key can't be parsed and are skipped with a warning in the connector logs.

!!! note
    The connector forwards the whole scan log, including the `Info` and `Notice` lines that describe the scan, not only the findings. A single scan can produce thousands of events. Use **Campaigns** to limit collection to the campaigns you need.

{!_shared_content/operations_center/integrations/generated/3960e1fc-1b9b-435e-bc5d-7a3c888a6b03_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_3960e1fc-1b9b-435e-bc5d-7a3c888a6b03_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3960e1fc-1b9b-435e-bc5d-7a3c888a6b03.md!}

## Further readings

- [How to integrate THOR Cloud into Sekoia](https://github.com/NextronSystems/guides/blob/master/sekoia-integrations/docs/sekoia-thor-cloud-integration-guide.md): Nextron's detailed guide, with troubleshooting and example detection rules
- [THOR documentation](https://thor-manual.nextron-systems.com/)
