# RiskIQ

![RiskIQ](/assets/playbooks/library/riskiq.png){ align=right width=150 }

[RiskIQ](https://www.riskiq.com/) is a cyber security company providing software as a service to detect phishing, fraud, malware, and other online security threats.

The module allows to request information such as:

- [Whois](#whois)
- Reverse Whois ([organization](#organization), [name server](#Name-server), [name](#name), [email](#email), [address](#address), [phone](#phone))
- Passive DNS ([Name](#name-passive-dns), [IP](#ip-passive-dns), [Hex](#hex-passive-dns))
- [SSL hosts](#ssl-hosts), 
- SSL Certificates ([Host](#ssl-certificates-by-host), [name](#ssl-Certificates-by-name), [SHA-1](#ssl-certificates-by-SHA-1), [Serial Number](#ssl-certificates-by-serial-number))


## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `base_url` | `string` | RiskIQ base url |
| `api_key` | `string` | API key |
| `api_secret` | `string` | API secret |

## Actions

### SSL Hosts

Get hosts by certificate.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `certSha1` | `string` |  |


#### Outputs

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

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `type` | `string` |  |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |
| `hex` | `string` | Hexadecimal encoding of data field bytes |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### IP Passive DNS

Retrieve results by searching for specified IP address within PDNS record data field.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` |  |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### Name Passive DNS

Retrieve results by searching for specified resource name within PDNS record data field.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |
| `type` | `string` | DNS resource record type |
| `max` | `string` |  |
| `lastSeenAfter` | `string` |  |
| `firstSeenBefore` | `string` |  |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `recordCount` | `integer` |  |
| `records` | `array` |  |

### SSL Certificates by Host

Get SSL certificates by host name.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `host` | `string` |  |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `content` | `array` |  |

### SSL Certificates by Name

Get SSL certificates by name.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |


#### Outputs

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

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `serial` | `string` |  |


#### Outputs

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

Get SSL certificate by SHA-1 hash.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `sha1` | `string` |  |


#### Outputs

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

### Whois

Get the current WHOIS for a domain.

#### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |
| `Authorization` | `string` |  |


#### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

### Reverse Whois 

#### Address

Get WHOIS records associated with an address.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `address` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |


#### Email

Get WHOIS records associated with an email address.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `email` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

#### Name

Get WHOIS records associated with a name.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `name` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

#### Name server

Get WHOIS records associated with a name server.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `nameserver` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

#### Organization

Get WHOIS records associated with an organization.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `org` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |

#### Phone

Get WHOIS records associated with a phone number.

##### Arguments

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `phone` | `string` |  |
| `exact` | `string` |  |
| `maxResults` | `string` |  |


##### Outputs

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `results` | `integer` |  |
| `domains` | `array` |  |


## Extra

Module **`RiskIQ` v1.14**
