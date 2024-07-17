name: Pulse Connect Secure
uuid: 7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5
type: intake

## Overview

Pulse Connect Secure is an SSL VPN solution for remote and mobile users.


{!_shared_content/operations_center/detection/generated/suggested_rules_7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5.md!}

## Configure

As of now, the main solution to collect Pulse Secure Connect logs leverages the Rsyslog recipe along with the WELF log format offered by Pulse Secure. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of Pulse Secure Connect to forward events to your syslog concentrator. The reader can consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
