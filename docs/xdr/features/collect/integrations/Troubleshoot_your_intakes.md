# Troubleshoot your intakes

Please find some information to help you to troubleshoot your intakes

## General verification steps

### Configuration verification
1. Check that all pre-requisites are met
2. Configuration setup need to be done with admin permissions
3. Depending on the integrations, a restart has to be done and delay might happen

### Collect issue
Please consult our documentation for each technology used

*Using a playbook connector*
1. Check the logs
2. Check your account configuration (credentials, url...)

*Using a log concentrator*
1. Check the logs and send it to a local file
2. Redo the installation following our documentation

   !!note
   When possible, we recommend using Sekoia.io Forwarder as it is simple and quick to use

### Test

1. Check the field `sekoia.intake.parsing_error` in the events page
<image>
2. Compare events send with the event sample in the documentation of the intake (expected log format)
<image>
3. For most intakes, it is possible to test through `intakes page > + new intake > <intake name>` and click on `See format`
<image>
4. Paste log and check the field `sekoia.intake.parsing_error`
<image>

   !!note
   Please contact Support if you have any questions or feedbacks. We will be glad to assist you.
