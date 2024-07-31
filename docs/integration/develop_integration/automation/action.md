# Action

An action helps to execute specific tasks (see [definition](https://docs.sekoia.io/xdr/features/automate/actions/)). It composes one of the three items of a playbook.

In a module, each action consists of 2 elements:

- A manifest file in the root directory of the module. The manifest of an action is prefixed with the string `action_`.
  This document contains:
  	- The unique identifier of the action (field `uuid`)
	- The name of the action (field `name`)
	- A short description about that the action (field `description`)
	- The unique command name of the action (field `docker_parameter`)
	- A description of the arguments of the action (field `arguments`). This description is a [JSON schema model](https://json-schema.org/)
	- A description of the output of the action (field `results`). This description is a [JSON schema model](https://json-schema.org/) and may be empty in the action returns no data.

  See [Azure Active Directory «Enable User» action’s manifest](../AzureActiveDirectory/action_enable_user.json)

- A python code 

## Python code

An action is a class based on [`Action`](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/action.py) from [sekoia-automation-sdk](https://github.com/SEKOIA-IO/sekoia-automation-sdk/). 

This class must implement the class properties `name` and `description`.

It also must implement the method `run` that accepts the arguments and may returns a result.
The arguments and the result must be declared as a [pydantic model](https://docs.pydantic.dev/), holding the same properties declared in the JSON schema model for the arguments and the result in the manifest.

(See [Azure Active Directory «Enable User» code](../AzureActiveDirectory/azure_ad/user.py))

## Entrypoint

To expose an action of the module, the action must be declared in `main.py` at the root of the module.

Import the class in `main.py` and register the class, against the module, with the unique command name of the action as second argument.

(See [Azure Active Directory main.py](../AzureActiveDirectory/main.py))
