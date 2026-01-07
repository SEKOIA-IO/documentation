---
uuid: cf5c916e-fa26-11ed-a844-f7f4d7348199
title: OGO Shield WAF
name: OGO Shield WAF
type: intake
---

## Overview

OGO Shield Web Application Firewall provides protection and performance for your web applications and APIs.

- **Vendor**: OGO
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Site and Cluster traffic

## Prerequisite

- Being an Administrator of the organization or Owner of the organization in OGO.

## Step-by-Step Configuration Procedure

This setup guide describes how to forward security events from OGO to Sekoia.io.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

### Instructions on the 3rd Party Solution

#### Set up the export type

In the OGO interface, go to `My Account > My Organization > Log Export`. Select `Sekoia` as the export type and **paste the Intake key** in the form.

#### Activate export for sites

In the general configuration tab of desired sites, in the `Organization Owner/Administrator` section, activate the `Log export`.

#### Activate export for clusters

For `OGO Shield Satellite` owners, go to `Admin Cluster > Maintenance` and activate the `Log export`.


{!_shared_content/operations_center/integrations/generated/cf5c916e-fa26-11ed-a844-f7f4d7348199_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_cf5c916e-fa26-11ed-a844-f7f4d7348199_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/cf5c916e-fa26-11ed-a844-f7f4d7348199.md!}

## Further Readings

- [OGO Log Export](https://help.ogosecurity.com/help/log-export)
