# Optimization rules reference

This reference provides the technical specifications for filters, operators, and actions used when configuring Sekoia.io intake optimization rules.

## Filter operators

 The following binary and unary operators are supported for use in filters:

| Operator | Description | Type |
| :--- | :--- | :--- |
| `==` |  Checks if two values are equal  | Binary |
| `!=` |  Checks if two values are not equal  | Binary |
| `>` |  Left value is greater than the right  | Binary |
| `<` |  Left value is less than the right  | Binary |
| `>=` |  Left value is greater than or equal to the right  | Binary |
| `<=` |  Left value is less than or equal to the right  | Binary |
| `in` |  Left value is in the right collection  | Binary |
| `not in` |  Left value is not in the right collection  | Binary |
| `contains` |  Left value contains the right value  | Binary |
| `not contains` |  Left value does not contain the right value  | Binary |
| `exists` |  Checks if the specified key exists | Unary |
| `not exists` |  Checks if the specified key does not exist  | Unary |

## Value data types
When defining the "value" in a filter, you must match the data type of the field you are evaluating.

* Integer fields: Use raw numbers without quotes (e.g., 4624).
* String fields: Use double quotes (e.g., "failed").
* Collections: Use arrays for "==", "in" or "not in" operators (e.g., ["rfc1918", "rfc5735"]

## Action bitmask values

 A rule can accept a combination of actions specified using a bit mask.

| Action ID | Action Name | Description |
| :--- | :--- | :--- |
| **1** | **Ignore Event** |  Prevents the event from being analyzed or stored in the system. |
| **2** | **Delete Message Field** |  Removes the message field from the event. |
| **4** | **Shrink Event** |  Retains only the minimum required fields necessary for processing. |
| **8** | **Ignore Useless Event** |  Discards the event if it contains no extractable data. |
| **16** | **Delete Non-Standard Fields** |  Deletes fields not included in official ECS or Sekoia Taxonomy. |

!!! note "Visibility"
    Currently, only the **Ignore Event** (action=1) action will have a visible impact on the platform's usage page.

## See also
* [Optimization rules overview](/xdr/features/collect/optimization_rules_overview.md) to understand how optimieation rules work.
* [Create an optimization rule](/xdr/features/collect/create_optimization_rule.md) to start creating your rule thanks to our step by step guide. 
