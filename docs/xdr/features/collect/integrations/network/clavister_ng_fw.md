uuid: 64d118f0-84a5-4f46-ab05-7776bd6d0eed
name: Clavister Next-Gen Firewall
type: intake

## Overview

Clavister Next-Gen Firewall offers advanced network protection with integrated features like intrusion prevention, application control, and content filtering, designed to safeguard enterprises from diverse cybersecurity threats.

- **Supported version**: Clavister cOS core 15.10.05
- **Supported events**:
  - **network**:
    - ALG
    - ARP
    - CONN
    - DNSCACHE
    - DYNROUTING
    - IP_PROTO
    - IPREPUTATION
    - OSPF
    - SNMP
    - SSL
    - TCP_FLAG
    - TCP_OPT
  - **session**:
    - IPSEC
    - ONECONNECT
    - SESMGR
  - **application control (APPCONTROL)**
  - **authentication (USERAUTH)**
  - **rule (RULE)**

{!_shared_content/operations_center/detection/generated/suggested_rules_64d118f0-84a5-4f46-ab05-7776bd6d0eed_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/64d118f0-84a5-4f46-ab05-7776bd6d0eed.md!}


## Configure

This setup guide will show you how to forward your Clavister Next-Gen Firewall events to Sekoia.io.

### Prerequisites
* Having an internal log concentrator

### Configure Clavister cOS to forward logs

There are two ways to configure Configure Clavister cOS to forward logs:
* Command line interface (CLI)
* Web interface

#### Command line interface (CLI)
To configure the Clavister cOS to forward logs using the CLI, follow these steps:

1. Log into the firewall console
2. Add a new log receiver
    ```shell
    Device:/> add LogReceiver LogReceiverSyslog <name of the receiver> IPAddress=<ip of the log concentrator> LogSeverity=Emergency,Alert,Critical,Error,Warning,Notice,Info Facility=local1
    ```
3. Exit the console

#### Web interface
To configure the Clavister cOS to forward logs using the web interface, follow these steps:

1. Log into the interface
2. Go to `System` > `Device` > `Log Receivers` > `Add` > `Syslog Receiver`
3. Type a name of the log receiver
4. Type the ip address of the log concentrator as IP Address
5. Select `local1` from the `Facility` list
6. Select from `Emergency` to `Info` as `SeverityFilter`
7. Click on `OK`

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Clavister Next-Gen Firewall`. Copy the intake key.
