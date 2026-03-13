uuid: c3621017-d090-44c8-af7a-9408332a15d0
name: Zscaler Private Access
type: intake

## Overview
The Zscaler Private Access (ZPA) service enables organizations to provide access to internal applications and services while ensuring the security of their networks. ZPA is an easier to deploy, more cost-effective, and more secure alternative to VPNs. Unlike VPNs, which require users to connect to your network to access your enterprise applications, ZPA allows you to give users policy-based secure access only to the internal apps they need to get their work done. With ZPA, application access does not require network access.

- **Vendor**: Zscaler
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Traffic, Web, VPN

### Supported logs

This integration can ingest the following logs:

- `User Activity logs`
- `User Status Logs`
- `App Connector Status Logs`
- `Browser Access Logs`
- `AppProtection Logs`
- `Audit logs`



## Configure

This section will guide you on how to forward Zscaler ZPA events to Sekoia.io.



### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Zscaler ZPA`format.

### Forward events to the Sekoia Forwarder using the LSS service

#### Prerequisites

You must have a Sekoia Forwarder instance running in your infrastructure. This forwarder must be reachable from one of your App Connector

#### Configure the forwarding


1. Go to `Configuration & Control` > `Private Infrastructure` > `Log Receivers` ![menu](/assets/integration/cloud_and_saas/zscaler/zpa_log_receivers_menu.png){: style="max-width:50%"}
2. Click on `Add` to create a new log receiver ![Log Receiver](/assets/integration/cloud_and_saas/zscaler/zpa_add_new_log_receiver.png){: style="max-width:100%"}
3. Give your new log receiver a Name and a description, then specify the `Port` and `Public address` of the sekoia forwarder inside your infrastructure ![configuration](/assets/integration/cloud_and_saas/zscaler/zpa_log_receiver_configuration.png)
4. Choose the Log Type you want to forward and select the `json` Log Template. Keep the default Log format ![log stream](/assets/integration/cloud_and_saas/zscaler/zpa_log_format.png)
5. Save your log receiver, you will need to create a new receiver for each of the log type you want to forward, you have to make them point to the same forwarder/port


#### Forward logs to Sekoia.io

For more information on forwarding logs to Sekoia.io using the Sekoia Forwarder, see [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md)


{!_shared_content/operations_center/integrations/generated/c3621017-d090-44c8-af7a-9408332a15d0.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_c3621017-d090-44c8-af7a-9408332a15d0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c3621017-d090-44c8-af7a-9408332a15d0.md!}

## Further Readings

- [Zscaler - Log Streaming Service](https://help.zscaler.com/zpa/log-streaming-service)