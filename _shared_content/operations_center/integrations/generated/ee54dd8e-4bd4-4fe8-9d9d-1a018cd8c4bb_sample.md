
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "account_modification"

    ```
	Un compte d’utilisateur a été modifié.#015#012#015#012Sujet :#015#012#011ID de sécurité :#011#011S-1-5-18#015#012#011Nom du compte :#011#011host.example.com$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d’ouverture de session :#011#011User1#015#012#015#012Compte cible :#015#012#011ID de sécurité :#011#011S-1-5-21-241366212-796369622-1890169025-500#015#012#011Nom du compte :#011#011USERNAME#015#012#011Domaine du compte :#011#011host.example.com#015#012#015#012Attributs modifiés :#015#012#011Nom du compte SAM :#011USERNAME#015#012#011Nom complet :#011#011<valeur non définie>#015#012#011Nom principal de l’utilisateur :#011-#015#012#011Répertoire de base :#011#011<valeur non définie>#015#012#011Lecteur de base :#011#011<valeur non définie>#015#012#011Chemin d’accès au script :#011#011<valeur non définie>#015#012#011Chemin d’accès au profil :#011#011<valeur non définie>#015#012#011Stations de travail utilisateurs :#011<valeur non définie>#015#012#011Dernière modification du mot de passe le :#01110/06/2020 14:27:09#015#012#011Le compte expire le :#011#011<jamais>#015#012#011ID de groupe principal :#011513#015#012#011Délégué autorisé :#011-#015#012#011Ancienne valeur UAC :#011#0110x210#015#012#011Nouvelle valeur UAC :#011#0110x210#015#012#011Contrôle du compte d’utilisateur :#011-#015#012#011Paramètres utilisateur :#011-#015#012#011Historique SID :#011#011-#015#012#011Horaire d’accès :#011#011Tout#015#012#015#012Informations supplémentaires :#015#012#011Privilèges:#011#011-
    ```



=== "exploit_protection"

    ```
	Process '\Device\HarddiskVolume2\Windows\System32\svchost.exe' (PID 6904) would have been blocked from generating dynamic code.
    ```



=== "logoff_mess"

    ```
	An account was logged off.#015#012#015#012Subject:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x523d454d#015#012#015#012Logon Type:#011#011#0115#015#012#015#012This event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer.
    ```



=== "logon_mess"

    ```
	An account was successfully logged on.#015#012#015#012Subject:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x1bc9bbee#015#012#015#012Logon Type:#011#011#0115#015#012#015#012New Logon:#015#012#011Security ID:#011#011S-1-5-21-1494196517-2992400115-1379426628-1000#015#012#011Account Name:#011#011username#015#012#011Account Domain:#011#011host.example.com#015#012#011Logon ID:#011#0110x222c4f34#015#012#011Logon GUID:#011#011{00000000-0000-0000-0000-000000000000}#015#012#015#012Process Information:#015#012#011Process ID:#011#0110x5df8#015#012#011Process Name:#011#011C:\ABSciex\drm\xGate.exe#015#012#015#012Network Information:#015#012#011Workstation Name:#011host.example.com#015#012#011Source Network Address:#011-#015#012#011Source Port:#011#011-#015#012#015#012Detailed Authentication Information:#015#012#011Logon Process:#011#011Advapi  #015#012#011Authentication Package:#011Negotiate#015#012#011Transited Services:#011-#015#012#011Package Name (NTLM only):#011-#015#012#011Key Length:#011#0110#015#012#015#012This event is generated when a logon session is created. It is generated on the computer that was accessed.#015#012#015#012The subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.#015#012#015#012The logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).#015#012#015#012The New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.#015#012#015#012The network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.#015#012#015#012The authentication information fields provide detailed information about this specific logon request.#015#012#011- Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.#015#012#011- Transited services indicate which intermediate services have participated in this logon request.#015#012#011- Package name indicates which sub-protocol was used among the NTLM protocols.#015#012#011- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.
    ```



=== "logon_mess_fr"

    ```
	L’ouverture de session d’un compte s’est correctement déroulée.#015#012#015#012Sujet :#015#012#011ID de sécurité :#011#011S-1-5-18#015#012#011Nom du compte :#011#011USERNAME$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d’ouverture de session :#011#011User1#015#012#015#012Type d’ouverture de session :#011#011#0115#015#012#015#012Nouvelle ouverture de session :#015#012#011ID de sécurité :#011#011S-1-5-18#015#012#011Nom du compte :#011#011Système#015#012#011Domaine du compte :#011#011AUTORITE NT#015#012#011ID d’ouverture de session :#011#011User1#015#012#011GUID d’ouverture de session :#011#011{00000000-0000-0000-0000-000000000000}#015#012#015#012Informations sur le processus :#015#012#011ID du processus :#011#0110x1d0#015#012#011Nom du processus :#011#011C:\Windows\System32\services.exe#015#012#015#012Informations sur le réseau :#015#012#011Nom de la station de travail :#011#015#012#011Adresse du réseau source :#011-#015#012#011Port source :#011#011-#015#012#015#012Informations détaillées sur l’authentification :#015#012#011Processus d’ouverture de session :#011#011Advapi  #015#012#011Package d’authentification :#011Negotiate#015#012#011Services en transit :#011-#015#012#011Nom du package (NTLM uniquement) :#011-#015#012#011Longueur de la clé :#011#0110#015#012#015#012Cet événement est généré lors de la création d’une ouverture de session. Il est généré sur l’ordinateur sur lequel l’ouverture de session a été effectuée.#015#012#015#012Le champ Objet indique le compte sur le système local qui a demandé l’ouverture de session. Il s’agit le plus souvent d’un service, comme le service Serveur, ou un processus local tel que Winlogon.exe ou Services.exe.#015#012#015#012Le champ Type d’ouverture de session indique le type d’ouverture de session qui s’est produit. Les types les plus courants sont 2 (interactif) et 3 (réseau).#015#012#015#012Le champ Nouvelle ouverture de session indique le compte pour lequel la nouvelle ouverture de session a été créée, par exemple, le compte qui s’est connecté.#015#012#015#012Les champs relatifs au réseau indiquent la provenance d’une demande d’ouverture de session à distance. Le nom de la station de travail n’étant pas toujours disponible, peut être laissé vide dans certains cas.#015#012#015#012Les champs relatifs aux informations d’authentification fournissent des détails sur cette demande d’ouverture de session spécifique.#015#012#011- Le GUID d’ouverture de session est un identificateur unique pouvant servir à associer cet événement à un événement KDC .#015#012#011- Les services en transit indiquent les services intermédiaires qui ont participé à cette demande d’ouverture de session.#015#012#011- Nom du package indique quel est le sous-protocole qui a été utilisé parmi les protocoles NTLM.#015#012#011- La longueur de la clé indique la longueur de la clé de session générée
    ```



=== "object_operation_space_separators"

    ```
	An operation was performed on an object.    Subject :  #011Security ID:#011#011S-1-5-21-1111111111-2222222222-3333333333-1000  #011Account Name:#011#011UserName  #011Account Domain:#011#011example.com  #011Logon ID:#011#01111111111    Object:  #011Object Server:#011#011DS  #011Object Type:#011#011%{bf967a86-0de6-11d0-a285-00aa003049e2}  #011Object Name:#011#011%{00000000-0000-0000-0000-000000000001}  #011Handle ID:#011#0110x0    Operation:  #011Operation Type:#011#011Object Access  #011Accesses:#011#011-  #011Access Mask:#011#0110x0  #011Properties:#011#011---  #011{bf967a86-0de6-11d0-a285-00aa003049e2}  Control Access  #011#011#011{6617e4ac-a2f1-43ab-b60c-11fbd1facf05}  #011#011#011{b3f93023-9239-4f7c-b99c-6745d87adbc2}  #011#011#011{b8dfa744-31dc-4ef1-ac7c-84baf7ef9da7}  #011#011#011{b7ff5a38-0818-42b0-8110-d3d154c97f24}  #011#011{91e647de-d96f-4b70-9557-d63ff4f3ccd8}      Additional Information:  #011Parameter 1:#011#011-  #011Parameter 2:#011#011
    ```



=== "pass_ch"

    ```
	Une tentative de réinitialisation de mot de passe d’un compte a été effectuée.#015#012#015#012Sujet :#015#012#011ID de sécurité :#011#011S-1-5-18#015#012#011Nom du compte :#011#011USERNAME$#015#012#011Domaine du compte :#011#011host.example.com#015#012#011ID d’ouverture de session :#011#011User1#015#012#015#012Compte cible :#015#012#011ID de sécurité :#011#011S-1-2-3#015#012#011Nom du compte :#011#011USERNAME#015#012#011Domaine du compte :#011#011host.example.com
    ```



=== "process2"

    ```
	Démarrage de Self-Service Plug-in (utilisateur=host.example.com\User1).
    ```



=== "wfp_bind_unsupported_structure"

    ```
	The Windows Filtering Platform has permitted a bind to a local port.#015#012#015#012Application Information:#015#012#011Process ID:#011#0114#015#012#011Application Name:#011System#015#012#015#012Network Information:#015#012#011Source Address:#011#0110.0.0.0#015#012#011Source Port:#011#01149152#015#012#011Protocol:#011#0116#015#012#015#012Filter Information:#015#012#011Filter Run-Time ID:#0110#015#012#011Layer Name:#011#011Resource Assignment#015#012#011Layer Run-Time ID:#01136
    ```



