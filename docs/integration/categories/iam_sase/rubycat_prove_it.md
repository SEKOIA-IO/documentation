uuid: d6f69e04-6ab7-40c0-9723-84060aeb5529
name: Rubycat PROVE IT
type: intake

## Overview
  - **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**: Telemetry
- **Version compatibility**:
- **Detection based on**:
- **Supported application or feature**:

PROVE IT by rubycat is a privileged access management solution.





## Setup

This setup guide will show you how to forward logs produced by PROVE IT to Sekoia.io by means of an Rsyslog transport channel.

On most GNU/Linux servers, two packages need to be installed: `rsyslog` and `rsyslog-gnutls`.

### Download the certificate

In order to allow the connection of your rsyslog server to the Sekoia.io intake, please download the Sekoia.io intake certificate:

```bash
$ wget -O /etc/rsyslog.d/Sekoia.io-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

### Configure the rsyslog server

Open or create a new PROVE IT configuration file for rsyslog:

```bash
sudo vim /etc/rsyslog.d/46-proveit.conf
```

Paste the following rsyslog configuration to trigger the emission of Pulse Connect Secure logs by your Rsyslog server to Sekoia.io:

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/Sekoia.io-intake.pem

# Configure up the network ssl connection
$ActionSendStreamDriver gtls # use gtls netstream driver
$ActionSendStreamDriverMode 1 # require TLS for the connection
$ActionSendStreamDriverAuthMode x509/name # server is authenticated

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOProveITTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")

# Send your events to Sekoia.io intake servers under SEKOIAIOPulseTemplate template
if $hostname == "YOUR_PROVEIT_HOSTNAME" then @@(o)intake.sekoia.io:10514;SEKOIAIOProveITTemplate
```

In the above template instruction, change the `YOUR_PROVEIT_HOSTNAME` variable with the correct value, and please replace `YOUR_INTAKE_KEY variable` with your intake key.

### Restart Rsyslog

```bash
$ sudo service rsyslog restart
```

### Enjoy your events

Go to the [events page](https://app.sekoia.io/operations/events) to watch your incoming events.

## Related files

- [Sekoia.io-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): Sekoia.io TLS Server Certificate (1674b)

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_d6f69e04-6ab7-40c0-9723-84060aeb5529_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d6f69e04-6ab7-40c0-9723-84060aeb5529.md!}

