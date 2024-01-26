# External Integrations: Splunk

Sekoia is providing an app for Splunk to detect threats in your logs based on our feed.

## Objective
Collect Sekoia.io CTI feed in an existing Splunk instance self-managed, for any operational purpose such as CTI aggregation, dissemination, hunting...
 
## Prerequisites:

- An operational Splunk Enterprise instance with administrator privileges
- An active Sekoia.io license with access to the CTI
- An access to Sekoia.io User Center with the permissions to create an API key with [CTI permissions](https://docs.sekoia.io/getting_started/Permissions/#cti-permissions)

## 1. Connect to Splunk

!!!note
    Splunk instance must be activated on your server

1. In a Web browser, type the following and replace `server_ip` and `port` by their values:
   http://server_ip:port
   
2. Enter your login and password of your Splunk instance
![Splunk-Login](/assets/intelligence_center/Splunk/Splunk-Login.png)

## 2.  Install and configure your Splunk TA

1. Go to Application Setup Page `Apps` > `Find more Apps`
![Splunk_Applications_access](/assets/intelligence_center/Splunk/Splunk_Applications_access.png){: style="width: 40%; max-width: 40%"}
   
2. Search for Sekoia.io application and and install it
![Splunk-Sekoia_in_App](/assets/intelligence_center/Splunk/Splunk-Sekoia_in_App.png)
   
3. Configure your Sekoia.io Application (with your Sekoia.io API Key, Sekoia.io API url  and feed ID)
![Splunk-Sekoia_API_key_in_Sekoia_application](/assets/intelligence_center/Splunk/Splunk-Sekoia_API_key_in_Sekoia_application.png)

Please consult [our documentation for feed ID](https://docs.sekoia.io/cti/features/consume/feeds/#feeds-listing)

!!! note
     After the launch of Sekoia.io app, IOCs will be downloaded and updated on Splunk
        
## 3. Sekoia intelligence in Splunk

In the following section, here are the Sekoia IOCs available in Splunk:

|IOC type|Meaning|
|--|--|
|domain| domaine name	|
|url	|  Website url		|
|ipv4	| Internet Protocol version 4 (32-bit number e.g. 111.111.1.11 )		|
|md5	| Cryptographic hash function that results in a 128-bit hash value	|
|sha1	| Hash function which takes an input and produces a 160-bit (20-byte) 	|
|sha256| Secure Hash Algorithm 256-bit	|

An IOC is an observable that represents a malicious activity. For more information, please consult [this page](https://docs.sekoia.io/cti/features/consume/observables/)

!!! note
     Only Sekoia Indicators will be updated.
     Update is scheduled every night to ensure that valid IOCs are used to detect threats.

## 4. Search Sekoia intelligence and match with IOCs in Splunk TA

[WORK IN PROGRESS]

### Search existing Sekoia IOCs in Splunk TA with expiry date

1. Click on Sekoia.io on Application page
2. Go to the Seek tab and query on 
`| inputlookup sekoia_iocs_url | rename _key as indicator | convert ctime(valid_until)`

![Splunk-Search_IOCs_validity](/assets/intelligence_center/Splunk/Splunk-Search_IOCs_validity.png)

### Search and compare Sekoia IOCs with logs in Splunk

!!! note
     Prerequisites: Logs have to be collected in Splunk

1. Setup a lookup table - A typical query would be `index=* sourcetype=<YOUR_SOURCETYPE>`

!!! note
     When installing Sekoia CTI integration, a message will be displayed requesting to configure the lookup table.

2. Sightings will be displayed on this section of the Sekoia integration
![Sekoia.io App for Splunk](/assets/intelligence_center/splunk.png){: style="width: 100%; max-width: 100%"}

Please refer to [our documentation to search IOCs in Intelligence page](https://docs.sekoia.io/cti/features/consume/intelligence/#search-for-objects) for more information

## 5. Troubleshoot
[WORK IN PROGRESS]

**1. False positive**

Compare Sekoia IOCs valid date in Sekoia Intelligence

**2. Splunk issues**

Please search in the Internal logs for errors

Please consult [Splunk documentation on this subject](https://docs.splunk.com/Documentation/Splunk/9.1.2/Troubleshooting/WhatSplunklogsaboutitself)  for more information

## 6. Other resources

- **Sekoia.io App for Splunk**

https://github.com/SEKOIA-IO/SEKOIA.IO-for-Splunk

- **Splunk TA official documentation**

https://splunkbase.splunk.com/app/6327

https://community.splunk.com/t5/Installation/bd-p/installation
