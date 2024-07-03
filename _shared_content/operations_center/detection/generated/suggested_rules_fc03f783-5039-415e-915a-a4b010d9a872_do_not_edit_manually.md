## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **IBM iSeries [BETA]**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x IBM iSeries [BETA] on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_fc03f783-5039-415e-915a-a4b010d9a872_do_not_edit_manually.json){ .md-button }
??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Active Directory Data Export Using Csvde"
    
    Detects the use of Csvde, a command-line tool from Windows Server that can be used to export Active Directory data to CSV files. This export doesn't include password hashes, but can be used as a discovery tool to enumerate users, machines and group memberships.
    
    - **Effort:** elementary

??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? abstract "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
    - **Effort:** advanced

??? abstract "Aspnet Compiler"
    
    Detects the starts of aspnet compiler.
    
    - **Effort:** advanced

??? abstract "CVE-2017-11882 Microsoft Office Equation Editor Vulnerability"
    
    Detects the exploitation of CVE-2017-11882 vulnerability. The Microsoft Office Equation Editor has no reason to do a network request or drop an executable file. This requires a sysmon configuration with file and network events.
    
    - **Effort:** master

??? abstract "CVE-2021-34527 PrintNightmare Suspicious Actions From Spoolsv"
    
    Detects suspicious image loads and file creations from the spoolsv process which could be a sign of an attacker trying to exploit the PrintNightmare vulnerability, CVE-2021-34527. A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. This works as well as a Local Privilege escalation vulnerability. To fully work the rule requires to log for Loaded DLLs and File Creations, which can be done respectively using the Sysmon's event IDs 7 and 11.
    
    - **Effort:** master

??? abstract "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** intermediate

??? abstract "Computer Account Deleted"
    
    Detects computer account deletion.
    
    - **Effort:** master

??? abstract "Cookies Deletion"
    
    Detects when cookies are deleted by a suspicious process.
    
    - **Effort:** master

??? abstract "Cron Files Alteration"
    
    Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation.
    
    - **Effort:** advanced

??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate

??? abstract "Kernel Module Alteration"
    
    Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems.
    
    - **Effort:** advanced

??? abstract "Microsoft Exchange Server Creating Unusual Files"
    
    Look for Microsoft Exchange Server’s Unified Messaging service creating non-standard content on disk, which could indicate web shells or other malicious content, suggesting exploitation of CVE-2021-26858 vulnerability
    
    - **Effort:** intermediate

??? abstract "Microsoft Office Creating Suspicious File"
    
    Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.
    
    - **Effort:** master

??? abstract "NTDS.dit File In Suspicious Directory"
    
    The file NTDS.dit is supposed to be located mainly in C:\Windows\NTDS. The rule checks whether the file is in a legitimate directory or not (through file creation events). This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** advanced

??? abstract "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate

??? abstract "OneNote Embedded File"
    
    Detects creation or uses of OneNote embedded files with unusual extensions.  
    
    - **Effort:** intermediate

??? abstract "Package Manager Alteration"
    
    Package manager (eg: apt, yum) can be altered to install malicious software
    
    - **Effort:** advanced

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate

??? abstract "PsExec Process"
    
    Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 
    
    - **Effort:** advanced

??? abstract "RDP Session Discovery"
    
    Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.
    
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

??? abstract "Remote Monitoring and Management Software - Atera"
    
    Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool Atera.
    
    - **Effort:** master

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "SSH Authorized Key Alteration"
    
    The file authorized_keys is used by SSH server to identify SSH keys that are authorized to connect to the host, alteration of one of those files might indicate a user compromision.
    
    - **Effort:** advanced

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "SolarWinds Suspicious File Creation"
    
    Detects SolarWinds process creating a file with a suspicious extension. The process solarwinds.businesslayerhost.exe created an unexpected file whose extension is ".exe", ".ps1", ".jpg", ".png" or ".dll".
    
    - **Effort:** intermediate

??? abstract "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** advanced

??? abstract "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host.
    
    - **Effort:** master

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? abstract "User Account Created"
    
    Detects user creation on windows servers, which shouldn't happen in an Active Directory environment. Apply this on your windows server logs and not on your DC logs. One default account `defaultuser0` is excluded as only used during Windows set-up. This detection use Security Event ID 4720. 
    
    - **Effort:** master

??? abstract "User Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate

??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced

??? abstract "Webshell Creation"
    
    Detects possible webshell file creation. It requires File Creation monitoring, which can be done using Sysmon's Event ID 11. However the recommended SwiftOnSecurity configuration does not fully cover the needs for this rule, it needs to be updated with the proper file names extensions.
    
    - **Effort:** master
