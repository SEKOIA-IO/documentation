# Push Sekoia.io IOCs to Palo Alto XSIAM Collection

This guide explains how to build and configure a Sekoia.io playbook that:

1. Consumes your Sekoia CTI feed of IOCs (Indicators of Compromise).
2. Transforms them into the JSON format expected by Palo Alto XSIAM.
3. Pushes them via API into a XSIAM Collection for detection.

---

## Prerequisites

1. A **Sekoia Intelligence License** and a user account with access to **Playbooks** feature.
2. A **Palo Alto XSIAM Standard API Key** and its associated **XSIAM API ID**.

---

## Playbook Overview

The playbook has **3 nodes**:

1. **Feed Consumption** (Trigger)
   Pulls the latest STIX objects (IOCs) from your custom Sekoia feed.
2. **Transform Sekoia STIX to XSIAM** (Action)
   Converts STIX patterns and metadata into the JSON schema expected by XSIAM.
3. **Send Batch to XSIAM** (Action)
   Calls the XSIAM `indicators/insert_jsons` API to inject indicators into a Collection.

![xsiam_playbook_workflow](/assets/intelligence_center/XSIAM/xsiam_playbook_workflow.png){:style="max-width:100%"}

---

## 1. Create a Custom Feed

1. In Sekoia.io, navigate to **Observe ➔ Feeds**.
2. Click **+ New feed**.
3. Enter a **Title** (e.g. “XSIAM IOC Feed”).
4. Under **Object types**, select **Indicator**.
5. Under **Observable types**, check:
   - Directory
   - Domain name
   - File
   - Filename
   - IPv4 address
6. Keep the **Feed format** as **JSON (default)**.
7. Click **Save**.

![xsiam_custom_feed](/assets/intelligence_center/XSIAM/xsiam_custom_feed.png){:style="max-width:100%"}

8. In the feed details view, click **Copy Feed ID**.
   You will need this in the playbook configuration.

![xsiam_custom_feed_copy_id](/assets/intelligence_center/XSIAM/xsiam_custom_feed_copy_id.png){:style="max-width:100%"}

---

## 2. Create the Playbook from the Template

1. Go to **Configure ➔ Playbooks**.
2. Click **+ New Playbook**.
3. Choose **Use a template**.
4. Search for **xsiam**.
5. Select **Push Sekoia.io IOCs to Palo Alto XSIAM Collection**.
6. Click **Save**.

---

## 3. Configure Each Node

### 3.1 Feed Consumption (Node 0)

- **Module**: CTI Feed Consumption
- **Account**: None
- **Configuration**:
  - **Batch Size Limit**: `200`
  - **Feed ID**: Paste the Feed ID from step 1 (e.g. `feed--xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).
  - **Modified After**: an RFC-3339 timestamp (e.g. `2025-06-12T23:20:50.52Z`). We recommend to start with a week of history to avoid disruption of SOC Analysts processes.
  - **Resolve Sources**: `true`

![xsiam_custom_feed_consumption_configuration](/assets/intelligence_center/XSIAM/xsiam_custom_feed_consumption_configuration.png){:style="max-width:100%"}

> This trigger outputs `{{ node.0.stix_objects_path }}`, a JSONPath to the STIX objects array.

### 3.2 Transform Sekoia STIX to XSIAM (Node 1)

- **Module**: Transform Sekoia STIX to XSIAM
- **Source code**: is availabe [here](https://github.com/SEKOIA-IO/automation-library/blob/main/PaloAltoXSIAM/xsiam/stix_to_xsiam.py)
- **Account**: None
- **Configuration**: Defaults are ready to use—no mandatory overrides.

#### Built-in Mappings

1. **Observable → XSIAM field**

   | Sekoia type   | XSIAM field  |
   |--------------:|-------------:|
   | file          | HASH         |
   | filename      | FILENAME     |
   | directory     | PATH         |
   | domain-name   | DOMAIN_NAME  |
   | ipv4-addr     | IP           |

2. **Severity mapping**

   - `confidence 0–39` → LOW
   - `confidence 40–79` → MEDIUM
   - `confidence 80–100` **and** kill_chain_phases ∈ {exploitation, installation, command-and-control, actions-on-objectives} → HIGH
   - Others → INFO

3. **Reputation**: all selected observables → BAD
4. **Reliability** based on confidence:

   | Confidence | Reliability |
   |-----------:|------------:|
   | 80–100     | A           |
   | 60–79      | B           |
   | 40–59      | C           |
   | 20–39      | D           |
   | 0–19       | E           |
   | —          | F / G (unused) |

5. **Comment**: Valid from {valid_from} AND STIX Pattern: {pattern}
6. **Expiration date**: uses `valid_until` date converted to epoch (ms).
7. **Class override**: uses the Sekoia indicator ID, enabling a link back to
`https://app.<region_id>.sekoia.io/objects/indicator--<indicator-id>`.

#### UI Overrides

You can override these arguments in the node’s UI:

| Parameter            | Default                                         | Notes                                 |
|----------------------|-------------------------------------------------|---------------------------------------|
| class_override       | `{id}`                                          | Open string, ≤36 characters           |
| comment              | `Valid from {valid_from} AND STIX Pattern: {pattern}` | Free text                 |
| severity_mapping     | this field is *empty* but is applying the mapping explained in section **3.2.2.Severity mapping**                                         | Use any of: LOW, MEDIUM, HIGH, CRITICAL, INFO |
| reliability_mapping  | this field is *empty* but is applying the mapping explained in section **3.2.4.Reliabilit**                                        | Use any of: A, B, C, D, E, F, G       |
| stix_objects_path    | `{{ node.0.stix_objects_path }}`                | JSONPath to STIX objects available in Sekoia             |

**Examples**

- Force all severities to LOW (i.e. all Confidence values highier than 0 will be traduced in "LOW"):

![xsiam_override_severity](/assets/intelligence_center/XSIAM/xsiam_override_severity.png){:style="max-width:100%"}

- Custom reliability bands:

   | Confidence | Reliability |
   |-----------:|------------:|
   | 75–100     | A           |
   | 50–74      | B           |
   | 0–49       | C           |
   | —          | D / E / F / G (unused) |

![xsiam_override_reliability](/assets/intelligence_center/XSIAM/xsiam_override_reliability.png){:style="max-width:100%"}

> After running, `{{ node.1.data }}` contains a list of XSIAM-ready JSON objects.

### 3.3 Send Batch to XSIAM (Node 2)

- **Module**: Send batch to XSIAM
- **Account**: None
- **Configuration**:
- **Method**: `POST`
- **URL**:
 ```
 https://<your-region>.xdr.fa.paloaltonetworks.com/public_api/v1/indicators/insert_jsons
 ```
 Replace `<your-region>` with your XSIAM region.
- **Headers**:
 ```json
 {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": "<REPLACE_WITH_API_KEY>",
   "x-xdr-auth-id": "<REPLACE_WITH_API_ID>"
 }
 ```
- **JSON payload**:
 ```json
 {
   "request_data": {{ node.1.data }},
   "validate": true
 }
 ```
- **fail_on_http_error**: `true`
- **verify_ssl**: `false` (set `true` in production)

> This sends the transformed JSON to your XSIAM Collection.

---

## 4. Finalize and Test

1. **Save** and **Activate** the playbook.
2. Wait for the next scheduled run (a few seconds).
3. In the playbook UI, check **Trigger logs** for messages like:

```
Start SEKOIA feed consumption trigger
Fetched objects in X seconds
Fetched 200 objects from the feed
```

4. Verify the run status under **Runs**.

![xsiam_run_success](/assets/intelligence_center/XSIAM/xsiam_run_success.png){:style="max-width:100%"}

5. In Palo Alto XSIAM, go to **Collections ➔ Indicators** to confirm your IOCs arrived.

---

## Known Limitations

- The **DOMAIN_NAME** indicator type in XSIAM does _not_ support URL observables. URLs are omitted from the custom feed.
- The **IP** indicator type does _not_ support port information from network‐traffic STIX patterns. Only the IPv4 address is extracted, which may lose context. Ports are preserved in the comment field.

---

## External Resources

- Palo Alto XSIAM API [documentation](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/4qm63q1zsrw8l-insert-simple-indicators-json)