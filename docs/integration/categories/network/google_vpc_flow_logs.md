uuid: 515ed00f-bf70-4fce-96cc-0ca31abd5d24
name: Google VPC Flow Logs
type: intake

{!_shared_content/operations_center/integrations/google_cloud.md!}



## Google VPC Flow Logs configuration

To start working with VPC Flow Logs, activate the option by editing or creating a subnet (see [Google's documentation](https://cloud.google.com/vpc/docs/using-flow-logs#enable-logging-new))

This subnet can be assigned to your node or kubernetes cluster.

The network logs should now be visible in Cloud Logging. A filter can now be created to stream your logs to Sekoia.io. To create this filter, follow this [documentation](https://cloud.google.com/vpc/docs/using-flow-logs#access-logs).

Start the playbook and enjoy your events.

{!_shared_content/integration/detection_section.md!}
{!_shared_content/operations_center/integrations/generated/515ed00f-bf70-4fce-96cc-0ca31abd5d24.md!}

