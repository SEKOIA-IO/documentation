uuid: 40deb162-6bb1-4635-9c99-5c2de7e1d340
name: SentinelOne Cloud Funnel 2.0
type: intake

## Overview

SentinelOne Cloud Funnel 2.0 is the state of the art method to collect SentinelOne Deep Visibility data and extend the SentinelOne EDR to provide full visibility into endpoint data. Its patented kernel-based monitoring allows a near real-time search across endpoints for all indicators of compromise (IOC) to empower security teams to augment real-time threat detection capabilities with a powerful tool that enables threat hunting.

SentinelOne Deep Visibility logs provides in-depth logs that are useful for detection and investigation purposes.

!!! warning
    This format is still in beta, please use it wisely.

!!! note
    No additional installation or configuration on the agents is needed.

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

This setup guide will show you how to pull events produced by SentinelOne Deep Visibility on [SEKOIA.IO](https://app.sekoia.io/).

### Create a AWS S3 bucket

The AWS S3 bucket that will hold the SentinelOne Deep Visibility telemetry can be created in any region you like, the bucket name must be globally unique and follow [AWS naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
You will need to authorize SentinelOne's AWS account to list and write objects on your bucket (please refer to SentinelOne documentation to obtain the account canonical ID).

{!_shared_content/operations_center/integrations/aws_create_sqs_queue.md!}

{!_shared_content/operations_center/integrations/aws_create_s3_notification.md!}

### Setup SentinelOne Cloud Funnel 2.0

Once the AWS S3 bucket is created, you can configure your SentinelOne instance to stream the telemetry to it. This is done in the "Settings > Integrations > Cloud Funnel" page of your SentinelOne instance (a SentinelOne admin account with a "Account" user scope is required to perform this configuration).

**Important**: If you have multiple SentinelOne Management Consoles, you must configure Cloud Funnel 2.0 for each console.

### Create a SentinelOne Cloud Funnel 2.0 intake

In the [SEKOIA.IO Operation Center](https://app.sekoia.io/operations/intakes):

1. Click on the `Intake` page.
2. Search for `SentinelOne Cloud Funnel 2.0` by navigating the page or using the search bar.
3. Click `Create` on the relevant object.
4. Specify the `Name` of your intake that will be displayed and the related `Entity`:

### Pull events

Go to the [playbook page](https://app.sekoia.io/operations/playbooks) and create a new playbook with the [AWS Fetch new logs on S3 connector](../../../../automate/library/aws.md#fetch-new-logs-on-s3).

Set up the module configuration with the [AWS Access Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), the secret key and the region name. Set up the trigger configuration with the name of the SQS queue and the intake key, from the intake previously created.

Start the playbook and enjoy your events.