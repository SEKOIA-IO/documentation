# How to develop a new integration

## Before starting, make sure that the integration you want to develop does not exist

1. Check our [Integration catalog](https://www.sekoia.io/en/integrations-catalog/)
2. Check also our [roadmap portal](https://roadmap-integrations.sekoia.io/tabs/18-coming-next) for upcoming integrations
3. If you still have doubts, ask our Support for confirmation

## What is your usecase?

- **You want to ingest data from a product not supported by Sekoia, go to this [section](#usecase-1-you-want-to-ingest-data-from-a-product-not-supported-by-sekoia)**
- **You want to modify an existing intake, go to this [section](#usecase-2-you-want-to-modify-an-existing-intake)**
- **You want to create a new automation, go to this [section](#usecase-3-you-want-to-create-a-new-automation)**

## List of development usecases

### Usecase 1. You want to ingest data from a product not supported by Sekoia

#### Step 1. Understand the general concepts

Before starting, read these resources:

- [Overview of intake format](formats/overview.md) to get a grasp of event parsing.
- [Overview of ingestion methods](/integration/ingestion_methods/index.md) to get a grasp of event ingestion.

#### Step 2. Create your custom intake

To ingest a format of data, you will first create a custom format with the custom parser editor. A custom format describe the way data are extracted from an event.

Create a custom format to describe the format of the data to extract:

- Start by creating a [custom format](formats/create_a_format.md#custom-format-creation-on-the-platform)
- Write the parser of the custom format by following this [guide](formats/parser.md)

!!! info
    Additional resources to support development:

    - Best practices for [Authentications](formats/best_practices/authentications.md) logs
    - An E-learning module for the development of custom format is available in our training catalog, you can request an access [here](https://www.sekoia.io/en/lets-talk-about-your-training-project/)

Once you are done, you will create a custom intake based using this custom format. A custom intake is an instance of your custom format.

1. Click on the `+ Intake` from the Intakes homepage
2. Choose the custom format that you have created (you can search for custom format by its name)
3. Click on the `Create` button of the custom format
4. Provide an intelligible name
5. Select the entity to which you want to associate the corresponding data
6. Click on `Create`
7. Find your newly created source of events as well as the intake key in the Intakes homepage

You have now successfully ingested data from a new product. If you would like to share your custom format to the cybersecurity community or let Sekoia handle the maintenance of this custom format, proceed to the next step.

#### Step 3. Create your custom connector (optional)

If there are no compatible methods in Sekoia to collect events from your product, you can create a custom connector that will handle the collection process.
Sekoia will trigger this connector on a recurring basis to connect to your product and collect new events.

!!! Prerequisites
    A custom connector requires Python development skills, as connectors are custom Python code developped using sekoia-automation SDK.

If you're all set, then:
1. Click on `+ New Integration` in the **Integrations** page, then click on `Get Started` and follow the steps given to set up your development environment
2. Follow the [indications](/integration/develop_integration/automation/create_a_module.md) given to develop your module with a connector (no need to follow the trigger and action sections)
3. Once your code is finalized, click on `Import my custom integration`, then follow the steps given to import your code from your Github or Gitlab repository

Once you have created your custom connector, return to Step 2 and edit your custom format.
In the top right of the screen, select your custom connector to associate it with your custom format. When creating an intake using this format, the selected custom connector will be used to collect events.

![intake_connector](/assets/operation_center/intakes/custom_intake_connector.png){: style="max-width:100%"}

#### Step 4. Homologate your custom format in the Sekoia catalog (optional)

If you have created a new format and want Sekoia to manage its maintenance, you can request homologation for your custom format. Once approved, the format will be added to Sekoia's public catalog.

!!! info
    To homologate your custom format, you will need to contribute through our Github repository

- Fork the Github repository [SEKOIA-IO/intake-formats](https://github.com/SEKOIA-IO/intake-formats)
- Follow this [guide](formats/create_a_format.md#custom-format-creation-with-the-github-repository) to add the custom format in Github and request an homologation

### Usecase 2. You want to modify an existing intake

You would like to parse additional fields in an existing intake or modify the way existing fields are extracted. To do this, you can create a custom format based on an existing intake:

1. Click on the `+ Intake` from the Intakes homepage
2. Search for the intake you wish to modify
3. Click on the `See format` button at the top right of the card
4. Click on the `Duplicate` button at the top right of the custom parser editor
5. Modify the parser by using this [guide](formats/parser.md)

Once you have finished your modifications, [create a custom intake](#step-2-create-your-custom-intake) based on this new custom format.

### Usecase 3. You want to create a new automation

!!! warning
    Please note that all automations are available in the public library of the Sekoia SOC platform, making them accessible to other Sekoia customers. We are currently working on implementing private automations.

#### Step 1. Understand the general concepts

Before developing a new playbook trigger or playbook action, read this [overview of automations](automation/overview.md) to get a grasp of the general concepts of automations.

#### Step 2. Create your automation

Once you have acquired a basic understanding of automations:

- Fork the Github repository [SEKOIA-IO/automation-library](https://github.com/SEKOIA-IO/automation-library)
- Follow this guide to [create your module](automation/create_a_module.md)

#### Step 3. Homologate your automation in the Sekoia catalog

The last step is to homologate your automation in order to make it available in the automation library.

- Follow these [instructions](automation/create_a_module.md#homologation-request) to homologate your automation