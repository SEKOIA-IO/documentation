# External Integrations: Splunk

Sekoia is providing an application for Splunk to detect threats in your logs based on Sekoia.io CTI feed.
 
## Prerequisites

- An operational Splunk instance with administrator privileges (**Enterprise** for OnPrem or **Cloud** for the Saas version)
- An active Sekoia.io license with access to the CTI
- An access to Sekoia.io User Center with the role that contains the permission to [create an API key](https://docs.sekoia.io/getting_started/manage_api_keys/) (e.g. Built-in [Analyst Role](https://docs.sekoia.io/getting_started/roles/#functionality-of-built-in-roles) or create a custom role with [ic_viewer permissions](https://docs.sekoia.io/getting_started/roles/#legacy-roles) <a name="api_key"></a>

!!!note
    This following guide is for Splunk solutions (**Enterprise** (OnPrem) or Splunk **Cloud** (Cloud)).

## 1. Connect to Splunk Enterprise

1. In a Web browser, type the following and replace `server_ip` and `port` by their values:
   http://server_ip:port

   !!!note
       For Cloud version, only the next step is required
   
   2. Enter your login and password of your Splunk Enterprise instance
![Splunk-Login](/assets/intelligence_center/Splunk/Splunk-Login.png){: style="width: 60%; max-width: 60%"}

## 2.  Install and configure your Sekoia application for Splunk

1. Go to Application Setup Page by clicking on `Apps` > `Find more Apps`
![Splunk_Applications_access](/assets/intelligence_center/Splunk/Splunk_Applications_access.png){: style="width: 40%; max-width: 40%"}
   
2. Search for `Sekoia.io` application and install it
![Splunk-Sekoia_in_App](/assets/intelligence_center/Splunk/Splunk-Sekoia_in_App.png)
   
3. Configure your Sekoia application for Splunk by completing fields
![Splunk-Sekoia_API_key_in_Sekoia_application](/assets/intelligence_center/Splunk/Splunk-Sekoia_API_key_in_Sekoia_application.png)

_Please find below the explanation of the fields to be configured_

**Required**

- `SEKOIA.IO API Key`: Sekoia API Key to be created as stated in the [Prerequisites](#api_key)

**Optional**

- `Sekoia API url`: the default url is https://api.sekoia.io
- `Feed ID`: default feed is used by default. For custom feed, add the feed ID. Please find [more information on this documentation](https://docs.sekoia.io/cti/features/consume/feeds/#feeds-listing)
- `Proxy URL` - Here are 2 ways to configure a proxy:
    1. If you need the Sekoia application for Splunk to connect directly through a proxy, this field needs to be filled on the installation page (To connect, in a Web browser, type and replace `username`, `password`,`host` and `port` by their values: http://[username:password@]host:port)
    2. If you don't want to distinguish the Sekoia application for Splunk network configuration from the configuration of your Splunk instance, the Sekoia application for Splunk takes into account the global Splunk proxy configuration provided by means of the `HTTP_PROXY` and `HTTPS_PROXY` environment variables.

!!! note
     After the launch of Sekoia application for Splunk, only valid IOCs of [these types](#sourcetype) will be downloaded and updated on Splunk from current date.

## 3. Sekoia Intelligence in Splunk

In the following section, here are the Sekoia IOC types available in Splunk: <a name="sourcetype"></a>

|IOC type|Meaning|
|--|--|
|domain| Domain name	|
|url	|  Url website 		|
|ipv4	| Internet Protocol version 4 (32-bit number e.g. `111.111.1.11` )		|
|md5	| Cryptographic hash function that results in a 128-bit hash value	|
|sha1	| Hash function which takes an input and produces a 160-bit (20-byte) 	|
|sha256| Secure Hash Algorithm 256-bit	|

An IOC is an observable that represents a malicious activity. For more information, please consult [this page](https://docs.sekoia.io/cti/features/consume/observables/).

!!! note
     Only these Sekoia Indicator types will be updated.
     
     Update is **scheduled every night** to ensure that valid IOCs are used to detect threats.

## 4. Search Sekoia Intelligence and match with IOCs in Splunk

### Search existing Sekoia IOCs in Splunk with expiry date

1. Go to Application Setup Page by clicking on `Apps` > `Sekoia.io`
2. In the search tab, query on `| inputlookup sekoia_iocs_url | rename _key as indicator | convert ctime(valid_until)`

![Splunk-Search_IOCs_validity](/assets/intelligence_center/Splunk/Splunk-Search_IOCs_validity.png)

### Search and compare Sekoia IOCs with logs in Splunk

!!! note
     Logs have to be collected in Splunk. Please consult [Splunk documentation](https://www.splunk.com/en_us/blog/learn/centralized-logging.html).

1. Setup a lookup table
 
    A typical query would be `index=* sourcetype=<YOUR_SOURCETYPE>` (`<YOUR_SOURCETYPE>` is to be replaced by the **Sekoia IOCs types** listed [above](#sourcetype)).

    When installing Sekoia application for Splunk, a message will be displayed requesting to configure the lookup table.

2. Sightings will be displayed on a section
![Sekoia.io App for Splunk](/assets/intelligence_center/splunk.png)

Please refer to [our documentation to search IOCs in Intelligence page](https://docs.sekoia.io/cti/features/consume/intelligence/#search-for-objects) for more information.

## 5. Troubleshoot

### 1. False positive

Compare Sekoia IOCs valid date in [Sekoia Intelligence](https://docs.sekoia.io/cti/features/consume/intelligence/#search-bars).

### 2. Splunk issues

Search in the Internal logs for errors. Please consult [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/9.1.2/Troubleshooting/WhatSplunklogsaboutitself) for more information.

## 6. Other resources

- **Sekoia.io App for Splunk**

[https://github.com/SEKOIA-IO/SEKOIA.IO-for-Splunk](https://github.com/SEKOIA-IO/SEKOIA.IO-for-Splunk)

- **Splunk official documentation**

[https://splunkbase.splunk.com/app/6327](https://splunkbase.splunk.com/app/6327)

[https://community.splunk.com/t5/Installation/bd-p/installation](https://community.splunk.com/t5/Installation/bd-p/installation)

[https://docs.splunk.com/Documentation/SplunkCloud/9.1.2308/SearchTutorial/InstallSplunk](https://docs.splunk.com/Documentation/SplunkCloud/9.1.2308/SearchTutorial/InstallSplunk)

[https://docs.splunk.com/Documentation/SplunkCloud/9.1.2308/SearchTutorial/NavigatingSplunk](https://docs.splunk.com/Documentation/SplunkCloud/9.1.2308/SearchTutorial/NavigatingSplunk) 
