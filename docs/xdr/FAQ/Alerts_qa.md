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
    See more informaiton on `timestamp` and `event.created`fields [here](Events_qa.md).
