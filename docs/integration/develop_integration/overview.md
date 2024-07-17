# How to develop a new integration

## Make sure that the integration you want to develop does not exist

1. Check our [Integration catalog](https://www.sekoia.io/en/integrations-catalog/)
2. Check also our [roadmap portal](https://roadmap-integrations.sekoia.io/tabs/18-coming-next) for upcoming integrations
3. If you still have doubts, ask our **Support** for confirmation

## What is your usecase?

- **You want to create a new format or modify an existing format, go to this [section](#i-want-to-create-a-new-format-or-modify-an-existing-format)**
- **You want to create a new automation, go to this [section](#i-want-to-create-a-new-automation)**

## List of development usecases

### I want to create a new format or modify an existing format

#### Step 1. Create a new format with the custom parser editor

!!! info
    Requirement: your data can be forwarded into Sekoia XDR platform with the existing [ingestion methods](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/)

You can create a custom format to ingest any unsupported type of data. Follow this [documentation page](../formats/create_a_format/) to create a new intake format:

Additional resources to support development:

- General concepts of [Intake format](../formats/overview/)
- [Parser development guide](../formats/parser/)
- Best practices for [Authentications](../formats/best_practices/authentications/) logs
- An E-learning module for the development of custom format is available in our training catalog, you can request an access [here](https://www.sekoia.io/en/lets-talk-about-your-training-project/)

Once you are done, you can create an intake based on this new format:

#### Step 2. Homologate a new format in the Sekoia catalog (optional)

If you have already developed a new format and would like Sekoia to perform the maintenance this format, you can request an homologation of your custom format. Once homologated, the format will integrate the public catalog of Sekoia.

!!! info
    To homologate your format, you will have to need to contribute through our Github repository 

- Fork the Github repository [SEKOIA-IO/intake-formats](https://github.com/SEKOIA-IO/intake-formats)
- Follow this contributing [guide](../formats/contribute/)

### I want to create a new automation

!!! warning
    Please note that all automations are available in the public library of Sekoia XDR platform. Other customers of Sekoia can access your automation module. We are still working on the implementation of private automations.

#### Step 1. Understand the general concepts

Before developing a new playbook trigger or playbook action, read this [introduction](../automation/overview) to get a grasp of the general concepts of automations.

#### Step 2. Create your automation

Once you have acquired a basic understanding of automations:

- Fork the Github repository [SEKOIA-IO/automation-library](https://github.com/SEKOIA-IO/automation-library)
- Follow this guide to [create your module](../automation/create_a_module/)