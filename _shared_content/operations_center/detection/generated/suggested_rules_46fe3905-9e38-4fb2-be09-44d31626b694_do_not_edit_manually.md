### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Retarus Email Security**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Retarus Email Security on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_46fe3905-9e38-4fb2-be09-44d31626b694_do_not_edit_manually.json){ .md-button }
??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).
    
    - **Effort:** intermediate

??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced

??? abstract "Remote Access Tool Domain"
    
    Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).
    
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

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced
