uuid: 5cac7207-1711-4654-9932-929fe619f6ea
name: Cisco Catalyst SD-WAN
type: intake

## Overview

Cisco Catalyst SD-WAN is a cloud-managed solution that delivers secure, high-performance SD-WAN connectivity across campuses, branches and multi-cloud environments.

- **Vendor**: Cisco
- **Supported environment**: On Premise
- **Version compatibility**: 17.4.1 and upper
- **Detection based on**: Telemetry
- **Supported application or feature**: Network traffic monitoring

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Specification

### Prerequisites

- **Resource**:
    - Sekoia.io netflow forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Administrator or Root access to the Cisco Catalyst SD-WAN device
    - Root access to the Linux server with the netflow forwarder

### Transport Protocol/Method

- **Indirect Netflow**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: IPFIX
- **Supported verbosity level**: Informational

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward Cisco Catalyst SD-WAN netflows

This setup guide will show you how to provide an integration between Cisco Catalyst SD-WAN traffic monitoring and Sekoia.io.

**Create the Centralized policy:**

- Log on your Catalyst SD‑WAN Manager
- Go to `Configuration` > `Policies`
- Select `Centralized Policy`
- Click `Add Policy`
- At the `Create Group of Interest` step, click items on the left panel to create your group of interest.
- For example:
    - To add a list of VPNs:
        - On the left panel, go to `VPN`
        - Click `New VPN List`
        - Type a `VPN List Name`
        - Type the VPNs to add in `Add VPN`
    - To add a list of sites:
        - On the left panel, go to `Site`
        - Click `New Site List`
        - Type a `Site List Name`
        - Type the sites to add in `Add Site`
- When done, click `Next`
- At the `Configure Topology and VPN Membership` step, add topology and VPN Membership as you wish
- Click `Next`
- At the `Configure Traffic Rules`, go to `Cflowd`
- Click `Add Policy` > `Create New`
- Type a name and a description for the Policy
- In the `Cflowd Template` section, set the properties at your convenience
- Go to the `Collector List` section
- Click `New Collector`
- Type the VPN ID
- Type the address of the netflow collector as `IP address`
- Type the listen port of the netflow collector as `Port`
- Select `UDP` as `Transport Protocol`
- Type enter the name of the interface to use to send flows to the collector as `Source interface`
- Click `Add`
- Click `Next`
- At `Apply Policies to Sites and VPNs`, type a `Policy Name` and a `Policy Description`
- Click the `CFlowd` tab
- Select sites to add in the `Site List`
- Click `Save Policy`
- In the `Centralized Policy` view, click `...` at the right of your policy
- Click `Activate` menu
- In the confirmation box, Click `Activate`

See [documentation](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/policies/ios-xe-17/policies-book-xe/traffic-flow-monitor.html#id_114091)


**Create the Localized policy:**

- Log on your Catalyst SD‑WAN Manager
- Go to `Configuration` > `Policies`
- Select `Localized Policy`
- Click `Add Policy`
- Click `Next` until reaching the `Policy Overview`
- Type a `Policy Name`
- Type a `Policy Description`
- Check `Netflow` for IPv4 traffic
- Check `Netflow IPv6` for IPv6 traffic
- Click `Save Policy`


See [documentation](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/policies/ios-xe-17/policies-book-xe/traffic-flow-monitor.html#id_114090)

**Apply the localized policy:**

- Go to `Configuration` > `Templates`
- Click `Device Templates`
- Select a template and click `...` at the right of the template
- Click `Edit` menu
- Go to `Additional Templates`
- Select the localized policy as `Policy`
- Click `Save`


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/netflow_forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/5cac7207-1711-4654-9932-929fe619f6ea_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_5cac7207-1711-4654-9932-929fe619f6ea_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/5cac7207-1711-4654-9932-929fe619f6ea.md!}

## Further readings

- [Cisco - Traffic Flow Monitoring](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/policies/ios-xe-17/policies-book-xe/traffic-flow-monitor.html)
- [Youtube - Configure SNMP and Netflow on Cisco SD-WAN](https://www.youtube.com/watch?v=a1Tw1xANgsU)
