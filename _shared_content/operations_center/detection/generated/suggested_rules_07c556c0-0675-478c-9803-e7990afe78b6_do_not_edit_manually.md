### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **SentinelOne EDR**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x SentinelOne EDR on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_07c556c0-0675-478c-9803-e7990afe78b6_do_not_edit_manually.json){ .md-button }
??? abstract "ACLight Discovering Privileged Accounts"
    
    Detects use of ACLight tool. This tool aims to discover privileged accounts by scanning the network.
    
    - **Effort:** advanced

??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? abstract "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate

??? abstract "Adidnsdump Enumeration"
    
    Detects use of the tool adidnsdump for enumeration and discovering DNS records.
    
    - **Effort:** advanced

??? abstract "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master

??? abstract "Audio Capture via PowerShell"
    
    Detects audio capture via PowerShell Cmdlet
    
    - **Effort:** intermediate

??? abstract "Autorun Keys Modification"
    
    Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "AzureEdge in Command Line"
    
    Detects use of azureedge in the command line.
    
    - **Effort:** advanced

??? abstract "BITSAdmin Download"
    
    Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.
    
    - **Effort:** advanced

??? abstract "BazarLoader Persistence Using Schtasks"
    
    Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.
    
    - **Effort:** intermediate

??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate

??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary

??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).
    
    - **Effort:** intermediate

??? abstract "CMSTP UAC Bypass via COM Object Access"
    
    Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects
    
    - **Effort:** intermediate

??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.
    
    - **Effort:** intermediate

??? abstract "CVE-2020-0688 Microsoft Exchange Server Exploit"
    
    Detects the exploitation of CVE-2020-0688. The POC exploit a .NET serialization vulnerability in the Exchange Control Panel (ECP) web page. The vulnerability is due to Microsoft Exchange Server not randomizing the keys on a per-installation basis resulting in them using the same validationKey and decryptionKey values. With knowledge of these, values an attacker can craft a special viewstate to use an OS command to be executed by NT_AUTHORITY\SYSTEM using .NET deserialization. To exploit this vulnerability, an attacker needs to leverage the credentials of an account it had already compromised to authenticate to OWA.
    
    - **Effort:** elementary

??? abstract "CVE-2020-17530 Apache Struts RCE"
    
    Detects the exploitation of the Apache Struts RCE vulnerability (CVE-2020-17530).
    
    - **Effort:** intermediate

??? abstract "CVE-2021-20021 SonicWall Unauthenticated Administrator Access"
    
    Detects the exploitation of SonicWall Unauthenticated Admin Access.
    
    - **Effort:** advanced

??? abstract "CVE-2021-20023 SonicWall Arbitrary File Read"
    
    Detects Arbitrary File Read, which can be used with other vulnerabilities as a mean to obtain outputs generated by attackers, or sensitive data.
    
    - **Effort:** advanced

??? abstract "CVE-2021-22893 Pulse Connect Secure RCE Vulnerability"
    
    Detects potential exploitation of the authentication by-pass vulnerability that can allow an unauthenticated user to perform remote arbitrary file execution on the Pulse Connect Secure gateway. It is highly recommended to apply the Pulse Secure mitigations and seach for indicators of compromise on affected servers if you are in doubt over the integrity of your Pulse Connect Secure product.
    
    - **Effort:** intermediate

??? abstract "CertOC Loading Dll"
    
    Detects when a user installs certificates by using CertOC.exe to loads the target DLL file.
    
    - **Effort:** intermediate

??? abstract "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master

??? abstract "Certify Or Certipy"
    
    Detects the use of certify and certipy which are two different tools used to enumerate and abuse Active Directory Certificate Services.
    
    - **Effort:** advanced

??? abstract "Change Default File Association"
    
    When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.
    
    - **Effort:** advanced

??? abstract "Clear EventLogs Through CommandLine"
    
    Detects a command that clears event logs which could indicate an attempt from an attacker to erase its previous traces.
    
    - **Effort:** intermediate

??? abstract "Cmd.exe Used To Run Reconnaissance Commands"
    
    Detects command lines with suspicious args
    
    - **Effort:** advanced

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** intermediate

??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate

??? abstract "Component Object Model Hijacking"
    
    Detects component object model hijacking. An attacker can establish persistence with COM objects.
    
    - **Effort:** advanced

??? abstract "Compression Followed By Suppression"
    
    Detects when a file is compressed and deleted.
    
    - **Effort:** advanced

??? abstract "Container Credential Access"
    
    Adversaries could abuse containers tools to obtain credential like Kubernetes secret or Kubernetes service account access token
    
    - **Effort:** intermediate

??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced

??? abstract "Copy Of Legitimate System32 Executable"
    
    A script has copied a System32 executable.
    
    - **Effort:** intermediate

??? abstract "Copying Browser Files With Credentials"
    
    Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.
    
    - **Effort:** elementary

??? abstract "Correlation Multi Service Disable"
    
    The rule detects a high number of services stopped or de-activated in a short period of time.
    
    - **Effort:** master

??? abstract "Correlation Priv Esc Via Remote Thread"
    
    Detect a process that obtains system privilege via a remote thread
    
    - **Effort:** intermediate

??? abstract "Correlation Supicious Powershell Drop and Exec"
    
    Detects a PowerShell process that download and exec a payload
    
    - **Effort:** intermediate

??? abstract "Credential Dump Tools Related Files"
    
    Detects processes or file names related to credential dumping tools and the dropped files they generate by default.
    
    - **Effort:** advanced

??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master

??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate

??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate

??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master

??? abstract "Data Compressed With Rar With Password"
    
    An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program. This is a more specific one for rar where the arguments allow to encrypt both file data and headers with a given password.
    
    - **Effort:** intermediate

??? abstract "Debugging Software Deactivation"
    
    Deactivation of some debugging softwares using taskkill command. It was observed being used by Ransomware operators.
    
    - **Effort:** elementary

??? abstract "Default Encoding To UTF-8 PowerShell"
    
    Detects PowerShell encoding to UTF-8, which is used by Sliver implants. The command line just sets the default encoding to UTF-8 in PowerShell.
    
    - **Effort:** advanced

??? abstract "Detect requests to Konni C2 servers"
    
    This rule detects requests to Konni C2 servers. These patterns come from an analysis done in 2022, September.
    
    - **Effort:** elementary

??? abstract "Disable .NET ETW Through COMPlus_ETWEnabled"
    
    Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.
    
    - **Effort:** intermediate

??? abstract "Disable Task Manager Through Registry Key"
    
    Detects commands used to disable the Windows Task Manager by modifying the proper registry key in order to impair security tools. This technique is used by the Agent Tesla RAT, among others.
    
    - **Effort:** elementary

??? abstract "Disabled IE Security Features"
    
    Detects from the command lines or the registry, changes that indicate unwanted modifications to registry keys that disable important Internet Explorer security features. This has been used by attackers during Operation Ke3chang.
    
    - **Effort:** advanced

??? abstract "Discord Suspicious Download"
    
    Discord is a messaging application. It allows users to create their own communities to share messages and attachments. Those attachments have little to no overview and can be downloaded by almost anyone, which has been abused by attackers to host malicious payloads.
    
    - **Effort:** intermediate

??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate

??? abstract "Domain Trust Discovery Through LDAP"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. "trustedDomain" which is detected here is a Microsoft Active Directory ObjectClass Type that represents a domain that is trusted by, or trusting, the local AD DOMAIN. Several tools are using LDAP queries in the end to get the information (DSQuery, sometimes ADFind as well, etc.)
    
    - **Effort:** elementary

??? abstract "Download Files From Suspicious TLDs"
    
    Detects download of certain file types from hosts in suspicious TLDs
    
    - **Effort:** master

??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master

??? abstract "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** master

??? abstract "ETW Tampering"
    
    Detects a command that clears or disables any ETW Trace log which could indicate a logging evasion
    
    - **Effort:** intermediate

??? abstract "Equation Group DLL_U Load"
    
    Detects a specific tool and export used by EquationGroup
    
    - **Effort:** elementary

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master

??? abstract "Exfiltration Domain In Command Line"
    
    Detects commands containing a domain linked to http exfiltration.
    
    - **Effort:** intermediate

??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate

??? abstract "FLTMC command usage"
    
    Detects the use of fltmc to list and load/unload a filter driver.
    
    - **Effort:** advanced

??? abstract "Formbook File Creation DB1"
    
    Detects specific file creation (Users\*\AppData\Local\Temp\DB1) to store data to exfiltrate (Formbook behavior). Logging for Sysmon event 11 is usually used for this detection. 
    
    - **Effort:** intermediate

??? abstract "Formbook Hijacked Process Command"
    
    Detects process hijacked by Formbook malware which executes specific commands to delete the dropper or copy browser credentials to the database before sending them to the C2.
    
    - **Effort:** intermediate

??? abstract "FromBase64String Command Line"
    
    Detects suspicious FromBase64String expressions in command line arguments.
    
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

??? abstract "HackTools Suspicious Process Names In Command Line"
    
    Detects the default process name of several HackTools and also check in command line. This rule is here for quickwins as it obviously has many blind spots.
    
    - **Effort:** intermediate

??? abstract "High Privileges Network Share Removal"
    
    Detects high privileges shares being deleted with the net share command.
    
    - **Effort:** intermediate

??? abstract "ICacls Granting Access To All"
    
    Detects suspicious icacls command granting access to all, used by the ransomware Ryuk to delete every access-based restrictions on files and directories. ICacls is a built-in Windows command to interact with the Discretionary Access Control Lists (DACLs) which can grand adversaries higher permissions on specific files and folders.
    
    - **Effort:** elementary

??? abstract "ISO LNK Infection Chain"
    
    Detection of an ISO (or any other similar archive file) downloaded file, followed by a child-process of explorer, which is characteristic of an infection using an ISO containing an LNK file. For events with `host.name`.
    
    - **Effort:** intermediate

??? abstract "Impacket Wmiexec Module"
    
    Detection of impacket's wmiexec example, used by attackers to execute commands remotely.
    
    - **Effort:** elementary

??? abstract "Inhibit System Recovery Deleting Backups"
    
    Detects adversaries attempts to delete backups or inhibit system recovery. This rule relies on differents known techniques using Windows events logs from Sysmon (ID 1), and PowerShell (ID 4103, 4104).
    
    - **Effort:** intermediate

??? abstract "Invoke-TheHash Commandlets"
    
    Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.
    
    - **Effort:** elementary

??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate

??? abstract "Koadic MSHTML Command"
    
    Detects Koadic payload using MSHTML module
    
    - **Effort:** intermediate

??? abstract "Lazarus Loaders"
    
    Detects different loaders used by the Lazarus Group APT
    
    - **Effort:** elementary

??? abstract "Legitimate Process Execution From Unusual Folder"
    
    Detects the execution of a legitimate, windows built-in process name from an unusual / suspicious folder. Legitimate folders are c:\windows\system32\, \SystemRoot\system32\, c:\windows\syswow64\ and c:\windows\winsxs\. Many malwares/attackers use legitimate names to masquerade but if they are not Administrator yet, they often can't write file into these legitimate folders.
    
    - **Effort:** advanced

??? abstract "Leviathan Registry Key Activity"
    
    Detects registry key used by Leviathan APT in Malaysian focused campaign.
    
    - **Effort:** elementary

??? abstract "Linux Bash Reverse Shell"
    
    To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using shell commands
    
    - **Effort:** intermediate

??? abstract "Linux Shared Lib Injection Via Ldso Preload"
    
    Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process
    
    - **Effort:** intermediate

??? abstract "Listing Systemd Environment"
    
    Detects a listing of systemd environment variables. This command could be used to do reconnaissance on a compromised host.
    
    - **Effort:** advanced

??? abstract "Login Brute-Force Successful On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.
    
    - **Effort:** master

??? abstract "Login Failed Brute-Force On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.
    
    - **Effort:** master

??? abstract "Logon Scripts (UserInitMprLogonScript)"
    
    Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.
    
    - **Effort:** advanced

??? abstract "MS Office Product Spawning Exe in User Dir"
    
    Detects an executable in the users directory started from Microsoft Word, Excel, Powerpoint, Publisher or Visio. This is a common technique used by attackers with documents embedding macros. It requires Windows command line logging events.
    
    - **Effort:** master

??? abstract "Malicious Browser Extensions"
    
    Detects browser extensions being loaded with the --load-extension and -base-url options, which works on Chromium-based browsers. We are looking for potentially malicious browser extensions. These extensions can get access to informations.
    
    - **Effort:** advanced

??? abstract "Malspam Execution Registering Malicious DLL"
    
    Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).
    
    - **Effort:** elementary

??? abstract "Malware Persistence Registry Key"
    
    Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.
    
    - **Effort:** master

??? abstract "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate

??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Disable Services"
    
    The rule detects attempts to deactivate/disable Windows Defender through command line and registry.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Disable Using Registry"
    
    The rule detects attempts to deactivate/disable Microsoft Defender Antivirus using registry modification via command line or PowerShell scripts.
    
    - **Effort:** master

??? abstract "Microsoft Defender Antivirus Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line or scripts.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus History Directory Deleted"
    
    Windows Defender history directory has been deleted. This could be an attempt by an attacker to remove its traces.
    
    - **Effort:** elementary

??? abstract "Microsoft Defender Antivirus Restoration Abuse"
    
    The rule detects attempts to abuse Windows Defender file restoration tool. The Windows Defender process is allowed to write files in its own protected directory. This functionality can be used by a threat actor to overwrite Windows Defender files in order to prevent it from running correctly or use Windows Defender to execute a malicious DLL.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender through command line or PowerShell scripts. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Signatures Removed With MpCmdRun"
    
    Detects attempts to remove Windows Defender Signatures using MpCmdRun legitimate Windows Defender executable. No signatures mean Windows Defender will be less effective (or completely useless depending on the option used).
    
    - **Effort:** elementary

??? abstract "Microsoft Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data"
    
    Detects PowerShell SnapIn command line or PowerShell script, often used with Get-Mailbox to export Exchange mailbox data.
    
    - **Effort:** intermediate

??? abstract "Microsoft Office Macro Security Registry Modifications"
    
    Detects registry changes allowing an attacker to make Microsoft Office products runs Macros without warning. Events are collected either from ETW/Sysmon/EDR depending of the integration.
    
    - **Effort:** master

??? abstract "Mimikatz Basic Commands"
    
    Detects Mimikatz most popular commands. 
    
    - **Effort:** elementary

??? abstract "Msdt (Follina) File Browse Process Execution"
    
    Detects various Follina vulnerability exploitation techniques. This is based on the Compatability Troubleshooter which is abused to do code execution.
    
    - **Effort:** elementary

??? abstract "Mustang Panda Dropper"
    
    Detects specific process parameters as used by Mustang Panda droppers
    
    - **Effort:** elementary

??? abstract "NTDS.dit File In Suspicious Directory"
    
    The file NTDS.dit is supposed to be located mainly in C:\Windows\NTDS. The rule checks whether the file is in a legitimate directory or not (through file creation events). This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** advanced

??? abstract "NTDS.dit File Interaction Through Command Line"
    
    Detects interaction with the file NTDS.dit through command line. This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** intermediate

??? abstract "NetSh Used To Disable Windows Firewall"
    
    Detects NetSh commands used to disable the Windows Firewall
    
    - **Effort:** intermediate

??? abstract "Netsh Allowed Python Program"
    
    Detects netsh command that performs modification on Firewall rules to allow the program python.exe. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate

??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** intermediate

??? abstract "Netsh RDP Port Forwarding"
    
    Detects netsh commands that configure a port forwarding of port 3389 used for RDP. This is commonly used by attackers during lateralization on windows environments.
    
    - **Effort:** elementary

??? abstract "Network Share Discovery"
    
    Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. File sharing over a Windows network occurs over the SMB protocol. This technique is frequently leveraged by threat actors such as APT32, APT41, Wizard Spider. But also, through the use of some malware such as Cobalt Strike, Empire, PlugX and Ramsay.
    
    - **Effort:** master

??? abstract "New DLL Added To AppCertDlls Registry Key"
    
    Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "Ngrok Process Execution"
    
    Detects possible Ngrok execution, which can be used by attacker for RDP tunneling.
    
    - **Effort:** intermediate

??? abstract "NjRat Registry Changes"
    
    Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.
    
    - **Effort:** master

??? abstract "Njrat Registry Values"
    
    Detects specifis registry values that are related to njRat usage.
    
    - **Effort:** intermediate

??? abstract "NlTest Usage"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. These command lines were observed in numerous attacks, but also sometimes from legitimate administrators for debugging purposes. The rule does not cover very basics commands but rather the ones that are interesting for attackers to gather information on a domain.
    
    - **Effort:** advanced

??? abstract "Non-Legitimate Executable Using AcceptEula Parameter"
    
    Detects accepteula in command line with non-legitimate executable name. Some attackers are masquerading SysInternals tools with decoy names to prevent detection.
    
    - **Effort:** advanced

??? abstract "Office Application Startup Office Test"
    
    Detects the addition of office test registry that allows a user to specify an arbitrary DLL that will be executed everytime an Office application is started. An adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system.
    
    - **Effort:** elementary

??? abstract "OneNote Embedded File"
    
    Detects creation or uses of OneNote embedded files with unusual extensions.  
    
    - **Effort:** intermediate

??? abstract "OneNote Suspicious Children Process"
    
    In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.
    
    - **Effort:** advanced

??? abstract "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** master

??? abstract "Pandemic Windows Implant"
    
    Detects Pandemic Windows Implant through registry keys or specific command lines. Prerequisites: Logging for Registry events is needed, which can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "Phorpiex DriveMgr Command"
    
    Detects specific command used by the Phorpiex botnet to execute a copy of the loader during its self-spreading stage. As described by Microsoft, this behavior is unique and easily identifiable due to the use of folders named with underscores "__" and the PE name "DriveMgr.exe".
    
    - **Effort:** elementary

??? abstract "Phorpiex Process Masquerading"
    
    Detects specific process executable path used by the Phorpiex botnet to masquerade its system process network activity. It looks for a pattern of a system process executable name that is not legitimate and running from a folder that is created via a random algorithm 13-15 numbers long.
    
    - **Effort:** elementary

??? abstract "Possible Malicious File Double Extension"
    
    Detects request to potential malicious file with double extension
    
    - **Effort:** elementary

??? abstract "PowerCat Function Loading"
    
    Detect a basic execution of PowerCat. PowerCat is a PowerShell function allowing to do basic connections, file transfer, shells, relays, generate payloads.
    
    - **Effort:** intermediate

??? abstract "PowerShell AMSI Deactivation Bypass Using .NET Reflection"
    
    Detects Request to amsiInitFailed that can be used to disable AMSI (Antimalware Scan Interface) Scanning. More information about Antimalware Scan Interface https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal.
    
    - **Effort:** advanced

??? abstract "PowerShell Commands Invocation"
    
    Detects the execution to invoke a powershell command. This was used in an intrusion using Gootloader to access Mimikatz.
    
    - **Effort:** advanced

??? abstract "PowerShell Data Compressed"
    
    Detects data compression through a PowerShell command (could be used by an adversary for exfiltration).
    
    - **Effort:** advanced

??? abstract "PowerShell EncodedCommand"
    
    Detects popular file extensions in commands obfuscated in base64 run through the EncodedCommand option.
    
    - **Effort:** advanced

??? abstract "PowerShell Invoke Expression With Registry"
    
    Detects keywords from well-known PowerShell techniques to get registry key values
    
    - **Effort:** advanced

??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced

??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced

??? abstract "Powershell AMSI Bypass"
    
    This rule aims to detect attempts to bypass AMSI in powershell using specific techniques.
    
    - **Effort:** advanced

??? abstract "Powershell UploadString Function"
    
    Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host.
    
    - **Effort:** intermediate

??? abstract "Powershell Web Request"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell.
    
    - **Effort:** advanced

??? abstract "Privilege Escalation Awesome Scripts (PEAS)"
    
    Detect PEAS privileges escalation scripts and binaries
    
    - **Effort:** elementary

??? abstract "Process Memory Dump Using Comsvcs"
    
    Detects the use of comsvcs in command line to dump a specific process memory. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** intermediate

??? abstract "Process Memory Dump Using Rdrleakdiag"
    
    Detects the use of rdrleakdiag.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary

??? abstract "Process Trace Alteration"
    
    PTrace syscall provides a means by which one process ("tracer") may observe and control the execution of another process ("tracee") and examine and change the tracee's memory and registers. Attacker might want to abuse ptrace functionnality to analyse memory process. It requires to be admin or set ptrace_scope to 0 to allow all user to trace any process.
    
    - **Effort:** advanced

??? abstract "ProxyShell Microsoft Exchange Suspicious Paths"
    
    Detects suspicious calls to Microsoft Exchange resources, in locations related to webshells observed in campaigns using this vulnerability.
    
    - **Effort:** elementary

??? abstract "PsExec Process"
    
    Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 
    
    - **Effort:** advanced

??? abstract "Python HTTP Server"
    
    Detects command used to start a Simple HTTP server in Python. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate

??? abstract "QakBot Process Creation"
    
    Detects QakBot like process executions
    
    - **Effort:** intermediate

??? abstract "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate

??? abstract "RSA SecurID Failed Authentification"
    
    Detects many failed attempts to authenticate followed by a successfull login for a super admin account.
    
    - **Effort:** advanced

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "Raccine Uninstall"
    
    Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.
    
    - **Effort:** elementary

??? abstract "Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL"
    
    Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.
    
    - **Effort:** elementary

??? abstract "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced

??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate

??? abstract "RedMimicry Winnti Playbook Registry Manipulation"
    
    Detects actions caused by the RedMimicry Winnti playbook. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
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

??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "SOCKS Tunneling Tool"
    
    Detects the usage of a SOCKS tunneling tool, often used by threat actors. These tools often use the socks5 commandline argument, however socks4 can sometimes be used as well. Unfortunately, socks alone (without any number) triggered too many false positives. 
    
    - **Effort:** intermediate

??? abstract "STRRAT Scheduled Task"
    
    Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'
    
    - **Effort:** intermediate

??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Agent Disabled"
    
    A SentinelOne EDR agent has been disabled according to SentinelOne logs.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Custom Rule Alert"
    
    A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively"
    
    A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Malicious Threat Not Mitigated"
    
    A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR SSO User Added"
    
    A SSO User was added.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Detected (Malicious)"
    
    A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Detected (Suspicious)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Mitigation Report Kill Success"
    
    A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Failed"
    
    A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Success"
    
    A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR Threat Mitigation Report Remediate Success"
    
    A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.
    
    - **Effort:** master

??? abstract "SentinelOne EDR User Failed To Log In To The Management Console"
    
    A user has failed to log in to the management console.
    
    - **Effort:** master

??? abstract "SentinelOne EDR User Logged In To The Management Console"
    
    A user has logged in to the management console.
    
    - **Effort:** master

??? abstract "Socat Relaying Socket"
    
    Socat is a linux tool used to relay local socket or internal network connection, this technics is often used by attacker to bypass security equipment such as firewall
    
    - **Effort:** advanced

??? abstract "Socat Reverse Shell Detection"
    
    Socat is a linux tool used to relay or open reverse shell that is often used by attacker to bypass security equipment.
    
    - **Effort:** intermediate

??? abstract "SolarWinds Wrong Child Process"
    
    Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.
    
    - **Effort:** intermediate

??? abstract "Spyware Persistence Using Schtasks"
    
    Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).
    
    - **Effort:** intermediate

??? abstract "SquirrelWaffle Malspam Execution Loading DLL"
    
    Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.
    
    - **Effort:** intermediate

??? abstract "Stop Backup Services"
    
    Detects adversaries attempts to stop backups services or disable Windows previous files versions feature. This could be related to ransomware operators or legit administrators. This rule relies Windows command line logging and registry logging, and PowerShell (ID 4103, 4104).
    
    - **Effort:** master

??? abstract "Suncrypt Parameters"
    
    Detects SunCrypt ransomware's parameters, most of which are unique.
    
    - **Effort:** elementary

??? abstract "Suspicious ADSI-Cache Usage By Unknown Tool"
    
    Detects the usage of ADSI (LDAP) operations by tools. This may also detect tools like LDAPFragger. It needs file monitoring capabilities (Sysmon Event ID 11 with .sch file creation logging).
    
    - **Effort:** advanced

??? abstract "Suspicious Cmd File Copy Command To Network Share"
    
    Copy suspicious files through Windows cmd prompt to network share
    
    - **Effort:** intermediate

??? abstract "Suspicious Cmd.exe Command Line"
    
    Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.
    
    - **Effort:** master

??? abstract "Suspicious CommandLine Lsassy Pattern"
    
    Detects the characteristic lsassy loop used to identify lsass PIDs
    
    - **Effort:** intermediate

??? abstract "Suspicious DLL Loading By Ordinal"
    
    Detects suspicious DLL Loading by ordinal number in a non legitimate or rare folders. For example, Sofacy (APT28) used this technique to load their Trojan in a campaign of 2018.
    
    - **Effort:** intermediate

??? abstract "Suspicious Desktopimgdownldr Execution"
    
    Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.
    
    - **Effort:** intermediate

??? abstract "Suspicious Download Links From Legitimate Services"
    
    Detects users clicking on Google docs links to download suspicious files. This technique was used a lot by Bazar Loader in the past.
    
    - **Effort:** intermediate

??? abstract "Suspicious File Name"
    
    Detects suspicious file name possibly linked to malicious tool.
    
    - **Effort:** advanced

??? abstract "Suspicious Microsoft Defender Antivirus Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master

??? abstract "Suspicious Netsh DLL Persistence"
    
    Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
    
    - **Effort:** elementary

??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? abstract "Suspicious PowerShell Invocations - Generic"
    
    Detects suspicious PowerShell invocation command parameters through command line logging or ScriptBlock Logging.
    
    - **Effort:** intermediate

??? abstract "Suspicious PowerShell Invocations - Specific"
    
    Detects suspicious PowerShell invocation command parameters.
    
    - **Effort:** intermediate

??? abstract "Suspicious PowerShell Keywords"
    
    Detects keywords that could indicate the use of some PowerShell exploitation framework.
    
    - **Effort:** advanced

??? abstract "Suspicious PrinterPorts Creation (CVE-2020-1048)"
    
    Detects new commands that add new printer port which point to suspicious file
    
    - **Effort:** advanced

??? abstract "Suspicious Process Requiring DLL Starts Without DLL"
    
    Detects potential process injection and hollowing on processes that usually require a DLL to be launched, but are launched without any argument. 
    
    - **Effort:** intermediate

??? abstract "Suspicious Scheduled Task Creation"
    
    Detects suspicious scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 
    
    - **Effort:** intermediate

??? abstract "Suspicious TOR Gateway"
    
    Detects suspicious TOR gateways. Gateways are often used by the victim to pay and decrypt the encrypted files without installing TOR. Tor intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** advanced

??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate

??? abstract "Suspicious URI Used In A Lazarus Campaign"
    
    Detects suspicious requests to a specific URI, usually on an .asp page. The website is often compromised.
    
    - **Effort:** intermediate

??? abstract "Suspicious Windows Installer Execution"
    
    Detects suspicious execution of the Windows Installer service (msiexec.exe) which could be used to install a malicious MSI package hosted on a remote server.
    
    - **Effort:** intermediate

??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate

??? abstract "Suspicious desktop.ini Action"
    
    Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.
    
    - **Effort:** advanced

??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? abstract "UAC Bypass Via Sdclt"
    
    Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)
    
    - **Effort:** elementary

??? abstract "Usage Of Procdump With Common Arguments"
    
    Detects the usage of Procdump sysinternals tool with some common arguments and followed by common patterns.
    
    - **Effort:** intermediate

??? abstract "Usage Of Sysinternals Tools"
    
    Detects the usage of Sysinternals Tools due to accepteula key being added to Registry. The rule detects it either from the command line usage or from the regsitry events. For the later prerequisite is logging for registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "Venom Multi-hop Proxy agent detection"
    
    Detects Venom Multi-hop Proxy agent.
    
    - **Effort:** intermediate

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate

??? abstract "WMI Fingerprint Commands"
    
    Detects attacker fingerprint activities based on the correlation of specific WMIC commands. This has been observed with Aurora malware.
    
    - **Effort:** intermediate

??? abstract "WMI Install Of Binary"
    
    Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.
    
    - **Effort:** elementary

??? abstract "WMIC Command To Determine The Antivirus"
    
    Detects WMIC command to determine the antivirus on a system, characteristic of the ZLoader malware (and possibly others)
    
    - **Effort:** advanced

??? abstract "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate

??? abstract "WMImplant Hack Tool"
    
    WMImplant is a powershell framework used by attacker for reconnaissance and exfiltration, this rule attempts to detect WMimplant arguments and invokes commands. 
    
    - **Effort:** intermediate

??? abstract "Wdigest Enable UseLogonCredential"
    
    Detects modification of the Windows Registry value of HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential. This technique is used to extract passwords in clear-text using WDigest. The rule requires to log for Registry Events, which can be done using Sysmon Event IDs 12, 13 and 14.
    
    - **Effort:** elementary

??? abstract "Webshell Creation"
    
    Detects possible webshell file creation. It requires File Creation monitoring, which can be done using Sysmon's Event ID 11. However the recommended SwiftOnSecurity configuration does not fully cover the needs for this rule, it needs to be updated with the proper file names extensions.
    
    - **Effort:** master

??? abstract "WiFi Credentials Harvesting Using Netsh"
    
    Detects the harvesting of WiFi credentials using netsh.exe.
    
    - **Effort:** advanced

??? abstract "Windows Firewall Changes"
    
    Detects changes on Windows Firewall configuration
    
    - **Effort:** master

??? abstract "Windows Registry Persistence COM Key Linking"
    
    Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.
    
    - **Effort:** master

??? abstract "Wmic Process Call Creation"
    
    The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.
    
    - **Effort:** intermediate

??? abstract "Wmic Service Call"
    
    Detects either remote or local code execution using wmic tool.
    
    - **Effort:** intermediate

??? abstract "XCopy Suspicious Usage"
    
    Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.
    
    - **Effort:** advanced

??? abstract "ZIP LNK Infection Chain"
    
    Detection of an ZIP download followed by a child-process of explorer, followed by multiple Windows processes.This is widely used as an infection chain mechanism.
    
    - **Effort:** advanced
