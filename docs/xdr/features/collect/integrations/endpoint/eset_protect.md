uuid: 2ffff1fd-fed7-4a24-927a-d619f2bb584a
name: ESET Protect
type: intake

## Overview

ESET Protect is a cybersecurity platform offering advanced threat detection, endpoint protection, and management tools for businesses, ensuring robust defense against malware and cyber threats.

{!_shared_content/operations_center/detection/generated/suggested_rules_2ffff1fd-fed7-4a24-927a-d619f2bb584a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2ffff1fd-fed7-4a24-927a-d619f2bb584a.md!}

## Configure

This setup guide will show you how to enable log export in ESET Protect using syslog.

Only events from the following log categories are being exported to Syslog server: Detection, Firewall, HIPS, Audit and ESET Inspect.

To enable Syslog server in ESET Protect, follow the steps below:

1. In admin console go to `More` > `Settings`.
2. Open `Advanced Settings` tab.

    ![Advanced Settings](/assets/instructions/eset_protect/enable_syslog_1.png)

3. Click on `Syslog server` > `Use Syslog server`.
4. Then click on `Logging` > `Export logs to Syslog` and choose `JSON` format.
5. Save configuration.

    ![Syslog configuration](/assets/instructions/eset_protect/enable_syslog_2.png)

## Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `ESET Protect`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

## Further Readings
- [Export logs to Syslog](https://help.eset.com/protect_admin/10.0/en-US/admin_server_settings_export_to_syslog.html)
- [Export logs to Syslog server from ESET PROTECT (8.x–10.x)](https://techcenter.eset.nl/en-US/kb/articles/export-logs-to-syslog-server-from-eset-protect-8x-10x)
- [Collect logs from ESET PROTECT with Elastic Agent](https://docs.elastic.co/integrations/eset_protect#to-collect-data-from-eset-protect-via-syslog-follow-the-below-steps)
- [Support: Export logs to Syslog server from ESET PROTECT On-Prem](https://support.eset.com/en/kb8022-export-logs-to-syslog-server-from-eset-protect)
