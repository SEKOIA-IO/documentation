uuid: 3ba4b84b-c323-48ef-93d2-6f3544c783d6
name: GLIMPS
type: playbook

# GLIMPS

![GLIMPS](/assets/playbooks/library/glimps.png){ align=right width=150 }

[Glimps](https://www.glimps.fr/) offers a DeepLearning solution to detect, analyze and classify malwares. It enables faster responses during incidents with a detailed understanding of the threat

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | Glimps detect token |
| `base_url` | `string` | Glimps detect url |

## Actions

### [TEST] Analyse a file

Submit file to Glimps Detect to be analysed

**Configuration**

{'title': 'Description', 'description': 'Description added to the analysis', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_name` | `string` | Name of submitted file |
| `bypass_cache` | `boolean` | If true, file is analyzed, even if a result already exists |
| `user_tags` | `array` | Analysis will be tagged with those tags |
| `description` | `string` | Description added to the analysis |
| `archive_pwd` | `string` | Password used to extract archive |
| `push_timeout` | `number` | Maximum time (in seconds) to wait for a response when submitting file |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `boolean` | False means that an error occured |
| `uuid` | `string` | UUID of the submitted analysis |

### [TEST] Analyse a file and wait for result

Submit file to Glimps Detect to be analysed and wait for its results

**Configuration**

{'title': 'Description', 'description': 'Description added to the analysis', 'type': 'string'}

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_name` | `string` | Name of submitted file |
| `bypass_cache` | `boolean` | If true, file is analyzed, even if a result already exists |
| `user_tags` | `array` | Analysis will be tagged with those tags |
| `description` | `string` | Description added to the analysis |
| `archive_pwd` | `string` | Password used to extract archive |
| `push_timeout` | `number` | Maximum time (in seconds) to wait for a response when submitting file |
| `pull_time` | `number` | Time to wait (in seconds) between each requests to get a result |
| `timeout` | `number` | Maximum time (in seconds) to wait for the analysis to end |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `analysis` | `` | Analysis response details |
| `view_url` | `string` | Analysis URL |

### [TEST] Export analysis result

Export analysis result with the requested layout and format

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | Unique analysis identifier |
| `format` | `string` | Export format |
| `layout` | `string` | Export layout |
| `is_full` | `string` | Export full analysis or summarized |

### [TEST] Get profile status

Get Glimps detect profile status, it includes quotas, eastimated analysis duration and cache

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `daily_quota` | `integer` | Number of submissions authorized for the profile within 24h |
| `available_daily_quota` | `integer` | Number of submissions still available within 24h. It's a sliding window, so a new slot will be released 24h after each submission |
| `cache` | `boolean` | If True, the profile is configured to use cached result by default |
| `estimated_analysis_duration` | `integer` | Estimation of the duration for the next submissions in milliseconds. It's based on the average time of submissions and the submission queue state. The real duration could differ from the estimation |

### [TEST] Retrieve analysis

Retrieve the analysis matching the given uuid

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `string` | UUID of the analysis |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `analysis` | `` | Analysis response details |
| `view_url` | `string` | Analysis URL |

### [Deprecated] Get the results of an analysis



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

### [Deprecated] Search previous analysis



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

### Search analysis

Search an analysis for a given sha256 input file

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sha256` | `string` | SHA256 of file to search |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `analysis` | `` | Analysis response details |
| `view_url` | `string` | Analysis URL |

### [Deprecated] Analyse a file



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

Module **`GLIMPS` v1.14.2**