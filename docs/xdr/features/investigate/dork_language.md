# Dork Language

Dork is a domain-specific language used to generate search queries that integrate advanced search operators.
This language offers to exceed filters available on APIs.

## Example

On the Operations Center, on the events page, the following query will match all not failed events received from the start of January 1st, 2020 to the end of January 2nd, 2020:

`NOT(error_code:"Failed") AND timestamp:>=2020-01-01T00:00:00Z AND timestamp:<2020-01-03T00:00:00Z`

## Syntax

A dork query contains one or more terms. Each terms hold a field, an operator and a literal.

e.g: `id:"ALWyJiGeJSiw"`

These terms can be combined though the use of logical operators.

## Literals

| Type | Format | Example |
|------|--------|---------|
| String   | `"\w+"` | `"value"` |
| Number   | `\d+[.,]\d*` | `17.23` |
| Boolean  | `0` (false) or `1` (true) | `0` |
| Date     | `yyyy[-mm[-dd]]` | `2020-01-01` |
| DateTime | `yyyy-mm-ddThh:mm:ss[.sss][+-hh:mm|Z]` | `2020-01-01T12:23:45.2342+02:00` |

## Operators

### String operators

| Operator | Description | Example |
|----------|-------------|---------|
| : | The field must exactly match the literal | `type:"malware"` |
| :^ | The field must start with the literal | `type:^"Mal"` |
| :$ | The field must end with the literal | `type:$"ware"` |
| :~ | The field must partially match the literal | `type:~"dicat"` |

If the field represents a list:

| Operator | Description | Example |
|----------|-------------|---------|
| : | The field must match one item of the list | `tag:"binary"` |

### Number operators

| Operator | Description | Example |
|----------|-------------|---------|
| : | The field must equal the literal | `urgency:100` |
| := | The field must equal the literal | `urgency:=100` |
| :> | The field must be less than literal | `urgency:>10` |
| :&lt; | The field must be greater than literal | `urgency:<50` |

### Boolean operators

| Operator | Description | Example |
|----------|-------------|---------|
| : | The field must equal the literal | `deleted:1` |

### Date operators

| Operator | Description | Example |
|----------|-------------|---------|
| : | The field must equal the literal | `timestamp:2020-01-01` |
| := | The field must equal the literal | `timestamp:=2020-01-01T12:13:45Z` |
| :> | The field must be less than literal | `timestamp:>2020-01-01T00:00:00Z` |
| :&lt; | The field must be greater than literal | `timestamp:<2020-12-31T23:59:59+12:00` |

### Logical operators

| Operator | Description | Example |
|----------|-------------|---------|
| AND | Match if both terms are verified | `timestamp:>2020-01-01T00:00:00Z AND type:$"ware"` |
| OR | Match if any terms are verified | `timestamp:>2020-01-01T00:00:00Z OR type:^"mal"` |
| NOT | Inverse the result of the term | `NOT type:^"mal"` |

### Grouping operators

| Operator | Description | Example |
|----------|-------------|---------|
| () | Groups operands | `(timestamp:>2020-01-01T00:00:00Z OR type:$"ware") AND NOT type:^"mal"` |
