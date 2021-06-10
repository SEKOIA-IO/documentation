uuid: 5702ae4e-7d8a-455f-a47b-ef64dd87c981
name: fortigate

## Overview

The range of Fortigate firewalls is a complete appliance solution whose security functions are highly developed. The firewalls run on the FortiOS operating system.

In this documentation we will explain one way to collect and send Fortigate logs to SEKOIA.IO.

- From the Fortigate machine to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

## Fortigate logs

On Fortigate appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Local out traffic, Denied traffic, Allowed traffic
- Web
- Url-Filtering
- VPN

## Transport to the concentrator

### Prerequisites

The following prerequisites are needed in order to setup efficient log concentration:

- Have administrator writes on the Fortigate
- Traffic towards the Rsyslog must be open on `TCP/514`

### Configure Fortigate

The first step is to configure Fortigate to log the awaited traffic.
You can configure FortiOS to send log messages to remote syslog servers in standard, CSV or CEF (Common Event Format) format. These three formats are accepted by the SEKOIA.IO intake.
To enable syslog, log into the CLI and enter the following commands:

```bash
config log syslogd setting
set status enable
set port 514
set mode reliable
set server [IP address of syslog server]
set facility user
end
```

Most FortiGate features are enabled for logging by default. Ensure they are enabled by executing the following command:

```bash
show full-configuration
```

Make sure the Traffic, Web and URL Filtering features are enabled for logging with the following commands:

```bash
config log syslogd filter
set forward-traffic enable
set local-traffic enable
set multicast-traffic enable
....
set vpn enable
set web enable
set url-filter enable
end
```

With some Fortigate appliance, it may not be possible to do the above configuration through the command line. An alternative method is to use the graphical interface and go to the `Log Settings` menu. From there you can choose every logging options within `Event Logging` and `Local Traffic Log` except for the `Denied` options.

Then in order to use CEF format, use the following commands :

```bash
config log syslogd setting
set format cef
end
```

## Transport to SEKOIA.IO

### Configure the Rsyslog to forward to SEKOIA.IO

#### Rsyslog prerequisites
In order to allow the rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog rsyslog-gnutls wget
```

Please ensure the TCP incoming events are allows in the /etc/rsyslog.conf

```bash
....
# provides TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")
....
```

#### Download the certificate
In order to allow the connection of your Rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

##### Configure the Rsyslog server
Open or create a new Fortigate configuration file for Rsyslog:

```bash
sudo vim /etc/rsyslog.d/12-fortigate.conf
```

Paste the following Rsyslog configuration to trigger the emission of Fortigate logs by your Rsyslog server to SEKOIA.IO:

```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOFortigateTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] CEF:%msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOFortigateTemplate template
if ($hostname == "YOUR_FORTIGATE_HOSTNAME") then {
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
        Template="SEKOIAIOFortigateTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operation Center > Configure > Intakes
> And change the `YOUR_FORTIGATE_HOSTNAME` variable with the correct value.

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Related files

- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

## Enjoy your events

Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
