uuid: 46e45417-187b-45bb-bf81-30df7b1963a0
name: Amazon WAF
type: intake

## Overview
AWS WAF is a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources.

- **Vendor**: AWS
- **Plan**: Defend Prime
- **Supported environment**: SaaS
- **Detection based on**: Alert, Telemetry
- **Supported application or feature**: Web application firewall logs	

## Configure

!!! important
    In this guide, your S3 bucket for AWS WAF logging must start with `aws-waf-logs-` and can end with any suffix you want. For example, `aws-waf-logs-DOC-EXAMPLE-BUCKET-SUFFIX`. More information in [this guide](https://docs.aws.amazon.com/waf/latest/developerguide/logging-s3.html)

{!_shared_content/operations_center/integrations/aws_create_s3_sqs_notification.md!}

#### Forward traffic logs to S3

To forward events produced by AWS WAF to S3, you have to: 

1. Configure the [Permissions required to publish logs to Amazon S3](https://docs.aws.amazon.com/waf/latest/developerguide/logging-s3.html#logging-s3-permissions) in order to authorize your bucket to receive AWS WAF logs
2. In your AWS console, navigate to: `Services > WAF & Shield > Web ACLs`
3. Select the acl you want forwarding logs to your bucket
4. Select the tab `Logging and metrics`
5. In the first section, in front of the title `Logging`, click the button `Enable`
6. Check `S3 bucket` as `Logging destination` and select your bucket in the dropdown
7. Click the button `Save`

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `AWS WAF`.

### Pull events

To start to pull events, you have to: 

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3)
2. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created
3. Start the playbook and enjoy your events

{!_shared_content/operations_center/integrations/generated/46e45417-187b-45bb-bf81-30df7b1963a0_sample.md!}

## Detection section

The following section provides information for those who wish to learn more about the detection capabilities enabled by collecting this intake. It includes details about the built-in rule catalog, event categories, and ECS fields extracted from raw events. This is essential for users aiming to create [custom detection rules](/docs/xdr/features/detect/sigma.md), perform hunting activities, or pivot in the [events page](/docs/xdr/features/investigate/events.md).

{!_shared_content/operations_center/detection/generated/suggested_rules_46e45417-187b-45bb-bf81-30df7b1963a0_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/46e45417-187b-45bb-bf81-30df7b1963a0.md!}

## Further Readings
- [AWS WAF Overview](https://aws.amazon.com/waf/)
- [AWS WAF Documentation](https://docs.aws.amazon.com/waf/)
- [AWS S3 Overview](https://aws.amazon.com/s3/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
