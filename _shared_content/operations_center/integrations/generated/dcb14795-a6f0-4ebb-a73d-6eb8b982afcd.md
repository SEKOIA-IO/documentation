
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Authentication logs` | Privileged Access Management mechanism |





In details, the following table denotes the type of events produced by this integration.

| Name | Values |
| ---- | ------ |
| Kind | `` |
| Category | `process`, `session` |
| Type | `end`, `info`, `start` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "connexion1.json"

    ```json
	
    {
        "message": "Connexion au portail web org:example, user:jdoe@local, ip:1.2.3.4",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "Connexion au portail web",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "local",
            "name": "jdoe"
        }
    }
    	
	```


=== "connexion2.json"

    ```json
	
    {
        "message": "Connexion d'un plugin utilisateur org:example, user:jdoe@local, ip:1.2.3.4",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "Connexion d'un plugin utilisateur",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "local",
            "name": "jdoe"
        }
    }
    	
	```


=== "connexion3.json"

    ```json
	
    {
        "message": "Connexion au portail web org:example, user:toto@ORGANIZATION, ip:1.1.1.1",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "Connexion au portail web",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "toto"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "user": {
            "domain": "ORGANIZATION",
            "name": "toto"
        }
    }
    	
	```


=== "connexion4.json"

    ```json
	
    {
        "message": "Connexion d&#39;une passerelle org:example, user:@local, ip:1.1.1.1",
        "event": {
            "category": [
                "session"
            ],
            "reason": "Connexion d&#39;une passerelle",
            "type": [
                "info"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        }
    }
    	
	```


=== "deconnexion1.json"

    ```json
	
    {
        "message": "D\u00e9connexion du portail web org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "D\u00e9connexion du portail web",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "EXAMPLE",
            "name": "jdoe"
        }
    }
    	
	```


=== "deconnexion2.json"

    ```json
	
    {
        "message": "D\u00e9connexion d'un plugin utilisateur org:example, user:jdoe@local, ip:10.48.178.33",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "D\u00e9connexion d'un plugin utilisateur",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "10.48.178.33"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "10.48.178.33",
            "ip": "10.48.178.33"
        },
        "user": {
            "domain": "local",
            "name": "jdoe"
        }
    }
    	
	```


=== "deconnexion3.json"

    ```json
	
    {
        "message": "D\u00e9connexion du portail web org:example, user:toto@ORGANIZATION, ip:1.1.1.1",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "D\u00e9connexion du portail web",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "toto"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "user": {
            "domain": "ORGANIZATION",
            "name": "toto"
        }
    }
    	
	```


=== "deconnexion4.json"

    ```json
	
    {
        "message": "D&#233;connexion d&#39;une passerelle org:example, user:@local, ip:1.1.1.1",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "D&#233;connexion d&#39;une passerelle",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        }
    }
    	
	```


=== "echec1.json"

    ```json
	
    {
        "message": "Echec de la connexion &#224; la console d&#39;administration org:example, user:toto@example, ip:1.1.1.1 17b82585-3f88-4500-baf4-bb95ca7c3344",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "success",
            "reason": "Echec de la connexion &#224; la console d&#39;administration",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "toto"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "user": {
            "domain": "example",
            "name": "toto"
        }
    }
    	
	```


=== "fermeture1.json"

    ```json
	
    {
        "message": "Fermeture d'une application SSH (Secure Shell) : MultiTOTOAPP org:example, user:titi@ORGANIZATION, ip:1.1.1.1",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Fermeture d'une application SSH (Secure Shell) : MultiTOTOAPP",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "titi"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "user": {
            "domain": "ORGANIZATION",
            "name": "titi"
        }
    }
    	
	```


=== "lancement1.json"

    ```json
	
    {
        "message": "Lancement d'une application Web : MultiTOTOAPP org:example, user:toto@ORGANIZATION, ip:1.1.1.1",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Lancement d'une application Web : MultiTOTOAPP",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.1.1.1"
            ],
            "user": [
                "toto"
            ]
        },
        "source": {
            "address": "1.1.1.1",
            "ip": "1.1.1.1"
        },
        "user": {
            "domain": "ORGANIZATION",
            "name": "toto"
        }
    }
    	
	```


=== "process1.json"

    ```json
	
    {
        "message": "Fermeture d'une application  RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Fermeture d'une application  RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "EXAMPLE",
            "name": "jdoe"
        }
    }
    	
	```


=== "process2.json"

    ```json
	
    {
        "message": "Lancement d'une application RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Lancement d'une application RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "EXAMPLE",
            "name": "jdoe"
        }
    }
    	
	```


=== "session.json"

    ```json
	
    {
        "message": "Echec de la connexion au portail web : erreur d'authentification d'un utilisateur org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": [
                "session"
            ],
            "outcome": "failure",
            "reason": "Echec de la connexion au portail web : erreur d'authentification d'un utilisateur",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "organization": {
            "name": "example"
        },
        "related": {
            "ip": [
                "1.2.3.4"
            ],
            "user": [
                "jdoe"
            ]
        },
        "source": {
            "address": "1.2.3.4",
            "ip": "1.2.3.4"
        },
        "user": {
            "domain": "EXAMPLE",
            "name": "jdoe"
        }
    }
    	
	```


=== "user_first_new_process.json"

    ```json
	
    {
        "message": "johndoe@local New process: \"C:\\Windows\\System32\\RuntimeBroker.exe\"",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "New process: \"C:\\Windows\\System32\\RuntimeBroker.exe\"",
            "type": [
                "start"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "process": {
            "executable": "C:\\Windows\\System32\\RuntimeBroker.exe"
        },
        "related": {
            "user": [
                "johndoe"
            ]
        },
        "user": {
            "domain": "local",
            "name": "johndoe"
        }
    }
    	
	```


=== "user_first_other_1.json"

    ```json
	
    {
        "message": "john.doe@Azure SSO idle saved.",
        "event": {
            "category": [
                "session"
            ],
            "reason": "SSO idle saved.",
            "type": [
                "info"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "related": {
            "user": [
                "john.doe"
            ]
        },
        "user": {
            "domain": "Azure",
            "name": "john.doe"
        }
    }
    	
	```


=== "user_first_other_2.json"

    ```json
	
    {
        "message": "john.doe@Azure SSO Window closed: \"G:\\ - TreeSize Professional\"",
        "event": {
            "category": [
                "session"
            ],
            "reason": "SSO Window closed: \"G:\\ - TreeSize Professional\"",
            "type": [
                "info"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "related": {
            "user": [
                "john.doe"
            ]
        },
        "user": {
            "domain": "Azure",
            "name": "john.doe"
        }
    }
    	
	```


=== "user_first_other_3.json"

    ```json
	
    {
        "message": "john.doe@Azure SSO key sequence :\"<BACK<BACK\"",
        "event": {
            "category": [
                "session"
            ],
            "reason": "SSO key sequence :\"<BACK<BACK\"",
            "type": [
                "info"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "related": {
            "user": [
                "john.doe"
            ]
        },
        "user": {
            "domain": "Azure",
            "name": "john.doe"
        }
    }
    	
	```


=== "user_first_process_end_1.json"

    ```json
	
    {
        "message": "johndoe@local Process end: \"dllhost.exe\"",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Process end: \"dllhost.exe\"",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "process": {
            "executable": "dllhost.exe"
        },
        "related": {
            "user": [
                "johndoe"
            ]
        },
        "user": {
            "domain": "local",
            "name": "johndoe"
        }
    }
    	
	```


=== "user_first_process_end_2.json"

    ```json
	
    {
        "message": "johndoe@local Process end: \"backgroundTaskHost.exe\"",
        "event": {
            "category": [
                "process"
            ],
            "outcome": "success",
            "reason": "Process end: \"backgroundTaskHost.exe\"",
            "type": [
                "end"
            ]
        },
        "observer": {
            "product": "Systancia Cleanroom",
            "vendor": "Systancia"
        },
        "process": {
            "executable": "backgroundTaskHost.exe"
        },
        "related": {
            "user": [
                "johndoe"
            ]
        },
        "user": {
            "domain": "local",
            "name": "johndoe"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`event.category` | `keyword` | Event category. The second categorization field in the hierarchy. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`event.reason` | `keyword` | Reason why this event happened, according to the source |
|`event.type` | `keyword` | Event type. The third categorization field in the hierarchy. |
|`observer.product` | `keyword` | The product name of the observer. |
|`observer.vendor` | `keyword` | Vendor name of the observer. |
|`organization.name` | `keyword` | Organization name. |
|`process.executable` | `keyword` | Absolute path to the process executable. |
|`source.ip` | `ip` | IP address of the source. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Systancia/cleanroom).