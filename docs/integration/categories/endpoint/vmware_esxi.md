uuid: 2b13307b-7439-4973-900a-2b58303cac90
name: VMWare ESXi
type: intake

## Overview
- **Vendor**:
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

VMware ESXi is a hypervisor and an operation system. It serves virtual computers while running directly on the server hardware



## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Browse to the host thank to the vSphere Client inventory and follow [this guide](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.upgrade.doc/GUID-9F67DB52-F469-451F-B6C8-DAE8D95976E7.html) to enable the log forwarding to the log concentrator.

For syslog forwarding, the only parameter required is [loghost](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.upgrade.doc/GUID-8981F5FA-BB2A-47FB-A59A-7FC5C523CFDE.html) that set the location of the syslog server.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `VMWare ESXi`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/2b13307b-7439-4973-900a-2b58303cac90_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_2b13307b-7439-4973-900a-2b58303cac90_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/2b13307b-7439-4973-900a-2b58303cac90.md!}

