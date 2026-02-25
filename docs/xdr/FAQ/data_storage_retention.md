# Data storage and retention

Sekoia.io uses a hybrid storage architecture to balance real-time detection performance with long-term compliance requirements. This system categorizes security events into two distinct tiers: Hot and Cold storage.

## Hot storage

Hot storage contains your most recent events. This tier is mandatory for all Sekoia.io Defend plans and is optimized for immediate operational use.

* **Availability**: Events are immediately searchable for threat hunting and detection.
* **Retention**: The default period is 30 days, extendable up to 365 days.
* **Performance**: High-performance indexing for rapid querying.

## Cold storage

Cold storage (or "Archives") is an optional tier for older events. It provides a cost-effective way to store data for compliance without maintaining it in the active search index.

* **Availability**: Events are not immediately searchable. You must trigger a rehydration process to access this data.
* **Retention**: Combined retention (Hot + Cold) typically ranges from 30 to 365 days.
* **Resiliency**: Sekoia.io maintains the same level of data resiliency for both storage tiers.

## View your storage capacity

You can verify the specific storage durations included in your subscription directly within the platform.

To view your current plan:

1.  Navigate to **Settings > Subscription**.
2.  Locate the **Storage** section to see your allocated days for each tier.

![Navigation to Settings > Subscription to view hot and cold storage days](/assets/xdr/storage_subscription.png)



## Storage limitations

Retention periods are strictly governed by your contractual agreement. 

!!! warning "Data Permanence"

    Sekoia.io cannot retrieve data that exceeds your defined storage thresholds. For example, if your total retention is 120 days, any data older than this limit is permanently deleted and cannot be recovered by Support.

## Next steps
To learn how to access your archived events for a specific investigation, follow our guide to [restore data from cold storage](/xdr/FAQ/restore_data_cold_storage.md).
