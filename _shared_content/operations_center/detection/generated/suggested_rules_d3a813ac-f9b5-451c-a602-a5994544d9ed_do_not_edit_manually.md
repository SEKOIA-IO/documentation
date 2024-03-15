## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **AWS CloudTrail**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x AWS CloudTrail on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_d3a813ac-f9b5-451c-a602-a5994544d9ed_do_not_edit_manually.json){ .md-button }
??? abstract "AWS CloudTrail Config DeleteConfigurationRecorder"
    
    Detects when the Configuration Recorder was deleted. The configuration recorder is used to detect changes in your resource configurations and capture these changes as configuration items.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail Config Disable Channel/Recorder"
    
    Detects AWS Config Service disabling channel or recorder
    
    - **Effort:** elementary

??? abstract "AWS CloudTrail Disable MFA"
    
    Detects a user disabling the multi factor authentication mechanism for its account. It could be a sign of malicious activity.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail EC2 CreateKeyPair"
    
    Detects when a key pair is created. Usually, SendSSHPublicKey is used afterwards to push the created key to an EC2 instance in order to be able to establish a connection to that instance.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail EC2 CreateVPC"
    
    Detects when a VPC is created.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail EC2 DeleteKeyPair"
    
    Detects when a specific key pair is deleted. This means the public key was removed from EC2.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail EC2 Instance Connect SendSSHPublicKey"
    
    Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a connection to the console using SSH.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail EC2 Instance Connect SendSerialConsoleSSHPublicKey"
    
    Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a serial connection to the console using SSH.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail EC2 Security Group Modified"
    
    Detects when an AWS EC2 security group has been modified
    
    - **Effort:** master

??? abstract "AWS CloudTrail EC2 Startup Script Changed"
    
    Detects changes to the EC2 instance startup script. The shell script will be executed as root/SYSTEM everytime the specific instances are booted up.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail EC2 Subnet Deleted"
    
    Detects when an attacker is destroying an EC2 subnet.
    
    - **Effort:** master

??? abstract "AWS CloudTrail ECS Cluster Deleted"
    
    Detects when an attacker is destroying an AWS ECS Cluster
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail EventBridge Rule Disabled Or Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting or disabling EventBridge rules
    
    - **Effort:** master

??? abstract "AWS CloudTrail GuardDuty Detector Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting a GuardDuty detector
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail GuardDuty Detector Suspended"
    
    Detects the suspension of the GuardDuty service
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail GuardDuty Disruption"
    
    Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts against malicious IPs
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM AWSCompromisedKeyQuarantineV2"
    
    Detects when AWS CloudTrail detected an AWS Access Key that was compromised, and then quarantined by AWS. This could indicate for instance that the private key was found on a GitHub public repository.
    
    - **Effort:** elementary

??? abstract "AWS CloudTrail IAM AddClientIDToOpenIDConnectProvider"
    
    Detects the addition of a Client ID to an existing identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM ChangePassword"
    
    Detects when an IAM user wants to change its password.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail IAM CreateOpenIDConnectProvider"
    
    Detects the creation of an IAM entity to describe an identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM CreateSAMLProvider"
    
    Detects when an IAM user creates a SAML provider, which could allow third-party connection and therefore could be used by attackers.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM DeleteOpenIDConnectProvider"
    
    Detects the deletion of an IAM entity to describe an identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM DeleteSAMLProvider"
    
    Detects when an IAM user deletes a SAML provider, which could be performed by attackers to cover their tracks.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM Failed User Creation"
    
    Detects an attemp to create a user account where the result is an explicit denied.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM Password Policy Updated"
    
    Detects an update to the password policy. This could be an attempt to lower accounts security level.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM Policy Changed"
    
    Detects change on AWS IAM Policy
    
    - **Effort:** master

??? abstract "AWS CloudTrail IAM RemoveClientIDFromOpenIDConnectProvider"
    
    Detects when a Client ID is removed from an identity provider that supports OpenID Connect. Could be used by attackers for sabotage or to cover their tracks.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM UpdateOpenIDConnectProviderThumbprint"
    
    Detects the update of a ThumbPrint from an identity provider that supports OpenID Connect. This could be a sign of an attacker adding a trusted certificate.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail IAM UpdateSAMLProvider"
    
    Detects when an IAM user updates a SAML provider. Attackers could perform that to be stealthy by adding a third-party connection into an existing SAML provider.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail Important Change"
    
    Detects disabling, deleting and updating of a Trail source which could be done by some attackers trying to masquerade their activity.
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail KMS CMK Key Deleted"
    
    Detects when a CMK is deleted or scheduled for deletion
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail RDS Change Master Password"
    
    Detects the change of database master password. It may be a part of data exfiltration.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail RDS DB Cluster/Instance Deleted"
    
    Detects when an attacker is destroying a RDS Cluster or Instance
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail RDS Public DB Restore"
    
    Detects the recovery of a new public database instance from a snapshot. It may be a part of data exfiltration.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail Remove Flow logs"
    
    Detects when an attacker is removing Flow Logs to cover their tracks
    
    - **Effort:** advanced

??? abstract "AWS CloudTrail Root ConsoleLogin"
    
    Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail Route 53 Domain Transfer Attempt"
    
    Detects when a request in success or failure is made to transfer a domain name to an other AWS account
    
    - **Effort:** intermediate

??? abstract "AWS CloudTrail Route 53 Domain Transfer Lock Disabled"
    
    Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.
    
    - **Effort:** elementary

??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
