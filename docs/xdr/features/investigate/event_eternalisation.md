# Event Eternalisation

Event eternalisation is the process of **permanently storing the events related to an alert** into a dedicated index. It is a critical step in the alert pipeline: once the relevant events are eternalised, the corresponding alert is published and becomes visible in your interface.

The key idea behind eternalisation is **durability**: eternalised events are stored separately from the raw events index, ensuring they remain accessible for investigation regardless of the standard log retention period.


## How it works

When a detection rule triggers an alert, the following sequence occurs:

1. The platform identifies the events that matched the rule.
2. Those events are **fetched from the raw events index** and **permanently indexed** into a dedicated store.
3. Once eternalisation is complete, the **alert is published** and becomes visible to analysts.

!!! note
    The alert is only made visible **after** its events have been successfully eternalised. This means eternalisation is a mandatory step before you can see and investigate an alert.

## What This Means for Analysts

### Alerts may appear with a delay

Because eternalisation must complete before an alert is published, any slowdown in this process will directly impact **when alerts appear** in your queue. If you notice an unusual delay in alert delivery, eternalisation latency may be the cause.

### Events may be missing from an Alert

If eternalisation partially fails, an alert may be published with **fewer events than expected** â€” or none at all. This can make investigation difficult, as the supporting evidence is incomplete.

!!! warning
    If you open an alert and find that events are missing or the alert seems incomplete, this may be the result of an eternalisation issue. Contact your platform administrator so the events can be replayed and reindexed.

### Eternalised Events Have Extended Accessibility

Unlike raw events, which are subject to your standard retention policy, eternalised events are stored in a **dedicated, durable index**. This means you can always return to an alert and review its associated events, even after the raw logs would have expired.

## What to do if you suspect an issue

If you observe alerts with missing events or unexpected delays:

!!! tip
    - **Do not close the alert**: missing events may be reinjected once the issue is resolved.
    - **Note the alert UUID and timestamp**: this will help your administrator locate and replay the affected events.
    - **Escalate to your platform administrator**: eternalisation failures require an infrastructure-level fix and cannot be resolved from the analyst interface.

---

## Further Reading

- [Alerts â€“ Sekoia.io Documentation](https://docs.sekoia.io/xdr/features/investigate/alerts/)
- [Events â€“ Sekoia.io Documentation](https://docs.sekoia.io/xdr/features/investigate/events/)
