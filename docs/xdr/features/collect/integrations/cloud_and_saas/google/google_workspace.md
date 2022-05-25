uuid: 44439212-c2d8-4645-ad60-8fd5e39140b3
name: Google Cloud Audit
type: intake

{!xdr/features/collect/integrations/cloud_and_saas/google/google_cloud.md!}

{!xdr/features/collect/integrations/generated/google-cloud-audit_do_not_edit_manually.md!}

## Google Workspace configuration

To begin, follow the official documentation to [share audit logs with Google Cloud](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

Once log sharing is activated, you should be able to see Google Workspace events in Google Cloud Log Explorer.

To forward these events to SEKOIA.IO, go to `Logs Router > Create Sink` and enter the information related to your PubSub topic ([Google Cloud related documentation](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs)).
