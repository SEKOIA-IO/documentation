
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "event_attack"

    ```
	20-03-2025 07:49:10 WARNING 1282 ErtFeed "ERT Active Attacker: ERT;SCN" TCP 1.2.3.4 56789 5.6.7.8 8080 1 Regular "test4" occur 1 0 2605 0 N/A high drop FFFFFFFF-0000-4567-8989-012345678901
    ```



=== "event_bdos"

    ```
	01-08-2025 12:55:01 INFO BDoS baseline learning is being suppressed now on inbound IPv4 traffic for policy "test".
    ```



=== "event_login"

    ```
	01-07-2025 10:49:12 INFO User jdoe logged in via ssh 1.2.3.4
    ```



