uuid: 469bd3ae-61c9-4c39-9703-7452882e70da
name: Cato SASE
type: intake

## Overview

Cato Networks is a software company providing solutions to protect cloud applications. Cato SASE Cloud provides zero trust network access to on-premises and cloud applications.

- **Vendor**: Cato Networks
- **Supported environment**: Cloud
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: Application, Web, Authentication



## Configure

This setup guide will show you how to provide an integration between Cato SASE events and Sekoia.io.

### Enable the EventsFeed API

1. Log in to your Cato Management Application
2. Click on the `Administration` section then click on `API & Integrations`
    ![Administration](/assets/integration/cloud_and_saas/cato/administration.png){: style="max-width:100%"} 
3. Select the tab `Events Integration`
4. Click on `Enable integration with Cato events`
    ![Administration](/assets/integration/cloud_and_saas/cato/enable_eventsfeed.png){: style="max-width:100%"}

### Generate the API key

To collect the events from the Cato Networks platform, an API key is required:

1. Click on the `Administration` section then click on `API & Integrations`
2. Click on the button `New` to generate a new API key
3. On the panel, give a name to the api key, select the `View` permission
    ![Administration](/assets/integration/cloud_and_saas/cato/panel.png){: style="max-width:100%"}
4. Click on apply and copy the API key

In addition to the API key, Cato `account ID` is also required for the Account configuration in Sekoia

!!! Note
     In the Cato Management Application, please note the four or five digits in the browser address.

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cato SASE. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Cato SASE](/integration/action_library/network/cato-networks) trigger
2. Set up the module configuration with the Api Key and Account Id. Set up the trigger configuration with the intake key
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/469bd3ae-61c9-4c39-9703-7452882e70da_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_469bd3ae-61c9-4c39-9703-7452882e70da_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/469bd3ae-61c9-4c39-9703-7452882e70da.md!}

## Further readings
- [Cato Networks - Generating API Keys for the Cato API](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API)
