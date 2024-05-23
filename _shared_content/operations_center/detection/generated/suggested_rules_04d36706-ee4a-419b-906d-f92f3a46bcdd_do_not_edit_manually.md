## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Google Report**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Google Report on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_04d36706-ee4a-419b-906d-f92f3a46bcdd_do_not_edit_manually.json){ .md-button }
??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Google Workspace Admin Creation"
    
    Detects when an admin is created or when his role is changed.
    
    - **Effort:** master

??? abstract "Google Workspace Admin Deletion"
    
    Detects when an admin is deleted or when his role is unassigned.
    
    - **Effort:** master

??? abstract "Google Workspace Admin Modification"
    
    Detects when an admin is modified.
    
    - **Effort:** master

??? abstract "Google Workspace App Script Scheduled Task"
    
    Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.
    
    - **Effort:** advanced

??? abstract "Google Workspace Bypass 2FA"
    
    Detects when user tries to bypass the 2FA.
    
    - **Effort:** master

??? abstract "Google Workspace Domain Delegation"
    
    Detects when a domain delegation is granted.
    
    - **Effort:** master

??? abstract "Google Workspace Email Forwarding"
    
    Detects when a user enables email forwarding out of the domain
    
    - **Effort:** advanced

??? abstract "Google Workspace MFA changed"
    
    Detects when the settings for the MFA are modified.
    
    - **Effort:** master

??? abstract "Google Workspace Password Change"
    
    Detects when a password is changed. An attacker can perform this action to impact the availability of the account.
    
    - **Effort:** master

??? abstract "Google Workspace User Creation"
    
    Detects when a new user is created.
    
    - **Effort:** master

??? abstract "Google Workspace User Deletion"
    
    Detects when an user is deleted.
    
    - **Effort:** master

??? abstract "Google Workspace User Suspended"
    
    Detects when an user is suspended. An attacker can use this to remove an account used during the intrusion.
    
    - **Effort:** master

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

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

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
