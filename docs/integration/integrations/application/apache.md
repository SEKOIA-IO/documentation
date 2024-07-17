uuid: 6c2a44e3-a86a-4d98-97a6-d575ffcb29f7
name: Apache HTTP Server
type: intake

## Overview
The Apache HTTP Server, colloquially called Apache, is free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.

!!! info
    Access logs from Tomcat are compatible with existing format Apache HTTP server. Catalina logs are not supported.


This integration supports:

- error logs
- access logs formatted with the `Common Log Format` (also known as `NCSA Common Log Format`)
- access logs formatted with the `Combined Log Format`

{!_shared_content/operations_center/detection/generated/suggested_rules_6c2a44e3-a86a-4d98-97a6-d575ffcb29f7_do_not_edit_manually.md!}


{!_shared_content/operations_center/integrations/generated/6c2a44e3-a86a-4d98-97a6-d575ffcb29f7.md!}

## Configure

As of now, the main solution to collect Apache logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Forward logs to Sekoia.io

This setup guide will show you how to forward both your access and error logs to Sekoia.io by means of an syslog transport channel. The reader is also invited to consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

At the beginning of your rsyslog configuration file for the Apache logs,  paste the following instruction to order the rsyslog server to load the module `imfile`:
```bash
$ModLoad imfile
```

Then use the following configuration to leverage this module to monitor apache httpd access and error output files (please note that the path to the log file may change depending on the OS and your configuration):
```bash
# error log
$InputFileName /var/log/apache2/error.log
$InputFileTag apache:
$InputFileStateFile stat-apache-error
$InputFileSeverity error
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor

# access log
$InputFileName /var/log/apache2/access.log
$InputFileTag apache:
$InputFileStateFile stat-apache-access
$InputFileSeverity notice
$InputFileFacility local5
$InputFilePollInterval 1
$InputRunFileMonitor
```

## Further Reading
- [Apache documentation](http://httpd.apache.org/docs/)
