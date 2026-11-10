## Alert date

When an alert is triggered, additional events can enrich this alert but the date of the alert will not be updated (date= 1st trigger).

## Bell icon in alerts page

The bell icon means that "the event is involved in an alert".

When a bell on an event is displayed on an alert page, the event is involved in the current alert AND in another alert.

If it is involved in the current alert, the bell is not displayed.

## How an alert is triggered with a delay ?

Besides matching a rule in real time, an alert can be triggered with a delay when:

    - An IOC is published, old events are scanned and if an event matches, the rule will automatically trigger an alert.
    - Logs from the source were received by Sekoia with a delay. Common route causes:
        * the log collection was interrupted, if logs are buffered loccaly on customer's side, before being sent later when the collection restarts
        * Reingestion of old logs

{% hint style="info" %}
See more information on `timestamp` and `event.created`fields [here](Events_qa.md).
{% endhint %}

## Alert Storm Control

**Alert Storm Control** (also referred to as Alert Rate Limitation) is a safeguard that detects and limits **runaway detection rules** to reduce alert flooding, lower alert fatigue, and improve platform resilience during high-volume bursts.

### How it works

Rate limiting is applied at the rule level, and at the individual IOC level for CTI rules:

##### Detection Rules

- Rate limiting is applied at the rule level.
- If a detection rule generates **30 distinct alerts within 30 seconds**, that rule enters a **rate-limited state** for **30 minutes**.
- Alerts considered similar to an existing alert do not count toward this threshold.

##### CTI Rules

- Rate limiting is applied at the individual IOC level.
- If a specific IOC reaches **30 matches**, only that **rule + IOC combination** enters a **rate-limited state** for **30 minutes**.
- Other IOCs within the same CTI rule remain unaffected and continue generating alerts normally.

#### During the rate-limited state

- No new alerts are raised for the affected rule, or affected **rule + IOC combination** for CTI rules.
- Matching events remain visible, allowing investigations to continue uninterrupted.

#### Reset behavior

- If new threshold breaches occur during the rate-limited state, the **30-minute timer resets**.
- The affected rule, or affected **rule + IOC combination** for CTI rules, exits the rate-limited state only after **30 minutes** pass without a new threshold breach.

#### What you'll see in the UI

- A **Rate-Limited icon/indicator** on matching events.
- An explanation message when expanding an event.
- A **Learn more** link on rate limiting.

Example:

<img width="437" height="559" alt="Rate-limited indicator on an event" src="https://github.com/user-attachments/assets/f3ee6754-58db-4135-ac36-6eb7da549a3a" />

### Benefits

- Reduced noise from excessive alert bursts
- Improved analyst focus during investigations
- Reduced risk of platform degradation caused by alert storms

### Get notified when a rule enters a rate-limited state

You can configure a notification when a rule enters a rate-limited state.

- Notification name: **A detection rule entered rate-limited state**

### To get started

- Review rules with high alert volumes
- Configure the notification **"A detection rule entered rate-limited state"** where relevant
- Adjust noisy rules as needed

## Why does an alert contain fewer events than the rule matched?

**Symptom:** An alert shows fewer events than expected. When you test the rule over the same period, it returns more matching events.

**Cause:** Sekoia adds at most **10 events to the same alert every 60 seconds**. During a burst, the events beyond this limit are not added to the alert.

### How it works

- The limit applies to each group of [similar events](../features/investigate/alerts.md#alert-similarity), so each alert has its own counter.
- The 60-second window starts with the first matching event. The first 10 events are added to the alert, and the following ones are not.
- After 60 seconds, the counter resets and new matching events are added to the alert again.
- Events that are not similar go to another alert, with its own counter.

The alert is still created, and its **Occurrence** count only includes the events that were added. The other events are not added later, but they remain available on the [Events page](../features/investigate/events.md). No indicator is displayed on these events, and no notification is sent.

**Example:** A rule matches 28 similar events within the same second. The first 10 events create the alert, and the other 18 are not added to it. Testing the rule over the same period returns all 28 events.

{% hint style="info" %}
This limit is different from [Alert Storm Control](#alert-storm-control).

| | Alert Storm Control | Events per alert limit |
| --- | --- | --- |
| What is counted | Distinct alerts raised by a rule | Events added to the same alert |
| Threshold | 30 alerts in 30 seconds | 10 events in 60 seconds |
| Effect | No new alert for the rule | Additional events are not added to the alert |
| Duration | 30 minutes without a new breach | Until the end of the 60-second window |
| Visible in the UI | Rate-limited indicator and notification | No |
{% endhint %}

**What to do:**

1. To see every event that matched the rule, [test the rule](../features/detect/rules_catalog.md#rule-testing) over the period of the alert. Sigma correlation rules cannot be tested: search their events on the [Events page](../features/investigate/events.md) instead.
2. If bursts of similar events are expected and each event must appear in an alert, create a custom rule with a more specific [similarity strategy](../features/detect/rules_catalog.md#custom-similarity-strategy). Events with different similarity values go to different alerts, and each alert has its own limit.
