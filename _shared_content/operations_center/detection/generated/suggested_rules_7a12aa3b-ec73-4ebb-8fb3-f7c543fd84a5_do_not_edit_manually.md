### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Ivanti / Pulse Connect Secure**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Ivanti / Pulse Connect Secure on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_7a12aa3b-ec73-4ebb-8fb3-f7c543fd84a5_do_not_edit_manually.json){ .md-button }
??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Backup Catalog Deleted"
    
    The rule detects when the Backup Catalog has been deleted. It means the administrators will not be able to access any backups that were created earlier to perform recoveries. This is often being done using the wbadmin.exe tool.
    
    - **Effort:** intermediate

??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).
    
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

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate

??? abstract "Potential Azure AD Phishing Page (Adversary-in-the-Middle)"
    
    Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.
    
    - **Effort:** intermediate

??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced

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

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced

??? abstract "User Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master
