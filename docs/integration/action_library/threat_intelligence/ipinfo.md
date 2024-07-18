# IPInfo

![IPInfo](/assets/playbooks/library/ipinfo.png){ align=right width=150 }

[IPINFO.IO](https://ipinfo.io//) is a database that gives access to daily updates for IP to country and IP to ASN

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | ipinfo.io token |

## Triggers

### Fetch ipinfo.io database

Upload the ipinfo.io database regularly in json format

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `interval` | `integer` | Interval in hours to wait between each trigger call. Defaults to 24. |
| `chunk_size` | `integer` | Number of items to include in each chunk. Defaults to 10 000. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path of the generated observables |
| `chunk_offset` | `integer` | Offset of the chunk in the full database |
| `chunk_size` | `integer` | Size of the chunk |


## Extra

Module **`IPInfo` v1.0**