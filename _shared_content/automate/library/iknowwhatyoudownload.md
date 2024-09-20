# IKnowWhatYouDownload

![IKnowWhatYouDownload](/assets/playbooks/library/iknowwhatyoudownload.png){ align=right width=150 }

[iknowwhatyoudownload](https://iknowwhatyoudownload.com) collects torrent files and peers from torrent sites and DHT network. It allows associating IP addresses to downloaded and shared data

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `host` | `string` | IknowWhatYouDownload host for API queries |
| `key` | `string` | APIKEY for the IKnowWhatYouDownload Service |

## Actions

### Check IP existence

Fast check if IP exists or not in the IKnowWhatYouDownload database

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | The IP address to query |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | ip address |
| `exists` | `boolean` | does IKnowWhatYouDownload have history for this ip or not |
| `date` | `string` | last seen date in UTC, optional |

### Get IP History

Fetches the historical data of downloaded and shared content using the BitTorrent protocol of an IP

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | The IP address to query |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | ip address |
| `isp` | `string` | Interner Service Provider if known |
| `hasPorno` | `boolean` | if any content has category XXX |
| `hasChildPorno` | `boolean` | if any content has category 'ChildPorno' |
| `geoData` | `object` | geo data for ip if known |
| `contents` | `array` | list of found contents |

### List IPs from CIDR

Fetch the list IP that can be found in a CIDR notation

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `cidr` | `string` | The CIDR address to query |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `CIDR` | `string` | the requested CIDR address |
| `peers` | `array` | array of peers |


## Extra

Module **`IKnowWhatYouDownload` v1.24.0**