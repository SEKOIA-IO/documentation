uuid: eaa34af4-a194-485c-a33e-4cdd18d064b0
name: Linux AuditBeat

## Overview

Auditbeat communicates directly with the Linux audit framework, collects the same data as auditd then the data can be stored locally on a JSON format before beeing sent to a log concentrator.

## AuditBeat logs

With AuditBeat it is possible to collect various activities such as the following:

- Authentication: From system module, login dataset retreive User logins, logouts, and system boots
- File monitoring: From audit module, the file metricset sends events when a file is changed (created, updated, or deleted) on disk. The events contain file metadata and hashes
- Process command-line parameters: command-lines and arguments are extracted from Linux logs
- Process monitoring: From system module, process dataset retreive Started and stopped processes
- Process use of network: From system module, socket dataset retreive Opened and Closed sockets

## Transport to the collector

### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator privileges on the server
- Traffic towards the Rsyslog must be open on `TCP 514`

### Configure the Client

#### Install and configure AuditBeat

To download and install Auditbeat, use the commands that work with your system:

```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-7.13.1-amd64.deb
sudo dpkg -i auditbeat-7.13.1-amd64.deb
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

# ================================= Migration ==================================

# This allows to enable 6.7 migration aliases
#migration.6_to_7.enabled: false
```

In order to make it easier, you can download the auditbeat configuration file:

```bash
$ wget -O /etc/auditbeat/auditbeat.yml https://docs.sekoia.io/integrations/configurations/auditbeat.yml
```

> Don't forget to set the right level of permission of the new `auditbeat.yml` if you edited a new one.
> `sudo chmod 0600 auditbeat.yml`
> Plus in this case ensure the owner of the file is root: `sudo chown root:root auditbeat.yml`

Auditbeat comes with predefined assets for parsing, indexing, and visualizing your data. To load these assets:
```bash
sudo auditbeat -e
```

> If no error occurs, use `Ctrl + C` to stop running it in the terminal.

Start AuditBeat with the folling command:
```bash
sudo systemctl restart auditbeat.service
```

> Check your logs in `/tmp/auditbeat/auditbeat` in JSON format.

#### Configure the client Rsyslog

In order to allow the rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog
```

Settup a light client rsyslog by editing the `/etc/rsyslog.conf` file.

```bash
### Create a dedicated Rsyslog configuration file
module(load="imuxsock")                                 # provides support for local system logging
module(load="imklog" permitnonkernelfacility="on")      # provides kernel logging support

module(load="imfile" PollingInterval="10")              #needs to be done just once
input(type="imfile"
      File="/tmp/auditbeat/auditbeat"
      Tag="linux_auditbeat"
      Severity="info"
      Facility="local7")

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

if ($syslogtag contains 'linux_auditbeat') then {
     action(
         type="omfwd"
         protocol="tcp"
         target="YOUR_RSYSLOG_DESTINATION_SERVER"
         port="514"
         TCP_Framing="octet-counted"
     )
}

# Rules
*.*          -/var/log/syslog
```
> Don't forget to change the value of `YOUR_RSYSLOG_DESTINATION_SERVER` in the bottom of the `rsyslog.conf` file

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Transport to SEKOIA.IO

### Configure the Rsyslog to forward to SEKOIA.IO

#### Rsyslog prerequisites
In order to allow the rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog rsyslog-gnutls wget
```

Please ensure the UDP incoming events are allows in the /etc/rsyslog.conf
```bash
....
# provides UDP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")
....
```

#### Download the certificate
In order to allow the connection of your Rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

##### Configure the Rsyslog Server
Open or create a new AuditBeat configuration file for Rsyslog:
```bash
sudo vim /etc/rsyslog.d/9-auditbeat_linux.conf
```

Paste the following Rsyslog configuration to trigger the emission of AuditBeat logs by your Rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOAuditBeatLinuxTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOAuditBeatLinuxTemplate template
if ($syslogtag contains 'linux_auditbeat') then {
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
        Template="SEKOIAIOAuditBeatLinuxTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operation Center > Configure > Intakes
> And change the `YOUR_LINUX_HOSTNAME` variable with the correct value.

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
