# fileutils

![fileutils](/assets/playbooks/library/fileutils.svg){ align=right width=150 }

This module exposes action to manipulate files. It extracts data from XML or JSON files.

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


## Extra

Module **`fileutils` v1.26**