uuid: e4a758fc-7620-49e6-b8ed-b7fb3d7fa232
name: Vade M365
type: intake

## Overview

Vade for M365 offers AI-based protection against dynamic, email-borne cyberattacks targeting Microsoft 365.
It improves user experience and catches 10x more advanced threats than Microsoft.

In this documentation we will explain how to collect and send Vade for M365 logs to Sekoia.io.

- **Vendor**: Vade
- **Supported environment**: Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway, Anti-virus


## Configure

!!! info
     Consuming logs from Vade now requires the Vade Threat Intel & Investigation (TII) module. MSSP partners can benefit from this module from their Partner's Portal. Final customers are invited to contact their Vade commercial contact to setup this module.

First you need to reach the `Playbooks` page in order to initiate your playbook using the dedicated button.

You can directly choose the `Get M365 Email Events` trigger if you are creating a playbook from scratch otherwise you will have to find it
within the `Actions library` panel under the `Vade secure` menu to drag and drop the trigger on the graph.

To start configuring the selected trigger, you'll need to bring Vade's documentation which can be found [here](https://m365.eu.vadesecure.com/docs/).
This documentation will allow you to get the following information: your `client_id` and your `client_secret`. You can also get the `api_host` and `oauth2_authorization_url`, if necessary.
In most common cases, the `api_host` is `https://m365.eu.vadesecure.com` and the `oauth2_authorization_url` is `https://api.vadesecure.com/oauth2/v2/token`

Then you just have to configure the trigger itself by filling its `name`, by setting its `frequency` in seconds and by adding your Office 365 tenant identifier (`tenant_id`)

Lastly, you must add the Sekoia's action `Push Events to intake` to the graph and configure it using :

- the Sekoia.io `api_key` generated within the user center
- the `base_url` (`https://intake.sekoia.io`)
- the `events_path` to push on Intake (your logs, you will probably fill it with `{{ node.0['emails_path'] }}`)
- the `intake_key` of the intake you have previously created (documentation can be found [here](/xdr/features/collect/intakes))

{!_shared_content/operations_center/integrations/generated/e4a758fc-7620-49e6-b8ed-b7fb3d7fa232_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e4a758fc-7620-49e6-b8ed-b7fb3d7fa232_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/e4a758fc-7620-49e6-b8ed-b7fb3d7fa232.md!}