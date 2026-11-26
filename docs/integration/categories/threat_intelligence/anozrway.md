uuid: 519c7378-7fbb-4008-870a-535675f50cdc
name: Anozr Way
type: intake

## Overview

Anozr Way monitors the exposure of the individuals of an organization: its scans detect the data leaks that expose their professional identity and compute a risk score for each individual. At the end of each scan, the Anozr Way platform sends an alert to Sekoia.io for every new professional leak exposing an individual and for every individual whose risk score becomes high.

- **Vendor**: Anozr Way
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Leak detection and risk scoring of the individuals monitored by Anozr Way

## Specification

### Prerequisites

- **Permissions**:

    - An Anozr Way administration account allowed to manage the scans of the monitored context
    - The right to create intakes in Sekoia.io

- **Region**:

    - A Sekoia.io community hosted in the FRA1 region (`app.sekoia.io`): Anozr Way sends the events to `intake.sekoia.io`

### Transport Protocol/Method

- HTTPS push of JSON events by the Anozr Way platform, authenticated with the intake key. There is no connector to configure in Sekoia.io.

### Logs details

- **Supported functionalities**:

    - `new_pro_leaks`: a new leak exposing the professional identity of an individual, with its source, its type and dates, and the types of data it exposes, without their values (`anozrway.exposed_data_types`)
    - `new_high_risk_individual`: an individual whose risk score becomes high, with the overall score and one score per threat (account takeover, phishing, identity theft, coercion). Scores range from 0 to 10 (low below 4, medium from 4, high from 6, very high from 8)

- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Alert

### When Anozr Way sends an event

| At the end of a scan of the context... | Sent to Sekoia.io |
|---|---|
| a professional leak of an individual has not been sent yet | `new_pro_leaks`, one event per leak |
| an individual's risk score reaches the high level, for the first time or again after falling below it | `new_high_risk_individual` |
| nothing new | nothing |

The first scan after the connector is created sends every professional leak already known for the context, old ones included, and every individual already at a high risk; the next scans send only what is new. Each leak of an individual is sent once, and an individual is sent again only after their score fell below high and reached it again. Events that Sekoia.io cannot receive are retried.

## Step-by-Step Configuration Procedure

### Create the intake in Sekoia.io

1. Go to the [Intakes page](https://app.sekoia.io/operations/intakes) and click `+ Intake`.
2. Choose `Anozr Way`.
3. Give the intake a name and select its entity.
4. Copy the intake key.

### Configure Anozr Way

1. Sign in to the Anozr Way administration and open the contexts of your company.
2. On the row of the context to monitor, click the `Connectors` button, then `Sekoia`.
3. Select the `Events sent`: `New professional leaks`, `Individuals reaching a high risk`, or both.
4. Paste the intake key in the `Intake key` field and save.

!!! note
    The connector shows the date of the last event sent and, when sending fails, the date and the error. The `Connectors` button turns red while a connector is in error. Changing the intake key resets this status; deleting the connector stops the sending.

### Check the events

1. Events are sent at the end of the next scan of the context.
2. In Sekoia.io, open the [Events page](https://app.sekoia.io/operations/events) and search for the events of your Anozr Way intake, with their smart description.

{!_shared_content/operations_center/integrations/generated/519c7378-7fbb-4008-870a-535675f50cdc_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_519c7378-7fbb-4008-870a-535675f50cdc_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/519c7378-7fbb-4008-870a-535675f50cdc.md!}
