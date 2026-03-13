# Optimization rules reference

This reference provides the technical specifications for filters, operators, and actions used when configuring Sekoia.io intake optimization rules.

## Filter operators

[cite_start]The following binary and unary operators are supported for use in filters[cite: 21]:

| Operator | Description | Type |
| :--- | :--- | :--- |
| `==` | [cite_start]Checks if two values are equal [cite: 22] | Binary |
| `!=` | [cite_start]Checks if two values are not equal [cite: 23] | Binary |
| `>` | [cite_start]Left value is greater than the right [cite: 24] | Binary |
| `<` | [cite_start]Left value is less than the right [cite: 25] | Binary |
| `>=` | [cite_start]Left value is greater than or equal to the right [cite: 26] | Binary |
| `<=` | [cite_start]Left value is less than or equal to the right [cite: 27] | Binary |
| `in` | [cite_start]Left value is in the right collection [cite: 28] | Binary |
| `not in` | [cite_start]Left value is not in the right collection [cite: 29] | Binary |
| `contains` | [cite_start]Left value contains the right value [cite: 30] | Binary |
| `not contains` | [cite_start]Left value does not contain the right value [cite: 31] | Binary |
| `exists` | [cite_start]Checks if the specified key exists [cite: 32] | Unary |
| `not exists` | [cite_start]Checks if the specified key does not exist [cite: 33] | Unary |

## Value data types
When defining the "value" in a filter, you must match the data type of the field you are evaluating.

* Integer fields: Use raw numbers without quotes (e.g., "4624").
* String fields: Use double quotes (e.g., "failed").
* Collections: Use arrays for "in" or "not in" operators (e.g., ["rfc1918", "rfc5735"]).

## Action bitmask values

[cite_start]A rule can accept a combination of actions specified using a bit mask[cite: 36].

| Action ID | Action Name | Description |
| :--- | :--- | :--- |
| **1** | **Ignore Event** | [cite_start]Prevents the event from being analyzed or stored in the system[cite: 37]. |
| **2** | **Delete Message Field** | [cite_start]Removes the message field from the event[cite: 38]. |
| **4** | **Shrink Event** | [cite_start]Retains only the minimum required fields necessary for processing[cite: 39]. |
| **8** | **Ignore Useless Event** | [cite_start]Discards the event if it contains no extractable data[cite: 40]. |
| **16** | **Delete Non-Standard Fields** | [cite_start]Deletes fields not included in official ECS or Sekoia Taxonomy[cite: 41]. |

!!! note "Visibility"
    Currently, only the **Ignore Event** (action=1) action will have a visible impact on the platform's usage page[cite: 42].

## See also
* [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md) to understand how optimieation rules work.
* [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md) to start creating your rule thanks to our step by step guide. 
