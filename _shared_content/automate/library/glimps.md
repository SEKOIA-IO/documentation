# GLIMPS

![GLIMPS](/assets/playbooks/library/glimps.png){ align=right width=150 }

[Glimps](https://www.glimps.fr/) offers a DeepLearning solution to detect, analyze and classify malwares. It enables faster responses during incidents with a detailed understanding of the threat

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | Glimps base URL (ex. https://gmalware.ggp.glimps.re) |
| `api_key` | `string` | APIKEY for the Glimps's API |

## Actions

### Get the results of an analysis



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | Unique analysis identifier |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `done` | `boolean` | is the analysis finished |
| `duration` | `integer` | duration of the analysis in milliseconds |
| `error` | `string` | error message if Status is false |
| `errors` | `object` | error message by services |
| `file_count` | `integer` | amount of file in the submission (input + extracted) |
| `filenames` | `array` | list of analysed filename |
| `files` | `array` | array of submission files (input file and extracted sub-files) |
| `filetype` | `string` |  |
| `is_malware` | `boolean` | analysis result, is a malware or not |
| `malwares` | `array` | list of malware names found in analysis |
| `md5` | `string` | string hex encoded input file MD5 |
| `score` | `integer` | highest score given by probes |
| `sha1` | `string` | string hex encoded input file SHA1 |
| `sha256` | `string` | string hex encoded input file SHA256 |
| `sid` | `string` | analysis UUID handled by GLIMPS malware finder - expert<br/>could be used to construct expert link like:<br/>https://gmalware.useddomain.glimps.re/expert/en/analysis/results/advanced/${SID} |
| `size` | `integer` | input file size (in bytes) |
| `ssdeep` | `string` | string input file SSDeep |
| `status` | `boolean` | true => no error to report,<br/>false => an error occurred |
| `timestamp` | `integer` | timestamp of the start of analysis in milliseconds |
| `token` | `string` | token that can be used to view analysis result in expert view |
| `uuid` | `string` | Unique analysis identifier |

### Search previous analysis



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sha256` | `string` | string hex encoded input file SHA256 |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `done` | `boolean` | is the analysis finished |
| `duration` | `integer` | duration of the analysis in milliseconds |
| `error` | `string` | error message if Status is false |
| `errors` | `object` | error message by services |
| `file_count` | `integer` | amount of file in the submission (input + extracted) |
| `filenames` | `array` | list of analysed filename |
| `files` | `array` | array of submission files (input file and extracted sub-files) |
| `filetype` | `string` |  |
| `is_malware` | `boolean` | analysis result, is a malware or not |
| `malwares` | `array` | list of malware names found in analysis |
| `md5` | `string` | string hex encoded input file MD5 |
| `score` | `integer` | highest score given by probes |
| `sha1` | `string` | string hex encoded input file SHA1 |
| `sha256` | `string` | string hex encoded input file SHA256 |
| `sid` | `string` | analysis UUID handled by GLIMPS malware finder - expert<br/>could be used to construct expert link like:<br/>https://gmalware.useddomain.glimps.re/expert/en/analysis/results/advanced/${SID}<br/> |
| `size` | `integer` | input file size (in bytes) |
| `ssdeep` | `string` | string input file SSDeep |
| `status` | `boolean` | true => no error to report,<br/>false => an error occurred<br/> |
| `timestamp` | `integer` | timestamp of the start of analysis in milliseconds |
| `token` | `string` | token that can be used to view analysis result in expert view |
| `uuid` | `string` | Unique analysis identifier<br/> |

### Analyse a file



**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `bypass-cache` | `boolean` | ask the API to bypass cache and always submit the file to the orchestrator (optional) |
| `file` | `string` | The file to scan |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `error` | `string` | string describing error |
| `status` | `boolean` | false => an error occurred |
| `uuid` | `string` | Unique analysis identifier |


## Extra

Module **`GLIMPS` v1.10**