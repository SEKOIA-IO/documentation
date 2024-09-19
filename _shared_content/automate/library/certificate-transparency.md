# Certificate Transparency

![Certificate Transparency](/assets/playbooks/library/certificate-transparency.png){ align=right width=150 }

[Certificate transparency](https://certificate.transparency.dev/) is a security standard to monitor and audit certificates. This module rely on [certstream](https://certstream.calidog.io/) to get updates from the Certificate Transparency Log network.

## Configuration

This module accepts no configuration.

## Triggers

### Certificate update

Trigger playbook run on certificate of interest update

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `keywords` | `array` | The keywords you're looking for. Please consider splitting composite words into two keywords when max_distance > 0. |
| `max_distance` | `integer` | The maximum Levenshtein distance acceptable. It is the number of modification you have to do to go from a word to another. E.g. sekoia -> sequoia => 2 |
| `ignoring` | `array` | Ignoring words list for faster processing. |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` | The domain that matched |
| `matched_keyword` | `string` | The keyword that matched |
| `certstream_object` | `object` | The certstream object the domain comes from |


## Extra

Module **`Certificate Transparency` v1.24**