uuid: 6c2a44e3-a86a-4d98-97a6-d575ffcb29f7
name: Apache
type: intake

## Overview
The Apache HTTP Server, colloquially called Apache, is free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.


{!operation_center/integration_catalog/generated/apache_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect Apache logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

This setup guide will show you how to forward both your access and error logs to SEKOIA.IO by means of an rsyslog transport channel. The reader is also invited to consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

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
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
