
### Event Categories


The following table lists the data source offered by this integration.

| Data Source | Description                          |
| ----------- | ------------------------------------ |
| `Access tokens` | security identifiers are extracted from several events |
| `Authentication logs` | audit logon events are examined in detail |








### Transformed Events Samples after Ingestion

This section demonstrates how the raw logs will be transformed by our parsers. It shows the extracted fields that will be available for use in the [built-in detection rules](/xdr/features/detect/rules_catalog.md) and hunting activities in the [events page](/xdr/features/investigate/events.md). Understanding these transformations is essential for analysts to create effective detection mechanisms with [custom detection rules](/xdr/features/detect/sigma.md) and to leverage the full potential of the collected data.

=== "account_modification.json"

    ```json
	
    {
        "message": "Un compte d\u2019utilisateur a \u00e9t\u00e9 modifi\u00e9.#015#012#015#012Sujet :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-5-18#015#012#011Nom du compte :#011#011host.example.com$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d\u2019ouverture de session :#011#011User1#015#012#015#012Compte cible :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-5-21-241366212-796369622-1890169025-500#015#012#011Nom du compte :#011#011USERNAME#015#012#011Domaine du compte :#011#011host.example.com#015#012#015#012Attributs modifi\u00e9s :#015#012#011Nom du compte SAM :#011USERNAME#015#012#011Nom complet :#011#011<valeur non d\u00e9finie>#015#012#011Nom principal de l\u2019utilisateur :#011-#015#012#011R\u00e9pertoire de base :#011#011<valeur non d\u00e9finie>#015#012#011Lecteur de base :#011#011<valeur non d\u00e9finie>#015#012#011Chemin d\u2019acc\u00e8s au script :#011#011<valeur non d\u00e9finie>#015#012#011Chemin d\u2019acc\u00e8s au profil :#011#011<valeur non d\u00e9finie>#015#012#011Stations de travail utilisateurs :#011<valeur non d\u00e9finie>#015#012#011Derni\u00e8re modification du mot de passe le :#01110/06/2020 14:27:09#015#012#011Le compte expire le :#011#011<jamais>#015#012#011ID de groupe principal :#011513#015#012#011D\u00e9l\u00e9gu\u00e9 autoris\u00e9 :#011-#015#012#011Ancienne valeur UAC :#011#0110x210#015#012#011Nouvelle valeur UAC :#011#0110x210#015#012#011Contr\u00f4le du compte d\u2019utilisateur :#011-#015#012#011Param\u00e8tres utilisateur :#011-#015#012#011Historique SID :#011#011-#015#012#011Horaire d\u2019acc\u00e8s :#011#011Tout#015#012#015#012Informations suppl\u00e9mentaires :#015#012#011Privil\u00e8ges:#011#011-",
        "event": {
            "code": "4738",
            "outcome": "success"
        },
        "action": {
            "id": 4738,
            "name": "Un compte d\u2019utilisateur a \u00e9t\u00e9 modifi\u00e9.",
            "properties": {
                "domain": "host",
                "id": "S-1-5-21-241366212-796369622-1890169025-500",
                "name": "USERNAME",
                "type": "targetedUser"
            },
            "target": "user",
            "type": "Security"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "related": {
            "user": [
                "host.example.com$"
            ]
        },
        "user": {
            "target": {
                "domain": "host.example.com",
                "id": "User1",
                "name": "host.example.com$",
                "sid": "S-1-5-18"
            }
        }
    }
    	
	```


=== "exploit_protection.json"

    ```json
	
    {
        "message": "Process '\\Device\\HarddiskVolume2\\Windows\\System32\\svchost.exe' (PID 6904) would have been blocked from generating dynamic code.",
        "event": {
            "outcome": "success"
        },
        "action": {
            "name": "Process '\\Device\\HarddiskVolume2\\Windows\\System32\\svchost.exe' (PID 6904) would have been blocked from generating dynamic code.",
            "properties": {
                "type": "targetedUser"
            },
            "target": "user"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        }
    }
    	
	```


=== "logoff_mess.json"

    ```json
	
    {
        "message": "An account was logged off.#015#012#015#012Subject:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x523d454d#015#012#015#012Logon Type:#011#011#0115#015#012#015#012This event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.",
        "event": {
            "code": "4634",
            "outcome": "success"
        },
        "action": {
            "id": 4634,
            "name": "An account was logged off.",
            "properties": {
                "logon_type": 5,
                "type": "targetedUser"
            },
            "target": "user",
            "type": "Security"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "related": {
            "user": [
                "username"
            ]
        },
        "user": {
            "target": {
                "domain": "host.example.com",
                "id": "0x523d454d",
                "name": "username",
                "sid": "S-1-5-21-1494196517-2992400115-1379426628-1000"
            }
        }
    }
    	
	```


=== "logon_mess.json"

    ```json
	
    {
        "message": "An account was successfully logged on.#015#012#015#012Subject:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x1bc9bbee#015#012#015#012Logon Type:#011#011#0115#015#012#015#012New Logon:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x222c4f34#015#012#011Logon GUID:#011#011{00000000-0000-0000-0000-000000000000}#015#012#015#012Process Information:#015#012#011Process ID:#011#0110x5df8#015#012#011Process Name:#011#011C:\\ABSciex\\drm\\xGate.exe#015#012#015#012Network Information:#015#012#011Workstation Name:#011host.example.com#015#012#011Source Network Address:#011-#015#012#011Source Port:#011#011-#015#012#015#012Detailed Authentication Information:#015#012#011Logon Process:#011#011Advapi  #015#012#011Authentication Package:#011Negotiate#015#012#011Transited Services:#011-#015#012#011Package Name (NTLM only):#011-#015#012#011Key Length:#011#0110#015#012#015#012This event is generated when a logon session is created. It is generated on the computer that was accessed.#015#012#015#012The subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.#015#012#015#012The logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).#015#012#015#012The New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.#015#012#015#012The network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.#015#012#015#012The authentication information fields provide detailed information about this specific logon request.#015#012#011- Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.#015#012#011- Transited services indicate which intermediate services have participated in this logon request.#015#012#011- Package name indicates which sub-protocol was used among the NTLM protocols.#015#012#011- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.",
        "event": {
            "category": [
                "authentication"
            ],
            "code": "4624",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "action": {
            "id": 4624,
            "name": "An account was successfully logged on.",
            "outcome": "success",
            "properties": {
                "domain": "host.example.com",
                "id": "S-1-5-21-1494196517-2992400115-1379426628-1000",
                "logon_guid": "00000000-0000-0000-0000-000000000000",
                "logon_id": "0x222c4f34",
                "logon_type": 5,
                "name": "username",
                "type": "targetedUser"
            },
            "target": "user",
            "type": "Security"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "process": {
            "id": "0x5df8",
            "name": "C:\\ABSciex\\drm\\xGate.exe"
        },
        "related": {
            "user": [
                "username"
            ]
        },
        "sekoiaio": {
            "authentication": {
                "process": {
                    "name": "C:\\ABSciex\\drm\\xGate.exe"
                }
            },
            "server": {
                "os": {
                    "type": "windows"
                }
            }
        },
        "user": {
            "target": {
                "domain": "host.example.com",
                "id": "0x1bc9bbee",
                "name": "username",
                "sid": "S-1-5-21-1494196517-2992400115-1379426628-1000"
            }
        }
    }
    	
	```


=== "logon_mess_fr.json"

    ```json
	
    {
        "message": "L\u2019ouverture de session d\u2019un compte s\u2019est correctement d\u00e9roul\u00e9e.#015#012#015#012Sujet :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-5-18#015#012#011Nom du compte :#011#011USERNAME$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d\u2019ouverture de session :#011#011User1#015#012#015#012Type d\u2019ouverture de session :#011#011#0115#015#012#015#012Nouvelle ouverture de session :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-5-18#015#012#011Nom du compte :#011#011Syst\u00e8me#015#012#011Domaine du compte :#011#011AUTORITE NT#015#012#011ID d\u2019ouverture de session :#011#011User1#015#012#011GUID d\u2019ouverture de session :#011#011{00000000-0000-0000-0000-000000000000}#015#012#015#012Informations sur le processus :#015#012#011ID du processus :#011#0110x1d0#015#012#011Nom du processus :#011#011C:\\Windows\\System32\\services.exe#015#012#015#012Informations sur le r\u00e9seau :#015#012#011Nom de la station de travail :#011#015#012#011Adresse du r\u00e9seau source :#011-#015#012#011Port source :#011#011-#015#012#015#012Informations d\u00e9taill\u00e9es sur l\u2019authentification :#015#012#011Processus d\u2019ouverture de session :#011#011Advapi  #015#012#011Package d\u2019authentification :#011Negotiate#015#012#011Services en transit :#011-#015#012#011Nom du package (NTLM uniquement) :#011-#015#012#011Longueur de la cl\u00e9 :#011#0110#015#012#015#012Cet \u00e9v\u00e9nement est g\u00e9n\u00e9r\u00e9 lors de la cr\u00e9ation d\u2019une ouverture de session. Il est g\u00e9n\u00e9r\u00e9 sur l\u2019ordinateur sur lequel l\u2019ouverture de session a \u00e9t\u00e9 effectu\u00e9e.#015#012#015#012Le champ Objet indique le compte sur le syst\u00e8me local qui a demand\u00e9 l\u2019ouverture de session. Il s\u2019agit le plus souvent d\u2019un service, comme le service Serveur, ou un processus local tel que Winlogon.exe ou Services.exe.#015#012#015#012Le champ Type d\u2019ouverture de session indique le type d\u2019ouverture de session qui s\u2019est produit. Les types les plus courants sont 2 (interactif) et 3 (r\u00e9seau).#015#012#015#012Le champ Nouvelle ouverture de session indique le compte pour lequel la nouvelle ouverture de session a \u00e9t\u00e9 cr\u00e9\u00e9e, par exemple, le compte qui s\u2019est connect\u00e9.#015#012#015#012Les champs relatifs au r\u00e9seau indiquent la provenance d\u2019une demande d\u2019ouverture de session \u00e0 distance. Le nom de la station de travail n\u2019\u00e9tant pas toujours disponible, peut \u00eatre laiss\u00e9 vide dans certains cas.#015#012#015#012Les champs relatifs aux informations d\u2019authentification fournissent des d\u00e9tails sur cette demande d\u2019ouverture de session sp\u00e9cifique.#015#012#011- Le GUID d\u2019ouverture de session est un identificateur unique pouvant servir \u00e0 associer cet \u00e9v\u00e9nement \u00e0 un \u00e9v\u00e9nement KDC .#015#012#011- Les services en transit indiquent les services interm\u00e9diaires qui ont particip\u00e9 \u00e0 cette demande d\u2019ouverture de session.#015#012#011- Nom du package indique quel est le sous-protocole qui a \u00e9t\u00e9 utilis\u00e9 parmi les protocoles NTLM.#015#012#011- La longueur de la cl\u00e9 indique la longueur de la cl\u00e9 de session g\u00e9n\u00e9r\u00e9e",
        "event": {
            "category": [
                "authentication"
            ],
            "code": "4624",
            "outcome": "success",
            "type": [
                "start"
            ]
        },
        "action": {
            "id": 4624,
            "name": "L\u2019ouverture de session d\u2019un compte s\u2019est correctement d\u00e9roul\u00e9e.",
            "outcome": "success",
            "properties": {
                "domain": "AUTORITE NT",
                "id": "S-1-5-18",
                "logon_guid": "00000000-0000-0000-0000-000000000000",
                "logon_id": "User1",
                "logon_type": 5,
                "name": "Syst\u00e8me",
                "type": "targetedUser"
            },
            "target": "user",
            "type": "Security"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "process": {
            "id": "0x1d0",
            "name": "C:\\Windows\\System32\\services.exe"
        },
        "related": {
            "user": [
                "USERNAME$"
            ]
        },
        "sekoiaio": {
            "authentication": {
                "process": {
                    "name": "C:\\Windows\\System32\\services.exe"
                }
            },
            "server": {
                "os": {
                    "type": "windows"
                }
            }
        },
        "user": {
            "target": {
                "domain": "host.example.com",
                "id": "User1",
                "name": "USERNAME$",
                "sid": "S-1-5-18"
            }
        }
    }
    	
	```


=== "object_operation_space_separators.json"

    ```json
	
    {
        "message": "An operation was performed on an object.    Subject :  #011Security ID:#011#011S-1-5-21-1111111111-2222222222-3333333333-1000  #011Account Name:#011#011UserName  #011Account Domain:#011#011example.com  #011Logon ID:#011#01111111111    Object:  #011Object Server:#011#011DS  #011Object Type:#011#011%{bf967a86-0de6-11d0-a285-00aa003049e2}  #011Object Name:#011#011%{00000000-0000-0000-0000-000000000001}  #011Handle ID:#011#0110x0    Operation:  #011Operation Type:#011#011Object Access  #011Accesses:#011#011-  #011Access Mask:#011#0110x0  #011Properties:#011#011---  #011{bf967a86-0de6-11d0-a285-00aa003049e2}  Control Access  #011#011#011{6617e4ac-a2f1-43ab-b60c-11fbd1facf05}  #011#011#011{b3f93023-9239-4f7c-b99c-6745d87adbc2}  #011#011#011{b8dfa744-31dc-4ef1-ac7c-84baf7ef9da7}  #011#011#011{b7ff5a38-0818-42b0-8110-d3d154c97f24}  #011#011{91e647de-d96f-4b70-9557-d63ff4f3ccd8}      Additional Information:  #011Parameter 1:#011#011-  #011Parameter 2:#011#011",
        "event": {
            "code": "4662",
            "outcome": "success"
        },
        "action": {
            "id": 4662,
            "name": "An operation was performed on an object.",
            "properties": {
                "type": "targetedUser"
            },
            "target": "user"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "related": {
            "user": [
                "UserName"
            ]
        },
        "user": {
            "target": {
                "domain": "example.com",
                "id": "11111111",
                "name": "UserName",
                "sid": "S-1-5-21-1111111111-2222222222-3333333333-1000"
            }
        }
    }
    	
	```


=== "pass_ch.json"

    ```json
	
    {
        "message": "Une tentative de r\u00e9initialisation de mot de passe d\u2019un compte a \u00e9t\u00e9 effectu\u00e9e.#015#012#015#012Sujet :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-5-18#015#012#011Nom du compte :#011#011USERNAME$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d\u2019ouverture de session :#011#011User1#015#012#015#012Compte cible :#015#012#011ID de s\u00e9curit\u00e9 :#011#011S-1-2-3#015#012#011Nom du compte :#011#011USERNAME#015#012#011Domaine du compte :#011#011host.example.com",
        "event": {
            "code": "4724",
            "outcome": "success"
        },
        "action": {
            "id": 4724,
            "name": "Une tentative de r\u00e9initialisation de mot de passe d\u2019un compte a \u00e9t\u00e9 effectu\u00e9e.",
            "properties": {
                "domain": "host",
                "id": "S-1-2-3",
                "name": "USERNAME",
                "type": "targetedUser"
            },
            "target": "user",
            "type": "Security"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "related": {
            "user": [
                "USERNAME$"
            ]
        },
        "user": {
            "target": {
                "domain": "host.example.com",
                "id": "User1",
                "name": "USERNAME$",
                "sid": "S-1-5-18"
            }
        }
    }
    	
	```


=== "process2.json"

    ```json
	
    {
        "message": "D\u00e9marrage de Self-Service Plug-in (utilisateur=host.example.com\\User1).",
        "event": {
            "outcome": "success"
        },
        "action": {
            "name": "D\u00e9marrage de Self-Service Plug-in",
            "properties": {
                "type": "targetedUser"
            },
            "target": "user"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        },
        "related": {
            "user": [
                "User1"
            ]
        },
        "user": {
            "domain": "host.example.com",
            "name": "User1"
        }
    }
    	
	```


=== "wfp_bind_unsupported_structure.json"

    ```json
	
    {
        "message": "The Windows Filtering Platform has permitted a bind to a local port.#015#012#015#012Application Information:#015#012#011Process ID:#011#0114#015#012#011Application Name:#011System#015#012#015#012Network Information:#015#012#011Source Address:#011#0110.0.0.0#015#012#011Source Port:#011#01149152#015#012#011Protocol:#011#0116#015#012#015#012Filter Information:#015#012#011Filter Run-Time ID:#0110#015#012#011Layer Name:#011#011Resource Assignment#015#012#011Layer Run-Time ID:#01136",
        "event": {
            "code": "5158",
            "outcome": "success"
        },
        "action": {
            "id": 5158,
            "name": "The Windows Filtering Platform has permitted a bind to a local port.",
            "properties": {
                "type": "targetedUser"
            },
            "target": "user"
        },
        "os": {
            "family": "windows",
            "platform": "windows"
        }
    }
    	
	```





### Extracted Fields

The following table lists the fields that are extracted, normalized under the ECS format, analyzed and indexed by the parser. It should be noted that infered fields are not listed.

| Name | Type | Description                |
| ---- | ---- | ---------------------------|
|`action.properties.domain` | `keyword` |  |
|`action.properties.id` | `keyword` |  |
|`action.properties.logon_guid` | `keyword` |  |
|`action.properties.logon_id` | `keyword` |  |
|`action.properties.logon_type` | `number` |  |
|`action.properties.name` | `keyword` |  |
|`action.properties.target` | `keyword` |  |
|`action.properties.type` | `keyword` |  |
|`action.target` | `keyword` |  |
|`event.code` | `keyword` | Identification code for this event. |
|`event.outcome` | `keyword` | The outcome of the event. The lowest level categorization field in the hierarchy. |
|`process.id` | `keyword` |  |
|`process.name` | `keyword` | Process name. |
|`user.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.id` | `keyword` | Unique identifier of the user. |
|`user.name` | `keyword` | Short name or login of the user. |
|`user.sid` | `keyword` |  |
|`user.target.domain` | `keyword` | Name of the directory the user is a member of. |
|`user.target.id` | `keyword` | Unique identifier of the user. |
|`user.target.name` | `keyword` | Short name or login of the user. |
|`user.target.sid` | `keyword` |  |



For more information on the Intake Format, please find the code of the Parser, Smart Descriptions, and Supported Events [here](https://github.com/SEKOIA-IO/intake-formats/tree/main/Log Insight Windows/log-insight-windows).