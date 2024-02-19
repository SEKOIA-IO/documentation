# Custom format

Sekoia.io provides a list of intakes that allows you to integrate events from different sources such as systems, applications and security appliances.

Some technologies may not have an associated Intake in the official Sekoia.io catalog and therefore cannot be parsed in Sekoia.io.

The "Custom format" feature allows you to easily develop your own Intake. It gives you the tools to parse your events in the Elastic Common Schema (ECS) format to ensure agnostic detection and to index fields for search in the Events page.

!!!note
    In order to use this feature, you need to have the `SIC_WRITE_INTAKE` permission associated to your Sekoia.io account. This permission also allows you to create an existing Intake.

!!!warning
    A custom format created on a MSSP community will be available for its sub-communities.

## Overview
### Create an empty Custom format

The creation of an empty Custom format is the first step to develop your own Intake.
After that, you will be able to create an instance of this Intake and start sending your logs. No event will be parsed but you will be able to see the evolution of your parser while you are developping it.

!!!note
    Modifications of custom format will be applied in the existing intake created from the custom format.

To create an empty custom format:

1. Go to `Intakes`, `+ INTAKE` and select `Custom format`
2. Write the name of your Intake
3. Give a description for your Intake
4. Select a module. A module is linked to a taxonomy in relation with your format which will help you develop your parser. For instance, if you develop a Custom format for a Fortinet product, you will choose the Fortinet module. If your module does not exist, just write the name of your module (name of the application or compagny if they have different products) and click on `Create`
5. Select the data sources associated to your events. You can have multiple ones. Data sources can be use when you want to deploy rules.
6. Click on `Save`

![!Sekoia.io Custom format creation](/assets/operation_center/custom_format/create_custom_format.png){: style="max-width:100%}


### Panel overview
The custom format panel is structured like this:

1. Metadata information about your Intake
2. An area where you can build your Intake with `Stages`
3. A button to switch to `Expert mode` (YAML visualization of your Intake)
4. A button to display the `Taxonomy manager`
5. An area to test your Intake with an event sample.

![!Sekoia.io Custom format Panel Overview](/assets/operation_center/custom_format/panel_overview.png){: style="max-width:100%}

## Stages
A Custom format consists of a sequence of stages organized under a pipeline that modifies the event on the fly.
A stage is a parsing step that will have a specific behaviour on the event.
The goal is to define a sequence of stages that will parse your events in the ECS format.

### Custom stage

The custom stage is used to create actions. An action is an elementary operation that can `set`, `translate` or `delete` a field.
!!! Important
    While the [Common stages](#common-stages) are used to extract fields from your logs, this stage must be present in every intake to set the extracted fields in the ECS format expected by Sekoia.io.

#### Set
![!Sekoia.io Set action](/assets/operation_center/custom_format/set_action.png){: style="max-width:100%"}

This action is used to set the value of one field in the ECS format in the final version of the event.

The value corresponding to the field you want to set can either be a constant (for instance `my-constant`, `10` ...) or a reference to a field from a stage (for instance `{{stage1.message.myfield.subfield}}`).

!!! note
    If the value cannot be computed or is empty, the field is not modified.

**Example**

The JSON stage:

- Name: `parsed_json`
- Output_field: `message`

was previously used to parse the following event:
```
{'protocol':'tcp','traffic':{'source':'127.0.0.1','target':'8.8.8.8'}}
```

To put the `source` and the `target` IP in the final version of the parsed event, the `Set` action can be used:

![!Sekoia.io Set example](/assets/operation_center/custom_format/set_example.png){: style="max-width:100%"}

`source.ip` and `destination.ip` are the fields used in Elastic Common Format taxonomy.

#### Translate
![!Sekoia.io Set action](/assets/operation_center/custom_format/translate_action.png){: style="max-width:100%"}

The `Translate` action sets value of one or more fields according to the value of a source field and a dictionary that connects values.
An optional "fallback" value can be defined.
If the value of the source field does not match any entry of the mapping dictionary, the fallback value will be used to set the target field.
If no fallback value is defined and the value of the source field does not match any entries, the target field will not be created in the final event.

**Example**

You want to set the value of `http.response.status_message` according to the value `http.response.status_code` and a dictionary.
`http.response.status_code` contains only status codes values.

You can define a `Translate` action with the following parameters:
![!Sekoia.io Set action](/assets/operation_center/custom_format/translate_example.png){: style="max-width:100%"}

#### Delete
![!Sekoia.io Delete action](/assets/operation_center/custom_format/delete_action.png){: style="max-width:100%"}

The `Delete` action allows you to delete fields in the final version of the event.

**Example**

The following action will delete the fields `source.ip` and `destination.ip` from the final event.
![!Sekoia.io Delete action](/assets/operation_center/custom_format/delete_example.png){: style="max-width:100%"}

### Common stages
Common stages are provided by Sekoia.io to help you parse your events. There are currently 5 different common stages, each having its specifities:

- [Json](#json-stage)
- [Date](#date)
- [Delimiter Separeted Value](#delimiter-separated-values)
- [Grok](#grok)
- [Key-Value](#key-value)

#### JSON Stage

![!Sekoia.io Json stage](/assets/operation_center/custom_format/json_stage.png){: style="max-width:100%"}

The JSON stage can be used to deserialize a JSON from a string.

You will need to provide the stage with:

- A `Name`
- A `Description` (optional)
- An `Input_field` - As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your logs will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
- An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a JSON field.

**Example**

- Generic

In the following event, a JSON is present in the `message` field. The JSON stage can be used to get all the information you need.

```json
{
  "protocol":"tcp","traffic":{"source":"127.0.0.1","target":"8.8.8.8"}
}
```

To get the reference of the source IP in another stage, we will use the reference `{{stage1.message.traffic.source}}`

    - `stage1` is the name of the JSON stage
    - `message` is the name of the `Output_field`
    - `traffic.source` is the field we want in the JSON

- field with '-'

We would like to parse `rules-match` of the following event:

```json
{
"protocol":"tcp","traffic":{"source":"127.0.0.1","target":"8.8.8.8","rules-match":"rule1"}
}
```

To get the reference of the `rules-match` in another stage, we will use the reference `{{stage1.message.get('rules-match')}}`

    - `stage1` is the name of the JSON stage
    - `message` is the name of the `Output_field`
    - `rules-match` is the field we want in the JSON
    - `get('<field>')` needs to be added


#### Key Value
![!Sekoia.io Key Value stage](/assets/operation_center/custom_format/kv_stage.png){: style="max-width:100%"}

The Key-Value stage can be used to deserialize a Key-Value string.
You will need to provide the stage with:

 - A `Name`
 - A `Description` (optional)
 - An `Input_field` -  As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a value corresponding to a key.
 - A `Value Separator` - It is the separator that differentiates the key from the value. It it set to `=` by default.
 - An `Item Separator` - It is the separator that differentiates two different key-value. The default separator is `\s` which means a whitespace character.

**Example**

In the following event, a key-value string is present in the `message` field. The Key-Value Stage can be used to get all information we need.

```
to=john.doe@example.com, relay=mail.isp.com, delay=xxx, delays=xxx, dsn=2.0.0, status=sent (250 2.0.0 OK)
```

With `Value Separator: "="` and `Item Separator: ",\s"`, the log can be parsed. For example, to get the relay value, we will use the reference `{{stage1.message.relay}}`

- `stage1` is the name of the Key-Value stage
- `message` is the name of the `Output_field`
- `relay` if the key corresponding to the value we want

#### Grok
![!Sekoia.io Grok stage](/assets/operation_center/custom_format/grok_stage.png){: style="max-width:100%"}

The Grok stage can be used to match a field against a Grok pattern. Grok is a tool provided by Elasticsearch that gives you the ability to parse an arbitrary string and structure it.
You can find more information about Grok in the [official documentation](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html).
The list of all the Grok patterns that can be used can be found [here](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns).

You will need to provide the stage with:

- An `Input_field` -  As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
- An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a value corresponding to a key.
- A `Pattern` - It is the Grok pattern you want to apply.
- A `Custom Patterns` - If no Grok pattern satisfies you in this [list](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns), you can create your own custom patterns with the `+` button on the right of the line. Then, on the left column, write the name of your pattern. On the right column, write the regex corresponding to that pattern.

**Example 1**

![!Grok custom pattern](/assets/operation_center/custom_format/grok_custom_pattern.png)
In this example, the pattern `SSHD_MESSAGE_ILLEGAL_USER` will match the strings `Illegal user` or `illegal user`.


**Example 2**

In the following event, a Grok Stage can be used to parse the event.

```
64.3.89.2 took 300 ms
```

If you want to parse the IP and the time in milliseconds, the following Pattern can be used:
`%{IP:client} took %{NUMBER:duration} ms`

To get the IP in a next stage, you can use the reference `{{stage1.message.client}}`.
To get the duration, you can use `{{stage1.message.duration}}`.

!!! note
    The pattern should take into account every singe character of your event, from the first one to the last one.

#### Date
![!Sekoia.io Date stage](/assets/operation_center/custom_format/date_stage.png){: style="max-width:100%"}


The Date stage can be used to parse a date field. The output of this stage is a date normalized in ISO 8601, which is the format used by Sekoia.io. This stage accepts, as optional properties, the format to parse the date and the IANA timezone of the parsed date.

You will need to provide the stage with:

 - A `Name`
 - A `Description` (optional)
 - An `Input_field` - As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field.
`original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get the output value.
 - A `Format` (optional) - You can specify the format of the date. By default, the stage tries to autodetect the format.
 - A `Timezone` (optional) - You can specify the timezone of the date. It is set to `UTC` by default.

**Example**

In the following event, a Date stage can be used to parse the field.

```
May 21, 2021 at 11:04:35
```

You can configure the stage as follow:

- Input_field: `{{original.date}}`
- Output_field: `date`
- Format: `%MMM %dd, %yyyy at %hh:%mm:%ss`
- Timezone: `UTC`

To get the date parsed in a next stage, you will then use the reference `{{stage1.date}}`. The output will be `2021-05-21T11:04:35Z` (ISO 8601).


#### Delimiter Separated Values
![!Sekoia.io DSV stage](/assets/operation_center/custom_format/dsv_stage.png){: style="max-width:100%"}

The Delimiter Separated Values stage can be used to extract values from a delimiter-separated values string. This stage needs the list of columns and, as optional, the delimiter (by default, the delimiter is the comma ',').

You will need to provide the stage with:

 - A `Name`
 - A `Description` (optional)
 - An `Input_field` - As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field.
`original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a value corresponding to a key.
 - A `Column Names` - You need to list the column names used to retrieve information. The format has to be the following : `<column_A>,<column_B>,<column_C>...`
 - A `Delimiter` - The delimiter used to differenciate two columns (By default `,`).

**Example**

In the following event, a DSV stage can be used to parse the `message` field.

```
2020/12/04 16:47:48;LOGIN;jenkins;2305
```

You can configure the stage as follow:

- Input_field: `{{original.message}}`
- Output_field: `message`
- Column Names: `date;action;username;user_id`
- Delimiter: `;`

To get for instance the `user_id` in a next stage, you can use `{{stage1.message.user_id}}`

## Filters

Reference to a field can be extended with filters.
Filters are separated from the field path by a pipe symbol (|).
Multiple filters can be chained.

**Example**

`{{stage1.message.type | strip | upper}}` removes the whitespace and returns the uppercase value of the field `type` computed in `stage1`.

The following built-in filters are available:

| filter       |  description
|---------------|------------------------------------------------
|`abs`          | returns the absolute value of the variable.
|`capitalize`   | returns the first character uppercase, all others lowercase.
|`float`        | converts the variable in float
|`int`| converts the value as an integer
|`string` | converts the value as a string
|`length`| returns the number of items
|`lower`| returns the value all lowercase
|`max`| returns the largest item from the variable
|`min`| returns the smallest item from the variable
|`strip`| returns the variable removed from heading and leading whitespaces
|`upper`| returns the value all uppercase

## Conditions
The structure of events often varies depending on certain conditions such as the type of data (network, audit, security...) and it can be interesting to set up stages that only run when certain conditions are met.
This feature is called `Filter` too but applies to a block. It should not be confused with [filters](#filters) that apply to a specific field.

**Example**

To run the stage `set_stage` when the value of the `type` field is equal to `network`, you can use this filter:
![!Sekoia.io Condition example](/assets/operation_center/custom_format/conditions_example.png)


## Taxonomy manager
A taxonomy is a hierarchical schema used to normalize events. The taxonomy used by Sekoia.io is the ECS standard (Elastic Common Schema).
The taxonomy manager allows you to view all the ECS fields available with their description.
If a field in an event is custom to the technology and cannot be placed in any field of the ECS standard, you can create your own field.
!!! note
    By convention, the name of the field must start with the name of your intake followed by the field name.

**Fields type available:**
- `Keyword`: corresponds to a string
- `Long`: corresponds to a numeric value
- `Date`: corresponds to a date in ISO8601 format
- `Geo_point`: corresponds to gelocalisation in Longitude and Latitude format (e.g. `POINT (48.8705 2.3052)`)

!!! note
    Keyword is the broadest type and can be used for most case.
    Therefore, we recommend to use the type according to the field format.

**Example**

The product `technoexample` has a field called `environment` which is custom to this technology and does not exist in ECS. With the taxonomy manager, you can create a custom field
`technoexample.environment`. This field will then be available in the [Custom Stage](#custom-stage)
![!Sekoia.io Taxonomy custom field](/assets/operation_center/custom_format/taxonomy_custom_field.png)

## Practical example
You now have all the knowledge to start developing your custom Intake! To deepen your knowledge, you can follow the example below that uses the different notions explained before.

### Context
Let's suppose you want to develop a Custom format for a firewall solution. This firewall creates two types of events:

- Traffic events
- Audit events (When a user logs in to the device)

Traffic events are structed like this:
```bash
traffic logs: {"date": "1651507525", "traffic": {"sourceip": "1.1.1.1", "destinationip": "2.2.2.2", "srcport": 50436, "dstport": 443}}
```

Audit events are structured like this:
```bash
audit logs: {"date": "1651507525", "username": "john", "role": "administrator", "status": "connect"}
```

### Solution
* The first thing you can see is that the two types of events look the same but the keys used in the JSON are different.
* You can also notice that the first word identifies the type of event (traffic or audit).
* And finally you can see that each type of event contains a key `date` containing the date of the event in epoch format (The Unix epoch is the number of seconds that have elapsed since January 1, 1970 at midnight UTC).

For our Intake, we will need :

- a `JSON` stage to parse the JSON
- a `Grok` stage to parse the start of each event and identify the type (Audit or Traffic)
- At least one `Date` stage to parse to `date` field in epoch format and converts it in ISO 8601

Let's get into it!

#### Identify the type of event
To identify the type, we can use a `Grok` stage with the following pattern:
`^%{WORD:type} logs: %{DATA:jsondata}$`
![!Sekoia.io Solution Grok stage](/assets/operation_center/custom_format/exercice_grok_stage.png){: style="max-width:100%"}

This pattern will extract :

- The "type" in the field `{{parse_type.message.type}}`
- The "JSON" in the field `{{parse_type.message.jsondata}}`


#### Parse the JSON

To parse the JSON, we will use a `JSON` stage:
![!Sekoia.io Solution JSON stage](/assets/operation_center/custom_format/exercice_json_stage.png){: style="max-width:100%"}

#### Parse the date of the event

To parse the date of the event, we will use a `Date` stage:
![!Sekoia.io Solution Date stage](/assets/operation_center/custom_format/exercice_date_stage.png){: style="max-width:100%"}

#### Set the fields in ECS for traffic logs

Now that everything is parsed, we can use a "Custom stage" to set the values in ECS for traffic logs:
![!Sekoia.io Solution set traffic stage](/assets/operation_center/custom_format/exercice_set_traffic.png){: style="max-width:100%"}

#### Set the fields in ECS for audit logs

We can use a custom stage to set the values in ECS for audit logs:
![!Sekoia.io Solution set audit stage](/assets/operation_center/custom_format/exercice_set_audit.png){: style="max-width:100%"}

### Results

With the `Test your parser` feature, you can see the results.

**Traffic event**:
![!Sekoia.io Solution result traffic](/assets/operation_center/custom_format/exercice_result_traffic.png){: style="max-width:60%"}

**Audit event**:
![!Sekoia.io Solution result audit](/assets/operation_center/custom_format/exercice_result_audit.png){: style="max-width:60%"}
