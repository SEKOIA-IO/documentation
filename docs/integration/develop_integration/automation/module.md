# Module

A Module groups a set of [triggers](trigger.md) and [actions](action.md) sharing a same interest. Most of the time, a module is associated to a product vendor.

A module contains the following items:

- a manifest `manifest.json`
- a pyproject file
- a `<module_name>_module` subdirectory holding the python code for triggers and actions.
- a list of json file
- an entrypoint `main.py`

## The Manifest

The manifest holds the information about the module. It defines:

- The unique identifier of the module (field `uuid`)
- The name of the module (field `name`)
- A slug for the module (field `slug`). The value of this field should match the following regex `[a-z-]\+`)
- A little description of the module (field `description`)
- The version number of the module (field `version`). This field should be updated each time a change is made in the module. This field follows the [Semantic versioning](https://semver.org/).
- A description of the configuration of the module with a [JSON schema model](https://json-schema.org/)


## The pyproject file

A module always hosts a pyproject file. This file describes the dependencies for the triggers and actions of the modules.


## The actions and triggers

Actions and triggers are split in two parts:

- a code hosted in the subdirectory `<module_name>_module`
- a json file that describes the action or the trigger.

See [action.md](action.md) and [trigger.md](trigger.md) for more information.

## The entrypoint

The entrypoint of the module is the file `main.py`. This file declares the actions and the triggers to use for the module and associate the actions and the triggers with the description file

## Python code

A module must be represented as a Python class, based on ['Module'](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/module.py) from [sekoia-automation-sdk](https://github.com/SEKOIA-IO/sekoia-automation-sdk/), with its configuration as a [pydantic model](https://docs.pydantic.dev/).

See [Azure Active Directory module code](https://github.com/SEKOIA-IO/automation-library/blob/main/AzureActiveDirectory/azure_ad/base.py)
