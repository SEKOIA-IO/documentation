uuid: ab1540c3-1b60-4bad-9f5b-13d86a554826
name: RiskIQ
type: playbook

# RiskIQ

![RiskIQ](/assets/playbooks/library/riskiq.png){ align=right width=150 }

RiskIQ is a cyber security company providing software as a service to detect phishing, fraud, malware, and other online security threats.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | RiskIQ base url |
| `api_key` | `string` | API key |
| `api_secret` | `string` | API secret |

## Actions

### SSL Hosts

Get hosts by certificate

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `certSha1` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `array` |  |
| `first` | `boolean` |  |
| `last` | `boolean` |  |
| `number` | `integer` |  |
| `numberOfElements` | `integer` |  |
| `size` | `integer` |  |
| `sort` | `string` |  |
| `totalElements` | `integer` |  |
| `totalPages` | `integer` |  |

### Hex Passive DNS

Retrieve results by searching for specified hexadecimal bytes within PDNS record data field.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` |  |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |
| `hex` | `string` | Hexadecimal encoding of data field bytes |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### IP Passive DNS

Retrieve results by searching for specified IP address within PDNS record data field

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` |  |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### Name Passive DNS

Retrieve results by searching for specified resource name within PDNS record data field.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |
| `type` | `string` | DNS resource record type |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### SSL Certificates by Host

Get SSL certificates by host name

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `host` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `array` |  |

### SSL Certificates by Name

Get SSL certificates by name

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `array` |  |
| `first` | `boolean` |  |
| `last` | `boolean` |  |
| `number` | `integer` |  |
| `numberOfElements` | `integer` |  |
| `size` | `integer` |  |
| `sort` | `string` |  |
| `totalElements` | `integer` |  |
| `totalPages` | `integer` |  |

### SSL Certificates by Serial Number

None

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `serial` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `array` |  |
| `first` | `boolean` |  |
| `last` | `boolean` |  |
| `number` | `integer` |  |
| `numberOfElements` | `integer` |  |
| `size` | `integer` |  |
| `sort` | `string` |  |
| `totalElements` | `integer` |  |
| `totalPages` | `integer` |  |

### SSL Certificats by SHA-1

Get SSL certificate by SHA1 hash

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sha1` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `count` | `integer` |  |
| `firstSeen` | `string` |  |
| `id` | `string` |  |
| `issuer` | `array` |  |
| `issuerAlternativeNames` | `array` |  |
| `issuerID` | `string` |  |
| `lastSeen` | `string` |  |
| `notAfter` | `string` |  |
| `notBefore` | `string` |  |
| `publicKeyAlgorithm` | `string` |  |
| `serialNumber` | `string` |  |
| `sha1` | `string` |  |
| `signatureAlgorithm` | `string` |  |
| `signatureAlgorithmOid` | `string` |  |
| `subject` | `array` |  |
| `subjectAlternativeNames` | `array` |  |
| `subjectID` | `string` |  |
| `version` | `integer` |  |

### Reverse Whois (address)

Get WHOIS records associated with an address

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `address` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Whois

Get the current WHOIS for a domain

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |
| `Authorization` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois (email)

Get WHOIS records associated with an email address

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `email` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois (name)

Get WHOIS records associated with a name

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois (nameserver)

Get WHOIS records associated with a name server

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `nameserver` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois (organization)

Get WHOIS records associated with an organization

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `org` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois (phone)

Get WHOIS records associated with a phone number

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `phone` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |


## Extra

Module **`RiskIQ` v1.25.1**