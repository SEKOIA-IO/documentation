uuid: dc0f339f-5dbe-4e68-9fa0-c63661820941
name: Zscaler Internet Access
type: intake

## Overview
Zscaler Internet Access is a cloud-native security platform that delivers secure and direct internet access for users and devices, providing real-time protection against cyber threats while enabling secure and efficient web access from anywhere.

- **Vendor**: Zscaler
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Process monitoring, Process use of network

### Supported logs

This integration can ingest the following logs:

- `Admin Audit`
- `DNS logs`
- `Firewall Logs`
- `SaaS Security`
- `SaaS Security Activity`
- `Tunnel`
- `Web Log`



## Configure

This section will guide you on how to forward Zscaler ZIA events to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Zscaler ZIA`format.

### Forward events with NSS Servers

#### Prerequisites

You must have an internal log concentrator to forward events with NSS servers.

#### Configure the forwarding

In the Zscaler ZIA console:

1. Go to `Administration` > `Cloud Configuration` > `Nanolog Streaming Service`
   ![menu](/assets/integration/cloud_and_saas/zscaler/zia_menu.png){: style="max-width:100%"}
2. Select the `NSS Feeds` tab
   ![nanolog](/assets/integration/cloud_and_saas/zscaler/zia_nss_feeds.png){: style="max-width:50%"}
3. Select `Add NSS Feed` for each log type you want to forward
4. In the modal, type a name for the feed, select the `NSS Server`, and then select the `Enabled`status
5. In the `SIEM IP Address` field, enter the IP address of the log concentrator
6. In the `SIEM TCP Port` field, enter the port of the log concentrator
7. Select the desired log type
8. Select `Custom` as the `Feed Output Type`. When possible, fill the `Feed Escape Character` input with the characters `,\"`
9. For `Feed Output Format`, paste the following format according to the log type:
	
	For RFC3164 format:

	=== "Web Log"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-web", "event" : \{"datetime":"%d{yy}-%02d{mth}-%02d{dd} %02d{hh}:%02d{mm}:%02d{ss}","reason":"%s{reason}","event_id":"%d{recordid}","protocol":"%s{proto}","action":"%s{action}","transactionsize":"%d{totalsize}","responsesize":"%d{respsize}","requestsize":"%d{reqsize}","urlcategory":"%s{urlcat}","serverip":"%s{sip}","requestmethod":"%s{reqmethod}","refererURL":"%s{ereferer}","useragent":"%s{eua}","product":"NSS","location":"%s{elocation}","ClientIP":"%s{cip}","status":"%s{respcode}","user":"%s{elogin}","url":"%s{eurl}","vendor":"Zscaler","hostname":"%s{ehost}","clientpublicIP":"%s{cintip}","threatcategory":"%s{malwarecat}","threatname":"%s{threatname}","filetype":"%s{filetype}","appname":"%s{appname}","pagerisk":"%d{riskscore}","department":"%s{edepartment}","urlsupercategory":"%s{urlsupercat}","appclass":"%s{appclass}","dlpengine":"%s{dlpeng}","urlclass":"%s{urlclass}","threatclass":"%s{malwareclass}","dlpdictionaries":"%s{dlpdict}","fileclass":"%s{fileclass}","bwthrottle":"%s{bwthrottle}","contenttype":"%s{contenttype}","unscannabletype":"%s{unscannabletype}","deviceowner":"%s{deviceowner}","devicehostname":"%s{devicehostname}","keyprotectiontype":"%s{keyprotectiontype}"\}\}
		```

	=== "SaaS Security"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-casb", "event" :\{"datetime":"%s{time}","recordid":"%d{recordid}","company":"%s{company}","tenant":"%s{tenant}","login":"%s{user}","dept":"%s{department}","applicationname":"%s{applicationname}","filename":"%s{filename}","filesource":"%s{filesource}","filemd5":"%s{filemd5}","threatname":"%s{threatname}","policy":"%s{policy}","dlpdictnames":"%s{dlpdictnames}","dlpdictcount":"%s{dlpdictcount}","dlpenginenames":"%s{dlpenginenames}","fullurl":"%s{fullurl}","lastmodtime":"%s{lastmodtime}","filescantimems":"%d{filescantimems}","filedownloadtimems":"%d{filedownloadtimems}"\}\}
		```

	=== "SaaS Security Activity"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-casb", "event" :\{"login":"%s{username}","tenant":"%s{tenant}","object_type":"%d{objtype1}","applicationname":"%s{appname}","object_name_1":"%s{objnames1}","object_name_2":"%s{objnames2}"\}\}
		```

	=== "Tunnel IKE Phase 1"
		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","destinationport":"%d{dstport}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","spi_in":"%lu{spi_in}","spi_out":"%lu{spi_out}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","recordid":"%d{recordid}"\}\}
		```

	=== "Tunnel IKE Phase 2"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","sourceportstart":"%d{srcportstart}","destinationportstart":"%d{destportstart}","srcipstart":"%s{srcipstart}","srcipend":"%s{srcipend}","destinationipstart":"%s{destipstart}","destinationipend":"%s{destipend}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","lifebytes":"%d{lifebytes}","spi":"%d{spi}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","protocol":"%s{protocol}","tunnelprotocol":"%s{tunnelprotocol}","policydirection":"%s{policydirection}","recordid":"%d{recordid}"\}\}
		```

	=== "Tunnel"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"%s{tunneltype}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","event":"%s{event}","eventreason":"%s{eventreason}","recordid":"%d{recordid}"\}\}
		```

	=== "Admin Audit"

		```
		%s{mon} %02d{dd} %02d{hh}:%02d{mm}:%02d{ss} zscaler-nss NSS \{"sourcetype" : "zscalernss-audit", "event" :\{"time":"%s{time}","recordid":"%d{recordid}","action":"%s{action}","category":"%s{category}","subcategory":"%s{subcategory}","resource":"%s{resource}","interface":"%s{interface}","adminid":"%s{adminid}","clientip":"%s{clientip}","result":"%s{result}","errorcode":"%s{errorcode}","auditlogtype":"%s{auditlogtype}","preaction":"%s{epreaction}","postaction":"%s{epostaction}"\}\}
		```

	For RFC5424 format:

	=== "Web Log"

		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-web","event":\{"datetime":"%d{yy}-%02d{mth}-%02d{dd} %02d{hh}:%02d{mm}:%02d{ss}","reason":"%s{reason}","event_id":"%d{recordid}","protocol":"%s{proto}","action":"%s{action}","transactionsize":"%d{totalsize}","responsesize":"%d{respsize}","requestsize":"%d{reqsize}","urlcategory":"%s{urlcat}","serverip":"%s{sip}","requestmethod":"%s{reqmethod}","refererURL":"%s{ereferer}","useragent":"%s{eua}","product":"NSS","location":"%s{elocation}","ClientIP":"%s{cip}","status":"%s{respcode}","user":"%s{elogin}","url":"%s{eurl}","vendor":"Zscaler","hostname":"%s{ehost}","clientpublicIP":"%s{cintip}","threatcategory":"%s{malwarecat}","threatname":"%s{threatname}","filetype":"%s{filetype}","appname":"%s{appname}","pagerisk":"%d{riskscore}","department":"%s{edepartment}","urlsupercategory":"%s{urlsupercat}","appclass":"%s{appclass}","dlpengine":"%s{dlpeng}","urlclass":"%s{urlclass}","threatclass":"%s{malwareclass}","dlpdictionaries":"%s{dlpdict}","fileclass":"%s{fileclass}","bwthrottle":"%s{bwthrottle}","contenttype":"%s{contenttype}","unscannabletype":"%s{unscannabletype}","deviceowner":"%s{deviceowner}","devicehostname":"%s{devicehostname}","keyprotectiontype":"%s{keyprotectiontype}"\}\}
		```

	=== "SaaS Security"

		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-casb","event":\{"datetime":"%s{time}","recordid":"%d{recordid}","company":"%s{company}","tenant":"%s{tenant}","login":"%s{user}","dept":"%s{department}","applicationname":"%s{applicationname}","filename":"%s{filename}","filesource":"%s{filesource}","filemd5":"%s{filemd5}","threatname":"%s{threatname}","policy":"%s{policy}","dlpdictnames":"%s{dlpdictnames}","dlpdictcount":"%s{dlpdictcount}","dlpenginenames":"%s{dlpenginenames}","fullurl":"%s{fullurl}","lastmodtime":"%s{lastmodtime}","filescantimems":"%d{filescantimems}","filedownloadtimems":"%d{filedownloadtimems}"\}\}
		```

	=== "SaaS Security Activity"

		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-casb","event":\{"login":"%s{username}","tenant":"%s{tenant}","object_type":"%d{objtype1}","applicationname":"%s{appname}","object_name_1":"%s{objnames1}","object_name_2":"%s{objnames2}"\}\}
		```

	=== "Tunnel IKE Phase 1"
		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-tunnel","event":\{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","destinationport":"%d{dstport}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","spi_in":"%lu{spi_in}","spi_out":"%lu{spi_out}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","recordid":"%d{recordid}"\}\}
		```

	=== "Tunnel IKE Phase 2"

		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-tunnel","event":\{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","sourceportstart":"%d{srcportstart}","destinationportstart":"%d{destportstart}","srcipstart":"%s{srcipstart}","srcipend":"%s{srcipend}","destinationipstart":"%s{destipstart}","destinationipend":"%s{destipend}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","lifebytes":"%d{lifebytes}","spi":"%d{spi}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","protocol":"%s{protocol}","tunnelprotocol":"%s{tunnelprotocol}","policydirection":"%s{policydirection}","recordid":"%d{recordid}"\}\}
		```

	=== "Tunnel"

		```
		<134>1 %d{yyyy}-%02d{mm}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-tunnel","event":\{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"%s{tunneltype}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","event":"%s{event}","eventreason":"%s{eventreason}","recordid":"%d{recordid}"\}\}
		```

	=== "Admin Audit"

		```
		<134>1 %d{yyyy}-%02d{mth}-%02d{dd}T%02d{hh}:%02d{mm}:%02d{ss}Z zscaler-nss NSS - - - event=\{"sourcetype":"zscalernss-audit","event":\{"time":"%s{time}","recordid":"%d{recordid}","action":"%s{action}","category":"%s{category}","subcategory":"%s{subcategory}","resource":"%s{resource}","interface":"%s{interface}","adminid":"%s{adminid}","clientip":"%s{clientip}","result":"%s{result}","errorcode":"%s{errorcode}","auditlogtype":"%s{auditlogtype}","preaction":"%s{epreaction}","postaction":"%s{epostaction}"\}\}
		```

10. Select `Save`

#### Forward logs to Sekoia.io

For more information on forwarding logs to Sekoia.io, see [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md)

### Forward events with Cloud NSS Feed

In the Zscaler ZIA console:

1. Go to `Administration` > `Cloud Configuration` > `Nanolog Streaming Service`
   ![menu](/assets/integration/cloud_and_saas/zscaler/zia_menu.png){: style="max-width:100%"}
2. Select the `Cloud NSS Feeds` tab
   ![nanolog](/assets/integration/cloud_and_saas/zscaler/zia_cloud.png){: style="max-width:100%"}
3. Select `Add Clous NSS Feed` for each log type you want to forward
4. In the modal, in the `General section`, enter a name for the feed, select the status `Enabled`. According to the log type you want to forward, select the `NSS type`
    1. For `Admin Audit`, `SaaS Security`, `SaaS Security Activity` and `Web Log`, select `NSS for web`
      ![General/web](/assets/integration/cloud_and_saas/zscaler/zia_general_web.png){: style="max-width:100%"}
    2. For `Firewall Logs` or `DNS logs`, select `NSS for firewall`
      ![General/firewall](/assets/integration/cloud_and_saas/zscaler/zia_general_firewall.png){: style="max-width:100%"}
5. In the `SIEM Connectivity` section
    1. Select `Other` as the `SIEM Type`
    2. Turn off the `OAUTH2.0 Authentication`toggle
    3. In the `Max batch size` field, enter `512 kb`
    4. As the API URL, enter `HTTP_INTAKE_ENDPOINT/plain/batch?status_code=200`. You can find the value for HTTP_INTAKE_ENDPOINT [here](https://docs.sekoia.io/getting_started/regions/), depending on your region. For instance, on FRA1 platform you will use `https://intake.sekoia.io/plain/batch?status_code=200`
    5. Select `Add HTTP Header` and add the HTTP header `X-SEKOIAIO-INTAKE-KEY` with our intake key as the value
    ![Connectivity](/assets/integration/cloud_and_saas/zscaler/zia_siem_connectivity.png){: style="max-width:100%"}
6. In the `Formatting` section
    1. Select the desired `Log type`
    2. Select `JSON` as the `Feed Output Type`
    3. Turn off the `JSON Array Notation`toggle
    4. Keep `Feed Escape Character` with the characters `,\"`
    5. Keep `Feed Output Format` unchanged
    6. Keep `Timezone` to `GMT`
    ![Formatting](/assets/integration/cloud_and_saas/zscaler/zia_formatting.png){: style="max-width:100%"}
7. Select `Save`


{!_shared_content/operations_center/integrations/generated/dc0f339f-5dbe-4e68-9fa0-c63661820941_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_dc0f339f-5dbe-4e68-9fa0-c63661820941_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/dc0f339f-5dbe-4e68-9fa0-c63661820941.md!}

## Further Readings

- [Zscaler - Nanolog Streaming Service](https://help.zscaler.com/zia/nanolog-streaming-service)
