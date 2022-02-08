uuid: c3888137-b34e-4526-ab61-836b2d45a742
name: Netfilter

## Overview

Netfilter is a framework provided by the Linux kernel that offers
various functions and operations for packet filtering, network address
translation, and port translation.

The firewall ruleset might be configured by using several user-space
tools such as `iptables` or `nftables` or even with high level
configuration tools such as firewalld, UFW or ferm. The framework also
provides several ways to log events (`LOG`, `NFLOG`, `ULOG`, etc.).

In this example, we only cover the `iptables` syntax and the basic
`LOG` targets that sends messages to your local syslog server.

The only requirement from SEKOIA.IO’s perspective is that your
`iptables` uses the following prefix: `IPTables/XXX: ` (`XXX` is user
configurable and represents the action, could be `Dropped` for
example).

{!operation_center/integration_catalog/generated/netfilter_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect Windows logs with Log Insight leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of Linux to forward events to your rsyslog server. The reader can consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

### Configure Netfilter
The first step is to configure Netfilter to log the awaited
trafic. For example, if you want to only allow HTTP and HTTPS trafic
and log everything else, you could use the following `iptables`
commands:

```bash
# Create a chain that logs packets and then drops them.
$ iptables -N DROP_LOGGING
$ iptables -A DROP_LOGGING -m limit --limit 60/min -j LOG --log-prefix "IPTables/Dropped: " --log-level 4
$ iptables -A DROP_LOGGING -j DROP

# Allow established communications.
$ iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow HTTP communications.
$ iptables -A INPUT -p tcp --dport 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Log and drop everything else.
$ iptables -A INPUT -j DROP_LOGGING
```



## Further Reading
- [netfilter/iptables project homepage](https://www.netfilter.org/)
