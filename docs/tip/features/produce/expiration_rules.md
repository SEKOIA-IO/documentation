# Expiration Rules

Indicators don’t stay valid forever. For most of them, they have a defined validity period. 

When creating/adding an Indicator to a Content Proposal, analysts have to provide a `valid_from` (required) and `valid_until` (optional) date which is the time from which this Indicator is considered a valid indicator of the behaviors it is related to or represents.

This is when Expiration Rules come to play. They have been designed to set default validity periods for Indicators depending on the type of observable they related to. 

### Default Expiration Rules

By default, these validity periods are: 

| Observable type | Time to live |
| --- | --- |
| URL | 6 months |
| IPv4 | 1 month |
| IPv6 | 1 month |
| Domain name | 6 months |
| Others | 6 months |
| File (hash) | 5 years |

### Example

When importing an IP address into a Content Proposal, if you don't change the fields corresponding to the validity date, it will be automatically set to 1 month in the CTI database.
