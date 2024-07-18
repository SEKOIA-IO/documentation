```markdown
uuid: 23813540-b658-48dd-b030-e9b92168bbf4
name: Daspren Parad
type: intake

## Overview

- **Vendor**: Daspren
- **Plan**: Defend Prime
- **Supported environment**: On Premise / SaaS
- **Version compatibility, if applicable**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
  - Data loss prevention
  - Kernel drivers
  - File monitoring
- **Coverage Score**: 1

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![consume_azure_logs](/assets/integration/daspren.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
  - Self-managed syslog forwarder
- **Network**:
  - Outbound traffic allowed
- **Permissions**:
  - Administrator or Root access to the Parad CLI

### Transport Protocol/Method

- **Direct Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: informational

!!! Note
    This is a description of the log level based on the taxonomy of the [RFC5425](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

- **Default Log Location**:

### Sample of supported raw events

**TODO**: Add a directory with raw event in every integration.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Detailed Procedure:

1. **Open the Parad CLI**:
2. **Create a Sink from the CLI**:
   - Go to `Sinks > Add Sink`.
   - Select the Sekoia Sink Variant.
   - Type a name and paste the intake key.
3. **Create a Reporter from the CLI**:
   - Go to `Reporters > Add Reporter`.
4. **Create a Link**:
   - Link the previously created Sink and Reporter.

#### Event Categories:
- List explicit event types supported by the format (e.g., Fortigate: forward-traffic, local-traffic, multicast-traffic, vpn, web, url-filter).

#### Event Selection:
- Guidance on selecting event types when sending logs.
- Visual Aids: Include screenshots or videos if possible.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014_sample.md!}

## Detection section


The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/d6d15297-e977-4584-9bb3-f0290b99f014.md!}


## Further readings

- [Daspren Documentation](https://www.daspren.com/documentation)
- [Sekoia.io Documentation](https://docs.sekoia.io)
```