# iptoasn



IPtoASN Module

## Configuration



This module accepts no configuration.




## Triggers

### Fetch Database

Fetches IPtoASN database



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| chunk_size | integer | Number of items to include in each chunk. Defaults to 10 000. |
| interval | integer | Interval in hours to wait between each trigger call. Defaults to 24. |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file_path | string | Database file path |
| chunk_offset | integer | Offset of the chunk in the full database |
| chunk_size | integer | Size of the chunk |















## Extra

Module **iptoasn v.1.14**
