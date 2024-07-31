uuid: de9ca004-991e-4f5c-89c5-e075f3fb3216
name: Netskope Events
type: intake


## Overview

[Netskope](https://www.netskope.com/) is a cybersecurity company that provides solutions to protect data in cloud apps and network security while applying zero trust principles.

- **Vendor**: Netskope
- **Plan**: Defend Core & Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: authentications and activities in your Cloud applications

## Step-by-Step Configuration Procedure

This setup guide will lead you into forwarding netskope's events to Sekoia.io.

!!! Important
    This integration will collect events from the APIv2 of the Netskope platform.

### Instructions on the 3rd Party Solution
#### Generate API token

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

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_de9ca004-991e-4f5c-89c5-e075f3fb3216_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/de9ca004-991e-4f5c-89c5-e075f3fb3216.md!}

## Further Readings

- [Netskope documentation - create an API token](https://docs.netskope.com/en/rest-api-v2-overview-312207.html)
