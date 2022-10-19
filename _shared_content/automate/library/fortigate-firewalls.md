# Fortigate Firewalls

Fortigate is a firewall appliance from [Fortinet](http://www.fortinet.com/) with anti-spam and anti-virus features. Initially distributed as a physical, rack-mounted product, Fortigate can now be installed as a virtual appliance that could run on virtualization platforms such as VMware vSphere.

With the Fortigate module, you'll be able to:

- Add an IP in the Address list of a Fortigate FW: [Post Fortigate IP Address](#post-fortigate-ip-address)
- Add a FQDN in the Address list of a Fortigate FW: [Post Fortigate FQDN Address](#post-fortigate-fqdn-address)
- Create a Group with an Address member: [Post Fortigate Address Group](#post-fortigate-address-group)

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `firewalls` | `array` |  |

## Actions

### Post Fortigate Address Group

Add a new Address Group to a Fortigate Firewall.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address Group. |
| `member` | `array` | The Object LIST to be added in the Address Group (can be an IP address, a FQDN or event a Group), for example Address1 |

### Post Fortigate FQDN Address

Add a new FQDN object to a Fortigate Firewall.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address. |
| `fqdn` | `string` | The FQDN to be blocked (for ex: 'example.domain.com'). |
| `associated-interface` | `string` | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| `comment` | `string` | A commentary to be displayed in the Fortigate GUI (default none). |

### Post Fortigate IP Address

Add a new IP Address object to a Fortigate Firewall.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` | The name of the Address. |
| `ip` | `string` | The IPv4 linked with the Address to be blocked, (for ex: '1.1.1.1'). |
| `associated-interface` | `string` | The associated interface of the firewall leave blank for 'Any' (default: Any). |
| `comment` | `string` | A commentary to be displayed in the Fortigate GUI (default none). |


## Extra

Module **`Fortigate Firewalls` v1.15**
