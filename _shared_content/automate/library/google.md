# Google



Google module

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| credentials | object | Credentials to use. You can find them in the credentials file |





## Triggers

### Connect to the specified project subscription

Connect to the Google Cloud Pub/Sub topic and return events



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| intake_key | string | Intake key to use when sending events |
| frequency | integer | Batch frequency in seconds |
| intake_server | string | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| project_id | string | Project ID |
| subject_id | string | Subscription ID |
| chunk_size | integer | The size of chunks for the batch processing |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| messages_path | string | Path to the file holding the results |













## Actions

### Run a query against a BigQuery table

Execute the given query and return the results



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| query | string | Query to run |
| parameters | array | Parameters to use inside the query |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| items_path | string | Path to the file holding the results |












## Extra

Module **Google v.1.4.6**