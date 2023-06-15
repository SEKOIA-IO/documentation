uuid: 2b13307b-7439-4973-900a-2b58303cac90
name: Salesforce
type: intake

## Overview

Salesforce provides customer relationship management software and applications focused on sales, customer service, marketing automation, e-commerce, analytics, and application development.

{!_shared_content/operations_center/detection/generated/suggested_rules_2b13307b-7439-4973-900a-2b58303cac90_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2b13307b-7439-4973-900a-2b58303cac90.md!}

## Configure

This setup guide will show you how to provide an integration between Salesforce events and SEKOIA.IO.

### Prerequisites

- Have an internal concentrator (Salesforce)

### Configure OAuth

1. Go to the [Salesforce App Manager](https://login.salesforce.com)
2. Follow up [these instructions](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5) to configure new app

   ***Note: After configuration is complete please check if your OAuth credentials are valid and you can interact with salesforce api***

3. Get `clientId` and `clientSecret` from your app

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Salesforce.

