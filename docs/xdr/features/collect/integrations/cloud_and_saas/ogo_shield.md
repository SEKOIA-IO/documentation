uuid: cf5c916e-fa26-11ed-a844-f7f4d7348199
name: OGO Shield WAF
type: intake

## Overview

OGO Shield Web Application Firewall provides protection and performance for your web applications and APIs.

This setup guide describes how to forward security events from OGO to Sekoia.io.

!!! warning
    This format is still in beta, please use it wisely.


{!_shared_content/operations_center/detection/generated/suggested_rules_cf5c916e-fa26-11ed-a844-f7f4d7348199_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cf5c916e-fa26-11ed-a844-f7f4d7348199.md!}

## Configure

### Create the intake in Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `OGO WAF`. Copy the intake key.

### Configure log export

#### Set up the export type

In the OGO interface, go to `My Profile > Log Export`. Select `Sekoia` as the export type and paste the intake key in the form.

#### Activate export for sites

In the general configuration tab of desired sites, in the `Owner` section, activate the `Log export`.

#### Activate export for clusters

For `OGO Shield Satellite` owners, go to `Admin Cluster > Maintenance` and activate the `Log export`.


## Further Readings

- [OGO Log Export](https://help.ogosecurity.com/help/log-export)
