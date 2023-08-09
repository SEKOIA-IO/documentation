uuid: 3f99cdd8-aeca-4860-a846-6f2a794583e1
name: Azure MySQL
type: intake

## Overview

Azure Database for MySQL provides fully managed, enterprise-ready community MySQL database as a service. The service is developed and managed by Microsoft Corp.

{!_shared_content/operations_center/detection/generated/suggested_rules_3f99cdd8-aeca-4860-a846-6f2a794583e1_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/3f99cdd8-aeca-4860-a846-6f2a794583e1.md!}

## Configure

To forward **Azure MySQL** events from Azure to Sekoia.io you need to send your event to an Azure **Event Hub** where Sekoia.io will collect the events.
<div style="text-align: center;">
    <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/event_hub/consume_azure_logs.png">
</div>

### Prerequisite

You must have Contributor write on Azure to perfom the following installation.

{!_shared_content/operations_center/integrations/event_hub.md!}


### Send logs from Azure MySQL to Azure Event Hub

You need to activate and configure the Azure MySQL diagnostic settings (e.g. `company-mysql`).

Navigate to “Home”, “SQL databases” (e.g. `company-mysql`), “Monitoring” and “Diagnostic settings”:

- Add a new diagnostic setting, and select “Stream to an event hub” and click on configure.
- Select the previously created “Event hubs”, “Event Hub” and `SharedAccessKey`.
- In the log section, select `MySqlAuditLogs` and `MySqlSlowLogs`.
- Choose a name for this configuration and click on “Save”.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Azure Database for MySQL`.

{!_shared_content/operations_center/integrations/configure_consume_event_hub.md!}
