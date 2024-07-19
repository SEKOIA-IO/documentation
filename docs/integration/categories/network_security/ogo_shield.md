uuid: cf5c916e-fa26-11ed-a844-f7f4d7348199
name: OGO Shield WAF
type: intake

## Overview
  - **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

OGO Shield Web Application Firewall provides protection and performance for your web applications and APIs.

This setup guide describes how to forward security events from OGO to Sekoia.io.



## Configure

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `OGO WAF`. Copy the intake key.

### Configure log export

#### Prerequisite

- Being an Administrator of the organization or Owner of the organization.

#### Set up the export type

In the OGO interface, go to `My Account > My Organization > Log Export`. Select `Sekoia` as the export type and paste the intake key in the form.

#### Activate export for sites

In the general configuration tab of desired sites, in the `Organization Owner/Administrator` section, activate the `Log export`.

#### Activate export for clusters

For `OGO Shield Satellite` owners, go to `Admin Cluster > Maintenance` and activate the `Log export`.



## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_cf5c916e-fa26-11ed-a844-f7f4d7348199_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/cf5c916e-fa26-11ed-a844-f7f4d7348199.md!}

## Further Readings

- [OGO Log Export](https://help.ogosecurity.com/help/log-export)
