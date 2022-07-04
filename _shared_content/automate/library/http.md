# HTTP



This module exposes actions to request HTTP resources

## Configuration



This module accepts no configuration.







## Actions

### Download File

Donwload the given file and save it



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string | Url of the file to download |
| headers | object | Headers to use when sending the requests |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| file_path | string | File path on disk |







### Request URL

Requests a resource at a specified URL and returns the response as Raw or JSON



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| url | string | Target URL of the HTTP request |
| headers | object | Headers to use when sending the requests |
| method | string | Method of the HTTP request |
| data | string | The body to attach to the request |
| json | object | The JSON to attach as body of the request |
| params | string | Query string parameters to append to the URL |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| reason | string | Textual reason of responded HTTP Status, e.g. 'Not Found' or 'OK'. |
| status_code | integer | Integer code of responded HTTP Status |
| url | string | Final URL of the triggered resource |
| headers | object | Headers used by the server in the response |
| encoding | string | Encoding of the response |
| elapsed | number | The amount of seconds elapsed between sending the request and the arrival of the response |
| text | string | Content of the response in unicode |
| json | object | JSON-encoded value of the response |












## Extra

Module **HTTP v.1.101**