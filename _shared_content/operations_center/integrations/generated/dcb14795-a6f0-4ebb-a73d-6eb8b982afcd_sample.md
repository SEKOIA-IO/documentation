
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "connexion1"

    ```
	Connexion au portail web org:example, user:jdoe@local, ip:1.2.3.4
    ```



=== "connexion2"

    ```
	Connexion d'un plugin utilisateur org:example, user:jdoe@local, ip:1.2.3.4
    ```



=== "deconnexion1"

    ```
	Déconnexion du portail web org:example, user:jdoe@EXAMPLE, ip:1.2.3.4
    ```



=== "deconnexion2"

    ```
	Déconnexion d'un plugin utilisateur org:example, user:jdoe@local, ip:10.48.178.33
    ```



=== "process1"

    ```
	Fermeture d'une application  RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT org:example, user:jdoe@EXAMPLE, ip:1.2.3.4
    ```



=== "process2"

    ```
	Lancement d'une application RDS  : DETECTION CENTRAL (RDP) AGENT CLIENT org:example, user:jdoe@EXAMPLE, ip:1.2.3.4
    ```



=== "session"

    ```
	Echec de la connexion au portail web : erreur d'authentification d'un utilisateur org:example, user:jdoe@EXAMPLE, ip:1.2.3.4
    ```



