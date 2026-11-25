# Cortex Analyzer

Sekoia.io is providing a [Cortex analyzer](https://github.com/TheHive-Project/Cortex-Analyzers/tree/master/analyzers/SEKOIAIntelligenceCenter) to enrich data in [TheHive](https://thehive-project.org/) ecosystem.

## Objective

Collect Sekoia.io CTI feed in an existing Cortex instance self-managed, for any operational purpose such as CTI aggregation, dissemination, hunting...

## Prerequisites:

* An operational Cortex instance with administrator privileges
* An active Sekoia.io licence with access to the CTI
* An API key with the permission "View intelligence"

## 1. Connect to Cortex

{% hint style="info" %}
Cortex instance must be activated on your server
{% endhint %}

1. In a Web browser, type the following _http://server\_ip:cortex\_port_
2. Enter your login and password of your Cortex instance setup beforehand with `orgadmin` role

## 2. Configuration

### 1. Setup the Analyzer configuration

{% hint style="info" %}
The setup of Analyzers in Cortex will allow to be used in Cortex and in theHive

1. Select your _Organization_ on the top right corner
{% endhint %}

![Orga\_setup\_1](../../.gitbook/assets/orga_setup_1.png)

2. Go to _Analyzers Config_ tab and Search `SekoiaIntelligenceCenter` ![Orga\_setup\_2](../../.gitbook/assets/orga_setup_2.png)
3. Edit and Add your Sekoia API key and Base url ![Orga\_setup\_3](../../.gitbook/assets/orga_setup_3.png)

{% hint style="info" %}
If your Sekoia community is hosted on FRA1 region, leave the "Base url" field empty.
{% endhint %}

### 2. Enable and Setup the Analyzer

The configuration setup in the previous section will provide 3 Analyzers to enable and setup:

* SEKOIAIntelligenceCenter\_Indicators\_1\_0
* SEKOIAIntelligenceCenter\_Context\_1\_0
* SEKOIAIntelligenceCenter\_Observables\_1\_0

Here is below one example of setup to be done for the 3 analyzers:

1. Go to _Analyzers_ tab and Search `SekoiaIntelligenceCenter` ![Analyzer\_ config\_1](../../.gitbook/assets/analyzer_config_1.png)
2. Edit and Add your `Sekoia API key` and `Base url` ![Analyzer\_ config\_2](../../.gitbook/assets/analyzer_config_2.png)

## 3. Sekoia intelligence in Cortex

In the following section, you will find information on how Sekoia intelligence is available in Cortex

### Summary of the information

| Artefact   | Analyzers                                   | in Cortex               | in Sekoia.io                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Indicator  | SEKOIAIntelligenceCenter\_Indicators\_1\_0  | indicators              | Details of an [indicator](../consume/observables.md) also called IOC (Indicator of Compromission) such as Dates, Confidence level, Indicator types, Kill chain, Pattern. The indicator is found under objects tab of Intelligence page |
| Context    | SEKOIAIntelligenceCenter\_Context\_1\_0     | context of an indicator | Side details in an indicator (Related threats, Linked Observables, Latest reports, Indicator types, Kill chain)                                                                                                                        |
| Observable | SEKOIAIntelligenceCenter\_Observables\_1\_0 | known observables       | [Observable](../consume/observables.md) under observables tab of Intelligence page                                                                                                                                                     |

## 4. Steps to retrieve and search Sekoia intelligence

### Search existing Sekoia intelligence in Cortex

1. Select `Data Types`, `Job Type` and `Analyzers`
2. Type your indicator or observable in the Observable search bar (here is an example with `Google`)

![TheHive\_searchExisting\_SekoiaCTI](../../.gitbook/assets/searchExisting_SekoiaCTI.png)

### Verify a Sekoia feed artefact in Cortex

Here is an example on how to verify if a Sekoia Indicator exist in Cortex and import its content for verification (same process for Context and Observable)

{% hint style="info" %}
* IOC (associated threat) is found on Indicator
* Details of an Indicator (IOC) is found on Indicator
* Observables is found on Observable
{% endhint %}

1. Go to Sekoia.io connector `Analyzers > SEKOIAIntelligenceCenter_Indicators` and click on button Run (button play symbol in the right side)

![TheHive\_Sekoia\_connector1](../../.gitbook/assets/search_SekoiaCTI-1_indicators.png)

2. Fill the information with the indicator ![TheHive\_Sekoia\_connector2a](../../.gitbook/assets/search_SekoiaCTI-2_indicators.png)
3. Check the indicator in _Jobs History_ ![TheHive\_Sekoia\_job](../../.gitbook/assets/search_SekoiaCTI-3_indicators.png)
4. Check the Sekoia indicator ![TheHive\_Sekoia\_feed1](../../.gitbook/assets/search_SekoiaCTI-4_indicators.png)
5. Check the Indicator in Sekoia Intelligence page ![TheHive\_Sekoia\_objects](../../.gitbook/assets/searchCTI_Sekoia_objects.png)

## 5. Troubleshoot

1. Make a verification on the artefact, follow steps of `Verify a Sekoia feed artefact in Cortex` (see previous section)
2. Check the jobs in _Jobs History_ tab to see if the observable or the indicator have been retrieved AND
3. Compare this artefact in Sekoia Intelligence Center under the Intelligence page

## 6. Other resources

* **The Cortex official documentation**

https://github.com/TheHive-Project/CortexDocs/blob/master/installation/install-guide.md#docker

http://docs.thehive-project.org/cortex/user-guides/first-start/

https://github.com/TheHive-Project/CortexDocs/blob/master/admin/quick-start.md
