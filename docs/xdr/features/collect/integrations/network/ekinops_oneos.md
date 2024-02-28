uuid: 4760d0bc-2194-44e5-a876-85102b18d832
name: Ekinops OneOS
type: intake

## Overview

  Ekinops OneOS is a comprehensive and flexible network operating system designed to meet the evolving needs of modern telecommunications networks. It provides a unified platform for managing and orchestrating a wide range of network functions, including routing, switching, security, and more. With its modular architecture and open APIs, OneOS enables network operators to easily deploy and scale their networks, while also providing the flexibility to integrate with third-party applications and services. This allows for greater innovation and agility in network operations, ultimately leading to improved service delivery and customer satisfaction.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_4760d0bc-2194-44e5-a876-85102b18d832_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/4760d0bc-2194-44e5-a876-85102b18d832.md!}

## Configure

This setup guide will show you how to forward your Ekinops OneOS logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator

### Enable Syslog forwarding logs

To enable syslog forwarding logs, you must follow the steps below:

1. Connect on the Ekinops OneOS console
2. Add the log concentrator as a new syslog server
```bash
localhost#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
localhost(config)#syslog server  <log concentrator server ip> 23 tcp <log concentrator port>
localhost(config)#logging syslog filter all
localhost(config)#logging syslog informational
localhost(config)#end
localhost#write mem
```
3. Check the configuration
```bash
localhost#show syslog servers
S.No Syslog Server                                    Facility VrfName                       Protocol  port    Interface                  Bytes-Sent
1    <log concentrator server ip>                      23      default 
```
4. exit the console

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Ekinops OneOS.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.