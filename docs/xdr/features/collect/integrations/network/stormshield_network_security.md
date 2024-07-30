uuid: 79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4
name: Stormshield Network Security
type: intake

## Overview

Stormshield Network Security firewalls provides comprehensive security and high performance network protection. In addition, they offer a high degree of scalability to support the evolution of IT and OT networks

In this documentation we will explain how to collect and send Stormshield Network Security logs to Sekoia.io.


{!_shared_content/operations_center/detection/generated/suggested_rules_79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/79029ef9-e5d3-44f3-b70f-fd3b54ba1fe4.md!}

## Configure

This section will guide you to forward Stormshield SNS logs to Sekoia.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Stormshield Network Security.

### Import the intake certificate

On a device, please download the [Sekoia.io intake certificate](https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem)

1. Log on the UTM administration console
2. Click `Configuration` tab
3. On the left panel, Click `Objects` > `Certificats and PKI`
4. Click `+ Add`
5. Select the intake certificate
6. Click `Import`

### Configure the log forwarding

1. Log on the UTM administration console
2. Click `Configuration` tab
3. On the left panel, Click `Notification` > `Traces - syslog - IPFX`
4. Click `syslog` tab
5. Click `SEKOIA syslog` profile
6. Type `intake.sekoia.io` as the syslog server
7. Select `TLS` as the protocol
8. Select `sekoia_syslog_tls` (10514) as the destination port
9. Select `ISRG Root X` as the Certificate authority
10. Select `RFC5424` as the format
11. In the advanced configuration section, paste the intake key
12. Click `APPLY`
