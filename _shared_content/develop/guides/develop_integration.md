# How to develop a new integration

## Make sure that the integration you want to develop does not exist

1. Go to our [Integration catalog](https://www.sekoia.io/en/integrations-catalog/)
2. Check also our [roadmap portal](https://roadmap-integrations.sekoia.io/tabs/18-coming-next) for upcoming integrations
3. If you still have doubts, ask [support@sekoia.io](mailto:support@sekoia.io) for confirmation

## What is your usecase?

- You want to create a new format or modify an existing format, go to this [section](#i-want-to-create-a-new-format-or-modify-an-existing-format)
- You want to create a new automation, go to this [section](#i-want-to-create-a-new-automation)

## Different development usecases

### I want to create a new format or modify an existing format

#### Step 1. Create a new format with the custom parser editor

Requirement: your data can be forwarded into Sekoia XDR platform with the existing [ingestion methods](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/)

You can create a custom format to ingest any unsupported type of data. Follow this documentation page to create a new intake format:

- https://docs.sekoia.io/xdr/features/collect/integrations/custom_format/
- https://docs.sekoia.io/xdr/features/collect/intakes/#custom-intakes
- [TODO merge the two pages]

If you need help to understanding how parsers works, read this documentation:

- https://github.com/SEKOIA-IO/intake-formats/blob/main/doc/overview.md
- [TODO Add here resources for fields to parse depending on the category]
- An E-learning module for the development of custom format is available in our training catalog, you can request an access [here](https://www.sekoia.io/en/lets-talk-about-your-training-project/)

Once you are done, follow this [documentation page](https://docs.sekoia.io/xdr/features/collect/intakes/#create-an-intake-from-our-integrations-catalog) to a create an intake based on this new format:

#### Step 2. Homologate a new format in the Sekoia catalog (optional)

If you have already developed a new format and would like Sekoia to perform the maintenance this format, you can request an homologation of your custom format. Once homologated, the format will integrate the public catalog of Sekoia.

- Follow this contributing [guide](https://github.com/SEKOIA-IO/intake-formats/blob/296e3460ff26ed61f3e1c3473c7e2a97a720e1fa/CONTRIBUTING.md)
- Create a pull request of your automation
- Send an email to [team-integration@sekoia.io](mailto:team-integration@sekoia.io)
- You will get an acknowledgement from Sekoia Integration team
- In the following days, you will receive feedbacks in your pull request that you must take into account
- Once all feedbacks are taken into account, Integration team will validate your pull request

The homologation process is now finished. Your intake will appear in the public intake catalog.

### I want to create a new automation

#### Step 1. Understand the general concepts

Before developing a new playbook trigger or playbook action, you will need to read completely this documentation to get a grasp of the general concepts of automations.

- https://github.com/SEKOIA-IO/automation-library/tree/main/docs
- https://docs.sekoia.io/xdr/develop/guides/automation/overview/

#### Step 2. Develop and test

Once you have acquired a basic understanding of these concepts:

- Fork the automation [repository](https://github.com/SEKOIA-IO/automation-library)
- Create your module: https://docs.sekoia.io/xdr/develop/guides/automation/create_a_module/
- Code your integration
- Write unit test to test your code
- You can run your test with this command line: https://github.com/SEKOIA-IO/automation-library/blob/main/docs/testing.md
- Validate requirements with this utility tool: https://github.com/SEKOIA-IO/automation-library/blob/main/_utils/compliance/__main__.py
- [TODO write a doc for the util tool]

#### Step 3. Homologate your automation module

Once you are done developing and testing your automation module, the last step is to request an homologation to Sekoia. Once your automation is homologated, it will appear in the automation library of Sekoia XDR platform.

- Create a pull request of your automation
- Send an email to [team-integration@sekoia.io](mailto:team-integration@sekoia.io)
- You will get an acknowledgement from Sekoia Integration team
- In the following days, you will receive feedbacks in your pull request that you must take into account
- Once all feedbacks are taken into account, Integration team will validate your pull request

The homologation process is now finished. Your automation will appear in the automation library and you will be able to use it in your playbooks.