### Prerequisites

- An administator access to the [Amazon console]( https://console.aws.amazon.com) with the permission to create SQS queue and S3 notifications.
- A **self managed** AWS S3 bucket where events will be published prior to be consumed by Sekoia.io.

### Create a SQS queue

This integration relies on S3 Event Notifications (SQS) to discover new S3 objects.

To enable the S3 Event Notification:

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
          "Action": "SQS:*",
          "Resource": "arn:aws:sqs:XXX:XXX"
        }
      ]
    }
    ```

!!! note
    Keep in mind that you have to create the SQS queue in the same region as the S3 bucket you want to watch.
