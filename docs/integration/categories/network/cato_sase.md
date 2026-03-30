# cato\_sase

uuid: 469bd3ae-61c9-4c39-9703-7452882e70da name: Cato SASE type: intake

### Overview

Cato Networks is a software company providing solutions to protect cloud applications. Cato SASE Cloud provides zero trust network access to on-premises and cloud applications.

* **Vendor**: Cato Networks
* **Supported environment**: Cloud
* **Detection based on**: Telemetry / Alert
* **Supported application or feature**: Application, Web, Authentication

### Configure

This setup guide will show you how to provide an integration between Cato SASE events and Sekoia.io.

#### Enable the EventsFeed API

1. Log in to your Cato Management Application
2. Click on the `Administration` section then click on `API & Integrations` {: style="max-width:100%"}
3. Select the tab `Events Integration`
4. Click on `Enable integration with Cato events` {: style="max-width:100%"}

#### Generate the API key

To collect the events from the Cato Networks platform, an API key is required:

1. Click on the `Administration` section then click on `API & Integrations`
2. Click on the button `New` to generate a new API key
3. On the panel, give a name to the api key, select the `View` permission {: style="max-width:100%"}
4. Click on apply and copy the API key

In addition to the API key, Cato `account ID` is also required for the Account configuration in Sekoia

!!! Note In the Cato Management Application, please note the four or five digits in the browser address.

#### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Cato SASE.
2. Set up the intake account configuration with the Api Key and Account Id.

{!\_shared\_content/operations\_center/integrations/generated/469bd3ae-61c9-4c39-9703-7452882e70da\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_469bd3ae-61c9-4c39-9703-7452882e70da\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/469bd3ae-61c9-4c39-9703-7452882e70da.md!}

### Further readings

* [Cato Networks - Generating API Keys for the Cato API](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API)
