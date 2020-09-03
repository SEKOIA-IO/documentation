# Integrations

In order to protect your business, you need to know what happens. The monitoring of your network and your devices is a prerequisite to their security.

SEKOIA.IO rely on your log to identify threats and malicious activities.

In this chapter, you will learn how to configure your log system to make it forward your events to SEKOIA.IO.

SEKOIA.IO is able to collect logs through various mechanisms, configuration on your side should be easy! Here is an overview on how integration could be done with SEKOIA.IO.

![SEKOIA.IO Operation Center integration overview](/assets/sekoiaio_oc_integration.png){: style="max-width:800px"}

SEKOIA.IO supports the following log collectors:

- Syslog over TLS (`intake.sekoia.io:10515`): you can forward your events by using the Syslog protocol specified in RFC 5424.
- HTTPS (`https://intake.sekoia.io`): you can `POST` your JSON events.
- Cloud hosting polling: you can configure SEKOIA.IO to regularly retrieve your logs.

If these solutions do not meet your needs, we can also configure a dedicated secured network through a VPN and retrieve your logs directly (please contact us for more information).

## Syslog integration

We are providing documentation and example configurations on how to configure your log system for Rsyslog, but it should be easy to configure other log collectors to forward their events to SEKOIA.IO.

## HTTPS integration

To push your events through our HTTP log collector, you have to `POST` your logs in the JSON or MessagePack format. To send us events, you should set `Content-Type` HTTP header:

- `application/javascript` for JSON messages.
- `application/msgpack` for MessagePack message.

## Cloud & SaaS integration

SEKOIA.IO is also able to retrieve logs and data from cloud platforms, such as Microsoft Azure, Amazon Web Services or Google Cloud.

## Log formats

### Cloud and SaaS

- [AWS CloudTrail](aws_cloudtrail.md)
- [Microsoft Azure Active Directory](azure_ad.md)
- [Microsoft Azure MySQL](azure_mysql.md)
- [Microsoft Azure Linux machines](azure_linux.md)
- [Microsoft Azure Windows machines](azure_windows.md)
- [Microsoft Office 365](o365.md)
- [CISCO Umbrella Dns Logs](umbrella_dns.md)
- [CISCO Umbrella Ip Logs](umbrella_ip.md)
- [CISCO Umbrella Proxy Logs](umbrella_proxy.md)

### Operating Systems

- [Linux](linux.md)
- [Windows / NXLog](windows.md)
- [Windows / Log Insight](log_insight_windows.md)

### Applications

- [Alsid](alsid.md)
- [Apache](apache.md)
- [Checkpoint](checkpoint.md)
- [Cisco](cisco_asa.md)
- [F5 BigIP](f5-big-ip.md)
- [Fortigate](fortigate.md)
- [HAProxy](haproxy.md)
- [ISC DHCP](dhcpd.md)
- [NetFilter](netfilter.md)
- [Nginx](nginx.md)
- [OpenSSH](openssh.md)
- [PaloAlto](paloalto.md)
- [Postfix](postfix.md)
- [Sophos](sophos.md)
- [SpamAssassin](spamassassin.md)
- [Squid](squid.md)
- [Suricata](suricata.md)
- [Unbound](unbound.md)
- [Zeek](zeek.md)

### Generic

- [Common Event Format](cef.md)
