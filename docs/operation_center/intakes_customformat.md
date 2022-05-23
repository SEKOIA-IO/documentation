# Custom format

SEKOIA.IO provides a list of intakes that allows you to integrate events from different applications and security appliances.

Some technologies may not have an associated Intake and therefore cannot be parsed in SEKOIA.IO

The Custom format feature allows you to easily develop your own Intake. It gives you the tools to parse your events in the Elastic Common Schema (ECS) format to ensure agnostic detection and to index fields for search in the event page.

!!!note
    In order to use this feature, you need to have the `SIC_WRITE_INTAKE` permission associated to your SEKOIA.IO account. This is also this permission that allows you to create an existing Intake. 

## Overview
### Create an empty Custom format

The creation of an empty Custom format is the first step to develop your own Intake.
After that, you will be able to create an instance of this Intake and start sending your logs. No event will be parsed but you will be able to see the evolution of your parser while you are developping it.

First of all, go to `Intakes`, `+ INTAKE` and select `Custom format` : 

1. Write the name of your Intake
2. Give a description for your Intake
3. Select a module. A module is linked to a taxonomy in relation with your format which will help you to develop your parser. For instance, if you develop a custom format for a Fortinet product, you will choose the Fortinet module. If your module does not exist, just write the name of your module (name of the application or compagny if they have different products) and click on `Create`
4. Select the data sources associated to your events. You can have severals ones. Data sources can be use when you want to deploy rules.
5. Click on `Save`

![SEKOIA.IO Custom format creation](../assets/operation_center/custom_format/create_custom_format.png){: style="max-width:150%}


### Panel overview
The custom format panel is structured like this :

1. Metadata information about your Intake
2. The area where you can build your Intake with `Stages`
3. A button to switch in `Expert mode` (yaml visualization of your Intake)
4. A button to display the `Taxonomy manager`
5. An area to test your Intake with an event sample.

![SEKOIA.IO Custom format Panel Overview](../assets/operation_center/custom_format/panel_overview.png){: style="max-width:150%}

## Stages
A Custom format consists in a sequence of stages organized under a pipeline that modifies the event on the fly.
A stage is a parsing step that will have a specefic behaviour on the event.
The goal is to define a sequence of stages that will parse your events in the ECS format. 

### Common stages
Common stages are provided by SEKOIA.IO to help you parse your events. There are currently 5 different common stages, each having its specifities :

- [Json](#json-stage)
- [Date](#date)
- [Delimiter Separeted Value](#delimiter-separated-values)
- [Grok](#grok)
- [Key-Value](#key-value)

#### JSON Stage

![SEKOIA.IO Json stage](../assets/operation_center/custom_format/json_stage.png){: style="max-width:100%"}

The JSON stage can be used to deserialize a JSON from a string.
You will need the provide :

- `Name`
- `Description` (optional)
- `Input_field` - It corresponds to the entry of the stage. It corresponds to the field you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
- `Output_field` - It corresponds to the output of the stage. It will be used in next stages to get a JSON field.

**Example**

In the following event, a JSON is present in the `message` field. The JSON stage can be used to get all information we need.

```json
{
  "message": "{'protocol':'tcp','traffic':{'source':'127.0.0.1','target':'8.8.8.8'}}"
}
```
To get the reference of the source IP in another stage, we will use the reference `{{stage1.message.traffic.source}}`

- `stage1` is the name of the JSON stage
- `message` is the name of the `Output_field`
- `traffic.source` is the field we want in the JSON

#### Key Value
![SEKOIA.IO Key Value stage](../assets/operation_center/custom_format/kv_stage.png){: style="max-width:100%"}

The Key-Value stage can be used to deserialize a key-value string.
You will need to provide :

 - `Name`
 - `Description` (optional)
 - `Input_field` - It corresponds to the entry of the stage. It corresponds to the field you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - `Output_field` - It corresponds to the output of the stage. It will be used in next stages to get a value corresponding to a key.
 - `Value Separator` - It is the separator that differentiates the key from the value. It it set to `=` by default. 
 - `Item Separator` - It is the separator that differentiates two different key-value. The default separator is `\s` which means a whitespace character.

**Example**

In the following event, a key-value string is present in the `message` field. The Key-Value Stage can be used to get all information we need.

```json
{
  "message": "to=john.doe@example.com, relay=mail.isp.com, delay=xxx, delays=xxx, dsn=2.0.0, status=sent (250 2.0.0 OK)"
}
```

With `Value Separator: "="` and `Item Separator: ",\s"`, the log can be parsed. To get for example the relay, we will use the reference `{{stage1.message.relay}}`

- `stage1` is the name of the Key-Value stage
- `message` is the name of the `Output_field`
- `relay` if the key corresponding to the value we want

#### Grok
![SEKOIA.IO Grok stage](../assets/operation_center/custom_format/grok_stage.png){: style="max-width:100%"}

The Grok stage can be used to match a field against a Grok pattern. Grok is a tool provided by Elasticsearch and gives you the ability to parse arbitrary string and structure it.
You can find more information about Grok in the [official documentation](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html).
The list of all the Grok patterns that can be used can be found [here](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns)

For this stage, you will need to provide :

- `Input_field` - It corresponds to the entry of the stage. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
- `Output_field` - It corresponds to the output of the stage. It will be used in next stages to get a value corresponding to a key.
- `Pattern` - It is the Grok pattern you want to apply.
- `Custom Patterns` - If no Grok pattern satisfies you in this [list](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns), you can create your own custom patterns.
On the left column, write the name of your pattern. On the right column, write the regex corresponding to that pattern.  
**Example** : 
![Grok custom pattern](../assets/operation_center/custom_format/grok_custom_pattern.png)  
In this example, the pattern `SSHD_MESSAGE_ILLEGAL_USER` will match the strings `Illegal user` or `illegal user`.  


**Example**

In the following event, a Grok Stage can be used to parse the event.

```json
{
  "message": "64.3.89.2 took 300 ms"
}
```

If we want to parse the IP and the time in milliseconds, the following Pattern can be used :
`%{IP:client} took %{NUMBER:duration} ms`

To get the IP in a next stage, we will then use the reference `{{stage1.message.client}}`.  
To get the duration, we will use `{{stage1.message.duration}}`.

#### Date
![SEKOIA.IO Date stage](../assets/operation_center/custom_format/date_stage.png){: style="max-width:100%"}


The Date stage can be used to parse a date field. The output of this stage is a date normalized in ISO 8601 which is the format used by SEKOIA.IO. This stage accepts, as optional properties, the format to parse the date (by default, the stage try to autodetect the format) and the IANA timezone of the parsed date (by default, "UTC").

You will need to provide :

 - `Name`
 - `Description` (optional)
 - `Input_field` - It corresponds to the is the entry of the stage. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field.
`original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - `Output_field` - is the output of the stage. It will be used in next stages to get the output value.
 - `Format` (optional) - You can specify the format of the date. By default, the stage try to autodetect the format.
 - `Timezone` (optional) - You can specify the timezone of the date. It is set to `UTC` by default.

**Exemple**

In the following event, a Date stage can be used to parse the field.

```json
{
  "date": "May 21, 2021 at 11:04:35"
}
```

One can configure the stage as follow :

- `Input_field: {{original.date}}`
- `output_field: date`
- `format: %MMM %dd, %yyyy at %hh:%mm:%ss`
- `timezone: UTC`

To get the date parsed in a next stage, we will then use the reference `{{stage1.date}}`. The output will be `2021-05-21T11:04:35Z` (ISO 8601).


#### Delimiter Separated Values
![SEKOIA.IO DSV stage](../assets/operation_center/custom_format/dsv_stage.png){: style="max-width:100%"}

The Delimiter Separated Values stage can be used to extract values from a delimiter-separated values string. This stage needs the list of columns and, as optional, the delimiter (by default, the delimiter is the comma ',').

You will need to provide :

 - `Name`
 - `Description` (optional)
 - `Input_field` - It corresponds to the is the entry of the stage. It corresponds to the field you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field.
`original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.
 - `Output_field` - It corresponds to the output of the stage. It will be used in next stages to get a value corresponding to a key.
 - `Column Names` - You need to list the column names used to retrieve information. The format has to be the following : `<column_A>,<column_B>,<column_C>...`
 - `Delimiter` - The delimiter used to differenciate two columns (By default `,`).

**Example**

In the following event, a DSV stage can be used to parse the `message` field.

```json
{
  "message": "2020/12/04 16:47:48;LOGIN;jenkins;2305"
}
```

We can configure the stage as follow : 
- `Input_field: {{original.message}}`
- `Output_field: message`
- `Column Names: date,action,username,user_id`
- `Delimiter: ;`

To get for instance the `user_id` in a next stage, we will use `{{stage1.message.user_id}}`


### Custom stage

The custom stage is used to create actions. An action is an elementary operation that can `set`, `translate` or `delete` a field.
!!! Important
    While the "Common stages" are used to extract fields from your logs, this stage must be present in every intake to set the extracted fields in the ECS format expected by SEKOIA.IO.

#### Set
![SEKOIA.IO Set action](../assets/operation_center/custom_format/set_action.png){: style="max-width:100%"}

This action is used to set the value of one field in the ECS format in the final version of the event.

The value corresponding to the field you want to set can either be a constant (for instance `my-constant`, `10` ...) or a reference to a field from a stage (for instance `{{stage1.message.myfield.subfield}}`).

!!! note
    If the value cannot be computed or is empty, the field is not modified.

**Example**

The JSON stage :

- `Name: parsed_json`
- `Output_field: message` 

was previously used to parse the following event : 
```json
{
  "message": "{'protocol':'tcp','traffic':{'source':'127.0.0.1','target':'8.8.8.8'}}"
}
```
We now want to put the `source` and the `target` IP in the final version of the parsed event.
The `Set` action can be used :

![SEKOIA.IO Set example](../assets/operation_center/custom_format/set_example.png){: style="max-width:100%"}

`source.ip` and `destination.ip` are the fields used in Elastic Common Format taxonomy.

#### Translate
![SEKOIA.IO Set action](../assets/operation_center/custom_format/translate_action.png){: style="max-width:100%"}

The `Translate` action sets value of one or more fields according to the value of a source field and a dictionary that connect values.
An optional `fallback` value can be defined. If the value of the source field doesn't match any entry of the mapping dictionary, the fallback value will be used to set the target field. If no fallback value is defined and the value of the source field doesn't match any entries, the target field will not be created in the final event.

**Example**

We want to set the value of `http.response.status_message` according to the value `http.response.status_code` and a dictionary.
`http.response.status_code` contains only status codes values.

We can define a `Translate` action with the following parameters :
![SEKOIA.IO Set action](../assets/operation_center/custom_format/translate_example.png){: style="max-width:100%"}

#### Delete
![SEKOIA.IO Delete action](../assets/operation_center/custom_format/delete_action.png){: style="max-width:100%"}

The `Delete` action allows you to delete fields in the final version of the event.

**Example**

The following action will delete the fields `source.ip` and `destination.ip` from the final event.
![SEKOIA.IO Delete action](../assets/operation_center/custom_format/delete_example.png){: style="max-width:100%"}

### Filters

Reference to a field can be extended with filters.
Filters are separated from the field path by a pipe symbol (|).
Multiple filters can be chained. The output of a filter is applied to the next.

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

## Taxonomy manager
A taxonomy is a hierarchical schema used to normalize events. The taxonomy used by SEKOIA.IO is the ECS standard (Elastic Common Schema).
The taxonomy manager allows you to view all the ECS fields available with their description.  
If a field in an event is custom to the technology and cannot be placed in any field of the ECS standard, you can create your own field.
!!! note
    By convention, the name of the field must start with the name of your intake followed by the field name.

**Example** :

The product `technoexample` has a field called `environment` which is custom to this technology and does not exist in ECS. With the taxonomy manager, you can create a custom field
`technoexample.environment`. This field will then be available in the [Custom Stage](#custom-stage)
![SEKOIA.IO Taxonomy custom field](../assets/operation_center/custom_format/taxonomy_custom_field.png)

## Example
You now have all the knowledge to start developping your custom Intake ! You can follow this example that uses different notions explained before.

### Context
Let's suppose you want to develop a custom format for a firewall solution. This firewall creates two types of events :

- Traffic events
- Audit events (When a user logs in to the device)

Traffic events are structed like this :
```bash
traffic logs: {"date": "1651507525", "status": "accept" ,"traffic": {"sourceip": "1.1.1.1", "destinationip": "2.2.2.2", "srcport": 50436, "dstport": 443}}
```

Audit events are structured like this :
```bash
audit logs: {"date": "1651507525", "username": "john", "role": "administrator", "status": "connect"}
```

### Solution
* The first thing we can see is that the two types of events look the same but the keys used in the JSON are different.
* We can also notice that the first word identifies the type of event (traffic or audit).
* Finally we can notice that each type of event contains a key `date` containing the date of the event in epoch format (The Unix epoch is the number of seconds that have elapsed since January 1, 1970 at midnight UTC)

For our Intake, we will need :

- a `JSON` stage to parse the JSON
- a `Grok` stage to parse the start of each event and identify the type (Audit or Traffic)
- At least one `Date` stage to parse to `date` field in epoch format and converts it in ISO 8601

Let's get into it !

#### Identify the type of event
To identify the type, we can use a `Grok` stage :
![SEKOIA.IO Solution Grok stage](../assets/operation_center/custom_format/exercice_grok_stage.png)

This pattern will extract :

- The type in the field `{{parse_type.message.type}}`
- The JSON in the field `{{parse_type.message.jsondata}}` 


#### Parse the JSON
To parse the JSON, we will use a `JSON` stage:
![SEKOIA.IO Solution JSON stage](../assets/operation_center/custom_format/exercice_json_stage.png){: style="max-width:100%"}

#### Parse the date of the event
To parse the date of the event, we will use a `Date` stage:
![SEKOIA.IO Solution Date stage](../assets/operation_center/custom_format/exercice_date_stage.png){: style="max-width:100%"}

#### Set the fields in ECS for traffic logs
Now that everything is parsed, we can use a custom stage to set the values in ECS :
![SEKOIA.IO Solution set traffic stage](../assets/operation_center/custom_format/exercice_set_traffic.png){: style="max-width:100%"}

#### Results
With the `Test your parser` feature, you can see the result.  
**Traffic events** :
![SEKOIA.IO Solution result traffic](../assets/operation_center/custom_format/exercice_result_traffic.png){: style="max-width:60%"}