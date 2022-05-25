uuid: b28db14b-e3a7-463e-8659-9bf0e577944f
name: OpenSSH
type: intake

## Overview
OpenSSH is the premier connectivity tool for remote login with the SSH protocol. It encrypts all traffic to eliminate eavesdropping, connection hijacking, and other attacks. In addition, OpenSSH provides a large suite of secure tunneling capabilities, several authentication methods, and sophisticated configuration options.

{!xdr/features/collect/integrations/generated/openssh_do_not_edit_manually.md!}

## Configure

As of now, the main solution to collect OpenSSH logs leverages the Rsyslog recipe. Please share your experiences with other recipes by editing this documentation.

### Rsyslog

Please refer to the documentation of OpenSSH to forward events to your rsyslog server. The reader can consult the [Rsyslog Transport](../../../data_collection/ingestion_methods/rsyslog/) documentation to forward these logs to SEKOIA.IO.

## Further Readings

- [OpenSSH Manuals](https://www.openssh.com/manual.html)
- [OpenSSH Logging and Troubleshooting](https://en.wikibooks.org/wiki/OpenSSH/Logging_and_Troubleshooting)
