uuid: 9c17d041-4930-4c23-a108-811a25ef6d64
name: ElasticSearch
type: playbook

# ElasticSearch

![ElasticSearch](/assets/playbooks/library/elasticsearch.png){ align=right width=150 }

Elasticsearch is a scalable, real-time search and analytics engine designed for handling large volumes of structured and unstructured data. Built on Apache Lucene, it allows users to perform complex queries quickly and analyze data in near real-time. Its distributed architecture ensures high availability and reliability, making it ideal for applications ranging from website search to log analysis and business intelligence. Elasticsearch also integrates seamlessly with the Elastic Stack, enhancing data visualization and management capabilities.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | Url of the tenant |
| `api_key` | `string` | The API Key to authenticate to ElasticSearch |
| `disable_certificate_verification` | `boolean` | Disable certificate verification for the connection. Optional |
| `sha256_tls_fingerprint` | `string` | The SHA256 TLS fingerprint of the server certificate. Optional |

## Actions

### Execute ES|QL query

Query data from ElasticSearch with ES|QL

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `drop_null_columns` | `boolean` | Determines if null columns should be dropped from the result |
| `query` | `string` | The query to be executed. |
| `timeout` | `integer` | The number of seconds to wait before timing out the query. Default is 60 seconds. Maximum is 10 minutes |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `data` | `array` | Query results |


## Extra

Module **`ElasticSearch` v1.0.1**