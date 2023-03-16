uuid: 23b75d0c-2026-4d3e-b916-636c27ba4931
name: Cisco Web Security Appliance
type: intake

## Overview

The Cisco Web Security Appliance is a security device analyzing HTTP(S) traffic with malware detection and reputation filtering.
Sending Cisco Web Security Appliance logs to SEKOIA.IO enables the discovering of potential network security threats. Spotted threats are contextualized by means of  SEKOIA.IO's Cyber Threat Intelligence (CTI).
  
{!_shared_content/operations_center/integrations/generated/23b75d0c-2026-4d3e-b916-636c27ba4931.md!}

## Configure

### Prerequisites

An internal log concentrator is required to collect and forward events to SEKOIA.IO.

### Enable Syslog forwarding

Log on your Web Security appliance and follow [this guide](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-0/user_guide/b_WSA_UserGuide/b_WSA_UserGuide_chapter_010111.html#ariaid-title7) to create a log subscription with the retrieval method `Syslog Push` and the concentrator as the destination.


## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Cisco Secure Web Applicance`.

## Transport to SEKOIA.IO

Please consult the [Syslog Forwarding](../../../../ingestion_methods/sekoiaio_docker_concentrator/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [User Guide for AsyncOS 11.0 for Cisco Web Security Appliances](https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-0/user_guide/b_WSA_UserGuide/b_WSA_UserGuide_chapter_010111.html)
