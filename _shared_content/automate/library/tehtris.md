# TEHTRIS

![TEHTRIS](/assets/playbooks/library/tehtris.png){ align=right width=150 }

[TEHTRIS](https://tehtris.com) is a cybersecurity company offering products designed to protect endpoints against known and unknown threats.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `apikey` | `string` | The API key to authenticate calls to the API |
| `tenant_id` | `string` | The identifier of your tenant (most of the time, your tenant ID is a trigram in the URL of your TEHTRIS instance; e.g. `https://{tenant_id}.tehtris.net`) |
| `alternative_url` | `string` | The alternative URL to contact the TEHTRIS instance |

## Triggers

### Fetch new events from TEHTRIS

Get the latest events from the TEHTRIS XDR platform.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `filter_id` | `['integer', 'string']` | The Filter ID used to retrieve events |

!!! note
    This module uses TEHTRIS API pull mode. TEHTRIS recommends syslog push mode as the default integration mode for performance and robustness when available.


## Extra

Module **`TEHTRIS` v1.15.1**