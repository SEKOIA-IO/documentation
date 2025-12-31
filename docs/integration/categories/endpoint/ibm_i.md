---
uuid: fc03f783-5039-415e-915a-a4b010d9a872
title: IBM iSeries (AS/400)
name: IBM iSeries (AS/400)
type: intake
---

## Overview

IBM iSeries (AS/400) is a robust, scalable family of midrange business computers running the IBM i operating system, known for its integrated DB2 database and strong security features.

- **Vendor**: IBM
- **Supported environment**: On prem
- **Version Compatibility**: 7.5
- **Detection based on**: Telemetry

!!! warning
	Important - This integration requires the installation of Syslog Reporting Manager on IBM i, for which a fee is charged.

## Supported versions

This integration supports the following versions:

- 7.3
- 7.4
- 7.5

## Supported events

This integration supports the following events:

- Audit journal (Command entry, Authority failure)
- Integrated file system monitoring
- Message queues monitoring
- Database monitoring
- History logs

## Configure

In this guide, you will configure the gateway to forward events to syslog.

### Prerequisites

1. An internal syslog concentrator is required to collect and forward events to Sekoia.io.
2. Syslog Reporting Manager installed on the iSeries. See [docs](https://www.ibm.com/support/pages/ibm-i-security) for more info.

### Forward IBM iSeries events

1. Ensure having `Syslog Reporting Manager` installed and configured
2. On the SLMON menu, type `CFGSRM`
3. On the Configure global settings, select Option `2`
4. Type the address and the port of the log concentrator
5. Select `RFC5424` as `Syslog format`
6. Select `CEF` as `SIEM message format`
7. Select the protocol for the log concentrator (`TCP` is recommended)
8. At the bottom of the screen, press `Enter` to save the changes

### Enable Audit logs (optional)

1. On the SLMON menu, type `CFGSRM`
2. On the Configure global settings, select Option `10`
3. Enable the following type:
	- AF: Authority failures
	- CD: Command string audit
4. Press `F3` to save the changes

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format IBM iSeries.

## Send logs to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

{!_shared_content/operations_center/integrations/generated/fc03f783-5039-415e-915a-a4b010d9a872_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_fc03f783-5039-415e-915a-a4b010d9a872_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/fc03f783-5039-415e-915a-a4b010d9a872.md!}
