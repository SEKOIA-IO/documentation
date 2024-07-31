uuid: e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e
name: Proofpoint On Demand
type: intake

## Overview

ProofPoint On Demand (PoD) offers a real-time email processing feed to detect, classify and mitigate threats.

- **Vendor**: Proofpoint
- **Plan**: Defend Prime
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway


## Configure

### Proofpoint On Demand

As a prerequisite, you need to create an APIKey and to get your cluster id:

Copy your cluster id. It is diplayed on the upper-right corner of your management interface, next to the release number.

To create an APIKey, from our dashboard:

- Open the menu, unfold the `Settings` section and go to `API Key Management`.
- Click on the button `Create New` to display the `Create New API Key` dialog box.
- Type a name and generate the API Key.
- Select `View Details` from the ellipsis menu on the fresh API Key and copy the key.


### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Proofpoint PoD`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [ProofPoint PoD connector](../../../automate/library/proofpoint.md#get-proofpoint-pod-events).

Set up the trigger configuration with the api key, the cluster id and the intake key. Customize others parameters if needed.

Start the playbook and enjoy your events.

{!_shared_content/operations_center/integrations/generated/e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e.md!}


## Further Readings
- [ProofPoint APIKey Management](https://help.proofpoint.com/Admin_Portal/Settings/API_Key_Management)
