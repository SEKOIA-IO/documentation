# Optimization rules overview

!!! note "This article covers platform-level optimization rules"
    Platform-level optimization rules filter events after they reach Sekoia, at the intake level. If you use the Sekoia Endpoint Agent, a separate set of agent-level optimization rules lets you filter events before transmission. See [Reduce event volume with the Sekoia Endpoint Agent](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md).

Intake optimization rules allow you to control the processing and handling of incoming events before they are subjected to detection. These rules can be tailored to specific needs using filters and actions to effectively manage event data.

## When to use platform-level optimization rules

Platform-level optimization rules are appropriate when:

- You cannot modify the log source configuration (source-level filtering is not possible).
- You do not use the Sekoia Endpoint Agent, or the event type does not support agent-level filtering.
- You need to filter a non-endpoint source (firewall, cloud service, SIEM connector).

If you use the Sekoia Endpoint Agent, configure [agent-level rules](/integration/categories/endpoint/reduce_event_volume_endpoint_agent.md) first. If you are unsure which approach fits your situation, start with the [log volume reduction strategies playbook](/xdr/usecases/playbook/log_volume_reduction_strategies.md).

## Logic and execution

Optimization rules act as a pre-processing layer. When an event enters the platform, the system evaluates it against your defined rules before any detection logic or long-term storage occurs.

* **Execution order**: Rules do not follow a specific sequential execution order, such as priority or creation date. 
* **Quotas**: There is no limit on the number of rules you can create per community or per intake.
* **Rule types**: Rules can be Global (at the workspace level) or Community-based (managed by individual communities).

## Rule components

A rule is defined by the following components:

* **Scope**: You can target specific intakes using a **Community UUID**, **Dialect UUID**, or **Intake UUID**.
* **Filters**: A rule can accept several filters. All defined filters of a rule must match an existing field to apply.
* **Action**: This specifies the particular operation executed to optimize the event.

## Benefits

* **Cost management**: By ignoring high-volume, low-value events, you reduce the volume of data stored.
* **Data consistency**: You can delete non-standard fields to ensure logs align with official ECS or Sekoia Taxonomy.
* **Processing efficiency**: Actions like shrinking events or deleting message fields optimize the internal workflow and associated storage.

## See also
* [Investigate overusage](/xdr/usecases/playbook/investigate_overusage.md) to learn more about overusage and how to avoid it. 
* [Optimization rules technical reference](/xdr/features/collect/optimization_rules_reference.md) to learn more about filter operators, action bitmask values and more.
* [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md) to start creating your rule thanks to our step by step guide. 
* [Log volume reduction strategies](/xdr/usecases/playbook/log_volume_reduction_strategies.md) to align your rules on your usage.
