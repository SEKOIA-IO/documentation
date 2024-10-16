uuid: ca9a9497-bcd2-4d0c-b0c1-72699231feb2
name: Fortigate Firewalls
type: playbook

# Fortigate Firewalls

![Fortigate Firewalls](/assets/playbooks/library/fortigate-firewalls.svg){ align=right width=150 }

Fortigate is a firewall appliance from [Fortinet](http://www.fortinet.com/) with anti-spam and anti-virus features. Initially distributed as a physical, rack-mounted product, Fortigate can now be installed as a virtual appliance that could run on virtualization platforms such as VMware vSphere

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `firewalls` | `array` |  |

## Actions

### Post Fortigate Address Group

Add a new Address Group to a Fortigate Firewall

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address Group. |
| `member` | `array` | The Object LIST to be added in the Address Group (can be an IP address, a FQDN or event a Group), for example Address1 |

### Post Fortigate FQDN Address

Add a new FQDN object to a Fortigate Firewall

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address. |
| `fqdn` | `string` | The FQDN to be blocked (for ex: 'example.domain.com'). |
| `associated-interface` | `string` | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| `comment` | `string` | A commentary to be displayed in the Fortigate GUI (default none). |

### Post Fortigate IP Address

Add a new IP Address object to a Fortigate Firewall

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address. |
| `ip` | `string` | The IPv4 linked with the Address to be blocked, (for ex: '1.1.1.1'). |
| `associated-interface` | `string` | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| `comment` | `string` | A commentary to be displayed in the Fortigate GUI (default none). |


## Extra

Module **`Fortigate Firewalls` v1.29.0**