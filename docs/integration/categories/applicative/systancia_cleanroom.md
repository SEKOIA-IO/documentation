# systancia\_cleanroom

uuid: dcb14795-a6f0-4ebb-a73d-6eb8b982afcd name: Systancia Cleanroom type: intake

### Overview

* **Vendor**: Systancia
* **Supported environment**: On-premise
* **Version compatibility**: 4.5 and newer
* **Detection based on**: Telemetry
* **Supported application or feature**: Application Logs

Systancia Cleanroom is a secure and isolated virtualized environment that ensures confidentiality and integrity for sensitive data and applications, offering a controlled and monitored workspace for high-security operations without compromising efficiency or user experience.

### Configure

This setup guide will show you how to forward your Systancia Cleanroom logs to Sekoia.io by means of a syslog transport channel.

#### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../../integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

#### Systancia Cleanroom

1. In the Systancia Clearoom system console, go to `Logger settings`
2. In the `Logger setting` panel:
   1. Select `Send events to a remote syslog`
   2. Type the address and the port to the log concentrator
   3. Select `TCP` (recommended) or `TLS` as the transport protocol
   4. Click Validate

#### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Systancia Cleanroom.

{!\_shared\_content/operations\_center/integrations/generated/dcb14795-a6f0-4ebb-a73d-6eb8b982afcd\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_dcb14795-a6f0-4ebb-a73d-6eb8b982afcd\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/dcb14795-a6f0-4ebb-a73d-6eb8b982afcd.md!}
