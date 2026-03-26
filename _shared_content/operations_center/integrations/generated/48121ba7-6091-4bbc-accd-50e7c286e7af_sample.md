
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "external_connection"


    ```json
	{
        "event_id": 7077685489580260926,
        "event_type": "External connection",
        "source": 8903162277747742819,
        "seen_at": 1764596280793,
        "source_ip": "192.0.2.0",
        "source_mac": "00:1A:2B:3C:4D:5E",
        "dest_ip": "198.51.100.0",
        "dest_mac": "00:1A:2B:3C:4D:5E",
        "proto_path": "/Ethernet/Ipv4/Tcp/Http/",
        "network_protocol": "http"
    }
    ```



