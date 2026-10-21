uuid: c10307ea-5dd1-45c6-85aa-2a6a900df99b
name: Winlogbeat
type: intake

# Winlogbeat

## Overview

Winlogbeat is an open-source log collector from Elastic that reads Windows Event Logs and sends them as JSON events to a Logstash log concentrator. Logstash then forwards the events to Sekoia.io over HTTPS.

- **Vendor**: Elastic
- **Supported environment**: On-premise
- **Detection based on**: Telemetry
- **Supported application or feature**: System monitoring and security

## High-level architecture diagram

- **Type of integration**: Outbound, with Winlogbeat sending events to Logstash and Logstash forwarding them to Sekoia.io
- **Schema**: JSON

![Winlogbeat architecture](/assets/integration/winlogbeat_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- A self-managed Logstash server.
- Outbound HTTPS traffic from the Logstash server to Sekoia.io.
- Administrator access to the Windows server running Winlogbeat.
- Root access to the Linux server running Logstash, if Logstash is hosted on Linux.

### Transport protocol and method

Winlogbeat sends events to Logstash through the Beats input. Logstash forwards the complete JSON events to Sekoia.io through the Sekoia.io HTTP intake endpoint.

### Log details

- **Supported functionalities**: Windows application, system, security, forwarded events, and PowerShell event collection. See [Overview](#overview).
- **Supported structure**: JSON.
- **Supported verbosity level**: Informational.

!!! note "Log levels"

    Log levels follow the taxonomy defined in [RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt this description if the source uses different terminology.

## Configure Winlogbeat

### Install and configure Winlogbeat

1. Download the Winlogbeat archive from the [Elastic download page](https://www.elastic.co/downloads/beats/winlogbeat).

2. Extract the archive to `C:\Program Files\winlogbeat`.

3. Open PowerShell as an administrator.

4. Change to the Winlogbeat installation directory.

    ````powershell
    cd 'C:\Program Files\winlogbeat'
    ````

5. Install the Winlogbeat service.

    ````powershell
    .\install-service-winlogbeat.ps1
    ````

6. Replace `C:\Program Files\winlogbeat\winlogbeat.yml` with the following configuration:

    ````yaml
    winlogbeat.event_logs:
      - name: Application
        ignore_older: 72h

      - name: System

      - name: Security

      - name: ForwardedEvents
        tags: [forwarded]

      - name: Windows PowerShell
        event_id: 400, 403, 600, 800

      - name: Microsoft-Windows-PowerShell/Operational
        event_id: 4103, 4104, 4105, 4106

    setup.template.settings:
      index.number_of_shards: 1

    output.elasticsearch:
      enabled: false

    output.logstash:
      hosts: ["LOGSTASH_HOST:5044"]

      # Uncomment these options when your Logstash Beats input uses TLS.
      # ssl.certificate_authorities: ["C:\\path\\to\\ca.pem"]
      # ssl.certificate: "C:\\path\\to\\client.crt"
      # ssl.key: "C:\\path\\to\\client.key"

    processors:
      - add_host_metadata:
          when.not.contains.tags: forwarded
      - add_cloud_metadata: ~

    logging.level: info
    ````

    Replace `LOGSTASH_HOST` with the hostname or IP address of your Logstash server. Keep the `:5044` port unless you configure the Logstash Beats input to use another port.

    !!! warning "Use the correct Logstash address"

        The value of `output.logstash.hosts` must resolve from the Windows server running Winlogbeat. If the Logstash server uses a different port, update the value to match the Beats input configuration.

7. Validate the configuration.

    ````powershell
    .\winlogbeat.exe test config -c .\winlogbeat.yml -e
    ````

8. Start the Winlogbeat service.

    ````powershell
    Start-Service winlogbeat
    ````

`winlogbeat setup` is not required for this configuration because events are sent to Logstash and the Elasticsearch output is disabled. Run that command only when you separately configure the Elasticsearch and Kibana assets required by Winlogbeat.

### Configure your intake

{!_shared_content/integration/intake_configuration.md!}

## Forward logs to Sekoia.io

Configure Logstash to accept Winlogbeat events and forward the complete JSON payload to Sekoia.io. Follow the [Logstash forwarding guide](/integration/ingestion_methods/logstash.md) and replace its intake key placeholder with the key from the Winlogbeat intake.

{!_shared_content/operations_center/integrations/generated/c10307ea-5dd1-45c6-85aa-2a6a900df99b_sample.md!}

## Detection section

The related built-in detection rule list is generated automatically from the fields declared by the intake format. The generated list can omit a compatible rule when the rule uses fields that the format does not declare, even when the parser produces those fields through a shortcut or post-processing step.

!!! note "Windows Security detection coverage"

    The **LSASS Access From Non System Account** rule detects access to the LSASS process from a non-system account in Windows Security events 4656 and 4663. It uses the following normalized fields:

    - `action.properties.ObjectName`
    - `action.properties.AccessMask`
    - `action.properties.SubjectUserName`

    Verify this rule in the [built-in detection rule catalog](/xdr/features/detect/rules_catalog.md). The rule should be included in the generated Winlogbeat detection list after these `action.properties.*` fields are declared in the Winlogbeat intake taxonomy.

    Review other Windows Security rules that use the same field family when checking detection coverage. Do not create a custom rule when an applicable native rule already exists in the catalog.

{!_shared_content/operations_center/integrations/generated/021e9def-5a55-4369-941e-af269b45bef1.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_c10307ea-5dd1-45c6-85aa-2a6a900df99b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/c10307ea-5dd1-45c6-85aa-2a6a900df99b.md!}

## Further readings

- [Winlogbeat overview](https://www.elastic.co/guide/en/beats/winlogbeat/current/_winlogbeat-overview.html)
- [Winlogbeat configuration reference](https://github.com/elastic/beats/blob/main/winlogbeat/winlogbeat.yml)
