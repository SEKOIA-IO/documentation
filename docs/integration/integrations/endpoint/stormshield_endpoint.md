uuid: f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0
name: Stormshield SES
type: intake

## Overview

Stormshield SES is a comprehensive cybersecurity solution designed to protect individual devices, such as computers and servers, from various cyber threats and attacks. It encompasses advanced features like antivirus, firewall, intrusion detection and prevention, application control, and data encryption. This solution aims to safeguard endpoints from malware, ransomware, phishing, and other malicious activities, while providing centralized management and real-time threat visibility for enhanced security posture.

- **Vendor**: Stormshield
- **Plan**: Defend Prime
- **Supported environment**: On Cloud / On Premise
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**: File monitoring, Application logs and Anti-virus
- **Coverage Score**: 4

## Configure

This section will guide you to forward Stormshield SES logs to SEKOIA.IO

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Stormshield Endpoint Security.

### Configure the Agent handler

1. Log on out Stormshield SES console
2. Go to `Backoffice > Agent handlers`
3. Select an Agent handler group or create a new one
4. On the Agent handler group, in the `Syslog servers`, click `+ Add a server`
   ![Agent handlers](/assets/operation_center/integration_catalog/endpoint/stormshield/stormshield_ses_01.png){: style="max-width:100%"}
5. In the syslog server configuration:

   1. Set the address of the syslog destination to `intake.sekoia.io`
   2. Select `TCP/TLS` as the protocol
   3. Define the syslog destination port to 10514
   4. Select `Raw Json` as message Content
   5. Select `Non-Transparent-Framing` as transfert-type
   6. In the `Structured data` input, add `[SEKOIA@53288 intake_key="<YOUR_INTAKE_KEY>"]` with our intake key as replacement of the placeholder
   7. Save the configuration
   ![Configuration](/assets/operation_center/integration_catalog/endpoint/stormshield/stormshield_ses_02.png){: style="max-width:100%"}

## Troubleshooting

### The SES Agent handler cannot authenticate the Sekoia.io syslog endpoint

The Sekoia.io syslog endpoint is secured with a [Letsencrypt](https://letsencrypt.org) certificate.

According to our SES Agent handler installation, it may be necessary to install `ISRG ROOT X1` certificate in our **trusted root certification authorities certificate store**:

On the SES Agent handler machines:

1. Download the `ISRG ROOT X1` certificate: <https://letsencrypt.org/certs/isrgrootx1.pem>
2. Rename the downloaded certificate by suffixing it with the extension`.crt`
3. Import the certificate in the trusted root certification authorities certificate store of the machine
   ![Certificate store](/assets/operation_center/integration_catalog/endpoint/stormshield/stormshield_ses_03.png){: style="max-width:100%"}


{!_shared_content/operations_center/integrations/generated/f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/f5e6cf5e-bd9f-4caf-9098-fe4a9e0aeaa0.md!}


## Further Readings

You can read all documentation [here](https://documentation.stormshield.eu/SES/v7.2/en/Content/PDF/ses-en-administration_guide-v7.2.pdf)
