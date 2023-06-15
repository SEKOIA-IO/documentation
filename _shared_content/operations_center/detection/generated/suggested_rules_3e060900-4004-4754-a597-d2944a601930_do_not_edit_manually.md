## Related Built-in Rules

Benefit from Sekoia.io built-in rules and upgrade **AWS GuardDuty [BETA]** with the following detection capabilities out-of-the-box.

[Sekoia.io x AWS GuardDuty [BETA] on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_3e060900-4004-4754-a597-d2944a601930_do_not_edit_manually.json){ .md-button }
??? abstract "AWS GuardDuty High Severity Alert"
    
    GuardDuty has detected a threat with a high severity level. A High severity level indicates that the resource in question (an EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.
    
    - **Effort:** intermediate

??? abstract "AWS GuardDuty Low Severity Alert"
    
    GuardDuty has detected a threat with a low severity level. A low severity level indicates attempted suspicious activity that did not compromise your network, for example, a port scan or a failed intrusion attempt.
    
    - **Effort:** master

??? abstract "AWS GuardDuty Medium Severity Alert"
    
    GuardDuty has detected a threat with a medium severity level. A Medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.
    
    - **Effort:** advanced

??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner)
    
    - **Effort:** intermediate

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

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced
