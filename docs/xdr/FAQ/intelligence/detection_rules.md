# Detection Rules on Sekoia

Sekoia provides various types of detection rules to monitor events in real time and identify threats. These rules are categorized as **"built-in"**. In addition, you can create your own detection rules, referred to as **"custom"** rules. Below is a FAQ to guide you through creating, modifying, and validating these rules.

## What types of detection rules are available on Sekoia?

Sekoia supports the following types of detection rules:

1. **Sigma rules** (simple and correlation): Signature-based rules using the Sigma detection language.
2. **CTI (Cyber Threat Intelligence) rules**: Rules based on indicators of compromise (IoCs) from threat intelligence feeds.
3. **Anomaly rules**: Detect anomalies by identifying deviations from normal behavior using time-series machine learning.
4. **SOL detection rules**: Execute a Sekoia Operating Language (SOL) query on a defined schedule and generate alerts when the query returns results. See the [SOL detection rules overview](/xdr/features/detect/sol_detection_rule.md).
5. **STIX rules (deprecated)**: Signature rules based on the STIX language, now deprecated.

## Which detection engine should I use to trigger an alert for a specific event?

The appropriate engine for triggering an alert on a specific event is the **Sigma engine**.

For more details, visit the [Sigma documentation](/xdr/features/detect/sigma.md).

## Which detection engine should I use to trigger an alert for a set of events?

**Sigma correlation rules** rely on one or more Sigma rules and correlation attributes such as action, type, reference, and time period. Depending on the correlation type (temporal, event\_count, value\_count), the rule evaluates if events occur within the same timeframe, exceed a frequency threshold, or compare the number of values in a given field to a threshold.

Learn more in the [Sigma correlation rules documentation](/xdr/features/detect/sigma.md#correlation).

## Which detection engine should I use to detect anomalies in time-series data?

Use **Anomaly Detection Rules** to analyze time-series data, identify abnormal patterns, and generate alerts. These rules use machine learning to establish normal behavior and detect unusual deviations.

Consider the following questions when planning your analysis:
\- Am I interested in monitoring deviations of a specific indicator from its historical data?
\- Does my time series exhibit periodic trends (daily, weekly)?

If yes, anomaly detection rules are a suitable choice.

> **Note:** Anomaly alerts have a delay of 30 minutes + 2 × time interval.

## Which detection engine should I use to identify IoCs in a knowledge base?

Use **CTI Rules**, which rely on IoC collections to raise alerts when matching IoCs are found in parsed events. You can create your own IoC collections or use preconfigured ones like the **SEKOIA Intelligence Feed**.

CTI rules also support retrohunting.

## What if a rule generates too many false positives?

If a **built-in** rule generates excessive false positives but remains useful, you have several options:

1. **Adjust the rule with alert filters or limit its scope**: Restrict the rule to specific entities or assets or exclude patterns using alert filters.
2. **Duplicate and modify the Sigma pattern**: Create a custom version of the rule by duplicating and editing it. Note that duplicated rules are not maintained by Sekoia analysts.
3. **Propose improvements**: For minor adjustments, submit suggestions to Support. For significant changes, duplicate the rule and deactivate the original.
4. **Disable the rule**: If the rule is not relevant to your use cases, you can simply disable it.

## How can I track the number of alerts prevented by alert filters?

On the rule's page, navigate to the **alert filters** section. Here, you can view the number of alerts filtered in the last 30 days and check the expiration details of your alert filters.

## Why does Test pattern show results from other communities?

For an MSSP community, **Test pattern** evaluates events according to the detection rule's status:

| Detection rule status | Communities evaluated |
| --- | --- |
| Disabled | Events from all communities |
| Enabled for a list of communities | Events from the communities where the detection is enabled |

The **Community** filter in the Rules Catalog only filters the detections displayed in the list. It does not change the communities evaluated by **Test pattern**, and the test does not currently provide an independent community selector.

The community selector in **Rule Details > Rule scope** applies to alert filters. It does not control the scope of **Test pattern**.

For example:

- If the detection rule is disabled, **Test pattern** evaluates events from all communities, even when the Rules Catalog is filtered to one community.
- If the detection rule is enabled for Communities B and C, **Test pattern** evaluates events from Communities B and C. It does not evaluate Community A unless the detection is also enabled there.

For the rule-testing procedure, see [Rules Catalog](/xdr/features/detect/rules_catalog.md#community-scope-for-existing-detections).

## How do I distinguish between OR and AND logic in Sigma patterns?

- **"OR"**: Triggers an alert if at least one condition is met.

```yaml
selection:
    process.name:
    - "malware.exe"
    - "ransomware.exe"
condition: selection
```

_Explanation_: Triggers an alert if `process.name` is **"malware.exe"** OR **"ransomware.exe"**.

- **"AND"**: Triggers an alert only if all conditions are met.

```yaml
selection:
    process.name: "malware.exe"
    destination.ip: "192.168.1.1"
condition: selection
```

_Explanation_: Triggers an alert if `process.name` is **"malware.exe"** AND `destination.ip` is **"192.168.1.1"**.

- **Combining OR and AND**:

```yaml
selection:
    process.name:
    - "malware.exe"
    - "ransomware.exe"
destination.ip: "192.168.1.1"
condition: selection
```

Back to top

## Related articles

[Rules Catalog](/xdr/features/detect/rules_catalog.md): How to create, test, enable, and scope detection rules.

[SOL detection rules](/xdr/features/detect/sol_detection_rule.md): Overview of scheduled SOL queries that generate security alerts.
