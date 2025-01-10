# Detection Rules on Sekoia.io

Sekoia.io provides various types of detection rules to monitor events in real time and identify threats. These rules are categorized as **"built-in"**. In addition, you can create your own detection rules, referred to as **"custom"** rules. Below is a FAQ to guide you through creating, modifying, and validating these rules.


## What types of detection rules are available on Sekoia.io?

Sekoia.io supports the following types of detection rules:

1. **Sigma Rules** (simple and correlation): Signature-based rules using the Sigma detection language.
2. **CTI (Cyber Threat Intelligence) Rules**: Rules based on indicators of compromise (IoCs) from threat intelligence feeds.
3. **Anomaly Rules**: Detect anomalies by identifying deviations from normal behavior using time-series machine learning.
4. **STIX Rules (Deprecated)**: Signature rules based on the STIX language, now deprecated.


## Which detection engine should I use to trigger an alert for a specific event?

The appropriate engine for triggering an alert on a specific event is the **Sigma engine**.  
For more details, visit the [Sigma documentation](/xdr/features/detect/sigma.md).


## Which detection engine should I use to trigger an alert for a set of events?

**Sigma correlation rules** rely on one or more Sigma rules and correlation attributes such as action, type, reference, and time period. Depending on the correlation type (temporal, event_count, value_count), the rule evaluates if events occur within the same timeframe, exceed a frequency threshold, or compare the number of values in a given field to a threshold.  
Learn more in the [Sigma correlation rules documentation](/xdr/features/detect/sigma.md#correlation).


## Which detection engine should I use to detect anomalies in time-series data?

Use **Anomaly Detection Rules** to analyze time-series data, identify abnormal patterns, and generate alerts. These rules use machine learning to establish normal behavior and detect unusual deviations.  

Consider the following questions when planning your analysis:
- Am I interested in monitoring deviations of a specific indicator from its historical data?
- Does my time series exhibit periodic trends (daily, weekly)?

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


## How to distinguish between OR and AND logic in Sigma patterns:

- **"OR"**: Triggers an alert if at least one condition is met.
    ```yaml
    selection:
      process.name: 
        - "malware.exe"
        - "ransomware.exe"
    condition: selection
    ```
    *Explanation*: Triggers an alert if `process.name` is **"malware.exe"** OR **"ransomware.exe"**.

- **"AND"**: Triggers an alert only if all conditions are met.
    ```yaml
    selection:
      process.name: "malware.exe"
      destination.ip: "192.168.1.1"
    condition: selection
    ```
    *Explanation*: Triggers an alert if `process.name` is **"malware.exe"** AND `destination.ip` is **"192.168.1.1"**.

- **Combining OR and AND**:
    ```yaml
    selection:
      process.name: 
        - "malware.exe"
        - "ransomware.exe"
      destination.ip: "192.168.1.1"
    condition: selection
    ```

