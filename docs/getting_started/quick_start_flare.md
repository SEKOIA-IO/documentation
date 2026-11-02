# Get started with Flare in Sekoia Digital Risk

Use this quick start to configure Flare, send Flare events to Sekoia, activate detections, and investigate a Flare alert. The workflow is divided into four objectives so you can complete the setup progressively.

## At a glance

| Objective | What you do | Result |
| --- | --- | --- |
| 1. Configure Flare | Add users, create identifiers, define policies, and create an API key. | Flare monitors the data that matters to your organization. |
| 2. Send events to Sekoia | Create a Flare Events intake and configure the connector. | Flare events arrive in Sekoia as events. |
| 3. Generate Sekoia alerts | Activate detection rules for Flare Events. | Matching Flare events generate Sekoia alerts. |
| 4. Investigate an alert | Open the related Flare event from `event.url`. | You can review the source event in Flare. |

This quick start covers the first configuration path. For the complete event catalog, raw event samples, and parser details, see [Flare Events](/integration/categories/threat_intelligence/flare_events.md).

## Before you start

Make sure that:

- Sekoia has provisioned your Flare tenant.
- You have received an invitation to create your Flare account.
- You have permission to manage the required settings in Flare.
- You have permission to create intakes and activate detection rules in Sekoia.

!!! note "Flare tenant provisioning"

    Sekoia creates the Flare tenant and adds the email address provided during onboarding. If you do not receive the invitation email, contact your Sekoia commercial contact.

## Objective 1: Configure Flare

Configure the Flare tenant before you create the Sekoia intake. These settings determine which data Flare collects and which events it sends to the tenant feed.

### Add users

Add the members of your organization who need access to Flare.

!!! note "Required Flare permission"

    Only Flare members with the Organization Administrator role can open the **Team** page and invite organization members.

1. Sign in to your Flare tenant.
2. Go to **Settings > Team**.
3. Enter the user's first name, last name, and email address.
4. Set the organization and tenant permissions for the user.
5. Click **Create** to send the invitation.

For more information, see the [Flare Team documentation](https://docs.flare.io/team).

### Create identifiers

Flare uses identifiers to monitor data related to your organization, assets, or people.

1. Go to **Identifiers**.
2. Create the identifiers that you want to monitor.
3. Review the identifiers to confirm that they match your monitoring scope.

For more information, see the [Flare documentation about identifiers](https://docs.flare.io/identifiers).

### Configure policies

Flare policies control which events appear in your tenant and which alerts you receive. Policies can define identifier matching, automatic identifier discovery, ignored terms, and duplicate handling.

1. Open the policy configuration in Flare.
2. Add the exclusions and ignored terms that should not generate events.
3. Configure matching and duplicate-handling policies for your identifiers.
4. Review the resulting monitoring scope.

Policy changes can take a few hours to affect the events in your tenant.

For more information, see the [Flare documentation about policies](https://docs.flare.io/policies).

### Create an API key

Create an API key that Sekoia can use to retrieve events from your Flare tenant.

1. In Flare, go to **Account > Profile**.
2. Scroll to **API keys**.
3. Click **Generate key**.
4. Enter a name for the API key.
5. Choose the permission scope for the key. If you use a restricted key, grant it the read permissions required to retrieve tenant events.
6. Set an expiration date if your organization requires one.
7. Click **Create key**.
8. Copy the secret and store it securely.

!!! warning "Store the API key securely"

    The secret is shown only when the key is created. Store it in a password manager or another protected location.

For more information, see the [Flare Profile documentation](https://docs.flare.io/profile).

## Objective 2: Send events to Sekoia

Create a Flare Events intake to retrieve and normalize events from Flare.

### Create the intake

1. Open the [Intakes page](https://app.sekoia.io/operations/intakes).
2. Click **+ Intake**.
3. Select **Flare Events**.
4. Enter a name for the intake.
5. Select the target entity.
6. Create or select the account used by the intake.
7. Enter the Flare API key in the `api_key` field.
8. Enter the Flare tenant ID in the `tenant_id` field if your API key can access several tenants.
9. Start the **Fetch new events from Flare** trigger.

### Review the connector parameters

The default values are recommended for most environments. You can modify them within the supported limits. These parameters change the connector's execution behavior and do not modify Flare data or Sekoia detection rules.

| Parameter | Limits | Recommended default | Description |
| --- | --- | --- | --- |
| `frequency` | Minimum `1` second, no documented maximum | `60` seconds | Time between two searches for new events. A higher value slows collection. |
| `page_size` | `1` to `10` | `10` | Number of events retrieved per page. |
| `lookback` | Minimum `1` hour, no documented maximum | `1` hour | Number of hours in the past from which the connector starts retrieving events. |
| `throttle_seconds` | Minimum `0` | `0.25` seconds | Wait time between two pages. Lower values are faster. The API retries when it reaches its rate limit. |

!!! note "Collection behavior"

    The supported limits prevent invalid values from breaking the intake. Larger intervals or smaller page sizes can increase the time needed to collect events.

   
    ![![Flare Events trigger configuration dialog with frequency set to 60 seconds, page size set to 10, throttle set to 0.25 seconds, and the lookback value set to 1 hour.](/assets/intelligence_center/flare_intake_parameters.png){: style="display: block; width: 100%; max-width: 100%; height: auto;"}]


### Verify event reception

After the trigger starts, Flare events are available in Sekoia as events associated with the Flare Events intake.

1. Open the Sekoia events view.
2. Filter the results by the Flare Events intake.
3. Open an event and verify that it contains Flare data.

> 📸 [SCREENSHOT SUGGESTION: Sekoia intake event details with the Flare event fields visible | ALT TEXT: Sekoia intake event details showing a valid Flare event and its event URL.]

## Objective 3: Generate Sekoia alerts

Detection rules create Sekoia alerts from matching Flare events.

1. Open the [Rules catalog](/xdr/features/detect/rules_catalog.md).
2. Filter the rules by the **Flare Events** intake format.
3. Review the available rules.
4. Activate the rules that match your monitoring and response requirements.

The available rules can change as Sekoia adds or updates detections for Flare events. After you activate a rule, Sekoia generates an alert when an ingested Flare event matches its conditions.

## Objective 4: Investigate a Flare alert

The Sekoia event contains the Flare event identifier and, when Flare provides one, the URL of the corresponding event. The `event.url` field is used to pivot from Sekoia to Flare.

1. Open a Sekoia alert generated from a Flare event.
2. Review the event details.
3. Locate the `event.url` field.
4. Click or copy the URL to open the corresponding event in Flare.

For more information, see the [Flare documentation about events](https://docs.flare.io/events).

## Result

You have configured the Flare workflow in Sekoia Digital Risk. Flare monitors the identifiers and policies that you defined, Sekoia retrieves the resulting events, and activated detection rules can generate alerts for investigation.

## Related articles

[Flare events in Sekoia Digital Risk](/cti/features/flare_events_overview.md): Overview of how Flare events are collected, normalized, detected, and investigated in Sekoia.

[Flare Events](/integration/categories/threat_intelligence/flare_events.md): Reference for the integration prerequisites, supported event types, raw samples, collection model, and detection coverage.

[Rules catalog](/xdr/features/detect/rules_catalog.md): How to review and activate built-in detection rules.

[Events](/xdr/features/investigate/events.md): How to review and investigate events collected in Sekoia.
