# BinaryEdge's API


![BinaryEdge's API](../../assets/playbooks/library/binaryedge-s-api.png)


[BinaryEdge](https://www.binaryedge.io/) is Cybersecurity/Data Science company that focuses its effort on acquiring, analyzing and classifying internet wide data. We have developed a platform - [40fy](https://app.binaryedge.io/) that allows us and our customers to gather several data points from exposed servers online.

 The API provides access to that scanning platform, for your own usage, along with access to our curated databases so that you can do querying and analytics on our worldwide (constantly updated) collected data.

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| api_key | string | Binary Edge's API key |
| base_url | string | Binary Edge's base URL (ex. https://api.binaryedge.io/v2/) |








## Actions

### get_query_domains_search

List of Domains/DNS data based on a Query. Can be used with specific parameters and/or full-text search. Possible types of records currently available:

 -A, AAAA, NS, MX, CNAME, TXT



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_sensors_tag__tag_

Get a list of IPs that have been associated with a specific TAG.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| tag | string |  |
| days | integer |  |









### get_query_search_stats

Statistics of recent events for the given query. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| type | string |  |
| order | string |  |









### get_query_domains_ip__target_

Return records that have the specified IP address in their A or AAAA records.

 **Nota**: Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_image_tags

Get the list of possible tags for the images.








### get_query_domains_subdomain__target_

Return list of subdomains known from the target domains.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_sensors_search

Events based on a Query. List of recent events for the given query, including details of scanned ports, payloads and tags. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| days | integer |  |
| page | integer |  |
| only_ips | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_ip_historical__target_

Details about an Host, with data up to 6 months.

 List of events for the specified host, with events for each time that:
 - A port was detected open
 - A service was found running
 - Other modules were successfully executed



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| query | string |  |
| events | array |  |







### get_query_sensors_ip__target_

Details about an Scanner. List of recent events form the specified host, including details of scanned ports, payloads and tags.

 **Note**: Querying CIDRs is available for paid subscriptions only. When using CIDR, the number of credits that will be spent correspond to the number of targets that returned results. Example: a request for a /24 (256 targets) in which only 200 targets have results, will decrement 200 credits.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| total | integer |  |
| targets_found | integer |  |
| events | array |  |







### get_query_torrent_search

Events based on a Query. List of recent events for the given query, including details of the peer and torrent. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_score_ip__target_

IP Risk Score. Scoring is based on all information found on our databases regarding an IP and refers to the level of exposure of a target, i.e, the higher the score, the greater the risk of exposure.

 More details about scoring can be found on [here](https://github.com/binaryedge/ratemyip-openframework/blob/master/ip-score.md).

 **Note**: Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| normalized_ip_score | float |  |
| normalized_ip_score_detailed | object |  |
| ip_score_detailed | object |  |
| results_detailed | object |  |
| ip_address | string |  |







### get_query_domains_dns__target_

Return list of known DNS results for the target domain. Possible types of records currently available:

 -A, AAAA, NS, MX



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| pagesize | integer |  |
| total | integer |  |
| events | array |  |







### get_query_dataleaks_info

Get all available information about the dataleaks our platform keeps track.





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| sktorrent | object |  |
| samsclub | object |  |
| yandex | object |  |







### get_user_subscription

Return details about your current subscription package.





#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| subscription | object |  |
| end_date | string |  |
| requests_left | integer |  |
| requests_plan | integer |  |







### get_query_torrent_historical__target_

Details about torrents transferred by an Host, with data up to 6 months.

  List of torrent events for the specified host, with events for each time that a new transfer was detected on the DHT. See [Torrent Data](https://docs.binaryedge.io/torrent/) for more details.

 **Note:** Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| total | integer |  |
| events | array |  |







### get_query_dataleaks_email__email_

Allows you to search across multiple data breaches to see if any of your email addresses has been compromised. If you are affected, we recommend you change your password on the respective services.

 Verify how many dataleaks affected an specific email address.

 **Note:** Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| email | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| events | array |  |
| query | string |  |







### get_query_torrent_search_stats

Statistics of events for the given query. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| type | string |  |
| days | integer |  |
| order | string |  |









### get_query_cve_ip__target_

Get list of CVEs that migh affect a specific IP.

 **Note**: Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| events | object |  |







### get_query_dataleaks_organization__domain_

Verify how many emails are affected by dataleaks for a specific domain. We don't provide the list of affected emails.

 **Note:** Available for paid subscriptions only.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| domain | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| groups | array |  |
| query | string |  |







### get_query_image_ip__target_

Details about Remote Desktops found on an Host. List of screenshots and details extracted from them for the specified host, including OCR and whether faces were found or not, with data up to 2 months.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| pagesize | integer |  |
| query | string |  |
| total | integer |  |
| page | integer |  |
| events | array |  |







### get_query_search

Events based on a Query. List of recent events for the given query, including details of exposed ports and services. Can be used with [specific parameters](https://docs.binaryedge.io/image-search/) and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |
| only_ips | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| total | integer |  |
| page | integer |  |
| pagesize | integer |  |
| events | array |  |







### get_query_torrent_ip__target_

Details about torrents transferred by an Host. List of recent torrent events for the specified host, including details of the peer and torrent. See [Torrent Data](https://docs.binaryedge.io/torrent/) for more details.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| total | integer |  |
| events | array |  |







### get_query_sensors_search_stats

Statistics of recent events for the given query. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| type | string |  |
| days | integer |  |
| order | string |  |









### get_query_image_search

Remote Desktops based on a Query. List of screenshots and details extracted from them for the given query, including OCR and whether faces were found or not. Can be used with specific parameters and/or full-text search.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string |  |
| page | integer |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| pagesize | integer |  |
| query | string |  |
| total | integer |  |
| page | integer |  |
| events | array |  |







### get_query_ip__target_

Details about an Host. List of recent events for the specified host, including details of exposed ports and services.

 **Note**: Querying CIDRs is available for paid subscriptions only. When using CIDR, the number of credits that will be spent correspond to the number of targets that returned results. Example: a request for a /24 (256 targets) in which only 200 targets have results, will decrement 200 credits.



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| target | string |  |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| total | integer |  |
| query | string |  |
| events | array |  |












## Extra

Module **BinaryEdge's API v.1.9**
