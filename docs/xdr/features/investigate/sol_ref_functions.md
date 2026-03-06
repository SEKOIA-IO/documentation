# Reference: Functions

## Datetime: now()

**Description**

Returns the current **UTC** time, optionally offset by a given timespan.

**Example**

``` shell
let time = now();

let time_earlier = now(-2d);

```

---

## Datetime: ago()

**Description**

Returns a datetime value equal to the current UTC time minus the timespan.

| Syntax | Description | Example | Length of time |
| --- | --- | --- | --- |
| d | day time interval | `2d` | 2 days |
| h | hour time interval | `1h` | 1 hour |
| m | minute time interval | `30m` | 30 minutes |
| s | second time interval | `10s` | 10 seconds |

**Example**

``` shell
let time = ago(1h);

```

---

## Timestamp: bin()

**Description**

Rounds values down to an integer multiple of a given bin size.

**Example**

``` shell
events
| aggregate count() by bin(timestamp, 1d)

```

---

## Year

**Description**

Returns the year by a given date in the following format: `YYYY`.

**Example**

``` shell
let time = year(now());

```

---

## Month

**Description**

Returns the year and month by a given date in the following format: `YYYY-MM`.

**Example**

``` shell
let time = month(now());

```

---

## Week

**Description**

Returns the year and month by a given date in the following format: `YYYY - Week {week number}`.

**Example**

``` shell
let time = week(now());

```

---

## To scalar

**Description**

Use the `toscalar` function to return a constant value of a statement.

**Example**

``` shell
let total = toscalar(alerts | where created_at >= ago(7d) | count);

alerts
| where created_at >= ago(7d)
| aggregate count() by detection_type
| extend percentage = (count / total) * 100

```

---

## String: tolower()

**Description**

Converts a string to lowercase. This function is useful for normalizing text data for case-insensitive comparisons and analysis.

**Syntax**

``` shell
tolower(<string>)
```

**Parameters**

- `string`: A string value to be converted to lowercase

**Return Value**

Returns the lowercase version of the input string.

**Example**

Normalize user names to lowercase for consistent analysis:

``` shell
events
| where timestamp > ago(24h) and user.name != null
| aggregate count_by_user = count() by user.name
| aggregate sum(count_by_user) by normalized_user = tolower(user.name)
| limit 100
```

---

## String: toupper()

**Description**

Converts a string to uppercase. This function is useful for normalizing text data for case-insensitive comparisons and analysis.

**Syntax**

``` shell
toupper(<string>)
```

**Parameters**

- `string`: A string value to be converted to uppercase

**Return Value**

Returns the uppercase version of the input string.

**Example**

Normalize command lines to uppercase for consistent analysis:

``` shell
events
| where timestamp > ago(24h) and process.command_line != null
| aggregate count_by_cmd = count() by process.command_line
| aggregate sum(count_by_cmd) by normalized_cmd = toupper(process.command_line)
| limit 100
```

---

## String: extract()

**Description**

Extracts a match for a regular expression from a string. Optionally targets a specific capture group. This function is useful for parsing structured data from free-text fields such as URLs, log messages, or command lines.

**Syntax**

``` shell
extract(<regex>, <capture_group>, <source>)
```

**Parameters**

- `regex`: A regular expression pattern to match against the source string (required). Use the `@` prefix for raw string literals to avoid double-escaping backslashes (e.g., `@'https?://([^/]+)'`).
- `capture_group`: The capture group index to extract (required). `0` returns the entire match; `1` returns the first parenthesized group; `2+` for subsequent groups.
- `source`: The string to search (required)

**Return Value**

Returns the matched substring for the specified capture group. Returns `null` if the regex finds no match.

**Example 1**

Extract the domain from a URL:

``` shell
events
| where timestamp > ago(24h) and url.original != null
| select timestamp, domain = extract(@'https?://([^/]+)', 1, url.original)
| limit 100
```

**Example 2**

Extract user identifiers from log messages:

``` shell
events
| where timestamp > ago(24h) and message != null
| select timestamp, user_id = extract(@'user_(\d+)', 1, message)
| where user_id != null
| limit 100
```

---

## String: replace_regex()

**Description**

Replaces all matches of a regular expression in a string with a specified replacement pattern. This function is useful for sanitizing, normalizing, or transforming string data in security investigations.

**Syntax**

``` shell
replace_regex(<source>, <lookup_regex>, <rewrite_pattern>)
```

**Parameters**

- `source`: The source string to search and replace within (required)
- `lookup_regex`: The regular expression to search for (required). Can contain capture groups in parentheses. Use the `@` prefix for raw string literals to avoid double-escaping backslashes.
- `rewrite_pattern`: The replacement pattern (required). Use `$0` for the whole match, `$1` for the first capture group, `$2` for the second, etc.

**Return Value**

Returns the modified string with all non-overlapping matches replaced. If no matches are found, the original string is returned unchanged.

**Example 1**

Strip the protocol from URLs:

``` shell
events
| where timestamp > ago(24h) and url.original != null
| select timestamp, cleaned_url = replace_regex(url.original, @'https?://', '')
| limit 100
```

**Example 2**

Sanitize email addresses in logs:

``` shell
events
| where timestamp > ago(24h) and user.email != null
| select timestamp, sanitized_email = replace_regex(user.email, @'(\w+)@.*', '$1@example.com')
| limit 100
```

---

## Math: round()

**Description**

Rounds a number to a specified precision (number of decimal places). This function is useful for formatting numerical results and creating cleaner reports with rounded values.

**Syntax**

``` shell
round(<number> [, <precision>])
```

**Parameters**

- `number`: The number to round (required)
- `precision`: Number of decimal places to round to (optional, defaults to 0)

**Return Value**

Returns the rounded number to the specified precision.

**Example**

Round time_to_detect values to 2 decimal places for cleaner reporting:

``` shell
alerts
| where created_at > ago(7d)
| select ttd_minutes = round(time_to_detect / 60.0, 2)
| limit 100
```

---

## Type conversion: toint()

**Description**

Converts a value to a signed 32-bit integer representation. This function is useful for converting string fields to numeric values for comparisons, calculations, or filtering.

**Syntax**

``` shell
toint(<value>)
```

**Parameters**

- `value`: The value to convert to an integer (required). Can be a string, float, or other scalar type.

**Return Value**

Returns the integer representation of the value. Returns `null` if the conversion fails (e.g., non-numeric string).

If the input is a decimal number, the value is truncated to the integer portion (e.g., `toint(2.9)` returns `2`).

**Example 1**

Convert a string field to integer for numeric comparison:

``` shell
events
| where timestamp > ago(24h)
| select port_number = toint(destination.port)
| where port_number > 1024
| limit 100
```

**Example 2**

Convert and aggregate by numeric field:

``` shell
events
| where timestamp > ago(24h)
| extend severity_int = toint(event.severity)
| aggregate count() by severity_int
| order by severity_int desc
```

---

## Conditional: iff()

**Description**

Returns a value based on a conditional expression. Evaluates a boolean condition and returns one value if the condition is true, another value if the condition is false. This function is useful for data categorization and conditional transformations.

**Syntax**

``` shell
 iff(<condition>, <then_value>, <else_value>)
```

**Parameters**

- `condition`: A boolean expression to evaluate (required)
- `then_value`: Value returned if condition is true (required)
- `else_value`: Value returned if condition is false (required)

**Return Value**

Returns the `then_value` when condition is true, otherwise returns `else_value`.

**Example**

Categorize alerts based on urgency and time to detect:

``` shell
alerts
| where created_at > ago(7d)
| aggregate count() by severity_category = iff(urgency >= 80, "Critical",
    iff(urgency >= 50, "High", "Medium"))
| limit 100
```

---

## Null handling: coalesce()

**Description**

Returns the first non-null value from a list of expressions. This function is useful for providing fallback values when dealing with potentially null data, ensuring queries can handle missing or incomplete information gracefully.

**Syntax**

``` shell
coalesce(<arg1>, <arg2>, [<arg3>, ...])
```

**Parameters**

- `arg1, arg2, ...`: A list of expressions of the same type to evaluate (at least 2 arguments required)

**Return Value**

Returns the first non-null value from the argument list, or null if all arguments are null.

**Example**

Provide fallback values for user identification when some fields might be null:

``` shell
events
| where timestamp > ago(24h)
| aggregate count() by user_identifier = coalesce(user.name, user.email, "Unknown")
| limit 100
```

---

## Datetime: format_datetime()

**Description**

Formats datetime values using Python strftime format specifiers, enabling flexible datetime representation in SOL queries. Supports both datetime objects and ISO format datetime strings.

**Syntax**

``` shell
format_datetime(<datetime>, <format>)
```

**Parameters**

- `datetime`: Datetime object (from functions like `now()`) or ISO format string to format (required)
- `format`: String specifying the output format using Python strftime specifiers (required)

**Return Value**

Returns a formatted string representation of the datetime.

**Common Format Specifiers**

| Specifier | Description | Example |
|-----------|-------------|---------|
| `%Y` | 4-digit year | 2025 |
| `%m` | Month (01-12) | 12 |
| `%d` | Day of month (01-31) | 25 |
| `%H` | Hour (00-23) | 14 |
| `%M` | Minutes (00-59) | 30 |
| `%S` | Seconds (00-59) | 45 |
| `%B` | Full month name | December |
| `%b` | Abbreviated month | Dec |
| `%A` | Full weekday name | Monday |

**Example**

Format timestamps for cleaner reporting:

``` shell
alerts
| where created_at > ago(24h)
| extend date_only = format_datetime(created_at, '%Y-%m-%d')
| extend readable_time = format_datetime(created_at, '%B %d, %Y at %H:%M')
| extend eu_format = format_datetime(created_at, '%d-%m-%Y')
| aggregate count() by date_only, readable_time, eu_format, detection_type
| limit 100
```

---

## Aggregation: countif()

**Description**

Counts the number of rows for which a predicate evaluates to `true`. This function is used within the `aggregate` operator and is useful for computing conditional counts in a single query, such as counting successes and failures side by side.

**Syntax**

``` shell
countif(<predicate>)
```

**Parameters**

- `predicate`: A boolean expression to evaluate for each row (required). Rows where this evaluates to `true` are counted; rows where it evaluates to `false` or `null` are not counted.

**Return Value**

Returns the count of rows for which the predicate is `true`. Returns `0` if no rows match.

**Example 1**

Count successful and failed login attempts per source IP:

``` shell
events
| where timestamp > ago(24h) and event.category == 'authentication'
| aggregate success_count = countif(event.code == '4624'), failed_count = countif(event.code == '4625') by source.ip
| order by failed_count desc
| limit 100
```

**Example 2**

Count high-urgency vs. low-urgency alerts per detection type:

``` shell
alerts
| where created_at > ago(7d)
| aggregate high = countif(urgency >= 80), low = countif(urgency < 80) by detection_type
```
