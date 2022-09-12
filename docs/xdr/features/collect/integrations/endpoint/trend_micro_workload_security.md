uuid: b2d961ae-0f7e-400b-879a-f97be24cc02d
name: Trend Micro Workload Security
type: intake

## Overview

Trend Micro Cloud One Workload Security detect malware, vulnerabilities and any other threats.
It protect your physical and virtual servers as well as, your cloud and containers instances.

{!_shared_content/operations_center/integrations/generated/cloud-one_do_not_edit_manually.md!}

## Configure

In this guide, you will configure your Workload Security Manager to forward events through syslog.

### Prerequisites

An internal log concentrator (Rsyslog) is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your Workload Security console and follow [this guide](https://cloudone.trendmicro.com/docs/workload-security/event-syslog/) to enable logs forwarding.
Provide the IP and the listening port (`514`) of the log concentrator and select `CEF` as the event format.

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
Check the certificate and click OK to accept it. Test the connection again; it should succeed. If not, please see the "Troubleshoot event forwarding" section on the Trend-Micro documentation.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Trend Micro Cloud One.


## Transport to SEKOIA.IO

Please consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
