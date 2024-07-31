
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_conf_events"

    ```
	INFO: Configuration Changed: Admin=john.doe; Object Type=EPPurgeScheduler; Object Name=f36afcff-e3af-4a70-99c0-5e5304c1c336
    ```



=== "test_miscellaneous"

    ```
	INFO: 5 endpoint(s) purged successfully
    ```



=== "test_miscellaneous1"

    ```
	2023-06-07 04:26:17.306 +0200 60198 INFO null: MnT purge event occurred, MESSAGE=completed successfully,
    ```



=== "test_miscellaneous2"

    ```
	WARN: AcsSyslogContentAaaDiagnostics:: ACTIVE_DIRECTORY_DIAGNOSTIC_TOOL_ISSUES_FOUND need to complete
    ```



=== "test_network_info_events"

    ```
	INFO: EAP Connection Timeout : Server=servername; NAS IP Address=1.2.3.4; NAS Identifier=A4:57:00:64:47:C0:test1
    ```



=== "test_network_warm1"

    ```
	WARN: Dynamic Authorization Failed for Device : Server=servername; Calling Station Id=N/A; Network device IP=1.2.3.4; Network Device
    ```



=== "test_network_warm2"

    ```
	WARN: Profiler SNMP Request Failure : Server= servername; NAD Address=1.2.3.4; Error Message=Request timed out.
    ```



=== "test_network_warn_events"

    ```
	WARN: TrustSec deploy verification failed to reach NAD.: Device Name=device005.internal.example.org; Device Ip=1.2.3.4; Device login username=admin
    ```



