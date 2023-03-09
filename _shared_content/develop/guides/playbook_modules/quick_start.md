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

### Add the code

Now that we have a manifest describing our action we can add the code!


#### Specify the requirements

Our action is going to use `requests` to send HTTP requests, so the first step is to add the package in our requirements.

Poetry can be used to add the requirements by simply running:

```
poetry add requests
```

!!! note
    If poetry is not installed on your system you may need to run `pip install poetry` before.


#### Create the action

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

1. We import the base `Action` class from the SEKOIA.IO automation SDK
2. Define the expected arguments using the `Pydantic` lib
3. Define the format of the response using the `Pydantic` lib
4. Our action is a class that inherit from `Action`, a base class from SEKOIA.IO's automation SDK.
5. The child actions must define the `run` method that will be passed the arguments provided to the action
6. The base `Action` class provides few helpers like the `log` method. This method makes sure the log is sent to the API so when checking the run of the action we can see a trace of what happened.
7. The `error` method will mark the action as failed and send back the error to the API.
8. Finally if everything went well we can return the results. The base action will take care of sending it back to the playbook API.

### Generate the manifest and update the entrypoint

Now that the code has been created we can generate the manifest and update the entrypoint by calling

```
sekoia-automation generate-files-from-code
```

!!! note
    The command must be executed from the root of the module or we can provide the path to the module as argument

### Update the manifest

The previous step generated an `action_request.json` manifest file for us.
We can edit the manifest to add a description:

```json
{
  "name": "Request URL",
  "uuid": "429e8715-fdde-4064-b8e8-96e408917d25",
  "description": "Requests a resource at a specified URL and returns the response",
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


#### Generated entrypoint

The `main.py` entrypoint file has been updated as well. It now contains our action.

```python
from testhttp_modules import TesthttpModule

from testhttp_modules.action_request import Request  # (1)!


if __name__ == "__main__":
    module = TesthttpModule()
    module.register(Request, "Request")  # (2)!
    module.run()
```

1. Our action is imported
2. Action is registered. The first argument of `module.register` is our action class and the second is the `docker_parameter` that is specified in our action's manifest.

That's it! Now we have a module containing our action and ready to run !