uuid: 064f7e8b-ce5f-474d-802e-e88fe2193365
name: Trend Micro Apex One
type: intake

## Overview
- **Vendor**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

Trend Micro Apex One is Endpoint Detection and Response (EDR) solution that detects and protects your endpoints against threats.

This integration supports the following log types:

- Application Control violations
- Attack Discovery detections
- Behavior Monitoring detections
- C&C Callback
- Content Violation
- Data Loss Prevention
- Device Control violations
- Suspicious File detections
- Network Content Inspection
- Virus/Malware detections
- Spyware/Grayware detections
- Predictive Machine Learning detections
- Virtual Analyzer detections
- Web Violation
- Engine Update Status
- Pattern Update Status


!!! warning
    This format is in beta



## Configure

In this guide, you will configure your Apex Central to forward detection through syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

To enable syslog forwarding:

1. Log to Apex Central
2. Go to `Administration > Settings > Syslog Settings`
3. Select the checkbox `Enable syslog forwarding`
4. Provide the IP, listening port and the protocol of our syslog concentrator
5. Select `CEF` as the log format
6. Configure the frequency of the log forwarding
7. Select the log types to forward according to the list of supported log types:
	- Application Control violations
	- Attack Discovery detections
	- Behavior Monitoring detections
	- C&C Callback
	- Content Violation
	- Data Loss Prevention
	- Device Control violations
	- Suspicious File detections
	- Network Content Inspection
	- Virus/Malware detections
	- Spyware/Grayware detections
	- Predictive Machine Learning detections
	- Virtual Analyzer detections
	- Web Violation
	- Engine Update Status
	- Pattern Update Status
8. Click `Test Connection` to validate the configuration
9. Click `Save`

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Trend Micro Apex One`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.


{!_shared_content/operations_center/integrations/generated/064f7e8b-ce5f-474d-802e-e88fe2193365_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_064f7e8b-ce5f-474d-802e-e88fe2193365_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/064f7e8b-ce5f-474d-802e-e88fe2193365.md!}

## Further Readings

- [Trend Micro Apex One - Configure syslog forwarding](https://docs.trendmicro.com/en-us/enterprise/trend-micro-apex-central-2019-online-help/detections/logs_001/syslog-forwarding.aspx)
- [Trend Micro Apex One - Supported Log Types and Formats](https://docs.trendmicro.com/en-us/enterprise/trend-micro-apex-central-2019-online-help/detections/logs_001/syslog-forwarding/syslog-log-types-for.aspx)
