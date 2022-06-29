uuid: 5a8ef52f-d143-4735-8546-98539fc07725
name: Umbrella Proxy Logs
type: intake

## Overview
Cisco Umbrella offers flexible, cloud-delivered security. It combines multiple security functions into one solution, so that protection can be extended to devices, remote users, and distributed locations anywhere. CISCO Umbrella is a leading provider of network security and recursive DNS services.

{!xdr/features/collect/integrations/generated/umbrella-proxy_do_not_edit_manually.md!}

## Configure
This setup guide will show you how to forward logs produced by CISCO Umbrella service to SEKOIA.IO by means of an Rsyslog transport channel.

### Collect proxylogs files and send them to rsyslog
After configuring Umbrella Log Management with AWS S3, the logs you download will be gzipped CSVs in appropriate subfolder with the following naming format:

```bash
proxylogs/<year>-<month>-<day>/<year>-<month>-<day>-<hour>-<minute>.csv.gz
```

To send these logs to SEKOIA.IO, we suggest the use of the logger Unix command. For each unzipped file, use the following command line:

```bash
logger -t proxylogs -f <YYYY>-<MM>-<DD>-<hh>-<mm>-<xxxx>.csv
```

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](../../../../ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [CISCO Umbrella User Guide - Logs Management](https://docs.umbrella.com/deployment-umbrella/docs/log-management)
