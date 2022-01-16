# iknowwhatyoudownload


![iknowwhatyoudownload](../../assets/playbooks/library/iknowwhatyoudownload.png)


Torrent downloads and distributions tracker

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| host | string | IknowWhatYouDownload host for API queries |
| key | string | APIKEY for the IKnowWhatYouDownload Service |








## Actions

### IP History

Fetches the historical data of downloaded and shared content using the BitTorrent protocol of an IP



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The IP address to query |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | ip address |
| isp | string | Interner Service Provider if known |
| hasPorno | boolean | if any content has category XXX |
| hasChildPorno | boolean | if any content has category 'ChildPorno' |
| geoData | object | geo data for ip if known |
| contents | array | list of found contents |







### IP Check

Fast check if IP exists or not in the IKnowWhatYouDownload database



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The IP address to query |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | ip address |
| exists | boolean | does IKnowWhatYouDownload have history for this ip or not |
| date | string | last seen date in UTC, optional |







### IP List

Fetch the list IP that can be found in a CIDR notation



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| cidr | string | The CIDR address to query |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| CIDR | string | the requested CIDR address |
| peers | array | array of peers |












## Extra

Module **iknowwhatyoudownload v.1.12**
