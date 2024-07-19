uuid: 20876735-c423-4bbc-9d19-67edc91fb063
name: RSA SecurID
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

SecurID is a token system, or authenticator, produced by RSA Security and intended to offer strong authentication to its user in the context of access to an information system.



## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

In the Security Console of the RSA Authentication Manager:

1. On the upper bar, go to `Setup` and select `System Settings`.
2. Under `Basic Settings`, click on `Logging`.
3. Select `Primary` as the selected instance and click `Next`
4. In the section `Log levels`, choose the level for each type.
5. In the section `Log Data Retention`, for each log data, select `Save to internal database and remote Syslog at the following hostname or IP address`, then type the location of the log concentration.
6. Click `Save`


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `RSA SecurID`.

## Forward logs to Sekoia.io

Please consult the [Sekoia Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder) documentation to forward these logs to Sekoia.io.



{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/detection/generated/suggested_rules_20876735-c423-4bbc-9d19-67edc91fb063_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/20876735-c423-4bbc-9d19-67edc91fb063.md!}

## Further Readings

- [How to configure RSA Authentication Manager to send log messages to a local file for an audit trail](https://community.rsa.com/t5/securid-knowledge-base/how-to-configure-rsa-authentication-manager-to-send-log-messages/ta-p/6449)
- [How to configure RSA Authentication Manager 8.1, 8.2, 8.3 to send data to multiple remote syslog servers](https://community.rsa.com/t5/securid-knowledge-base/how-to-configure-rsa-authentication-manager-8-1-8-2-8-3-to-send/ta-p/2525)
