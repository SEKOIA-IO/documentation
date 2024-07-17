# Create a Module

In this section we will see how to create a simple module from scratch.

This module will contain one trigger and one action:

* The trigger will watch for new entries exposed by an HTTP endpoint
* The action will allow to send an HTTP request and return its response.

## Technical Requirements

- Clone the Github repository [SEKOIA-IO/automation-library](https://github.com/SEKOIA-IO/automation-library)
- Install the SEKOIA's automation SDK. This SDK contains various command line utilities that will help us manage    modules. Simply run the following command:
``` shell
pip install sekoia-automation-sdk

```
!!! note
    The SDK needs a Python version equal or newer to 3.10.

## Initialize the module

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

### Specify the requirements

Our trigger and action are going to use `requests` to send HTTP requests, so the first step is to add the package in our requirements.

Poetry can be used to add the requirements by simply running:

```
poetry add requests
```

!!! note
    If poetry is not installed on your system you may need to run `pip install poetry` before.

## Create our trigger

Our trigger will take one argument, the URL that exposed the objects we want to handle with our module.
This argument will be required.

### Add the code

Inside our Python package `testhttp_modules` we can create a new file `trigger_new_entries.py` that will contain the logic of our trigger:

```python
import time

from pydantic import BaseModel, HttpUrl
import requests
from requests import HTTPError
from sekoia_automation.trigger import Trigger  # (1)!


class TriggerConfiguration(BaseModel):
    url: HttpUrl


class Entry(BaseModel):
    id: int
    value: str
    timestamp: int


class NewEntries(BaseModel):
    entries: list[Entry]


class NewEntriesTrigger(Trigger):
    configuration: TriggerConfiguration  # (2)!
    results_model = NewEntries  # (3)!

    def run(self):  # (4)!
        while True:
            try:
                response = requests.get(self.configuration.url)
                response.raise_for_status()

                entries = response.json()
                self.send_event(  # (5)!
                    event_name=f"Pushing {len(entries)} new entries", 
                    event=NewEntries(entries=entries),
                )
            except HTTPError:
                self.log(  # (6)!
                    f"HTTP Request failed: {self.configuration.url} with {response.status_code}",
                    level="error",
                )
            time.sleep(3600)
```

1. We import the base `Trigger` class from the Sekoia.io automation SDK
2. Define the expected configuration using the `Pydantic` lib
3. Define the format of the results using the `Pydantic` lib
4. The child triggers must define the `run` method that runs the trigger.
  This method must run forever
  It must handle all the expected errors 
1. The base `Trigger` class provides a `send_event` method that allows to trigger a new event. For each playbook having this trigger a new run will be started with `event` as argument.
2. The `log` method allows to log errors and informations. Those logs are visible in the UI.


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

### Add the code

Now that we have a manifest describing our action we can add the code!

Inside our Python package `testhttp_modules` we can create a new file `action_request.py` that will contain the logic of our action:

```python
from typing import Literal

from pydantic import BaseModel, HttpUrl
import requests
from sekoia_automation.action import Action  # (1)!


class RequestArguments(BaseModel):  # (2)!
    url: HttpUrl
    headers: dict | None = None
    method: Literal["get", "post", "put", "patch", "delete"]
  
class Response(BaseModel):  # (3)!
  status_code: int
  headers: dict
  text: str


class Request(Action):  # (4)!
    """
    Action to request an HTTP resource
    """

    results_model = Response

    def run(self, arguments: RequestArguments) -> Response:  # (5)!
        self.log(  # (6)!
          message=f"Request URL module started. Target URL: {arguments.url}", level="info"
          )

        response = requests.request(
            method=arguments.method,
            url=arguments.url,
            headers=arguments.headers,
        )

        if not response.ok:
            # Will end action as in error
            self.error(  # (7)!
              f"HTTP Request failed: {arguments.url} with {response.status_code}"
              )

        return Response(  # (8)!
          status_code=response.status_code,
          headers=dict(response.headers),
          text=response.text,
        )
```

1. We import the base `Action` class from the Sekoia.io automation SDK
2. Define the expected arguments using the `Pydantic` lib
3. Define the format of the response using the `Pydantic` lib
4. Our action is a class that inherit from `Action`, a base class from Sekoia.io's automation SDK.
5. The child actions must define the `run` method that will be passed the arguments provided to the action
6. The base `Action` class provides few helpers like the `log` method. This method makes sure the log is sent to the API so when checking the run of the action we can see a trace of what happened.
7. The `error` method will mark the action as failed and send back the error to the API.
8. Finally, if everything went well we can return the results. The base action will take care of sending it back to the playbook API.

## Test your code 
Make sure you test your code with unitary and integration tests. In the following code, 
we will test `get request`our previous example's action code. In practice, you have to cover all the use cases of the module. 
```python
import pytest
import requests_mock
from pydantic import HttpUrl
from your_module import Request, RequestArguments, Response  # Adjust the import according to your module structure

@requests_mock.Mocker()
def test_get_request(mock_request):
    # Mock the HTTP response
    mock_response = {
        'status_code': 200,
        'headers': {'Content-Type': 'application/json'},
        'text': 'Success'
    }
    mock_request.get('http://example.com', status_code=mock_response['status_code'],
                     headers=mock_response['headers'], text=mock_response['text'])

    # Create the arguments
    arguments = RequestArguments(
        url='http://example.com',
        headers=None,
        method='get'
    )

    # Instantiate and run the action
    action = Request()
    result = action.run(arguments)

    # Assert the response
    assert result.status_code == mock_response['status_code']
    assert result.headers == mock_response['headers']
    assert result.text == mock_response['text']


```
To effectively manage dependencies and run your tests, you should use Poetry. For more detailed information, you can check the [Poetry documentation](https://python-poetry.org/docs/). Additionally, you can look at the tests in the existing module.

## Generate the manifest and update the entrypoint

Now that the code has been created we can generate the manifest and update the entrypoint by calling

```
sekoia-automation generate-files-from-code
```

!!! note
    The command must be executed from the root of the module or we can provide the path to the module as argument

### Generated manifests

The previous step generated two manifests files for us:

* `trigger_newentriestrigger.json` describing the trigger
* `action_request.json` for the action

We can edit the manifests to add a description:

=== "action_request.json"

    ```json
    {
      "name": "Request URL",
      "uuid": "429e8715-fdde-4064-b8e8-96e408917d25",
      "description": "Requests a resource at a specified URL and returns the response",
      "slug": "Request",
      "docker_parameters": "Request",
      "arguments": {  // (1)!
        "title": "RequestArguments",
        "type": "object",
        "properties": {
          "url": {
            "title": "Url",
            "minLength": 1,
            "maxLength": 2083,
            "format": "uri",
            "type": "string"
          },
          "headers": {
            "title": "Headers",
            "type": "object"
          },
          "method": {
            "title": "Method",
            "enum": [
              "get",
              "post",
              "put",
              "patch",
              "delete"
            ],
            "type": "string"
          }
        },
        "required": [  // (2)!
          "url",
          "method"
        ]
      },
      "results": {  // (3)!
        "title": "Response",
        "type": "object",
        "properties": {
          "status_code": {
            "title": "Status Code",
            "type": "integer"
          },
          "headers": {
            "title": "Headers",
            "type": "object"
          },
          "text": {
            "title": "Text",
            "type": "string"
          }
        },
        "required": [
          "status_code",
          "headers",
          "text"
        ]
      }
    }
    ```

    1.  Arguments is a JSON Schema that describes the expected arguments. 
        It was generated based on the `RequestArguments` class we defined
    2.  Required arguments have been specified in the schema
    3.  Results is a JSON Schema describing the output of the action.
        It was generated based on the `Response` class we defined

=== "trigger_newentriestrigger.json"

    ```json
    {
      "name": "NewEntriesTrigger",
      "description": "Fetch new entries from the remote URL",
      "uuid": "acc45c1f-f203-55c2-96e7-87c534e7d2e4",
      "docker_parameters": "NewEntriesTrigger",
      "arguments": {  // (1)!
        "title": "TriggerConfiguration",
        "type": "object",
        "properties": {
          "url": {
            "title": "Url",
            "minLength": 1,
            "maxLength": 2083,
            "format": "uri",
            "type": "string"
          }
        },
        "required": [  // (2)!
          "url"
        ]
      },
      "results": {  // (3)!
        "title": "NewEntries",
        "type": "object",
        "properties": {
          "entries": {
            "title": "Entries",
            "type": "array",
            "items": {
              "$ref": "#/definitions/Entry"
            }
          }
        },
        "required": [
          "entries"
        ],
        "definitions": {
          "Entry": {
            "title": "Entry",
            "type": "object",
            "properties": {
              "id": {
                "title": "Id",
                "type": "integer"
              },
              "value": {
                "title": "Value",
                "type": "string"
              },
              "timestamp": {
                "title": "Timestamp",
                "type": "integer"
              }
            },
            "required": [
              "id",
              "value",
              "timestamp"
            ]
          }
        }
      }
    }
    ```

    1.  Arguments is a JSON Schema that describes the expected arguments. 
        It was generated based on the `TriggerConfiguration` class we defined
    2.  Required arguments have been specified in the schema
    3.  Results is a JSON Schema describing the output of the trigger.
        It was generated based on the `NewEntries` class we defined


#### Generated entrypoint

The `main.py` entrypoint file has been updated as well. It now contains our trigger and our action.

```python
from testhttp_modules import TesthttpModule

from testhttp_modules.trigger_new_entries import NewEntriesTrigger  # (1)!
from testhttp_modules.action_request import Request  # (2)!


if __name__ == "__main__":
    module = TesthttpModule()
    module.register(NewEntriesTrigger, "NewEntriesTrigger")  # (3)!
    module.register(Request, "Request")    # (4)!
    module.run()

```

1. Our trigger is imported.
2. Our action is imported.
3. Trigger is registered. The first argument of `module.register` is our action class and the second is the `docker_parameter` that is specified in our trigger's manifest.
4. Action is registered.

## Compliance Validation
This step will enable you to verify different components of the module and detect any errors. Before proceeding, ensure all test dependencies are installed by running the following command in the /_utils directory:
``` shell
poetry install 
```
To check the correctness of the module the following command should be run :

```shell
poetry run python _utils/compliance/__main__.py check --module modules\<module_name> 
```
## Homologation request 
Once you have validated your unit and integration tests, as well as ensured compliance, you can proceed with the homologation request. Refer to this [section](../develop/guides/develop_integration/#step-3-homologate-your-automation-module) in the documentation and follow the required steps.
