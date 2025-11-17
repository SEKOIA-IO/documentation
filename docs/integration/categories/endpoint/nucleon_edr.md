uuid: 516d93f9-86b0-4038-a85b-c9be72035ac4
name: NucleonEDR
type: intake

## Overview

Nucleon EDR is an Endpoint Detection & Response platform built on Zero-Trust principles and enhanced by AI-driven detection.
This documentation shows how to setup the automated events forwarding from the EDR to Sekoia.io.

- **Vendor**: Nucleon Security
- **Supported environment**: On Premise / Cloud
- **Detection based on**: Telemetry / Alert
- **Supported application or feature**: System & network events

## Configure

### Prerequisite

For on-premise environment, network access must be open to forward logs from the EDR Console to Sekoia.io on the expected port.

### Steps

#### Create your intake on Sekoia.io

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Nucleon EDR`.

Copy the intake key. This key will be configured in the EDR Console.

#### In Nucleon EDR Console

1. Open the Entities view to access the list of all entities your user can manage.
![Nucleon EDR Entities view](/assets/integration/endpoint/nucleonedr/nucleonedr-entities-view.png)

2. Click on the entity where the forwarding must be configured.

3. In the "Entity details" section, click on `Syslog Export` button.
![Nucleon EDR Syslog Export](/assets/integration/endpoint/nucleonedr/nucleonedr-syslog-export.png)

4. In the `Syslog Configuration` panel, click on `Add New Configuration`

5. Fill in all required fields in the form, and the Intake key previously generated:
    - Name: `Sekoia`
    - Host: `intake.sekoia.io`
    - Port: `10514`
    - Protocol: `TLS`
    - Format: `RFC 5424`
    - Click on `Add Block` to add structured data to the syslog exporter
    - Block ID: `sekoia@53288`
    - Click on `Add Parameter` to add a new parameter in the structured block
    - Key: `intake_key`
    - Value: *Insert the generated intake key here*
![Nucleon EDR Syslog Settings](/assets/integration/endpoint/nucleonedr/nucleonedr-syslog-settings.png)

6. Select the information you want to export in the Event filtering rules. We suggest enabling all options by default.
![Nucleon EDR Event Settings](/assets/integration/endpoint/nucleonedr/nucleonedr-event-settings.png)

7. Click on `Save` button to finish the setup. New events will then be forwarded directly.
