---
title: # Datetime
---

# Datetime


## Representation

In the events, Sekoia.io accepts any representation of a datetime:

- as a string representation:
	- [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) representation
	- [RFC3339](https://www.ietf.org/rfc/rfc3339.html) representation
	- [C-formatted datetime representation](#c-formatted) in the English locale
- as a timestamp representation with any precision (from second precision to nanosecond precision)

### C formatted

The following is a list of all the format codes that the C89 standard requires.
These work on all platforms with a standard C-based implementation.

| Directive   | Meaning                                                          | Example                                      |
|-------------|------------------------------------------------------------------|----------------------------------------------|
| ``%a``      | Weekday                                                          | Sun, Mon, ..., Sat                           |
| ``%A``      | Weekday full name.                                               | Sunday, Monday, ..., Saturday                |
| ``%w``      | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday | 0, 1, ..., 6                                 |
| ``%d``      | Day of the month as a  zero-padded decimal number.               | 01, 02, ..., 31                              |
| ``%b``      | Month as abbreviated name.                                       | Jan, Feb, ..., Dec                           |
| ``%B``      | Month full name.                                                 | January, February, ..., December             |
| ``%m``      | Month as a zero-padded decimal number                            | 01, 02, ..., 12                              |
| ``%y``      | Year without century as a zero-padded decimal number.            | 00, 01, ..., 99                              |
| ``%Y``      | Year with century as a decimal number                            | 0001, 0002, ..., 2013, 2014, ..., 9998, 9999 |
| ``%H``      | Hour (24-hour clock) as a zero-padded decimal number.            | 00, 01, ..., 23                              |
| ``%I``      | Hour (12-hour clock) as a zero-padded decimal number.            | 01, 02, ..., 12                              |
| ``%p``      | AM or PM                                                         | AM, PM                                       |
| ``%M``      | Minute as a zero-padded decimal number                           | 00, 01, ..., 59                              |
| ``%S``      | Second as a zero-padded decimal number                           | 00, 01, ..., 59                              |
| ``%f``      | Microsecond as a decimal number. zero-padded to 6 digits         | 000000, 000001, ..., 99999                   |
| ``%z``      | UTC offset in the form ``±HHMM[SS[.ffffff]]``                    | (empty), 0000, 063415, -030712.345216        |
| ``%Z``      | Time zone name                                                   | (empty), UTC, GMT                            |
| ``%j``      | Day of the year as a zero-padded decimal number                  | 001, 002, ..., 366                           |
| ``%U``      | Week number of the year as a zero-padded decimal number          | 00, 01, ..., 53                              |
| ``%W``      | Week number of the year as a zero-padded decimal number          | 00, 01, ..., 53                              |

## Timezone 

The datetime must satisfy one of the following conditions:

- a string representation with a timezone (like ISO8601 or RFC3339 strings)
- a string representation or a timestamp representation together with a timezone in the event
- a string representation or a timestamp representation in the UTC timezone



