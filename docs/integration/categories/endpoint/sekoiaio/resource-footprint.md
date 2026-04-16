---
description: Review average CPU, memory, and disk usage for the agent.
---

# Resource footprint

The agent is designed to keep host impact low. Use this page to review average CPU, memory, and disk usage.

### CPU and memory

On average, the agent uses less than `1%` CPU and about `36` MB of RAM.

### Disk usage

#### Installation

The agent binary and each new download use about `15` MB. The configuration file uses only a few KB.

#### Operation

During normal operation, disk usage depends on log volume. By default, log files rotate at `100` MB and the agent keeps up to `5` old compressed log files.

### Related articles

* [Manage data retention](manage-data-retention.md) Change the local event buffer size.
* [Optional steps](optional-steps.md) Review features that may increase log volume.
* [Troubleshoot](troubleshoot.md) Investigate disk or resource issues from the local logs.
