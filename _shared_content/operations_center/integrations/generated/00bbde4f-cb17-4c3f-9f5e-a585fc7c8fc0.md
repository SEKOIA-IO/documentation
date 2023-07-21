
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Application logs` | Google Kubernetes Engine logs contains events from applications deployed in Google Cloud containers. |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `process` |
| Type | `change` |




## Event Samples

Find below few samples of events and how they are normalized by Sekoia.io.


=== "gke_container_runtime2.json"

    ```json
	
    {
        "message": "{\n  \"insertId\": \"mf28fmdkt05bbyjk\",\n  \"jsonPayload\": {\n    \"_CAP_EFFECTIVE\": \"1ffffffffff\",\n    \"_BOOT_ID\": \"e61a95dc40fd44f6ba5c6bfcb18b46a2\",\n    \"_SYSTEMD_CGROUP\": \"/system.slice/containerd.service\",\n    \"_PID\": \"1478\",\n    \"_SYSTEMD_INVOCATION_ID\": \"ebd8a874b9bf4797a358a0403ec7e1e7\",\n    \"_EXE\": \"/usr/bin/containerd\",\n    \"_TRANSPORT\": \"stdout\",\n    \"_SYSTEMD_SLICE\": \"system.slice\",\n    \"MESSAGE\": \"time=\\\"2022-06-01T14:01:35.371006269Z\\\" level=info msg=\\\"StopContainer for \\\\\\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\\\\\" with timeout 30 (s)\\\"\",\n    \"_CMDLINE\": \"/usr/bin/containerd\",\n    \"_STREAM_ID\": \"949cd6779ed34897a1b74883881ddfe8\",\n    \"_HOSTNAME\": \"gke-cluster-1-default-pool-476246ab-wnl7\",\n    \"_COMM\": \"containerd\",\n    \"SYSLOG_IDENTIFIER\": \"containerd\",\n    \"_MACHINE_ID\": \"3fa273bf9f602a2286f55eac7ffa6d36\",\n    \"_GID\": \"0\",\n    \"_SYSTEMD_UNIT\": \"containerd.service\",\n    \"PRIORITY\": \"6\",\n    \"SYSLOG_FACILITY\": \"3\",\n    \"_UID\": \"0\"\n  },\n  \"resource\": {\n    \"type\": \"k8s_node\",\n    \"labels\": {\n      \"cluster_name\": \"cluster-1\",\n      \"project_id\": \"hazel-aria-348413\",\n      \"node_name\": \"gke-cluster-1-default-pool-476246ab-wnl7\",\n      \"location\": \"europe-west1-c\"\n    }\n  },\n  \"timestamp\": \"2022-06-01T14:01:35.371492Z\",\n  \"logName\": \"projects/hazel-aria-348413/logs/container-runtime\",\n  \"receiveTimestamp\": \"2022-06-01T14:01:36.219094561Z\"\n}",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ],
            "reason": "StopContainer for \\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\" with timeout 30 (s)"
        },
        "@timestamp": "2022-06-01T14:01:35.371492Z",
        "orchestrator": {
            "type": "kubernetes",
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "type": "k8s_node"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "mf28fmdkt05bbyjk",
            "logName": "projects/hazel-aria-348413/logs/container-runtime",
            "receiveTimestamp": "2022-06-01T14:01:36.219094561Z",
            "jsonPayload": {
                "MESSAGE": "time=\"2022-06-01T14:01:35.371006269Z\" level=info msg=\"StopContainer for \\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\" with timeout 30 (s)\"",
                "SYSLOG_IDENTIFIER": "containerd",
                "_BOOT_ID": "e61a95dc40fd44f6ba5c6bfcb18b46a2",
                "_CAP_EFFECTIVE": "1ffffffffff",
                "_COMM": "containerd",
                "_GID": 0,
                "_STREAM_ID": "949cd6779ed34897a1b74883881ddfe8",
                "_SYSTEMD_CGROUP": "/system.slice/containerd.service",
                "_SYSTEMD_INVOCATION_ID": "ebd8a874b9bf4797a358a0403ec7e1e7",
                "_SYSTEMD_SLICE": "system.slice",
                "_SYSTEMD_UNIT": "containerd.service",
                "_TRANSPORT": "stdout",
                "_UID": "0"
            }
        },
        "log": {
            "syslog": {
                "priority": 6,
                "facility": {
                    "code": 3
                }
            }
        },
        "process": {
            "command_line": "/usr/bin/containerd",
            "executable": "/usr/bin/containerd",
            "pid": 1478
        },
        "host": {
            "name": "gke-cluster-1-default-pool-476246ab-wnl7",
            "id": "3fa273bf9f602a2286f55eac7ffa6d36"
        },
        "server": {
            "geo": {
                "name": "europe-west1-c"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```


=== "gke_log_id_event.json"

    ```json
	
    {
        "message": "{\n  \"insertId\": \"17ahw8eg29q74y6\",\n  \"jsonPayload\": {\n    \"reportingComponent\": \"\",\n    \"reason\": \"Pulling\",\n    \"eventTime\": null,\n    \"reportingInstance\": \"\",\n    \"kind\": \"Event\",\n    \"message\": \"Pulling image \\\"gke.gcr.io/prometheus-to-sd:v0.11.3-gke.0\\\"\",\n    \"apiVersion\": \"v1\",\n    \"type\": \"Normal\",\n    \"source\": {\n      \"host\": \"gke-cluster-1-default-pool-476246ab-wnl7\",\n      \"component\": \"kubelet\"\n    },\n    \"metadata\": {\n      \"resourceVersion\": \"954\",\n      \"creationTimestamp\": \"2022-06-01T14:05:30Z\",\n      \"namespace\": \"kube-system\",\n      \"managedFields\": [\n        {\n          \"manager\": \"kubelet\",\n          \"apiVersion\": \"v1\",\n          \"fieldsV1\": {\n            \"f:message\": {},\n            \"f:involvedObject\": {},\n            \"f:lastTimestamp\": {},\n            \"f:source\": {\n              \"f:host\": {},\n              \"f:component\": {}\n            },\n            \"f:type\": {},\n            \"f:reason\": {},\n            \"f:count\": {},\n            \"f:firstTimestamp\": {}\n          },\n          \"operation\": \"Update\",\n          \"fieldsType\": \"FieldsV1\",\n          \"time\": \"2022-06-01T14:05:30Z\"\n        }\n      ],\n      \"uid\": \"658b3d26-ed26-4d32-a5b4-3bb87bdefa99\",\n      \"name\": \"kube-dns-56494768b7-544n6.16f48435f72a4bd9\"\n    },\n    \"involvedObject\": {\n      \"resourceVersion\": \"6551\",\n      \"namespace\": \"kube-system\",\n      \"fieldPath\": \"spec.containers{prometheus-to-sd}\",\n      \"apiVersion\": \"v1\",\n      \"name\": \"kube-dns-56494768b7-544n6\",\n      \"uid\": \"52017f74-5157-4788-a62e-b83c4eac4acf\",\n      \"kind\": \"Pod\"\n    }\n  },\n  \"resource\": {\n    \"type\": \"k8s_pod\",\n    \"labels\": {\n      \"location\": \"europe-west1-c\",\n      \"namespace_name\": \"kube-system\",\n      \"cluster_name\": \"cluster-1\",\n      \"pod_name\": \"kube-dns-56494768b7-544n6\",\n      \"project_id\": \"hazel-aria-348413\"\n    }\n  },\n  \"timestamp\": \"2022-06-01T14:05:30Z\",\n  \"severity\": \"INFO\",\n  \"logName\": \"projects/hazel-aria-348413/logs/events\",\n  \"receiveTimestamp\": \"2022-06-01T14:05:39.683992581Z\"\n}",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ],
            "reason": "Pulling image \"gke.gcr.io/prometheus-to-sd:v0.11.3-gke.0\"",
            "action": "Pulling"
        },
        "@timestamp": "2022-06-01T14:05:30Z",
        "orchestrator": {
            "type": "kubernetes",
            "api_version": "v1",
            "namespace": "kube-system",
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "name": "kube-dns-56494768b7-544n6",
                "type": "k8s_pod"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "17ahw8eg29q74y6",
            "logName": "projects/hazel-aria-348413/logs/events",
            "receiveTimestamp": "2022-06-01T14:05:39.683992581Z",
            "severity": "INFO",
            "jsonPayload": {
                "apiVersion": "v1",
                "kind": "Event",
                "type": "Normal",
                "involvedObject": {
                    "fieldPath": "spec.containers{prometheus-to-sd}",
                    "kind": "Pod",
                    "name": "kube-dns-56494768b7-544n6",
                    "resourceVersion": "6551",
                    "uid": "52017f74-5157-4788-a62e-b83c4eac4acf"
                },
                "metadata": {
                    "creationTimestamp": "2022-06-01T14:05:30Z",
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
                    "resourceVersion": "954",
                    "uid": "658b3d26-ed26-4d32-a5b4-3bb87bdefa99"
                },
                "source": {
                    "component": "kubelet"
                }
            }
        },
        "host": {
            "name": "gke-cluster-1-default-pool-476246ab-wnl7"
        },
        "server": {
            "geo": {
                "name": "europe-west1-c"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```


=== "gke_log_id_event2.json"

    ```json
	
    {
        "message": "{\n  \"insertId\": \"17ahw8eg29q74yc\",\n  \"jsonPayload\": {\n    \"eventTime\": null,\n    \"reportingInstance\": \"\",\n    \"type\": \"Warning\",\n    \"reportingComponent\": \"\",\n    \"metadata\": {\n      \"resourceVersion\": \"960\",\n      \"name\": \"kube-dns.16f484369d214dae\",\n      \"namespace\": \"kube-system\",\n      \"uid\": \"828b8cd3-1eec-4093-95fb-907ebeab0efa\",\n      \"creationTimestamp\": \"2022-06-01T14:05:33Z\",\n      \"managedFields\": [\n        {\n          \"apiVersion\": \"v1\",\n          \"operation\": \"Update\",\n          \"fieldsV1\": {\n            \"f:firstTimestamp\": {},\n            \"f:involvedObject\": {},\n            \"f:reason\": {},\n            \"f:count\": {},\n            \"f:lastTimestamp\": {},\n            \"f:type\": {},\n            \"f:message\": {},\n            \"f:source\": {\n              \"f:component\": {}\n            }\n          },\n          \"manager\": \"kube-controller-manager\",\n          \"time\": \"2022-06-01T14:05:33Z\",\n          \"fieldsType\": \"FieldsV1\"\n        }\n      ]\n    },\n    \"apiVersion\": \"v1\",\n    \"kind\": \"Event\",\n    \"message\": \"Failed to update endpoint kube-system/kube-dns: Operation cannot be fulfilled on endpoints \\\"kube-dns\\\": the object has been modified; please apply your changes to the latest version and try again\",\n    \"source\": {\n      \"component\": \"endpoint-controller\"\n    },\n    \"involvedObject\": {\n      \"apiVersion\": \"v1\",\n      \"uid\": \"75cc3b54-2a5f-42fa-8dd9-1669695113cd\",\n      \"kind\": \"Endpoints\",\n      \"namespace\": \"kube-system\",\n      \"resourceVersion\": \"7416\",\n      \"name\": \"kube-dns\"\n    },\n    \"reason\": \"FailedToUpdateEndpoint\"\n  },\n  \"resource\": {\n    \"type\": \"k8s_cluster\",\n    \"labels\": {\n      \"cluster_name\": \"cluster-1\",\n      \"location\": \"europe-west1-c\",\n      \"project_id\": \"hazel-aria-348413\"\n    }\n  },\n  \"timestamp\": \"2022-06-01T14:05:33Z\",\n  \"severity\": \"WARNING\",\n  \"logName\": \"projects/hazel-aria-348413/logs/events\",\n  \"receiveTimestamp\": \"2022-06-01T14:05:39.683992581Z\"\n}",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ],
            "reason": "Failed to update endpoint kube-system/kube-dns: Operation cannot be fulfilled on endpoints \"kube-dns\": the object has been modified; please apply your changes to the latest version and try again",
            "action": "FailedToUpdateEndpoint"
        },
        "@timestamp": "2022-06-01T14:05:33Z",
        "orchestrator": {
            "type": "kubernetes",
            "api_version": "v1",
            "namespace": "kube-system",
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "type": "k8s_cluster"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "17ahw8eg29q74yc",
            "logName": "projects/hazel-aria-348413/logs/events",
            "receiveTimestamp": "2022-06-01T14:05:39.683992581Z",
            "severity": "WARNING",
            "jsonPayload": {
                "apiVersion": "v1",
                "kind": "Event",
                "type": "Warning",
                "involvedObject": {
                    "kind": "Endpoints",
                    "name": "kube-dns",
                    "resourceVersion": "7416",
                    "uid": "75cc3b54-2a5f-42fa-8dd9-1669695113cd"
                },
                "metadata": {
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
                    ],
                    "resourceVersion": "960",
                    "uid": "828b8cd3-1eec-4093-95fb-907ebeab0efa"
                },
                "source": {
                    "component": "endpoint-controller"
                }
            }
        },
        "host": {
            "name": "kube-dns.16f484369d214dae"
        },
        "server": {
            "geo": {
                "name": "europe-west1-c"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```


=== "gke_log_id_event3.json"

    ```json
	
    {
        "message": "{\n  \"insertId\": \"17ahw8eg29q74yb\",\n  \"jsonPayload\": {\n    \"involvedObject\": {\n      \"namespace\": \"kube-system\",\n      \"uid\": \"52017f74-5157-4788-a62e-b83c4eac4acf\",\n      \"kind\": \"Pod\",\n      \"resourceVersion\": \"6551\",\n      \"fieldPath\": \"spec.containers{prometheus-to-sd}\",\n      \"apiVersion\": \"v1\",\n      \"name\": \"kube-dns-56494768b7-544n6\"\n    },\n    \"kind\": \"Event\",\n    \"apiVersion\": \"v1\",\n    \"eventTime\": null,\n    \"reportingInstance\": \"\",\n    \"metadata\": {\n      \"managedFields\": [\n        {\n          \"time\": \"2022-06-01T14:05:32Z\",\n          \"manager\": \"kubelet\",\n          \"fieldsType\": \"FieldsV1\",\n          \"operation\": \"Update\",\n          \"apiVersion\": \"v1\",\n          \"fieldsV1\": {\n            \"f:count\": {},\n            \"f:type\": {},\n            \"f:involvedObject\": {},\n            \"f:source\": {\n              \"f:component\": {},\n              \"f:host\": {}\n            },\n            \"f:reason\": {},\n            \"f:firstTimestamp\": {},\n            \"f:message\": {},\n            \"f:lastTimestamp\": {}\n          }\n        }\n      ],\n      \"namespace\": \"kube-system\",\n      \"creationTimestamp\": \"2022-06-01T14:05:32Z\",\n      \"name\": \"kube-dns-56494768b7-544n6.16f48436899e3f4a\",\n      \"resourceVersion\": \"959\",\n      \"uid\": \"2836bb34-8703-4475-a7d8-5cf0ec2232f8\"\n    },\n    \"message\": \"Created container prometheus-to-sd\",\n    \"reason\": \"Created\",\n    \"type\": \"Normal\",\n    \"source\": {\n      \"host\": \"gke-cluster-1-default-pool-476246ab-wnl7\",\n      \"component\": \"kubelet\"\n    },\n    \"reportingComponent\": \"\"\n  },\n  \"resource\": {\n    \"type\": \"k8s_pod\",\n    \"labels\": {\n      \"project_id\": \"hazel-aria-348413\",\n      \"namespace_name\": \"kube-system\",\n      \"cluster_name\": \"cluster-1\",\n      \"pod_name\": \"kube-dns-56494768b7-544n6\",\n      \"location\": \"europe-west1-c\"\n    }\n  },\n  \"timestamp\": \"2022-06-01T14:05:32Z\",\n  \"severity\": \"INFO\",\n  \"logName\": \"projects/hazel-aria-348413/logs/events\",\n  \"receiveTimestamp\": \"2022-06-01T14:05:39.683992581Z\"\n}",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ],
            "reason": "Created container prometheus-to-sd",
            "action": "Created"
        },
        "@timestamp": "2022-06-01T14:05:32Z",
        "orchestrator": {
            "type": "kubernetes",
            "api_version": "v1",
            "namespace": "kube-system",
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "name": "kube-dns-56494768b7-544n6",
                "type": "k8s_pod"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "17ahw8eg29q74yb",
            "logName": "projects/hazel-aria-348413/logs/events",
            "receiveTimestamp": "2022-06-01T14:05:39.683992581Z",
            "severity": "INFO",
            "jsonPayload": {
                "apiVersion": "v1",
                "kind": "Event",
                "type": "Normal",
                "involvedObject": {
                    "fieldPath": "spec.containers{prometheus-to-sd}",
                    "kind": "Pod",
                    "name": "kube-dns-56494768b7-544n6",
                    "resourceVersion": "6551",
                    "uid": "52017f74-5157-4788-a62e-b83c4eac4acf"
                },
                "metadata": {
                    "creationTimestamp": "2022-06-01T14:05:32Z",
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
                    "resourceVersion": "959",
                    "uid": "2836bb34-8703-4475-a7d8-5cf0ec2232f8"
                },
                "source": {
                    "component": "kubelet"
                }
            }
        },
        "host": {
            "name": "gke-cluster-1-default-pool-476246ab-wnl7"
        },
        "server": {
            "geo": {
                "name": "europe-west1-c"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```


=== "k8s_node.json"

    ```json
	
    {
        "message": "{\"insertId\":\"32ez47f5wz17i\",\"jsonPayload\":{\"apiVersion\":\"v1\",\"eventTime\":null,\"involvedObject\":{\"kind\":\"Node\",\"name\":\"gke-cluster-1-default-pool-eb66079e-k3zf\",\"uid\":\"gke-cluster-1-default-pool-eb66079e-k3zf\"},\"kind\":\"Event\",\"message\":\"{\\\"unmanaged\\\": {\\\"net.netfilter.nf_conntrack_buckets\\\": \\\"32768\\\"}}\",\"metadata\":{\"creationTimestamp\":\"2022-06-15T01:55:51Z\",\"managedFields\":[{\"apiVersion\":\"v1\",\"fieldsType\":\"FieldsV1\",\"fieldsV1\":{\"f:count\":{},\"f:firstTimestamp\":{},\"f:involvedObject\":{},\"f:lastTimestamp\":{},\"f:message\":{},\"f:reason\":{},\"f:source\":{\"f:component\":{},\"f:host\":{}},\"f:type\":{}},\"manager\":\"node-problem-detector\",\"operation\":\"Update\",\"time\":\"2022-06-15T01:55:51Z\"}],\"name\":\"gke-cluster-1-default-pool-eb66079e-k3zf.16f8813a8514b8c0\",\"namespace\":\"default\",\"resourceVersion\":\"894\",\"uid\":\"7e26b736-331a-4896-961f-96688918ba7e\"},\"reason\":\"NodeSysctlChange\",\"reportingComponent\":\"\",\"reportingInstance\":\"\",\"source\":{\"component\":\"sysctl-monitor\",\"host\":\"gke-cluster-1-default-pool-eb66079e-k3zf\"},\"type\":\"Warning\"},\"logName\":\"projects/hazel-aria-348413/logs/events\",\"receiveTimestamp\":\"2022-06-15T01:55:52.012275121Z\",\"resource\":{\"labels\":{\"cluster_name\":\"cluster-1\",\"location\":\"europe-central2-a\",\"node_name\":\"gke-cluster-1-default-pool-eb66079e-k3zf\",\"project_id\":\"hazel-aria-348413\"},\"type\":\"k8s_node\"},\"severity\":\"WARNING\",\"timestamp\":\"2022-06-15T01:55:51Z\"}",
        "event": {
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ],
            "reason": "{\"unmanaged\": {\"net.netfilter.nf_conntrack_buckets\": \"32768\"}}",
            "action": "NodeSysctlChange"
        },
        "@timestamp": "2022-06-15T01:55:51Z",
        "orchestrator": {
            "type": "kubernetes",
            "namespace": "default",
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "type": "k8s_node"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "32ez47f5wz17i",
            "logName": "projects/hazel-aria-348413/logs/events",
            "receiveTimestamp": "2022-06-15T01:55:52.012275121Z",
            "severity": "WARNING",
            "jsonPayload": {
                "apiVersion": "v1",
                "kind": "Event",
                "type": "Warning",
                "involvedObject": {
                    "kind": "Node",
                    "name": "gke-cluster-1-default-pool-eb66079e-k3zf",
                    "uid": "gke-cluster-1-default-pool-eb66079e-k3zf"
                },
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
                    "resourceVersion": "894",
                    "uid": "7e26b736-331a-4896-961f-96688918ba7e"
                },
                "source": {
                    "component": "sysctl-monitor"
                }
            }
        },
        "host": {
            "name": "gke-cluster-1-default-pool-eb66079e-k3zf"
        },
        "server": {
            "geo": {
                "name": "europe-central2-a"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```


=== "k8s_textPayload.json"

    ```json
	
    {
        "message": "{\"insertId\":\"1wtrhknf2gg14w\",\"logName\":\"projects/hazel-aria-348413/logs/events\",\"receiveTimestamp\":\"2022-06-16T09:42:59.259491841Z\",\"resource\":{\"labels\":{\"cluster_name\":\"cluster-1\",\"location\":\"europe-central2-a\",\"project_id\":\"hazel-aria-348413\"},\"type\":\"k8s_cluster\"},\"severity\":\"WARNING\",\"textPayload\":\"Event exporter started watching. Some events may have been lost up to this point.\",\"timestamp\":\"2022-06-16T09:42:39.200653463Z\"}",
        "event": {
            "reason": "Event exporter started watching. Some events may have been lost up to this point.",
            "kind": "event",
            "category": [
                "process"
            ],
            "type": [
                "change"
            ]
        },
        "@timestamp": "2022-06-16T09:42:39.200653Z",
        "orchestrator": {
            "type": "kubernetes",
            "cluster": {
                "name": "cluster-1"
            }
        },
        "google_kubernetes_engine": {
            "insertId": "1wtrhknf2gg14w",
            "logName": "projects/hazel-aria-348413/logs/events",
            "receiveTimestamp": "2022-06-16T09:42:59.259491841Z",
            "severity": "WARNING"
        },
        "server": {
            "geo": {
                "name": "europe-central2-a"
            }
        },
        "cloud": {
            "project": {
                "id": "hazel-aria-348413"
            }
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloud.project.id` | `keyword` | The cloud project id. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`google_kubernetes_engine.insertId` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.MESSAGE` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.SYSLOG_IDENTIFIER` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._BOOT_ID` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._CAP_EFFECTIVE` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._COMM` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._GID` | `number` |  |
|`google_kubernetes_engine.jsonPayload._STREAM_ID` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_CGROUP` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_INVOCATION_ID` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_SLICE` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_UNIT` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._TRANSPORT` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload._UID` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.apiVersion` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.eventTime` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.involvedObject.fieldPath` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.involvedObject.kind` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.involvedObject.name` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.involvedObject.resourceVersion` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.involvedObject.uid` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.kind` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.metadata.creationTimestamp` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.metadata.managedFields` | `array` |  |
|`google_kubernetes_engine.jsonPayload.metadata.resourceVersion` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.metadata.uid` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.reportingComponent` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.reportingInstance` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.source.component` | `keyword` |  |
|`google_kubernetes_engine.jsonPayload.type` | `keyword` |  |
|`google_kubernetes_engine.labels.authorization.k8s.io.decision` | `keyword` |  |
|`google_kubernetes_engine.logName` | `keyword` |  |
|`google_kubernetes_engine.receiveTimestamp` | `keyword` |  |
|`google_kubernetes_engine.severity` | `keyword` |  |
|`host.id` | `keyword` | Unique host id. |
|`host.name` | `keyword` | Name of the host. |
|`log.syslog.facility.code` | `long` | Syslog numeric facility of the event. |
|`log.syslog.priority` | `long` | Syslog priority of the event. |
|`orchestrator.api_version` | `keyword` | API version being used to carry out the action |
|`orchestrator.cluster.name` | `keyword` | Name of the cluster. |
|`orchestrator.namespace` | `keyword` | Namespace in which the action is taking place. |
|`orchestrator.resource.name` | `keyword` | Name of the resource being acted upon. |
|`orchestrator.resource.type` | `keyword` | Type of resource being acted upon. |
|`orchestrator.type` | `keyword` | Orchestrator cluster type (e.g. kubernetes, nomad or cloudfoundry). |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.pid` | `long` | Process id. |
|`server.geo.name` | `keyword` | User-defined description of a location. |

