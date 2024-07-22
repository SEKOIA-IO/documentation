uuid: de9ca004-991e-4f5c-89c5-e075f3fb3216
name: Netskope Events
type: intake


## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**:

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

This integration will collect events from your netskope's tenant to monitor authentications and activities in your Cloud applications.



## Configure

This setup guide will lead you into forwarding netskope's events to Sekoia.io.

!!! note
    This integration will collect events from the APIv2 of the Netskope platform.

### Generate API token

Please follow [this guide](https://docs.netskope.com/en/rest-api-v2-overview-312207.html) to create an API token.

To the API token, add the following scopes with the privilege `Read`:

- /api/v2/events/dataexport/events/page	
- /api/v2/events/dataexport/events/alert	
- /api/v2/events/dataexport/events/incident	
- /api/v2/events/dataexport/events/application	
- /api/v2/events/dataexport/events/infrastructure	
- /api/v2/events/dataexport/events/audit	
- /api/v2/events/dataexport/events/network	
- /api/v2/events/dataexport/events/connection	

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Netskope events`. Copy the intake key.

### Pull events

To start to pull events, you have to:

1. Go to the [playbooks page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [Fetch new events from Netskope](../../../../automate/library/netskope.md) trigger
2. Set up the module configuration with the base URL of your Netskope instance. Set up the trigger configuration with the API token and the intake key
3. Start the playbook and enjoy your events


{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_de9ca004-991e-4f5c-89c5-e075f3fb3216_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216.md!}

## Further Readings

- [Netskope documentation - create an API token](https://docs.netskope.com/en/rest-api-v2-overview-312207.html)
