# Trigger

A trigger is the entry point of a playbook. It monitors an event source and starts a playbook run when the source produces an event.

A trigger is implemented with Python code based on the Sekoia automation SDK and registered in the module entrypoint.

## Python code

Create a Python class that inherits from [`Trigger`](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/trigger.py) in the `sekoia-automation-sdk` package.

The class must define the trigger configuration and result model. Its `run` method must monitor the event source and call `send_event` when it detects an event.

The result model must describe the payload sent to the playbook.

??? example "Trigger implementation"

    ```python
    import requests
    from pydantic import BaseModel, HttpUrl
    from sekoia_automation.trigger import Trigger


    class TriggerConfiguration(BaseModel):
        url: HttpUrl


    class Entry(BaseModel):
        id: int
        value: str
        timestamp: int


    class NewEntries(BaseModel):
        entries: list[Entry]


    class NewEntriesTrigger(Trigger):
        configuration: TriggerConfiguration
        results_model = NewEntries

        def run(self):
            response = requests.get(str(self.configuration.url))
            response.raise_for_status()

            entries = [Entry(**entry) for entry in response.json()]
            self.send_event(
                event_name=f"Pushing {len(entries)} new entries",
                event=NewEntries(entries=entries),
            )
    ```

## Entrypoint registration

Declare the trigger in `main.py` at the root of the module. Import the trigger class and register it with the command name used to run the trigger.

```python
from testhttp_modules import TesthttpModule
from testhttp_modules.trigger_new_entries import NewEntriesTrigger


if __name__ == "__main__":
    module = TesthttpModule()
    module.register(NewEntriesTrigger, "NewEntriesTrigger")
    module.run()
```

## Related articles

[Automation modules](/integration/develop_integration/automation/overview.md): Overview of module structure and automation components.

[Module](/integration/develop_integration/automation/module.md): Reference for the files and entrypoint in an automation module.

[Create a module](/integration/develop_integration/automation/create_a_module.md): How to create a module with an action, connector, or trigger.

[Triggers](/xdr/features/automate/triggers.md): Overview of triggers in playbooks.
