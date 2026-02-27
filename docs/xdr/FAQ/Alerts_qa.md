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

Alert Rate Limitations automatically contain **misconfigured or runaway detection rules** to protect your community from alert storms. For SOC teams, this preserves **triage usability**, keeps **queues and notifications actionable**, and reduces **analyst fatigue** — so high-signal alerts don’t get buried under noise.

This safeguard is evaluated **per rule, per community**.

### How it works

Alert Flood Protection is evaluated **per detection rule** and **per community**:

#### 1) Rate threshold (sliding window)
- The platform tracks how fast a rule is producing new unique alerts using a **sliding (rolling) counter** (not cron-aligned fixed windows).
- **Threshold:** **30 alerts / 30 seconds** *(per rule, per community)*.

#### 2) Entering **Rate-Limited**
A rule becomes **Rate-Limited** when it exceeds the threshold.

#### 3) While **Rate-Limited**
- The rule **emits no new alerts** (alerts are suppressed).
- The rule **continues matching events** and evaluating conditions.

#### 4) Cooldown (exit conditions)
- **Cooldown duration:** **30 minutes**
- A rule exits Rate-Limited **only after 30 minutes pass without any new threshold breaches**.
- **Any threshold breach during cooldown resets the 30-minute timer**, which can keep a rule Rate-Limited indefinitely.

### Staying investigative while alerts are suppressed

When a Detection Rule is Rate-Limited, matching events remain visible for investigation and can be shown with UI metadata such as.

#### What you’ll see in the UI
- A **Rate-Limited icon/indicator** on matching events.
- An explanation message when expanding an event.
  - **Learn more** documentation on rate limiting.
Example,
<img width="437" height="559" alt="image" src="https://github.com/user-attachments/assets/f3ee6754-58db-4135-ac36-6eb7da549a3a" />

## Notifications when Alert Rate Limitation engage
You can configure notifications using:
- **A detection rule entered rate-limited state**

