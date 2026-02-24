# Facing issues with logs collection

Please find some general information that will help you to troubleshoot your logs collection

## General verification steps

### Configuration verification

1. Check that all pre-requisites are met
2. Configuration setup need to be done with admin permissions
3. Depending on the integration and ingestion method, a restart has to be done and delay might happen

### Collect issue

Please consult our documentation for each technology used

*Using a playbook connector*

1. Check the playbook logs
2. Check your account configuration (credentials, url...)
3. Check if the logs are generated on your technological platform

*Using a log concentrator*

1. Check the logs and send it to a local file for testing
2. Redo the installation following our documentation

!!! note
   When possible, we recommend using Sekoia.io Forwarder as it is simple and quick to use

### Parsing verification when in error

1. Check the field `sekoia.intake.parsing_error` in the events page
2. Compare events sent with the `Event Samples` of the intake documentation (expected log format)
3. For most intakes, it is possible to test through `intakes page > + new intake > <intake name>` and click on `See format`
![Intake parser access](/assets/operation_center/intakes/Intake_parser_access.png){: style="max-width:100%"}

4. Paste log and check the field `sekoia.intake.parsing_error`, please refer to [this section to test your log](https://docs.sekoia.io/xdr/features/collect/intakes/#panel-overview)

**Fields to observe**

|fields|meaning|
|--|--|
|`sekoiaio.intake.parsing_status`|result of the parsing (success / failure)|
|`sekoiaio.intake.parsing_error`|when the parsing is in failure, this field is available with information on the error that causes the failure|
|`sekoiaio.intake.parsing_warning`|some fields are not parsed correctly (detail will be displayed)|

!!! note
   Please contact Support if you have any questions or feedbacks. We will be glad to assist you.

### Truncating verification when in error

1. Check the size of the raw event, we truncate events larger than 250 KiB.
2. If events are truncated of less than 250 KiB, we recommend to check each component on the collection chain and the source to identify where the event is truncated. 
