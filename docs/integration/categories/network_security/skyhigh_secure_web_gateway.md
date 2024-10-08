uuid: 40bac399-2d8e-40e3-af3b-f73a622c9687
name: McAfee Web Gateway / Skyhigh Secure Web Gateway
type: intake

## Overview
Skyhigh Secure Web Gateway (SWG) (previously McAfee Web Gateway (MWG)) is a web gateway offering malware detection, threat prevention and reputation filtering.

- **Vendor**: Skyhigh Security
- **Supported environment**: On prem
- **Version compatibility**: 12.2.10
- **Detection based on**: Telemetry
- **Supported application or feature**: Anti-virus, Web proxy,	Web logs


## Configure

In this guide, you will configure a rule set to forward events to syslog and add a new forwarding in the rsyslog server provided with MWG.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Configure a Rule Set

Prior to the configuration, download the “Rule Set” configuration [`SEKOIAIO_SKYHIGH_swg.xml`](/assets/integration/network/skyhigh_secure_web_gateway/SEKOIAIO_SKYHIGH_swg.xml).


In your SWG console:

- Select `Policy` section then the `Rule sets` tab. From the menu, select `Log Handler`.
- Right-click on the `Default` Log Handler in the tree then select `Add > Rule Set from Library...`.
- Once the `Add from Rule Set library` window opened, under the `Rule Set Library` tree, click on the `Import from file...` button and import `SEKOIAIO_mwg.xml` file.
- Select the `Rule Set` `Sekoia.io` and ensure the rule `forward logs` is enabled.


### Configure Rsyslog

To forward your logs to your log concentrator, in our MWG console:

- Select `Configuration` section then the `File Editor` tab.
- In the tree, select `rsyslog.conf`.
- Add the following line:
  ```
  if $programname == 'mwg' and $syslogfacility-text == 'daemon' and $syslogseverity-text == 'info' then  @@<log concentrator ip>:<port>
  ```
  Replace the `<log concentrator ip>` placeholder with the ip address of our log concentrator and `<port>` by the listening port on the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder) for the Skyhigh raw events.

!!!Note
  The double at characters without spaces (@@) indicates that syslog messages are transferred to a host using the TCP protocol. To use the UDP protocol, use single at character (@).


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/40bac399-2d8e-40e3-af3b-f73a622c9687_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_40bac399-2d8e-40e3-af3b-f73a622c9687_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/40bac399-2d8e-40e3-af3b-f73a622c9687.md!}

