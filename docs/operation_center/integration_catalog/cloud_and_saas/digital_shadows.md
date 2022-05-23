uuid: ccf942fe-c839-42be-a081-5c3f946e80f5
name: Digital Shadows SearchLight
type: intake

## Overview

Digital Shadows SearchLight continuously searches and identifies any unwanted exposures, and provides contextualised alerts to better understand the associated risks.

In this documenation we will explain how to collect and send SearchLight logs to SEKOIA.IO.

{!operation_center/integration_catalog/generated/digital-shadows-searchlight_do_not_edit_manually.md!}

## Configure

First of all, you will have to retrieve configuration information.
To do so, connect to the [Digital Shadows portal](https://portal-digitalshadows.com/) to get an API key under the heading "api" > "Stored Objects" > "Portal" > "Searchlight API doc".
Then, you will need to retrieve the following information from the portal:

- `API URL`
- `Basicauth key`
- `Basicauth secret`
- Your Searchlight account ID

You now have all information to configure the Digital Shadows Searchlight module and its `Send events` action to SEKOIA.IO.

To start your playbook with a template, go to: "Create a new playbook" > "Use a template" > Search for Searchlight.

You can also create your own on the same basis. A typical playbook to retrieve and send Searchlight logs to SEKOIA.IO will use this kind of chain:

- A "Pull alerts from Searchlight" trigger
- An action that sends events to SEKOIA.IO
