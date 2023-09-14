# External Integrations: Cortex Analyzer

SEKOIA is providing a [Cortex analyzer](https://github.com/TheHive-Project/Cortex-Analyzers/tree/master/analyzers/SEKOIAIntelligenceCenter) to enrich data in [TheHive](https://thehive-project.org/) ecosystem.

## Objective

Collect Sekoia.io CTI feed in an existing Cortex instance self-managed, for any operational purpose such as CTI aggregation, dissemination, hunting...

## Prerequisites:

- An operational Cortex instance with administrator privileges
- An active Sekoia.io licence with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key with [CTI permissions](https://docs.sekoia.io/getting_started/Permissions/#cti-permissions)

!!!note
   Sekoia Intelligence Center will be available upon Cortex setup

## 1. Connect to Cortex

1- In a Web browser, type the following	_http://server_ip:Cortex_port_

2- Enter your login and password of your Cortex instance setup beforehand


## 2. Configuration
**1- Setup the organization**

1- Connect into Cortex with `orgadmin` role

2- Select your _organization_ on the top right corner
![Orga_setup_1](../../../../docs/assets/intelligence_center/Orga_setup_1.png){: style="width: 100%; max-width: 100%"}

3- Go to _Analyzers Config_ tab and Search `SekoiaIntelligenceCenter`
![Orga_setup_2](../../../../docs/assets/intelligence_center/Orga_setup_2.png){: style="width: 100%; max-width: 100%"}

4- Edit and Add your Sekoia API key and Base url
![Orga_setup_3](../../../../docs/assets/intelligence_center/Orga_setup_3.png){: style="width: 100%; max-width: 100%"}

**2- Check Sekoia intelligence**
1- Go to _Analyzers_ tab and Search `SekoiaIntelligenceCenter`
![Analyzer_ config_1](../../../../docs/assets/intelligence_center/Analyzer_ config_1.png){: style="width: 100%; max-width: 100%"}

2- Edit and Add your Sekoia API key and Base url
![Analyzer_ config_2](../../../../docs/assets/intelligence_center/Analyzer_ config_2.png){: style="width: 100%; max-width: 100%"}

**3- Check Sekoia intelligence**

1- Go to job page

2- Select `SekoiaIntelligenceCenter` in _Analyzers_
![job_1](../../../../docs/assets/intelligence_center/job_1.png){: style="width: 100%; max-width: 100%"}

3- Click on `view` to see details of the job
![job_2](../../../../docs/assets/intelligence_center/job_2.png){: style="width: 100%; max-width: 100%"}

## 3. Troubleshoot
1- Go to _Analyzers_ tab > Run an analyzer

2- Check the jobs in _Jobs History_ tab

## 4. Other resources
- **The Cortex official documentation**
https://github.com/TheHive-Project/CortexDocs/blob/master/installation/install-guide.md#docker
http://docs.thehive-project.org/cortex/user-guides/first-start/
https://github.com/TheHive-Project/CortexDocs/blob/master/admin/quick-start.md
