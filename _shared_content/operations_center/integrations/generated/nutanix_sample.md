### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by Nutanix sources. These examples help integrators understand the data format before ingestion and parsing.

=== "api_audit_example"


    ```json
    {"entityType":"vm","name":"web-01","uuid":"e4f1c7d2-1234-5678-9abc-def012345678","alertUid":"VmCreateAudit","operationType":"Create","userName":"admin@example.com","userUuid":"u-9a8b7c6d","creationTimestampUsecs":1682890496000000}
    ```


=== "policy_hit_syslog"


    ```text
    <14>1 2026-05-01T12:35:10Z prism.example.com NUTANIX POLICY_HIT - timestamp=2026-05-01T12:35:09Z policy_uuid=abcd-1234 policy_name=default session=Create SRC=10.0.0.5 DST=10.0.0.10 PROTO=6 ACTION=Allow packets=10 bytes=1250
    ```


These samples are taken from the integration documentation and should be adapted if your Prism version uses different field names or formats.
