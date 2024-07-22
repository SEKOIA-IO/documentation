uuid: 890207d2-4878-440d-9079-3dd25d472e0a
name: ManageEngine ADAudit Plus
type: intake


## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

ManageEngine ADAudit Plus is a robust Active Directory auditing and compliance solution, empowering organizations to track and monitor changes, detect security threats, and ensure regulatory compliance within their Active Directory environment.

## Supported events

This integration supports the following events from ADAudit Plus:

- Alerts (`ADAPAlerts`)
- Group managements reports (`GroupMgmtReports`)
- User managements reports (`UserMgmtReports`)
- Logon reports (`LogonReports`)
- Audit reports (`DNSAuditReports` and `ADObjectsAuditReports`)


## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

In the ADAudit Plus console:

1. Click on 'Admin' Tab → 'SIEM Integration'.
2. Check the 'Enable forwarding of ADAudit Plus Data' checkbox
3. Choose the 'ArcSight (CEF)' radio button.
4. Enter the log concentrator server name.
5. Enter the log concentrator port number and protocol.
6. Save the configuration
7. After saving this configuration, Choose the categories to forward.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `ManageEngine ADAuditPlus`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.




## Futher Readings

- [SIEM Integration](https://www.manageengine.com/products/active-directory-audit/help/admin-settings/siem-integration.html)
- [Collected logs in CEF format](https://pitstop.manageengine.com/portal/en/community/topic/collected-syslog-files-in-cef-format)

{!_shared_content/operations_center/integrations/generated/890207d2-4878-440d-9079-3dd25d472e0a_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_890207d2-4878-440d-9079-3dd25d472e0a_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/890207d2-4878-440d-9079-3dd25d472e0a.md!}

