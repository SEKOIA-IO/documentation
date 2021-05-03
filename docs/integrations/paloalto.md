uuid: 903ec1b8-f206-4ba5-8563-db21da09cafd
name: Palo Alto

## Overview

Palo Alto Networks offers an enterprise cybersecurity platform which provides network security, cloud security, endpoint protection, and various cloud-delivered security services.

## Palo Alto logs

On Palo Alto appliances, most of the important hardward and software activities that are relevant for security detection and analysis, are logged into three files.

- Traffic: Local out traffic, Denied traffic, Allowed traffic
- System
- Security


## Transport to the collector

### Prerequisites
The following prerequisites are needed in order to setup efficient log concentration:
- Have administrator priviledge on the Palo Alto
- Traffic towards the Rsyslog must be open on `UDP 514`

### Configure Palo Alto

#### Configure a Syslog server profile

1. In the GUI, go to `Device > Serve Profiles > Syslog`.
2. Click `Add` and enter a name for the profile such as `Syslog server`.
3. If the firewall has more than one virtual system (vsys), select the `Location` (vsys or `Shared`) where this profile is available.
4. Click `Add` and enter the information that the firewall requires to connect to it:

- Name — Unique name for the server profile.
- Syslog Server — IP address or fully qualified domain name (FQDN) of the syslog server.
- Transport — Select UDP.
- Port — Select the default is UDP on port 514.
- Format — Select the syslog message format to use: BSD (the default).
- Facility — Select a syslog standard value (default is LOG_USER) to calculate the priority (PRI) field.

5) Click `OK` to save the server profile.

#### Configure syslog forwarding for Traffic logs

1. Select `Objects > Log Forwarding`, click `Add`, and enter a `Name` to identify the profile.
2. For each log type (here Traffic, Threat and WileFire Malicious) and each severity level, select the `Syslog server` profile and click `OK`.
3. Select `Policies > Security` and select a policy rule.
4. Select the `Actions` tab and select the `Log Forwarding` profile you created.
5. In the `Profile Type` drop-down, select `Profiles` or `Groups`, and then select the security profiles or `Group Profiles` required to trigger log generation and forwarding.
6. Select both of the `Log at Session Start` and `Log At Session End` check boxes, and click `OK`.

For detailed information about configuring a log forwarding profile and assigning the profile to a policy rule, see [Configure Log Forwarding](https://docs.paloaltonetworks.com/pan-os/8-1/pan-os-admin/monitoring/configure-log-forwarding.html#id1443a62b-8a0b-41db-a08d-5df934bf0ffc)

#### Configure syslog forwarding for System and User-ID logs

1. In the GUI, go to `Device > Log Settings`.
2. Click each Severity level (High and Critical if also fine), select the `Syslog server` profile, and click `OK`.

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
Open or create a new Palo Alto configuration file for Rsyslog:
```bash
sudo vim /etc/rsyslog.d/38-paloalto.conf
```

Paste the following Rsyslog configuration to trigger the emission of Palo Alto logs by your Rsyslog server to SEKOIA.IO:
```bash
# Define the SEKIOA-IO intake certificate
$DefaultNetstreamDriverCAFile /etc/rsyslog.d/SEKOIA-IO-intake.pem

# Template definition [RFC5424](https://tools.ietf.org/html/rfc5424#section-7.2.2)
# IMPORTANT: don't forget to set your intake key in the template
template(name="SEKOIAIOPaloAltoTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\"] %msg%\n")


# Send your events to SEKOIA.IO intake servers under SEKOIAIOPaloAltoTemplate template
if ($hostname == "YOUR_PALOALTO_HOSTNAME") then {
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
        Template="SEKOIAIOPaloAltoTemplate"
    )
}
```

> In the above `template` instruction, please replace `YOUR_INTAKE_KEY` variable with your intake key you can find in the Operation Center > Configure > Intakes
> And change the `YOUR_PALOALTO_HOSTNAME` variable with the correct value.

##### Restart Rsyslog

```bash
$ sudo systemctl restart rsyslog.service
```

## Related files
- [SEKOIA-IO-intake.pem](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem): SEKOIA.IO TLS Server Certificate (1674b)

### Enjoy your events
Go to the [events page](https://app.sekoia.io/sic/events) to watch your incoming events.
