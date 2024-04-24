## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Fortinet FortiMail**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Fortinet FortiMail on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_60af2bd6-7ef0-48a7-a6db-90fcdd7236f1_do_not_edit_manually.json){ .md-button }
??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).
    
    - **Effort:** intermediate

??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master

??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Suspicious Email Attachment Received"
    
    Detects email containing an .exe|.dll|.ps1|.bat|.hta attachment. Most of the time files send by mail like this are malware.
    
    - **Effort:** elementary

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
