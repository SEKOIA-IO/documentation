 # 1. Overview
 
Vade for M365 offers AI-based protection against dynamic, email-borne cyberattacks targeting Microsoft 365.  
API-based, Vade for M365 offers a native Microsoft 365 user experience and catches 10x more advanced threats than Microsoft.  

In this documenation we will explain how to collect and send Vade for M365 logs to SEKOIA.IO.

# 2. Configure

First you need to reach the `Playbooks` page in order to initiate your playbook using the dedicated button.  

You can directly choose the `Get M365 Email Events` trigger if you are creating a playbook from scratch otherwise you will have to find it
within the `Actions library` panel under the `Vade secure` menu to drag and drop the trigger on the graph.  

To start configuring the selected trigger, you'll need to bring Vade's documentation which can be found [here](https://m365.eu.vadesecure.com/docs/).
This documentation will allow you to enter module information such as `api_host`, `client_id`, `client_secret` and `oauth2_authorization_url`.  

Then you just have to configure the trigger itself by filling its `name`, `frequency` in seconds and the `tenant_id`, the identifier of your 365 tenant.  

Lastly, you must add the Sekoia's action `Push Events to intake` to the graph and configure it using :
- the `api_key` generated within the user center
- the `base_url`
- the `events` to push on Intake (your logs) 
- the `intake_key` of the intake you have previously created (documentation can be found [here](https://docs.sekoia.io/operation_center/intakes/))
