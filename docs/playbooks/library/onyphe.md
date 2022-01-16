# onyphe


![onyphe](../../assets/playbooks/library/onyphe.png)


Onyphe

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| apikey | string | APIKEY for Onyphe |








## Actions

### IP Threat List

Get threatlist information on IP with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Datascan

Get datascan information on IP with Onyphe: "Application responses to [Onyphe's] application requests"



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan. Exactly one of 'ip' or 'string' must be specified |
| string | string | The string to scan. Exactly one of 'ip' or 'string' must be specified |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Geolocalization

Geo-localize ip with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |







### MD5 Lookup

Get Onyphe datascans with the given md5 in the datamd5 field



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| md5 | string | The md5 to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### Sniffer

Get sniffer information on IP with Onyphe: "[Onyphe has] a number of distributed honeypots on the Internet. [They] are listening to Internet background noise and performing passive operating system identification"



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Lookup

Get information on IP with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### Pastries

Get pastries information collected by Onyphe on pastebin.com



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### Onion Scan

Get information on the given onion domain with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| onion | string | The onion domain to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### Domain Name CTLs

Get domain name X509 certificate information from Certificate Transparency Logs (CTLs) with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| domain | string | The domain to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Reverse DNS

Get reverse DNS lookup information on IP with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### Syn Scan

Get synscan information on IP with Onyphe: "Open TCP ports found on the Internet. Each open port is also enriched with detected operating system"



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Forward DNS

Get forward DNS lookup information on IP with Onyphe



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |







### IP Inetnum

Get inetnum information on IP with Onyphe: "IP (v4 and v6) networks description as given by RIRs (Regional Internet Registries), except for the United States which does not disclose that information publicly."



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| ip | string | The ip to scan |
| budget | integer | Maximum number of pages to retrieve |
| first_page | integer | Start retrieving data from this page |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| count | integer | Number of elements in results |
| error | integer | Error code, 0 for no error |
| message | string | Error message, only if error is not 0 |
| myip | string | IP from which the request is made |
| results | array | array of data |
| status | string | Status of the request: ok/nok |
| took | string | Time to serve the request |
| total | integer | Total number of pieces of information, only up to 10000 are returned in results |
| max_page | integer | Maximal number of pages |
| page | integer | Last page requested |












## Extra

Module **onyphe v.1.11**
