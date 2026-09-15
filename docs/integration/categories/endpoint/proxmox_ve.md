uuid: 8fad985c-bb61-4f96-8244-56ea8f625ac5
name: Proxmox VE
type: intake

## Overview

- **Vendor**: Proxmox
- **Supported environment**: On-Prem
- **Version compatibility**: 9.2
- **Detection based on**: Telemetry
- **Supported application or feature**:

Proxmox VE is an open-source virtualization platform combining KVM virtual machines, LXC containers, cluster orchestration, integrated networking, and firewall capabilities.

!!! warning "Beta"
	This integration is currently in beta. Features, field names and suggested rules may change.
	Validate parsing and detection rules before deploying to production.

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Proxmox VE`.

### Mount Sekoia forwarder

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

### Configure Proxmox node
Create a new configuration file:

Run these commands on your Proxmox VE 9.2 host via SSH/shell as root:

```shell
# 1. Install rsyslog (required for Debian 13 / PVE 9.2)
apt update && apt install rsyslog -y

# 2. Write targeted Sekoia forwarding configuration
cat << 'EOF' > /etc/rsyslog.d/50-sekoia.conf
# Tail web access and firewall files directly from disk
module(load="imfile")

input(type="imfile"
  File="/var/log/pveproxy/access.log"
  Tag="pveproxy-access"
  Severity="info"
  Facility="local0")

input(type="imfile"
  File="/var/log/pve-firewall.log"
  Tag="pve-firewall"
  Severity="info"
  Facility="local0")

# Filter and forward high-value security logs
if (
    $syslogfacility-text == 'auth' or
    $syslogfacility-text == 'authpriv' or
    $programname == 'sshd' or
    $programname == 'sudo' or
    $programname == 'pvedaemon' or
    $programname == 'pveproxy' or
    $programname == 'pvestatd' or
    $programname == 'corosync' or
    $programname == 'pve-ha-crm' or
    $programname == 'pveproxy-access' or
    $programname == 'pve-firewall'
) then {
    action(type="omfwd"
       target="192.168.1.50"
       port="20516"
       protocol="tcp")
}
EOF

# 3. MUST REPLACE: 192.168.1.50 with your Sekoia Forwarder IP address
FORWARDER_IP="192.168.1.50"
sed -i "s/192.168.1.50/${FORWARDER_IP}/g" /etc/rsyslog.d/50-sekoia.conf

# 4. Verify configuration syntax and restart rsyslog
rsyslogd -N1
systemctl enable --now rsyslog
```

### Test connection

Run this command on your Proxmox VE 9.2 node to trigger a test log:

```bash
logger -t pvedaemon "Sekoia Test Log from Proxmox VE 9.2 Node"
```

Verify that the message appears under Events in your Sekoia workspace.


{!_shared_content/operations_center/integrations/generated/8fad985c-bb61-4f96-8244-56ea8f625ac5_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_8fad985c-bb61-4f96-8244-56ea8f625ac5_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/8fad985c-bb61-4f96-8244-56ea8f625ac5.md!}
