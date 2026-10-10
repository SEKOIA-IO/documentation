# Log volume and fair use

Sekoia licenses include a monthly data volume allowance per defended asset. Understanding this allowance and planning for it from the start helps you stay within your agreed limits and keeps the platform performing well for you and all other customers on the shared infrastructure.

## How the volume allowance works

Your license define a maximum monthly ingestion volume.

**Defended asset** means the higher of (users or workstations) plus servers in the monitored information system:

```
Total assets = Max(Users, Workstations) + Servers
```

Going over the allowance does not interrupt your service. Sekoia monitors usage patterns and reaches out when a community consistently exceeds its threshold to help you find the right solution.

!!! note "Why volume limits exist"
    The platform is designed for unlimited ingestion at scale. Volume thresholds exist because sending large amounts of low-value data degrades detection performance for all communities and makes your own query results slower. The goal is to ingest security-relevant data, not everything.

## Why act before you exceed the limit

Partners and customers who address volume management proactively avoid the 2-3 month implementation delay that typically occurs when optimization is introduced reactively after a breach. Setting up filtering at the start of an integration is far cheaper than adjusting a live, production pipeline later, especially when end users and customer teams both need to be involved.

## The three filtering levels

Sekoia recommends filtering as early as possible in the data pipeline. The three available levels are listed below, from most efficient to least efficient.

| Level | Where filtering happens | Effect |
|---|---|---|
| **Source** | On the device or application itself | Eliminates volume before it enters your network |
| **Forwarder** | On your Rsyslog, Syslog-ng instance, or Sekoia Endpoint Agent | Eliminates volume before it reaches Sekoia |
| **Platform** | On the Sekoia intake (optimization rules) | Events reach Sekoia but are discarded before storage and detection |

!!! warning "Platform-level filtering is a last resort"
    Platform-level optimization rules reduce storage and detection load, but events still travel to Sekoia. For volume reduction that also reduces network bandwidth and ingestion cost, apply filtering at the source or forwarder level first.

## Your action plan

Use this checklist when onboarding a new integration or reviewing an existing one.

**Before going live**

1. Estimate expected daily event volume for each source. Most vendors publish average EPS (events per second) figures in their documentation.
2. Calculate your monthly GB estimate: `EPS × 60 × 60 × 24 × 30 × average_event_size_bytes ÷ 1,073,741,824`.
3. Identify high-volume, low-security-value event categories for each source (for example: successful local logons, DNS queries to known-safe resolvers, process telemetry from monitoring agents).
4. Apply source-level filtering where possible (disable Info/Debug log levels on firewalls and cloud services, adjust EDR agent policies).
5. Set up forwarder-level filters for any remaining high-volume, low-value events.
6. Create platform-level optimization rules for edge cases that cannot be filtered earlier.

**After going live**

1. Monitor your community's volume from **Home > Settings > Usage**.
2. Investigate spikes using the [investigate overusage playbook](/xdr/usecases/playbook/investigate_overusage.md).
3. Review your optimization rules quarterly as your environment changes.

## Involving your end users

If you manage Sekoia for multiple customer organizations (MSSP or partner model), communicate the volume policy to your end customers at the start of the engagement. Waiting until a threshold is crossed makes optimization feel like an emergency. Setting the expectation upfront gives customers time to plan, test, and approve configuration changes on their own devices before any action is required.

A simple checklist to share with customers at onboarding:

- Which event sources will forward logs to Sekoia?
- What log levels are currently enabled on firewalls, cloud services, and endpoint agents?
- Are there known noisy, low-security-value event types (scheduled tasks, monitoring agent heartbeats, internal health checks)?
- Who on the customer side approves changes to log source configuration?

## Related articles

- [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md): How to choose and apply the right filtering level for your situation.
- [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md): How to identify which sources or event types are driving unexpected volume.
- [Filter logs with Rsyslog or Syslog-ng](/xdr/features/collect/filter_logs_with_rsyslog_or_syslog_ng.md): How to drop unwanted events at the forwarder level before they reach Sekoia.
- [Reduce event volume with the Sekoia Endpoint Agent](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md): How to configure agent-side optimization rules to filter events before transmission.
- [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md): How to create a platform-level optimization rule on an intake.
