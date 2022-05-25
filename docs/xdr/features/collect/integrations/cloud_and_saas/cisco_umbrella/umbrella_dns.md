uuid: 90179796-f949-490c-8729-8cbc9c65be55
name: Umbrella DNS Logs
type: intake

## Overview
Cisco Umbrella offers flexible, cloud-delivered security. It combines multiple security functions into one solution, so that protection can be extended to devices, remote users, and distributed locations anywhere.

{!xdr/features/collect/integrations/generated/umbrella-dns_do_not_edit_manually.md!}

## Configure
This setup guide will show you how to forward logs produced by CISCO Umbrella service to SEKOIA.IO by means of an Rsyslog transport channel.

### Collect proxylogs files and send them to rsyslog
After configuring Umbrella Log Management with AWS S3, the logs you download will be gzipped CSVs in appropriate subfolder with the following naming format:

```bash
dnslogs/<year>-<month>-<day>/<year>-<month>-<day>-<hour>-<minute>.csv.gz
```

To send these logs to SEKOIA.IO, we suggest the use of the logger Unix command. For each unzipped file, use the following command line:

```bash
logger -t dnslogs -f <YYYY>-<MM>-<DD>-<hh>-<mm>-<xxxx>.csv
```

### Configure the Rsyslog server
Please consult the [Rsyslog Transport](../../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [CISCO Umbrella User Guide - Logs Management](https://docs.umbrella.com/deployment-umbrella/docs/log-management)
