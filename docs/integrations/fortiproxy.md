uuid: d971c8c7-b7d0-4de1-9b5c-b58235c1d7e4
name: fortiproxy

## Overview

FortiProxy is a web proxy that protects clients against internet threats.
In this documentation we will explain one way to collect and send FortiProxy logs to SEKOIA.IO.
- From the FortiProxy server to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

## FortiProxy logs

On FortiProxy appliances, differents type of logs are available. This intake currently supports :

- Traffic: Records traffic flow information, such as HTTP/HTTPS requests and responses.
- HTTP Transaction: Records HTTP transaction-related traffic log.
- DLP: Records data leak prevention events.

## Transport to the concentrator

### Prerequisites

The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator rights on FortiProxy
- Traffic towards the Rsyslog must be open on `UDP 514`

### Configure FortiProxy

#### Configure logging to a RSYSLOG server

1. Go to `Log > Log Settings > Remote Logging and Archiving`
2. Tick the box `Send Logs to Syslog`
3. In `IP Address/FQDN`, enter the IP address or the domain name of the remote Syslog server.
4. In `Log Settings` you can customize what types of events you want to send to SEKOIA.IO. By default :
   - `Event Logging` : `All`
   - `Local Traffic Log` : `All`

5. Click `Apply`

For more information please refer to the official documentation of [FortiProxy](https://docs.fortinet.com/document/fortiproxy/7.0.0/administration-guide/707542/log-settings#Log_Settings)

## Transport to SEKOIA.IO

### Configure the Rsyslog to forward to SEKOIA.IO

#### Rsyslog prerequisites
In order to allow the rsyslog to work properly, please ensure the following packages are installed:

```bash
sudo apt install rsyslog rsyslog-gnutls wget
```

Please ensure the UDP incoming events are allowed in the /etc/rsyslog.conf
```bash
....
# provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")
....
```

#### Download the certificate
In order to allow the connection of your Rsyslog server to the SEKOIA.IO intake, please download the SEKOIA.IO intake certificate:

```bash
$ wget -O /etc/rsyslog.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

##### Configure the Rsyslog server
Open or create a new FortiProxy configuration file for Rsyslog:
```bash
sudo vim /etc/rsyslog.d/15-fortiproxy.conf
```

Paste the following Rsyslog configuration to trigger the emission of FortiProxy logs by your Rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOFortiproxyTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOFortiproxyTemplate template
if ($hostname == "YOUR_FORTIPROXY_HOSTNAME") then {
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
        Template="SEKOIAIOFortiproxyTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operation Center > Configure > Intakes
> And change the `YOUR_FORTIPROXY_HOSTNAME` variable with the correct value.

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### IV. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
