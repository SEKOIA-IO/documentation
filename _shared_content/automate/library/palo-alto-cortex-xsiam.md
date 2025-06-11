uuid: 537e1880-5b6c-4b46-ae6c-f228cfc6c6e4
name: Palo Alto Cortex XSIAM
type: playbook

# Palo Alto Cortex XSIAM

![Palo Alto Cortex XSIAM](/assets/playbooks/library/palo-alto-cortex-xsiam.png){ align=right width=150 }

Palo Alto Cortex XSIAM is Palo Alto Networks’ security analytics platform that unifies SIEM, XDR, threat intelligence and SOAR for real-time detection and response.

## Configuration

This module accepts no configuration.

## Actions

### STIX to XSIAM

Convert STIX objects to XSIAM objects

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `stix_objects` | `array` | STIX objects |
| `stix_objects_path` | `string` | STIX objects file path |
| `reliability_mapping` | `array` | Overriding reliability mapping for XSIAM objects |
| `severity_mapping` | `array` | Overriding severity mapping for XSIAM objects |
| `comment` | `string` | Comment to add to the XSIAM objects |
| `class_override` | `string` | Override the class of the XSIAM objects |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `array` | XSIAM objects list |


## Extra

Module **`Palo Alto Cortex XSIAM` v1.0.0**