uuid: 07cce76b-a319-40ee-a0cf-1ba433431e21
name: Utils
type: playbook

# Utils

![Utils](/assets/playbooks/library/utils.svg){ align=right width=150 }

This module exposes utility actions

## Configuration

This module accepts no configuration.

## Actions

### Read JSON File

Read the json file and return its content evaluated against specified jsonpath

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the JSON file to read. |
| `file` | `object` | The JSON content to read. |
| `jsonpath` | `string` | JSON path to evaluate against read file content |
| `return_list` | `boolean` | Always return a list of results. Default to false. |
| `to_file` | `boolean` | Whether the event should be saved in a file or sent directly |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `output` | `object` | Content read from file |
| `output_path` | `object` | Path to the file with the content |

### Read XML File

Read the XML file and return its content evaluated against specified xpath

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `file_path` | `string` | File path to the XML or HTML file to read. |
| `file` | `object` | The XML content to read. |
| `xpath` | `string` | XML path to evaluate against read file content |
| `source_type` | `string` | Source type of the input, it can be XML or HTML |
| `return_list` | `boolean` | Always return a list of results. Default to false. |
| `to_file` | `boolean` | Whether the event should be saved in a file or sent directly |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `output` | `object` | Content read from file |
| `output_path` | `object` | Path to the file with the content |

### GroupBy

GroupBy

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `group_key` | `string` | GroupBy element by value for a specific key |
| `filter_key` | `string` | GroupBy element with filter for a specific key |
| `filter_value` | `string` | GroupBy element with a filter for a specific value on a specific key |
| `input` | `array` | Input Data to sort |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `array` |  |

### Password Generator

Generate a password securely based on specified parameters

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `password_length` | `integer` | Password length |
| `number_of_digits` | `integer` | Number of digits in the password |
| `number_of_special_characters` | `integer` | Number of special characters in the password |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `password` | `string` |  |

### Get the current time

Get the current time according to the timezone

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `selectedTimezone` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `epoch` | `integer` | The current datetime represented as an epoch |
| `iso8601` | `string` | The current datetime represented as an iso8601-formatted string |

### Wait

Wait

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `duration` | `integer` | Time to wait, in seconds |


## Extra

Module **`Utils` v1.4.3**