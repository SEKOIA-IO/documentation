## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Sophos Analysis Threat Center [BETA]** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Sophos Analysis Threat Center [BETA] on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_99da26fc-bf7b-4e5b-a76c-408472fcfebb_do_not_edit_manually.json){ .md-button }
??? abstract "AccCheckConsole Executing Dll"
    
    Detects suspicious LOLBIN AccCheckConsole execution with parameters as used to load an arbitrary DLL.
    
    - **Effort:** advanced

??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? abstract "Add User to Privileged Group"
    
    Add user in a potential privileged group which can be used to elevate privileges on the system
    
    - **Effort:** advanced

??? abstract "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate

??? abstract "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
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
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner)
    
    - **Effort:** intermediate

??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate

??? abstract "Capture a network trace with netsh.exe"
    
    Detects capture a network trace via netsh.exe trace functionality
    
    - **Effort:** intermediate

??? abstract "CertOC Loading Dll"
    
    Detects when a user installs certificates by using CertOC.exe to loads the target DLL file.
    
    - **Effort:** intermediate

??? abstract "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master

??? abstract "Change Default File Association"
    
    When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.
    
    - **Effort:** advanced

??? abstract "Clear EventLogs Through CommandLine"
    
    Detects a command that clears event logs which could indicate an attempt from an attacker to erase its previous traces.
    
    - **Effort:** intermediate

??? abstract "Cmd.exe Used To Run Reconnaissance Commands"
    
    Detects command lines with suspicious args
    
    - **Effort:** advanced

??? abstract "Cmdkey Cached Credentials Recon"
    
    Detects usage of cmdkey to look for cached credentials.
    
    - **Effort:** intermediate

??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate

??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced

??? abstract "Copying Browser Files With Credentials"
    
    Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.
    
    - **Effort:** elementary

??? abstract "Copying Sensitive Files With Credential Data"
    
    Detects copy of files with well-known filenames (sensitive files with credential data) using esentutl. This requires Windows Security event log with the Detailed File Share logging policy enabled.
    
    - **Effort:** elementary

??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate

??? abstract "DNS Tunnel Technique From MuddyWater"
    
    Detecting DNS Tunnel Activity For Muddywater intrusion set. This is the loading of a specific DLL from an Excel macro which is detected.
    
    - **Effort:** elementary

??? abstract "Data Compressed With Rar"
    
    An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program.
    
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

??? abstract "Disable .NET ETW Through COMPlus_ETWEnabled"
    
    Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.
    
    - **Effort:** intermediate

??? abstract "Disable Task Manager Through Registry Key"
    
    Detects commands used to disable the Windows Task Manager by modifying the proper registry key in order to impair security tools. This technique is used by the Agent Tesla RAT, among others.
    
    - **Effort:** elementary

??? abstract "Disable Workstation Lock"
    
    Registry change in order to disable the ability to lock the computer by using CTRL+ALT+DELETE or CTRL+L. This registry key does not exist by default. Its creation is suspicious and the value set to "1" means an activation. It has been used by FatalRAT, but other attacker/malware could probably use it. This rule needs Windows Registry changes (add,modification,deletion) logging which can be done through Sysmon Event IDs 12,13,14.
    
    - **Effort:** elementary

??? abstract "Disabled IE Security Features"
    
    Detects from the command lines or the registry, changes that indicate unwanted modifications to registry keys that disable important Internet Explorer security features. This has been used by attackers during Operation Ke3chang.
    
    - **Effort:** advanced

??? abstract "Domain Group And Permission Enumeration"
    
    Detects adversaries attempts to find domain-level groups and permission settings. Commands such as net group /domain of the Net utility can list domain-level groups The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Wizard Spider, FIN6, and other groups used net in their campaigns.
    
    - **Effort:** advanced

??? abstract "Domain Trust Discovery Through LDAP"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. "trustedDomain" which is detected here is a Microsoft Active Directory ObjectClass Type that represents a domain that is trusted by, or trusting, the local AD DOMAIN. Several tools are using LDAP queries in the end to get the information (DSQuery, sometimes ADFind as well, etc.)
    
    - **Effort:** elementary

??? abstract "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** advanced

??? abstract "ETW Tampering"
    
    Detects a command that clears or disables any ETW Trace log which could indicate a logging evasion
    
    - **Effort:** intermediate

??? abstract "Elise Backdoor"
    
    Detects Elise backdoor activity as used by Lotus Blossom
    
    - **Effort:** elementary

??? abstract "Empire Monkey Activity"
    
    Detects EmpireMonkey APT reported Activity
    
    - **Effort:** elementary

??? abstract "Equation Group DLL_U Load"
    
    Detects a specific tool and export used by EquationGroup
    
    - **Effort:** elementary

??? abstract "Erase Shell History"
    
    Malware and attacker try to reduce their fingerprints on compromised host by deleting shell history
    
    - **Effort:** advanced

??? abstract "Exchange Mailbox Export"
    
    Detection of a standard Exchange Mailbox export, which stores all mails from a user in a pst file.
    
    - **Effort:** intermediate

??? abstract "Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data"
    
    Detects PowerShell SnapIn command line, often used with Get-Mailbox to export Exchange mailbox data.
    
    - **Effort:** intermediate

??? abstract "Exchange Server Spawning Suspicious Processes"
    
    Look for Microsoft Exchange Server’s Unified Messaging service spawning suspicious sub-processes, suggesting exploitation of CVE-2021-26857 vulnerability.
    
    - **Effort:** intermediate

??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? abstract "Exfiltration Domain In Command Line"
    
    Detects commands containing a domain linked to http exfiltration.
    
    - **Effort:** intermediate

??? abstract "Exploit For CVE-2015-1641"
    
    Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641
    
    - **Effort:** elementary

??? abstract "Exploit For CVE-2017-0261 Or CVE-2017-0262"
    
    Detects Winword starting uncommon sub process FLTLDR.exe as used in exploits for CVE-2017-0261 and CVE-2017-0262. This is a very basic detection method relying on the rare usage of EPS files from Winword.
    
    - **Effort:** advanced

??? abstract "Explorer Process Executing HTA File"
    
    Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.
    
    - **Effort:** intermediate

??? abstract "Explorer Wrong Parent"
    
    Detects suspicious spawning of explorer.exe process created by the rundll32.exe or regsvr32.exe. This behaviour is abnormal. Malware injecting itself into the explorer.exe process is quite common, in order to evade process-based defenses.
    
    - **Effort:** elementary

??? abstract "Fail2ban Unban IP"
    
    An IP was ubaned by Fail2ban. It could be use to allow malicous traffic.
    
    - **Effort:** advanced

??? abstract "File Or Folder Permissions Modifications"
    
    Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.
    
    - **Effort:** master

??? abstract "FlowCloud Malware"
    
    Detects FlowCloud malware from threat group TA410. This requires Windows Event registry logging.
    
    - **Effort:** elementary

??? abstract "Grabbing Sensitive Hives Via Reg Utility"
    
    Detects dump of SAM, System or Security hives using reg.exe utility. Adversaries may attempt to dump these Windows Registry to retrieve password hashes and access credentials.
    
    - **Effort:** intermediate

??? abstract "HackTools Suspicious Process Names In Command Line"
    
    Detects the default process name of several HackTools and also check in command line. This rule is here for quickwins as it obviously has many blind spots.
    
    - **Effort:** intermediate

??? abstract "Hiding Files With Attrib.exe"
    
    Detects usage of attrib.exe to hide files from users.
    
    - **Effort:** advanced

??? abstract "High Privileges Network Share Removal"
    
    Detects high privileges shares being deleted with the net share command.
    
    - **Effort:** intermediate

??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate

??? abstract "ICacls Granting Access To All"
    
    Detects suspicious icacls command granting access to all, used by the ransomware Ryuk to delete every access-based restrictions on files and directories. ICacls is a built-in Windows command to interact with the Discretionary Access Control Lists (DACLs) which can grand adversaries higher permissions on specific files and folders.
    
    - **Effort:** elementary

??? abstract "IIS Module Installation Using AppCmd"
    
    Detects the installation of a new IIS module from the command line. It can used used to backdoor an IIS/OWA/Sharepoint server.
    
    - **Effort:** intermediate

??? abstract "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary

??? abstract "Impacket Wmiexec Module"
    
    Detection of impacket's wmiexec example, used by attackers to execute commands remotely.
    
    - **Effort:** elementary

??? abstract "Inhibit System Recovery Deleting Backups"
    
    Detects adversaries attempts to delete backups or inhibit system recovery. This rule relies on differents known techniques using Windows events logs from Sysmon (ID 1), and PowerShell (ID 4103, 4104).
    
    - **Effort:** intermediate

??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate

??? abstract "Kernel Module Alteration"
    
    Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems.
    
    - **Effort:** advanced

??? abstract "Koadic Execution"
    
    Detects command line parameters used by Koadic hack tool
    
    - **Effort:** intermediate

??? abstract "Lazarus Loaders"
    
    Detects different loaders used by the Lazarus Group APT
    
    - **Effort:** elementary

??? abstract "Leviathan Registry Key Activity"
    
    Detects registry key used by Leviathan APT in Malaysian focused campaign.
    
    - **Effort:** elementary

??? abstract "List Shadow Copies"
    
    Detects command line used to list shadow copies. An adversary may attempt to get information on shadow volumes to perform deletion or extract password hashes from the ntds.dit file. This rule requires command line logging or Windows PowerShell events (4104).
    
    - **Effort:** master

??? abstract "Listing Systemd Environment"
    
    Detects a listing of systemd environment variables. This command could be used to do reconnaissance on a compromised host.
    
    - **Effort:** elementary

??? abstract "MMC Spawning Windows Shell"
    
    Detects a Windows command line executable started from MMC process
    
    - **Effort:** intermediate

??? abstract "MMC20 Lateral Movement"
    
    Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe.
    
    - **Effort:** intermediate

??? abstract "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate

??? abstract "MSBuild Abuse"
    
    Detection of MSBuild uses by attackers to infect an host. Focuses on XML compilation which is a Metasploit payload, and on connections made by this process which is unusual.
    
    - **Effort:** intermediate

??? abstract "Malicious Browser Extensions"
    
    Detects browser extensions being loaded with the --load-extension and -base-url options, which works on Chromium-based browsers. We are looking for potentially malicious browser extensions. These extensions can get access to informations.
    
    - **Effort:** advanced

??? abstract "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate

??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate

??? abstract "Meterpreter or Cobalt Strike Getsystem Service Installation"
    
    Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting some of the techniques being used (technique 1,2 and 5).
    
    - **Effort:** elementary

??? abstract "Microsoft Defender Antivirus Disable Scheduled Tasks"
    
    The rule detects attempts to deactivate/disable Windows Defender scheduled tasks via command line
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Disable Using Registry"
    
    The rule detects attempts to deactivate/disable Microsoft Defender Antivirus using registry modification via command line.
    
    - **Effort:** master

??? abstract "Microsoft Defender Antivirus Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line.
    
    - **Effort:** elementary

??? abstract "Microsoft Defender Antivirus History Directory Deleted"
    
    Windows Defender history directory has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** elementary

??? abstract "Microsoft Defender Antivirus Restoration Abuse"
    
    The rule detects attempts to abuse Windows Defender file restoration tool. The Windows Defender process is allowed to write files in its own protected directory. This functionality can be used by a threat actor to overwrite Windows Defender files in order to prevent it from running correctly or use Windows Defender to execute a malicious DLL.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender scan and updates. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate

??? abstract "Microsoft Defender Antivirus Signatures Removed With MpCmdRun"
    
    Detects attempts to remove Windows Defender Signatures using MpCmdRun legitimate Windows Defender executable. No signatures mean Windows Defender will be less effective (or completely useless depending on the option used).
    
    - **Effort:** elementary

??? abstract "Microsoft Office Product Spawning Windows Shell"
    
    Detects a Windows command or scripting interpreter executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware.
    
    - **Effort:** advanced

??? abstract "Microsoft Office Spawning Script"
    
    Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 
    
    - **Effort:** intermediate

??? abstract "Mshta JavaScript Execution"
    
    Identifies suspicious mshta.exe commands that execute JavaScript supplied as a command line argument.
    
    - **Effort:** elementary

??? abstract "Mshta Suspicious Child Process"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell
    
    - **Effort:** intermediate

??? abstract "NTDS.dit File Interaction Through Command Line"
    
    Detects interaction with the file NTDS.dit through command line. This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** intermediate

??? abstract "Net.exe User Account Creation"
    
    Identifies creation of local users via the net.exe command
    
    - **Effort:** master

??? abstract "NetSh Used To Disable Windows Firewall"
    
    Detects NetSh commands used to disable the Windows Firewall
    
    - **Effort:** intermediate

??? abstract "Netsh Allow Command"
    
    Netsh command line to allow a program to pass through firewall.
    
    - **Effort:** advanced

??? abstract "Netsh Allowed Python Program"
    
    Detects netsh command that performs modification on Firewall rules to allow the program python.exe. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate

??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** elementary

??? abstract "Netsh Port Opening"
    
    Detects netsh commands that opens a specific port. Can be used by malware or attackers for lateralisation/exfiltration (e.g. SMB/RDP opening).
    
    - **Effort:** master

??? abstract "Netsh RDP Port Forwarding"
    
    Detects netsh commands that configure a port forwarding of port 3389 used for RDP. This is commonly used by attackers during lateralization on windows environments.
    
    - **Effort:** elementary

??? abstract "Netsh RDP Port Opening"
    
    Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent Malware
    
    - **Effort:** intermediate

??? abstract "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate

??? abstract "New DLL Added To AppCertDlls Registry Key"
    
    Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "New Service Creation"
    
    Detects creation of a new service from command line
    
    - **Effort:** advanced

??? abstract "Ngrok Process Execution"
    
    Detects possible Ngrok execution, which can be used by attacker for RDP tunneling. 
    
    - **Effort:** intermediate

??? abstract "NlTest Usage"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. These command lines were observed in numerous attacks, but also sometimes from legitimate administrators for debugging purposes. The rule does not cover very basics commands but rather the ones that are interesting for attackers to gather information on a domain.
    
    - **Effort:** intermediate

??? abstract "Non-Legitimate Executable Using AcceptEula Parameter"
    
    Detects accepteula in command line with non-legitimate executable name. Some attackers are masquerading SysInternals tools with decoy names to prevent detection.
    
    - **Effort:** intermediate

??? abstract "OceanLotus Registry Activity"
    
    Detects registry keys created in OceanLotus (also known as APT32) attack. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "Opening Of a Password File"
    
    Command line detection of common office software opening some password related file. It could be a security breach if an unauthorized user access it.
    
    - **Effort:** advanced

??? abstract "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** elementary

??? abstract "Pandemic Windows Implant"
    
    Detects Pandemic Windows Implant through registry keys or specific command lines. Prerequisites: Logging for Registry events is needed, which can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "Phorpiex DriveMgr Command"
    
    Detects specific command used by the Phorpiex botnet to execute a copy of the loader during its self-spreading stage. As described by Microsoft, this behavior is unique and easily identifiable due to the use of folders named with underscores "__" and the PE name "DriveMgr.exe".
    
    - **Effort:** elementary

??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced

??? abstract "PowerCat Function Loading"
    
    Detect a basic execution of PowerCat. PowerCat is a PowerShell function allowing to do basic connections, file transfer, shells, relays, generate payloads.
    
    - **Effort:** intermediate

??? abstract "PowerShell AMSI Deactivation Bypass Using .NET Reflection"
    
    Detects Request to amsiInitFailed that can be used to disable AMSI (Antimalware Scan Interface) Scanning. More information about Antimalware Scan Interface https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal.
    
    - **Effort:** elementary

??? abstract "PowerShell Downgrade Attack"
    
    Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0
    
    - **Effort:** elementary

??? abstract "PowerShell Download From URL"
    
    Detects a Powershell process that contains download commands in its command line string
    
    - **Effort:** intermediate

??? abstract "PowerShell EncodedCommand"
    
    Detects popular file extensions in commands obfuscated in base64 run through the EncodedCommand option.
    
    - **Effort:** advanced

??? abstract "PowerShell Execution Via Rundll32"
    
    Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified
    
    - **Effort:** intermediate

??? abstract "PowerShell Malicious Nishang PowerShell Commandlets"
    
    Detects Commandlet names and arguments from the Nishang exploitation framework
    
    - **Effort:** advanced

??? abstract "Powershell UploadString Function"
    
    Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host. 
    
    - **Effort:** intermediate

??? abstract "Powershell Web Request"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell
    
    - **Effort:** advanced

??? abstract "Process Memory Dump Using Comsvcs"
    
    Detects the use of comsvcs in command line to dump a specific proces memory. This techinique is widlely used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary

??? abstract "Process Memory Dump Using Rdrleakdiag"
    
    Detects the use of rdrleakdiag.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary

??? abstract "Process Trace Alteration"
    
    PTrace syscall provides a means by which one process ("tracer") may observe and control the execution of another process ("tracee") and examine and change the tracee's memory and registers. Attacker might want to abuse ptrace functionnality to analyse memory process. It requires to be admin or set ptrace_scope to 0 to allow all user to trace any process.
    
    - **Effort:** advanced

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

??? abstract "RDP Sensitive Settings Changed"
    
    Detects changes to RDP terminal service sensitive settings. Logging for registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** advanced

??? abstract "RDP Session Discovery"
    
    Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.
    
    - **Effort:** advanced

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "Raccine Uninstall"
    
    Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.
    
    - **Effort:** elementary

??? abstract "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced

??? abstract "RedMimicry Winnti Playbook Registry Manipulation"
    
    Detects actions caused by the RedMimicry Winnti playbook. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary

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

??? abstract "Schtasks Persistence With High Privileges"
    
    Detection of scheduled task with high privileges used by attacker for persistence.
    
    - **Effort:** elementary

??? abstract "Schtasks Suspicious Parent"
    
    Detects schtasks started from suspicious and/or unusual processes.
    
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

??? abstract "Sticky Key Like Backdoor Usage"
    
    Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** elementary

??? abstract "Suncrypt Parameters"
    
    Detects SunCrypt ransomware's parameters, most of which are unique.
    
    - **Effort:** elementary

??? abstract "Suspicious Cmd File Copy Command To Network Share"
    
    Copy suspicious files through Windows cmd prompt to network share
    
    - **Effort:** intermediate

??? abstract "Suspicious Cmd.exe Command Line"
    
    Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.
    
    - **Effort:** advanced

??? abstract "Suspicious Commands From MS SQL Server Shell"
    
    Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.
    
    - **Effort:** intermediate

??? abstract "Suspicious Control Process"
    
    Detects suspicious execution of control.exe process when used to execute a DLL file.
    
    - **Effort:** advanced

??? abstract "Suspicious DLL Loading By Ordinal"
    
    Detects suspicious DLL Loading by ordinal number in a non legitimate or rare folders. For example, Sofacy (APT28) used this technique to load their Trojan in a campaign of 2018.
    
    - **Effort:** intermediate

??? abstract "Suspicious DNS Child Process"
    
    Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).
    
    - **Effort:** intermediate

??? abstract "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** elementary

??? abstract "Suspicious Driver Loaded"
    
    Checks the registry key for suspicious driver names that are vulnerable most of the time and loaded in a specific location by the KDU tool from hfiref0x. Some drivers are used by several SysInternals tools, which should have been whitelisted in the filter condition. The driver named "DBUtilDrv2" has been removed as it caused too many false positives unfortunately. It can be added under "drv_name" if more coverage is wanted. This rule needs registry key monitoring (can be done with Sysmon Event IDs 12,13 and 14).
    
    - **Effort:** intermediate

??? abstract "Suspicious Finger Usage"
    
    Detects suspicious aged finger.exe tool execution often used in malware attacks nowadays. An attacker can use finger to silently retrieve a command, a script or a payload from a remote server. For example, the tool Darkfinger-C2 uses this technique to download files from the C2 channel.
    
    - **Effort:** intermediate

??? abstract "Suspicious HWP Child Process"
    
    Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.
    
    - **Effort:** elementary

??? abstract "Suspicious Headless Web Browser Execution To Download File"
    
    Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.
    
    - **Effort:** elementary

??? abstract "Suspicious Microsoft Defender Antivirus Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master

??? abstract "Suspicious Mshta Execution"
    
    Detects suspicious mshta.exe execution patterns, either involving file polyglotism, remote file (http, ftp or ldap) or suspicious location. This technique is often used by threat actors.
    
    - **Effort:** intermediate

??? abstract "Suspicious Mshta Execution From Wmi"
    
    Detects mshta executed by wmiprvse as parent. It has been used by TA505 with some malicious documents.
    
    - **Effort:** intermediate

??? abstract "Suspicious Netsh DLL Persistence"
    
    Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
    
    - **Effort:** elementary

??? abstract "Suspicious Network Args In Command Line"
    
    Detection on some commonly observed suspicious processes command lines using HTTP schema with port 443.
    
    - **Effort:** intermediate

??? abstract "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate

??? abstract "Suspicious PowerShell Invocations - Specific"
    
    Detects suspicious PowerShell invocation command parameters
    
    - **Effort:** intermediate

??? abstract "Suspicious PrinterPorts Creation (CVE-2020-1048)"
    
    Detects new commands that add new printer port which point to suspicious file
    
    - **Effort:** advanced

??? abstract "Suspicious Regsvr32 Execution"
    
    Detects suspicious regsvr32.exe executions, either regsvr32 registering a DLL in an unusual repository (temp/, appdata/ or public/), or regsvr32 executed by an unusual parent process, or regsvr32 executing an unusual process, or regsvr32 registering a media file and not a DLL (as seen in IcedID campaigns), or regsvr32 registering a ocx file in appdata/.
    
    - **Effort:** intermediate

??? abstract "Suspicious Rundll32.exe Execution"
    
    The process rundll32.exe executes a newly dropped DLL with update /i in the command line. This specific technic was observed at least being used by the IcedID loading mechanism dubbed Gziploader.
    
    - **Effort:** intermediate

??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate

??? abstract "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary

??? abstract "Suspicious Windows Installer Execution"
    
    Detects suspicious execution of the Windows Installer service (msiexec.exe) which could be used to install a malicious MSI package hosted on a remote server.
    
    - **Effort:** intermediate

??? abstract "Suspicious Windows Script Execution"
    
    Detects wscript.exe or cscript.exe executing a script in user directories (C:\ProgramData or C:\Users) with a .txt extension, which is very suspicious. It could strongly correspond to a malware dropper, as seen during SquirrelWaffle maldoc campaign.
    
    - **Effort:** intermediate

??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate

??? abstract "Sysprep On AppData Folder"
    
    Detects suspicious Sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec). Sysprep is a Windows tool used to change Windows images from a generalized state to a specialized state, and then back to a generalized state. It can be used to remove all system-specific information and reset the computer.
    
    - **Effort:** intermediate

??? abstract "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host
    
    - **Effort:** master

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced

??? abstract "UAC Bypass Using Fodhelper"
    
    Detects UAC bypass method using Fodhelper after setting the proper registry key, used in particular by Agent Tesla (RAT) or more recently by Earth Luscas. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "UAC Bypass Via Sdclt"
    
    Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)
    
    - **Effort:** elementary

??? abstract "UAC Bypass via Event Viewer"
    
    Detects UAC bypass method using Windows event viewer. 
    
    - **Effort:** elementary

??? abstract "Ursnif Registry Key"
    
    Detects a new registry key created by Ursnif malware. The rule requires to log for Registry Events, which can be done using SYsmon's Event IDs 12,13 and 14.
    
    - **Effort:** elementary

??? abstract "Usage Of Procdump With Common Arguments"
    
    Detects the usage of Procdump sysinternals tool with some common arguments and followed by common patterns.
    
    - **Effort:** intermediate

??? abstract "Usage Of Sysinternals Tools"
    
    Detects the usage of Sysinternals Tools due to accepteula key being added to Registry. The rule detects it either from the command line usage or from the regsitry events. For the later prerequisite is logging for registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "WMI Install Of Binary"
    
    Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.
    
    - **Effort:** elementary

??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced

??? abstract "WMIC Command To Determine The Antivirus"
    
    Detects WMIC command to determine the antivirus on a system, characteristic of the ZLoader malware (and possibly others)
    
    - **Effort:** intermediate

??? abstract "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate

??? abstract "Webshell Execution W3WP Process"
    
    Detects possible webshell execution on Windows Servers which is usually a w3wp parent process with the user name DefaultAppPool.
    
    - **Effort:** advanced

??? abstract "WiFi Credentials Harvesting Using Netsh"
    
    Detects the harvesting of WiFi credentials using netsh.exe, used in particular by Agent Tesla (RAT) and Turla Mosquito (RAT)
    
    - **Effort:** elementary

??? abstract "Windows Credential Editor Registry Key"
    
    Detects the use of Windows Credential Editor (WCE). Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary

??? abstract "Windows Firewall Changes"
    
    Detects changes on Windows Firewall configuration
    
    - **Effort:** master

??? abstract "Windows Registry Persistence COM Key Linking"
    
    Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.
    
    - **Effort:** master

??? abstract "Windows Update LolBins"
    
    This rule try to detect a suspicious behavior of wuauclt.exe (windows update client) that could be a lolbins. Wuauctl.exe could be used to execute a malicious program.
    
    - **Effort:** elementary

??? abstract "Winword Document Droppers"
    
    Detects specific process characteristics of word document droppers. This techniques has been used by Maze ransomware operators.
    
    - **Effort:** elementary

??? abstract "Winword wrong parent"
    
    Word is a well known Windows process used to read documents. Some malicious process could use it to run malicious code. The rule tries to detect winword.exe launched with a suspect parent process name.
    
    - **Effort:** advanced

??? abstract "Wmic Process Call Creation"
    
    The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.
    
    - **Effort:** intermediate

??? abstract "Wmic Service Call"
    
    Detects either remote or local code execution using wmic tool.
    
    - **Effort:** intermediate

??? abstract "XCopy Suspicious Usage"
    
    Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.
    
    - **Effort:** advanced

??? abstract "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate

??? abstract "xWizard Execution"
    
    Detects the execution of Xwizard tool with specific arguments which utilized to run custom class properties.
    
    - **Effort:** master