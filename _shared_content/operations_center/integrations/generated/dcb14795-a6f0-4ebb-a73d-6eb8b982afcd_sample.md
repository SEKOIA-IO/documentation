
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



=== "connexion3"

    ```
	Connexion au portail web org:example, user:toto@ORGANIZATION, ip:1.1.1.1
    ```



=== "connexion4"

    ```
	Connexion d&#39;une passerelle org:example, user:@local, ip:1.1.1.1
    ```



=== "deconnexion1"

    ```
	Déconnexion du portail web org:example, user:jdoe@EXAMPLE, ip:1.2.3.4
    ```



=== "deconnexion2"

    ```
	Déconnexion d'un plugin utilisateur org:example, user:jdoe@local, ip:10.48.178.33
    ```



=== "deconnexion3"

    ```
	Déconnexion du portail web org:example, user:toto@ORGANIZATION, ip:1.1.1.1
    ```



=== "deconnexion4"

    ```
	D&#233;connexion d&#39;une passerelle org:example, user:@local, ip:1.1.1.1
    ```



=== "echec1"

    ```
	Echec de la connexion &#224; la console d&#39;administration org:example, user:toto@example, ip:1.1.1.1 17b82585-3f88-4500-baf4-bb95ca7c3344
    ```



=== "fermeture1"

    ```
	Fermeture d'une application SSH (Secure Shell) : MultiTOTOAPP org:example, user:titi@ORGANIZATION, ip:1.1.1.1
    ```



=== "lancement1"

    ```
	Lancement d'une application Web : MultiTOTOAPP org:example, user:toto@ORGANIZATION, ip:1.1.1.1
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



