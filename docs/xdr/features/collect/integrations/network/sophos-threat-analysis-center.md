uuid: 99da26fc-bf7b-4e5b-a76c-408472fcfebb
name: Sophos Threat Analysis Center
type: intake

## Overview

The Sophos Threat Analysis Center (STAC), is a dedicated tool for research and analysis of cybersecurity threats. so it can help continuously on monitoring the cyber threat landscape and analyze new forms of malware, attack techniques, and cybercrime trends. which has also the most important part which the _live Discover_ , with usage of queries you can have device informations from Sophos data lake.

!!! warning
    This format is still in beta, please use it wisely.

{!\_shared_content/operations_center/detection/generated/suggested_rules_99da26fc-bf7b-4e5b-a76c-408472fcfebb_do_not_edit_manually.md!}

{!\_shared_content/operations_center/integrations/generated/99da26fc-bf7b-4e5b-a76c-408472fcfebb.md!}

## Configure

### Prerequisites

You can find the system requirements for each respective platform below : <br />

- [Windows Requirements](https://support.sophos.com/support/s/article/KB-000035144?language=en_US)
- [Windows Server Requirements](https://support.sophos.com/support/s/article/KB-000034074?language=en_US)
- [MacOS Requirements](https://support.sophos.com/support/s/article/KB-000034670?language=en_US)

### Enable Syslog forwarding

Log on your Sophos Interface and follow [this guide](https://community.sophos.com/intercept-x-endpoint/f/recommended-reads/130364/getting-started-with-sophos-xdr-data-lake-hydration).

## Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Sophos Analysis Threat Center.

## Transport to SEKOIA.IO

Please consult the [Syslog Forwarding](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to SEKOIA.IO.

## Further Readings

- [Sophos Analysis Threat Center documentation](https://doc.sophos.com/central/customer/help/en-us/ManageYourProducts/ThreatAnalysisCenter/index.html)
