uuid: 6e2f8b2b-3412-4699-a96b-a9a769bff683
name: CyberArk Digital Vault
type: intake

## Overview

CyberArk Vault is a secure digital repository designed to protect and manage sensitive information, particularly privileged account credentials and secrets

- **Vendor**: CyberArk
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**
![cyberark_vault_architecture](/assets/integration/cyberark_vault_architecture.png){: style="max-width:100%"}

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Root access to the Cyberark Vault appliance
    - Root access to the Linux server with the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Syslog
- **Supported verbosity level**: Informational

!!! Note
    Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

## Step-by-Step Quick Configuration Procedure

1. Log in to your CyberArk Vault appliance.
2. Navigate to /Server/Conf, open the In DBParm.ini file, and configure the parameters that are relevant for syslog :

    > Note : if your security policy requires extra-security (ex: tls) between the application and the syslog forwarder, modify the configuration accordingly

    ```bash
    SyslogServerIP={IP_OF_YOUR_SEKOIA_FORWARDER}
    SyslogServerPort={SEKOIA_FORWARDER_SPECIFIC_PORT}
    SyslogServerProtocol=TCP
    SyslogTranslatorFile=Syslog\QRadar.sample.xsl
    UseLegacySyslogFormat=no
    ```

3. After saving DBPARM.ini file, restart the vault server 
4. Ensure that the Vault starts successfully and that there are no errors in the log.

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/6e2f8b2b-3412-4699-a96b-a9a769bff683_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/6e2f8b2b-3412-4699-a96b-a9a769bff683.md!}
