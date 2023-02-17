uuid: ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9
name: HAProxy
type: intake

## Overview
HAProxy is a free, open source software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers. HAProxy has a lot of features and because it is located between your infrastructure and your clients, it can give you a lot of information about either of them.

{!_shared_content/operations_center/detection/generated/suggested_rules_ff1873e7-8757-4b1a-b0ca-b33f9b27f3d9_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/haproxy_do_not_edit_manually.md!}

## Configure

Here is an example of HA Proxy setup and Collect HA Proxy logs:

1- Update and upgrade, to ensure you have the latest software packages and any security fixes
````
sudo apt update && sudo apt upgrade -y
````

2- Setup HaProxy
````
sudo apt install haproxy
````

3- Create HaProxy file configuration
````
vim /etc/haproxy/haproxy.cfg
````

4- Add following lines to file
````
global
        log 127.0.0.1    local2
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin
        stats timeout 30s
        user haproxy
        group haproxy
        daemon

        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private

        # See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.0.3&config=intermediate
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http

frontend web_front      # define the name of the frontend.
        bind *:81 # IP address of HAProxy server
        default_backend web_back
        
backend web_back        # define the name of the backend.
      server web1 127.0.0.1 :80
````


### Rsyslog

The reader is invited to consult the [Rsyslog Transport](../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
Example of setup in section **Use case: pattern matching for incoming HaProxy logs**

## Further Reading
- [HAProxy Official Documentation](http://www.haproxy.org/#docs)
