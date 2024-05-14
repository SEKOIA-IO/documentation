uuid: 331fa58d-8cf9-454a-a87f-48a3dc07d4d3
name: Suricata
type: intake

## Overview
Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.


{!_shared_content/operations_center/detection/generated/suggested_rules_331fa58d-8cf9-454a-a87f-48a3dc07d4d3_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/331fa58d-8cf9-454a-a87f-48a3dc07d4d3.md!}

## Configure
Suricata leverages its EVE output module to report alerts, metadata, file info and protocol records in JSON. As described in the [official documentation](https://docs.suricata.io/en/latest/configuration/suricata-yaml.html), this module can report its findings through the [syslog](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html#output-types) facility.

### Configure log settings
Open the Suricata configuration file: `suricata.yaml` (please note that the path to the configuration file may change depending on the OS and your configuration):
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

### Forward logs to sekoia 
Given this Suricata configuration, your local rsyslog server will handle produced records.
Once your Suricata is configure to log threw syslog you have many options to forward those logs to Sekoia.io app. All of those solutions have their advantages. You will find more details about the type of events that are handled by each of them and how to set up those solutions on the dedicated documentations that follows:
- [Sekoia.io agent](https://docs.sekoia.io/xdr/features/collect/integrations/endpoint/sekoiaio/)
- [Sekoia.io Forwarder](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/sekoiaio_forwarder/)
- [Rsyslog](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/syslog/rsyslog/)
Given this Suricata configuration, your local rsyslog server will handle produced records.
## Further Readings
- [Suricata User Guide](https://suricata.readthedocs.io/)
