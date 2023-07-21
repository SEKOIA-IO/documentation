# Automation Module

Playbooks are highly flexible and can be used to automate any processes that require a specific set of actions. 
For example, a playbook can automate the triage and investigation of recurrent phishing alerts. 

A playbook is made of interconnected triggers and actions as basic blocks. 
These basic blocs implement the logic of a specific service and are part of a module.

This section provides details on how modules are organized and developed.

## Overview

A module is a set of triggers and actions covering a specific service.

The module folder contains all the information required to be able to run the triggers and actions:

* A manifest that describes the module and the expected configuration
* For each action and trigger a manifest file describing the expected arguments and the results 
* The code to execute

For example, a module named `MyCyberEnricher` is organized under the following folder structure:
```json
MyCyberEnricher/
├── manifest.json  // (1)!
├── action_enrich_ip.json  //(2)!
├── trigger_pull_logs.json  // (3)!
├── logo.png  // (4)!
├── main.py  // (5)!
├── poetry.lock  // (6)!
├── pyproject.toml  // (7)!
├── Dockerfile  // (8)!
├── cyber_enricher/  // (9)!
└── tests/  // (10)!
```

1. the module manifest file that specifies elements such as the name or the module's configuration
2. the manifest file of the action `enrich_ip`
3. the manifest file of the trigger `trigger_pull_logs`
4. the logo of the module
5. the code entrypoint
6. the Poetry dependency listing file
7. the Python project definition
8. Dockerfile to build the module
9. the module source code
10. the tests source code

## The manifest file

Each module contains a `manifest.json` file that describes the module.

Here's an annotated example of a `manifest.json` file:

```json
{
  "name": "Okta",  // (1)!
  "uuid": "4ef895d1-3f21-4678-8d0a-5c39c37210fe",  // (2)!
  "slug": "okta",
  "version": "2.0.0",  // (3)!
  "description": "[Okta](https://www.okta.com/) is an entreprise-grade, identity management service compatible with cloud apps as well as many on-premises applications",
  "configuration": {  // (4)!
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Okta",
    "type": "object",
    "properties": {
      "base_url": {
        "description": "The url to your Okta tenant",
        "type": "string",
        "format": "uri"
      },
      "apikey": {
        "description": "The APIkey to authenticate call to the API",
        "type": "string"
      }
    },
    "required": [  // (5)!
      "base_url",
      "apikey"
    ]
  }
}
```

1. The name of the module. It will be displayed to the user in the playbook UI
2. The UUID of the module. It must be unique
3. A version for the module. This version must be incremented each time a change is made in the module
4. The configuration of the module
      * All the informations that are needed for the module to be able to communicate with the external service
      * The `configuration` attribute should be a valid JSON Schema object
5. A configuration item can be mandatory

## Triggers and Actions

### Trigger

A trigger is some code that runs indefinitely waiting for events to occur. Once an event happens the trigger will push it to the playbook API.
Those events will trigger new playbook runs for all the playbooks that have the trigger as an entrypoint.

An example of a trigger is when an alert is raised in Sekoia.io. There is a trigger that watches for alert creations. Once a new alert is created, all the playbooks that wait for an event from this trigger will have a new run created.

### Action

An action is a node inside a playbook. When the playbook runs it will follow its flow and call the actions when needed.

Those actions will take various arguments as an input.

Those arguments can be:

* The results of a previous action
* A part of the event from the trigger
* A value manually defined by the user
* Data from the playbook run store


### Manifest

Each trigger/action has its own manifest file that describes it. This manifest file is a json file prefixed by `trigger_`  or `action_` followed by the slug of the trigger/action.

i.e. The manifest for the action allowing to download a file is named `action_download_file.json`

Here's an annotated example of an action manifest:

```json
{
    "name": "Download File",  // (1)!
    "uuid": "09e9dc3a-aeb2-4dde-ad96-3ee543afdf51",  // (2)!
    "description": "Donwload the given file and save it",
    "slug": "download-file",  // (3)!
    "docker_parameters": "download-file",  // (4)!
    "arguments": {  // (5)!
        "$schema": "http://json-schema.org/draft-07/schema#",
        "properties": {
            "url": {
                "description": "Url of the file to download",
                "type": "string",
                "format": "uri"
            },
            "headers": {
                "description": "Headers to use when sending the requests. i.e. {\"authorization\": \"Bearer foo\"}",
                "type": "object"
            }
        },
        "required": [  // (6)!
            "url"
        ],
        "title": "Arguments",
        "type": "object"
    },
    "results": {  // (7)!
        "$schema": "http://json-schema.org/draft-07/schema#",
        "properties": {
            "file_path": {
                "description": "File path on disk",
                "type": "string"
            }
        },
        "required": [
            "file_path"
        ],
        "title": "Results",
        "type": "object"
    }
}
```

1. The name of the trigger/action. It will be displayed to the user in the playbook UI
2. The UUID of the trigger/action. It must be unique
3. The slug name of the trigger/action
      * It allows to execute the appropriate action/trigger in a module that may have many of them 
4. The Docker parameters that will be specified when running the trigger/action
5. The arguments expected to run
      * In addition to those arguments, the trigger/action will also have access to the configuration of the module
      * The `arguments` attribute must be a valid JSON Schema object
6. Arguments can be mandatory
7. The kind of events this trigger will create or the result of the action
      * It is located under the `results` key 
      * The `results` attribute should be a valid JSON Schema object

## Business logic

A module wouldn't exist without the code needed to run a trigger or an action. 
Each module contains all the code required to run the actions and triggers that are declared in the manifest files.

### Python code

In python the modules usually contain:

* A package (a folder) containing the python code that will run
* A `main.py` file, the entrypoint of the module 
* A `tests` package that holds all the unit tests for the module
* A `pyproject.toml` and a `poetry.lock` file that allow to define all the requirements for the module 
    * You can check the [Poetry documentation](https://python-poetry.org/ ) for more information

#### Module entrypoint

The `main.py` file is the only entrypoint in the module actions and trigger. 
It will execute the appropriate action or trigger depending on the argument that is provided to the command.
This argument is defined by the `docker_parameters` attribute in the manifest files.

The `sekoia-automation-sdk` PIP package makes it easier to declare the trigger and actions that can be executed.

Here's an example of a module entrypoint:

```python
from sekoia_automation.module import Module

from mwdb_module.action_config_to_observables import ConfigToObservablesAction  # (1)!
from mwdb_module.triggers import MWDBConfigsTrigger

if __name__ == "__main__":
    module = Module()
    module.register(MWDBConfigsTrigger, "trigger_mwdb_configs")
    module.register(ConfigToObservablesAction, "config_to_observables")  # (2)!
    module.run()
```

1. Import the action or trigger that should be registered in the entrypoint
2. Register the action. The first arguments of `module.register` is our action class and the second is the `docker_parameter` that was specified in our action's manifest.

## Additional files

### Logo

Additionally, a module should contain a logo image file. The file should be named either `logo.png` or `logo.svg` and located at the root of the module
