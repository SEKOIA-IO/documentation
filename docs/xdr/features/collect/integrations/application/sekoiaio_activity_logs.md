uuid: 41e3ca4e-a714-41aa-ad69-684a0b3835fc
name: SEKOIA.IO activity logs
type: intake

## Overview
SEKOIA.IO activity logs collect operations done, on SEKOIA.IO, by the members of the community. It helps to monitor activities and detect malicious behavior. The activity logs collect various operations such as
- listing observables
- creating a new rule
- updating the status of an alert
- inviting a new member in the community

{!xdr/features/collect/integrations/generated/sekoiaio-activity-logs_do_not_edit_manually.md!}

## Configure

To monitor activities, create a new intake `SEKOIA.IO activity logs` in your community. Once the intake is enabled, activities will automatically appear in your events (disclaimer: a delay of two minutes may be necessary before seeing the activities appear).
