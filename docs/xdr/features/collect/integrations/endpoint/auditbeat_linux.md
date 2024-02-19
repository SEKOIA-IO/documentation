uuid: 021e9def-5a55-4369-941e-af269b45bef1
name: Linux AuditBeat
type: intake

## Overview

Auditbeat communicates directly with the Linux audit framework, collects the same data as auditd then the data can be stored in JSON inside a log file before being sent to a log concentrator.

{!_shared_content/operations_center/detection/generated/suggested_rules_021e9def-5a55-4369-941e-af269b45bef1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/021e9def-5a55-4369-941e-af269b45bef1.md!}

## Configure

### Transport to the collector

#### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the server
- Traffic towards the log collector sever which is using syslog must be open on port `TCP/514`

#### Configure the client

##### Install and configure Auditbeat

To download and install Auditbeat on a Debian based distributions (including Ubuntu, Linux Mint, etc.). Use the commands that work with your system:

```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.11.4-amd64.deb
sudo dpkg -i auditbeat-8.11.4-amd64.deb
```

To download and install Auditbeat on Fedora, CentOS or Red Hat Enterprise Linux, use the commands that work with your system:

```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.11.4-x86_64.rpm
sudo rpm -vi auditbeat-8.11.4-x86_64.rpm
```

> Modify the version number with the newest one.

Auditbeat uses `modules` to collect audit information.
By default, Auditbeat uses a configuration that’s tailored to the operating system where Auditbeat is running.

Replace the configuration file `/etc/auditbeat/auditbeat.yml` by the following content:

```bash
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

# ================================== Outputs ===================================
# ---------------------------- Elasticsearch Output ----------------------------
output.elasticsearch:
  enabled: false

# -------------------------------- File Output ---------------------------------
output.file:
  enabled: true

  # Configure JSON encoding
  codec.json:
    #pretty: false
    # Configure escaping HTML symbols in strings.
    #escape_html: false

  # Path to the directory where to save the generated files.
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

# Elasticsearch template settings
setup.template.settings:
  # A dictionary of settings to place into the settings.index dictionary
  index:
    number_of_shards: 1
    #codec: best_compression

# ================================== Logging ===================================

logging.level: info

logging.to_files: true
logging.files:
  path: /var/log/auditbeat
  name: auditbeat
  rotateeverybytes: 10485760 # = 10MB
  keepfiles: 7
  permissions: 0600

```

> Don't forget to set the right level of permission of the new `auditbeat.yml` if you edited a new one.
> `sudo chmod 0600 auditbeat.yml`
> Plus in this case ensure the owner of the file is `root`: `sudo chown root:root auditbeat.yml`

Auditbeat comes with predefined assets for parsing, indexing, and visualizing your data. To load these assets:
```bash
sudo auditbeat -e
```

> If no error occurs, use `Ctrl + C` to stop running it in the terminal.

Start Auditbeat with the following command:
```bash
sudo systemctl restart auditbeat.service
```

> Check your logs in `/tmp/auditbeat/auditbeat` in JSON format.
> It may be recommended to set up logrotate for the Auditbeat logs generated in `/tmp/auditbeat`.

##### Configure local Rsyslog service

In order to allow the rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog
```

Settup a light client rsyslog by editing the `/etc/rsyslog.conf` file.

```bash
### Create a dedicated Rsyslog configuration file
module(load="imuxsock")                                 # provides support for local system logging
module(load="imklog" permitnonkernelfacility="on")      # provides kernel logging support

# Set the maximum supported message size
$MaxMessageSize 20k

# Use traditional timestamp format.
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

# Set the default permissions for all log files.
$FileOwner root
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022

$ActionQueueType LinkedList     # create a queue stored in the RAM
$ActionQueueFileName sek_fwd    # set up the prefix for writting
$ActionQueueMaxDiskSpace 5g     # allow 5 giga of storage for the buffer
$ActionQueueSaveOnShutdown on   # write on disk is the rsyslog is whut down
$ActionResumeRetryCount -1      # prevent the rsyslog from droping the logs if the connexion is interrupted

# Where to place spool and state files
$WorkDirectory /var/spool/rsyslog
$IncludeConfig /etc/rsyslog.d/*.conf

# Rules
*.*          -/var/log/syslog
```

Please ensure, options `$PrivDropToUser syslog` and `$PrivDropToGroup syslog` are removed, otherwise rsyslog process could not read auditbeat output.

And add a dedicated configuration file for the Auditbeat logs in `/etc/rsyslog.d/8-linux_auditbeat.conf` to be sent to a log concentrator.

```bash
module(load="imfile" PollingInterval="10")              #needs to be done just once
input(type="imfile"
      File="/tmp/auditbeat/auditbeat*.ndjson"
      Tag="linux_auditbeat"
      Severity="info"
      Facility="local7"
      ruleset="auditbeatSekoia"
      addMetadata="on"
      )

ruleset(name="auditbeatSekoia") {
    if (re_match($!metadata!filename, "auditbeat-[0-9]{8}.ndjson")) then {  
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

> Don't forget to change the value of `YOUR_RSYSLOG_DESTINATION_SERVER` in the bottom of the `rsyslog.conf` file

###### Restart Rsyslog

```bash
sudo systemctl restart rsyslog.service
```

### Forward logs to Sekoia.io

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation or [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to transport logs to Sekoia.io.

### Enjoy your events
Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.
