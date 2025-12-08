uuid: e44114c6-4c81-47b9-9298-3fe268b30f84
name: New Relic
type: playbook

# New Relic

![New Relic](/assets/playbooks/library/new-relic.png){ align=right width=150 }

New Relic is a cloud-based observability platform delivering full-stack monitoring for applications, infrastructure, logs and metrics. It ingests real-time telemetry—metrics, logs, traces and events—to help DevOps and engineering teams detect anomalies and troubleshoot faster. By transforming raw data into actionable insights, New Relic drives performance optimization and seamless digital experiences.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Base URL |
| `api_key` | `string` | API key |

## Actions

### Make NRQL query

Query New Relic data with NRQL

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `account_ids` | `array` | Account identifiers to use |
| `query` | `string` | The NRQL to execute |

## Set up

## How to create an API Key

1. Log in to the New Relic Console
2. Click your avatar

    ![Step 1](/assets/playbooks/library/setup/new-relic/apikey_step_01.png){: style="max-width:100%"}

3. Go to `API Keys`

    ![Step 2](/assets/playbooks/library/setup/new-relic/apikey_step_02.png){: style="max-width:100%"}

4. Click `Create a Key`

    ![Step 3](/assets/playbooks/library/setup/new-relic/apikey_step_03.png){: style="max-width:100%"}

5. Select the account to use
6. Select `User` as Key type
7. Type a name for the Key
8. Type a notes (Optional)
9. Click `Create a key`

    ![Step 4](/assets/playbooks/library/setup/new-relic/apikey_step_04.png){: style="max-width:100%"}

10. Click `Copy Key` and save it

    ![Step 5](/assets/playbooks/library/setup/new-relic/apikey_step_05.png){: style="max-width:100%"}



## Extra

Module **`New Relic` v1.0.1**