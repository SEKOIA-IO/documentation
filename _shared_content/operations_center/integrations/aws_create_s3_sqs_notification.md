### Deploying the Data Collection Architecture

This section will guide you through creating all the AWS resources needed to collect AWS logs. If you already have existing resources that you want to use, you may do so, but any potential issues or incompatibilities with this tutorial will be your responsibility.

#### Prerequisites

In order to set up the AWS architecture, you need an administator access to the [Amazon console]( https://console.aws.amazon.com) with the permissions to create and manage S3 buckets, SQS queues, S3 notifications and users.

!!! Important
    Your SQS queue must be dedicated to Sekoia's usage. Once the notification is read, it is then deleted from the queue to prevent reading the same message twice. If your queue is shared with another application, some messages will be deleted before your application can read them.

=== "Automatic"

    To get started, click on the button below and fill the form on AWS to set up the required environment for Sekoia [![Deploy to AWS](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=sekoia_stack&templateURL=https://sekoia-doc-bucket.s3.eu-west-3.amazonaws.com/resources.yml)

    You need to fill 4 inputs:

    - Stack name - Name of the stack in CloudFormation (Name of the template)
    - BucketName - Name of the S3 Bucket
    - IAMUserName - Name of the dedicated user to access the S3 and SQS queue
    - SQSName - Name of the SQS queue

    Read the different pages and click on `Next`, then click on `Submit`.

    You can follow the creation in the `Events` tab (it can take few minutes).

    Once finished, it should be displayed on the left `CREATE_COMPLETE`. Click on the `Outputs` tab in order to retrieve the information needed for Sekoia playbook.

    <div style="text-align: center;">
        <img width="100%" alt="image" src="/assets/operation_center/integration_catalog/cloud_and_saas/aws/aws_cloudformation.png">
    </div>

=== "Manual"

    **Create a S3 Bucket**

    Please refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) to create a S3 Bucket.

    **Create a SQS queue**

    The collect will rely on S3 Event Notifications (SQS) to get new S3 objects.

    1. Create a queue in the SQS service by following [this guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html)
    2. In the Access Policy step, choose the advanced configuration and adapt this configuration sample with your own SQS Amazon Resource Name (ARN) (the main change is the Service directive allowing S3 bucket access):
        ```json
        {
          "Version": "2008-10-17",
          "Id": "__default_policy_ID",
          "Statement": [
            {
              "Sid": "__owner_statement",
              "Effect": "Allow",
              "Principal": {
                "Service": "s3.amazonaws.com"
              },
              "Action": "SQS:SendMessage",
              "Resource": "arn:aws:sqs:XXX:XXX"
            }
          ]
        }
        ```

    !!! Important
        Keep in mind that you have to create the SQS queue in the same region as the S3 bucket you want to watch.

    ** Create a S3 Event Notification **

    Use the [following guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) to create S3 Event Notification.
    Once created:

    1. Select the notification for object creation in the Event type section
    2. As the destination, choose the SQS service
    3. Select the queue you created in the previous section
