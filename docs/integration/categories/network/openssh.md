uuid: b28db14b-e3a7-463e-8659-9bf0e577944f
name: OpenSSH
type: intake

## Overview
- **Vendor**:
- **Plan**: Defend Core & Defend Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:
OpenSSH is the premier connectivity tool for remote login with the SSH protocol. It encrypts all traffic to eliminate eavesdropping, connection hijacking, and other attacks. In addition, OpenSSH provides a large suite of secure tunneling capabilities, several authentication methods, and sophisticated configuration options.



## Configure

As of now, the main solution to collect OpenSSH logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of OpenSSH to forward events to your rsyslog server. The reader can consult the [Rsyslog Transport](/integration/ingestion_methods/syslog/overview) documentation to forward these logs to Sekoia.io.


{!_shared_content/operations_center/integrations/generated/b28db14b-e3a7-463e-8659-9bf0e577944f_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_b28db14b-e3a7-463e-8659-9bf0e577944f_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/b28db14b-e3a7-463e-8659-9bf0e577944f.md!}

## Further Readings

- [OpenSSH Manuals](https://www.openssh.com/manual.html)
- [OpenSSH Logging and Troubleshooting](https://en.wikibooks.org/wiki/OpenSSH/Logging_and_Troubleshooting)
