uuid: 44439212-c2d8-4645-ad60-8fd5e39140b3
name: Google Cloud Audit
type: intake

{!_shared_content/operations_center/integrations/google_cloud.md!}

{!_shared_content/operations_center/integrations/generated/44439212-c2d8-4645-ad60-8fd5e39140b3.md!}

## Google Workspace configuration

To begin, follow the official documentation to [share audit logs with Google Cloud](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

Once log sharing is activated, you should be able to see Google Workspace events in Google Cloud Log Explorer.

To forward these events to SEKOIA.IO, go to `Logs Router > Create Sink` and enter the information related to your PubSub topic ([Google Cloud related documentation](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs)).

Your inclusion filter should contain the following (don't forget to specify your organization ID):

```
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
logName="organizations/<YOUR ORGANISATION ID>/logs/cloudaudit.googleapis.com%2Factivity"
```