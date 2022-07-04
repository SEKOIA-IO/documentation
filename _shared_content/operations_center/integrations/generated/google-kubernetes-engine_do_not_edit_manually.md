
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

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "gke_container_runtime2.json"

    ```json
	
    {
        "event": {
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "reason": "StopContainer for \\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\" with timeout 30 (s)",
            "outcome": "success"
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
        "event": {
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "reason": "Pulling image \"gke.gcr.io/prometheus-to-sd:v0.11.3-gke.0\"",
            "outcome": "success",
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
        "event": {
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "reason": "Failed to update endpoint kube-system/kube-dns: Operation cannot be fulfilled on endpoints \"kube-dns\": the object has been modified; please apply your changes to the latest version and try again",
            "outcome": "success",
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
        "event": {
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "reason": "Created container prometheus-to-sd",
            "outcome": "success",
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
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z",
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
        "event": {
            "outcome": "success",
            "reason": "Event exporter started watching. Some events may have been lost up to this point.",
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ]
        },
        "@timestamp": "2022-06-16T09:42:39.200653463Z",
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
|`google_kubernetes_engine.insertId` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.MESSAGE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.SYSLOG_IDENTIFIER` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._BOOT_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._CAP_EFFECTIVE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._COMM` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._GID` | `number` | None |
|`google_kubernetes_engine.jsonPayload._STREAM_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_CGROUP` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_INVOCATION_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_SLICE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_UNIT` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._TRANSPORT` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._UID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.apiVersion` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.eventTime` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.involvedObject.fieldPath` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.involvedObject.kind` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.involvedObject.name` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.involvedObject.resourceVersion` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.involvedObject.uid` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.kind` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.metadata.creationTimestamp` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.metadata.managedFields` | `array` | None |
|`google_kubernetes_engine.jsonPayload.metadata.resourceVersion` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.metadata.uid` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.reportingComponent` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.reportingInstance` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.source.component` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.type` | `keyword` | None |
|`google_kubernetes_engine.labels.authorization.k8s.io.decision` | `keyword` | None |
|`google_kubernetes_engine.logName` | `keyword` | None |
|`google_kubernetes_engine.receiveTimestamp` | `keyword` | None |
|`google_kubernetes_engine.severity` | `keyword` | None |
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

