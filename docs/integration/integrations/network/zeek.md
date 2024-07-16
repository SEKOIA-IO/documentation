uuid: 428035c0-a251-4664-8e58-fed15f4e442c
name: Zeek
type: intake

## Overview
Zeek is a free and open-source software network analysis framework; it was originally developed in 1994 by Vern Paxson and was named in reference to George Orwell's Big Brother from his novel Nineteen Eighty-Four. It can be used as a network intrusion detection system (NIDS) but with additional live analysis of network events. It is released under the BSD license.


{!_shared_content/operations_center/detection/generated/suggested_rules_428035c0-a251-4664-8e58-fed15f4e442c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/428035c0-a251-4664-8e58-fed15f4e442c.md!}

## Configure
Refer to the configuration of Zeek's export to syslog to forward dns, http and conn logs to Sekoia.io by means of an rsyslog transport channel. Please consult the [Rsyslog Transport](../../../ingestion_methods/syslog/overview/) documentation to forward these logs to Sekoia.io.


## Further Reading
- [Zeek documentation](https://docs.zeek.org/en/stable/index.html)
- [Rsyslog IMFile module](https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html)
