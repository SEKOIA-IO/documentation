# Sigma Rules

Sigma is a generic and open format you can use to write signatures that will be applied to your event stream in real-time. This format makes it easy to write rules applicable to any field available in normalized events. Rules are documents using the YAML format.
## Detection Object
Each rule should contain a `detection` object using a set of `Search-Identifier`s to define a matching `condition`:
```yaml
detection:
  <Search-Idenfier>
    <string-list>
    <field:value>
  condition: <Condition>
```
`<Search-Identifier>` is a unique identifier that will be used in `<Condition>`. A `<Search-Idenfier>` can contain two different structures: **Maps** and **Lists**.

### Maps
Maps consist of key/value pairs in which the key is the name of a field in your normalized event. The value is the value that should be present in this field for the `Search-Identifier` to match. Several values can be specified at once, in which case they are joined together with a logical `OR`.

The keys of a map are joined together with a logical `AND`.

**Example** : Raise an alert when an event contains `event.type: allowed` and the `destination.ip` is either `1.2.3.4` or `4.3.2.1`

```yaml
detection:
  selection:
    event.type: allowed
    destination.ip:
      - 1.2.3.4
      - 4.3.2.1
  condition: selection
```
### Lists
A list contains one or more items that are joined together with a logical `OR`.
Lists of strings can be used to define any string that should be present in the whole event `message`:

**Example**: Raise an alert when an event contains `DangerousThreat.exe` or `powershell.exe maliciousfile.ps1`

```yaml
detection:
  keywords:
    - DangerousThreat.exe
    - powershell.exe maliciousfile.ps1
  condition: keywords
```

You can also use lists of maps to combine several maps with a logical `OR`.

**Example**: Raise an alert when a specific IP address is seen as a source or a destination:

```yaml
detection:
  selection:
    - source.ip: 6.6.6.6
    - destination.ip: 6.6.6.6
  condition: selection
```

### Values
Some things to know about values used in Sigma rules:

- All values are treated as case-insensitive strings
- You can use wildcard characters (`*` means any number of characters, `?` means any one character)
- You don't have to escape characters, except `'`, `*` and `?`. A single backslash `\` does not need to be escaped, but can be (`\` is the same as `\\`)
- You can use `''` to define an empty value
- You can use `null` to define a null value

### Value Modifiers
The values contained in Sigma rules can be modified with modifiers. Value modifiers are appended after the field name with a pipe character `|` and can be chained.
Here is the list of supported modifiers:

- `contains`: puts \* wildcards around the values, such that the value is matched anywhere in the field
- `all`: link values of a list with a logical `AND`
- `base64`: match the value encoded with Base64
- `endswith`: the value is expected at the end of the field's content (replaces e.g. `*\cmd.exe`)
- `startswith`: the value is expected at the beginning of the field's content. (replaces e.g. `adm*`)
- `re`: the value is a [regular expression](https://github.com/google/re2/wiki/Syntax). Regular expressions are case sensitive by default
- `cidr`: the value is a subnet in CIDR notation (e.g. `192.168.1.0/24`) the IP address should belong to
- `lt`: less than this value
- `lte`: less than or equal to this value
- `gt`: greater than this value
- `gte`: greater or equal to this value

**Example**: Raise an alert when the URL matches specified regex and the command line contains all specified values

```yaml
detection:
  selection:
    url.original|re: ".*(php|aspx)$"
    process.command_line|contains|all:
      - evil_arg1
      - evil_arg2
      - evil_arg3
  condition: selection
```

### Condition
The `condition` defines how `Search-Identifier`s should be combined to determine if the rule matched.
It supports the following expressions:

- Logical `AND`/`OR`

  **Example**: `selection1 or (selection2 and selection3)`

- `1/all of them`

  `1 of them` will link all the `Search-Identifier`s with a logical OR.

  `all of them` will link all the `Search-Identifier`s with a logical AND.

- `1/all of <Search-Identifier-Pattern>`

  It is the same as `1/all of them` but restricted to the Pattern defined. The pattern is written with wildcards `*` which means any number of characters.

  **Example** : Let's suppose we have 4 `Search-Identifier`s: `selection1`, `selection2`, `selection3` and `pattern`. The condition can be `1 of selection* and pattern`.

- Negation with `not`
  
  **Example**: `selection1 and not selection2`
  
  Now if in that example selection2 is simply `process.parent.name: 'test'` for instance, **Note that you might need to put in selection1 an "exists" value for the field you are excluding**:
  ```
  selection1:
    process.parent.name: '*'
  ```
  Otherwise the rule will also raise an alert if the field `process.parent.name` does not exist. Sometimes it is not an issue, however it can be in case of high false positives without that field for instance.

## Correlation
Detection objects apply a signature to a single event to determine if there is a match. What if you want to create more complex signatures that would require several events to match? You can do this with Sigma Correlation rules.
Sigma Correlation rules are also Yaml documents that allow the expression of aggregations and relationships between `detection` objects.
A correlation document has the following attributes:

- `action` set to `correlation`
- `type` is the [correlation type](#correlation-types)
- `rule` refers to one or multiple Sigma rules or correlations (allowing definition of chains of correlations) defining events to be correlated
- `group-by` optionally defines one or multiple fields which should be treated as separate event occurrence scope (example: count events by user)
- `timespan` defines a time period in which the correlation should be applied (such as `5m` or `1h`). This value can currently be set up to a maximum of `24h`.

Further fields might be required depending on the correlation type.

### Correlation Types

#### Event Count (`event_count`)
Counts events matching a given detection `rule` during the specified `timespan`, grouping events by the optional `group-by` fields. An alert is created when the count matches the specified `condition`.
**Example**: Raise an alert when a `user.name` fails to log in more than 5 times in the space of 5 minutes.

```yaml
name: login_failed
detection:
  selection:
    event.category: authentication
    event.outcome: failure
  condition: selection
---
action: correlation
type: event_count
rule: login_failed
group-by: user.name
timespan: 5m
condition:
  gte: 5
```

#### Value Count (`value_count`)
Counts the number of unique values in a field defined by `field`. Only events matching a given `rule` during the specified `timespan` are considered. Events are grouped by the optional `group-by` fields. An alert is created when the count matches the specified `condition`.
**Example**: Raise an alert when a `user.name` fails to log in to more than 5 different `log.hostname` in the space of 5 minutes.

```yaml
name: login_failed
detection:
  selection:
    event.category: authentication
    event.outcome: failure
  condition: selection
---
action: correlation
type: value_count
rule: login_failed
group-by: user.name
timespan: 5m
field: log.hostname
condition:
  gte: 5
```

#### Temporal Proximity (`temporal`)
All events defined by the rules referred to by the `rule` field must occur in the time frame defined by `timespan`. The values of fields defined in `group-by` must all have the same value. If the bool value `ordered` is set to `true`, events should also occur in the correct order.
**Example**: Raise an alert when a `user.name` uses two common reconnaissance commands in quick succession on the same host.

```yaml
name: quser
detection:
  selection:
    process.command_line|startswith: quser
  condition: selection
---
name: dir
detection:
  selection:
    process.command_line|startswith: dir
  condition: selection
---
action: correlation
type: temporal
rule:
  - quser
  - dir
group-by:
  - user.name
  - log.hostname
timespan: 1m
ordered: false
```

### Conditions
The field `condition` defined the condition that must be met to raise an alert. It operates on the count resulting from and `event_count` or `value_count` correlation. It is a map of exactly one condition criteria:

- `gt`: the count must be greater than the given value
- `gte`: the count must be greater than or equal to the given value

### Chaining
Correlation rules can be chained together to create even more complex detection logic. This means the `rule` attribute of a correlation document can refer to another correlation rule.
**Example**: Raise an alert when a `user.name` fails to log in more than 5 times on the same host and then succeeds, within 10 minutes.

```yaml
name: login_failed
detection:
  selection:
    event.category: authentication
    event.outcome: failure
  condition: selection
---
name: login_success
detection:
  selection:
    event.category: authentication
    event.outcome: success
  condition: selection
---
name: many_failed_logins
action: correlation
type: event_count
rule: login_failed
group-by:
  - user.name
  - log.hostname
timespan: 10m
condition:
  gte: 5
---
action: correlation
type: temporal
rule:
  - many_failed_logins
  - login_success
group-by:
  - user.name
  - log.hostname
timespan: 10m
ordered: true
```

### Grouping events from different fields
In some cases, you may want to correlate events from different sources of information that have the `group-by` value in different fields. In that case, you can use the `aliases` document to specify which fields should be considered for each `rule`.

**Example**: Raise an alert when a successful login is followed by a new network connection with the same couple `source.ip`, `destination.ip`.

```yaml
name: login_success
detection:
  selection:
    event.category: authentication
    event.outcome: success
  condition: selection
---
name: new_network_connection
detection:
  selection:
    event.category: network
    event.type: connection
    event.outcome: success
  condition: selection
---
action: correlation
type: temporal
rule:
  - login_success
  - new_network_connection
group-by:
  - internal_ip
  - remote_ip
timespan: 5m
ordered: true
aliases:
  internal_ip:
    login_success: destination.ip
    new_network_connection: source.ip
  remote_ip:
    login_success: source.ip
    new_network_connection: destination.ip
```
