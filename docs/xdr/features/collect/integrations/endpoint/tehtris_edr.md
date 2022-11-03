uuid: 8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd
name: Tehtris Endpoint Detection & Reponse
type: intake

## Overview

Tehtris EDR is a security product to monitor, detect and mitigate threats on endpoints. It reduces the attack surface and prevent attacks.

This setup guide shows how to forward events produced by Tehtris EDR to SEKOIA.IO.

{!_shared_content/operations_center/detection/generated/suggested_rules_8d8f040d-6a75-4bf4-bf1d-772e9a30f0dd_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/tehtris-edr_do_not_edit_manually.md!}

## Configure

### Prerequisites

Contact your Tehtris referent to activate the XDR Platform APIs for your tenant and to ask to add the [SEKOIA.IO IP address](../../../../FAQ.md#ip-behind-triggers-available-in-playbooks-section) to the allowlist.

Log on the Tehtris XDR platform and navigate to `SOAR > Key Management`.
Click on the button `Add`, enter the label of the API Key and select, at least, the api `Fetch Events`. You may have to create a filter. At the end, click on `Create` to generate the API Key

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Tehtris Endpoint Detection & Reponse`.

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new events from Tehtris](../../../automate/library/tehtris.md#fetch-new-events-from-tehtris) module. 

Set up the module configuration with your API key and your tenant ID (most of time, your tenant ID is the subdomain of your tehtris instance; eg: https://{tenant_id}.tehtris.net)

Start the playbook and enjoy your [events](https://app.sekoia.io/operations/events).
