# Proofpoint


![Proofpoint](/assets/playbooks/library/proofpoint.png)


Proofpoint Module

## Configuration



This module accepts no configuration.




## Triggers

### Get Proofpoint TAP events

Forward Proofpoint TAP Events



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| api_host | string | API Url of the ProofPoint TAP |
| client_principal | string | The authentication principal |
| client_secret | string | The authentication secret |
| intake_server | string | Server of the intake server (e.g. 'https://intake.sekoia.io') |
| intake_key | string | Intake key to use when sending events |
| frequency | integer | Batch frequency in seconds |
| chunk_size | integer | The max size of chunks for the batch processing |

















## Extra

Module **Proofpoint v.1.0.6**