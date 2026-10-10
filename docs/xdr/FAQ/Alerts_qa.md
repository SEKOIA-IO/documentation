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

!!! Note
    See more information on `timestamp` and `event.created`fields [here](Events_qa.md).

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
