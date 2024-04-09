# Intakes
Intakes correspond to data sources sent to Sekoia.io. They are identified by a name, a log format, an entity and an intake key.

You can configure as much intakes as you need in order to increase Sekoia.io knowledge of your infrastructure.

All features related to intakes are visible through the “Intakes” menu on the Operations Center.
## Intakes listing
The intakes homepage allows you to view the list of intakes already created within the community but also to create new intakes.

![intakes_listing](/assets/operation_center/intakes/intakes-listing.png){: style="max-width:100%"}

On this page, you can find:

- The created intakes in your community
- The entity associated with the intake
- The number of events sent to Sekoia.io for the past 7 days
- The number of events in error
- The intake key for each intake that you can copy directly from the table to your clipboard
- The creator as well as the creation date
- A delete button that implies the events produced by the intake will no longer be analyzed



## Create an intake from our integrations catalog
To configure a new source of events in your community, you can rely on our list of continuously growing integrations that are constantly developed and enhanced by Sekoia.io’s team.
![intakes_types](/assets/operation_center/intakes/intakes-types.png){: style="max-width:100%"}

To create an intake, you have to:

1. Click on the `+ Intake` from the Intakes homepage
2. Choose the source of events that suits your needs (you can filter these sources by clicking on the categories’ tags)
3. Click on the `Create` button in the source card
4. Provide an intelligible name
5. Select the entity to which you want to associate the corresponding data
6. Click on `Create`
7. Find your newly created source of events as well as the intake key in the Intakes homepage

![intakes_creation](/assets/operation_center/intakes/modal-intake-creation.png){: style="max-width:100%"}

!!! Note
    The documentation about the integration of your data sources is also available in the [integrations](integrations/index.md) page.

## Configure a notification to report on inactive intake
An inactive intake may have devastating consequences on your security monitoring. To prevent incidents from happening, you can set up notifications to get alerted when an intake stops sending events to Sekoia.io.

To set up your notification, you will have to:

1. Go to the Intakes listing page and click on:  ![Notification logo](/assets/operation_center/intakes/Monitor_intake_logo.png){: style="max-width:10%"} on the right side of the table
2. Specify how long the intake should be inactive before sending a notification. The duration can go from 15 min to 24 hours.
3. Select how you want to be notified. Triggered actions that are available are mentioned in the page [Turn on notifications](/getting_started/notifications-Listing_Creation).

!!! note
     You can also set up this notification from the User Center > Notifications by selecting the trigger `No events are received`.

![Create notification](/assets/operation_center/intakes/Monitor_intake_create_notification.png){: style="max-width:100%"}

## Custom intakes

Sekoia.io provides a list of intakes that allows you to integrate events from different sources such as systems, applications and security appliances.

Some technologies may not have an associated Intake in the official Sekoia.io catalog and therefore cannot be parsed in Sekoia.io.

The "Custom format" feature allows you to easily develop your own Intake. It gives you the tools to parse your events in the Elastic Common Schema (ECS) format to ensure agnostic detection and to index fields for search in the Events page.

!!!note
    In order to use this feature, you need to have the `SIC_WRITE_INTAKE` permission associated to your Sekoia.io account. This permission also allows you to create an existing Intake.

### Create an empty Custom format
The creation of an empty Custom format is the first step to develop your own Intake.

After that, you will be able to create an instance of this Intake and start sending your logs. No event will be parsed but you will be able to see the evolution of your parser while you are developping it.

To create an empty custom format:

1. Go to `Intakes`, `+ INTAKE` and select `Custom format`
2. Write the name of your Intake
3. Give a description for your Intake
4. Select a module. A module is linked to a taxonomy in relation with your format which will help you develop your parser. For instance, if you develop a Custom format for a Fortinet product, you will choose the Fortinet module. If your module does not exist, just write the name of your module (name of the application or compagny if they have different products) and click on `Create`
5. Select the data sources associated to your events. Note that you can have multiple ones and that data sources can be used when you want to deploy rules.
6. Click on `Save`

### Panel overview
The custom format panel is structured like this:

1. Metadata information about your Intake
2. An area where you can build your Intake with `Stages`
3. A button to switch to `Expert mode` (YAML visualization of your Intake)
4. A button to display the `Fields manager`
5. An area to test your Intake with an event sample.

![Sekoia.io Custom format Panel Overview](/assets/operation_center/intakes/custom_intake_header-1.png){: style="max-width:100%"}

## Stages
A Custom format consists of a sequence of stages organized under a pipeline that modifies the event on the fly.
A stage is a parsing step that will have a specific behaviour on the event.
The goal is to define a sequence of stages that will parse your events in the ECS format.

### Custom stage
The custom stage is used to create actions. An action is an elementary operation that can `set`, `translate` or `delete` a field.
!!! Important
    While the [Common stages](#common-stages) are used to extract fields from your logs, this stage must be present in every intake to set the extracted fields in the ECS format expected by Sekoia.io.

#### Set

This action is used to set the value of one field in the ECS format in the final version of the event.

![custom_set_stage](/assets/operation_center/intakes/custom_stage_set.png){:style="max-width:100%"}

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
![custom_set_stage](/assets/operation_center/intakes/custom_stage__set_example.png){: style="max-width:100%"}

`source.ip` and `destination.ip` are the fields used in Elastic Common Format taxonomy.

#### Translate
![Sekoia.io Set action](/assets/operation_center/intakes/custom_translate.png){: style="max-width:100%"}

The `Translate` action sets value of one or more fields according to the value of a source field and a dictionary that connects values.
An optional "fallback" value can be defined.

If the value of the source field does not match any entry of the mapping dictionary, the fallback value will be used to set the target field.

If no fallback value is defined and the value of the source field does not match any entries, the target field will not be created in the final event.

**Example**

You want to set the value of `http.response.status_message` according to the value `http.response.status_code` and a dictionary.
`http.response.status_code` contains only status codes values.

You can define a `Translate` action with the following parameters:
![Sekoia.io Set action](/assets/operation_center/intakes/example_translate.png){: style="max-width:100%"}

#### Delete

The `Delete` action allows you to delete fields in the final version of the event.

![Sekoia.io Delete action](/assets/operation_center/intakes/custom_delete.png){: style="max-width:100%"}

**Example**

The following action will delete the fields `source.ip` and `destination.ip` from the final event.

![Sekoia.io Delete action](/assets/operation_center/intakes/example_delete.png){: style="max-width:100%"}

### Common stages
Common stages are provided by Sekoia.io to help you parse your events.

There are currently 5 different common stages, each having its specifities:

- [Json](#json-stage)

- [Date](#date)

- [Delimiter Separeted Value](#delimiter-separated-values)

- [Grok](#grok)

- [Key-Value](#key-value)

#### JSON Stage

![Sekoia.io Json stage](/assets/operation_center/intakes/json_stage.png){: style="max-width:100%"}
The JSON stage can be used to deserialize a JSON from a string.

You will need to provide the stage with:

- A `Name`

- A `Description` (optional)

- An `Input_field` - As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your logs will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.

- An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a JSON field.

**Example**

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

#### Key Value

The Key-Value stage can be used to deserialize a Key-Value string.

![Sekoia.io Key Value stage](/assets/operation_center/intakes/key_value_stage.png){: style="max-width:100%"}
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

The Grok stage can be used to match a field against a Grok pattern. Grok is a tool provided by Elasticsearch that gives you the ability to parse an arbitrary string and structure it.
![Sekoia.io Grok stage](/assets/operation_center/intakes/grok_stage.png){: style="max-width:100%"}
!!! tip
    You can find more information about Grok in the [official documentation](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html). The list of all the Grok patterns that can be used can be found [here](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns).

You will need to provide the stage with:

- An `Input_field` -  As its name suggests, this is the stage's entry. It corresponds to the chain of characters you want to deserialize. It is set to `{{original.message}}` by default. When you start sending your logs in an empty parser, your log will be placed in that field. `original` refers to the event at the entry of the pipeline and `message` to the field corresponding to the log.

- An `Output_field` - It corresponds to the output of the stage and will be used in next stages to get a value corresponding to a key.

- A `Pattern` - It is the Grok pattern you want to apply.

- A `Custom Patterns` - If no Grok pattern satisfies you in this [list](https://github.com/elastic/logstash/blob/v1.4.0/patterns/grok-patterns), you can create your own custom patterns with the `+` button on the right of the line. Then, on the left column, write the name of your pattern. On the right column, write the regex corresponding to that pattern.

**Example 1**

![Grok custom pattern](/assets/operation_center/intakes/grok_stage_example.png)

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

The Date stage can be used to parse a date field. The output of this stage is a date normalized in ISO 8601, which is the format used by Sekoia.io.

This stage accepts, as optional properties, the format to parse the date and the IANA timezone of the parsed date.

![Sekoia.io Date stage](/assets/operation_center/intakes/date_stage.png){: style="max-width:100%"}

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

The Delimiter Separated Values stage can be used to extract values from a delimiter-separated values string.

This stage needs the list of columns and, as optional, the delimiter (by default, the delimiter is the comma ',').

![Sekoia.io DSV stage](/assets/operation_center/intakes/delimiter_sep_val.png){: style="max-width:100%"}

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

Reference to a field can be extended with filters. Filters are separated from the field path by a pipe symbol (|).

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

![Sekoia.io Condition example](/assets/operation_center/custom_format/conditions_example.png)

## Fields manager

A taxonomy is a hierarchical schema used to normalize events. The taxonomy used by Sekoia.io is the ECS standard (Elastic Common Schema).

The fields manager (previously called taxonomy manager) allows you to view all the ECS fields available with their description.

![fields manager](/assets/operation_center/intakes/field_manager.png){: style="max-width:100%"}

If a field in an event is custom to the technology and cannot be placed in any field of the ECS standard, you can create your own field.

!!! note
    By convention, the name of the field must start with the name of your intake followed by the field name.

Once the field manager panel is open, you will find two sections:

- `My custom fields`: This section is dedicated to the fields you’ve created

- `Existing fields`: This sections gather the fields already proposed by Sekoia.io

### Create and set a custom field

To create a custom field, you have to:

1. Click on the dedicated button `+ Custom field`

2. Fill in the following fields:

    - `Field name`: It is the name to refer to your custom field

    - `Field type`: You need to choose between Keyword, Long, Date, Geo point...

    - `Description`: This description will help you remember what this field is used for

![create a custom field](/assets/operation_center/intakes/custom_fields.png){: style="max-width:100%"}


### Set an observable type for graph investigation

If you want the field you are building to be displayed in graph investigation, you should activate the dedicated checkbox.

When checked, another part of the form appears to set this optional feature.

![set observables](/assets/operation_center/intakes/set_observables.png)

To display your custom field in the graph investigation, you first need to:

1. Select the observable type your field refers to
2. Depending on the type of observable selected, you might need to select:
    - The observable property associated with your custom field
    - The observable name that you want to associate your custom field with
3. Once saved, your new custom field will be displayed in the `Your custom field` section. You will be able to :
    - Edit it
    - Delete it
    - Manage custom fields

After this last step, your custom field is ready to be used in your parser. The events parsed will be then able to display a Smart Description and this field will appear in the graph investigations

**Example**

The product `technoexample` has a field called `environment` which is custom to this technology and does not exist in ECS. With the taxonomy manager, you can create a custom field `technoexample.environment`.

This field will then be available in the [Custom Stage](#custom-stage).

## Smart descriptions

The work of analysts can easily become difficult to deal with when there are a lot of events and different types of parsers and logs. Smart descriptions are a way to ease the analysis of events by adding a comprehensive and clear description generated from the event fields.

Users can define their own smart descriptions for their custom parser.
When creating a new intake, you can choose to create a custom format from the integrations catalog.
You can then define its `Smart Description` in the dedicated tab when setting it up.

The editor contains a list of smart descriptions. Each description has the following properties:

- `value`: the smart description itself, with variables from the event field expressed as `{FIELD_NAME}`

- `conditions`: a set of conditions that should be met for this description to be used. Each condition has a field name and a value. A condition without a value means that the field should be set (whatever the value)

- `relationships` (optional): this will be used to display events inside an investigation graph. Each relationship should have a `source` (object path), a `target` (object path) and a `type` (text, description of the relationship, with variables from the event field expressed as {FIELD_NAME})

When several conditions match the same event, the smart description with the most conditions is used as you can see in the test section.

## Notification when an intake is not receiving events

You can set a notification when an intake stops receiving events:

- On the Intake's page by clicking on the bell next to the delete button
- On the `Notifications` page of the User Center

![Intakenotification](/assets/operation_center/intakes/2022-12-30_16h35_06.png)

Here is the needed configuration setup:

- Trigger: `No Events are received`
- Period: Period of time when the intake selected did not receive any events
- Intake
- Actions to perform:  Choose a channel where the notification will be sent
- Notification name

---

Do not hesitate to contact your support if:

- The settings’ recommendations provided are not sufficient or not applicable to your system. We can then see with you how to transfer your events in the best conditions.
- The format of the logs you want to send us is not in the list. We regularly add new formats and we can let you know when yours is available in our catalog.
