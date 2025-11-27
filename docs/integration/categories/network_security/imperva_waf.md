uuid: d9f337a4-1303-47d4-b15f-1f83807ff3cc
name: Imperva Web Application Firewall
type: intake

## Overview

Imperva Web Application Firewall helps you to protect your web applications and your APIs.

- **Vendor**: Imperva
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Imperva WAF dataset



## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

- Log on to your [Imperva control panel](https://management.service.imperva.com/)

- Go to your `Account > Account Management`

    ![step](/assets/integration/network_security/imperva/step01.png)

- Go to [`SIEM Logs > Log Configuration`](https://management.service.imperva.com/siem-config-service).

    ![step](/assets/integration/network_security/imperva/step02.png)

- Click `Add connection`

    ![step](/assets/integration/network_security/imperva/step03.png)

- Select `Imperva API` as delivery method

    ![step](/assets/integration/network_security/imperva/step04.png)

- Type a name for the connection
- Click `Generate API keys`

    ![step](/assets/integration/network_security/imperva/step05.png)

!!! Note
    Copy the API ID, the API Key and the Log Server URI.

- Click `Close`

    ![step](/assets/integration/network_security/imperva/step06.png)

- On the new connection, click `Add log type`

    ![step](/assets/integration/network_security/imperva/step07.png)

- Select `Cloud WAF` as the dataset

    ![step](/assets/integration/network_security/imperva/step08.png)

- Select the log types to forward (at least, `Access logs`; You can add `Security Logs` for more detections)
- Select the default website log level (at least, a log level with `Access logs`)
- Select `CEF` as format
- Enable `Compress logs`
- If you wish to enable log encryption, upload your public key (see [Imperva documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm#EnableEncryption) for more details)

    ![step](/assets/integration/network_security/imperva/step09.png)

- Enable the state `Enabled`
- Click `Add log type` to save

    ![step](/assets/integration/network_security/imperva/step10.png)


### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/connector_configuration.md!}

{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_d9f337a4-1303-47d4-b15f-1f83807ff3cc_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/d9f337a4-1303-47d4-b15f-1f83807ff3cc.md!}

## Further Readings

- [Imperva Log Integration Documentation](https://docs-cybersec.thalesgroup.com/bundle/cloud-application-security/page/settings/log-integration.htm)
