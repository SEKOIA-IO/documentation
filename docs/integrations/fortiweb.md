uuid: d971c8c7-b7d0-4de1-9b5c-b58235c1d8e4
name: fortiweb

## Overview

In this documentation we will explain one way to collect and send FortiWeb logs to SEKOIA.IO.
- From the FortiWeb machine to an internal log concentrator (Rsyslog), then forwarded to SEKOIA.IO

## FortiWeb logs

On FortiWeb appliances, most of the important hardware and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Displays traffic flow information, such as HTTP/HTTPS requests and responses.
- Event: Displays administrative events, such as downloading a backup copy of the configuration, and hardware failures.
- Attack: Displays attack and intrusion attempt events.

## Transport to the concentrator

### Prerequisites

The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator writes on the FortiWeb (read & write permission)
- Traffic towards the Rsyslog must be open on `UDP 514`

### Configure FortiWeb

#### Enable logging via trigger mechanism

1. Go to `Log&Report > Log Config > Other Log Settings`
2. Tick the boxes : Enable Attack Log / Enable Traffic Log / Enable Event Log

#### Configure Syslog policies

1. Go to `Log&Report > Log Policy > Syslog Policy`.

> To access this part of the web UI, your administrator’s account access profile must have Read and Write permission to items in the Log & Report category. For details, see Permissions.

2. Click `Create New`.

> If the policy is new, in Policy Name, type the name of the policy as it will be referenced in the configuration.

3. Click Create New.
4. In `IP Address`, enter the address of the remote Syslog server.
5. In `Port`, enter the listening port number of the Syslog server. The default is 514.
6. Click `OK`.

#### Configure log destinations

1. Go to `Log&Report > Log Config > Global Log Settings`
2. Tick the syslog box
3. Select the relevant Syslog Policy, Log Level and Facility
4. Click `Apply`

For more information please refer to the official documentation of [FortiWeb](https://docs.fortinet.com/document/fortiweb/6.1.1/administration-guide/303842/logging)

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
Open or create a new FortiWeb configuration file for Rsyslog:
```bash
sudo vim /etc/rsyslog.d/14-fortiweb.conf
```

Paste the following Rsyslog configuration to trigger the emission of FortiWeb logs by your Rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOFortiwebTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOFortiwebTemplate template
if ($hostname == "YOUR_FORTIWEB_HOSTNAME") then {
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
        Template="SEKOIAIOFortiwebTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operations Center > Configure > Intakes
> And change the `YOUR_FORTIWEB_HOSTNAME` variable with the correct value.

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### IV. Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
