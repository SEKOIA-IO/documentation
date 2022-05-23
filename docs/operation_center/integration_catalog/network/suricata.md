uuid: 331fa58d-8cf9-454a-a87f-48a3dc07d4d3
name: Suricata

## Overview
Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

{!operation_center/integration_catalog/generated/suricata_do_not_edit_manually.md!}

## Configure
Suricata leverages its EVE output module to report alerts, metadata, file info and protocol records in JSON. As described in the official documentation, this module can report its findings through the syslog facility.

### Configure Suricata to forward events to rsyslog
Open the Suricata configuration file (please note that the path to the configuration file may change depending on the OS and your configuration):
```bash
sudo vim /etc/suricata/suricata.yaml
```

Paste the following declaration in your suricata configuration to trigger the production of syslog entries under the `local5` facility:
```
outputs:
  - eve-log:
      enabled: yes
      type:syslog
      identity: suricata
      facility: local5
      level: Info
      types:
        - alert
        - http
        - dns
        - tls
```

### Configure the Rsyslog server
Given this Suricata configuration, your local rsyslog server will handle produced records. Please consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings
- [Suricata User Guide](https://suricata.readthedocs.io/)
