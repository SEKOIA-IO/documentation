uuid: 915a119c-2ec8-4482-a3c6-4d4cae62b671
name: Sekoia.io forwarder logs
type: intake

## Overview
- **Vendor**: Sekoia
- **Plan**: Defend Core & Defend Prime
- **Detection based on**: Audit
- **Supported application or feature**:
Sekoia.io forwarder logs collect all statictics coming from Sekoia forwarder instances. It helps to monitor the forwarder health:

    - resource usage
    - queue size
    - number of messages received by the forwarder
    - number of messages sent by the forwarder

## Configure

To monitor forwarder health, create a new intake `Sekoia.io forwarer logs` in your community. Once the intake is enabled, please follow [this documentation](/integration/ingestion_methods/syslog/sekoiaio_forwarder/#monitor-your-concentrator) in order to activate metrics on the forwarder side. You can find also details about the generated metrics

{!_shared_content/operations_center/integrations/generated/915a119c-2ec8-4482-a3c6-4d4cae62b671fc_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_915a119c-2ec8-4482-a3c6-4d4cae62b671fc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/915a119c-2ec8-4482-a3c6-4d4cae62b671fc.md!}
