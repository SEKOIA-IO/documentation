# Create a Module

In this section we will see how to develop a simple module from scratch.

A module can contain several components of the following types:

* **Action**: custom code executed by Sekoia in a Playbook.
* **Connector**: custom code executed by Sekoia to collect and ingest events.
* **Trigger**: custom code executed by Sekoia as an entrypoint of a Playbook.


## Technical Requirements

!!! note
    The SDK needs a Python version equal or newer to 3.11.
    You can check the installed version on your system with the command `python -V`.

If not already done, install the Sekoia's automation SDK. This SDK contains various command line utilities that will help us manage modules. Simply run the following command:
```shell
pip install sekoia-automation-sdk
```

If you previously installed Sekoia's automation SDK, please make sure you are running the latest version by using this command:
```shell
pip install --upgrade sekoia-automation-sdk
```

## Initialize the module

Once the SDK is installed we can use it to create an empty module:

``` shell
sekoia-automation new-module .
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

Our connector, trigger, and action will use the `requests` library to send HTTP requests.
The first step is to add this package to our requirements.

Poetry can be used to add the requirements by simply running in the `TestHTTP` root directory:

```shell
cd TestHTTP
poetry add requests
```

As a result you should see the `requests` package added in the dependencies section of the `pyproject.toml` file. 

### Add a .gitignore file to ignore temporary files

Open your terminal or command prompt and navigate to the root folder containing your module. Once you're in the correct folder, run the following command:

```shell
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
```

## Sync your module code with Github

In order to import your custom module in Sekoia, you need to store it in a Github or GitLab instance accessible by Sekoia platform.
In this documentation we give examples with GitHub, but this can be easily adapted with GitLab following their documentation.

**Step 1: Create a new GitHub repository**

First, you'll need a new repository on GitHub to push your code to. Go to github.com, log in, and click the **"+"** icon in the top right corner, then select New repository.
Give your repository a name and an optional description.
!!! note
    Do not initialize it with a README, .gitignore, or license file. A blank repository is crucial for this method.

Once created, GitHub will show you a page with instructions on how to connect your local repository.

**Step 2: Initialize Git in your local folder**

Run the following command to initialize a new Git repository:
```shell
git init
```
This creates a hidden `.git` directory in your folder, which tracks all changes.

**Step 3: Add and commit your files**

Now, you need to stage and commit your files. Staging is the process of telling Git which files you want to include in your next commit. Add all files in the current directory with this command:
```shell
git add .
```

After adding the files, you need to create a commit, which is like a snapshot of your project at a specific point in time. The -m flag lets you add a short, descriptive message to your commit:
```shell
git commit -m "Initial commit of module TestHTTP"
```

**Step 4: Link your local repository to GitHub**

Next, you need to connect your local Git repository to the remote one you created on GitHub. Use the URL of your new GitHub repository, which you can find on the repository's main page. Run the following command, replacing [URL] with your repository's URL:
```shell
git remote add origin [URL]
```
For example: `git remote add origin https://github.com/your-username/your-repo-name.git`

**Step 5: Push your code to GitHub**

Finally, push your committed changes from your local machine to the `main` branch of your GitHub repository. The `-u` flag sets the upstream branch, so you can just use `git push` in the future.
```shell
git push -u origin main
```
You may be prompted to enter your GitHub username and password or a Personal Access Token (PAT). Once the push is complete, your code will be live on GitHub.


## Create your component

Depending on your needs, you can choose to create an **Action**, a **Connector**, or a **Trigger**. Each section below provides detailed instructions for implementing the respective component. Select the one that best fits your use case and follow the steps provided.

=== "Action"
    Our action will take three arguments:

    * The URL to query
    * The HTTP method to use
    * The HTTP headers to provide

    Two of those arguments will be required, the URL and the method.

    The result of our action will contain:

    * The status code
    * The response body as text
    * The response headers

    **Add the code**

    Now that we have a manifest describing our action we can add the code!

    Inside our Python package `testhttp_modules` we can create a new file `action_request.py` that will contain the logic of our action:

    ```python
    from typing import Literal

    from pydantic.v1 import BaseModel, HttpUrl
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

    **Generate the manifest and entrypoint**

    Now that the code has been created, generate the manifest and update the entrypoint by calling

    ```shell
    sekoia-automation generate-files-from-code
    ```

    **Generated manifest**

    The previous step generated the following manifest file for us:

    * `action_request.json` describing the action

    We can edit the manifest to add a description:

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



    **Generated entrypoint**

    The `main.py` entrypoint file has been updated as well. It now contains our action.

    ```python
    from testhttp_modules import TesthttpModule

    from testhttp_modules.action_request import Request  # (1)!


    if __name__ == "__main__":
        module = TesthttpModule()
        module.register(Request, "Request")    # (2)!
        module.run()

    ```

    1. Our action is imported.
    2. Action is registered.


=== "Connector"
    A connector is a Python code file executed by Sekoia to collect and ingest events.
    In this example the connector will regularly pull an external API and ingest the received events in Sekoia.

    The main logic is presented here:

    ```python
    import time
    from sekoia_automation.connector import Connector

    # Our connector inherits from the Connector class of the sekoia automation sdk
    class TesthttpConnector(Connector):

        # The run method is called by Sekoia when launching the connector
        def run(self) -> None:
            # The log method is used to trace logs in the Connector logs of the Sekoia interface
            self.log(message="Start fetching events", level="info")

            # Iterate until the Connector is shut down by Sekoia
            while self.running:
                # Complete with your custom code collecting events
                collected_events = []
                ...

                # Ingest the collected events in Sekoia
                self.push_events_to_intakes(events=collected_events)

                # Wait 60s before collecting the next batch of events
                time.sleep(60)
    ```

    Additionaly, you can define parameters that will be set during the instanciation of the Intake in Sekoia. For that you have 2 options depending of the type of parameter you want to define.

    * **Option 1**: Define parameters in the Module

    Defining a parameter in the module is useful if the parameter is reused between several components of the module, such as between the connector and other actions.
    This is where we typically define *API credentials* and *API Base URLs*.

    Once set these parameters can be seen and modified in the `Connected accounts` menu of the Integration and Playbooks pages in Sekoia.

    * **Option 2**: Define parameters in the Connector

    In that case the parameter is only accessible by the connector, and not by the other components of the module. This is where we define connector specific settings, such as the *connector polling frequency*.

    Once set these parameters can be seen and modifed in the `Configure` option in the Intake page in Sekoia.

    In the next example we will use both options for our connector.

    **Add the example code**

    To create the parameter `api_key` in the module, modify the file named `models.py` located in the  `testhttp_modules` directory with the following content:
    ```python
    from pydantic.v1 import BaseModel, Field


    class TesthttpModuleConfiguration(BaseModel):
        api_key: str = Field(..., description="API Key", secret=True)
    ```

    The `api_key` parameter is a required string. The `...` (ellipsis) signifies that a value for this field must be provided. `secret=True` ensures its value isn't exposed in logs,
    and `description` provides a helpful explanation.

    To create the connector, create a new file named `connector.py` in the `testhttp_modules` directory.

    Copy and paste in this file the following code:
    ```python
    import json
    import time
    from pydantic.v1 import Field
    from sekoia_automation.connector import Connector, DefaultConnectorConfiguration
    import requests

    from . import TesthttpModule


    class TesthttpConnectorConfiguration(DefaultConnectorConfiguration):
        polling_interval: int = Field(5, description="Polling interval in minutes")


    class TesthttpConnector(Connector):
        module: TesthttpModule
        configuration: TesthttpConnectorConfiguration

        def run(self):
            self.log(message="Start fetching events", level="info")

            while self.running:
                self.log("Polling Testhttp API...", level="info")

                # Fetch data from the Testhttp API
                data = []
                try:
                    response = requests.get(
                        "https://jsonplaceholder.typicode.com/posts",
                        headers={"Authorization": f"Bearer {self.module.configuration.api_key}"},
                    )
                    response.raise_for_status()
                    data = response.json()
                except requests.RequestException as error:
                    self.log_exception(error, message="Error fetching data from Testhttp API")

                # Process collected data (if needed)
                batch_of_events = []
                for item in data:
                    item["source"] = "testhttp"
                    batch_of_events.append(json.dumps(item))
                
                # Push events to Sekoia platform
                if batch_of_events:
                    self.log(
                        message=f"{len(batch_of_events)} events collected",
                        level="info",
                    )
                    self.push_events_to_intakes(events=batch_of_events)

                # Wait for the next polling interval
                time.sleep(self.configuration.polling_interval * 60)
    ```

    **Generate the manifest and entrypoint**

    Now that the code has been created, generate the manifest and update the entrypoint by calling

    ```shell
    sekoia-automation generate-files-from-code
    ```

    **Generated manifest**

    The previous step generated the following manifest file for us:

    * `connector_testhttpconnector.json` describing the connector

    We can edit the manifest to customize the description:

    ```json
    {
      "name": "TesthttpConnector",
      "description": "TesthttpConnector",
      "uuid": "8a7acb0b-0004-5e17-9ab0-4c110cea795b",
      "docker_parameters": "TesthttpConnector",
      "arguments": {  // (1)!
        "title": "TesthttpConnectorConfiguration",
        "type": "object",
        "properties": {
          "intake_server": {
            "title": "Intake Server",
            "type": "string"
          },
          "intake_key": {
            "title": "Intake Key",
            "type": "string"
          },
          "polling_interval": {
            "title": "Polling Interval",
            "description": "Polling interval in minutes",
            "default": 5,
            "type": "integer"
          }
        },
        "required": [  // (2)!
          "intake_key"
        ]
      }
    }
    ```

    1.  Arguments is a JSON Schema that describes the expected arguments. 
        It was generated based on the `TesthttpConnectorConfiguration` class we defined
    2.  Required arguments have been specified in the schema


    **Generated entrypoint**

    The `main.py` entrypoint file has been updated as well. It now contains our connector.

    ```python
    from testhttp_modules import TesthttpModule

    from testhttp_modules.connector import TesthttpConnector  # (1)!


    if __name__ == "__main__":
        module = TesthttpModule()
        module.register(TesthttpConnector, "TesthttpConnector")  # (2)!
        module.run()

    ```

    1. Our connector is imported.
    2. The connector is registered.


=== "Trigger"
    Our trigger will take one argument, the URL that exposed the objects we want to handle with our module.
    This argument will be required.

    **Add the code**

    Inside our Python package `testhttp_modules` we can create a new file `trigger_new_entries.py` that will contain the logic of our trigger:

    ```python
    import time

    from pydantic.v1 import BaseModel, HttpUrl
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

    **Generate the manifest and entrypoint**

    Now that the code has been created, generate the manifest and update the entrypoint by calling

    ```shell
    sekoia-automation generate-files-from-code
    ```

    **Generated manifest**

    The previous step generated the following manifest file for us:

    * `trigger_newentriestrigger.json` describing the trigger

    We can edit the manifests to add a description:

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

    1. Arguments is a JSON Schema that describes the expected arguments. 
        It was generated based on the `TriggerConfiguration` class we defined
    2. Required arguments have been specified in the schema
    3. Results is a JSON Schema describing the output of the trigger.
        It was generated based on the `NewEntries` class we defined


    **Generated entrypoint**

    The `main.py` entrypoint file has been updated as well. It now contains our trigger.

    ```python
    from testhttp_modules import TesthttpModule

    from testhttp_modules.trigger_new_entries import NewEntriesTrigger  # (1)!


    if __name__ == "__main__":
        module = TesthttpModule()
        module.register(NewEntriesTrigger, "NewEntriesTrigger")  # (2)!
        module.run()

    ```

    1. Our trigger is imported.
    2. Trigger is registered. The first argument of `module.register` is our action class and the second is the `docker_parameter` that is specified in our trigger's manifest.



## Test your code (optional)

Writing tests is optional, but it is considered a good practice to ensure your module works as expected and to catch potential issues early. In this section, we will test the `get request` action from our previous example.

In the `tests/` directory, create a test file named `test_action_request.py`. This file will contain the tests for our action.

While this example focuses on a single action, you should aim to write comprehensive unit and integration tests to cover all edge cases and expected behaviors of your module.

```python
import pytest
import requests_mock
from testhttp_modules.action_request import RequestArguments, Request, Response

def test_get_request(requests_mock):
  # Mock the HTTP response
  mock_response = {
      'status_code': 200,
      'headers': {'Content-Type': 'application/json'},
      'text': 'Success'
  }
  requests_mock.get('http://example.com', status_code=mock_response['status_code'],
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

  # Interprete the dict correctly if the response is serialized to a dict:
  if isinstance(result, dict):
      result = Response(**result)

  # Assert the response
  assert isinstance(result, Response)
  assert result.status_code == mock_response['status_code']
  assert result.headers['Content-Type'] == mock_response['headers']['Content-Type']
  assert result.text == mock_response['text']
```

To effectively manage dependencies and run your tests, you should use Poetry: 

```shell
poetry run pytest -v -s tests/
```
For more detailed information, you can check the [Poetry documentation](https://python-poetry.org/docs/). Additionally, you can look at the tests in the existing module.

## Deploy your module

To deploy your module, you first need to make sure the module version is unique and has not already been imported in Sekoia.
To update the module version, you must edit the `version` parameter in both the `manifest.json` file and the `CHANGELOG.md` file to ensure they match.
It is recommended to use semantic versioning (e.g., `1.0.1`) for your module versions to maintain consistency and traceability.

Then make sure all your code, including any untracked files, is staged and committed in git, as Sekoia will import the code from there.
To do so, proceed as follows:

1. Open your terminal and navigate to your module's root directory.
2. Stage all files for commit:
  ```shell
  git add .
  ```
3. Commit your changes with a descriptive message:
  ```shell
  git commit -m "Finalize module for Sekoia import"
  ```
4. Push your code to the remote repository:
  ```shell
  git push
  ```

Your latest code will now be available in GitHub or GitLab for Sekoia to import.

Once your code is finalized and available in GitHub or GitLab, go to the Integrations page in the Sekoia platform and click on **"Import my custom integration"**, then follow the steps given to import your code from your Github or Gitlab repository.

## Homologate your module (optional)

To publish a new automation in the Sekoia.io integration catalog, you must follow the homologation process. This process ensures that your automation is compliant with Sekoia's standards and can be used effectively by the community.

### Compliance Validation

This step will enable you to verify different components of the module and detect any errors. Before proceeding, ensure all test dependencies are installed by running the following command in the /_utils directory:
``` shell
poetry install 
```
To check the correctness of the module the following command should be run :

```shell
poetry run python3 compliance check --module modules\<module_name> 
```

### Homologation request 

Once you are done developing and testing your automation, the last step is to request an homologation to Sekoia. Once your automation is homologated, it will appear in the playbook library of **Sekoia SOC platform**:

- Create a pull request
- Send an email to [homologation-request@sekoia.io](mailto:homologation-request@sekoia.io) with the pull request link
- You will get an acknowledgement from Sekoia Integration team
- In the following days (5 days max), you will receive feedbacks in your pull request that you must take into account
- Once all feedbacks are taken into account, Integration team will **validate** your pull request

The homologation process is now finished.
