uuid: ab25af2e-4916-40ba-955c-34d2301c1f51
name: NGINX

## Overview
NGINX is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server. It has a lot of features and because it is located between your application and your clients, it can give you a lot of information about either of them.

{!xdr/features/collect/integrations/generated/nginx_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect Nginx logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

The following snippet is an illustration of rsyslog configuration to monitor nginx's `error.log` and `access.log` files.

```bash
# error log
$InputFileName /var/log/nginx/error.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-error
$InputFileSeverity error
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/nginx/access.log
$InputFileTag nginx:
$InputFileStateFile stat-nginx-access
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor
```

The reader can consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.


## Further Reading

- [Nginx Wiki](https://www.nginx.com/resources/wiki/start/)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
