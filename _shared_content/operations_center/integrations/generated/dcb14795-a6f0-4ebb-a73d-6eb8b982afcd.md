
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
| Type | `end`, `start` |




### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/docs/xdr/features/detect/rules_catalog) and hunting activities in the [events page](/docs/xdr/features/investigate/events). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/docs/xdr/features/detect/sigma) and to leverage the full potential of the collected data.

=== "connexion1.json"

    ```json
	
    {
        "message": "Connexion au portail web org:example, user:jdoe@local, ip:1.2.3.4",
        "event": {
            "category": "session",
            "outcome": "success",
            "reason": "Connexion au portail web",
            "type": "start"
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
            "category": "session",
            "outcome": "success",
            "reason": "Connexion d'un plugin utilisateur",
            "type": "start"
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


=== "deconnexion1.json"

    ```json
	
    {
        "message": "D\u00e9connexion du portail web org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": "session",
            "outcome": "success",
            "reason": "D\u00e9connexion du portail web",
            "type": "end"
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
            "category": "session",
            "outcome": "success",
            "reason": "D\u00e9connexion d'un plugin utilisateur",
            "type": "end"
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


=== "process1.json"

    ```json
	
    {
        "message": "Fermeture d'une application  RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT org:example, user:jdoe@EXAMPLE, ip:1.2.3.4",
        "event": {
            "category": "process",
            "outcome": "success",
            "reason": "Fermeture d'une application  RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT",
            "type": "end"
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
            "category": "process",
            "outcome": "success",
            "reason": "Lancement d'une application RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT",
            "type": "start"
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
            "category": "session",
            "outcome": "failure",
            "reason": "Echec de la connexion au portail web : erreur d'authentification d'un utilisateur",
            "type": "start"
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
|`source.ip` | `ip` | IP address of the source. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.name` | `keyword` | Short name or login of the user. |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Systancia/cleanroom).