
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "configuration_access1"


    ```json
	{
        "deviceType": "Desktop",
        "ipAddress": "8.8.8.8",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "taskDisplayName": "Get OMS Session Data (Web Service)",
        "requestTime": "2025-11-27T08:22:48.799Z",
        "taskId": "dc1bea8c446c11de98360015c5e6daf6",
        "systemAccount": "T00000000",
        "sessionId": "1a1a1a",
        "activityAction": "READ",
        "tenantId": "client",
        "tenantHost": "wd1-service.myworkday.com"
    }
    ```



=== "configuration_access2"


    ```json
	{
        "taskId": "dc71c6e6446c11de98360015c5e6daf6",
        "activityAction": "READ",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "deviceType": "Desktop",
        "ipAddress": "8.8.8.8",
        "systemAccount": "T0000000",
        "sessionId": "1a1a1a",
        "requestTime": "2025-11-26T14:41:19.892Z",
        "taskDisplayName": "getEditResult -> get edit result (System)",
        "tenantId": "client",
        "tenantHost": "wd1-services.myworkday.com"
    }
    ```



=== "configuration_change"


    ```json
	{
        "ipAddress": "8.8.8.8",
        "activityAction": "READ",
        "taskDisplayName": "Edit Customer Service Active View",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "taskId": "984c81981d0449af9ef5ef7231f146e8",
        "sessionId": "a1a1a1",
        "deviceType": "Desktop",
        "requestTime": "2025-11-26T14:14:48.238Z",
        "systemAccount": "T000000",
        "tenantId": "client",
        "tenantHost": "wd1-services.myworkday.com"
    }
    ```



=== "start_session"


    ```json
	{
        "sessionId": "1a1a1a",
        "deviceType": "Phone",
        "taskDisplayName": "Start New Session (Web Service)",
        "activityAction": "READ",
        "ipAddress": "8.8.8.8",
        "systemAccount": "T0000000",
        "taskId": "03f043df676e40cfad46bc576f89b07f",
        "userAgent": "Workday/2025.09.2.20064 (AndroidNative)",
        "requestTime": "2025-10-14T15:39:24.334Z",
        "tenantId": "client",
        "tenantHost": "wd1-service.myworkday.com"
    }
    ```



=== "task_info"


    ```json
	{
        "taskDisplayName": "Complete Manager Input",
        "taskId": "dc2d85a8446c11de98360015c5e6daf6",
        "ipAddress": "8.8.8.8",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "activityAction": "READ",
        "deviceType": "Desktop",
        "systemAccount": "T000000",
        "sessionId": "1a1a1a",
        "requestTime": "2025-11-27T09:05:07.593Z",
        "tenantId": "client",
        "tenantHost": "wd1-services.myworkday.com"
    }
    ```



=== "url_access"


    ```json
	{
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "deviceType": "Desktop",
        "taskDisplayName": "feature/toggles/get (GET) (v0 - \u2005)",
        "systemAccount": "T0000000",
        "activityAction": "READ",
        "ipAddress": "8.8.8.8",
        "taskId": "d71d2db783c51220103fd29958a38117",
        "sessionId": "1a1a1a",
        "requestTime": "2025-10-14T15:34:25.638Z",
        "tenantId": "client",
        "tenantHost": "wd1-service.myworkday.com"
    }
    ```



=== "url_access2"


    ```json
	{
        "sessionId": "1a1a1a",
        "activityAction": "READ",
        "taskDisplayName": "sso/idTokenForSession/forTargetService (GET) (v1 - \u2005)",
        "taskId": "dfdeaac4dec91000098116a0f74b8794",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "systemAccount": "T0000000",
        "deviceType": "Desktop",
        "ipAddress": "8.8.8.8",
        "requestTime": "2025-10-14T15:31:00.642Z",
        "tenantId": "client",
        "tenantHost": "wd1-service.myworkday.com"
    }
    ```



