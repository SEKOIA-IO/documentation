---
uuid: 9a7f6d4e-3b2a-4c1d-8f9e-0a1b2c3d4e5f
name: Nutanix
type: intake
---

## Nutanix (Prism) [BETA]

!!! warning "Beta"
	This integration is currently in beta. Features, field names and suggested rules may change.
	Validate parsing and detection rules before deploying to production.

This page explains how to collect Nutanix logs (Prism Central / Prism Element) and forward them to Sekoia.io using Syslog (recommended), API, or object storage exports.

### Overview

- Product: Nutanix Prism (Prism Central / Prism Element)
- Use cases: administrative audits, infrastructure events, Security Policy Hit Logs, and Flow service logs for troubleshooting.

## Overview

- **Vendor**: Nutanix
- **Supported environment**: On-premises (Prism Central / Prism Element)
- **Detection based on**: Audit logs, policy hit logs, and service telemetry

Nutanix Prism provides system and audit logs that are useful for security monitoring (administrative actions, infrastructure changes, and network policy hits).

## Specification

### Prerequisites

- Administrative access to Prism Central (or Prism Element for local configurations)
- Network connectivity from Prism to your log concentrator or Sekoia.io forwarder
- Intake key on Sekoia.io for the target intake

### Transport Protocol/Method

- Syslog (UDP/TCP)
- RELP (optional) for improved reliability
- TLS (between sources and concentrator) when configured in `intakes.yaml`
- API exports and object storage (S3) exports for offline/batch ingestion

### Logs details

- Supported formats: JSON payloads (API_AUDIT / AUDIT), and RFC5424 syslog lines for hit logs and service messages.
- Supported verbosity: INFO for audits (recommended), DEBUG only when troubleshooting.

## Step-by-Step Configuration Procedure

### Configure Prism Central (UI)

1. Log in to Prism Central as an administrator.
2. Navigate to Admin Center → Settings → Syslog Server.
3. Click Add Syslog Server and provide server name, IP, port, transport (UDP/TCP) and optional RELP.
4. On Data Sources, select `API_AUDIT`, `AUDIT`, `Security Policy Hit Logs` and set severity to `INFO` for audits.
5. Save and verify propagation to Prism Elements if desired.

### Configure via nCLI (illustrative)

```
# Example (verify exact syntax for your version)
ncli cluster add-remote-syslog-server server-name="sekoia" server-ip="10.0.0.10" server-port=514 transport=udp
ncli cluster update-remote-syslog-server server-name="sekoia" modules=API_AUDIT,AUDIT,SECURITY_POLICY_HIT_LOGS severity=INFO
```

### Create the intake

Go to the intake page and create a new intake using the Nutanix format on Sekoia.io: https://app.sekoia.io/operations/intakes

### Configure a forwarder

To forward events using syslog to Sekoia.io, you need to update the syslog header with the intake key you previously created.
Here is an example of your message before the forwarder
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG RAW_MESSAGE
```
and after
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key="YOUR_INTAKE_KEY"] RAW_MESSAGE
```

To achieve this you can:

- Use the [Sekoia.io forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) which is the official supported way to collect data using the syslog protocol in Sekoia.io. In charge of centralizing data coming from many equipments/sources and forwarding them to Sekoia.io with the apporpriated format, it is a prepackaged option. You only have to provide your intake key as parameter.
- Use your own [Syslog service](/integration/ingestion_methods/syslog/syslog_service.md) instance. Maybe you already have an intance of one of these components on your side and want to reuse it in order to centralize data before forwarding them to Sekoia.io. When using this mode, you have to configure and maintain your component in order to respect the expected Sekoia.io format.


!!! warning
	Only the Sekoia.io forwarder is officially supported. Other options are documented for reference purposes but do not have official support.

{!_shared_content/operations_center/integrations/generated/nutanix_sample.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9a7f6d4e-3b2a-4c1d-8f9e-0a1b2c3d4e5f_do_not_edit_manually.md!}

## Logs Details and Parsing Guidance

- Parse JSON payloads from `API_AUDIT` and `AUDIT` into structured fields.
- Convert microseconds timestamps (e.g., `creationTimestampUsecs`) to `@timestamp` ISO8601.
- Map fields into ECS (see mappings below).

### ECS mapping recommendations

- `userName` -> `user.name`
- `userUuid` -> `user.id`
- `operationType` -> `event.action`
- `entityType` -> `resource.type` or `host.type`
- `uuid` -> `resource.id` or `host.id`
- `SRC` / `DST` -> `source.ip` / `destination.ip`

## Detection

{!_shared_content/integration/detection_section.md!}

This section contains suggested detection rules and mappings that can be used in the Operations Center. The canonical, machine-generated rules are available via the Operations Center generated files included below.

### Suggested rule summaries

- **Mass provisioning detection** — counts `event.action: Create` over a short timeframe and alerts on spikes (grouped by `user.name` or globally).
- **Unusual admin activity** — flags administrative actions from unknown IPs or outside business hours; combine `user.name`, `source.ip` and `@timestamp`.
- **Policy hit drop spike** — alerts when the rate of `network.action: Drop` for a given policy exceeds a threshold.
- **Suspicious VM migration** — detects rapid or unusual `Migrate` actions, especially from non-maintenance users.

### How to use

- Import the generated suggested rules located in `_shared_content/operations_center/detection/generated/suggested_rules_9a7f6d4e-3b2a-4c1d-8f9e-0a1b2c3d4e5f_do_not_edit_manually.md` into your Operations Center.
- Tune thresholds and allowlists (known admin networks, maintenance accounts) according to your environment.
- Ensure ECS mappings are applied during parsing so the rules operate on normalized fields.


## Event samples

Example API_AUDIT message (JSON):

```
{"entityType":"vm","name":"web-01","uuid":"e4f1c7d2-1234-5678-9abc-def012345678","alertUid":"VmCreateAudit","operationType":"Create","userName":"admin@example.com","userUuid":"u-9a8b7c6d","creationTimestampUsecs":1682890496000000}
```

Example Security Policy Hit Log (syslog):

```
<14>1 2026-05-01T12:35:10Z prism.example.com NUTANIX POLICY_HIT - timestamp=2026-05-01T12:35:09Z policy_uuid=abcd-1234 policy_name=default session=Create SRC=10.0.0.5 DST=10.0.0.10 PROTO=6 ACTION=Allow packets=10 bytes=1250
```

## Further Readings

- Integration Roadmap
- Integrations Changelog
- Intake Catalog GitHub repository: https://github.com/sekoia-io/intake-catalog
- Nutanix documentation: https://portal.nutanix.com/
- Sekoia.io Forwarder documentation (see forwarder assets and README)
- Verify incoming packets on the concentrator or rsyslog host using `tcpdump` and the concentrator logs.

