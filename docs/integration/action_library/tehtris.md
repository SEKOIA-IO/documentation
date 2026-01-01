# TEHTRIS

![TEHTRIS](/assets/playbooks/library/tehtris.png){ align=right width=150 }

[TEHTRIS](https://tehtris.com) is a cybersecurity company offering products designed to protect endpoints against knwon and unknown threats

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `apikey` | `string` | The APIkey to authenticate call to the API |
| `tenant_id` | `string` | The identifier of your tenant (most of the time, your tenant id is a trigram in the url of your TETHRIS instance; eg: https://{tenant_id}.tehtris.net) |
| `alternative_url` | `string` | The alternative url to contact the TEHTRIS instance |

## Triggers

### Fetch new events from TEHTRIS

Get last events from the TEHTRIS XDR platform

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `frequency` | `integer` | Batch frequency in seconds |
| `chunk_size` | `integer` | The size of chunks for the batch processing |
| `intake_server` | `string` | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| `intake_key` | `string` | Intake key to use when sending events |
| `filter_id` | `['integer', 'string']` | The Filter ID used to retrieve events |


## Extra

Module **`TEHTRIS` v1.15.1**