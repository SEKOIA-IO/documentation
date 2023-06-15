## Related Built-in Rules

Benefit from Sekoia.io built-in rules and upgrade **AWS CloudTrail** with the following detection capabilities out-of-the-box.

[Sekoia.io x AWS CloudTrail on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_d3a813ac-f9b5-451c-a602-a5994544d9ed_do_not_edit_manually.json){ .md-button }
??? abstract "AWS CloudTrail Important Change"
    
    Detects disabling, deleting and updating of a Trail source which could be done by some attackers trying to masquerade their activity.
    
    - **Effort:** advanced

??? abstract "AWS Config Disable Channel/Recorder"
    
    Detects AWS Config Service disabling channel or recorder
    
    - **Effort:** elementary

??? abstract "AWS Disable MFA"
    
    Detects a user disabling the multi factor authentication mechanism for its account. It could be a sign of malicious activity.
    
    - **Effort:** intermediate

??? abstract "AWS EC2 Security Group Modified"
    
    Detects when an AWS EC2 security group has been modified
    
    - **Effort:** master

??? abstract "AWS EC2 Startup Script Changed"
    
    Detects changes to the EC2 instance startup script. The shell script will be executed as root/SYSTEM everytime the specific instances are booted up.
    
    - **Effort:** intermediate

??? abstract "AWS EC2 Subnet Deleted"
    
    Detects when an attacker is destroying an EC2 subnet.
    
    - **Effort:** master

??? abstract "AWS ECS Cluster Deleted"
    
    Detects when an attacker is destroying an AWS ECS Cluster
    
    - **Effort:** intermediate

??? abstract "AWS EventBridge Rule Disabled Or Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting or disabling EventBridge rules
    
    - **Effort:** master

??? abstract "AWS GuardDuty Detector Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting a GuardDuty detector
    
    - **Effort:** elementary

??? abstract "AWS GuardDuty Detector Suspended"
    
    Detects the suspension of the GuardDuty service
    
    - **Effort:** elementary

??? abstract "AWS GuardDuty Disruption"
    
    Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts against malicious IPs
    
    - **Effort:** intermediate

??? abstract "AWS IAM Failed User Creation"
    
    Detects an attemp to create a user account where the result is an explicit denied.
    
    - **Effort:** intermediate

??? abstract "AWS IAM Password Policy Updated"
    
    Detects an update to the password policy. This could be an attempt to lower accounts security level.
    
    - **Effort:** intermediate

??? abstract "AWS IAM Policy Changed"
    
    Detects change on AWS IAM Policy
    
    - **Effort:** master

??? abstract "AWS KMS CMK Key Deleted"
    
    Detects when a CMK is deleted or scheduled for deletion
    
    - **Effort:** advanced

??? abstract "AWS RDS Change Master Password"
    
    Detects the change of database master password. It may be a part of data exfiltration.
    
    - **Effort:** intermediate

??? abstract "AWS RDS DB Cluster/Instance Deleted"
    
    Detects when an attacker is destroying a RDS Cluster or Instance
    
    - **Effort:** advanced

??? abstract "AWS RDS Public DB Restore"
    
    Detects the recovery of a new public database instance from a snapshot. It may be a part of data exfiltration.
    
    - **Effort:** intermediate

??? abstract "AWS Remove Flow logs"
    
    Detects when an attacker is removing Flow Logs to cover their tracks
    
    - **Effort:** elementary

??? abstract "AWS Route 53 Domain Transfer Attempt"
    
    Detects when a request in success or failure is made to transfer a domain name to an other AWS account
    
    - **Effort:** intermediate

??? abstract "AWS Route 53 Domain Transfer Lock Disabled"
    
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

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "Sekoia.io Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
