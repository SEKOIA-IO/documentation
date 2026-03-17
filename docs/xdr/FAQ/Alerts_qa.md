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


## Alert Rate Limitation

Alert Rate Limitations automatically contain **misconfigured or runaway detection rules** to protect your community from alert storms. For SOC teams, this preserves **triage usability**, keeps **queues and notifications actionable**, and reduces **analyst fatigue** - so high-signal alerts don’t get buried under noise.

### How it works
Alert Flood Protection is evaluated **per detection rule** and **per community**:

##### Detection Rules
- Rate-limitation is applied at the rule level.
- The platform tracks how fast a rule is producing distinct alerts using a sliding (rolling) counter.
- If a detection rule generates **30 distinct alerts within 30 seconds**, that rule enters a **rate-limited state** for **30 minutes**.
- Alerts considered similar to an existing alert do not count toward this threshold.

##### CTI Rules
- Rate-limitation is applied at the individual IOC level.
- If a specific IOC reaches the threshold, only that **rule + IOC combination** enters a **rate-limited state** for **30 minutes**.
- Other IOCs within the same CTI rule remain unaffected and continue generating alerts normally.

#### During the rate-limited state
- No new alerts are raised for the affected rule, or affected **rule + IOC combination** for CTI rules.
- Matching events remain visible, allowing investigations to continue.
- Users can configure notifications when a rule enters a rate-limited state.

#### Cooldown behavior
- If new threshold breaches occur during the cooldown period, the **30-minute timer resets**.
- The affected rule, or affected **rule + IOC combination** for CTI rules, exits the rate-limited state only after **30 minutes** pass without a new threshold breach.

#### What you’ll see in the UI
- A **Rate-Limited icon/indicator** on matching events.
- An explanation message when expanding an event.
  - **Learn more** documentation on rate limiting.
Example,
<img width="437" height="559" alt="image" src="https://github.com/user-attachments/assets/f3ee6754-58db-4135-ac36-6eb7da549a3a" />

### Notifications when Alert Rate Limitation engage
You can configure notifications using:
- **A detection rule entered rate-limited state**

