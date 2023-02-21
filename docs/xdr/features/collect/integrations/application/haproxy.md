uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake

## Overview
HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/haproxy_do_not_edit_manually.md!}

## HAProxy Configuration

1- Setup HAProxy following the official documentation on section below
HaProxy configuration default file `haproxy.cfg` will be found on repo `/etc/haproxy`

2- Add the following line to this file as the 1st line of the `global` section 
````
        log 127.0.0.1    local2
````

3- Restart HaProxy for configuration to be taken account and verify the status
````
	sudo systemctl restart HaProxy.conf && systemctl status HaProxy.conf
````

HaProxy logs are now generated on your machine.

After HAProxy has been setup and configured, the logs have to be sent to a Rsyslog collector then forward to SEKOIA.IO

Here is an example of HAProxy configuration file on Rsyslog to be used (to be adapted):
````
# Use a condition that identifies specifically HaProxy logs that send them to a syslog concentrator
if ($programname startswith 'haproxy') then {
    action(
    type="omfwd"
    protocol="tcp"
    target="<Concentrator_FQDN_or_IP>"
    port="<Remote_Port>"
    TCP_Framing="octet-counted"
    )
}
````

For more information on Rsyslog configuration, please consult the next section.

### Rsyslog

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Reading
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
