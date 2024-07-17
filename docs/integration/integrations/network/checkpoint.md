uuid: f0a10c21-37d1-419f-8671-77903dc8de69
name: Check Point
type: intake

## Overview

Check Point’s Next Generation Firewalls (NGFW’s) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth generation cyber-attacks. Check Point’s NGFW includes 23 Firewall models optimized for running all threat prevention technologies simultaneously, including full SSL traffic inspection, without compromising on security or performance.


{!_shared_content/operations_center/detection/generated/suggested_rules_f0a10c21-37d1-419f-8671-77903dc8de69_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f0a10c21-37d1-419f-8671-77903dc8de69.md!}

## Configure

The solution to collect Checkpoint logs leverages the [Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323) method and Syslog forwarding. 

Log Exporter must be configured to send logs in the **CEF format**.

### Syslog forwading

Please refer to the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
