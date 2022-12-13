
## Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | PROVE IT traces the authentications on your services |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `event` |
| Category | `authentication` |
| Type | `end`, `start` |




## Event Samples

Find below few samples of events and how they are normalized by SEKOIA.IO.


=== "admin_services_service_modify.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"ADMIN\", \"modificationDiff\": \"\", \"serviceName\": \"MY-SERVICE\", \"serviceType\": \"https\", \"severity\": \"WARNING\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"172.17.0.30\", \"osInfo\": \"Windows(10)\", \"profiles\": [\"ADMINISTRATOR\"], \"protocol\": \"WEB\", \"realmName\": \"my-realm.local\", \"roles\": [\"PROVEIT-ADMINISTRATOR-PROFILE\"], \"sessionId\": \"6c036039-2ea0-4a12-bf54-98c827db986b\", \"softwareInfo\": \"Firefox (107.0)\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-08T21:37:18.323112+01:00\", \"type\": \"ADMIN_SERVICES_SERVICE_MODIFY\"}\n\n",
        "event": {
            "kind": "event",
            "action": "admin_services_service_modify",
            "severity": 30
        },
        "@timestamp": "2022-12-08T20:37:18.323112Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "PROVEIT-ADMINISTRATOR-PROFILE"
                    ],
                    "profiles": [
                        "ADMINISTRATOR"
                    ]
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "172.17.0.30",
            "address": "172.17.0.30"
        },
        "network": {
            "protocol": "web"
        },
        "related": {
            "user": [
                "my.user"
            ],
            "ip": [
                "172.17.0.30"
            ]
        }
    }
    	
	```


=== "system_simm_unlocked.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"SYSTEM\", \"severity\": \"INFO\", \"source\": {\"componentId\": \"coremanager\", \"type\": \"SYSTEM\"}, \"timestamp\": \"2022-12-13T06:25:56.859488+01:00\", \"type\": \"SYSTEM_SIMM_UNLOCKED\"}\n\n",
        "event": {
            "kind": "event",
            "action": "system_simm_unlocked",
            "severity": 10
        },
        "@timestamp": "2022-12-13T05:25:56.859488Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "SYSTEM",
                    "componentId": "coremanager"
                }
            }
        }
    }
    	
	```


=== "system_storage_stats.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"auditRecordsNumber\": 202, \"category\": \"SYSTEM\", \"severity\": \"INFO\", \"source\": {\"componentId\": \"coremanager\", \"type\": \"SYSTEM\"}, \"storageCurrentSpace\": 3336175616, \"storageFreeSpace\": 66275975168, \"storageId\": 1, \"storageName\": \"d\\\\u00e9faut\", \"storageTotalSpace\": 73386811392, \"timestamp\": \"2022-12-12T21:27:04.063158+01:00\", \"type\": \"SYSTEM_STORAGE_STATS\"}",
        "event": {
            "kind": "event",
            "action": "system_storage_stats",
            "severity": 10
        },
        "@timestamp": "2022-12-12T20:27:04.063158Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "SYSTEM",
                    "componentId": "coremanager"
                }
            }
        }
    }
    	
	```


=== "user_connection_failure.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"authServerName\": \"AD\", \"authServerType\": \"LDAP\", \"category\": \"USER\", \"reason\": \"BAD_CREDENTIALS\", \"severity\": \"WARNING\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.8\", \"osInfo\": \"Windows(10)\", \"profiles\": [\"USER\"], \"protocol\": \"web\", \"realmName\": \"my-realm.local\", \"roles\": [], \"sessionId\": \"\", \"softwareInfo\": \"Firefox (107.0)\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-09T10:38:55.552544+01:00\", \"type\": \"USER_CONNECTION_FAILURE\"}\n\n",
        "event": {
            "kind": "event",
            "action": "user_connection_failure",
            "reason": "BAD_CREDENTIALS",
            "severity": 30,
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "@timestamp": "2022-12-09T09:38:55.552544Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [],
                    "profiles": [
                        "USER"
                    ]
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.8",
            "address": "10.1.2.8"
        },
        "network": {
            "protocol": "web"
        },
        "related": {
            "user": [
                "my.user"
            ],
            "ip": [
                "10.1.2.8"
            ]
        }
    }
    	
	```


=== "user_connection_success.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.5\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - RESTREINT\"], \"sessionId\": \"20ed63ad-cd6d-4bfa-9251-09cdb3a2133e\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-12T09:06:39.737567+01:00\", \"type\": \"USER_CONNECTION_SUCCESS\"}\n\n",
        "event": {
            "kind": "event",
            "action": "user_connection_success",
            "severity": 10,
            "category": [
                "authentication"
            ],
            "type": [
                "start"
            ]
        },
        "@timestamp": "2022-12-12T08:06:39.737567Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - RESTREINT"
                    ],
                    "profiles": [
                        "USER"
                    ]
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.5",
            "address": "10.1.2.5"
        },
        "network": {
            "protocol": "rdp"
        },
        "related": {
            "user": [
                "my.user"
            ],
            "ip": [
                "10.1.2.5"
            ]
        }
    }
    	
	```


=== "user_disconnection.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.5\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - RESTREINT\"], \"sessionId\": \"7b4b9364-fa4a-4507-8976-f75056a3a546\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-12T17:23:52.226809+01:00\", \"type\": \"USER_DISCONNECTION\"}\n\n",
        "event": {
            "kind": "event",
            "action": "user_disconnection",
            "severity": 10,
            "category": [
                "authentication"
            ],
            "type": [
                "end"
            ]
        },
        "@timestamp": "2022-12-12T16:23:52.226809Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - RESTREINT"
                    ],
                    "profiles": [
                        "USER"
                    ]
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.5",
            "address": "10.1.2.5"
        },
        "network": {
            "protocol": "rdp"
        },
        "related": {
            "user": [
                "my.user"
            ],
            "ip": [
                "10.1.2.5"
            ]
        }
    }
    	
	```


=== "user_disconnection_on_inactivity.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.7\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - ALL\"], \"sessionId\": \"e4cc4c66-e7cd-4c13-b626-200016b048c5\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.other.user\"}, \"timestamp\": \"2022-12-12T11:34:36.291768+01:00\", \"type\": \"USER_DISCONNECTION_ON_INACTIVITY\"}\n",
        "event": {
            "kind": "event",
            "action": "user_disconnection_on_inactivity",
            "severity": 10,
            "category": [
                "authentication"
            ],
            "type": [
                "end"
            ]
        },
        "@timestamp": "2022-12-12T10:34:36.291768Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - ALL"
                    ],
                    "profiles": [
                        "USER"
                    ]
                }
            }
        },
        "source": {
            "user": {
                "name": "my.other.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.7",
            "address": "10.1.2.7"
        },
        "network": {
            "protocol": "rdp"
        },
        "related": {
            "user": [
                "my.other.user"
            ],
            "ip": [
                "10.1.2.7"
            ]
        }
    }
    	
	```


=== "user_service_connection_failure.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"context\": {\"authMode\": \"PASSWORD\", \"authUserName\": \"adminisitrateur\"}, \"reason\": \"AUTH_ERROR\", \"service\": {\"groupName\": \"Prod-Serveurs\", \"host\": \"10.1.0.26\", \"name\": \"AD2\", \"port\": 3389, \"protocol\": \"rdp\"}, \"severity\": \"WARNING\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.5\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - RESTREINT\"], \"sessionId\": \"20ed63ad-cd6d-4bfa-9251-09cdb3a2133e\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-12T09:09:20.974448+01:00\", \"type\": \"USER_SERVICE_CONNECTION_FAILURE\"}\n",
        "event": {
            "kind": "event",
            "action": "user_service_connection_failure",
            "reason": "AUTH_ERROR",
            "severity": 30
        },
        "@timestamp": "2022-12-12T08:09:20.974448Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - RESTREINT"
                    ],
                    "profiles": [
                        "USER"
                    ]
                },
                "context": {
                    "auth_mode": "PASSWORD"
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.5",
            "address": "10.1.2.5"
        },
        "network": {
            "protocol": "rdp"
        },
        "service": {
            "name": "AD2",
            "address": "10.1.0.26"
        },
        "user": {
            "name": "adminisitrateur"
        },
        "related": {
            "user": [
                "adminisitrateur",
                "my.user"
            ],
            "ip": [
                "10.1.2.5"
            ]
        }
    }
    	
	```


=== "user_service_connection_summary.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"beginDate\": \"2022-12-11T18:27:27.581333+01:00\", \"category\": \"USER\", \"context\": {\"authMode\": \"PASSWORD\", \"authUserName\": \"administrateur\"}, \"duration\": 10, \"endDate\": \"2022-12-11T18:27:37.690038+01:00\", \"service\": {\"groupName\": \"Prod-Serveurs\", \"host\": \"serveur17\", \"name\": \"serveur17\", \"port\": 3389, \"protocol\": \"rdp\"}, \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"172.17.0.10\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - ALL\"], \"sessionId\": \"82a60aef-dbde-4a3b-8b21-df00712038e6\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.other.user\"}, \"status\": \"NETWORK_ERROR\", \"timestamp\": \"2022-12-11T18:27:37.725334+01:00\", \"type\": \"USER_SERVICE_CONNECTION_SUMMARY\"}\n\n",
        "event": {
            "kind": "event",
            "action": "user_service_connection_summary",
            "start": "2022-12-11T17:27:27.581333Z",
            "end": "2022-12-11T17:27:37.690038Z",
            "severity": 10
        },
        "@timestamp": "2022-12-11T17:27:37.725334Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - ALL"
                    ],
                    "profiles": [
                        "USER"
                    ]
                },
                "context": {
                    "auth_mode": "PASSWORD"
                }
            }
        },
        "source": {
            "user": {
                "name": "my.other.user",
                "domain": "my-realm.local"
            },
            "ip": "172.17.0.10",
            "address": "172.17.0.10"
        },
        "network": {
            "protocol": "rdp"
        },
        "service": {
            "name": "serveur17",
            "address": "serveur17"
        },
        "user": {
            "name": "administrateur"
        },
        "related": {
            "user": [
                "administrateur",
                "my.other.user"
            ],
            "ip": [
                "172.17.0.10"
            ]
        }
    }
    	
	```


=== "user_service_disconnection.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"context\": {\"authMode\": \"PASSWORD\", \"authUserName\": \"administrateur\"}, \"service\": {\"groupName\": \"Prod-Serveurs\", \"host\": \"10.1.0.26\", \"name\": \"AD2\", \"port\": 3389, \"protocol\": \"rdp\"}, \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.5\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - RESTREINT\"], \"sessionId\": \"7b4b9364-fa4a-4507-8976-f75056a3a546\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.user\"}, \"timestamp\": \"2022-12-12T16:58:58.072633+01:00\", \"type\": \"USER_SERVICE_DISCONNECTION\"}",
        "event": {
            "kind": "event",
            "action": "user_service_disconnection",
            "severity": 10
        },
        "@timestamp": "2022-12-12T15:58:58.072633Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - RESTREINT"
                    ],
                    "profiles": [
                        "USER"
                    ]
                },
                "context": {
                    "auth_mode": "PASSWORD"
                }
            }
        },
        "source": {
            "user": {
                "name": "my.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.5",
            "address": "10.1.2.5"
        },
        "network": {
            "protocol": "rdp"
        },
        "service": {
            "name": "AD2",
            "address": "10.1.0.26"
        },
        "user": {
            "name": "administrateur"
        },
        "related": {
            "user": [
                "administrateur",
                "my.user"
            ],
            "ip": [
                "10.1.2.5"
            ]
        }
    }
    	
	```


=== "user_service_disconnection_on_inactivity.json"

    ```json
	
    {
        "message": "\ufeff@cee: {\"category\": \"USER\", \"context\": {\"authMode\": \"PASSWORD\", \"authUserName\": \"my.other.user\"}, \"service\": {\"groupName\": \"Prod-Serveurs\", \"host\": \"serveur1.my-realm.local\", \"name\": \"titan\", \"port\": 3389, \"protocol\": \"rdp\"}, \"severity\": \"INFO\", \"source\": {\"authenticationMode\": \"PASSWORD\", \"ip\": \"10.1.2.7\", \"osInfo\": \"Unknown Unknown\", \"profiles\": [\"USER\"], \"protocol\": \"rdp\", \"realmName\": \"my-realm.local\", \"roles\": [\"DSI - ALL\"], \"sessionId\": \"e4cc4c66-e7cd-4c13-b626-200016b048c5\", \"softwareInfo\": \"\", \"type\": \"HB\", \"userName\": \"my.other.user\"}, \"timestamp\": \"2022-12-12T11:34:35.608171+01:00\", \"type\": \"USER_SERVICE_DISCONNECTION_ON_INACTIVITY\"}\n",
        "event": {
            "kind": "event",
            "action": "user_service_disconnection_on_inactivity",
            "severity": 10
        },
        "@timestamp": "2022-12-12T10:34:35.608171Z",
        "observer": {
            "vendor": "RubyCat",
            "product": "prove-it",
            "type": "bastion"
        },
        "rubycat": {
            "proveit": {
                "source": {
                    "type": "HB",
                    "roles": [
                        "DSI - ALL"
                    ],
                    "profiles": [
                        "USER"
                    ]
                },
                "context": {
                    "auth_mode": "PASSWORD"
                }
            }
        },
        "source": {
            "user": {
                "name": "my.other.user",
                "domain": "my-realm.local"
            },
            "ip": "10.1.2.7",
            "address": "10.1.2.7"
        },
        "network": {
            "protocol": "rdp"
        },
        "service": {
            "name": "titan",
            "address": "serveur1.my-realm.local"
        },
        "user": {
            "name": "my.other.user"
        },
        "related": {
            "user": [
                "my.other.user"
            ],
            "ip": [
                "10.1.2.7"
            ]
        }
    }
    	
	```





## Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`@timestamp` | `date` | Date/time when the event originated. |
|`event.action` | `keyword` | The action captured by the event. |
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.end` | `date` | event.end contains the date when the event ended or when the activity was last observed. |
|`event.kind` | `keyword` | The kind of the event. The highest categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.start` | `date` | event.start contains the date when the event started or when the activity was first observed. |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`network.protocol` | `keyword` | Application protocol name. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.type` | `keyword` | The type of the observer the data is coming from. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`rubycat.proveit.context.auth_mode` | `string` | Authentication mode on the service |
|`rubycat.proveit.source.componentId` | `string` | Source Component Identifier |
|`rubycat.proveit.source.profiles` | `array` | User profiles |
|`rubycat.proveit.source.roles` | `array` | User roles |
|`rubycat.proveit.source.type` | `string` | Type of the source |
|`service.address` | `keyword` | Address of this service. |
|`service.name` | `keyword` | Name of the service. |
|`source.ip` | `ip` | IP address of the source. |
|`source.user.domain` | `keyword` | Name of the directory the user is a member of. |
|`source.user.name` | `keyword` | Short name or login of the user. |
|`user.name` | `keyword` | Short name or login of the user. |

