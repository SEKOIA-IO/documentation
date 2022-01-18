# fortigate_fw



Fortigate FW module

## Configuration



| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| firewalls | array |  |








## Actions

### Post Fortigate Address Group

Add a Fortigate Address Group



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| name | string | The name of the Address Group. |
| member | array | The Object LIST to be added in the Address Group (can be an IP address, a FQDN or event a Group), for example Address1 |









### Post Fortigate IP Address

Add a Fortigate IP Address object



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| name | string | The name of the Address. |
| ip | string | The IPv4 linked with the Address to be blocked, (for ex: '1.1.1.1'). |
| associated-interface | string | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| comment | string | A commentary to be displayed in the Fortigate GUI (default none). |









### Post Fortigate FQDN Address

Add a Fortigate FQDN object



#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| name | string | The name of the Address. |
| fqdn | string | The FQDN to be blocked (for ex: 'example.domaine.com'). |
| associated-interface | string | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| comment | string | A commentary to be displayed in the Fortigate GUI (default none). |














## Extra

Module **fortigate_fw v.1.14**
