---
uuid: 4b84d5b6-dee1-460a-8595-e9cfaeebf045
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

Use the [Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) to collect syslog events from multiple sources and forward them to their corresponding Sekoia intakes. The forwarder maps each listening port to an intake key, so each source normally requires a dedicated port.

!!! warning "Use the supported forwarder"

    The Sekoia.io Forwarder is the officially supported method for collecting syslog events with Sekoia. Other syslog services are documented for reference purposes and are not officially supported.

{!_shared_content/operations_center/integrations/generated/4b84d5b6-dee1-460a-8595-e9cfaeebf045_sample.md!}

{!_shared_content/operations_center/integrations/generated/nutanix_sample.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_4b84d5b6-dee1-460a-8595-e9cfaeebf045_do_not_edit_manually.md!}

{!_shared_content/integration/detection_section.md!}


