uuid: 41e3ca4e-a714-41aa-ad69-684a0b3835fc
name: Sekoia.io activity logs
type: intake

## Overview
- **Vendor**:
- **Plan**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:
Sekoia.io activity logs collect operations done, on Sekoia.io, by the members of the community. It helps to monitor activities and detect malicious behavior. The activity logs collect various operations such as:

- listing observables
- creating a new rule
- updating the status of an alert
- inviting a new member in the community




## Configure

To monitor activities, create a new intake `Sekoia.io activity logs` in your community. Once the intake is enabled, activities will automatically appear in your events (disclaimer: a delay of two minutes may be necessary before seeing the activities appear).

{!_shared_content/operations_center/integrations/generated/41e3ca4e-a714-41aa-ad69-684a0b3835fc_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_41e3ca4e-a714-41aa-ad69-684a0b3835fc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/41e3ca4e-a714-41aa-ad69-684a0b3835fc.md!}

