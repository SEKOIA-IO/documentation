uuid: 25c9c44e-b3dc-4485-a2cb-4e9a116bc8fd
name: Shodan
type: playbook

# Shodan

![Shodan](/assets/playbooks/library/shodan.png){ align=right width=150 }

[Shodan](https://www.shodan.io/) is a Cybersecurity company keeping track of devices exposed to the Internet. It collect information on devices, running software and related CVEs.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | The user API key |
| `base_url` | `string` | Shodan base url, like https://api.shodan.io/. |

## Actions

### Get DNS domain

Get all the subdomains and other DNS entries for the given domain. Uses 1 query credit per lookup.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` | Domain name to lookup; example "cnn.com". |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `domain` | `string` |  |
| `tags` | `array` |  |
| `data` | `array` |  |

### Lookup IPs

Look up the IP address for the provided list of hostnames.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `hostnames` | `array` | List of hostnames; example "google.com". |

### Lookup DNS

Look up the hostnames that have been defined for the given list of IP addresses.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ips` | `array` | List of IP addresses; example "74.125.227.230" |

### Get Host

Returns all services that have been found for the given host IP.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip` | `string` | Host IP address |
| `history` | `boolean` | True if all historical banners should be returned (default: False)  |
| `minify` | `boolean` | True to only return the list of ports and the general host information, no banners. (default: False)  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `region_code` | `string` |  |
| `ip` | `string` |  |
| `area_code` | `string` |  |
| `country_name` | `string` |  |
| `hostnames` | `array` |  |
| `postal_code` | `string` |  |
| `dma_code` | `string` |  |
| `country_code` | `string` |  |
| `data` | `array` |  |
| `city` | `string` |  |
| `longitude` | `number` |  |
| `country_code3` | `string` |  |
| `latitude` | `number` |  |
| `os` | `string` |  |
| `ports` | `array` |  |

### Count Hosts

This method behaves identical to "/shodan/host/search" with the only difference that this method does not return any host results, it only returns the total number of results that matched the query and any facet information that was requested. As a result this method does not consume query credits.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Shodan search query. The provided string is used to search the database of banners in Shodan, with the additional option to provide filters inside the search query using a "filter:value" format. For example, the following search query would find Apache webservers located in Germany: "apache country:DE". |
| `facets` | `string` | A comma-separated list of properties to get summary information on. Property names can also be in the format of "property:count", where "count" is the number of facets that will be returned for a property (i.e. "country:100" to get the top 100 countries for a search query). |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `matches` | `array` |  |
| `facets` | `object` |  |
| `total` | `integer` |  |

### Search Host

Search Shodan using the same query syntax as the website and use facets to get summary information for different properties.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Shodan search query. The provided string is used to search the database of banners in Shodan, with the additional option to provide filters inside the search query using a "filter:value" format. For example, the following search query would find Apache webservers located in Germany: "apache country:DE".  |
| `facets` | `string` | A comma-separated list of properties to get summary information on. Property names can also be in the format of "property:count", where "count" is the number of facets that will be returned for a property (i.e. "country:100" to get the top 100 countries for a search query). |
| `max_pages` | `integer` | Set the maximum number of pages retrieved. |
| `minify` | `boolean` | True or False; whether or not to truncate some of the larger fields (default: True)  |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `matches` | `array` |  |
| `facets` | `object` |  |
| `total` | `integer` |  |


## Extra

Module **`Shodan` v1.25.0**