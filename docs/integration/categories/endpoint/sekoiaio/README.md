---
tags:
  - tag: new
    primary: true
---

# Sekoia.io endpoint agent

Sekoia.io Endpoint Agent collects security-related events with minimal setup. It runs on supported Windows, Linux, and macOS hosts and sends events directly to Sekoia.io.

### Overview

The agent preserves the integrity of operating system event logs. It does not rewrite or modify the logs it collects.

{% hint style="info" %}
The agent preserves the integrity of collected operating system logs. It does not modify or rewrite them.
{% endhint %}

### Supported OS versions

The agent supports 64-bit operating systems only.

{% tabs %}
{% tab title="Windows" %}
* Windows 8
* Windows 10
* Windows 11
* Windows Server 2016
* Windows Server 2019
* Windows Server 2022
* Windows Server 2025
{% endtab %}

{% tab title="Linux" %}
The agent supports distributions based on kernel version `3.10` or newer.

This non-exhaustive list includes:

* Ubuntu 14.04 and newer
* Debian 8 and newer
* CentOS 7 and newer
* Red Hat 7 and newer
{% endtab %}

{% tab title="MacOS" %}
* macOS 13 Ventura and newer
{% endtab %}
{% endtabs %}

### New features

To review changes between agent versions, check the [agent changelog](https://changelog.sekoia.io/changelog?type=t6527b1484d556).

### Prerequisites

The agent uses HTTPS to send events and to retrieve updates. Allow outbound access to the required regional endpoints.

{% tabs %}
{% tab title="FRA1" %}
* [https://intake.sekoia.io/](https://intake.sekoia.io/)
* [https://api.sekoia.io/](https://api.sekoia.io/)
{% endtab %}

{% tab title="FRA2" %}
* [https://intake.fra2.sekoia.io/](https://intake.fra2.sekoia.io/)
* [https://app.fra2.sekoia.io/](https://app.fra2.sekoia.io/)
{% endtab %}

{% tab title="MCO1" %}
* [https://intake.mco1.sekoia.io/](https://intake.mco1.sekoia.io/)
* [https://app.mco1.sekoia.io/](https://app.mco1.sekoia.io/)
{% endtab %}

{% tab title="UAE1" %}
* [https://intake.uae1.sekoia.io/](https://intake.uae1.sekoia.io/)
* [https://app.uae1.sekoia.io/](https://app.uae1.sekoia.io/)
{% endtab %}

{% tab title="USA1" %}
* [https://intake.usa1.sekoia.io/](https://intake.usa1.sekoia.io/)
* [https://app.usa1.sekoia.io/](https://app.usa1.sekoia.io/)
{% endtab %}
{% endtabs %}

### Articles in this section

* [Install the endpoint agent](install-the-endpoint-agent.md) Install the agent and enable installation-time options.
* [Manage the endpoint agent](manage-the-endpoint-agent.md) Update the agent or remove it from a host.
* [Collect logs in files](collect-logs-in-files.md) Configure file-based log collection.
* [Manage data retention](manage-data-retention.md) Adjust the local event buffer size.
* [Manage events and fields](manage-events-and-fields.md) Configure optimization rules and review event data.
* [Proxy support](proxy-support.md) Send agent traffic through an HTTP proxy.
* [Optional steps](optional-steps.md) Enable extra telemetry sources on supported hosts.
* [Available arguments and options](available-arguments-and-options.md) Review commands, syntax, and flags.
* [Resource footprint](resource-footprint.md) Check CPU, memory, and disk usage.
* [Troubleshoot](troubleshoot.md) Find logs and diagnose common issues.

###
