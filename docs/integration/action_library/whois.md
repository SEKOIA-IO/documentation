---
uuid: a55461dd-cd8b-9e05-f87a-607b574804fd
name: "Whois"
type: playbook
description: "Provides data enrichment for domains and IP addresses."
---

# Whois

<img src="../.gitbook/assets/library/whois.svg" alt="Whois" width="150" align="right">

Provides data enrichment for domains and IP addresses.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `proxy` | `boolean` | Use system proxy settings |

## Actions

### Whois

Provides data enrichment for Domains, URLs, and IP addresses.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | URL, IP, or domain to be enriched |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `Domain` | `object` |  |


## Extra

Module **`Whois` v1.26.1**