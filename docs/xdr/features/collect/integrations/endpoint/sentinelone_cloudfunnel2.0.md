uuid: 40deb162-6bb1-4635-9c99-5c2de7e1d340
name: SentinelOne Cloud Funnel 2.0
type: intake

## Overview

SentinelOne Cloud Funnel 2.0 is the state of the art method to collect SentinelOne Deep Visibility data and extend the SentinelOne EDR to provide full visibility into endpoint data. Its patented kernel-based monitoring allows a near real-time search across endpoints for all indicators of compromise (IOC) to empower security teams to augment real-time threat detection capabilities with a powerful tool that enables threat hunting.

SentinelOne Deep Visibility logs provides in-depth logs that are useful for detection and investigation purposes.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

!!! note
    No additional installation or configuration on the agents is needed.

!!! warning
    Alerts and Events logs from the SentinelOne console are not available with CloudFunnel. To collect events to be able to have information on access to the console, one must configure the SentinelOne log collection from API as documented [here](./sentinelone.md).

Please find bellow a short list of activities that are available for security supervision thanks to SentinelOne Deep Visibility logs:

- Process Creation
- Command Script
- Duplicate Process Handle
- Duplicate Thread Handle
- Open Remote Process Handle
- Remote Thread Creation
- DNS Resolved
- DNS Unresolved
- File Creation
- File Deletion
- File Scan
- File Modification
- File Rename
- Pre Execution Detection
- Behavioral Indicators
- Login
- Logout
- Module Load
- Driver Load
- IP Connect
- IP Listen
- Registry Key Create
- Registry Key Delete
- Registry Key Export
- Registry Key Import
- Registry Key Security Changed
- Registry Key Rename
- Registry Value Create
- Registry Value Delete
- Registry Value Modified
- Scheduled Task Start
- Scheduled Task Delete
- Scheduled Task Update
- Scheduled Task Register
- Scheduled Task Trigger
- URL

{!_shared_content/operations_center/detection/generated/suggested_rules_40deb162-6bb1-4635-9c99-5c2de7e1d340_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/40deb162-6bb1-4635-9c99-5c2de7e1d340.md!}

## Configure

This setup guide will show you how to pull events produced by SentinelOne Deep Visibility on [Sekoia.io](https://app.sekoia.io/).

### Create a AWS S3 bucket

The AWS S3 bucket used to store SentinelOne Deep Visibility telemetry can be created in any preferred AWS region. However, it is important to ensure that the chosen bucket name adheres to the [AWS naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) and remains globally unique.

To enable SentinelOne's AWS account to perform necessary operations such as listing and writing objects in your bucket, it is required to authorize their account with the appropriate permissions. You can refer to the SentinelOne documentation to obtain the account's canonical ID, which is necessary for the authorization process.

By following these steps, you can set up the AWS S3 bucket to seamlessly handle SentinelOne Deep Visibility telemetry data.


{!_shared_content/operations_center/integrations/aws_create_sqs_queue.md!}

{!_shared_content/operations_center/integrations/aws_create_s3_notification.md!}

### Setup SentinelOne Cloud Funnel 2.0

Once the AWS S3 bucket is created, you can configure your SentinelOne instance to stream the telemetry to it. This is done in the "Settings > Integrations > Cloud Funnel" page of your SentinelOne instance.

A SentinelOne admin account with a "Account" user scope is required to perform this configuration.

!!! warning
    If you have multiple SentinelOne Management Consoles, you must configure Cloud Funnel 2.0 for each console.

### Create a SentinelOne Cloud Funnel 2.0 intake

In the [Sekoia.io Operations Center](https://app.sekoia.io/operations/intakes):

1. Click on the `Intake` page
2. Search for `SentinelOne Cloud Funnel 2.0` by navigating the page or using the search bar
3. Click `Create` on the relevant object
4. Specify the `Name` of your intake that will be displayed and select the `Entity` needed

### Pull events

To start pulling events, follow these steps:

1. Go to the [playbook page](https://app.sekoia.io/operations/playbooks)
2. Create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws#fetch-new-logs-on-s3)
3. Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name
4. Set up the trigger configuration with the name of the SQS queue and the intake key (from the intake previously created)
5. Start the playbook and enjoy your events
