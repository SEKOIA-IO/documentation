uuid: 919705ab-7a64-493e-a92b-4049fafea325
name: Triage
type: playbook

# Triage

![Triage](/assets/playbooks/library/triage.svg){ align=right width=150 }

Triage is a malware analysis sandbox as a service, brought by Hatching

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | API key |
| `api_url` | `string` | API endpoint (url) |

## Triggers

### Triage config

Get Triage configs

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Frequency at which the script collects IOCs |
| `malware_list` | `array` | List of malware family |
| `exclude_signed` | `boolean` | Do not retrieve report with signed binary |
| `exclude_suspicious_analysis` | `boolean` | Do not retrieve report with only one behavioral or with a score gap between two dynamic analysis |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | Triage raw results file path |

## Actions

### Triage to observables

Triage raw results to observables

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `triage_raw_results` | `array` | List of objects that contain Triage raw results |
| `triage_raw_results_path` | `string` | Path of objects that contain Triage raw results |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `observables` | `array` | Bundle with the list of observables |
| `observables_path` | `string` | Path of the file holding the bundle with the observables |


## Extra

Module **`Triage` v1.43.0**