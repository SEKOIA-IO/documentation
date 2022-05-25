# Events

## Search

The [Events page](https://app.sekoia.io/operations/events) exposes a search capability to investigate and hunt on your events. The search queries must follow the [dork language](dork_language.md). Type your search query in the box above the list of events to find expected events.

### Fields

The Tables below detail all the fields that can be used to narrow down your search.
In addition to them, one can filter the events based on their timestamps with the `timestamp` field.

#### Action

| name | type | description |
|------|------|-------------|
| action.id | number | Action unique identifier  |
| action.name | string | Name of the action  |
| action.outcome | string | Outcome status of the action |

#### Entity

| name | type | description |
|------|------|-------------|
| entity.name | string | Name of the entity |
| entity.uuid | string | Unique identifier of the entity |

#### Event

| name | type | description |
|------|------|-------------|
| event.intake_key | string | The intake key |
| event.original | string | The original message before normalization |
| event.dialect | string | The intake format |
| event.outcome | string | The parsing status (success or failure) |

#### Error

| name | type | description |
|------|------|-------------|
| error.code | string | If ingestion failed, this field hosts the error |


#### Network

| name | type | description |
|------|------|-------------|
| network.protocol | string | L7 Network protocol name. ex. http, lumberjack, transport protocol. |
| network.transport | string | Protocol Name corresponding to the field `iana_number`. |


#### Destination

| name | type | description |
|------|------|-------------|
| destination.ip | string | IP address of the destination. (IPv4 or IPv6) |
| destination.port | number | Port of the destination |
| destination.domain | string | Destination domain |
| destination.packets | number | Packets sent from the destination to the source. |

#### Source

| name | type | description |
|------|------|-------------|
| source.ip | string | IP address of the source. (IPv4 or IPv6) |
| source.port | number | Port of the source |
| source.domain | string | Source domain |
| source.packets | number | Packets sent from the source to the destination. |


#### HTTP

| name | type | description |
|------|------|-------------|
| http.request.method | string | HTTP request method |
| http.response.status_code | string | HTTP response status code |

#### URL


| name | type | description |
|------|------|-------------|
| url.original | string | Unmodified original url as seen in the event source. |
| url.full | string | Full unparsed URL. |


#### DNS

| name | type | description |
|------|------|-------------|
| dns.question.name | string | The name being queried. |
| dns.question.type | string | The type of record being queried. |
| dns.response_code | string | The DNS response code. |

#### User

| name | type | description |
|------|------|-------------|
| user.id | string | Unique identifier of the user. |
| user.name | string | Short name or login of the user. |
| user.email | string | User email address. |

#### User Agent

| name | type | description |
|------|------|-------------|
| user_agent.original | string | Unparsed user_agent string. |

#### Process

| name | type | description |
|------|------|-------------|
| process.pid | number | Process Id |
| process.name | string | Process name |
| process.executable | string | Absolute path to the process executable. |
| process.cmdline | string | Full command line that started the process. |
| process.working_directory | string | he working directory of the process. |
| process.ppid | number | Parent process' pid. |
| process.parent.name | string | Parent process' name |
| process.parent.executable | string | Parent process' executable |


### Example

Get valid event, from November 22nd to November 23rd 2019, that are neither apache nor nginx logs:

`timestamp:>="2019-11-22" AND timestamp:<"2019-11-23" AND event.outcome:"success" AND NOT(event.dialect:"apache" OR event.dialect:"nginx")`
