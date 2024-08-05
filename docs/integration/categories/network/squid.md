uuid: a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb
name: Squid
type: intake

# Squid

Squid is a caching proxy for the Web. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. The analysis of Squid logs by Sekoia.io can detect web threats along as in-progress intrusion and exfiltration attempts.





## Configure

As of now, the main solution to collect Squid logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

In this Section, we detail how to configure Squid’s logging output for Sekoia.io by means of the Rsyslog transport. We hereby focus on the configuration of Squid and invite the reader to the [Rsyslog Transport](/integration/ingestion_methods/syslog/overview) documentation to forward these logs to Sekoia.io.

To configure Squid logging, you can create a new configuration `99-sekoiaio.conf` file in the `/etc/squid/conf.d/` directory of your server. With most of Squid configurations (including Debian, Red Hat Entreprise Linux, etc.), this file will automatically be used.

This file should contain two information:

- The log format used for Sekoia.io.
- The Syslog facility and priority we would like to use.

Content of `/etc/squid/conf.d/99-sekoiaio.conf` file:

```
logformat sekoiaio %ts.%03tu %6tr %>a %Ss/%03>Hs %<st %rm %ru %[un %Sh/%<a %mt "%{Referer}>h" "%{User-Agent}>h"
access_log syslog:local5.info sekoiaio
```


## Further Readings

{!_shared_content/operations_center/integrations/generated/a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/a0dbb8f3-ca1c-4c6b-aafa-595bd430c0cb.md!}

- [Integration Source Code](https://github.com/Sekoia-io/intake-formats/tree/master/Squid)
- [Squid Wiki - Log configuration](https://wiki.squid-cache.org/SquidFaq/SquidLogs)
