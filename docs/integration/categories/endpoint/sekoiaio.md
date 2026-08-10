uuid: 250e4095-fa08-4101-bb02-e72f870fcbd1
name: Sekoia.io Endpoint Agent
type: intake

# Sekoia Endpoint Agent

The Sekoia Endpoint Agent collects security-related events from Windows, Linux, and macOS endpoints and sends them directly to Sekoia. It requires minimal configuration and preserves the integrity of all logs collected from the operating system event log without modification.

!!! note "Log integrity"
    The Sekoia Endpoint Agent does not modify or rewrite logs collected from the operating system event log.

## Supported OS versions

The agent supports the following operating systems on 64-bit versions only.

=== "Windows"

    * Windows 8
    * Windows 10
    * Windows 11
    * Windows Server 2016
    * Windows Server 2019
    * Windows Server 2022
    * Windows Server 2025

=== "Linux"

    The agent supports Linux distributions based on kernel version 3.10 or newer. The following list is non-exhaustive:

    * Ubuntu 14.04 and newer
    * Debian 8 and newer
    * CentOS 7 and newer
    * Red Hat 7 and newer

=== "macOS"

    * macOS 13 Ventura and newer

## Prerequisites

The agent uses HTTPS (port 443) to send events and includes an automatic update mechanism. Open the following network streams before installation.

=== "FRA1"

    * <https://intake.sekoia.io/>
    * <https://api.sekoia.io/>

=== "FRA2"

    * <https://intake.fra2.sekoia.io/>
    * <https://app.fra2.sekoia.io/>

=== "MCO1"

    * <https://intake.mco1.sekoia.io/>
    * <https://app.mco1.sekoia.io/>

=== "UAE1"

    * <https://intake.uae1.sekoia.io/>
    * <https://app.uae1.sekoia.io/>

=== "USA1"

    * <https://intake.usa1.sekoia.io/>
    * <https://app.usa1.sekoia.io/>

=== "SGP1"

    * <https://intake.sgp1.sekoia.io/>
    * <https://app.sgp1.sekoia.io/>

## Events collected

The following lists show a non-exhaustive sample of events the agent detects. The exact events depend on context, configuration, and agent version.

=== "Windows"

    * File creation, deletion, and rename
    * Process lifecycle
    * Remote thread execution
    * DNS resolution
    * TCP connection
    * PowerShell commands
    * WMI activity
    * NTLM
    * Windows Defender events
    * Sysmon events (if Sysmon is configured)

=== "Linux"

    * Root command executions
    * File creation, deletion, rename, and change
    * Process lifecycle
    * TCP connection
    * Python and Perl commands
    * PIP and APT installs
    * Cron configuration and scheduled jobs
    * Sudoers file changes
    * Passwd operations
    * Suspicious activity (curl, Wireshark, and similar tools)

=== "macOS"

    * Root command executions
    * File creation, deletion, rename, and change
    * DNS resolution
    * TCP connection
    * PIP and APT installs
    * Sudoers file changes
    * Passwd operations
    * Suspicious activity (curl, Wireshark, and similar tools)

## Resource footprint

The agent is designed to minimize impact on monitored systems.

| Resource | Typical usage |
|---|---|
| CPU | Less than 1% on average |
| RAM | Around 36 MB |
| Disk (installation) | ~15 MB for the binary; a few KB for the configuration file |
| Disk (operations) | Log files rotated at 100 MB by default; up to 5 compressed rotated files kept |

!!! tip
    You can customize the log rotation settings. See [Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md#customize-agents-log-file-rotation).

## Changelog

For a full list of changes between versions, see the [agent changelog](https://changelog.sekoia.com/changelog?type=t6527b1484d556).

## Related articles

[Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): How to create an intake, download, and install the agent on Windows, Linux, and macOS.

[Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): How to set up log file collection, proxy, retention, and optional features.

[Update and uninstall the Sekoia Endpoint Agent](/integration/categories/endpoint/update_uninstall_sekoia_endpoint_agent.md): How to update the agent manually and remove it from a host.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to read agent logs and resolve common errors.

[Sekoia Endpoint Agent — events and fields reference](/integration/categories/endpoint/sekoia_endpoint_agent_events_reference.md): Reference for data source categories, event samples, and extracted ECS fields.

[Sekoia Endpoint Agent — built-in detection rules](/integration/categories/endpoint/sekoia_endpoint_agent_rules_reference.md): Reference for all built-in detection rules that match this intake.
