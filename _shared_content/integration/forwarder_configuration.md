#### Configure a forwarder

To forward events using syslog to Sekoia.io, you need to update the syslog header with the intake key you previously created.
Here is an example of your message before the forwarder
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG RAW_MESSAGE]
```
and after
```
<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"YOUR_INTAKE_KEY\" RAW_MESSAGE]
```

To achieve this you can: 

- Use the [Sekoia.io forwarder](./sekoiaio_forwarder.md) which is the official supported way to collect data using the syslog protocol in Sekoia.io. In charge of centralizing data coming from many equipments/sources and forwarding them to Sekoia.io with the apporpriated format, it is a prepackaged option. You only have to provide your intake key as parameter.
- Use your own [Syslog service](./syslog_service.md) instance. Maybe you already have an intance of one of these components on your side and want to reuse it in order to centralize data before forwarding them to Sekoia.io. When using this mode, you have to configure and maintain your component in order to respect the expected Sekoia.io format. 


!!! warning 
    Only the Sekoia.io forwarder is officially supported. Other options are documented for reference purposes but do not have official support.