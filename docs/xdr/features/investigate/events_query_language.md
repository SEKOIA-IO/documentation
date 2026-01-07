# Events Query Language

This domain-specific language can be used to generate search queries that integrate advanced search operators.

Please refer to [Elastic Common Schema (ECS) Reference](https://www.elastic.co/docs/reference/ecs/ecs-field-reference) if you need to look up a field available in Sekoia.io. 

## Example

On the Events page, the following query will match all successful connections to a domain name starting by `evil`:

`event.type:connection AND NOT action.outcome:failure AND destination.domain:evil*`

## Syntax

A query can contain one or more terms, separated by logical operators.

Each term is composed of a field name, an operator and a literal.

e.g: `id:"ALWyJiGeJSiw"`

A term without a field name and an operator will search the literal value in all fields.

## Literals

| Type | Description | Example |
|------|-------------|---------|
| Word | Single word | `value` |
| Phrase | A phrase is surrounded by double quotes and matches all words in this exact order | `"exact phrase"` |
| Numbers | For numeric fields | `17.23` |
| Wildcards | Wildcard characters can be used to match more events. Use `?` to match a single character or `*` to replace any number of characters. | `evil*` |
| Regular Expressions | Regular Expressions can be used to filter for specific values. The regular expression is surrounded by forward slashes (`/`) | `/(evil|bad).*/`

!!! Note
    For regular expressions, do not use `^` and `$` which delimits the beginning and the ending of a line.

## Operators

### Term Operators

Term Operators can be used to customize the search

| Operator | Description | Example |
|----------|-------------|---------|
| `:` | The field must exactly match the literal. In case the field represents a list, this means that one item of the list must match. | `event.type:connection` |
| `:*` | The field must have a value. | `dns.question.name:*` |
| `:>` | The numerical value must be greater than the specified number | `destination.bytes:>42` |
| `:>=` | The numerical value must be greater than or equal to the specified number | `destination.bytes:>=42` |
| `:<` | The numerical value must be less than the specified number | `destination.bytes:<42` |
| `:<=` | The numerical value must be less than or equal to the specified number | `destination.bytes:<=42` |
| `:[X TO Y]` | The numerical value must be between X and Y | `destination.bytes:[100 TO 200]` |

!!! note
    for IP search, `:[X TO Y]` is available with X and Y as IP ranges e.g. `source.ip:[145.0.0.0 TO 145.255.255.255]`

### Logical operators

| Operator | Description | Example |
|----------|-------------|---------|
| AND | Match if both terms are verified | `event.type:connection AND action.outcome:success` |
| OR | Match if one of the terms is verified | `source.ip:"1.2.3.4" OR destination.ip:"1.2.3.4"` |
| NOT | Inverse the result of the term | `NOT event.type:connection` |

!!! note
    Take care, operators need to be uppercase in your query.

### Grouping operators

| Operator | Description | Example |
|----------|-------------|---------|
| () | Groups operands | `event.type:connection AND (source.ip:"1.2.3.4" OR destination.ip:"1.2.3.4")` |
