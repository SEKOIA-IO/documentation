uuid: 033cd098-b21b-4c9b-85c4-c8174c307e48
name: WithSecure Elements
type: intake

## Overview

WithSecure Elements is an advanced cloud-based EDR/EPP platform that provides a unified solution to protect your organization from cyber threats. By integrating WithSecure Elements with Sekoia.io, you can easily monitor and correlate alerts across all endpoints, ensuring maximum security for your business.

This setup guide shows how to forward events produced by WithSecures Elements to Sekoia.io.

- **Vendor**: WithSecure
- **Plan**: Defend Prime
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Process monitoring

## Configure

### Create WithSecure Elements Credentials

In the WithSecure Elements Central Admin console:

1. On the left panel, go to `Management` and select `API clients`.
2. Click on `Add new` to create a new API client dedicated to Sekoia.io.
3. Give it a description, check it is `Read-Only` and click on `Add`.
4. In the `API client` Summary, copy the `Client ID` and the `Secret` before checking the box `I have copied and stored the secret` and closing the windows. They will be used later in Sekoia.io to retrieve the events.

![WithSecure API Client Creation](/assets/integration/endpoint/withsecure/withsecure_create_api_client.png){: style="max-width:80%"}

### Create the intake

1. Go to the [Intake page](https://app.sekoia.io/operations/intakes) and create a new `WithSecure Elements` intake.
2. Copy the associated Intake key

### Create the playbook that fetches the events

1. Go to the [Playbook page](https://app.sekoia.io/operations/playbooks).
2. Click on `+ PLAYBOOK` and choose `Create a playbook from scratch`.
3. Give it a name such as `Collect WithSecure Elements events` and a description and click on `Next`.
4. In `Choose a trigger`, select the [Fetch security events](/integration/action_library/endpoint/withsecure).
5. Click on the `Fetch security events` trigger and, on the right sidebar, create a new `Module Configuration`. Give it a name  such as `My Organisation WithSecure` and enter your API Client credentials `Client ID`/`Secret`
6. In the Trigger Configuration section, Click on `Create new configuration`.
8. Write a `name`, paste the `intake_key` associated to your `WithSecure Elements` intake and click on `Save`.
9. On the top right corner, start the Playbook. You should see monitoring messages in the `Logs` section of your action.
10. After a couple of minutes check on the Events page that WithSecure Elements logs are being received.

![WithSecure Playbook Example](/assets/integration/endpoint/withsecure/withsecure_playbook_collect.png){: style="max-width:80%"}

{!_shared_content/operations_center/integrations/generated/033cd098-b21b-4c9b-85c4-c8174c307e48_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_033cd098-b21b-4c9b-85c4-c8174c307e48_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/033cd098-b21b-4c9b-85c4-c8174c307e48.md!}