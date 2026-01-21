This section will guide you to configure the forwarding of Cisco Umbrella logs to Sekoia.io by means of AWS S3 buckets.

### Prerequisites

In order to set up the AWS architecture, you need an administrator access to the [Amazon console]( https://console.aws.amazon.com) with the permissions to create and manage S3 buckets, SQS queues, S3 notifications and users.

Ensure that the IAM user dedicated to accessing the S3 bucket and SQS Queue has the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueUrl"
            ],
            "Principal": {
                "AWS": "arn:aws:iam::XXXXXXXXXXXX:user/USERNAME_HERE"
            },
            "Effect": "Allow",
            "Resource": "arn:aws:sqs:REGION_HERE:XXXXXXXXXXXX:NAME_HERE"
        },
        {
            "Action": [
                "s3:GetObject"
            ],
            "Principal": {
                "AWS": "arn:aws:iam::XXXXXXXXXXXX:user/USERNAME_HERE"
            },
            "Effect": "Allow",
            "Resource": "arn:aws:s3:REGION_HERE:XXXXXXXXXXXX:NAME_HERE/*"
        }
    ]
}
```

Also ensure that you have access to Sekoia.io Intakes and Playbook pages with write permissions.

### Create an AWS S3 Bucket

To create a new AWS S3 Bucket, please refer to [this guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

1. On the AWS S3, go to `Buckets` and select our bucket.
2. Select `Permissions` tab and go to `Bucket Policy` section
3. Click `Edit` and paste [the JSON Bucket policy from Cisco Umbrella](https://docs.umbrella.com/deployment-umbrella/docs/setting-up-an-amazon-s3-bucket#json-bucket-policy)
4. In the Policy, replace the `bucketname` placeholde by the name of our bucket.
5. Click `Save changes`.

!!! Important
    Keep in mind to conserve the `/*` when defining in the policy.

### Configure Cisco Umbrella

1. Log on the Cisco Umbrella console
2. Go to `Admin` > `Log Management`
3. In the `Amazon S3` section, select `Use your company-managed Amazon S3 bucket`
4. In `Amazon S3 bucket`, type the name of your bucket and click `Verify`.

5. On your AWS console, go in your bucket.
6. In the `Objects` tab, click on `README_FROM_UMBRELLA.txt` then click on `Open`
7. Copy the token from the readme
8. On the Cisco Umbrella console, in the field `Token Number`, paste the token and click `Save`

!!! Note
    After clicking `Verify`, the message `Great! We successfully verified your Amazon S3 bucket` must be displayed

!!! Note
    After clicking `Save`, the message `We’re sending data to your S3 storage` must be displayed

!!! Important
    According to the type of the logs, the objects will be prefixed with `dnslogs/` for DNS logs, `proxylogs` for proxy logs, `iplogs` for ip logs, ...

### Create a SQS queue

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
