---
uuid: d6f69e04-6ab7-40c0-9723-84060aeb5529
title: Rubycat PROVE IT
name: Rubycat PROVE IT
type: intake
---

## Overview
PROVE IT by Rubycat is a privileged access management solution.

- **Vendor**: Rubycat
- **Supported environment**: On prem
- **Version compatibility**: 5,0
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication logs


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

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d6f69e04-6ab7-40c0-9723-84060aeb5529_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d6f69e04-6ab7-40c0-9723-84060aeb5529.md!}

## Troubleshooting

### TLS error: Rsyslog cannot authenticate the Sekoia.io syslog endpoint

The Sekoia.io syslog endpoint is secured with a [Letsencrypt](https://letsencrypt.org) certificate.

According to our installation, it may be necessary to install `ISRG ROOT X1` certificate in our **trusted root certification authorities certificate store**:

1. Download the `ISRG ROOT X1` certificate: <https://letsencrypt.org/certs/isrgrootx1.pem>

```bash
$ wget https://letsencrypt.org/certs/isrgrootx1.pem -O /tmp/isrgrootx1.pem
```

2. Move the certificate to the relevant directory (e.g., `/etc/ssl/certs` for Debian-based distributions, `/etc/pki/tls/certs` for Red Hat-based distributions; please refer to the documentation of your operating system distribution)
