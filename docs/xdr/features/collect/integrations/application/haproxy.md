uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake

## Overview
HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9.md!}

## HAProxy Configuration

1- HAProxy Configuration file is created by default when HAProxy is setup on the machine

!!! Note
    HAProxy configuration default file `haproxy.cfg` will be found in the directory `/etc/haproxy`

2- Restart HAProxy for configuration to be taken account and verify the status

```bash
sudo systemctl restart haproxy && systemctl status haproxy
```

HAProxy logs are now generated on your machine.

## Forward the HAProxy logs to a concentrator

After HAProxy has been setup and configured, the logs have to be sent to a Rsyslog collector then forward to SEKOIA.IO.

Here is an example of rsyslog configuration file to be adapted, that will be available under `/etc/rsyslog.d/`:

```
# Create an additionnal socket in haproxy's chroot in order to allow logging via 
# /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

# Send HAProxy messages to a dedicated logfile
:programname, startswith, "haproxy" {
    /var/log/haproxy.log
    stop
}

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

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Reading
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
