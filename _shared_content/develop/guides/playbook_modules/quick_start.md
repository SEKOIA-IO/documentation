# Quick start

In this section we will see how to create a simple module from scratch.

This module will conain one action and one trigger:

* The action will allow to send an HTTP request and return its response.
* The trigger will watch for ??

## Initialize the module

The first step is to install the SEKOIA's automation SDK.
This SDK contains various command line utilities that will help us manage modules.

Simply run the following command:

```shell
pip install sekoia-automation-sdk
```

!!! note
    The SDK needs a python version equal or newer to python3.10

Once the SDK is installed we can use it to create an empty module:

```
sekoia-automation new-module modules  # modules is the path of the folder containing the modules
```

The command will ask for various info about the module:

* The name of the module: `TestHTTP`
* The description of the module: `My test HTTP module`

Once the command is executed we should have a new module created with all the boilerplate files:

```
TestHTTP
├── Dockerfile
├── main.py
├── manifest.json
├── pyproject.toml
├── testhttp_modules
│   ├── __init__.py
│   └── models.py
└── tests
    ├── conftest.py
    └── __init__.py
```


## Create our action

Our action will take three arguments:

* The URL to query
* The HTTP method to use
* The HTTP headers to provide

Two of those arguments will be required, the URL and the method.

The result of our action will contain:

* The status code
* The response body as text
* The response headers

### Define the manifest

Let's create an `action_request.json` file that describe our action:

```json
{
  "name": "Request URL",
  "uuid": "429e8715-fdde-4064-b8e8-96e408917d25",
  "description": "Requests a resource at a specified URL and returns the response",
  "docker_parameters": "request",
  "arguments": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
      "url": {
        "description": "Target URL of the HTTP request",
        "type": "string",
        "format": "uri"
      },
      "headers": {
        "description": "Headers to use when sending the requests. i.e. {\"authorization\": \"Bearer foo\"}",
        "type": "object"
      },
      "method": {
        "description": "Method of the HTTP request",
        "type": "string",
        "enum": [
          "get",
          "post",
          "put",
          "patch",
          "head",
          "delete"
        ]
      }
    },
    "required": [
      "url",
      "method"
    ],
    "title": "Arguments",
    "type": "object"
  },
  "results": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
      "status_code": {
        "description": "Integer code of responded HTTP Status",
        "type": "integer"
      },
      "headers": {
        "description": "Headers used by the server in the response",
        "type": "object"
      },
      "text": {
        "description": "Content of the response in unicode",
        "type": "string"
      }
    },
    "required": [
      "status_code",
      "url",
      "text"
    ],
    "title": "Results",
    "type": "object"
  }
}

```

### Add the code

Now that we have a manifest describing our action we can add the code!


#### Specify the requirements

Our action is going to use `requests` to send HTTP requests, so the first step is to add the package in our requirements.

Edit the `pyproject.toml` file and in the `[tool.poetry.dependencies]` section add the following line:

```toml
requests = "*"
```
Once the file has been modified we can lock the requirements with the command

```
poetry lock
```

!!! note
    If poetry is not installed on your system you may need to run `pip install poetry` before.


#### Create the action

Inside our Python package `testhttp_modules` we can create a new file `action_request.py` that will contain the logic of our action:

```python
import requests
from sekoia_automation.action import Action


class RequestAction(Action):
    """
    Action to request an HTTP resource
    """

    def run(self, arguments: dict) -> dict:
        method = arguments.get("method")
        url = arguments.get("url")
        headers = arguments.get("headers")

        self.log(message=f"Request URL module started. Target URL: {url}", level="info")

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
        )

        if not response.ok:
            # Will end action as in error
            self.error(f"HTTP Request failed: {url} with {response.status_code}")

        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "text": response.text,
        }
```

Let's explain a bit the code of the action.

Our action is a class that inherit from `Action`, a base class from SEKOIA.IO's automation SDK.
The child actions must define the `run` method that will be passed the arguments provided to the action

The base `Action` class provides few helpers like the `log` and `error` methods:

* The `log` method will make sure the log is sent to the API so when checking the run of the action we can see a trace of what happened.
* The `error` method will mark the action as failed and send back the error to the API.

Finally if everything went well we can return the results. The base action will take care of sending it back to the playbook API.


#### Register the action in the entrypoint

Now that we have a manifest and the code logic we must register the action to the entrypoint.

To do so edit the `main.py` file and register the action:

```python
from sekoia_automation.module import Module

from testhttp_module.request_action import RequestAction

if __name__ == "__main__":
    module = Module()

    module.register(RequestAction, "request")

    module.run()
```

The action has been registered between the creation of the module and the call running it. The first arguments of `module.register` is our action class and the second is the `docker_parameter` that was specified in our action's manifest.

That's it! Now we have a module containing our action and ready to run !