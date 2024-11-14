### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Vade for M365**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Vade for M365 on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_e4a758fc-7620-49e6-b8ed-b7fb3d7fa232_do_not_edit_manually.json){ .md-button }
??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Malware Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message.
    
    - **Effort:** master

??? abstract "Malware Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message and didn't delete it.
    
    - **Effort:** advanced

??? abstract "Phishing Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a phishing attempt.
    
    - **Effort:** master

??? abstract "Phishing Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365 has detected a phishing attempt and didn't move it to junk folder.
    
    - **Effort:** advanced

??? abstract "Remote Access Tool Domain"
    
    Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).
    
    - **Effort:** master

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Scam Detected By Vade For M365"
    
    Vade Secure product Vade for M365, has detected a scam e-mail.
    
    - **Effort:** master

??? abstract "Scam Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365, has detected a scam e-mail and didn't block it.
    
    - **Effort:** advanced

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "Spam Detected By Vade For M365"
    
    Vade Secure product Vade for M365, has detected a spam e-mail.
    
    - **Effort:** master

??? abstract "Spam Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365, has detected a spam e-mail and didn't block it.
    
    - **Effort:** advanced

??? abstract "Spearphishing (CEO Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with CEO fraud thematic. Impersonation of CEO or senior management members requesting urgent money transfer, usually on an unknown RIB.
    
    - **Effort:** master

??? abstract "Spearphishing (Gift Cards Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spear-phishing attempt with gift-cards fraud thematic. Executive impersonation requesting a money transfer to set up gift-cards for employees. Confidentiality and discretion are usually implied.
    
    - **Effort:** master

??? abstract "Spearphishing (Initial Contact Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with initial contact fraud thematic. Do not contains any malicious content or specific actions other than a request to reply to the email. “Are you available?”. The main goal is to incite a reply that could register the sending address as a known and legitimate address.
    
    - **Effort:** master

??? abstract "Spearphishing (Lawyer Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with lawyer fraud thematic. Impersonation of lawyers and lawyers' firms. The main goal is to make sure the victims will not raise awareness around them. Confidentiality restrictions are implied.
    
    - **Effort:** master

??? abstract "Spearphishing (W2 Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with W2 fraud thematic. Executive or HR impersonation phishing for social security numbers or tax identification numbers. Collected data are generally used for identity theft schemes.
    
    - **Effort:** master

??? abstract "Suspicious Email Attachment Received"
    
    Detects email containing a suspicious file as an attachment, based on its extension.
    
    - **Effort:** advanced

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master
