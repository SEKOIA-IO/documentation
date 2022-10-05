uuid: 44439212-c2d8-4645-ad60-8fd5e39140b3
name: Google Cloud Audit
type: intake

{!_shared_content/operations_center/integrations/google_cloud.md!}

{!_shared_content/operations_center/integrations/generated/google-cloud-audit_do_not_edit_manually.md!}

## Google Workspace configuration

To begin, follow the official documentation to [share audit logs with Google Cloud](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

Once log sharing is activated, you should be able to see Google Workspace events in Google Cloud Log Explorer.

To forward these events to SEKOIA.IO, go to `Logs Router > Create Sink` and enter the information related to your PubSub topic ([Google Cloud related documentation](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs)).

Your inclusion filter should contain the following (don't forget to specify your organization ID):

```
protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog"
logName="organizations/<YOUR ORGANISATION ID>/logs/cloudaudit.googleapis.com%2Factivity"
```

## Retrieve Google Cloud Audit logs with playbook module

Please create a playbook with module `Connect to the specified`

Fields to be completed
|Field|Meaning|
|---|---|
|name| Configuration name|
|auth_provider_x509_cert_url| The URL of the public x509 certificate, used to verify the signature on JWTs, such as ID tokens, signed by the authentication provider. `https://wwww.googleapis.com/oauth2/v1/certs`|
|auth_url| Google authentification url `https://accounts.google.com/o/oauth2/auth`|
|client_email| Client email|
|client_id| Client id|
|client_x509_cert_url| The URL of the public x509 certificate, used to verify JWTs signed by the client|
|private_key| Private key|
|private_key_id| Private key id|
|project_id| Project id|
|token_uri| token server endpoint URI `https://oauth2.googleapis.com/token`|
|type|Activity type `service_account`|

