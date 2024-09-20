# IPtoASN

![IPtoASN](/assets/playbooks/library/iptoasn.png){ align=right width=150 }

[IPtoASN](https://iptoasn.com/) is a free, downloadable and frequently updated ASN database. It allow associating IP addresses to ASN

## Configuration

This module accepts no configuration.

## Triggers

### Fetch Database

Download the IPtoASN database recurrently

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `chunk_size` | `integer` | Number of items to include in each chunk. Defaults to 10 000. |
| `interval` | `integer` | Interval in hours to wait between each trigger call. Defaults to 24. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | Database file path |
| `chunk_offset` | `integer` | Offset of the chunk in the full database |
| `chunk_size` | `integer` | Size of the chunk |


## Extra

Module **`IPtoASN` v1.31.0**