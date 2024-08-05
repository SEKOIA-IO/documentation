uuid: 5d9e261a-944c-4a76-8c61-6794fd44d9a8
name: Unbound
type: intake

## Overview
- **Vendor**:
- **Plan**: Defend Core & Defend Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
Unbound is a validating, recursive, and caching DNS resolver product from NLnet Labs. It is distributed free of charge in open-source form under the BSD license.



## Configure
This setup guide will show you how to forward logs produced by your Unbound server to Sekoia.io by means of an rsyslog transport channel.

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](/integration/ingestion_methods/syslog/overview) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/5d9e261a-944c-4a76-8c61-6794fd44d9a8_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_5d9e261a-944c-4a76-8c61-6794fd44d9a8_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/5d9e261a-944c-4a76-8c61-6794fd44d9a8.md!}

