
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


=== "gke_container_runtime.json"

    ```json
	
    {
        "@timestamp": "2022-06-01T13:50:44.190941Z",
        "google_kubernetes_engine": {
            "insertId": "rxi2u29itqwvaa18",
            "jsonPayload": {
                "MESSAGE": "time=\"2022-06-01T13:50:44.190869134Z\" level=info msg=\"ImageCreate event &ImageCreate{Name:gke.gcr.io/k8s-dns-sidecar:1.21.4-gke.0,Labels:map[string]string{io.cri-containerd.image: managed,},XXX_unrecognized:[],}\"",
                "SYSLOG_IDENTIFIER": "containerd",
                "_BOOT_ID": "e61a95dc40fd44f6ba5c6bfcb18b46a2",
                "_CAP_EFFECTIVE": "1ffffffffff",
                "_COMM": "containerd",
                "_STREAM_ID": "949cd6779ed34897a1b74883881ddfe8",
                "_SYSTEMD_CGROUP": "/system.slice/containerd.service",
                "_SYSTEMD_INVOCATION_ID": "ebd8a874b9bf4797a358a0403ec7e1e7",
                "_SYSTEMD_SLICE": "system.slice",
                "_SYSTEMD_UNIT": "containerd.service",
                "_TRANSPORT": "stdout",
                "_UID": "0"
            },
            "logName": "projects/hazel-aria-348413/logs/container-runtime",
            "receiveTimestamp": "2022-06-01T13:50:46.223587016Z",
            "resource": {
                "labels": {
                    "node_name": "gke-cluster-1-default-pool-476246ab-wnl7"
                }
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
        "file": {
            "gid": "0"
        },
        "host": {
            "name": "gke-cluster-1-default-pool-476246ab-wnl7",
            "id": "3fa273bf9f602a2286f55eac7ffa6d36"
        },
        "orchestrator": {
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "type": "k8s_node"
            }
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


=== "gke_container_runtime2.json"

    ```json
	
    {
        "@timestamp": "2022-06-01T14:01:35.371492Z",
        "google_kubernetes_engine": {
            "insertId": "mf28fmdkt05bbyjk",
            "jsonPayload": {
                "MESSAGE": "time=\"2022-06-01T14:01:35.371006269Z\" level=info msg=\"StopContainer for \\\"4c2b21624d4488ea8305bec91bb58135e840ab50b779da3db19ddf87864a760e\\\" with timeout 30 (s)\"",
                "SYSLOG_IDENTIFIER": "containerd",
                "_BOOT_ID": "e61a95dc40fd44f6ba5c6bfcb18b46a2",
                "_CAP_EFFECTIVE": "1ffffffffff",
                "_COMM": "containerd",
                "_STREAM_ID": "949cd6779ed34897a1b74883881ddfe8",
                "_SYSTEMD_CGROUP": "/system.slice/containerd.service",
                "_SYSTEMD_INVOCATION_ID": "ebd8a874b9bf4797a358a0403ec7e1e7",
                "_SYSTEMD_SLICE": "system.slice",
                "_SYSTEMD_UNIT": "containerd.service",
                "_TRANSPORT": "stdout",
                "_UID": "0"
            },
            "logName": "projects/hazel-aria-348413/logs/container-runtime",
            "receiveTimestamp": "2022-06-01T14:01:36.219094561Z",
            "resource": {
                "labels": {
                    "node_name": "gke-cluster-1-default-pool-476246ab-wnl7"
                }
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
        "file": {
            "gid": "0"
        },
        "host": {
            "name": "gke-cluster-1-default-pool-476246ab-wnl7",
            "id": "3fa273bf9f602a2286f55eac7ffa6d36"
        },
        "orchestrator": {
            "cluster": {
                "name": "cluster-1"
            },
            "resource": {
                "type": "k8s_node"
            }
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





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`cloud.project.id` | `keyword` | The cloud project id. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`file.gid` | `keyword` | Primary group ID (GID) of the file. |
|`google_kubernetes_engine.insertId` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.MESSAGE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload.SYSLOG_IDENTIFIER` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._BOOT_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._CAP_EFFECTIVE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._COMM` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._STREAM_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_CGROUP` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_INVOCATION_ID` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_SLICE` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._SYSTEMD_UNIT` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._TRANSPORT` | `keyword` | None |
|`google_kubernetes_engine.jsonPayload._UID` | `keyword` | None |
|`google_kubernetes_engine.logName` | `keyword` | None |
|`google_kubernetes_engine.receiveTimestamp` | `keyword` | None |
|`google_kubernetes_engine.resource.labels.node_name` | `keyword` | None |
|`host.id` | `keyword` | Unique host id. |
|`host.name` | `keyword` | Name of the host. |
|`log.syslog.facility.code` | `long` | Syslog numeric facility of the event. |
|`log.syslog.priority` | `long` | Syslog priority of the event. |
|`orchestrator.cluster.name` | `keyword` | Name of the cluster. |
|`orchestrator.resource.type` | `keyword` | Type of resource being acted upon. |
|`process.command_line` | `wildcard` | Full command line that started the process. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`process.pid` | `long` | Process id. |
|`server.geo.name` | `keyword` | User-defined description of a location. |

