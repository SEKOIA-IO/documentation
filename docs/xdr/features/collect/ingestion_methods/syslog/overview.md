# How to forward logs to Sekoia.io using Syslog

## Overview

To push your events to Sekoia.io, you can use also use the syslog protocol. 

Before processing, you have to:

- Connect to [Sekoia.io Operations Center](https://app.sekoia.io/operations/)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

To forward events using syslog to Sekoia.io, you need to send events using TLS to `intake.sekoia.io:10514` and ensure compliance with RFC 5426. Additionally, you must update the syslog header with the intake key you previously created.

To achieve this you can: 

- Use the [Sekoia.io forwarder](./sekoiaio_forwarder.md) which is the official supported way to collect data using the syslog protocol in Sekoia.io. In charge of centralizing data coming from many equipments/sources and forwarding them to Sekoia.io with the apporpriated format, it is a prepackaged option. You only have to provide your intake key as parameter.
- Use your own [Syslog service](./syslog_service.md) instance. Maybe you already have an intance of one of these components on your side and want to reuse it in order to centralize data before forwarding them to Sekoia.io. When using this mode, you have to configure and maintain your component in order to respect the expected Sekoia.io format. 


!!! warning 
    Only the Sekoia.io forwarder is officially supported. Other options are documented for reference purposes but do not have official support.