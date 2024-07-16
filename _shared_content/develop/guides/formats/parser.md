# How to write a parser

A parser consists of a sequence of stages organized under a pipeline that modifies the event on the fly. It transforms a raw event into a [structured one](structured_event.md).

Select the way who develop your parse to find the appropriate documentation: with the custom format feature in the product or from the github repository.

=== "parser in the platform"

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

=== "parsers in code"

    ## Pipeline

    The following pipeline is made of three stages (`stage1`, `stage2` and `stage3`)
    with the execution of `stage2` and `stage3` conditonned to a filter that evaluates the value of the event field `message.log_type` at the end of `stage2`.

    ```yaml
    pipeline:
      - name: stage1
      - name: stage2
        filter: '{{stage1.message.log_type == "network"}}'
      - name: stage3
        filter: '{{stage1.message.log_type == "process"}}'
    ```

    ## Stage

    A stage is a parsing step that denotes changes in the event that participate in the same semantic definition. A stage can create, update and delete fields by chaining execution of actions.

    For example, the following snippet shows a stage named `my_stage` which consists in two actions.

    ```yaml
    my_stage:
      actions:
        - set:
            destination.ip: 127.0.0.1
            source.ip: 127.0.0.2
        - delete:
            - event.data
    ```

    ### Common stages

    Common stages are provided to ease development of new intakes.
    `external` attribute must be used to reference a common stage along with its optional properties.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: example.external-stage
          properties:
            prop1: val1
            prop2: val2
    ```

    #### JSON

    The `json.parse-json` stage can be used to deserialize a json from a string.
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.

    **Example**

    In this example, the parser produces an event with fields that take their value from a deserialized json field. Below is the example of the input event.

    ```json
    {
      "message": "{'protocol':'tcp','traffic':{'source':'127.0.0.1','target':'8.8.8.8'}}"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set the `source.ip` and `destination.ip` fields.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: json.parseJSON
      - name: network
    stages:
      network:
        actions:
          - set:
              destination.ip: "{{parsed_event.message.traffic.target}}"
              source.ip: "{{parsed_event.message.traffic.source}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "{'protocol':'tcp','traffic':{'source':'127.0.0.1','target':'8.8.8.8'}}",
      "source": {
        "ip": "127.0.0.1"
      },
      "destination": {
        "ip": "8.8.8.8"
      }
    }
    ```

    #### Key-Value

    The `kv.parse-kv` stage can be used to deserialize a key-value string.
    Per default, the `message` field of the original event is parsed but this property can be overwritten to specify any field. Besides, default field separator is any whitespace `\s` and value separator is `=` however both can be overwritten with respective properties: `item_sep` and `value_sep`.

    **Example**

    In this example, the parser produces an event with fields and values parsed from a key-value string. Below is the example of the input event, a classical `postfix` event.

    ```json
    {
      "message": "to=john.doe@example.com, relay=mail.isp.com, delay=xxx, delays=xxx, dsn=2.0.0, status=sent (250 2.0.0 OK)"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set the `destination.user.email` field.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: kv.parseKV
          properties:
            item_sep: ',\s'
      - name: email
    stages:
      email:
        actions:
          - set:
              destination.user.email: "{{parsed_event.message.to}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "to=john.doe@example.com, relay=mail.isp.com, delay=xxx, delays=xxx, dsn=2.0.0, status=sent (250 2.0.0 OK)",
      "destination": {
        "user": {
          "email": "john.doe@example.com"
        }
      }
    }
    ```

    #### Grok

    The `grok.match` stage can be used to match a field against a Grok pattern.
    The grok pattern must be specified by means of the `pattern` property.
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.
    Parsing's result replaces the parsed content.
    Custom patterns can be specified with the `custom_patterns` property.

    **Example**

    In this example, the parser produces an event with fields and values parsed from a groked string. Below is the example of the input event.

    ```json
    {
      "message": "64.3.89.2 took 300 ms"
    }
    ```

    Below is the parsing pipeline that deserializes the `message` field and set the `destination.ip` field.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: grok.match
          properties:
            input_field: original.message
        output_field: message
            pattern: '%{IP:client} took %{NUMBER:duration} ms'
      - name: set_ip
    stages:
      set_ip:
        actions:
          - set:
              destination.ip: '{{parsed_event.message.client}}'
    ```

    The following shows the produced event.

    ```json
    {
      "message": "64.3.89.2 took 300 ms",
      "destination": {
        "ip": "64.3.89.2"
      }
    }
    ```

    #### Date

    The `date.parse` stage can be used to parse a date field.
    This stage accepts, as optional properties, the format to parse the date (by default, the stage try to autodetect the format) and the IANA timezone of the parsed date (by default, "UTC").
    Per default, the `@timestamp` field of the original message is parsed but this property can be overwritten to specify any field. The result of the resulting date is inserted in the `message` field of the current stage.

    **Example**

    In this example, the parser produces an event with a parsed date. Below is the example of the input event.

    ```json
    {
      "date": "May 21, 2021 at 11:04:35"
    }
    ```

    Below is the parsing pipeline that deserializes the `date` field and set the `@timestamp` field.

    ```yaml
    pipeline:
      - name: parsed_date
        external:
          name: date.parse
          properties:
            input_field: original.date
            output_field: date
            format: "%B %d, %Y at %H:%M:%S"
            timezone: "America/New_York"
      - name: set-date
    stages:
      set_date:
        actions:
          - set:
              @timestamp: '{{parsed_date.date}}'
    ```

    The following shows the produced event.

    ```json
    {
      "@timestamp": "2021-05-21T11:04:35Z",
      "date": "May 21, 2021 at 11:04:35"
    }
    ```

    #### DSV

    The `dsv.parse-dsv` stage can be used to extract values from a delimiter-separated values string.
    This stage accepts the list of columns and, as optional, the delimiter (by default, the delimiter is the comma ',').
    Per default, the `message` field of the original message is parsed but this property can be overwritten to specify any field.

    **Example**

    In this example, the parser produces an event with a delimiter-separated values string. Below is the example of the input event.

    ```json
    {
      "message": "2020/12/04 16:47:48;LOGIN;jenkins;2305"
    }
    ```

    Below is the parsing pipeline that deserializes the `message` field and set the `user` field.

    ```yaml
    pipeline:
      - name: parsed_dsv
        external:
          name: dsv.parse-dsv
          properties:
            columnnames:
              - date
              - action
              - username
              - user_id
            delimiter: ";"
      - name: set_user_id
    stages:
      set_user_id:
        actions:
          - set:
              user.name: "{{parsed_dsv.message.username}}"
              user.id: "{{parsed_dsv.message.user_id}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "2020/12/04 16:47:48;LOGIN;jenkins;2305",
      "user": {
        "id": "2305",
        "name": "jenkins"
      }
    }
    ```

    #### XML

    The `xml.parse-xml` stage can be used to transform a xml string into a dictionary.
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.

    **Example**

    In this example, the parser produces an event with fields that take their value from a deserialized xml field. Below is the example of the input event.

    ```json
    {
      "message": "<Event><Id>1234</Id><Provider><Name>system</Name><Id>6</Id></Provider>"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set the `agent.name` and `agent.id` fields.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: xml.parse-xml
      - name: agent
    stages:
      agent:
        actions:
          - set:
              agent.id: "{{parsed_event.message.Event.Provider.Id}}"
              agent.name: "{{parsed_event.message.Event.Provider.Name}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "<Event><Id>1234</Id><Provider><Name>system</Name><Id>6</Id></Provider>"
      "agent": {
        "id": 6,
        "name": "system"
      }
    }
    ```

    #### Windows

    The `xml.parse-windows-event` stage can be used to transform a xml windows event into a dictionary.
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.

    The parser produces an event in two parts:

    - The system part, holding data extracted from the System tag
    - The data part, flattening the data tags as key-value structure

    The following event:

    ```xml
    <Event><System><EventID>1234</EventID><Execution ProcessID="592" ThreadID="6452"/></System><EventData><Data Name="Key">Value</Data></EventData></Event>
    ```

    will be transformed in the following structure:

    ```json
    {
      "System": {
        "EventID": "1234",
        "Execution": {
          "ProcessID": "592",
          "ThreadID": "6452"
        }
      },
      "EventData": {
        "Key": "Value"
      }
    }
    ```

    **Example**

    Given the previous event as the input of the parser.

    ```json
    {
      "message": "<Event><System><EventID>1234</EventID><Execution ProcessID=\"592\" ThreadID=\"6452\"/></System><EventData><Data Name=\"Key\">Value</Data></EventData></Event>"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set the fields.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: xml.parse-windows-event
      - name: set-fields
    stages:
      set-fields:
        actions:
          - set:
              process.pid: "{{parsed_event.message.System.Execution.ProcessID}}"
              process.thread.id: "{{parsed_event.message.System.Execution.ThreadID}}"
              event.id: "{{parsed_event.message.System.EventID}}"
              custom.key: "{{parsed_event.message.EventData.Key}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "<Event><System><EventID>1234</EventID><Execution ProcessID=\"592\" ThreadID=\"6452\"/></System><EventData><Data Name=\"Key\">Value</Data></EventData></Event>",
      "process": {
        "pid": 592,
        "thread": {
          "id": 6452
        }
      },
      "event": { "id": 1234 },
      "custom": { "key": "Value" }
    }
    ```

    #### CEF

    The `cef.parse-cef` stage can be used to parse CEF messages.
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.

    This stage will extract the following keys from the header definition:

    - `CEFVersion`: The CEF version
    - `DeviceVendor`: The vendor of the product that generated the log
    - `DeviceProduct`: The product that generated the log
    - `DeviceVersion`: The version of the product
    - `DeviceEventClassID`: An unique identifier
    - `Name`: A human-readable description of the event
    - `Severity`: The severity of the event

    and will extract each key-value from the extension.

    **Example**

    In this example, the parser produces an event with fields that take their value from a CEF message. Below is the example of the input event.

    ```json
    {
      "message": "CEF:0|Security|threatmanager|1.0|100|worm successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 spt=1232"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set some fields.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: cef.parse-cef
      - name: agent
    stages:
      agent:
        actions:
          - set:
              event.id: "{{parsed_event.message.DeviceEventClassID}}"
              event.severity: "{{parsed_event.message.Severity}}"
              source.ip: "{{parsed_event.message.src}}"
              source.port: "{{parsed_event.message.spt}}"
              destination.ip: "{{parsed_event.message.dst}}"
              observer.vendor: "{{parsed_event.message.DeviceVendor}}"
              observer.product: "{{parsed_event.message.DeviceProduct}}"
              observer.version: "{{parsed_event.message.DeviceVersion}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "CEF:0|Security|threatmanager|1.0|100|worm successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 spt=1232"
      "source": {
        "ip": "10.0.0.1",
        "port": 1232
      },
      "destination": {
        "ip": "2.1.2.2"
      },
      "event": {"id": "100", "severity": 10},
      "observer": {
        "vendor": "Security",
        "product": "threatmanager",
        "version": "1.0"
      }
    }
    ```

    #### LEEF

    The `leef.parse-leef` stage can be used to parse LEEF messages (supported version of LEEF are 1 and 2)
    Per default, the `message` field is parsed but this property can be overwritten to specify any field.

    This stage will extract the following keys from the header definition:

    - `LEEFVersion`: The LEEF version
    - `DeviceVendor`: The vendor of the product that generated the log
    - `DeviceProduct`: The product that generated the log
    - `DeviceVersion`: The version of the product
    - `DeviceEventClassID`: An unique identifier

    and will extract each key-value from the extension.

    **Example**

    In this example, the parser produces an event with fields that take their value from a CEF message. Below is the example of the input event.

    ```json
    {
      "message": "LEEF:2|Security|threatmanager|1.0|100|^|src=10.0.0.1^dst=2.1.2.2^spt=1232"
    }
    ```

    Below is the parsing pipeline that deserialize the `message` field and set some fields.

    ```yaml
    pipeline:
      - name: parsed_event
        external:
          name: leef.parse-leef
      - name: agent
    stages:
      agent:
        actions:
          - set:
              event.id: "{{parsed_event.message.DeviceEventClassID}}"
              source.ip: "{{parsed_event.message.src}}"
              source.port: "{{parsed_event.message.spt}}"
              destination.ip: "{{parsed_event.message.dst}}"
              observer.vendor: "{{parsed_event.message.DeviceVendor}}"
              observer.product: "{{parsed_event.message.DeviceProduct}}"
              observer.version: "{{parsed_event.message.DeviceVersion}}"
    ```

    The following shows the produced event.

    ```json
    {
      "message": "LEEF:2|Security|threatmanager|1.0|100|^|src=10.0.0.1^dst=2.1.2.2^spt=1232"
      "source": {
        "ip": "10.0.0.1",
        "port": 1232
      },
      "destination": {
        "ip": "2.1.2.2"
      },
      "event": {"id": "100"},
      "observer": {
        "vendor": "Security",
        "product": "threatmanager",
        "version": "1.0"
      }
    }
    ```

    ## Action

    An action is an elementary operations that can create, update and delete fields.
    The execution of an action can be conditionned to a filter.

    ### set

    Sets the value of one or more fields in the final version of the event.

    The field in the final version of the event can be specified with a dotted path (i.e. `field1`, `field1.sub-field1`, …).

    The value can either be a constant (i.e. `'my-constant'`, `42`, …) or a reference to the value of another field in the stage (i.e. `{{stage1.my-field1.attribute2}}`).
    If the value cannot be computed or is empty, the field is not modified.

    Example:

    ```yaml
    - set:
        source.ip: 127.0.0.1
        destination.ip: { { stage1.target.ip } }
      filter: '{{stage1.log_type == "network"}}'
    ```

    ### translate

    Sets value of one or more fields according the value of a source field and a dictionary that connect values.

    The field in event's final version can be specified with a dotted path (i.e. `field1`, `field1.sub-field1`, …).

    An optional fallback value can be defined.
    If the value of the source field doesn't match any entry of the mapping dictionary, this fallback value will be used to set the target field.
    If no fallback value is defined and the value of the source field doesn't match any entries, the target field will not be created in the final event.

    Example:

    ```yaml
    - translate:
      dictionary:
        200: "OK"
        201: "Created"
        204: "No Content"
        400: "Bad Request"
        401: "Unauthorized"
        403: "Forbidden"
        404: "Not Found"
        500: "Internal Server Error"
        501: "Not Implemented"
        502: "Bad Gateway"
        503: "Service Unavailable"
        504: "Gateway Timeout"
      mapping:
        http.response.status_code: http.response.status_message
        api.status_code: api.status_message
      fallback: "Request Processed"
      filter: '{{stage1.log_type == "network"}}'
    ```

    ### References

    Each stage generates a layer with a set of produced fields in the stage.
    You can refer one of these field from another field, a filter or the input of a next common stage.
    To refer a field, use a [jinja](https://jinja.palletsprojects.com) placeholder (ie `{{xxxx}}`) with the name of the referred layed (ie, the name of the stage) as the prefix then the path to the field in dot-notation
    (eg, to refer the value of the field `date` from the `parsed_date` stage, use `{{parsed_date.date}}`).
    For incoming events, a first layer named `original` is created by Ingest and the ECS envelop as received.

    #### filters

    Reference to another field can be extended with filters.
    Filters are separated from the field path by a pipe symbol (|).
    Multiple filters can be chained. The output of a filter is applied to the next.

    For example, `{{stage1.username |strip |upper}}` removes the whitespace and returns the uppercase value of the `username` variable computed in `stage1`.

    Ingest makes available the [jinja built-in filters](https://jinja.palletsprojects.com/en/3.0.x/templates/#list-of-builtin-filters). Most popular filters are:

    | filter       | description                                                       |
    | ------------ | ----------------------------------------------------------------- |
    | `abs`        | returns the absolute value of the variable.                       |
    | `capitalize` | returns the first character uppercase, all others lowercase.      |
    | `float`      | converts the variable in float                                    |
    | `int`        | converts the variable in int                                      |
    | `length`     | returns the number of items                                       |
    | `lower`      | returns the value all lowercase                                   |
    | `max`        | returns the largest item from the variable                        |
    | `min`        | returns the smallest item from the variable                       |
    | `strip`      | returns the variable removed from heading and leading whitespaces |
    | `upper`      | returns the value all uppercase                                   |

    Ingest extends these built-in filters with a set of custom filters:

    | filter        | description                                                            |
    |---------------|------------------------------------------------------------------------|
    |`basename`     | returns the base name of a path (support unix and windows path)        |
    |`dirname`      | returns the directory name of a path (support unix and windows path)   |
    |`to_rfc3339(value: Any, format=None)`| converts and formats any date as rfc3339 string  |
    |`to_iso8601(value: Any, format=None)`| converts and formats any date as iso8601 string  |
    |`re_match`     | tests the value against an regular expression (the whole value)        |
    |`re_search`    | tests if a subset of the value match the regular expression            |

    ### delete

    Deletes fields in the final version of the event.

    Example:

    ```yaml
    - delete:
        - source.ip
        - destination.ip
      filter: '{{stage1.log_type != "network"}}'
    ```

    ## Inspirations

    - See [Azure Front Door parser](https://github.com/SEKOIA-IO/intake-formats/blob/main/Azure/azure-front-door/ingest/parser.yml) as an introduction.
    - See [AWS Flow logs parser](https://github.com/SEKOIA-IO/intake-formats/blob/main/AWS/aws-flow-logs/ingest/parser.yml) for textual extraction.
    - See [Wallix Bastion parser](https://github.com/SEKOIA-IO/intake-formats/blob/main/Wallix/wallix-bastion/ingest/parser.yml) for filters usage.
    - See [ProofPoint TAP parser](https://github.com/SEKOIA-IO/intake-formats/blob/main/ProofPoint/proofpoint-tap/ingest/parser.yml#L59-L110) and [Azure Windows parser](https://github.com/SEKOIA-IO/intake-formats/blob/main/Azure/azure-windows/ingest/parser.yml) for complex parsers.
 