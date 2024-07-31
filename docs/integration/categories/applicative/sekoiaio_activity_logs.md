uuid: 41e3ca4e-a714-41aa-ad69-684a0b3835fc
name: Sekoia.io activity logs
type: intake

## Overview
- **Vendor**: Sekoia
- **Plan**: Defend Core & Defend Prime
- **Detection based on**: Audit
- **Supported application or feature**:
Sekoia.io activity logs collect operations done, on Sekoia.io, by the members of the community. It helps to monitor activities and detect malicious behavior. The activity logs collect various operations such as:

    - listing observables
    - creating a new rule
    - updating the status of an alert
    - inviting a new member in the community

## Configure

To monitor activities, create a new intake `Sekoia.io activity logs` in your community. Once the intake is enabled, activities will automatically appear in your events (disclaimer: a delay of two minutes may be necessary before seeing the activities appear).

{!_shared_content/operations_center/integrations/generated/41e3ca4e-a714-41aa-ad69-684a0b3835fc_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_41e3ca4e-a714-41aa-ad69-684a0b3835fc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/41e3ca4e-a714-41aa-ad69-684a0b3835fc.md!}
