uuid: 40bac399-2d8e-40e3-af3b-f73a622c9687
name: McAfee Web Gateway
type: intake

## Overview
McAfee Web Gateway (MWG) is a web gateway offering malware detection, threat prevention and reputation filtering.
This product is supported by McAfee Corp.

{!xdr/features/collect/integrations/generated/mcafee-web-gateway_do_not_edit_manually.md!}

## Configure

In this guide, you will configure a rule set to forward events to syslog and add a new forwarding in the rsyslog server provided with MWG.

### Configure a Rule Set

Prior the configuration, download the “Rule Set” configuration [`SEKOIAIO_mwg.xml`](/assets/operation_center/integration_catalog/network/mcafee_web_gateway/SEKOIAIO_mwg.xml).


In your MWG console:

- Select `Policy` section then the `Rule sets` tab. From the menu, select `Log Handler`.
- Right-click on the `Default` Log Handler in the tree then select `Add > Rule Set from Library...`.
- Once the `Add from Rule Set library` window opened, under the `Rule Set Library` tree, click on the `Import from file...` button and import `SEKOIAIO_mwg.xml` file.
- Select the `Rule Set` `SEKOIA.IO` and ensure the rule `forward logs` is enabled.


### Configure Rsyslog

To forward your logs to our servers, in our MWG console:

- Select `Configuration` section then the `File Editor` tab.
- In the tree, select `rsyslog.conf`.
- Consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to configure Rsyslog in order to forward these logs to SEKOIA.IO.
