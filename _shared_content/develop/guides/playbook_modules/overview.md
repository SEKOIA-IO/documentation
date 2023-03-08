# Overview

## What is a playbook module?

A playbook module is a set of triggers and actions covering a specific service.

The module folder contains all the informations required to be able to run the triggers and actions:

* A manifest that describes the module and the expected configuration
* For each action and trigger a manifest file describing the expected arguments and the results 
* The code to execute

## The manifest file

Each module contains a `manifest.json` file that describes the module. This file contains:

* The name of the module
* A unique UUID identifying the module
* A version
* A description
* The configuration of the module
    * All the informations that are needed for the module to be able to communicate with the external service
    * The `configuration` key should be a valid JSON schema object

Here's an example of a `manifest.json` file:

```json
{
  "name": "Okta",
  "uuid": "4ef895d1-3f21-4678-8d0a-5c39c37210fe",
  "slug": "okta",
  "version": "2.0.0",
  "description": "[Okta](https://www.okta.com/) is an entreprise-grade, identity management service compatible with cloud apps as well as many on-premises applications",
  "configuration": {
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
    "required": [
      "base_url",
      "apikey"
    ]
  }
}
```

## Triggers and Actions

### Trigger

A trigger is some code that runs indefinitely waiting for events to occur. Once an event happens the trigger will push it to the playbook API.
Those events will trigger new playbook runs for all the palybooks that have the trigger as an entrypoint.

An example of a trigger is when an alert is raised in SEKOIA.IO. There is a trigger that watches for alert creations. Once a new alert is created, all the playbooks that wait for an event from this trigger will have a new run created.

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

The manifest contains:

* The name of the trigger/action
* A unique UUID
* A description
* The Docker parameters that will be specified when running the trigger/action
  * It allows to execute the appropriate action/trigger in a module that may have many of them 
* The arguments expected to run
    * Additionally to those arguments, the trigger/action will also have access to the configuration of the module
    * The `arguments` key should be a valid json schema object
* The kind of events this trigger will create or the result of the action
    * It is located under the `results` key 
    * The `results` key should be a valid json schema object


Here's an example of an action manifest:

```json
{
    "name": "Download File",
    "uuid": "09e9dc3a-aeb2-4dde-ad96-3ee543afdf51",
    "description": "Donwload the given file and save it",
    "docker_parameters": "download-file",
    "arguments": {
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
        "required": [
            "url"
        ],
        "title": "Arguments",
        "type": "object"
    },
    "results": {
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

from mwdb_module.action_config_to_observables import ConfigToObservablesAction
from mwdb_module.triggers import MWDBConfigsTrigger

if __name__ == "__main__":
    module = Module()
    module.register(MWDBConfigsTrigger, "trigger_mwdb_configs")
    module.register(ConfigToObservablesAction, "config_to_observables")
    module.run()
```

## Additional files

### Logo

Additionally a module should contain a logo image file. The file should be name either `logo.png` or `logo.svg` and located at the root of the module

### `Dockerfile`

The `Dockerfile` allows to create an image that will contain all the required code and dependencies to run the module's actions and triggers.

Here's an example of a `Dockerfile` allowing to run some python code:

```dockerfile
FROM python:3.11

WORKDIR /app

RUN pip install poetry

# Install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

RUN useradd -ms /bin/bash sekoiaio-runtime
USER sekoiaio-runtime

ENTRYPOINT [ "python", "./main.py" ]
```