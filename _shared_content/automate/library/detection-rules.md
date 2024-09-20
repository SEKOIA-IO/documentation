# Detection Rules

![Detection Rules](/assets/playbooks/library/detection-rules.svg){ align=right width=150 }

This module exposes a trigger to detect new snort rules on a repository

## Configuration

This module accepts no configuration.

## Triggers

### New Snort Rules

Trigger playbooks when new snort rules are detected of a repository

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `archives` | `array` | Snort rules archives |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bundle_path` | `string` | Resulting STIX Bundle (in a file) |


## Extra

Module **`Detection Rules` v1.25.0**