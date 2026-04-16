---
description: Enable additional data sources and auditing options.
---

# Optional steps

Optional steps help you collect more telemetry from supported hosts. Use this page for Sysmon, Windows security auditing, and Linux DNS resolution events.

### Windows options

#### Install Sysmon

You can collect additional events with Sysmon. When installed, the agent collects Sysmon logs if they are available.

{% hint style="warning" %}
Installing Sysmon generates more logs and increases CPU usage. Test it on lower-risk systems first.
{% endhint %}

Sysmon is available from [microsoft.com](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon). A common configuration is available on [Florian Roth's GitHub](https://github.com/Neo23x0/sysmon-config/blob/master/sysmonconfig-export.xml). You can also use the [SwiftOnSecurity configuration](https://github.com/SwiftOnSecurity/sysmon-config.md).

#### Configure security log auditing

A proper security log auditing configuration lets the agent collect more security-related events.

Use [Configuring Security Log Audit Settings](https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/main/ConfiguringSecurityLogAuditPolicies.md) for a baseline configuration.

### Linux options

#### Collect DNS resolution events

1. Edit the configuration file:

```shell
/etc/endpoint-agent/config.yaml
```

2. Add the following setting:

```yaml
EnableDNSResolutions: true
```

3. Restart the agent:

```shell
sudo systemctl restart SEKOIAEndpointAgent.service
```

### Related articles

* [Install the endpoint agent](install-the-endpoint-agent.md) Deploy the base agent before enabling optional telemetry.
* [Manage events and fields](manage-events-and-fields.md) Review the event types collected by the agent.
* [Resource footprint](resource-footprint.md) Estimate the host impact of additional telemetry sources.
