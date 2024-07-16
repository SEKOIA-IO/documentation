uuid: a199fbde-508e-4cb9-ae37-842703494be0
name: BIND
type: intake

## Overview

BIND is an implementation of the Domain Name System (DNS) of the Internet. It performs both of the main DNS server roles, acting as an authoritative name server for domains, and acting as a recursive resolver in the network.

{!_shared_content/operations_center/detection/generated/suggested_rules_a199fbde-508e-4cb9-ae37-842703494be0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/a199fbde-508e-4cb9-ae37-842703494be0.md!}

## Configure

As of now, the main solution to collect BIND logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

This Section shows how to configure BIND to forward its events to your rsyslog server. The reader is also invited to consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.

First, you need to configure your BIND daemon to log queries and forward them to your rsyslog instance. If rsyslog and BIND are installed on the same box, you can simply add the following statement in your BIND’s main configuration file:

```
logging {
        channel syslog_chan {
                syslog daemon;
                severity dynamic;
        };
        category default { syslog_chan; };
        category queries { syslog_chan; };
        category config { syslog_chan; };
        category security { syslog_chan; };
};
```

You can find more informations on [how to configure your BIND instance on its official website](https://kb.isc.org/docs/aa-01526).
