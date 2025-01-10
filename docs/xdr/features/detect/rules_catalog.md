# Rules Catalog

Once your event logs are collected and normalized by Sekoia.io, you probably want to leverage them to detect suspicious activity within your perimeter. Rules contain the detection logic that determines when Alerts should be created.

All rules are applied to your event stream in real-time, so that you can detect - and respond to - threats as fast as possible.

Please check the [dedicated FAQ page](/xdr/FAQ/intelligence/Detection_qa.md) related to detection rule strategy.

## Rule Types

Sekoia.io supports the following rule types:

- **Sigma**: signature rules using the [Sigma detection language](sigma.md)
- **CTI**: rules based on Indicators Of Compromise (IOCs) coming from a Threat Intelligence feed. These rules automatically detect thousands of known malicious indicators (such as domain names, URLs, IP addresses, etc.). A CTI rule "SEKOIA Intelligence Feed" is already built-in to detect malicious activity based on a list of indicators from Sekoia.io's own Intelligence feed, continuously updated by our Threat & Detection Research team
- **Anomaly**: [univariate anomaly detection rules](anomaly.md).

## Rules Catalog
The Rules Catalog page can be used to list and manage all detection rules. Many filters are available and can be combined to easily find the rules you are looking for.

!!! tip
    You can enable or disable rules one by one or all at once according to current filters.



### Rules Attributes

#### Available and verified rules
The Rules Catalog lists all detection rules available to your organization:
<figure markdown>![available_verified_rules](/assets/operation_center/rules_catalog/available_verified.png){ width=300 }</figure>.

- **Verified Rules**: rules with the following logo ![verified_logo](/assets/operation_center/rules_catalog/verified_logo.PNG) are verified. These rules are created for you by Sekoia.io's Threat & Detection Research team and already built-in. Verified rules are constantly updated to improve detection. Furthermore, they follow a specific process to test them and be certain they won't cause many false positives. This process is described in our blogpost [XDR detection engineering at scale: crafting detection rules for SecOps efficiency](https://blog.sekoia.io/xdr-detection-rules-at-scale/). This set of more than 900+ rules can be used to detect known threats, attack patterns, etc.
- **Your Rules**: rules created by your team that are specific to your organization.

#### Effort level

All rules have an associated effort level. The effort level is increasing from Elementary to Master according to two criteria:
![effort_level](/assets/operation_center/rules_catalog/effort_level.png){ align=right }

- Effort needed to enable a rule.
- Risk of false positives.

Description of each effort level:

- `Elementary`: rule requires no effort to enable rule and raises fewer alerts. Those rules are built to be effective and designed to raise as little false positives as possible
- `Intermediate`: similar to `Elementary` effort but a rule could raise more alerts
- `Advanced`: rule could require more effort to be enabled and could raise alerts frequently depending on the IT configuration
- `Master`: rule could require a specific configuration to be enabled and/or could raise a high number of alerts, but is designed to detect weaker signals. `Master` rules usually require an additional customization effort, depending on the IT context and configuration. They are designed for more mature organizations.

#### Intake formats

Rules are associated with Intake formats that they are compatible with. Detection rules can be enabled when they have a compatible intake format configured that provide the necessary data to detect suspicious activites.

Select an intake format in the left panel to list rules compatible with the intake format.

![intakes](/assets/operation_center/rules_catalog/filter_by_intake.png){: style="max-width:50%", align=right}

You can also filter by intake formats that you have already configured with the associated filter.

![filter](/assets/operation_center/rules_catalog/intake_configured.png){: style="max-width:50%", align=right}

#### Threats

Rules are associated with Threats or Attack Pattern that they can detect.

Use the associated search filter to list rules associated to specific threats.

![threats](/assets/operation_center/rules_catalog/search_filters.png){: style="max-width:50%", align=right}

#### Tags

To have a filtered view of your rules, you can rely on filters cited before ([Available/Verified](#available-and-verified-rules), [Effort level](#effort-level), Capabilities) but also on tags associated with rules.

These tags are defined by Sekoia.io analysts to help make searching for a rule easier and provide categories such as `AWS`, `CVE`, `O365` and `phishing`.

To filter rules using tags, there are two ways:

- Select a tag under a rule and it will filter all rules to show only those with the same tag
- Click the filter button and select "Tags" 

----

### Security Profile (MITRE ATT&CK)

The MITRE ATT&CK framework is a comprehensive matrix of **tactics** and **techniques** used by threat hunters and defenders to better classify attacks and assess an organization's risk.

Whenever you filter the Rules Catalog, the matrix will update and rules will appear in blue on the matrix in one or many cells. Each cell represents an attack technique.

![security_profile](/assets/operation_center/rules_catalog/security_profilev3.png){: style="max-width:100%"}

The color changes depending on the number of rules contained in one cell:

- Colored cells signify the presence of rules. **Darker cells** indicate a higher number of rules available for that specific technique. **Lighter cells** suggest that there are fewer enabled rules for the technique.
- A white cell means that no rule is available for that technique. 

![mitre_details](/assets/operation_center/rules_catalog/mitre_details.gif){: style="max-width:100%"}

Click on the MITRE preview to explore the distribution of rules across each technique and sub-technique.

To view the MITRE framework in fullscreen, click the fullscreen button in the top-right corner of the modal.

Use the "Sub-techniques" button to expand or collapse all sub-techniques.

You can scroll through the MITRE details both horizontally and vertically.

---

### Rule Details
You can click on the name of a rule to display additional details, such as, but not limited to:

- The severity which should be used to later determine the [Alert's Urgency](../investigate/alerts.md#alert-urgency)
- The category of created alerts
- Associated Threats
- Associated Data Sources
- Known False Positives
- The actual detection logic (the pattern)
- Alert filters
- [Similarity strategy](../investigate/alerts.md#similarity-strategies) for the produced alerts

![rule details](/assets/operation_center/rules_catalog/rule_details2.png)

### Compatible intake formats

This section list the compatible intake formats you can use with the detection rule. Configuring one of these intake formats allow the detection rule to receive compatible events to perform detection.

In the list, the `configured` badge indicates intake formats that are already configured. You can click on the configured intake to go the intake page.

![configured intake](/assets/operation_center/rules_catalog/configured_intake.png)

!!! tip
    You can use this feature to run simulations with the MITRE matrix to improve your security posture.
    Select a new intake to have a preview of the techniques that will be covered by configuring this datasource.

### Alert filters

In the section `Alert filters`, you can consult the list of alert filters that are currently enabled in the `Actives` tab. The number of alert `muted` in the `last 30 days` is displayed for each alert filter to help you audit its effectiveness.

Click on the `arrow` to expand the alert filter and consult the exclusion pattern.

![alert filters](/assets/operation_center/rules_catalog/alert_filters.png)

The `Expired` tab list all the alert filters that had an `expiration date` set and whose date has been reached. Expired alert filters can be deleted if needed.

### Rules with active alert filter

To search for rules that have at least one active alert filter, use the search `Alert filter` and select the criteria `Rules with alert filters`.
All rules with active alert filters will be returned in the list.

![search alert filters](/assets/operation_center/rules_catalog/search_alert_filters.png)

You can also search for rules that have no active alert filters with the other search criteria.

### Enable new rules
#### Automatically

New verified rules are created regularly. You may not want to look at the rules catalog daily to decide if you want to enable them or not. By clicking on the `configure` icon at the top right of the Rules Catalog page, you can configure which rules should be automatically enabled for your organization.

![auto-enable](/assets/operation_center/rules_catalog/enable_rules.png){: style="max-width:100%"}

Rules are automatically enabled based on the configured effort level, or you can decide to never automatically enable rules.

#### Manually

To ensure that activated rules comply with your security policy, you can choose which rules you want to enable.
For an MSSP Community, you can easily enable your custom and verified rules in multiple managed communities.
![Enable rules for MSSP community](/assets/operation_center/rules_catalog/enable_multi_communities.png){: style="max-width:70%"}

### Enable / Disable all rules

As seen previously, rules can be filtered by type, status, effort level and tags. To enable or disable these filtered rules, you can simply click on the button `Enable all` or `Disable all` that are displayed under the search bar.

![enable-disable](/assets/operation_center/rules_catalog/rules-enable-disable.png){: style="max-width:100%"}


----

### Create custom rules

In addition to the verified rules that are already built-in, you can create your own rules to support other detection use cases. To create a rule, click on the `+ Rule` button at the top right of the page and fill out the form.

The Rule creation form has the following sections:

#### General definition of the rule
- The rule name is mandatory during the creation, it will be used to name the corresponding raised alerts by default. You can add an optional description below.
- Select the effort level required and the threats detected with this rule if any, by selecting it from the MITRE ATT&CK or by using the search bar through keywords or the drop-down list.
- For an MSSP community, first select the community you want to create your rule in.
-
Two options are available: select `All communities` or select a specific community.

If you choose `All communities`, your rule will be available for all your communities and you can enable it later on the desired community.

  ![Create rules for MSSP community](/assets/operation_center/rules_catalog/create_new_rule_mssp_communities.png){: style="max-width:60%"}

#### Detection Pattern

  This is the detection logic itself. It varies according to the selected rule type.

!!! note
    Fields available to create a detection pattern follow the ECS standard and can be found on Events page  > **Show fields and top values**.

#### Security alerts
In the Alert properties part, you should indicate the category and type of the alerts raised by the rule and the severity of the rule, which is used to calculate the urgency of the corresponding raised alerts in association with assets criticality for events matching assets.

##### Fields displayed in alert events

You can select fields that will be displayed in events present inside your raised alerts to speed up alert qualification.

To search for fields you want to display, click on the select and type in your event field. This field works as an auto-complete.

##### Custom similarity strategy
Alerts are considered similar when some event fields have identical values.

You can select these event fields in your rule configuration. To do so, click on the select and type in your event field. You can select as many fields as needed.

In addition to that, these event fields can be added to the `Swappable fields`. A typical example of that is  `source.ip` and `destination.ip`.

!!! warning
    Custom similarity strategy are not supported with Sigma Correlation rules.
    Fields used in the `group-by` clause of the pattern will be used as similarity strategy.

!!! note
    You can learn more about similarity strategies in this [section](../investigate/alerts.md#similarity-strategies).


### Edit your custom rules
When the Rule Details panel is open, you can click on the `Configure` icon at the top right to edit the rule's configuration.
For Custom rule, you will be able to edit its main definition:

- General definition of the rule
- Detection Pattern
- Security alerts (event fields can be selected to define the similarity strategy in the section `Similarity strategy`).

For an MSSP communty, when you edit this part and your rule is multi-communities, changes will be shared with all your managed communities.



### Limiting the scope of a rule

For all types of rules, You will be able to limit its applicable scope with the following filters. For an MSSP community, these filters will be applied only on the community selected:

- **Alert Filters**: are additional patterns that you can add to any rule to exclude matching events. This is useful to exclude known false positives so that your detections are always spot on. It is often easier to create Alert Filters [directly from an Alert](../investigate/alerts.md#create-an-alert-filter).
- **Entities**: select the entities this rule should apply to. By default, rules apply to all entities.
- **Assets**: select the assets this rule should apply to. By default, rules apply to all assets

![limit-scope](/assets/operation_center/rules_catalog/rules_catalog_filters.png)

When rules have limited scope with selected entities or assets, these rules will not automatically apply to new entities or assets that are later created.

#### Create an alert Filter

To prevent known false positives from raising alerts in the future:

- Click on the `+ Alert filter` button to create an alert filter
- Enter the `name` of the alert filter (mandatory)
- Enter the `description` of the alert filter (optional)
- Enter the `pattern` to exclude events (mandatory)
- Set an `expiration date` (optional) to define a temporary alert filter

### Notify on new rules

![notif_rules](/assets/operation_center/rules_catalog/notification_rules.png){ align=right }

We continuously update the rules catalog with new rules.

To keep posted, we introduced a dedicated trigger in the Notification Center.
This new notification trigger enables the creation of notification rules that triggers when a new detection rule is added to the Rules Catalog by Sekoia.io.

This trigger supports additionnal filters on the name of the detection rule, its description, pattern or severity.
