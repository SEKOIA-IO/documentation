uuid: 35855de3-0728-4a83-ae19-e38e167432a1
name: OpenLDAP
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
OpenLDAP (Lightweight Directory Access Protocol) is an open-source implementation of a directory service protocol. It helps organizations to maintain and manage a centralized directory of user information, such as names, addresses, and other attributes.



## Configure

As of now, the main solution to collect OpenLDAP logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Collect the logs

Below is a couple of suggestions you can follow to configure your system to collect openLDAP logs with rsyslog:

1. Local `slapd.conf` or `slapd.d/cn=config.ldif` and modify loglvl setting there. For example:
   ```bash
   loglevel 256
   ```
2. Modify your `rsyslog.conf` or `/etc/rsyslog.d/*.conf` to specify log destination. For example:
   ```bash
   local4.* /var/log/openldap.log
   ```
3. Restart `rsyslog` services. For example:
   ```bash
   sudo systemctl restart slapd
   sudo systemctl restart rsyslog
   ```
4. Check that logs are being written to the destination file. For example:
   ```bash
   tail -f /var/log/openldap.log
   ```

### Forward logs to SEKOIA.IO
Please consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.


{!_shared_content/operations_center/integrations/generated/35855de3-0728-4a83-ae19-e38e167432a1_sample.md!}


## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).
{!_shared_content/operations_center/detection/generated/suggested_rules_35855de3-0728-4a83-ae19-e38e167432a1_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/35855de3-0728-4a83-ae19-e38e167432a1.md!}

## Further Readings

- [OpenLDAP Official Website](https://www.openldap.com)
- [OpenLDAP Quickstart Guide](https://www.openldap.com/doc/admin26/quickstart.html)
