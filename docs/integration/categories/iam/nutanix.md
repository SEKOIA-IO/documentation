uuid: 9a7f6d4e-3b2a-4c1d-8f9e-0a1b2c3d4e5f
name: Nutanix - IAM mappings
type: intake

## Nutanix - IAM mappings [BETA]

!!! warning "Beta"
	This IAM mappings guide is part of a beta integration. Field names and
	recommendations may change — validate in your environment before production use.

## Overview

This short guide shows how Nutanix AUDIT logs map to IAM-related ECS fields and recommended detection focuses.

- **Vendor**: Nutanix
- **Supported environment**: On-premises (Prism Central / Prism Element)
- **Detection based on**: Audit logs (AUDIT / API_AUDIT)

## Field mappings (recommended)

- `userName` -> `user.name`
- `userUuid` -> `user.id`
- `operationType` -> `event.action`
- `creationTimestampUsecs` -> `@timestamp` (convert from microseconds)
- `entityType`, `uuid` -> `entity.type`, `host.id` or `host.name` (depending on resource)

## Detection suggestions

- Alert on administrative actions from unexpected accounts: `user.name` + `operationType` in [Create, Delete, Migrate].
- Detect mass provisioning: spike in `event.action: Create` for `entityType: vm` within short window.
- Monitor failed login or IAM admin events (logged in AUDIT) and correlate with `user.id` anomalies.

## Notes

- Ensure timestamps are normalized to ECS `@timestamp` (microseconds -> ISO8601).
- Include these mappings in the intake's parser and in the Operations Center suggested rules.

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_9a7f6d4e-3b2a-4c1d-8f9e-0a1b2c3d4e5f_do_not_edit_manually.md!}

