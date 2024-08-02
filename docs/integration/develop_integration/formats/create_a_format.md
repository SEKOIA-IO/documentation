## Custom intakes

Sekoia.io provides a list of intakes that allows you to integrate events from different sources such as systems, applications and security appliances.

Some technologies may not have an associated Intake in the official Sekoia.io catalog and therefore cannot be parsed in Sekoia.io.

The "Custom format" feature allows you to easily develop your own Intake. It gives you the tools to parse your events in the Elastic Common Schema (ECS) format to ensure agnostic detection and to index fields for search in the Events page.

## Create a Custom format
### Custom format creation on the platform

!!!note
    In order to use this feature, you need to have the `SIC_WRITE_INTAKE` permission associated to your Sekoia.io account. This permission also allows you to create an existing Intake.

The creation of an empty Custom format is the first step to develop your own Intake.

After that, you will be able to create an instance of this Intake and start sending your logs. No event will be parsed but you will be able to see the evolution of your parser while you are developping it.

To create an empty custom format:

1. Go to `Intakes`, `+ INTAKE` and select `Custom format`
2. Write the name of your Intake
3. Give a description for your Intake
4. Select a module. A module is linked to a taxonomy in relation with your format which will help you develop your parser. For instance, if you develop a Custom format for a Fortinet product, you will choose the Fortinet module. If your module does not exist, just write the name of your module (name of the application or compagny if they have different products) and click on `Create`
5. Select the data sources associated to your events. Note that you can have multiple ones and that data sources can be used when you want to deploy rules.
6. Click on `Save`

#### Panel overview
The custom format panel is structured like this:

1. Metadata information about your Intake
2. An area where you can build your Intake with `Stages`
3. A button to switch to `Expert mode` (YAML visualization of your Intake)
4. A button to display the `Fields manager`
5. An area to test your Intake with an event sample.

![Sekoia.io Custom format Panel Overview](/assets/operation_center/intakes/custom_intake_header-1.png){: style="max-width:100%"}

### Custom format creation with the github repository
#### Technical Requirements

- Clone the Github repository [SEKOIA-IO/intake-formats](https://github.com/SEKOIA-IO/intake-formats)

#### Create a module

If the module that will contain your format doesn't exist, you will need to create it.

To create a new module, follow these steps: 

1. Execute the following command:

  ```bash
  > cd ~/dev/intake-formats/utils
  > poetry run python3 generate.py new-module
  ```

2. Complete the form with the name of the module, its description and its destination directory. 
  A new directory, with the name of the module, will appear at the root of your workspace.

3. In the `_meta` directory, add a logo to illustrate your module with the following criteria:

  - The logo must be a PNG image
  - The logo must be named `logo.png`
  - The background must be transparent
  - The image must be squared, ie the width is equal to the height
  - The weight of the logo must be lesser than 50kb

#### Create a format

To create a new format, follow these steps: 

1. Execute the following command:

  ```bash
  > cd ~/dev/intake-formats/utils
  > poetry run python3 generate.py new-format <module_directory>
  ```

2. Complete the form with the name of the format, its slug and a description. 
 Your new format will appear, as a directory, under its module directory.

3. Open your format’s manifest (`_meta/manifest.yml`) and provide some [data sources](datasources.md) with a description for each one

4. In the `_meta` directory, add a logo to illustrate your format with the following criteria:

  - The logo must be a PNG image
  - The logo must be named `logo.png`
  - The background must be transparent
  - The image must be squared, ie the width is equal to the height
  - The weight of the logo must be lesser than 50kb.

#### Create the parser

To create the parser, follow these steps: 

1. In the format directory, go to the `ingest` folder and edit `parser.yml`

2. Follow [this guide](parser.md) (go to tab `In code`) to develop the parser

Note that the parser must generate [structured events](structured_event.md) that respect the [taxonomy of the format](taxonomy.md)

#### Create a test

To create the test file, follow these steps: 

1. From a sample event, use [create_test.py](https://github.com/SEKOIA-IO/intake-formats/blob/main/utils/create_test.py) to create a new test file

  ```bash
  > cd ~/dev/intake-formats/utils
  > poetry run python3 create_test.py ~/dev/intake-formats/<module>/<format>/tests/test_my_event.json <event>
  > cat /tmp/raw_event.txt | poetry run python3 create_test.py ~/dev/intake-formats/<module>/<format>/tests/test_my_second_event.json -
  ```

2. Complete the test file with expected fields

#### Run tests

Tests are run from the `intake-formats/utils` directory. 

```bash
> cd ~/dev/intake-formats/utils
> poetry run pytest test_formats.py -vv               # run tests for all parsers
> poetry run pytest test_formats.py -vv --changes     # run tests only for updated parsers
> poetry run pytest test_formats.py --module='module-name' -vv # run tests for a specific module
> poetry run pytest test_formats.py --format='format-name' -vv # run tests for a specific format
> poetry run pytest test_formats.py --format='format-name' --fix-expectations # fix test expectations
```

#### Write smart descriptions

The [structured events](structured_event.md), generated by the parser can be hardly readable for a human. The smart descriptions will define how to describe the events and which important information must be displayed in the description to ease the decision-making process.

To write smart descriptions, follow these steps:

1. In the format directory, go to the `_meta` folder and edit `smart-descriptions.json`
  
2. Follow [this guide](smartdescriptions.md) to write smart descriptions for your format

#### Quality checklist

To ensure the quality of contribution, the following points are reviewed in Github pull requests:

- Have clear descriptions for new modules, new formats and taxonomy
- A logo is provided for any new modules and any new formats
- Tests should cover at least 75% of parsers
- At least one smart-description is provide for any new format

#### Homologation request 

Once you are done writing and testing your intake format, the last step is to request an homologation to Sekoia. Once your intake format is homologated, it will appear in the intake catalog of **Sekoia SOC platform**:

- Create a pull request
- Send an email to [homologation-requestn@sekoia.io](mailto:homologation-request@sekoia.io) with the pull request link
- You will get an acknowledgement from Sekoia Integration team
- In the following days (5 days max), you will receive feedbacks in your pull request that you must take into account
- Once all feedbacks are taken into account, Integration team will **validate** your pull request

The homologation process is now finished.