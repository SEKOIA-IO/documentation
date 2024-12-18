### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Google Report**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Google Report on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_04d36706-ee4a-419b-906d-f92f3a46bcdd_do_not_edit_manually.json){ .md-button }
??? abstract "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master

??? abstract "Certify Or Certipy"
    
    Detects the use of certify and certipy which are two different tools used to enumerate and abuse Active Directory Certificate Services.
    
    - **Effort:** advanced

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** intermediate

??? abstract "Credential Dump Tools Related Files"
    
    Detects processes or file names related to credential dumping tools and the dropped files they generate by default.
    
    - **Effort:** advanced

??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Google Workspace Account Warning"
    
    Detects a suspicious login, leaked password, or account disabled following suspicious activity.
    
    - **Effort:** elementary

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

??? abstract "Google Workspace Blocked Sender"
    
    Detects when a user is blocked by google workspace.
    
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

??? abstract "Google Workspace External Sharing"
    
    Detects a large number of external sharing.
    
    - **Effort:** master

??? abstract "Google Workspace Login Brute-Force"
    
    Detects when a user failed to login multiple times before a successful login.
    
    - **Effort:** master

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

??? abstract "HTA Infection Chains"
    
    Detect the creation of a ZIP file and an HTA file as it is often used in infection chains. Furthermore it also detects the use of suspicious processes launched by explorer.exe combined with the creation of an HTA file, since it is also often used in infection chains (LNK - HTA for instance).
    
    - **Effort:** advanced

??? abstract "HTML Smuggling Suspicious Usage"
    
    Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.
    
    - **Effort:** intermediate

??? abstract "HackTools Suspicious Names"
    
    Quick-win rule to detect the default process names or file names of several HackTools.
    
    - **Effort:** elementary

??? abstract "ISO LNK Infection Chain"
    
    Detection of an ISO (or any other similar archive file) downloaded file, followed by a child-process of explorer, which is characteristic of an infection using an ISO containing an LNK file. For events with `host.name`.
    
    - **Effort:** intermediate

??? abstract "Internet Scanner"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master

??? abstract "Internet Scanner Target"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "RSA SecurID Failed Authentification"
    
    Detects many failed attempts to authenticate followed by a successfull login for a super admin account.
    
    - **Effort:** advanced

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "Remote Access Tool Domain"
    
    Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).
    
    - **Effort:** master

??? abstract "Remote Monitoring and Management Software - AnyDesk"
    
    Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool AnyDesk.
    
    - **Effort:** master

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "Sign-In Via Known AiTM Phishing Kit"
    
    Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.
    
    - **Effort:** elementary

??? abstract "Suspicious File Name"
    
    Detects suspicious file name possibly linked to malicious tool.
    
    - **Effort:** advanced

??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate

??? abstract "ZIP LNK Infection Chain"
    
    Detection of an ZIP download followed by a child-process of explorer, followed by multiple Windows processes.This is widely used as an infection chain mechanism.
    
    - **Effort:** advanced
