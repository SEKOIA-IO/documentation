
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_login_success"

    ```json
    {
      "object": "event",
      "type": 1000,
      "itemId": null,
      "collectionId": null,
      "groupId": null,
      "policyId": null,
      "memberId": null,
      "actingUserId": "11111111-1111-1111-1111-111111111111",
      "date": "2026-10-01T08:14:22.331Z",
      "device": 2,
      "ipAddress": "198.51.100.42"
    }
    ```


=== "test_secret_accessed"

    ```json
    {
      "object": "event",
      "type": 2100,
      "secretId": "22222222-2222-2222-2222-222222222222",
      "projectId": "33333333-3333-3333-3333-333333333333",
      "serviceAccountId": "44444444-4444-4444-4444-444444444444",
      "actingUserId": "11111111-1111-1111-1111-111111111111",
      "date": "2026-10-02T10:00:00.000Z",
      "ipAddress": "203.0.113.10"
    }
    ```
