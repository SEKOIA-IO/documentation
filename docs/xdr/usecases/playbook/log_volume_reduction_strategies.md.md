# Log volume reduction strategies

Reducing log volume ensures your community remains within fair use limits and focuses your security analysis on high-value data. Effective reduction requires filtering logs as close to the source as possible.

## Context

To optimize your consumption, Sekoia.io recommends a hierarchy of filtering. By applying filters early in the data pipeline, you reduce unnecessary noise before it impacts platform performance or costs.

## Filtering levels

Sekoia.io recommends following this hierarchy, ordered from most efficient to least efficient:

| Level | Description | Recommended Actions | Related Documentation |
| :--- | :--- | :--- | :--- |
| **Source level** | The most effective method as it reduces network bandwidth and processing overhead. | <ul><li>**Firewalls/Cloud Services**: Configure the device to only send **Warning** or **Critical** logs. Disable **Info** or **Debug** logging.</li><li>**EDR/Endpoint Protection**: Adjust the agent policy to exclude noisy, non-security-relevant events.</li></ul> | Consult the official vendor documentation for your specific device. |
| **Forwarder level** | If you cannot modify the source configuration, use your collection infrastructure to drop logs. | <ul><li>**Rsyslog/Syslog-ng**: Implement filters to discard specific message types before they are forwarded to Sekoia.io.</li><li>**Sekoia.io Endpoint Agent**: Use **Optimization Rules** within the agent configuration to filter events directly on the host.</li></ul> | [Rsyslog filtering guide](/getting_started/ingest_data/syslog/rsyslog_forwarder/)<br><br>[Endpoint Agent Optimization Rules](/xdr/features/collect/endpoint_agent/) |
| **Platform level** | As a last resort, you can filter logs when they reach the Sekoia.io platform. | <ul><li>**Optimization Rules**: Define rules at the intake level to discard specific events. Note that while these events are not stored, they still reach the platform's entry point.</li></ul> | [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md) |

## Benefits

* **Improved Performance**: Faster query results due to reduced data noise.
* **Cost Management**: Maintain compliance with fair use policies and predictable costs.
* **Signal-to-Noise Ratio**: Security analysts focus on actionable events rather than routine system chatter.

## Use cases

* **Noise reduction**: Excluding known safe, high-frequency events like successful local logins in a non-critical environment.
* **Compliance**: Ensuring only logs required for specific regulatory frameworks are ingested.
* **Troubleshooting**: Temporarily increasing verbosity for a specific asset while keeping other sources filtered.

## See also: 
[Learn how to investigate your usage](/xdr/usecases/playbook/investigate_overusage.md)
