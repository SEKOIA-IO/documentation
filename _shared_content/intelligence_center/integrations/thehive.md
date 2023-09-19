# External Integrations: Cortex Analyzer

Sekoia.io is providing a [Cortex analyzer](https://github.com/TheHive-Project/Cortex-Analyzers/tree/master/analyzers/SEKOIAIntelligenceCenter) to enrich data in [TheHive](https://thehive-project.org/) ecosystem.

## Objective

Collect Sekoia.io CTI feed in an existing Cortex instance self-managed, for any operational purpose such as CTI aggregation, dissemination, hunting...

## Prerequisites:

- An operational Cortex instance with administrator privileges
- An active Sekoia.io licence with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key with [CTI permissions](https://docs.sekoia.io/getting_started/Permissions/#cti-permissions)

!!!note
   Sekoia Intelligence feed will be available upon Cortex setup

## 1. Connect to Cortex

1- In a Web browser, type the following	_http://server_ip:cortex_port_

2- Enter your login and password of your Cortex instance setup beforehand with `orgadmin` role


## 2. Configuration

#### 1- Setup the Analyzer configuration

   1- Select your _Organization_ on the top right corner
![Orga_setup_1](/assets/intelligence_center/orga_setup_1.png){: style="width: 100%; max-width: 100%"}

   2- Go to _Analyzers Config_ tab and Search `SekoiaIntelligenceCenter`
![Orga_setup_2](/assets/intelligence_center/orga_setup_2.png){: style="width: 100%; max-width: 100%"}

   3- Edit and Add your Sekoia API key and Base url
![Orga_setup_3](/assets/intelligence_center/orga_setup_3.png){: style="width: 100%; max-width: 100%"}

#### 2- Enable and Setup the Analyzer

The configuration setup in the previous section  will provide 3 Analyzers to enable and setup :
- SEKOIAIntelligenceCenter_Context_1_0
- SEKOIAIntelligenceCenter_Indicators_1_0 
- SEKOIAIntelligenceCenter_Observables_1_0

Here is below one example of setup to be done for the 3 analyzers:

   1- Go to _Analyzers_ tab and Search `SekoiaIntelligenceCenter`
![Analyzer_ config_1](/assets/intelligence_center/analyzer_config_1.png){: style="width: 100%; max-width: 100%"}

   2- Edit and Add your Sekoia API key and Base url
![Analyzer_ config_2](/assets/intelligence_center/analyzer_config_2.png){: style="width: 100%; max-width: 100%"}


## 3. Sekoia intelligence in TheHive Cortex

Here is an example on how to retrieve Sekoia feed on the 3 analyzers (and the match on Sekoia intelligence)

|Analyzers|Cortex|Sekoia.io|
|--|--|--|
|SEKOIAIntelligenceCenter_Context_1_0|context of an observable|Indicator side details (Related threats, Linked Observables, Latest reports, Indicator types,Kill chain)|
|SEKOIAIntelligenceCenter_Indicators_1_0 |indicators|Indicators under objects tab (details)|
|SEKOIAIntelligenceCenter_Observables_1_0|known observables|Observable under observable tab|

*Steps*

1- Go to Sekoia connector    _Analyzers > SEKOIAIntelligenceCenter_ (any) and click on button Run

![TheHive_Sekoia_connector1](/assets/intelligence_center/search_SekoiaCTI-1.png){: style="width: 100%; max-width: 100%"}

2- Fill the information (depending on which elements you would like to retrieve)

- Indicator
![TheHive_Sekoia_connector2a](/assets/intelligence_center/search_SekoiaCTI-2_indicators.png){: style="width: 100%; max-width: 100%"}

- Indicator side details
![TheHive_Sekoia_connector2b](/assets/intelligence_center/search_SekoiaCTI-2_context.png){: style="width: 100%; max-width: 100%"}

- Observable
![TheHive_Sekoia_connector2c](/assets/intelligence_center/search_SekoiaCTI-2_observables.png){: style="width: 100%; max-width: 100%"}


3- Check the observable in Jobs History
![TheHive_Sekoia_job](/assets/intelligence_center/search_SekoiaCTI-3.png){: style="width: 100%; max-width: 100%"}

4- Check the Sekoia feed

- Observable
![TheHive_Sekoia_feed1](/assets/intelligence_center/search_SekoiaCTI-4_Object.png){: style="width: 100%; max-width: 100%"}

- Object context
![TheHive_Sekoia_feed2](/assets/intelligence_center/search_SekoiaCTI-4_Object_context.png){: style="width: 100%; max-width: 100%"}

- Object
![TheHive_Sekoia_feed3](/assets/intelligence_center/search_SekoiaCTI-4_Observable.png){: style="width: 100%; max-width: 100%"}


*To only search existing Sekoia Intelligence feed*
![TheHive_Sekoia_connector1](/assets/intelligence_center/searchExisting_SekoiaCTI.png){: style="width: 100%; max-width: 100%"}

## 4. Where to find Sekoia intelligence feed ?

Search in Sekoia Intelligence page

- Observable
![TheHive_Sekoia_Observable](/assets/intelligence_center/searchCTI_Sekoia_observables.png){: style="width: 50%; max-width: 50%"}

- Indicators
![TheHive_Sekoia_objects](/assets/intelligence_center/searchCTI_Sekoia_objects.png){: style="width: 100%; max-width: 100%"}


## 5. Troubleshoot

1- Go to _Analyzers_ tab > Run an analyzer

2- Check the jobs in _Jobs History_ tab

## 6. Other resources

- **The Cortex official documentation**

https://github.com/TheHive-Project/CortexDocs/blob/master/installation/install-guide.md#docker

http://docs.thehive-project.org/cortex/user-guides/first-start/

https://github.com/TheHive-Project/CortexDocs/blob/master/admin/quick-start.md

