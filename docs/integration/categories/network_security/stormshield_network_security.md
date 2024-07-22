uuid: 79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4
name: Stormshield Network Security
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

Stormshield Network Security firewalls provides comprehensive security and high performance network protection. In addition, they offer a high degree of scalability to support the evolution of IT and OT networks

In this documentation we will explain how to collect and send Stormshield Network Security logs to Sekoia.io.




## Configure

### Sending logs to syslog server

You need to set some parameters to send your logs via Syslog.
It is necessary to create a profile using the specific tab named "Syslog" within your Stormshield interface.

_Note that you can configure up to 4 different profiles._

You need to specify the following information:

- Name
- Comments
- Syslog server
- Protocol
- Certification authority
- Server certificate
- Client certificate
- Format

You can find more information using [this documentation](https://stormshield.pl/storage/www_stormshield/doc/dokumentacja/sns-en-user_configuration_manual-v3.pdf) provided by Stormshield.

### Generate the intake_key

You have to go on your Sekoia.io instance to generate an "intake key".
Everything you need to do for this part of the configuration is described [here](../../../collect/intakes.md).

Finally, to push logs, you have to [configure](../../../collect/ingestion_methods/index.md) some filters and rewrite rules in Syslog that will add the proper “intake key” considering your logs.

{!_shared_content/operations_center/integrations/generated/79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4.md!}

