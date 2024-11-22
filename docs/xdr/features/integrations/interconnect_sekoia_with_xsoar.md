# Palo Alto Cortex XSOAR

This integration serves as an extension that leverages the **SEKOIA.IO Defend (XDR) API**, enabling requests from the **Cortex XSOAR** interface. It facilitates seamless interaction between **SEKOIA.IO** and **Cortex XSOAR**, allowing for efficient command execution and alert retrieval.

## Prerequisites

- Sekoia.io XDR licence
- Cotex XSOAR licence
- API Key with a role that contains at least the following permissions:
	* `Alerts`
	* `Assets`
	* `Cases`
	* `View users`
    * `Dashboards`
    * `IoC Collections`

!!! Note
    To create your API Key, follow this [documentation](/getting_started/manage_api_keys.md#create-an-api-key).

## Configure

This section of the documentation will guide you through the steps required to configure the SEKOIA.IO DEFEND (XDR) extension.

1. In your Palo Alto Cortex XSOAR instance, navigate to the Marketplace and search for **SekoiaXDR**.
![!View of Sekoia.io XDR extension in the marketplace](/assets/operation_center/external_integrations/sekoia_extension_marketplace.png)
2. Select the **SEKOIAXDR** pack to open its description, then click the Install button to add the pack to your instance.
![!View of Sekoia.io XDR extension install button](/assets/operation_center/external_integrations/sekoia_installation.png)
3. Once installed, go to Settings. You should see **SEKOIAXDR** listed. Click the Add instance button to create a new instance.
![!View of Sekoia.io XDR instance in XSOAR UI](/assets/operation_center/external_integrations/sekoia_pack_instance.png)
4. Complete the required fields in the configuration form, including the API key, and then save your configuration.
![!View of Sekoia.io XDR configuration part](/assets/operation_center/external_integrations/xsoar_config_part.png)
5. Use the Test button to validate your configuration (a successful test result should display in green).
![!View of Sekoia.io XDR test button](/assets/operation_center/external_integrations/xsoar_test_button.png)

You can now utilize the integration. For example, you can run a command like `!sekoia-xdr-list-assets limit=5 assets_type="computer"`.
