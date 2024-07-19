uuid: c3888137-b34e-4526-ab61-836b2d45a742
name: Netfilter
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

Netfilter is a framework provided by the Linux kernel that offers
various functions and operations for packet filtering, network address
translation, and port translation.

The firewall ruleset might be configured by using several user-space
tools such as `Iptables` or `Nftables` or even with high level
configuration tools such as firewalld, UFW or ferm. The framework also
provides several ways to log events (`LOG`, `NFLOG`, `ULOG`, etc.).

The only requirement from Sekoia.io’s perspective is that your
logs uses the following prefix: `IPTABLES: XXX ` (`XXX` is user
configurable and represents the action, could be `dropped` or `accept` for
example).




## Configure

As of now, the main solution to send Netfilter events to Sekoia.io is to use a Rsyslog concentrator. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io

### Configure Netfilter using Iptables
The first step is to configure Netfilter to log the awaited
trafic. For example, if you want to only allow HTTP and HTTPS trafic
and log everything else, you could use the following `iptables`
commands:

```bash
# Create a chain that logs packets and then drops them.
$ iptables -N DROP_LOGGING
$ iptables -A DROP_LOGGING -m limit --limit 60/min -j LOG --log-prefix "IPTables: Dropped: " --log-level 4
$ iptables -A DROP_LOGGING -j DROP

# Allow established communications.
$ iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow HTTP communications.
$ iptables -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Log and drop everything else.
$ iptables -A INPUT -j DROP_LOGGING
```

### Configure Netfilter using Nftables
Nftables is often installed by default as a replacement for iptables on the latest linux distributions.
To log events with Nftables the first step is to install ulogd2. Use the following command to install it :
```bash
sudo apt install ulogd2
```

You can then verify that the service is running with that command :
```bash
sudo systemctl status ulogd2.service
```

You can now configure the file `/etc/nftables.conf` to log what you want.
For instance, if you want to log all the new UDP and TCP traffic that go outside your network,
you can use this configuration :

```bash
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
        chain input {
                type filter hook input priority 0;
        }
        chain forward {
                type filter hook forward priority 0;
        }
        chain output {
                type filter hook output priority 0; policy accept;

                # Log all the new TCP connections
                ct state new tcp dport 0-65535 log prefix "IPTABLES: ACCEPT " level info accept;
                # Log all the new UDP traffic
                ct state new udp dport 0-65535 log prefix "IPTABLES: ACCEPT " level info accept;
        }
}
```

Finally, ensure that `Nftables` is running and the service is enabled :
```bash
sudo systemctl start nftables && sudo systemctl enable nftables
```



## Further Reading
- [netfilter/iptables project homepage](https://www.netfilter.org/)

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_c3888137-b34e-4526-ab61-836b2d45a742_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/c3888137-b34e-4526-ab61-836b2d45a742.md!}

