uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake

## Overview
HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9.md!}

## HAProxy Configuration

HAProxy Configuration file is created by default when HAProxy is setup on the machine

!!! Note
    HAProxy configuration default file `haproxy.cfg` will be found in the directory `/etc/haproxy`

By default events are forwarded to `/var/lib/haproxy/dev/log` then processed by a local rsyslog to store them on `/var/log/haproxy.log`.

## Forward the HAProxy logs to a concentrator

After HAProxy has been setup and configured, the logs have to be sent to a syslog concentrator then forwarded to Sekoia.io.

By default, at HAProxy first installation, an rsyslog configuration is created on the repository `/etc/rsyslog.d/`, it contains the following lines:

```
# Create an additionnal socket in haproxy's chroot in order to allow logging via 
# /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Send HAProxy messages to a dedicated logfile
:programname, startswith, "haproxy" {
    /var/log/haproxy.log
    stop
}
```

You only have to replace the configuration by the following lines:

```
# Create an additionnal socket in haproxy's chroot in order to allow logging via 
# /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Use a condition that identifies specifically HaProxy logs that send them to a syslog concentrator
if ($programname startswith 'haproxy') then {
    # Log events locally
    /var/log/haproxy.log
    
    # Forward HAProxy logs to a concentrator
    action(
    type="omfwd"
    protocol="tcp"
    target="<Concentrator_FQDN_or_IP>"
    port="<Remote_Port>"
    TCP_Framing="octet-counted"
    )
}
```

For more information on Rsyslog configuration, please consult the next section.

### Rsyslog

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

## Further Reading
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
