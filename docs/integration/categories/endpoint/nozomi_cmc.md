uuid: baf03007-4fbc-427e-a966-fa50cbe77856
name: Nozomi CMC
type: intake

## Overview

Nozomi Central Management Console is a centralized platform that streamlines the management of cybersecurity across 
industrial networks. It enables users to monitor, configure, and respond to threats in real-time, ensuring enhanced 
visibility and control over operational technology environments. With its user-friendly interface and powerful 
analytics, the console simplifies security operations and strengthens defense against cyber risks.

- **Supported environment**: On prem
- **Detection based on**: Alerts, Audit
- **Supported application or feature**:
    - Alerts
    - Health
    - Audit

## Configure

1. In the top navigation bar, select `settings`
2. In the `Settings` section, select `Data integration`.
3. In the top right section, select `Add`.
4. From the `Choose a configuration` dropdown, select CEF.

  <img width="100%" alt="Configuration" src="/assets/integration/cloud_and_saas/nozomi_cmc/configuration.png">

5. Enter the details as necessary.  ( Enable logs types as you wish )

  <img width="100%" alt="Details" src="/assets/integration/cloud_and_saas/nozomi_cmc/details.png">


### Create your intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Nozomi CMC`.


#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/baf03007-4fbc-427e-a966-fa50cbe77856_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_baf03007-4fbc-427e-a966-fa50cbe77856_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/baf03007-4fbc-427e-a966-fa50cbe77856.md!}

## Further Readings

- [Data integration overview](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration_overview_cmc.html)
- [Data integration](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration-1.html)
- [Syslog Forwarder](https://technicaldocs.nozominetworks.com/products/n2os/topics/administration/settings/data-integration/c_n2os_admin_settings_data-integration_syslog-forwarder-1.html)
- [Alerts and Incidents. Reference Guide](https://technicaldocs.nozominetworks.com/out/pdf-output/Alerts%20and%20Incidents-Reference%20Guide.pdf)
