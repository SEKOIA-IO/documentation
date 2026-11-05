---
uuid: 52686cd0-8636-48d3-a7d6-9c20ee47f111
name: "RSS"
type: playbook
description: "RSS is a internet standard for web syndication. It usually used by websites to publish frequently updated information.\n\nThis module exposes triggers to subscribe to RSS feeds."
---

# RSS

<img src="../.gitbook/assets/library/rss.png" alt="RSS" width="150" align="right">

RSS is a internet standard for web syndication. It usually used by websites to publish frequently updated information.

This module exposes triggers to subscribe to RSS feeds.

## Configuration

This module accepts no configuration.

## Triggers

### New Post

Trigger playbook when new posts are published

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `feeds` | `array` | RSS Feeds configuration |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `source` | `object` | Information about the RSS Feed's source |
| `item` | `object` | RSS Item content |
| `event_path` | `string` | Path to the file containing the RSS event |


## Extra

Module **`RSS` v1.29.1**