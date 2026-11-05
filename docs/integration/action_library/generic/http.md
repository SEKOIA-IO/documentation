---
uuid: 5894985f-91eb-46db-9306-cc5ac6463d3d
name: "HTTP"
type: playbook
description: "This module exposes actions to request HTTP resources"
---

# HTTP

<img src="../../.gitbook/assets/library/http.png" alt="HTTP" width="150" align="right">

This module exposes actions to request HTTP resources

## Configuration

This module accepts no configuration.

## Actions

### Download File

Download the given file and save it

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | URL of the file to download |
| `headers` | `object` | Headers to use when sending requests. e.g. {"authorization": "Bearer foo"} |
| `verify_ssl` | `boolean` | Whether the SSL certificate must be verified. Default to true. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | Absolute file path on disk (legacy; prefer file_relative_path for chaining with other modules). |
| `file_relative_path` | `string` | File path relative to the playbook data directory, suitable as input for other modules (for example: Scan File). |

### Request URL

Requests a resource at a specified URL and returns the response as Raw or JSON

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | Target URL of the HTTP request |
| `headers` | `object` | Headers to use when sending the requests. e.g. {"Content-Type": "application/json"} |
| `auth_type` | `string` | Type of authorization, if applicable |
| `auth_token` | `string` | Token for Bearer authentication |
| `auth_username` | `string` | Username for Basic and Digest authentications |
| `auth_password` | `string` | Password for Basic and Digest authentications |
| `method` | `string` | Method of the HTTP request |
| `data` | `string` | The body to attach to the request |
| `json` | `object` | The JSON to attach as the request body |
| `params` | `` | Query string parameters to append to the URL |
| `fail_on_http_error` | `boolean` | Fail when the HTTP query returns in error. Default to true. |
| `verify_ssl` | `boolean` | Whether the SSL certificate must be verified. Default to true. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `reason` | `string` | Textual reason phrase of the HTTP status (for example: Not Found, OK). |
| `status_code` | `integer` | Numeric HTTP status code returned by the server. |
| `url` | `string` | Final URL of the requested resource. |
| `headers` | `object` | Response headers returned by the server. |
| `encoding` | `string` | Character encoding detected for the response body. |
| `elapsed` | `number` | Elapsed time in seconds between sending the request and receiving the response. |
| `text` | `string` | Response body as text. |
| `json` | `['object', 'array', 'string', 'number', 'boolean', 'null']` | Response body parsed as JSON when available; can be an object, array, scalar, or null. |


## Extra

Module **`HTTP` v1.122.0**