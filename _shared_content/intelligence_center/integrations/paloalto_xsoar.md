# Palo Alto Cortex XSOAR


## Prerequisite

On Sekoia.io XDR, create an API KEY with the following permission:
- `INTHREAT_READ_OBJECTS` (`8d9901dc-0508-4472-b3c1-5ad5efc96032`): Read objects from InThreat

[More information on API KEY creation](../../../getting_started/manage_api_keys.md)

## Install

In your Palo Alto Cortex XSAOR instance go to "Marketplace" and search for "sekoia".

![!View of Sekoia.io CTI integration in PaloAlto Marketplace](paloalto_xsoar_images/marketplace.png)

Choose the "SEKOIAIntelligenceCenter" pack to open pack description and use the "Install" button to add the pack to your instance.

![!Installation of Sekoia.io CTI integration](paloalto_xsoar_images/installation.png)

![!Installed Sekoia.io CTI integration](paloalto_xsoar_images/installed.png)

Navigate to "Settings" where "SEKOIAIntelligenceCenter" should have appeared and clic the "Add instance" button to add a new instance.

![!Add a new instance of the integratino](paloalto_xsoar_images/add_instance.png)

Input a Sekoia.io XDR API KEY and save your configuration.

![!Configure instance API KEY](paloalto_xsoar_images/configure_apikey.png)

Use the test button to validate your configuration (your result should be green).

Example of failed test.

![!Test configuration, example of failed test](paloalto_xsoar_images/test_failed.png)

Example of successful test.

![!Test configuration, example of sucessfull test](paloalto_xsoar_images/test_ok.png)

You can now use the integration by typing for example `!GetObservable value="eicar@sekoia.io" type="email-addr"`.

![!Example of usage](paloalto_xsoar_images/usage.png)

To learn how to use the integration, please read the [following documentation](https://xsoar.pan.dev/docs/reference/integrations/sekoia-intelligence-center#commands) which describe every command input and output.
