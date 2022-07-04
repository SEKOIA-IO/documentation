# VirusTotal



[VirusTotal](https://www.virustotal.com) is a cybersecurity company specialized in malware analysis.

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| apikey | string | APIKEY for VirusTotal |





## Triggers

### livehunt_notification_files

Get LiveHunt notifications from the files endpoint



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| sleep_time | integer | frequency of the lookups (in seconds) |
| skip_history | boolean | only process new notifications |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| notification_path | string | Filepath of the notification |
| ruleset_name | string | Name of the Ruleset |
| rule_name | string | Name of the Rule |
| notification_id | string | ID of the notification |
| notification_date | integer | Timestamp of the notification |
| md5 | string | MD5 hash of the file that matched the Yara rule |
| sha1 | string | SHA-1 hash of the file that matched the Yara rule |
| sha256 | string | SHA-256 hash of the file that matched the Yara rule |
| name | string | Meaningful name of the file that matched the Yara rule |













## Actions

### Get Comments

Get comments from Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| resource | string | The hash or url to get comments from |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |







### Post Comment

Post comment to Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| comment | string | The comment to post |
| resource | string | The hash or url to comment |









### Scan Domain

Scan domain with Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| domain | string | The domain to scan |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |







### Scan File

Scan file with Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file | string | The file to scan |
| detect_treshold | integer | The number of positives from VirusTotal that will be used as a treshold of detection |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |







### Scan Hash

Scan hash with Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| hash | string | The hash to check |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |







### Scan IP

Scan ip with Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |







### Scan URL

Scan url with Virus Total



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string | The url to scan |
| detect_treshold | integer | The number of positives from VirusTotal that will be used as a treshold of detection |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| report | object | VirusTotal report |












## Extra

Module **VirusTotal v.1.16**