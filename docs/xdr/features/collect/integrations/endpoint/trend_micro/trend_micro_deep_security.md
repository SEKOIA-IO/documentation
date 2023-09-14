uuid: b2d961ae-0f7e-400b-879a-f97be24cc02d
name: Trend Micro Deep Security / Workload Security
type: intake

## Overview

Trend Micro Deep Security / Workload Security detect malware, vulnerabilities and some other threats.
It protect your physical and virtual servers as well as, your cloud and containers instances.

{!_shared_content/operations_center/detection/generated/suggested_rules_b2d961ae-0f7e-400b-879a-f97be24cc02d_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/b2d961ae-0f7e-400b-879a-f97be24cc02d.md!}

## Configure

In this guide, you will configure your Security Manager to forward events through syslog.

### Prerequisites

An internal syslog concentrator is required to collect and forward events to Sekoia.io.

### Enable Syslog forwarding

To enable syslog forwarding, for Trend Micro Deep Security, please follow [this guide](https://help.deepsecurity.trendmicro.com/20_0/on-premise/event-syslog.html).
For Trend Micro Workload Security, please refer to [this documentation](https://cloudone.trendmicro.com/docs/workload-security/event-syslog/)

Log on your Security console. Provide the IP and the listening port (`514`) of the log concentrator and select `CEF` as the event format.

#### Direct forwarding

If the concentrator and all your agents are on the same network or could communicate safely (VPN, ...),
select the transport protocol `UDP` and ask your agents to send events `Directly to the syslog server`. 
Apply the changes.

#### Indirect forwarding

If your agents should forward events over untrusted network,
select the transport protocol `TLS` and ask your agents to send events `Via the Workload Security Manager`. 
Generate and add a certificate to the log concentrator.
Apply the changes and test the connection.

For the first connection, the manager should display the error message "Accept Server Certificate?".
Check the certificate and click OK to accept it. Test the connection again; it should succeed.
If not, please see the "Troubleshoot event forwarding" section on the Trend-Micro documentation.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trend Micro Deep Security / Workload Security.


## Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
