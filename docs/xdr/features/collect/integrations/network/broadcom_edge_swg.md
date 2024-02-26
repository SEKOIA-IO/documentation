uuid: 2886cd2d-f686-4e7d-9976-250cba2eaf5b
name: Broadcom Edge Secure Web Gateway
type: intake

## Overview

Broadcom Edge Security Web Gateway provides comprehensive protection for web traffic, offering advanced threat detection and prevention capabilities, along with granular policy controls, to safeguard organizations against evolving cyber threats at the network edge.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_2886cd2d-f686-4e7d-9976-250cba2eaf5b_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/2886cd2d-f686-4e7d-9976-250cba2eaf5b.md!}

## Configure

This setup guide will show you how to provide an integration between Broadcom Edge Secure Web Gateway events and Sekoia.io.

### Prerequisites

An internal log concentrator is required to collect and forward events to Sekoia.io.

### Set access logs format
1. In the Management Console, go to `Administration` > `Logging` > `Access Logging`> `General`
2. In `Log Formats`, click `Add New Format`
3. Type a  format name
4. Select `Custom format string` as the format type
5. Paste the following template in the log fields
    
    ```json
    <111>1 $(date)T$(x-bluecoat-hour-utc):$(x-bluecoat-minute-utc):$(x-bluecoat-second-utc)$(s-computername) bluecoat - access_log - date=$(date) time=$(time) c-ip=$(c-ip) c-url=$(quot)$(url)$(quot) cs-Referer=$(quot)$(cs(Referer))$(quot) cs-user-agent=$(quot)$(cs(User-Agent))$(quot) cs-bytes=$(cs-bytes) cs-categories=$(cs-categories) cs-host=$(cs-host) cs-ip=$(cs-ip) cs-threat-risk=$(cs-threat-risk) cs-uri-path=$(cs-uri-path) cs-uri-port=$(cs-uri-port) cs-uri-query=$(quot)$(cs-uri-query)$(quot) cs-uri-scheme=$(cs-uri-scheme) cs-username=$(cs-username) cs-categories=$(cs-categories) cs-referer=$(cs-Referer) rs-content-type=$(quot)$(rs(Content-Type))$(quot) rs-status=$(rs-status) rs-version=$(rs-version) s-action=$(s-action) s-ip=$(s-ip) sc-bytes=$(sc-bytes) sc-status=$(sc-status) rs-content-type=$(rs-Content-Type) time-taken=$(time-taken) x-rs-certificate-hostname=$(x-rs-certificate-hostname) x-virus-id=$(x-virus-id) x-data-leak-detected=$(x-data-leak-detected) x-dns-cs-dns=$(x-dns-cs-dns) x-dns-cs-opcode=$(x-dns-cs-opcode) x-dns-cs-qclass=$(x-dns-cs-qclass) x-dns-cs-qtype=$(x-dns-cs-qtype) x-dns-cs-threat-risk-level=$(x-dns-cs-threat-risk-level) x-dns-rs-a-records=$(x-dns-rs-a-records) x-dns-rs-cname-records=$(x-dns-rs-cname-records) x-dns-rs-ptr-records=$(x-dns-rs-ptr-records) x-dns-rs-rcode-records=$(x-dns-rs-rcode-records)
    ```
    
6. Test the format
7. Apply the change

[Configure an Access Log Format](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/edge-swg/7-3/getting-started/page-help-administration/page-help-logging/log-formats/page-help-access-logging-format.html)

### Enable Syslog forwarding

1. Go to `Administration` > `Logging` > `Access Logging`> `General`
2. In `Logs`, click `Add New Log`
3. In `Log Setting`, type the name of the log and select the format created previously
4. In `Upload client`, select `custom client`
    1. Type log concentration ip address and port as the destination
5. In `Upload Schedule`, select `continuously` for the `Upload the access log` setting
6. Apply the change

[Configure an Access Log](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/edge-swg/7-3/getting-started/page-help-administration/page-help-logging/page-help-access-logging-log.html)

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Broadcom Edge Secure Web Gateway`.

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.
