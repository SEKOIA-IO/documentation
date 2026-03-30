# nozomi\_cmc

uuid: baf03007-4fbc-427e-a966-fa50cbe77856 name: Nozomi CMC \[Beta] type: intake

### Overview

Nozomi Central Management Console is a centralized platform that streamlines the management of cybersecurity across industrial networks. It enables users to monitor, configure, and respond to threats in real-time, ensuring enhanced visibility and control over operational technology environments. With its user-friendly interface and powerful analytics, the console simplifies security operations and strengthens defense against cyber risks.

* **Supported environment**: On Prem
* **Detection based on**: Alerts, Telemetry
* **Supported application or feature**:
  * Alerts
  * Health
  * Audit

### Specification

#### Prerequisites

* **Resource**:
  * Self-managed syslog forwarder
* **Network**:
  * **On Premise**: Outbound traffic allowed
* **Permissions**:
  * Administrator access to the Central Management Console
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog** for On Premise

#### Logs details

* **Supported functionalities**: See section [Overview](nozomi_cmc.md#overview)
* **Supported type(s) of structure**: CEF
* **Supported verbosity level**: Alert, Informational

!!! Note This is a description of the log level based on the taxonomy of the [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) for standardization purpose. Please adapt to the wording used by the editor.

### Step-by-Step Configuration Procedure

To Enable the CEF forwarding:

1. Log in the Nozomi Central Management Console.
2. Click `Administration`.



3. Go to `Settings` > `Data integration`.
4. Click `+ Add`.



5. From the `Choose a configuration` dropdown, select CEF.



6. Type a description.
7. In `To URI`, type `tcp://` following by the address of the log concentrator and the port for the intake
8. Check `Enable sending Alerts`
9. Check `Enable sending Audit Logs`
10. Check `Enable sending Health Logs`



#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/baf03007-4fbc-427e-a966-fa50cbe77856\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_baf03007-4fbc-427e-a966-fa50cbe77856\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/baf03007-4fbc-427e-a966-fa50cbe77856.md!}

### Further Readings

* [Data integration overview](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration_overview_cmc.html)
* [Data integration](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration-1.html)
* [Syslog Forwarder](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration_syslog-forwarder-1.html)
* [Alerts and Incidents. Reference Guide](https://technicaldocs.nozominetworks.com/out/pdf-output/Alerts%20and%20Incidents-Reference%20Guide.pdf)
