uuid: f0a10c21-37d1-419f-8671-77903dc8de69
name: Check Point
type: intake

## Overview

Check Point’s Next Generation Firewalls (NGFW’s) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth generation cyber-attacks. Check Point’s NGFW includes 23 Firewall models optimized for running all threat prevention technologies simultaneously, including full SSL traffic inspection, without compromising on security or performance.

{!xdr/features/collect/integrations/generated/checkpoint_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect Checkpoint logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

We are currently supporting the following firewall versions: R77.30, R80.10, R80.20, R80.30.

### Rsyslog

Please refer to the documentation of the [Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323) of checkpoint to forward events to your rsyslog server. The reader is also invited to consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.
