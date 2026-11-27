uuid: 94e374f4-f78f-4863-bee0-2c852f786bff
name: Clever Cloud
type: intake

## Overview
- **Vendor**: Clever Cloud
- **Supported environment**: SaaS
- **Detection based on**: Audit
- **Supported application or feature**: Application Logs and Access logs

Clever Cloud provides you with the best tools to host, deploy and maintain your applications in operational conditions, at a controlled cost.

In this documentation, you will learn how to collect and send Clever cloud Application and Access logs to Sekoia.io.

## Sekoia.io configuration procedure

#### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click on **+ Intake** button to create a new one
2. Choose **Clever cloud**, give it a name and choose the relevant Entity
3. Click on **Create** button
4. Copy your intake key

## Clever CLoud configuration procedure

### Prerequisites

- Clever tools cli installed and linked to your clever cloud instance (see https://www.clever.cloud/developers/doc/manage/cli/) 

### Clever tools cli command lines

#### Create an Application Logs drain for an application

Run the following command to create a Clever Cloud drain that will automatically send logs to your intake based on the intake key :
> Replace the <APP_ID> and <SEKOIA_INTAKE_KEY> placeholders with the app ID you want to drain the logs from and the intake key of your newly created Clever Cloud Intake.
```
clever drain create --app <APP_ID> --kind LOG sekoia https://intake.sekoia.io/jsons --intake-key "<SEKOIA_INTAKE_KEY>"
```

> see https://www.clever.cloud/developers/doc/develop/observability/drains/

#### Create an Access Logs drain for an application

Run the following command to create a Clever Cloud drain that will automatically send logs to your intake based on the intake key :
> Replace the <APP_ID> and <SEKOIA_INTAKE_KEY> placeholders with the app ID you want to drain the logs from and the intake key of your newly created Clever Cloud Intake.
```
clever drain create --app <APP_ID> --kind ACCESSLOG sekoia https://intake.sekoia.io/jsons --intake-key "<SEKOIA_INTAKE_KEY>"
```

> see https://www.clever.cloud/developers/doc/develop/observability/drains/

#### Verify that the logs are ingested

Go in your intakes view and wait for few minutes until you see new events arriving.

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/94e374f4-f78f-4863-bee0-2c852f786bff_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/94e374f4-f78f-4863-bee0-2c852f786bff.md!}

