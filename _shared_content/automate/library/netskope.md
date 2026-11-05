uuid: 1e3f2e33-fb9c-4387-bcf7-8d7ece37f913
name: Netskope
type: playbook

# Netskope

![Netskope](/assets/playbooks/library/netskope.png){ align=right width=150 }

Netskope is a cybersecurity company, providing solutions to protect data in cloud apps and network security applying zero trust principles.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | API base URL |

## Actions

### Append to Blocklist

Append IP addresses, domains, or URLs to an existing Netskope blocklist

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | API token for authentication |
| `blocklist_id` | `string` | The ID of the blocklist |
| `blocklist_type` | `string` | The type of the blocklist (exact, regex) |
| `items` | `array` | List of items in the blocklist (IPs, domains, or URLs) |
| `sort_items` | `boolean` | Sort items alphabetically |

### Get Blocklist

Retrieve an existing Netskope blocklist

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | API token for authentication |
| `blocklist_id` | `string` | The ID of the blocklist |

### Remove From Blocklist

Remove one or more items from an existing Netskope blocklist

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | API token for authentication |
| `blocklist_id` | `string` | The ID of the blocklist |
| `items` | `array` | List of items in the blocklist (IPs, domains, or URLs) |
| `sort_items` | `boolean` | Sort items alphabetically |

### Replace Blocklist

Replace an entire Netskope blocklist with new items

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_token` | `string` | API token for authentication |
| `blocklist_id` | `string` | The ID of the blocklist |
| `blocklist_type` | `string` | The type of the blocklist (exact, regex) |
| `items` | `array` | List of items in the blocklist (IPs, domains, or URLs) |
| `sort_items` | `boolean` | Sort items alphabetically |


## Extra

Module **`Netskope` v1.16.1**