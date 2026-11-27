# Build an event connector

An event connector collects events, such as logs, alerts and audit trails, from a product, and sends them to an intake of Sekoia. The [format](../formats/overview.md) of the intake then parses them. This page explains how an event connector runs, how to write one, and how to keep it from losing or duplicating events.

For the difference with an asset connector, see [Connectors](connectors.md).

## How an event connector runs

An event connector is a Python class based on [`Connector`](https://github.com/SEKOIA-IO/sekoia-automation-sdk/blob/main/sekoia_automation/connector/__init__.py) from [sekoia-automation-sdk](https://github.com/SEKOIA-IO/sekoia-automation-sdk). When you implement `iterate()`, the SDK runs it in cycles:

1. The SDK calls `iterate()`, which yields lists of events, each with the date of the most recent event of the list.
2. The SDK pushes each list to the intake.
3. When the cycle yielded no event, the connector waits until `frequency` seconds have passed since the start of the cycle. When it yielded events, the next cycle starts at once.

Because a cycle that yields events is followed at once by another one, `iterate()` must yield only the events that are newer than the checkpoint. See [Save progress with a checkpoint](#save-progress-with-a-checkpoint).

You can also override `run()` and write the loop yourself, as in the **Event connector** tab of [Create a module](create_a_module.md#create-your-component). Prefer `iterate()`: the SDK then handles the waits and errors, and reports the volume and the lag of the connector.

## Declare the event connector

An event connector belongs to a module, next to its actions, triggers and asset connectors. See [Create a module](create_a_module.md) for the module itself.

### Configuration

The credentials of the product go in the `configuration` of the module [manifest](module.md#the-manifest), so that every component of the module can use them.

The settings of the connector go in a configuration class based on `DefaultConnectorConfiguration`. It already declares:

| Argument | Description |
|---|---|
| `intake_key` | The key of the intake that receives the events. Sekoia sets it when a user creates the intake. |
| `intake_server` | The URL of the intake server. Leave it empty to use the default one. |

Add the settings the user can change, such as the frequency of the queries:

```python
from pydantic import Field
from sekoia_automation.connector import DefaultConnectorConfiguration


class TesthttpEventsConfiguration(DefaultConnectorConfiguration):
    frequency: int = Field(60, description="Seconds between two queries of the API")
```

### Manifest and entrypoint

Unlike an asset connector, the manifest of an event connector is generated from the code. Run:

```shell
sekoia-automation generate-files-from-code
```

The command writes `connector_<class name>.json` at the root of the module, with the `arguments` built from the configuration class, and registers the connector in `main.py`. Edit the `name` and `description` of the manifest so that users understand what the connector collects. Never change its `uuid` once the connector is released.

## Write the event connector

The following connector collects the events of the TestHTTP API and only fetches the events created since its previous run:

```python
from collections.abc import Generator
from datetime import UTC, datetime, timedelta

import requests
from pydantic import Field
from sekoia_automation.checkpoint import CheckpointDatetime
from sekoia_automation.connector import Connector, DefaultConnectorConfiguration

from testhttp_modules import TesthttpModule


class TesthttpEventsConfiguration(DefaultConnectorConfiguration):
    frequency: int = Field(60, description="Seconds between two queries of the API")


class TesthttpEventsConnector(Connector):
    module: TesthttpModule
    configuration: TesthttpEventsConfiguration

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.checkpoint = CheckpointDatetime(  # (1)!
            path=self.data_path,
            start_at=timedelta(hours=1),
            ignore_older_than=timedelta(days=7),
        )

    @property
    def frequency(self) -> int:  # (2)!
        return self.configuration.frequency

    def iterate(self) -> Generator[tuple[list[dict], datetime | None], None, None]:
        since: datetime = self.checkpoint.offset
        response = requests.get(
            "https://testhttp.example.com/api/events",
            headers={"Authorization": f"Bearer {self.module.configuration.api_key}"},
            params={"created_after": since.isoformat()},
            timeout=60,
        )
        response.raise_for_status()  # (3)!

        events = response.json()
        if not events:
            return

        most_recent = max(datetime.fromisoformat(event["created_at"]) for event in events)
        yield events, most_recent.astimezone(UTC).replace(tzinfo=None)  # (4)!

        self.checkpoint.offset = most_recent  # (5)!
```

1. The checkpoint is stored in the data directory of the connector. On the first run, the connector starts one hour ago. After a long interruption, it does not go back further than seven days.
2. `frequency` is `0` in `Connector`. Override it, or the connector queries the API without pause when there is nothing new.
3. An error of the API stops the cycle. The checkpoint does not move, so the next cycle fetches the same events again.
4. The SDK pushes the events, then computes the lag of the connector from this date. Give it in UTC, without a time zone.
5. The checkpoint moves only after the SDK has pushed the events.

The example reads one page. When the API paginates, yield each page as you read it, so that the connector does not keep the whole result in memory, and move the checkpoint once the last page has been pushed.

### Use an asynchronous client

When the client of the product is asynchronous, base the connector on `sekoia_automation.aio.connector.AsyncConnector` and implement `async_iterate()` instead of `iterate()`. It yields the same tuples.

## Push events

`push_events_to_intakes()` sends events to the intake. The SDK calls it for you with the events that `iterate()` yields. Call it yourself only when you override `run()`.

- **Event types.** An event is a string, a dictionary or a Pydantic model. The SDK serializes dictionaries and models to JSON.
- **Batches.** The SDK groups the events into batches of about 9 MB and sends them in parallel. Do not batch them yourself.
- **Event size.** The SDK drops each event larger than 250 kB and logs how many it dropped. Remove the large fields you do not need before you yield an event.
- **Retries.** When a push fails, the SDK retries the batch for up to one hour, then logs an error and drops it.

## Save progress with a checkpoint

A checkpoint is the point up to which the connector has collected events, such as the date of the most recent event it has sent. It lets the connector restart where it stopped, after a cycle or after a restart.

The SDK provides three checkpoints in `sekoia_automation.checkpoint`:

| Class | Use it when the API filters events on |
|---|---|
| `CheckpointDatetime` | A date |
| `CheckpointTimestamp` | A Unix timestamp, in seconds, milliseconds or nanoseconds |
| `CheckpointCursor` | A cursor or an opaque offset |

Each one stores its value in a `context.json` file. When the connector stores other values with `PersistentJSON`, use another file name.

The checkpoint decides whether events are lost or duplicated:

- **Move the checkpoint after the push, not before.** If the connector stops between the two, it sends the same events again on the next run instead of skipping them.
- **Use the date of the most recent event, not the current time.** An event the product indexes late is otherwise skipped.
- **Handle events that share the date of the checkpoint.** When the API filters with "after or equal", the last events of a cycle come back at the next one. Keep their identifiers and skip them.
- **Keep the checkpoint format across versions.** When you rename a key or change the format of a date, read the old value and convert it. A lost checkpoint restarts the collection from `start_at`.

## Handle errors

- **Let errors of the API raise.** When `iterate()` raises, the SDK logs the error, waits `frequency` seconds and starts a new cycle. Do not catch and silence these errors: the logs of the connector are where users see why it fails.
- **Skip the events you cannot read, but log them.** One malformed event must not stop the collection of the others.
- **Never log the credentials** of the product, nor the content of the events.
- **Expect quiet periods.** When a connector sends no event for 6 hours, Sekoia considers it stuck and restarts it. For a product that produces few events, set the `seconds_without_events` attribute of the connector to a longer period.

## Test the event connector

Test at least:

- The parsing of a sample of the API, with anonymised data.
- Pagination, including an empty page.
- The checkpoint: a second run sends only the new events, and an event that shares the date of the checkpoint is sent once.
- An error of the API of the product.

## Example

The [automation library](https://github.com/SEKOIA-IO/automation-library) contains the event connectors of every built-in integration. For instance, the [Upwind](https://github.com/SEKOIA-IO/automation-library/blob/develop/Upwind/upwind/upwind_detections_connector.py) connector uses `iterate()`, a `CheckpointDatetime`, and keeps the identifiers of the events that share the date of the checkpoint.

## Related articles

- [Connectors](connectors.md): Choose between an event connector and an asset connector.
- [Create a module](create_a_module.md): Set up a module and its components.
- [Intake formats](../formats/overview.md): Parse the events your connector sends.
- [Build an asset connector](asset_connector.md): Collect assets instead of events.
