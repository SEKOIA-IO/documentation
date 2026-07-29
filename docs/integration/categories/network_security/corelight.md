uuid: 21e0297d-93cc-4d92-90df-cefc92be563d
name: Corelight
type: intake

## Overview

Corelight is an Open NDR (Network Detection and Response) platform built on Zeek and Suricata. Corelight sensors transform raw network traffic into rich, structured JSON logs (connections, DNS, HTTP, SSL/TLS, files, notices) and Suricata IDS alerts, providing network ground-truth evidence for threat detection, threat hunting and incident response. In this documentation we will explain how to collect and send Corelight Sensor logs to Sekoia.io.

- **Vendor**: Corelight
- **Supported environment**: On premise (physical or virtual sensor)
- **Version compatibility**: Sensor / Fleet Manager 28.3.1 or above (HTTP export), 28.4 or above (Syslog export)
- **Detection based on**: Telemetry, Alert
- **Supported application or feature**: Network protocol analysis, Network intrusion detection system, DNS records, Web logs, SSL/TLS certificates

## Specification

### Prerequisites

- **Resource:**
    - A Corelight Sensor (physical or virtual) or a Corelight Fleet Manager
- **Network:**
    - Outbound HTTPS traffic allowed from the sensor to `https://intake.sekoia.io`
- **Permissions:**
    - Administrator access to the Corelight Sensor or Fleet Manager to configure an exporter

### Transport Protocol/Method

- **Direct HTTP(S)** — the Corelight sensor pushes JSON events directly to Sekoia.io

!!! Note
    Corelight sends events to Sekoia.io in **push** mode. No connector is required for this integration.

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON
- **Supported log types**: `conn`, `dns`, `http`, `ssl`, `files`, `notice`, `intel` (Zeek Intelligence Framework) and `suricata_corelight` (Suricata IDS alerts)

## Step-by-Step Configuration Procedure

This setup guide describes how to forward logs from a Corelight Sensor to Sekoia.io using the HTTP Exporter in push mode.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

!!! warning "Push mode — connector not required"
    Corelight sends its events to Sekoia.io in **push** mode. A connector is **not** needed for this integration.

    The `intake key` generated when you create the intake must be provided to the Corelight sensor (see below), where it is added as a custom HTTP header. The intake key identifies your community and routes the events to the correct intake. Do not modify its value: Sekoia.io rejects events carrying an altered intake key.

!!! Note
    Corelight includes the emitting sensor name in every event (`_system_name`, mapped to `observer.name`). A single intake key can therefore be shared across a whole fleet: each event remains attributable to its source sensor, and you can filter events per sensor in Sekoia.io.

### Instructions on the 3rd party solution

The following steps describe the configuration through the Corelight Fleet Manager. The equivalent settings are available directly on a standalone sensor.

#### Enable dynamic exporters

1. In the Fleet Manager (or sensor UI), go to **Configuration › Advanced › Advanced Configuration**.
2. Enable the setting `bro.exporters.dynamic.enable`.

#### Configure the HTTP Exporter

1. Go to **Policies › [your policy] › Export** and add a new **HTTP Exporter**.
2. Configure the exporter with the following values:

| Field         | Value                                                                                          |
|---------------|------------------------------------------------------------------------------------------------|
| URI           | `https://intake.sekoia.io`                                                                     |
| Method        | `POST`                                                                                         |
| HTTP Headers  | Add a header — key: `X-SEKOIAIO-INTAKE-KEY`, value: the `intake key` generated on Sekoia.io    |
| Compression   | `gzip` (default) — optional                                                                    |

3. (Recommended) Limit the volume by selecting the high-value log types for the SOC via **Exporter Log Filters** or **Zeek Logs to Include**: `conn`, `dns`, `http`, `ssl`, `files`, `notice`, `intel`, `suricata_corelight`.
4. Save the policy and apply it to the sensor.

Once applied, the sensor starts pushing JSON events to Sekoia.io over HTTPS.

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/21e0297d-93cc-4d92-90df-cefc92be563d_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_21e0297d-93cc-4d92-90df-cefc92be563d_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/21e0297d-93cc-4d92-90df-cefc92be563d.md!}

## Further Readings

- [Corelight documentation](https://docs.corelight.com/)
- [Zeek documentation](https://docs.zeek.org/)
