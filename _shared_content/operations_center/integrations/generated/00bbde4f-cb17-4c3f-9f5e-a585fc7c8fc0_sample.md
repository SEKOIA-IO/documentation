
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "gke_container_runtime2"


    ```json
	{
        "insertId": "mf28fmdkt05bbyjk",
        "jsonPayload": {
            "_CAP_EFFECTIVE": "1ffffffffff",
            "_BOOT_ID": "e61a95dc40fd44f6ba5c6bfcb18b46a2",
            "_SYSTEMD_CGROUP": "/system.slice/containerd.service",
            "_PID": "1478",
            "_SYSTEMD_INVOCATION_ID": "ebd8a874b9bf4797a358a0403ec7e1e7",
            "_EXE": "/usr/bin/containerd",
            "_TRANSPORT": "stdout",
            "_SYSTEMD_SLICE": "system.slice",
            "MESSAGE": "time=\"2022-06-01T14:01:35.371006269Z\" level=info msg=\"StopContainer for \\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\" with timeout 30 (s)\"",
            "_CMDLINE": "/usr/bin/containerd",
            "_STREAM_ID": "949cd6779ed34897a1b74883881ddfe8",
            "_HOSTNAME": "gke-cluster-1-default-pool-476246ab-wnl7",
            "_COMM": "containerd",
            "SYSLOG_IDENTIFIER": "containerd",
            "_MACHINE_ID": "3fa273bf9f602a2286f55eac7ffa6d36",
            "_GID": "0",
            "_SYSTEMD_UNIT": "containerd.service",
            "PRIORITY": "6",
            "SYSLOG_FACILITY": "3",
            "_UID": "0"
        },
        "resource": {
            "type": "k8s_node",
            "labels": {
                "cluster_name": "cluster-1",
                "project_id": "hazel-aria-348413",
                "node_name": "gke-cluster-1-default-pool-476246ab-wnl7",
                "location": "europe-west1-c"
            }
        },
        "timestamp": "2022-06-01T14:01:35.371492Z",
        "logName": "projects/hazel-aria-348413/logs/container-runtime",
        "receiveTimestamp": "2022-06-01T14:01:36.219094561Z"
    }
    ```



=== "gke_log_id_event"


    ```json
	{
        "insertId": "17ahw8eg29q74y6",
        "jsonPayload": {
            "reportingComponent": "",
            "reason": "Pulling",
            "eventTime": null,
            "reportingInstance": "",
            "kind": "Event",
            "message": "Pulling image \"gke.gcr.io/prometheus-to-sd:v0.11.3-gke.0\"",
            "apiVersion": "v1",
            "type": "Normal",
            "source": {
                "host": "gke-cluster-1-default-pool-476246ab-wnl7",
                "component": "kubelet"
            },
            "metadata": {
                "resourceVersion": "954",
                "creationTimestamp": "2022-06-01T14:05:30Z",
                "namespace": "kube-system",
                "managedFields": [
                    {
                        "manager": "kubelet",
                        "apiVersion": "v1",
                        "fieldsV1": {
                            "f:message": {},
                            "f:involvedObject": {},
                            "f:lastTimestamp": {},
                            "f:source": {
                                "f:host": {},
                                "f:component": {}
                            },
                            "f:type": {},
                            "f:reason": {},
                            "f:count": {},
                            "f:firstTimestamp": {}
                        },
                        "operation": "Update",
                        "fieldsType": "FieldsV1",
                        "time": "2022-06-01T14:05:30Z"
                    }
                ],
                "uid": "658b3d26-ed26-4d32-a5b4-3bb87bdefa99",
                "name": "kube-dns-56494768b7-544n6.16f48435f72a4bd9"
            },
            "involvedObject": {
                "resourceVersion": "6551",
                "namespace": "kube-system",
                "fieldPath": "spec.containers{prometheus-to-sd}",
                "apiVersion": "v1",
                "name": "kube-dns-56494768b7-544n6",
                "uid": "52017f74-5157-4788-a62e-b83c4eac4acf",
                "kind": "Pod"
            }
        },
        "resource": {
            "type": "k8s_pod",
            "labels": {
                "location": "europe-west1-c",
                "namespace_name": "kube-system",
                "cluster_name": "cluster-1",
                "pod_name": "kube-dns-56494768b7-544n6",
                "project_id": "hazel-aria-348413"
            }
        },
        "timestamp": "2022-06-01T14:05:30Z",
        "severity": "INFO",
        "logName": "projects/hazel-aria-348413/logs/events",
        "receiveTimestamp": "2022-06-01T14:05:39.683992581Z"
    }
    ```



=== "gke_log_id_event2"


    ```json
	{
        "insertId": "17ahw8eg29q74yc",
        "jsonPayload": {
            "eventTime": null,
            "reportingInstance": "",
            "type": "Warning",
            "reportingComponent": "",
            "metadata": {
                "resourceVersion": "960",
                "name": "kube-dns.16f484369d214dae",
                "namespace": "kube-system",
                "uid": "828b8cd3-1eec-4093-95fb-907ebeab0efa",
                "creationTimestamp": "2022-06-01T14:05:33Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "operation": "Update",
                        "fieldsV1": {
                            "f:firstTimestamp": {},
                            "f:involvedObject": {},
                            "f:reason": {},
                            "f:count": {},
                            "f:lastTimestamp": {},
                            "f:type": {},
                            "f:message": {},
                            "f:source": {
                                "f:component": {}
                            }
                        },
                        "manager": "kube-controller-manager",
                        "time": "2022-06-01T14:05:33Z",
                        "fieldsType": "FieldsV1"
                    }
                ]
            },
            "apiVersion": "v1",
            "kind": "Event",
            "message": "Failed to update endpoint kube-system/kube-dns: Operation cannot be fulfilled on endpoints \"kube-dns\": the object has been modified; please apply your changes to the latest version and try again",
            "source": {
                "component": "endpoint-controller"
            },
            "involvedObject": {
                "apiVersion": "v1",
                "uid": "75cc3b54-2a5f-42fa-8dd9-1669695113cd",
                "kind": "Endpoints",
                "namespace": "kube-system",
                "resourceVersion": "7416",
                "name": "kube-dns"
            },
            "reason": "FailedToUpdateEndpoint"
        },
        "resource": {
            "type": "k8s_cluster",
            "labels": {
                "cluster_name": "cluster-1",
                "location": "europe-west1-c",
                "project_id": "hazel-aria-348413"
            }
        },
        "timestamp": "2022-06-01T14:05:33Z",
        "severity": "WARNING",
        "logName": "projects/hazel-aria-348413/logs/events",
        "receiveTimestamp": "2022-06-01T14:05:39.683992581Z"
    }
    ```



=== "gke_log_id_event3"


    ```json
	{
        "insertId": "17ahw8eg29q74yb",
        "jsonPayload": {
            "involvedObject": {
                "namespace": "kube-system",
                "uid": "52017f74-5157-4788-a62e-b83c4eac4acf",
                "kind": "Pod",
                "resourceVersion": "6551",
                "fieldPath": "spec.containers{prometheus-to-sd}",
                "apiVersion": "v1",
                "name": "kube-dns-56494768b7-544n6"
            },
            "kind": "Event",
            "apiVersion": "v1",
            "eventTime": null,
            "reportingInstance": "",
            "metadata": {
                "managedFields": [
                    {
                        "time": "2022-06-01T14:05:32Z",
                        "manager": "kubelet",
                        "fieldsType": "FieldsV1",
                        "operation": "Update",
                        "apiVersion": "v1",
                        "fieldsV1": {
                            "f:count": {},
                            "f:type": {},
                            "f:involvedObject": {},
                            "f:source": {
                                "f:component": {},
                                "f:host": {}
                            },
                            "f:reason": {},
                            "f:firstTimestamp": {},
                            "f:message": {},
                            "f:lastTimestamp": {}
                        }
                    }
                ],
                "namespace": "kube-system",
                "creationTimestamp": "2022-06-01T14:05:32Z",
                "name": "kube-dns-56494768b7-544n6.16f48436899e3f4a",
                "resourceVersion": "959",
                "uid": "2836bb34-8703-4475-a7d8-5cf0ec2232f8"
            },
            "message": "Created container prometheus-to-sd",
            "reason": "Created",
            "type": "Normal",
            "source": {
                "host": "gke-cluster-1-default-pool-476246ab-wnl7",
                "component": "kubelet"
            },
            "reportingComponent": ""
        },
        "resource": {
            "type": "k8s_pod",
            "labels": {
                "project_id": "hazel-aria-348413",
                "namespace_name": "kube-system",
                "cluster_name": "cluster-1",
                "pod_name": "kube-dns-56494768b7-544n6",
                "location": "europe-west1-c"
            }
        },
        "timestamp": "2022-06-01T14:05:32Z",
        "severity": "INFO",
        "logName": "projects/hazel-aria-348413/logs/events",
        "receiveTimestamp": "2022-06-01T14:05:39.683992581Z"
    }
    ```



=== "k8s_node"


    ```json
	{
        "insertId": "32ez47f5wz17i",
        "jsonPayload": {
            "apiVersion": "v1",
            "eventTime": null,
            "involvedObject": {
                "kind": "Node",
                "name": "gke-cluster-1-default-pool-eb66079e-k3zf",
                "uid": "gke-cluster-1-default-pool-eb66079e-k3zf"
            },
            "kind": "Event",
            "message": "{\"unmanaged\": {\"net.netfilter.nf_conntrack_buckets\": \"32768\"}}",
            "metadata": {
                "creationTimestamp": "2022-06-15T01:55:51Z",
                "managedFields": [
                    {
                        "apiVersion": "v1",
                        "fieldsType": "FieldsV1",
                        "fieldsV1": {
                            "f:count": {},
                            "f:firstTimestamp": {},
                            "f:involvedObject": {},
                            "f:lastTimestamp": {},
                            "f:message": {},
                            "f:reason": {},
                            "f:source": {
                                "f:component": {},
                                "f:host": {}
                            },
                            "f:type": {}
                        },
                        "manager": "node-problem-detector",
                        "operation": "Update",
                        "time": "2022-06-15T01:55:51Z"
                    }
                ],
                "name": "gke-cluster-1-default-pool-eb66079e-k3zf.16f8813a8514b8c0",
                "namespace": "default",
                "resourceVersion": "894",
                "uid": "7e26b736-331a-4896-961f-96688918ba7e"
            },
            "reason": "NodeSysctlChange",
            "reportingComponent": "",
            "reportingInstance": "",
            "source": {
                "component": "sysctl-monitor",
                "host": "gke-cluster-1-default-pool-eb66079e-k3zf"
            },
            "type": "Warning"
        },
        "logName": "projects/hazel-aria-348413/logs/events",
        "receiveTimestamp": "2022-06-15T01:55:52.012275121Z",
        "resource": {
            "labels": {
                "cluster_name": "cluster-1",
                "location": "europe-central2-a",
                "node_name": "gke-cluster-1-default-pool-eb66079e-k3zf",
                "project_id": "hazel-aria-348413"
            },
            "type": "k8s_node"
        },
        "severity": "WARNING",
        "timestamp": "2022-06-15T01:55:51Z"
    }
    ```



=== "k8s_textPayload"


    ```json
	{
        "insertId": "1wtrhknf2gg14w",
        "logName": "projects/hazel-aria-348413/logs/events",
        "receiveTimestamp": "2022-06-16T09:42:59.259491841Z",
        "resource": {
            "labels": {
                "cluster_name": "cluster-1",
                "location": "europe-central2-a",
                "project_id": "hazel-aria-348413"
            },
            "type": "k8s_cluster"
        },
        "severity": "WARNING",
        "textPayload": "Event exporter started watching. Some events may have been lost up to this point.",
        "timestamp": "2022-06-16T09:42:39.200653463Z"
    }
    ```



