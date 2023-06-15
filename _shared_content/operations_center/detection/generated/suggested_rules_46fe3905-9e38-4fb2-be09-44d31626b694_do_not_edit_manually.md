## Related Built-in Rules

Benefit from Sekoia.io built-in rules and upgrade **Retarus Email Security** with the following detection capabilities out-of-the-box.

[Sekoia.io x Retarus Email Security on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_46fe3905-9e38-4fb2-be09-44d31626b694_do_not_edit_manually.json){ .md-button }
??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner)
    
    - **Effort:** intermediate

??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master

??? abstract "Retarus Email Security Threat Detected (CxO Or Patient Zero Detection)"
    
    Cx0 fraud and Patient Zero Detection alerts detected by Retarus Email Security. CxO Fraud Detection uses algorithms that identify from-spoofing and domain-spoofing, to detect falsified sender addresses (e.g. from high level executives - CEO, CFO...). Patient Zero Detection® uses a digital fingerprint to identify emails containing malware that have already been delivered.
    
    - **Effort:** advanced

??? abstract "Retarus Email Security Threat Detected (MultiScan)"
    
    Antivirus MultiScan alerts detected by Retarus Email Security. AntiVirus MultiScan automatically scans incoming and outgoing emails and file attachments for viruses with up to four virus scanners and uses heuristic analysis to protect from unknown malware.
    
    - **Effort:** intermediate

??? abstract "Retarus Email Security Threat Detected (Sandboxing)"
    
    Sandboxing alerts detected by Retarus Email Security. Sandboxing subjects specific file attachments to an in-depth analysis. Retarus uses a sandboxing solution from the specialized and highly respected third-party provider Palo Alto Networks for this advanced threat assessment. Emails identified as infected are either deleted or quarantined, and the intended recipient is notified.
    
    - **Effort:** elementary

??? abstract "Sekoia.io Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced
