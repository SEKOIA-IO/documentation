uuid: 0642b03a-9d4a-4c88-a5e2-4597e366b8c4
name: VMWare VCenter
type: intake

## Overview

VMWare VCenter is a centralized management software. It provides a single point of control for managing virtual machines and ESXi hosts from a centralized interface.

{!_shared_content/operations_center/detection/generated/suggested_rules_0642b03a-9d4a-4c88-a5e2-4597e366b8c4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/0642b03a-9d4a-4c88-a5e2-4597e366b8c4.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

Follow [this guide](https://kb.vmware.com/s/article/2003322) to enable the log forwarding to the log concentrator.

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `VMWare VCenter`.

## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

Create a new configuration file:

```
sudo vim ./extended_conf/11-vcenter.conf
```

with the following template:

```
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/Sekoia-io-intake.pem

input(type="imtcp" port="PORT" ruleset="remoteVmwarevCenter")

template(name="SEKOIAIOTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")
ruleset(name="remoteVmwarevCenter"){
  if($programname == "vpxd") {
    action(
	type="omfwd"
	protocol="tcp"
        target="intake.sekoia.io"
        port="10514"
        TCP_Framing="octet-counted"
        StreamDriver="gtls"
        StreamDriverMode="1"
        StreamDriverAuthMode="x509/name"
        StreamDriverPermittedPeers="intake.sekoia.io"
        Template="SEKOIAIOTemplate"
    )
  }
}
```

Please change using the YOUR_INTAKE_KEY accordingly, as well as, the PORT.

Update the `docker-compose.yml` file of the Sekoia.io forwarder to mount the extended conf:

```
volumes:
    - ./intakes.yaml:/intakes.yaml
...
    - ./extended_conf:/extended_conf
```
