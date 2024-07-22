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

??? abstract "AWS CloudTrail EC2 Enable Serial Console Access"
    
    Detects when the EC2 serial console access feature is enabled. This could abused by some attackers to avoid network detection when accessing to EC2 instances.
    
    - **Effort:** intermediate

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

??? abstract "AWS CloudTrail S3 Bucket Replication"
    
    Detects a replication rule being enable for a given S3 bucket: it could provide an attacker a way to exfiltrate data.
    
    - **Effort:** master

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Backup Catalog Deleted"
    
    The rule detects when the Backup Catalog has been deleted. It means the administrators will not be able to access any backups that were created earlier to perform recoveries. This is often being done using the wbadmin.exe tool.
    
    - **Effort:** intermediate

??? abstract "Computer Account Deleted"
    
    Detects computer account deletion.
    
    - **Effort:** master

??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "DHCP Server Error Failed Loading the CallOut DLL"
    
    This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.
    
    - **Effort:** intermediate

??? abstract "DHCP Server Loaded the CallOut DLL"
    
    This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.
    
    - **Effort:** intermediate

??? abstract "DNS Server Error Failed Loading The ServerLevelPluginDLL"
    
    This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.
    
    - **Effort:** master

??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Microsoft Defender Antivirus History Deleted"
    
    Windows Defender history has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** master

??? abstract "Microsoft Defender Antivirus Tampering Detected"
    
    Detection of Windows Defender Tampering, from definitions' deletion to deactivation of parts or all of Defender.
    
    - **Effort:** advanced

??? abstract "Microsoft Defender Antivirus Threat Detected"
    
    Detection of a windows defender alert indicating the presence of potential malware
    
    - **Effort:** advanced

??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "Potential RDP Connection To Non-Domain Host"
    
    Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.
    
    - **Effort:** master

??? abstract "Remote Access Tool Domain"
    
    Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).
    
    - **Effort:** master

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? abstract "User Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master
