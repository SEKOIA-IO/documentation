
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `GCP audit logs` | Google Cloud Audit contains logs from multiple Google Cloud source such as Google Cloud Console and Google Workspace. |








## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "2sv_disable.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-24T05:06:02.686Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T05:06:03.845372592Z",
            "insertId": "-tn3jrd3lko",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.2svDisable",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi"
                                }
                            ],
                            "eventName": "2sv_disable",
                            "eventType": "2sv_change"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632459962686000",
                        "uniqQualifier": "-7789616625639281959"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.2svDisable",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "2sv_enroll.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "@timestamp": "2021-09-24T04:45:45.769Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T04:45:46.331843829Z",
            "insertId": "g3k8gid3b3p",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.2svEnroll",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "2sv_change",
                            "status": {
                                "success": true
                            },
                            "eventName": "2sv_enroll",
                            "parameter": [
                                {
                                    "value": "INfDlrzP9IH8_QE",
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "name": "dusi"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632458745769000",
                        "uniqQualifier": "1624031130844323135"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.2svEnroll",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "account_disabled_generic.json"

    ```json
	
    {
        "@timestamp": "2021-04-30T23:33:09.352Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T23:33:10.673412983Z",
            "insertId": "nlgrf8d6ygj",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.accountDisabledGeneric",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "account_disabled_generic",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619825589352000",
                        "uniqQualifier": "-3303614929287073633"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.accountDisabledGeneric",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "account_disabled_hijacked.json"

    ```json
	
    {
        "@timestamp": "2021-04-30T23:33:09.352Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T23:33:10.673412983Z",
            "insertId": "nlgrf8d6ygj",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.accountDisabledHijacked",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "account_disabled_hijacked",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619825589352000",
                        "uniqQualifier": "-3303614929287073633"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.accountDisabledHijacked",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "account_disabled_password_leak.json"

    ```json
	
    {
        "@timestamp": "2021-04-30T18:41:23.475Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T18:41:24.650965796Z",
            "insertId": "-xkklkzcxkl",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.accountDisabledPasswordLeak",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "account_disabled_password_leak",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619808083475000",
                        "uniqQualifier": "6286848759980589624"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.accountDisabledPasswordLeak",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "account_disabled_spamming.json"

    ```json
	
    {
        "@timestamp": "2021-04-30T18:41:23.475Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T18:41:24.650965796Z",
            "insertId": "-xkklkzcxkl",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.accountDisabledSpamming",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "account_disabled_spamming",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619808083475000",
                        "uniqQualifier": "6286848759980589624"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.accountDisabledSpamming",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "account_disabled_spamming_through_relay.json"

    ```json
	
    {
        "@timestamp": "2021-04-30T18:41:23.475Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T18:41:24.650965796Z",
            "insertId": "-xkklkzcxkl",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.accountDisabledSpammingThroughRelay",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "account_disabled_spamming_through_relay",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619808083475000",
                        "uniqQualifier": "6286848759980589624"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.accountDisabledSpammingThroughRelay",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "attack_warning.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z",
            "reason": "NodeSysctlChange"
        },
        "@timestamp": "2021-09-24T05:06:02.686Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T05:06:03.845372592Z",
            "insertId": "-tn3jrd3lko",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.2svDisable",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi"
                                }
                            ],
                            "eventName": "2sv_disable",
                            "eventType": "2sv_change"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632459962686000",
                        "uniqQualifier": "-7789616625639281959"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.2svDisable",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "email_forwarding_out_of_domain.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-24T16:32:32.256Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T16:32:33.319260836Z",
            "insertId": "rrcp9gd3y2f",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.emailForwardingOutOfDomain",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "email_forwarding_out_of_domain",
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "name": "dusi",
                                    "type": "TYPE_STRING",
                                    "value": "INfDlrzP9IH8_QE",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "test-user@google.com",
                                    "name": "email_forwarding_destination_address"
                                }
                            ],
                            "eventType": "email_forwarding_change"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632501152256000",
                        "uniqQualifier": "-5683698025624301037"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.emailForwardingOutOfDomain",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "gke_container_runtime.json"

    ```json
	
    {
        "event": {
            "kind": "event",
            "category": "process",
            "type": [
                "change"
            ],
            "reason": "ImageCreate event &ImageCreate{Name:gke.gcr.io/k8s-dns-sidecar:1.21.4-gke.0,Labels:map[string]string{io.cri-containerd.image: managed,},XXX_unrecognized:[],}",
            "outcome": "success"
        },
        "@timestamp": "2022-06-14T14:32:09.910723Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2022-06-14T14:32:10.838967694Z",
            "insertId": "2f93b0a6-f932-4d91-ad61-785ae9587360",
            "logName": "projects/hazel-aria-348413/logs/cloudaudit.googleapis.com%2Factivity",
            "resource": {
                "type": "k8s_cluster",
                "labels": {
                    "project_id": "hazel-aria-348413",
                    "cluster_name": "cluster-1",
                    "location": "europe-central2-a"
                }
            },
            "protoPayload": {
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "authorizationInfo": [
                    {
                        "granted": true,
                        "permission": "io.k8s.coordination.v1.leases.update",
                        "resource": "coordination.k8s.io/v1/namespaces/kube-system/leases/kube-scheduler"
                    }
                ],
                "methodName": "io.k8s.coordination.v1.leases.update",
                "resourceName": "coordination.k8s.io/v1/namespaces/kube-system/leases/kube-scheduler"
            },
            "operation": {
                "id": "2f93b0a6-f932-4d91-ad61-785ae9587360",
                "first": true,
                "last": true,
                "producer": "k8s.io"
            }
        },
        "user": {
            "name": "system:kube-scheduler"
        },
        "service": {
            "name": "k8s.io"
        },
        "source": {
            "ip": "10.186.0.146",
            "address": "10.186.0.146"
        },
        "user_agent": {
            "original": "kube-scheduler/v1.22.8 (linux/amd64) kubernetes/2dca91e/leader-election"
        },
        "related": {
            "ip": [
                "10.186.0.146"
            ],
            "user": [
                "system:kube-scheduler"
            ]
        }
    }
    	
	```


=== "gov_attack_warning.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z",
            "reason": "NodeSysctlChange"
        },
        "@timestamp": "2021-04-30T23:37:17.106Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-04-30T23:37:18.488559815Z",
            "insertId": "bxuophd1vlw",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.govAttackWarning",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "gov_attack_warning",
                            "eventType": "attack_warning",
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1619825837106000",
                        "uniqQualifier": "7230131091737932677"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.govAttackWarning",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "k8s_cluster.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2022-06-15T07:27:36.652663Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2022-06-15T07:27:38.524909478Z",
            "insertId": "9d92cd5d-5043-4c8d-9a3b-92c0be113704",
            "logName": "projects/hazel-aria-348413/logs/cloudaudit.googleapis.com%2Factivity",
            "resource": {
                "type": "k8s_cluster",
                "labels": {
                    "project_id": "hazel-aria-348413",
                    "cluster_name": "cluster-1",
                    "location": "europe-central2-a"
                }
            },
            "protoPayload": {
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "authorizationInfo": [
                    {
                        "granted": true,
                        "permission": "io.k8s.core.v1.configmaps.update",
                        "resource": "core/v1/namespaces/kube-system/configmaps/cluster-kubestore"
                    }
                ],
                "methodName": "io.k8s.core.v1.configmaps.update",
                "resourceName": "core/v1/namespaces/kube-system/configmaps/cluster-kubestore"
            },
            "operation": {
                "id": "9d92cd5d-5043-4c8d-9a3b-92c0be113704",
                "first": true,
                "last": true,
                "producer": "k8s.io"
            }
        },
        "user": {
            "name": "system:kubestore-collector"
        },
        "service": {
            "name": "k8s.io"
        },
        "source": {
            "ip": "10.186.0.146",
            "address": "10.186.0.146"
        },
        "user_agent": {
            "original": "kubestore_collector/v0.0.0 (linux/amd64) kubernetes/$Format"
        },
        "related": {
            "ip": [
                "10.186.0.146"
            ],
            "user": [
                "system:kubestore-collector"
            ]
        }
    }
    	
	```


=== "k8s_delete_cluster.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2022-06-15T16:19:47.720234784Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2022-06-15T16:19:48.068568099Z",
            "insertId": "ofj3qoe4mbih",
            "logName": "projects/hazel-aria-348413/logs/cloudaudit.googleapis.com%2Factivity",
            "severity": "NOTICE",
            "resource": {
                "type": "gke_cluster",
                "labels": {
                    "project_id": "hazel-aria-348413",
                    "cluster_name": "cluster-1",
                    "location": "europe-central2-a"
                }
            },
            "protoPayload": {
                "metadata": {
                    "operationType": "DELETE_CLUSTER"
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.container.v1.ClusterManager.DeleteCluster",
                "resourceName": "projects/hazel-aria-348413/zones/europe-central2-a/clusters/cluster-1",
                "resourceLocation": {
                    "currentLocations": [
                        "europe-central2-a"
                    ]
                }
            },
            "operation": {
                "id": "operation-1655309832996-a5fd6e18",
                "last": true,
                "producer": "container.googleapis.com"
            }
        },
        "service": {
            "name": "container.googleapis.com"
        }
    }
    	
	```


=== "login_challenge.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z",
            "reason": "NodeSysctlChange"
        },
        "@timestamp": "2021-09-24T16:16:57.183211Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T17:51:28.041126044Z",
            "insertId": "-nahbepd4l2j",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.loginChallenge",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "login_challenge",
                            "parameter": [
                                {
                                    "name": "login_type",
                                    "value": "google_password",
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_REPEATED",
                                    "name": "login_challenge_method",
                                    "multiStrValue": [
                                        "idv_preregistered_phone"
                                    ]
                                },
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING",
                                    "value": "incorrect_answer_entered",
                                    "name": "login_challenge_status"
                                },
                                {
                                    "type": "TYPE_STRING",
                                    "name": "dusi",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "IOWJlfPwgvrTfg"
                                }
                            ],
                            "eventType": "login"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632500217183211",
                        "uniqQualifier": "358068855354"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.loginChallenge",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "login_failure.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-24T16:16:57.183212Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T17:51:25.034361197Z",
            "insertId": "-nahbepd4l1x",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.loginFailure",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "login_failure",
                            "eventType": "login",
                            "parameter": [
                                {
                                    "value": "google_password",
                                    "type": "TYPE_STRING",
                                    "name": "login_type",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "name": "login_challenge_method",
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_REPEATED",
                                    "multiStrValue": [
                                        "password",
                                        "idv_preregistered_phone",
                                        "idv_preregistered_phone"
                                    ]
                                },
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "name": "dusi",
                                    "type": "TYPE_STRING",
                                    "value": "IOWJlfPwgvrTfg"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632500217183212",
                        "uniqQualifier": "358068855354"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.loginFailure",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "login_success.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "@timestamp": "2021-09-24T04:40:29.811809Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T05:43:20.474338130Z",
            "insertId": "ci1svzd3hfk",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.loginSuccess",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "value": "google_password",
                                    "name": "login_type",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "name": "login_challenge_method",
                                    "label": "LABEL_REPEATED",
                                    "type": "TYPE_STRING",
                                    "multiStrValue": [
                                        "password"
                                    ]
                                },
                                {
                                    "type": "TYPE_BOOL",
                                    "boolValue": false,
                                    "name": "is_suspicious",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi",
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL"
                                }
                            ],
                            "eventType": "login",
                            "eventName": "login_success"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632458429811809",
                        "uniqQualifier": "358068855354"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.loginSuccess",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "login_verification.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-24T05:05:36.762Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T06:39:22.386813664Z",
            "insertId": "ivb9z4d41rh",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.loginVerification",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "login_verification",
                            "parameter": [
                                {
                                    "name": "login_type",
                                    "type": "TYPE_STRING",
                                    "value": "google_password",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "name": "login_challenge_method",
                                    "multiStrValue": [
                                        "idv_preregistered_phone"
                                    ],
                                    "label": "LABEL_REPEATED",
                                    "type": "TYPE_STRING"
                                },
                                {
                                    "value": "passed",
                                    "name": "login_challenge_status",
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL"
                                },
                                {
                                    "value": "INfDlrzP9IH8_QE",
                                    "label": "LABEL_OPTIONAL",
                                    "name": "dusi",
                                    "type": "TYPE_STRING"
                                },
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "boolValue": true,
                                    "type": "TYPE_BOOL",
                                    "name": "is_second_factor"
                                }
                            ],
                            "eventType": "login"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632459936762000",
                        "uniqQualifier": "358068855354"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.loginVerification",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "logout.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "@timestamp": "2021-09-24T05:05:03.014598Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-24T06:39:22.229734504Z",
            "insertId": "v37ytid14th",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.logout",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "logout",
                            "eventType": "login",
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "name": "login_type",
                                    "value": "google_password"
                                },
                                {
                                    "type": "TYPE_STRING",
                                    "name": "dusi",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632459903014598",
                        "uniqQualifier": "358068855354"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.logout",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "password_edit.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "@timestamp": "2021-09-28T04:23:33.900566Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T04:23:37.724654918Z",
            "insertId": "-u8coc0d6n78",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.passwordEdit",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "password_edit",
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi"
                                }
                            ],
                            "eventType": "password_change"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632803013900566",
                        "uniqQualifier": "8894052787391296929"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.passwordEdit",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "recovery_email_edit.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-28T04:22:22.940979Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T04:22:26.523242112Z",
            "insertId": "-nkwfupd26zt",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.recoveryEmailEdit",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "recovery_info_change",
                            "eventName": "recovery_email_edit",
                            "parameter": [
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632802942940979",
                        "uniqQualifier": "-7373127890859496609"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.recoveryEmailEdit",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "recovery_phone_edit.json"

    ```json
	
    {
        "event": {
            "outcome": "success"
        },
        "@timestamp": "2021-09-28T04:47:19.611095Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T04:47:25.741574446Z",
            "insertId": "-1xtrgbd2vl2",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.recoveryPhoneEdit",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "status": {
                                "success": true
                            },
                            "eventType": "recovery_info_change",
                            "eventName": "recovery_phone_edit",
                            "parameter": [
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "type": "TYPE_STRING",
                                    "name": "dusi"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632804439611095",
                        "uniqQualifier": "1470137036135837564"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.recoveryPhoneEdit",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "recovery_secret_qa_edit.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-28T04:47:35.273424Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T04:47:37.650432219Z",
            "insertId": "vn31slcpmy",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.recoverySecretQaEdit",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "recovery_secret_qa_edit",
                            "eventType": "recovery_info_change",
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi",
                                    "label": "LABEL_OPTIONAL"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632804455273424",
                        "uniqQualifier": "8328506129139272243"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.recoverySecretQaEdit",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "suspicious_login.json"

    ```json
	
    {
        "@timestamp": "2021-05-04T02:26:21Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-05-04T02:56:23.806722355Z",
            "insertId": "-778d70d2n5b",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.suspiciousLogin",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "suspicious_login",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1620095181000000",
                        "uniqQualifier": "-2034771694824799453"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.suspiciousLogin",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "suspicious_login_less_secure_app.json"

    ```json
	
    {
        "@timestamp": "2021-05-04T02:26:21Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-05-04T02:56:23.806722355Z",
            "insertId": "-778d70d2n5b",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.suspiciousLoginLessSecureApp",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "suspicious_login_less_secure_app",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1620095181000000",
                        "uniqQualifier": "-2034771694824799453"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.suspiciousLoginLessSecureApp",
                "resourceName": "organizations/123"
            }
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "user": {
            "email": "test-user@example.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "suspicious_programmatic_login.json"

    ```json
	
    {
        "@timestamp": "2021-05-04T02:26:21Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-05-04T02:56:23.806722355Z",
            "insertId": "-778d70d2n5b",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.suspiciousProgrammaticLogin",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "account_warning",
                            "eventName": "suspicious_programmatic_login",
                            "parameter": [
                                {
                                    "name": "affected_email_address",
                                    "value": "test-user@example.com",
                                    "label": "LABEL_OPTIONAL",
                                    "type": "TYPE_STRING"
                                }
                            ],
                            "status": {
                                "success": true
                            }
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1620095181000000",
                        "uniqQualifier": "-2034771694824799453"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.suspiciousProgrammaticLogin",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
            "address": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "related": {
            "ip": [
                "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
            ]
        }
    }
    	
	```


=== "titanium_enroll.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z"
        },
        "@timestamp": "2021-09-28T15:38:04.846Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T15:38:05.969683854Z",
            "insertId": "-bxbn5bd167i",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.titaniumEnroll",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventName": "titanium_enroll",
                            "status": {
                                "success": true
                            },
                            "parameter": [
                                {
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "type": "TYPE_STRING",
                                    "name": "dusi"
                                }
                            ],
                            "eventType": "titanium_change"
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632843484846000",
                        "uniqQualifier": "4206430548119220064"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.titaniumEnroll",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```


=== "titanium_unenroll.json"

    ```json
	
    {
        "event": {
            "start": "2022-06-03T12:09:42.501046130Z",
            "kind": "event",
            "category": "network",
            "type": [
                "info"
            ],
            "outcome": "success",
            "end": "2022-06-03T12:09:42.768509812Z",
            "reason": "NodeSysctlChange"
        },
        "@timestamp": "2021-09-28T15:45:14.653434Z",
        "google_cloud_audit": {
            "receiveTimestamp": "2021-09-28T15:45:15.862755277Z",
            "insertId": "-vw60qad1861",
            "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
            "severity": "NOTICE",
            "resource": {
                "type": "audited_resource",
                "labels": {
                    "method": "google.login.LoginService.titaniumUnenroll",
                    "service": "login.googleapis.com"
                }
            },
            "protoPayload": {
                "metadata": {
                    "type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
                    "event": [
                        {
                            "eventType": "titanium_change",
                            "status": {
                                "success": true
                            },
                            "eventName": "titanium_unenroll",
                            "parameter": [
                                {
                                    "type": "TYPE_STRING",
                                    "label": "LABEL_OPTIONAL",
                                    "value": "INfDlrzP9IH8_QE",
                                    "name": "dusi"
                                }
                            ]
                        }
                    ],
                    "activityId": {
                        "timeUsec": "1632843914653434",
                        "uniqQualifier": "-6706492269209711994"
                    }
                },
                "type": "type.googleapis.com/google.cloud.audit.AuditLog",
                "methodName": "google.login.LoginService.titaniumUnenroll",
                "resourceName": "organizations/123"
            }
        },
        "user": {
            "email": "test-user@example.com",
            "name": "test-user@example.com"
        },
        "service": {
            "name": "login.googleapis.com"
        },
        "source": {
            "ip": "203.0.113.255",
            "address": "203.0.113.255"
        },
        "related": {
            "ip": [
                "203.0.113.255"
            ],
            "user": [
                "test-user@example.com"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`google_cloud_audit.insertId` | `keyword` | None |
|`google_cloud_audit.logName` | `keyword` | None |
|`google_cloud_audit.operation.first` | `bool` | None |
|`google_cloud_audit.operation.id` | `keyword` | None |
|`google_cloud_audit.operation.last` | `bool` | None |
|`google_cloud_audit.operation.producer` | `keyword` | None |
|`google_cloud_audit.protoPayload.authorizationInfo` | `object` | None |
|`google_cloud_audit.protoPayload.metadata.activityId.timeUsec` | `keyword` | None |
|`google_cloud_audit.protoPayload.metadata.activityId.uniqQualifier` | `keyword` | None |
|`google_cloud_audit.protoPayload.metadata.event` | `object` | None |
|`google_cloud_audit.protoPayload.metadata.operationType` | `keyword` | None |
|`google_cloud_audit.protoPayload.metadata.type` | `keyword` | None |
|`google_cloud_audit.protoPayload.methodName` | `keyword` | None |
|`google_cloud_audit.protoPayload.request.policy.bindings` | `keyword` | None |
|`google_cloud_audit.protoPayload.request.policy.etag` | `keyword` | None |
|`google_cloud_audit.protoPayload.request.resource` | `keyword` | None |
|`google_cloud_audit.protoPayload.request.type` | `keyword` | None |
|`google_cloud_audit.protoPayload.requestMetadata.requestAttributes.time` | `keyword` | None |
|`google_cloud_audit.protoPayload.resourceLocation.currentLocations` | `keyword` | None |
|`google_cloud_audit.protoPayload.resourceName` | `keyword` | None |
|`google_cloud_audit.protoPayload.response.bindings` | `keyword` | None |
|`google_cloud_audit.protoPayload.response.etag` | `keyword` | None |
|`google_cloud_audit.protoPayload.response.type` | `keyword` | None |
|`google_cloud_audit.protoPayload.type` | `keyword` | None |
|`google_cloud_audit.receiveTimestamp` | `keyword` | None |
|`google_cloud_audit.resource.labels.cluster_name` | `keyword` | None |
|`google_cloud_audit.resource.labels.location` | `keyword` | None |
|`google_cloud_audit.resource.labels.method` | `keyword` | None |
|`google_cloud_audit.resource.labels.node_name` | `keyword` | None |
|`google_cloud_audit.resource.labels.project_id` | `keyword` | None |
|`google_cloud_audit.resource.labels.service` | `keyword` | None |
|`google_cloud_audit.resource.labels.topic_id` | `keyword` | None |
|`google_cloud_audit.resource.type` | `keyword` | None |
|`google_cloud_audit.severity` | `keyword` | None |
|`orchestrator.type` | `keyword` | Orchestrator cluster type (e.g. kubernetes, nomad or cloudfoundry). |
|`service.name` | `keyword` | Name of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`user.email` | `keyword` | User email address. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user_agent.original` | `keyword` | Unparsed user_agent string. |

