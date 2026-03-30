---
uuid: 7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162
name: Netskope Log Streaming (Transaction Events)
type: intake
---

# netskope\_log\_streaming

### Overview

Netskope Log Streaming allows you to access all Netskope-generated logs directly within your preferred cloud storage and further SIEM tools without the need for additional infrastructure like VMs, improving scalability, cost efficiency, and real-time data availability.

* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**:
  * Transaction Events

### Configure

{!\_shared\_content/operations\_center/integrations/aws\_create\_s3\_sqs\_notification.md!}

#### Configure Netskope Log stream

1.  Navigate to **Settings > Tools > Log Streaming** to add names and properties for the streams you want to monitor.

    {: style="max-width:100%"}
2.  Click **Create Stream**. In **Name**, enter a human-readable name for the stream

    {: style="max-width:100%"}
3. Select `Transaction Events` dataset
4. Choose `GZIP`
5.  For the Amazon S3 destination field, fill in the fields

    {: style="max-width:100%"}
6. Activate the stream upon saving

!!! Note Select Amazon S3 with SQS for optimum performance. Stream activation takes about 60 minutes from creation.

#### Instruction on Sekoia

#### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Netskope Transaction Events with AWS S3`.

#### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the AWS `Fetch new logs on S3` trigger.

Set up the module configuration with the `AWS access Key ID`, the `AWS secret access Key` and the `AWS region name`. Set up the trigger configuration with the `AWS SQS queue name` and the `intake key`, from the intake previously created.

Start the playbook and enjoy your events.

{!\_shared\_content/operations\_center/integrations/generated/7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/7b6d0592-9e0e-4db0-adf0-c9ab2d5c2162.md!}
