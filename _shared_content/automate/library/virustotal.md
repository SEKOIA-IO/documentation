# VirusTotal

![VirusTotal](/assets/playbooks/library/virustotal.svg){ align=right width=150 }

[VirusTotal](https://www.virustotal.com) is a cybersecurity company specialized in malware analysis.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `apikey` | `string` | APIKEY for VirusTotal |

## Triggers

### livehunt_notification_files

Get LiveHunt notifications from the files endpoint

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sleep_time` | `integer` | frequency of the lookups (in seconds) |
| `skip_history` | `boolean` | only process new notifications |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `notification_path` | `string` | Filepath of the notification |
| `ruleset_name` | `string` | Name of the Ruleset |
| `rule_name` | `string` | Name of the Rule |
| `notification_id` | `string` | ID of the notification |
| `notification_date` | `integer` | Timestamp of the notification |
| `md5` | `string` | MD5 hash of the file that matched the Yara rule |
| `sha1` | `string` | SHA-1 hash of the file that matched the Yara rule |
| `sha256` | `string` | SHA-256 hash of the file that matched the Yara rule |
| `name` | `string` | Meaningful name of the file that matched the Yara rule |

## Actions

### Get Comments

Get comments from Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `resource` | `string` | The hash or url to get comments from |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `resource` | `string` | Resource Identifier |
| `comments` | `array` | List of comments |

### Post Comment

Post comment to Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `comment` | `string` | The comment to post |
| `resource` | `string` | The hash or url to comment |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |

### Scan Domain

Scan domain with Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` | The domain to scan |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `undetected_referrer_samples` | `array` | List of undetected samples referring to this domain |
| `undetected_downloaded_samples` | `array` | List of undetected samples downloaded from this domain |
| `undetected_urls` | `array` | List of undetected URLs on this domain |
| `detected_referrer_samples` | `array` | List of detected samples referring to this domain |
| `detected_downloaded_samples` | `array` | List of detected samples downloaded from this domain |
| `detected_urls` | `array` | List of detected URLs on this domain |
| `resolutions` | `array` | List of IP addresses this domain resolved to |
| `subdomains` | `array` | List of subdomains |
| `domain_siblings` | `array` | List of domain siblings |
| `categories` | `array` | List of categories |

### Scan File

Scan file with Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file` | `string` | The file to scan |
| `detect_treshold` | `integer` | The number of positives from VirusTotal that will be used as a treshold of detection |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `resource` | `string` | Resource Identifier |
| `scan_id` | `string` | Scan Identifier |
| `scan_date` | `string` | Date of last scan |
| `md5` | `string` | MD5 hash of the sample |
| `sha1` | `string` | SHA-1 hash of the sample |
| `sha256` | `string` | SHA-256 hash of the sample |
| `permalink` | `string` | Permalink to the scan report |
| `positives` | `integer` | Number of antivirus detecting this sample as malicious |
| `total` | `integer` | Number of antivirus that scanned the sample |
| `scans` | `object` | Scan results (one scan result per key) |

### Scan Hash

Scan hash with Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hash` | `string` | The hash to check |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `resource` | `string` | Resource Identifier |
| `scan_id` | `string` | Scan Identifier |
| `scan_date` | `string` | Date of last scan |
| `md5` | `string` | MD5 hash of the sample |
| `sha1` | `string` | SHA-1 hash of the sample |
| `sha256` | `string` | SHA-256 hash of the sample |
| `permalink` | `string` | Permalink to the scan report |
| `positives` | `integer` | Number of antivirus detecting this sample as malicious |
| `total` | `integer` | Number of antivirus that scanned the sample |
| `scans` | `object` | Scan results (one scan result per key) |

### Scan IP

Scan ip with Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | The ip to scan |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `country` | `string` | Country hosting this IP address |
| `asn` | `string` | Autonomous System number hosting this IP address |
| `undetected_downloaded_samples` | `array` | List of undetected samples downloaded from this IP address |
| `undetected_urls` | `array` | List of undetected URLs on this IP address |
| `detected_downloaded_samples` | `array` | List of detected samples downloaded from this IP address |
| `detected_urls` | `array` | List of detected URLs on this IP address |
| `resolutions` | `array` | List of domain names that resolved to this IP address |

### Scan URL

Scan url with Virus Total

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | The url to scan |
| `detect_treshold` | `integer` | The number of positives from VirusTotal that will be used as a treshold of detection |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `response_code` | `integer` | Response Code |
| `verbose_msg` | `string` | Textual description of the response code |
| `scan_id` | `string` | Scan Identifier |
| `scan_date` | `string` | Date of last scan |
| `url` | `string` | Scanned URL |
| `permalink` | `string` | Permalink to the scan report |
| `positives` | `integer` | Number of antivirus detecting this sample as malicious |
| `total` | `integer` | Number of antivirus that scanned the sample |
| `scans` | `object` | Scan results (one scan result per key) |


## Extra

Module **`VirusTotal` v1.28.0**