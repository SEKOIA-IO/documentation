uuid: 4970d347-495b-4f40-8e66-244abec12d8b
name: ilert
type: playbook

# ilert

![ilert](/assets/playbooks/library/ilert.png){ align=right width=150 }

ilert is an incident management platform. This module triggers alerts and manages incidents.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `integration_key` | `string` | The integration key of your ilert alert source |
| `integration_url` | `string` | URL of the ilert Events API endpoint |

## Actions

### Trigger Alert

Trigger alert to ilert

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `alert_uuid` | `string` | The Unique identifier of the alert |
| `api_key` | `string` | The Sekoia.io API-Key to read the alert content. |
| `base_url` | `string` | Base URL of Sekoia.io api (e.g. https://api.sekoia.io/). |

## Set up

## Configuration

Forward Sekoia.io alerts to ilert via the `Trigger Alert` action so your on-call teams are notified and security incidents are tracked through to resolution.

### In ilert: Create a Sekoia.io alert source

1. Go to `Alert sources` > `Alert sources` and click `Create new alert source`.

    ![Step 1](/assets/playbooks/library/setup/ilert/Step01.png)

2. Search for `Sekoia.io` in the search field, click the `Sekoia.io` tile, and then click `Next`.

    ![Step 2](/assets/playbooks/library/setup/ilert/Step02.png)

3. Give your alert source a name, optionally assign teams, and click `Next`. Then select an escalation policy by creating a new one or assigning an existing one.

    ![Step 3](/assets/playbooks/library/setup/ilert/Step03.png)

4. Select your alert grouping preference and click `Continue setup`. You may click `Do not group alerts` for now and change it later.

    ![Step 4](/assets/playbooks/library/setup/ilert/Step04.png)

5. The next page shows additional settings, such as custom alert templates or notification priority. Click `Finish setup` for now. On the final page, copy the generated `integration key` and `Sekoia.io URL`. You will use both in the next steps.

    ![Step 5](/assets/playbooks/library/setup/ilert/Step05.png)

### In Sekoia.io: Connect the ilert integration

6. In Sekoia.io, open `Integrations` from the sidebar.

    ![Step 6](/assets/playbooks/library/setup/ilert/Step06.png)

7. Search for `ilert` and select the ilert integration from the results.

    ![Step 7](/assets/playbooks/library/setup/ilert/Step07.png)

8. Click `Show accounts`, then `Connect an account`.

    ![Step 8](/assets/playbooks/library/setup/ilert/Step08.png)

9. Fill in the `Add new account` form:

    - `Give a name to this account`: a label of your choice (e.g. `ilert account`).
    - `Integration Key`: the integration key from your ilert alert source.
    - `Integration Url`: `https://api.ilert.com/api/v1/events/sekoia`.

    Click `Add account`.

    ![Step 9](/assets/playbooks/library/setup/ilert/Step09.jpg)

### In Sekoia.io: Use the Trigger Alert action in a playbook

10. Open or create a playbook in Sekoia.io, then add the `Trigger Alert` action from the ilert integration. In the `Account` tab, select the ilert account you just connected, configure the action input, and save the playbook.

    ![Step 10](/assets/playbooks/library/setup/ilert/Step10.png)

Whenever the playbook runs the `Trigger Alert` action, a new alert is created on the corresponding Sekoia.io alert source in ilert.

> `Note:` If a Sekoia.io event is sent with the `status` key set to `resolved` or `closed`, the corresponding ilert alert is resolved automatically. If the `status` key is set to `acknowledged`, the alert is acknowledged automatically.

## Extra

Module **`ilert` v1.0.0**
