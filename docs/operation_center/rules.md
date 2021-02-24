# Detection Rules Management

## Rules list

On the alerts list, you can see in one look the following information.

- The status of your rules: Enabled or Disabled, plus the rules that can't compile will appear on a red background.
- The number of entities and assets to which the rule will be applied (default: all).
- The total of filtered alerts for the rule, corresponding to the number of alerts that where not raised, because the events corresponding to the signature of the rule where matching filter conditions.
- The total numbers of alerts raised and rejected during the past 7 days for each rule.

A toggle button allows a quick enablement/disablement of rules.

![Rules List](/assets/operation_center/rule_list.gif)

## Rule details

On top of the details of a rule, you can see when it was last updated and by who. The name of the rule will be used to name the corresponding raised alerts by default.

Detection rules can be applied to all events, whatever the entity to which they are attached or the assets to which they can be linked, or applied only to some of them. If 'Using all entities' and 'Using all assets' are selected, rules will apply to all events even if new entites or new assets were added since last rule modification. For rules for which some entities or some assets were selected, if new entities or new assets are created, detection will not occur on corresponding events whithout rule modification.

The signature part corresponds to the rule itself, the detection pattern applied to events. There're two type of rules: CTI or correlation.

- For CTI rules, you just have to select the source of the indicators: SEKOIA Intelligence Feed is an IOCs feed managed by SEKOIA's Purple Team (Indicators present in the SEKOIA.IO Intelligence Center).
- For correlation rules, the language used is STIX Patterning. More details about this langage are given [below](rules.md#stix-patterning).

Alert filters are used to avoid triggering alerts even if the events match the rule. Events that match the signature rule AND the alert filter criteria won't lead to the raising of an alert. Exclusion patterns are written in STIX patterning, like rules.

In the Alert properties part, you must indicate the category and type of the alerts raised by the rule and the severity of the rule, which is used to calculate the urgency of the corresponding raised alerts in association with assets criticality for events matching assets.

The alert generation mode affects the alert processing workflow. There are two generation modes: 'Automatic', for which the alerts passed to the status 'Ongoing' immediately after their creation, and 'Manual', for which the alerts remain in the 'Pending' status until a manual action. When selecting 'Inherit from entity', then the generation mode defined for each entity is used. When selecting a generation mode for an alert, it will override the entity's default value.

![Rules Details](/assets/operation_center/rule_details.gif)

!!! note
    Modification of rules parameters will be applied for new alerts, raised after the compilation of the rule.

## STIX Patterning

Correlation rules are written using STIX Patterning.

In order to enhance detection of possibly malicious activity on networks and endpoints, a standard language is needed to describe what to look for in a cyber environment. STIX, abbreviation for Structured Threat Information eXpression, is a standardized language developed by MITRE and OASIS Cyber Threat Intelligence (CTI) Technical Committee to describe information about cyber-threats. It has been adopted as an international standard by various communities and organizations sharing information.

STIX Patterns are composed of multiple building blocks, ranging from simple key-value comparisons to more complex, context-sensitive expressions. The most fundamental building block is the Comparison Expression, which is a comparison between a single property of a Cyber Observable Object and a given constant using a Comparison Operator. As a simple example, one might use the following Comparison Expression (contained within an Observation Expression) to match against an IPv4 address:

```
[ipv4-addr:value = '127.0.0.1']
```

Observation Expressions are contained in square brackets [ ... ] and may consist of one or more Comparison Expressions joined by Boolean Operators. Observation Expressions may be followed by one or more Qualifiers, which allow for the expression of further restrictions on the set of data matching the pattern. The final, highest level building block of STIX Patterning combines two or more Object Expressions via Observation Operators, yielding a STIX Pattern capable of matching across multiple STIX Observed Data SDOs.

![STIX Patterning](/assets/operation_center/stix_patterning.png)

!!! note
    When matching an Observation against an Observation Expression, all Comparison Expressions contained within the Observation Expression _MUST_ start matching against the same SCO in the Observation. That is, when resolving object paths of each Comparison Expression, the `<object-type>:<property_name>` _MUST_ start from the same SCO. Different SCOs may ultimately be used in matching, but they MUST be referenced from the same, single SCO.

    An Observation Expression _MAY_ contain Comparison Expressions with Object Paths that start with different object types, but such Comparison Expressions _MUST_ be joined by `OR`. **The Comparison Expressions of an Observation Expression that use `AND` MUST use the same base Object Path**.

!!! note
    Regarding the use of regular expressions (`MATCHES` keyword) in STIX Patterning rules, it is necessary to escape the “`\`”. Thus, the STIX Patterning rule to identify countries other than France, you will need to use the following rule:

    ```
    [ipv4-addr:x_tags[*].name MATCHES '^country:(?!FR)\\w+']
    ```

For more information about STIX and STIX Patterning, please refers to the [OASIS STIX Patterning specification](http://docs.oasis-open.org/cti/stix/v2.0/stix-v2.0-part5-stix-patterning.html).

## Observed Data

In order to trigger alerts, rule patterns must match with Observed Data. An "Observed Data" is the internal representation of any collected event in SEKOIA.IO. All events are normalized into a JSON object compliant with the STIX Observed Data specification. Detection rules are applied on events in STIX Observed Data format.

Here is an example of an Observed Data that could be obtained from a squid event:

```json
{
    "x_sic_entity_by_ref": "identity--d6358bb4-d9bb-47aa-b074-c6d1aeb673e2",
    "created": "2019-09-20T16:17:42.971Z",
    "objects": {
        "0": {
            "value": "127.0.0.1",
            "type": "ipv4-addr"
        },
        "1": {
            "value": "216.58.215.48",
            "type": "ipv4-addr"
        },
        "2": {
            "start": "2019-09-20T16:17:40.935Z",
            "type": "network-traffic",
            "end": "2019-09-20T16:17:40.935Z",
            "extensions": {
                "http-request-ext": {
                    "request_header": {
                        "Content-Type": "application/xml"
                    },
                    "request_method": "HEAD",
                    "request_value": "http://216.58.215.48/"
                }
            },
            "src_ref": "0",
            "dst_ref": "1",
            "protocols": [ "ipv4" ]
        },
        "3": {
            "type": "user-account",
            "extensions": {
                "x-log": {
                    "hostname": "DESKTOP-UPU7IFP"
                }
            }
        }
    },
    "type": "observed-data",
    ...
	"x_event_type": "http"
}
```

The JSON object has a type of **observed-data** and is composed by smaller objects following another STIX specification: **Cyber Observables**.

The main observable is the third one, with a type of network-traffic. It has references to indicate the source of the packet (`src_ref` - `127.0.0.1`) and its destination (`dst_ref` - `216.58.215.48`).

These information can be used to construct correlation rules. Below, a non-exhaustive list of information which can be used in your rules:

- `ipv4-addr:value`
- `ipv6-addr:value`
- `domain-name:value`
- `url:value`
- `network-traffic:dst_port`
- `network-traffic:src_port`
- `network-traffic:dst_packets`
- `network-traffic:src_packets`
- `network-traffic:dst_ref.value` (corresponding to IP value, in the above example, network-traffic:dst_ref refers to object 0, which has a value of '127.0.0.1')
- `network-traffic:src_ref.value`
- `network-traffic:extensions.'http-request-ext'.request_value`
- `network-traffic:protocols[*]`
- `process:pid`
- `process:name`
- `process:command_line`
- `file:hashes.md5`
- `user-account:account_login`
