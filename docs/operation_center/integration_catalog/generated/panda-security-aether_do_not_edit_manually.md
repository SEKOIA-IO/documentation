
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Asset Management` | Panda Aether integrates every Panda Endpoints in a single management console. |





In details, the following Table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `metric` |
| Category | `host` |
| Type | `info` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "CountsofSecurityEvents.json"

    ```json
	
    {
        "event": {
            "category": [
                "host"
            ],
            "kind": "metric",
            "outcome": "success",
            "type": [
                "info"
            ]
        },
        "aether": {
            "exploit_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "malware_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "program_blocked_counters": {
                "total_programs_blocked": 1
            },
            "pups_counters": {
                "total_affected_devices": 1,
                "total_alerts": 1,
                "total_data_access": 1,
                "total_executed": 1,
                "total_external_communications": 1
            },
            "threats_by_av_counters": {
                "total_dangerous_actions_blocked_by_av": 1,
                "total_devices_blocked_by_av": 1,
                "total_intrusion_attempted_blocked_by_av": 1,
                "total_malware_urls_blocked_by_av": 1,
                "total_phishing_detected_by_av": 1,
                "total_tracking_cookies_detected_by_av": 1
            }
        },
        "ecs": {
            "version": "1.10.0"
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`aether.exploit_counters.total_affected_devices` | `long` | None |
|`aether.exploit_counters.total_alerts` | `long` | None |
|`aether.exploit_counters.total_data_access` | `long` | None |
|`aether.exploit_counters.total_executed` | `long` | None |
|`aether.exploit_counters.total_external_communications` | `long` | None |
|`aether.malware_counters.total_affected_devices` | `long` | None |
|`aether.malware_counters.total_alerts` | `long` | None |
|`aether.malware_counters.total_data_access` | `long` | None |
|`aether.malware_counters.total_executed` | `long` | None |
|`aether.malware_counters.total_external_communications` | `long` | None |
|`aether.program_blocked_counters.total_programs_blocked` | `long` | None |
|`aether.pups_counters.total_affected_devices` | `long` | None |
|`aether.pups_counters.total_alerts` | `long` | None |
|`aether.pups_counters.total_data_access` | `long` | None |
|`aether.pups_counters.total_executed` | `long` | None |
|`aether.pups_counters.total_external_communications` | `long` | None |
|`aether.threats_by_av_counters.total_dangerous_actions_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_devices_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_intrusion_attempted_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_malware_urls_blocked_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_phishing_detected_by_av` | `long` | None |
|`aether.threats_by_av_counters.total_tracking_cookies_detected_by_av` | `long` | None |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |

