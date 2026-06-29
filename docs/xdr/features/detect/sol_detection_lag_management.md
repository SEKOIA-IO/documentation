# Lag management for SOL detection rules

Lag management is the built-in behavior that lets SOL detection rules evaluate events that reach the platform after their own timestamp. It combines a fixed overlap on every run with deduplication of overlapping results, so late events are still detected and the same alert is never raised twice.

## Why ingestion lag affects detection

SOL detection rules run on a schedule and evaluate the events that fall inside each run's time window. Events do not always arrive in real time: depending on the intake, an event timestamped at a given moment can land in Sekoia several minutes later. When this ingestion lag pushes an event past the moment its window has already been evaluated, the rule never sees it and the alert is never raised, even though the rule logic is correct.

For example, a rule that runs every 15 minutes evaluates a window that closes at the run time. An event timestamped shortly before the window closes, but delivered to the platform a few minutes after the run, would fall outside that already-evaluated window and go undetected.

## How the overlap window works

To catch these late events, every SOL detection run reaches back into the period the previous run already covered. Each run overlaps the previous run's window by a fixed 5 minutes, extending the start of the window 5 minutes earlier than where the last run ended.

Consider a rule that runs every 15 minutes:

| Run time | Window evaluated |
|---|---|
| 10:15 | Events timestamped 10:00 to 10:15 |
| 10:30 | Events timestamped 10:10 to 10:30 |
| 10:45 | Events timestamped 10:25 to 10:45 |

The 10:30 run reaches back to 10:10, so it re-covers the final 5 minutes of the 10:15 run. An event timestamped 10:14 that only arrives in Sekoia at 10:21 is missed by the 10:15 run, but the 10:30 run still evaluates it because its window starts at 10:10. The detection fires.

!!! note "Automatic behavior"
    The 5-minute overlap is applied to every SOL detection run. It is managed by the platform and is not configurable on the rule.

## Deduplication in the overlap window

The overlap that recovers late events also re-reads events that arrived on time and were already evaluated by the previous run. Left unchecked, those events would be evaluated twice and could raise the same alert twice.

To prevent this, the engine deduplicates the overlapping results before any alert is created. Results that the previous run already processed are dropped, so only genuinely new matches reach alert creation.

Using the same example, an event timestamped 10:12 that arrived on time was already evaluated by the 10:15 run. It falls inside the 10:10 to 10:15 overlap that the 10:30 run re-reads, so the 10:30 run discards it during deduplication and does not raise a second alert for it.

!!! note "Different from alert similarity"
    Overlap deduplication is a row-level safeguard internal to rule execution: it removes results the rule has already evaluated. It is not the same as alert similarity, which groups similar events from different matches into a single alert as occurrences. The two work at different layers. For how matches are grouped into an alert, see [Alert similarity](/xdr/features/operation_center/alerts.md#alert-similarity).

## Related articles

* [SOL detection rules](/xdr/features/detect/sol_detection_rule.md): Conceptual overview of the SOL and Event Drop detection patterns, how they work, and when to use them.
* [Create a SOL detection rule](/xdr/features/detect/create_sol_detection_rule.md): Step-by-step instructions to configure and activate a SOL or Event Drop detection rule.
* [Alert similarity](/xdr/features/operation_center/alerts.md#alert-similarity): How the platform groups similar events into a single alert as occurrences.
