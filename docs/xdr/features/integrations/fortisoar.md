# FortiSOAR

## Prerequisites

To install the FortiSOAR integration, you first have to create an API Key in Sekoia.io XDR with the following permissions: 

| Name of the permission | ID | Description |
| --- | --- | --- |
| SIC_READ_ALERTS | 9ea2b8a3-593f-4bab-92f5-d0af9b563f6f | List and consult SIC alerts |
| SIC_WRITE_ALERTS_WORKFLOW | 9f3df1b1-4db7-44bd-b615-af5873ad7f8a | Triggers an action on the alert workflow |
| SIC_READ_ALERT_STATS | b1642ef8-4bc0-40b4-9ddf-7bd368659941 | Get statistics about SIC alerts |
| SIC_WRITE_ALERTS_COMMENTS | 341436f9-1c33-4cf7-bec3-a6955133ea04 | Post a comment on an alert |
| SIC_READ_INTAKES | 2f0da527-2cf1-4a00-8f4c-033bfb43ddeb | Get information about a set of intakes |
| SIC_READ_INCIDENTS | 7c0bac3f-f2ce-491b-b663-638145078516 | Get incidents |
| SIC_READ_EVENT_STATS | 74bc185a-eb82-4eac-a638-ebae41425fa0 | Get statistics about SIC events |
| ASSETMANAGEMENT_VIEW_ASSET_CATEGORY | fb8c8a83-6843-4be0-abed-7a0ab32c2b6d | Allow to list categories of assets |
| ASSETMANAGEMENT_VIEW_ATTRIBUTE_NAME | 8734c047-de38-4693-9ca4-3e9ffdccde1a | Allow to list attribute names |
| ASSETMANAGEMENT_VIEW_ASSET | 4b0f38a9-a890-4f9b-ae7a-e5025162ff33 | Allow to retrieve or list assets |
| ASSETMANAGEMENT_VIEW_ASSET_ATTRIBUTE | 9541580b-8ced-4037-a534-28666ca8fcf8 | Allow to retrieve or list attributes of an asset |
| SIC_READ_GENERATION_MODES | 25868e4c-987f-41e6-8b09-86aeb4a2a22d | Get generation modes |
| SIC_READ_ENTITIES | 0d9c0f86-fbcb-4db8-8842-f7451e4705b2 | Get information about entities |
| SIC_READ_COUNTERMEASURES | cd2fe256-8ee0-4fcf-b255-cbc237a49ab9 | Get information about a set of countermeasures |
| ASSETMANAGEMENT_VIEW_ASSET_TYPE | d53187c1-b6c4-4660-a2e7-30b598b6150e | Allow to list types of assets |


!!! tip
    You can find more details on how to create an API Key in this [section.](../../../getting_started/manage_api_keys.md)

On the FortiSOAR server, make sure you have the outbound connectivity to app.sekoia.io on the port 443 (HTTPS).

## Install

To install the FortiSOAR integration, follow these steps: 

1. In your FortiSOAR instance, go to the `Connector Store` and search for "sekoia"

2. Choose the `Sekoia.io XDR` connector and click on the `Install` button

3. Navigate to `Configurations`. Give a name to the configuration and paste the APIKEY as requested.

Please specify, if necessary, whether the SSL certificate of the server should be verified and the proxy through which the calls should be directed.

To learn how to use the integration, please read the [following documentation](https://github.com/fortinet-fortisoar/connector-sekoia-io-xdr/blob/release/1.0.0/docs/SekoiaioXDR.md) which describes most commands, their inputs and their outputs.
