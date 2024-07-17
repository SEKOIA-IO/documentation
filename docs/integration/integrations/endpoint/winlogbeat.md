uuid: c10307ea-5dd1-45c6-85aa-2a6a900df99b
name: Winlogbeat
type: intake

## Overview

Winlogbeat is an open-source log collector that ships Windows Event Logs as JSON events.

{!_shared_content/operations_center/detection/generated/suggested_rules_c10307ea-5dd1-45c6-85aa-2a6a900df99b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c10307ea-5dd1-45c6-85aa-2a6a900df99b.md!}

## Transport to the collector

### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the host
- Traffic towards a logstash server which must listen beats input on port `TCP/5044`

### Configure the client

#### Install and configure Winlogbeat

1. Download Winlogbeat zip from the Elastic.co [download page](https://www.elastic.co/downloads/beats/winlogbeat)
2. Extract the archive into `C:\Program Files\winlogbeat`
3. Open a PowerShell prompt as an Administrator and run the following commands to install the service

	```powershell
	PS C:\Users\Administrator> cd 'C:\Program Files\winlogbeat'
	PS C:\Program Files\winlogbeat> .\install-service-winlogbeat.ps1
	```

4. Replace the configuration file `C:\Program Files\winlogbeat\winlogbeat.yml` by the following content:

	```yaml
	winlogbeat.event_logs:
	  - name: Application
	    ignore_older: 72h
	  - name: System
	  - name: Security
	  - name: ForwardedEvents
	    tags: [forwarded]
	  - name: Windows PowerShell
	    event_id: 400, 403, 600, 800
	  - name: Microsoft-Windows-PowerShell/Operational
	    event_id: 4103, 4104, 4105, 4106

	# ====================== Elasticsearch template settings =======================

	setup.template.settings:
	  index.number_of_shards: 1
	  #index.codec: best_compression
	  #_source.enabled: false

	# ================================== Outputs ===================================

	# Configure what output to use when sending the data collected by the beat.

	# ---------------------------- Elasticsearch Output ----------------------------
	output.elasticsearch:
	  enabled: false

	# ------------------------------ Logstash Output -------------------------------

	output.logstash:
	  # The Logstash hosts
	  hosts: ["logstash_concentrator:5044"]

	  # Optional SSL. By default is off.
	  # List of root certificates for HTTPS server verifications
	  #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

	  # Certificate for SSL client authentication
	  #ssl.certificate: "/etc/pki/client/cert.pem"

	  # Client Certificate Key
	  #ssl.key: "/etc/pki/client/cert.key"

	# ================================= Processors =================================

	processors:
	  - add_host_metadata:
	      when.not.contains.tags: forwarded
	  - add_cloud_metadata: ~

	# ================================== Logging ===================================

	logging.level: info
	#logging.to_files: true
	#logging.files:
	  #path: C:\ProgramData\winlogbeat\Logs
	  #name: winlogbeat
	  #keepfiles: 7
	  #permissions: 0640
	```

	!!! warning
	    Don't forget to specify the location of your logstash server in this configuration

5. Save and validate the configuration with the command:

	```powershell
	PS C:\Program Files\Winlogbeat> .\winlogbeat.exe test config -c .\winlogbeat.yml -e
	```

6. Set up assets:

	```powershell
	PS C:\Program Files\Winlogbeat> .\winlogbeat.exe setup -e
	```

7. Start the Winlogbeat service:

	```powershell
	PS C:\Program Files\Winlogbeat> Start-Service winlogbeat
	```

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Winlogbeat.

## Forward logs to Sekoia.io

Please consult our [guide](../../../ingestion_methods/logstash/) to configure logs forwarding from Logstash to Sekoia.io.

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.

## Further Readings
- [Winlogbeat documentation](https://www.elastic.co/guide/en/beats/winlogbeat/current/_winlogbeat_overview.html)
- [Winlogbeat configuration](https://github.com/elastic/beats/blob/main/winlogbeat/winlogbeat.yml)
