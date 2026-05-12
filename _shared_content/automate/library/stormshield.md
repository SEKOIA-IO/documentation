uuid: 59498b29-5cfb-46e6-aaf1-9c0c3afeb00c
name: Stormshield
type: playbook

# Stormshield

![Stormshield](/assets/playbooks/library/stormshield-ses.png){ align=right width=150 }

Stormshield Network Security is a range of network security appliances.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | Base URL of the Stormshield SNS API |
| `api_token` | `string` | Authentication token for the API |

## Actions

### Block IP address

Block an IPv4 or IPv6 address on Stormshield SNS.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip_address` | `string` | IPv4 or IPv6 address to block |
| `duration_s` | `integer` | Duration in seconds for which the IP should be blocked |

**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` |  |
| `ip_address` | `string` |  |
| `duration_s` | `integer` |  |
| `message` | `string` |  |
| `response` | `object` |  |
