# Rules Catalog

Once your event logs are collected and normalized by SEKOIA.IO, you probably want to leverage them to detect suspicious activity within your perimeter. Rules contain the detection logic that determines when Alerts should be created.

All rules are applied to your event stream in real-time, so that you can detect - and respond to - threats as fast as possible.

## Rule Types

SEKOIA.IO supports the following rule types:

- **Sigma**: signature rules using the [Sigma detection language](sigma.md)
- **CTI**: rules based on Indicators Of Compromise (IOCs) coming from a Threat Intelligence feed. These rules automatically detect thousands of known malicious indicators (such as domain names, URLs, IP addresses, etc.). A CTI rule "SEKOIA Intelligence Feed" is already built-in to detect malicious activity based on a list of indicators from SEKOIA.IO's own Intelligence feed, continuously updated by our Threat & Detection Research team
- **Anomaly**: [univariate anomaly detection rules](anomaly.md).
- **STIX** (deprecated): signature rules using the STIX Patterning language

## Rules Catalog
The Rules Catalog page can be used to list and manage all detection rules. Many filters are available and can be combined to easily find the rules you are looking for.
You can enable or disable rules one by one are all at once according to current filters.

### Rules Attributes

#### Available / Verified Rules
The Rules Catalog lists all detection rules available to your organization:

- **Verified Rules**: rules created for you by SEKOIA.IO's Threat & Detection Research team and already built-in. This set of more than 500 rules can be used to detect known threats, attack patterns, etc. Verified rules are constantly updated to improve detection.
- **Custom Rules**: rules created by your team that are specific to your organization.

The Available Rules counter displays the total number of rules (verified + custom). You can click on the Verified counter to list only Verified rules. You can then click on the Verified filter if you would rather see only Custom rules.

#### Effort Level

All rules have an associated effort level. The effort level is increasing from Elementary to Master according to two criteria:

- Effort needed to enable a rule.
- Risk of false positives.

For example:

- `Elementary` rules require almost no effort and raise fewer alerts
- `Master` rules are generic and raise a lot of alerts that will require qualification, but they can detect weaker signals. Those rules require an additional customisation effort, which has to be adapted to the customer context
You can click on each counter associated with an effort level to see only the rules for this level

#### Capabilities
The rules are also associated with different capabilities:

- Offensive Capabilities: `threats` or `attack patterns` that they can detect
- Defensive Capabilities: `data sources` on which they operate

Capabilities that have associated rules inside the catalog are listed on the left of the page. You can click on any Threat, Attack Pattern, or Datasource to list only rules that are associated with it.

### Security Profile (MITRE ATT&CK)
The MITRE ATT&CK framework is a comprehensive matrix of **tactics** and **techniques** used by threat hunters and defenders to better classify attacks and assess an organization's risk.
Every time you enable a rule, it appears on the matrix in blue in one or many cells.
Each cell represents an attack technique. The cells are clickable and enable you to see or disable the rules activated in each one.
You can see how many rules are enabled in a cell by hovering over it.
The color changes depending on the number of rules activated in one cell. The blue gets darker when more rules are enabled and a white cell means that no rule is activated in it.

### Rule Details
You can click on the name of a rule to display additional details, such as, but not limited to:

- The Severity which should be used to later determine the Alert's Urgency
- The Category of created alerts
- Associated Threats
- Associated Data Sources
- Known False Positives
- The actual detection logic (the pattern)

### Limiting the scope of a rule

When the Rule Details panel is open, you can click on the Configure icon at the top right to edit the rule's configuration. If the rule is Custom, you will be able to edit every aspect of it. Otherwise, you will only be able to limit its applicable scope with the following filters:

- **Alert Filters**: are additional patterns that you can add to any rule to exclude matching events. This is useful to exclude known false positives so that your detections are always spot on. It is often easier to create Alert Filters [directly from an Alert](../../investigate/alerts/#create-an-alert-filter).
- **Entities**: select the entities this rule should apply to. By default, rules apply to all entities.
- **Assets**: select the assets this rule should apply to. By default, rules apply to all assets.

When rules have limited scope with selected entities or assets, these rules will not automatically apply to new entities or assets that are later created.

### Create custom rules

In addition to the verified rules that are already built-in, you can create your own rules to support other detection use cases. To create a rule, click on the `+ Rules` button at the top right of the page and fill out the form.

The Rule creation form has the following sections:

- **General definition of the rule:**
  The rule name is mandatory during the creation, it will be used to name the corresponding raised alerts by default. You can add an optional description below.
  Select the effort level required and the threats detected with this rule if any, by selecting it from the MITRE ATT&CK or by using the search bar through keywords or the drop-down list.

- **Detection Pattern:**
  This is the detection logic itself. It varies according to the selected rule type.

- **Security alerts:**
  In the Alert properties part, you should indicate the category and type of the alerts raised by the rule and the severity of the rule, which is used to calculate the urgency of the corresponding raised alerts in association with assets criticality for events matching assets.

  You can also pre-select fields that will be displayed inside alerts to speed up alert qualification.

- **Entities & Assets:**
  As discussed in the [limiting the scope](#limiting-the-scope-of-a-rule) section, you can select specific entities or assets this rule should apply to.

### Automatically enable new rules

New verified rules are created regularly. You may not want to look at the rules catalog daily to decide if you want to enable them or not. By clicking on the `configure` icon at the top right of the Rules Catalog page, you can configure which rules should be automatically enabled for your organization.

Rules are automatically enabled based on the configured effort level, or you can decide to never automatically enable rules.

### Notify on new rules

We continuously update the rules catalog with new rules. To keep posted, we introduced a dedicated trigger in the Notification Center.
This new notification trigger enables the creation of notification rules that triggers when a new detection rule is added to the Rules Catalog by SEKOIA.IO.

This trigger supports additionnal filters on the name of the detection rule, its description, pattern or severity.
