uuid: 40bac399-2d8e-40e3-af3b-f73a622c9687
name: McAfee Web Gateway / Skyhigh Secure Web Gateway
type: intake

## Overview

Skyhigh Secure Web Gateway (SWG) (previously McAfee Web Gateway (MWG)) is a web gateway offering malware detection, threat prevention and reputation filtering.
This product is supported by Skyhigh Security.


{!_shared_content/operations_center/detection/generated/suggested_rules_40bac399-2d8e-40e3-af3b-f73a622c9687_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/40bac399-2d8e-40e3-af3b-f73a622c9687.md!}

## Configure

In this guide, you will configure a rule set to forward events to syslog and add a new forwarding in the rsyslog server provided with MWG.

### Configure a Rule Set

Prior to the configuration, download the “Rule Set” configuration [`SEKOIAIO_SKYHIGH_swg.xml`](/assets/operation_center/integration_catalog/network/skyhigh_secure_web_gateway/SEKOIAIO_SKYHIGH_swg.xml).


In your SWG console:

- Select `Policy` section then the `Rule sets` tab. From the menu, select `Log Handler`.
- Right-click on the `Default` Log Handler in the tree then select `Add > Rule Set from Library...`.
- Once the `Add from Rule Set library` window opened, under the `Rule Set Library` tree, click on the `Import from file...` button and import `SEKOIAIO_mwg.xml` file.
- Select the `Rule Set` `Sekoia.io` and ensure the rule `forward logs` is enabled.


### Configure Rsyslog

To forward your logs to our servers, in our MWG console:

- Select `Configuration` section then the `File Editor` tab.
- In the tree, select `rsyslog.conf`.
- Consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to configure Rsyslog in order to forward these logs to Sekoia.io.
