
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "flow_logs_gke"


    ```json
	{
        "insertId": "1sxgleif1dyxla",
        "jsonPayload": {
            "dest_gke_details": {
                "cluster": {
                    "cluster_location": "europe-central2-a",
                    "cluster_name": "cluster-3"
                }
            },
            "src_location": {
                "continent": "Europe",
                "country": "pol",
                "asn": 15169
            },
            "dest_vpc": {
                "vpc_name": "foo",
                "project_id": "hazel-aria-348413",
                "subnetwork_name": "foo"
            },
            "start_time": "2022-06-03T12:09:42.501046130Z",
            "end_time": "2022-06-03T12:09:42.768509812Z",
            "bytes_sent": "1872",
            "reporter": "DEST",
            "connection": {
                "src_ip": "34.118.64.229",
                "dest_port": 45950,
                "dest_ip": "10.0.0.4",
                "src_port": 443,
                "protocol": 6
            },
            "dest_instance": {
                "region": "europe-central2",
                "zone": "europe-central2-a",
                "vm_name": "gke-cluster-3-default-pool-4e355575-tdhx",
                "project_id": "hazel-aria-348413"
            },
            "packets_sent": "16"
        },
        "resource": {
            "type": "gce_subnetwork",
            "labels": {
                "subnetwork_id": "7449846049104218257",
                "subnetwork_name": "foo",
                "project_id": "hazel-aria-348413",
                "location": "europe-central2-a"
            }
        },
        "timestamp": "2022-06-03T12:09:43.654174991Z",
        "logName": "projects/hazel-aria-348413/logs/compute.googleapis.com%2Fvpc_flows",
        "receiveTimestamp": "2022-06-03T12:09:43.654174991Z"
    }
    ```



=== "flow_logs_gke2"


    ```json
	{
        "insertId": "17aa0kaf4hig5c",
        "jsonPayload": {
            "end_time": "2022-06-03T12:09:44.424429165Z",
            "packets_sent": "32",
            "src_location": {
                "asn": 15169,
                "country": "pol",
                "continent": "Europe"
            },
            "start_time": "2022-06-03T12:09:44.421947861Z",
            "dest_vpc": {
                "subnetwork_name": "foo",
                "vpc_name": "foo",
                "project_id": "hazel-aria-348413"
            },
            "bytes_sent": "33792",
            "reporter": "DEST",
            "dest_instance": {
                "region": "europe-central2",
                "project_id": "hazel-aria-348413",
                "vm_name": "gke-cluster-3-default-pool-4e355575-k1w8",
                "zone": "europe-central2-a"
            },
            "dest_gke_details": {
                "cluster": {
                    "cluster_location": "europe-central2-a",
                    "cluster_name": "cluster-3"
                }
            },
            "connection": {
                "protocol": 6,
                "dest_ip": "10.0.0.3",
                "src_ip": "34.118.64.229",
                "src_port": 443,
                "dest_port": 41834
            }
        },
        "resource": {
            "type": "gce_subnetwork",
            "labels": {
                "project_id": "hazel-aria-348413",
                "subnetwork_name": "foo",
                "subnetwork_id": "7449846049104218257",
                "location": "europe-central2-a"
            }
        },
        "timestamp": "2022-06-03T12:09:52.418604934Z",
        "logName": "projects/hazel-aria-348413/logs/compute.googleapis.com%2Fvpc_flows",
        "receiveTimestamp": "2022-06-03T12:09:52.418604934Z"
    }
    ```



