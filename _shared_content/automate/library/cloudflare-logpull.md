# Cloudflare Logpull


![Cloudflare Logpull](/assets/playbooks/library/cloudflare-logpull.png)


Cloudflare Logpull Module

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| api_url | string | URL of the Cloudflare API |
| x_auth_email | string | Cloudflare account email |
| x_auth_key | string | Cloudflare authentication key |
| zone_id | string | Cloudflare Zone ID |





## Triggers

### Cloudflare Logpull fetch events

Get lastest events from Cloudflare Logpull



#### Arguments
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| frequency | integer | Batch frequency in seconds (Must be at least 1 minute) |






#### Outputs
| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| records_path | string | Path to the file holding the results |















## Extra

Module **Cloudflare Logpull v.1.5**