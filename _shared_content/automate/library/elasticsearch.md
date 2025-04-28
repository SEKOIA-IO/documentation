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


## Set up

## Configuration

To create credentials for the `ElasticSearch` integration please follow next steps:

1. Log in to your Kibana console
2. Go to `Management` > `Stack Management`
   
     ![Step 1](/assets/playbooks/library/setup/elasticsearch/step01.png){: style="max-width:100%"}

3. In the Stack Management interface, go to `Security` > `API Keys`

     ![Step 2](/assets/playbooks/library/setup/elasticsearch/step02.png){: style="max-width:100%"}

4. In the `API Keys` section, click `+ Create API key`

     ![Step 3](/assets/playbooks/library/setup/elasticsearch/step03.png){: style="max-width:100%"}

5. Type a name for the API key
6. If requested by our security practices, define an expiration date for the API key. 
   
   > **_NOTE:_** Be aware that an expiration date on an API key will force you to renew the API key on a regular basis. Expired API keys will break playbooks.

7. Use the following template to define the control security privileges of the API Key
   
   ```json> 
   {
      "read-only-role": {
        "cluster": ["all"],
        "indices": [
          {
            "names": ["*"],
            "privileges": ["read"]
          }
        ]
      }
    }
   ```

8. Click `Create API key`

     ![Step 4](/assets/playbooks/library/setup/elasticsearch/step04.png){: style="max-width:100%"}

9. Use your API key token

     ![Step 5](/assets/playbooks/library/setup/elasticsearch/step05.png){: style="max-width:100%"}

## Extra

Module **`ElasticSearch` v1.0.1**
