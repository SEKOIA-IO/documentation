uuid: 021e9def-5a55-4369-941e-af269b45bef1
name: Linux AuditBeat
type: intake

## Overview

Auditbeat communicates directly with the Linux audit framework, collects the same data as auditd, then the data can be stored in JSON inside a log file before being sent to a log concentrator.

- **Vendor**: Elastic
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: System Monitoring and Security

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

![linux_auditbeat_architecture](/assets/integration/linux_auditbeat_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Root access to the Linux machine
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

This setup guide will show you how to forward your Auditbeat logs to Sekoia.io by means of a syslog transport channel.

#### Install and Configure Auditbeat

- To download and install Auditbeat on a Debian-based distribution (including Ubuntu, Linux Mint, etc.):

```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.11.4-amd64.deb
sudo dpkg -i auditbeat-8.11.4-amd64.deb
```

- To download and install Auditbeat on Fedora, CentOS, or Red Hat Enterprise Linux:

```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.11.4-x86_64.rpm
sudo rpm -vi auditbeat-8.11.4-x86_64.rpm
```

> Modify the version number with the newest one.

- Replace the configuration file `/etc/auditbeat/auditbeat.yml` with the following content:

```yaml
########################## Auditbeat Configuration #############################

# =========================== Modules configuration ============================
auditbeat.modules:

# The auditd module collects events from the audit framework in the Linux
# kernel. You need to specify audit rules for the events that you want to audit.
- module: auditd
  resolve_ids: true
  failure_mode: silent
  backlog_limit: 8196
  rate_limit: 0
  include_raw_message: false
  include_warnings: false

  # Load audit rules
  audit_rules: |
    ## Example of audit rules here. Comment what is NOT needed
    ## Executions.
    -a always,exit -F arch=b64 -S execve,execveat -k exec

    ## External access (warning: these can be expensive to audit).
    -a always,exit -F arch=b64 -S accept,bind,connect -F key=external-access

    ## Identity changes.
    -w /etc/group -p wa -k identity
    -w /etc/passwd -p wa -k identity
    -w /etc/gshadow -p wa -k identity

    ## Unauthorized access attempts.
    -a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -k access
    -a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -k access

# The file integrity module sends events when files are changed (created,
# updated, deleted). The events contain file metadata and hashes.
- module: file_integrity
  paths:
  - /bin
  - /usr/bin
  - /sbin
  - /usr/sbin
  - /etc
  - /var/spool/cron/crontabs
  - /etc/cron.d
  - /etc/cron.daily
  - /etc/cron.hourly
  - /etc/cron.monthly
  - /etc/cron.weekly

  scan_at_start: true
  scan_rate_per_sec: 50 MiB
  max_file_size: 100 MiB
  hash_types: [sha1]

  # Detect changes to files included in subdirectories. Disabled by default.
  recursive: false

- module: system
  datasets:
    - package   # Installed, updated, and removed packages
  period: 2m

- module: system
  datasets:
    - host      # General host information, e.g. uptime, IPs
    - login     # User logins, logouts, and system boots.
    - process   # Started and stopped processes
    - socket    # Opened and closed sockets
    - user      # User information

  user.detect_password_changes: true
  processors:
    - drop_event:
        when:
          or:
            - and:
              - equals:
                  destination.port: 53
              - equals:
                  event.action: network_flow
            - and:
              - equals:
                  event.action: network_flow
              - network:
                  source.ip: private
              - network:
                  destination.ip: private

# ================================== Outputs ===================================
output.elasticsearch:
  enabled: false

output.file:
  enabled: true
  codec.json:
  path: "/tmp/auditbeat"
  filename: auditbeat
  rotate_every_kb: 10000
  number_of_files: 7
  permissions: 0600

# =================================== Paths ====================================
path.home: "/usr/share/auditbeat/bin"
path.config: "/etc/auditbeat"
path.data: "/var/lib/auditbeat"
path.logs: "/var/log/auditbeat"

# ================================== Template ==================================
setup.template.settings:
  index:
    number_of_shards: 1

logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/auditbeat
  name: auditbeat
  rotateeverybytes: 10485760 # = 10MB
  keepfiles: 7
  permissions: 0600
```

- Ensure the permissions for the new `auditbeat.yml` are correct:

```bash
sudo chmod 0600 auditbeat.yml
sudo chown root:root auditbeat.yml
```

- Load the predefined assets for parsing, indexing, and visualizing your data:

```bash
sudo auditbeat -e
```

- Start Auditbeat:

```bash
sudo systemctl restart auditbeat.service
```

#### Configure Local Rsyslog Service

- Install rsyslog if it's not already installed:

```bash
sudo apt install rsyslog
```

- Edit the `/etc/rsyslog.conf` file for a light client rsyslog setup:

```bash
module(load="imuxsock")                                 # provides support for local system logging
module(load="imklog" permitnonkernelfacility="on")      # provides kernel logging support

$MaxMessageSize 20k
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat
$FileOwner root
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022
$ActionQueueType LinkedList
$ActionQueueFileName sek_fwd
$ActionQueueMaxDiskSpace 5g
$ActionQueueSaveOnShutdown on
$ActionResumeRetryCount -1
$WorkDirectory /var/spool/rsyslog
$IncludeConfig /etc/rsyslog.d/*.conf
*.* -/var/log/syslog
```

- Add a dedicated configuration file for Auditbeat logs in `/etc/rsyslog.d/8-linux_auditbeat.conf`:

```bash
module(load="imfile" PollingInterval="10")
input(type="imfile"
      File="/var/log/auditbeat/auditbeat*.ndjson"
      Tag="linux_auditbeat"
      Severity="info"
      Facility="local7"
      ruleset="auditbeatSekoia"
      addMetadata="on"
      )

ruleset(name="auditbeatSekoia") {
    if (re_match($!metadata!filename, "auditbeat-[0-9]{8}(-[0-9]*)?.ndjson")) then {
      action(
        type="omfwd"
        protocol="tcp"
        target="YOUR_RSYSLOG_DESTINATION_SERVER"
        port="514"
        TCP_Framing="octet-counted"
      )
    }
}
```

- Ensure the destination server in the rsyslog config is correctly set:

```bash
sudo systemctl restart rsyslog.service
```

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/021e9def-5a55-4369-941e-af269b45bef1_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_021e9def-5a55-4369-941e-af269b45bef1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/021e9def-5a55-4369-941e-af269b45bef1.md!}

## Further readings

- [Configure a remote Syslog server](https://docs.cyberwatch.fr/help/en/administration/remote_syslog_configuration/)