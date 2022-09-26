## Suggested Built-in Rules

This integration enables the following built-in detection rules. Use the Rules Catalog to customize and adapt these to your security posture.


??? tip "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? tip "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate

??? tip "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
    - **Effort:** advanced

??? warning "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master

??? tip "BITSAdmin Download"
    
    Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.
    
    - **Effort:** advanced

??? tip "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate

??? tip "Capture a network trace with netsh.exe"
    
    Detects capture a network trace via netsh.exe trace functionality
    
    - **Effort:** intermediate

??? warning "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master

??? tip "Change Default File Association"
    
    When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.
    
    - **Effort:** advanced

??? tip "Clear EventLogs Through CommandLine"
    
    Detects a command that clears event logs which could indicate an attempt from an attacker to erase its previous traces.
    
    - **Effort:** intermediate

??? tip "Cmd.exe Used To Run Reconnaissance Commands"
    
    Detects command lines with suspicious args
    
    - **Effort:** advanced

??? tip "Cmdkey Cached Credentials Recon"
    
    Detects usage of cmdkey to look for cached credentials.
    
    - **Effort:** intermediate

??? tip "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate

??? tip "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced

??? tip "Copying Sensitive Files With Credential Data"
    
    Detects copy of files with well-known filenames (sensitive files with credential data) using esentutl. This requires Windows Security event log with the Detailed File Share logging policy enabled.
    
    - **Effort:** elementary

??? tip "DNS Tunnel Technique From MuddyWater"
    
    Detecting DNS Tunnel Activity For Muddywater intrusion set. This is the loading of a specific DLL from an Excel macro which is detected.
    
    - **Effort:** elementary

??? tip "Domain Group And Permission Enumeration"
    
    Detects adversaries attempts to find domain-level groups and permission settings. Commands such as net group /domain of the Net utility can list domain-level groups The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Wizard Spider, FIN6, and other groups used net in their campaigns.
    
    - **Effort:** advanced

??? tip "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** advanced

??? tip "ETW Tampering"
    
    Detects a command that clears or disables any ETW Trace log which could indicate a logging evasion
    
    - **Effort:** intermediate

??? tip "Elise Backdoor"
    
    Detects Elise backdoor activity as used by Lotus Blossom
    
    - **Effort:** elementary

??? tip "Empire Monkey Activity"
    
    Detects EmpireMonkey APT reported Activity
    
    - **Effort:** elementary

??? tip "Equation Group DLL_U Load"
    
    Detects a specific tool and export used by EquationGroup
    
    - **Effort:** elementary

??? tip "Erase Shell History"
    
    Malware and attacker try to reduce their fingerprints on compromised host by deleting shell history
    
    - **Effort:** advanced

??? tip "Exchange Server Spawning Suspicious Processes"
    
    Look for Microsoft Exchange Server’s Unified Messaging service spawning suspicious sub-processes, suggesting exploitation of CVE-2021-26857 vulnerability.
    
    - **Effort:** intermediate

??? tip "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? tip "Exploit For CVE-2015-1641"
    
    Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641
    
    - **Effort:** elementary

??? tip "Explorer Process Executing HTA File"
    
    Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.
    
    - **Effort:** intermediate

??? tip "Explorer Wrong Parent"
    
    Detects suspicious spawning of explorer.exe process created by the rundll32.exe or regsvr32.exe. This behaviour is abnormal. Malware injecting itself into the explorer.exe process is quite common, in order to evade process-based defenses.
    
    - **Effort:** elementary

??? warning "File Or Folder Permissions Modifications"
    
    Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.
    
    - **Effort:** master

??? tip "Formbook Hijacked Process Command"
    
    Detects process hijacked by Formbook malware which executes specific commands to delete the dropper or copy browser credentials to the database before sending them to the C2.
    
    - **Effort:** intermediate

??? tip "Gpscript Suspicious Parent"
    
    Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.
    
    - **Effort:** intermediate

??? tip "Grabbing Sensitive Hives Via Reg Utility"
    
    Detects dump of SAM, System or Security hives using reg.exe utility. Adversaries may attempt to dump these Windows Registry to retrieve password hashes and access credentials.
    
    - **Effort:** intermediate

??? tip "Hiding Files With Attrib.exe"
    
    Detects usage of attrib.exe to hide files from users.
    
    - **Effort:** advanced

??? tip "ICacls Granting Access To All"
    
    Detects suspicious icacls command granting access to all, used by the ransomware Ryuk to delete every access-based restrictions on files and directories. ICacls is a built-in Windows command to interact with the Discretionary Access Control Lists (DACLs) which can grand adversaries higher permissions on specific files and folders.
    
    - **Effort:** elementary

??? tip "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary

??? tip "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate

??? tip "Koadic Execution"
    
    Detects command line parameters used by Koadic hack tool
    
    - **Effort:** intermediate

??? tip "Lazarus Loaders"
    
    Detects different loaders used by the Lazarus Group APT
    
    - **Effort:** elementary

??? tip "MMC Spawning Windows Shell"
    
    Detects a Windows command line executable started from MMC process
    
    - **Effort:** intermediate

??? tip "MMC20 Lateral Movement"
    
    Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe.
    
    - **Effort:** intermediate

??? tip "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate

??? tip "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate

??? tip "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate

??? tip "Microsoft Office Product Spawning Windows Shell"
    
    Detects a Windows command or scripting interpreter executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware.
    
    - **Effort:** advanced

??? tip "Microsoft Office Spawning Script"
    
    Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 
    
    - **Effort:** intermediate

??? tip "Mshta JavaScript Execution"
    
    Identifies suspicious mshta.exe commands that execute JavaScript supplied as a command line argument.
    
    - **Effort:** elementary

??? tip "NTDS.dit File Interaction Through Command Line"
    
    Detects interaction with the file NTDS.dit through command line. This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** intermediate

??? warning "Net.exe User Account Creation"
    
    Identifies creation of local users via the net.exe command
    
    - **Effort:** master

??? tip "NetSh Used To Disable Windows Firewall"
    
    Detects NetSh commands used to disable the Windows Firewall
    
    - **Effort:** intermediate

??? tip "Netsh Allow Command"
    
    Netsh command line to allow a program to pass through firewall.
    
    - **Effort:** advanced

??? tip "Netsh Allowed Python Program"
    
    Detects netsh command that performs modification on Firewall rules to allow the program python.exe. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate

??? tip "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** elementary

??? warning "Netsh Port Opening"
    
    Detects netsh commands that opens a specific port. Can be used by malware or attackers for lateralisation/exfiltration (e.g. SMB/RDP opening).
    
    - **Effort:** master

??? tip "Netsh Program Allowed With Suspicious Location"
    
    Detects Netsh commands that allow a suspcious application location on Windows Firewall, seen on kasidet worm. Last part of the existing rule (commandline startwith) was not added to this rule because it is not relevant.
    
    - **Effort:** intermediate

??? tip "Netsh RDP Port Forwarding"
    
    Detects netsh commands that configure a port forwarding of port 3389 used for RDP. This is commonly used by attackers during lateralization on windows environments.
    
    - **Effort:** elementary

??? tip "Netsh RDP Port Opening"
    
    Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent Malware
    
    - **Effort:** intermediate

??? tip "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? tip "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? tip "NlTest Usage"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. These command lines were observed in numerous attacks, but also sometimes from legitimate administrators for debugging purposes. The rule does not cover very basics commands but rather the ones that are interesting for attackers to gather information on a domain.
    
    - **Effort:** intermediate

??? tip "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** elementary

??? tip "Phorpiex DriveMgr Command"
    
    Detects specific command used by the Phorpiex botnet to execute a copy of the loader during its self-spreading stage. As described by Microsoft, this behavior is unique and easily identifiable due to the use of folders named with underscores "__" and the PE name "DriveMgr.exe".
    
    - **Effort:** elementary

??? tip "PowerShell Downgrade Attack"
    
    Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0
    
    - **Effort:** elementary

??? tip "PowerShell Execution Via Rundll32"
    
    Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified
    
    - **Effort:** intermediate

??? tip "Powershell Web Request"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell
    
    - **Effort:** advanced

??? tip "Process Memory Dump Using Comsvcs"
    
    Detects the use of comsvcs in command line to dump a specific proces memory. This techinique is widlely used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary

??? tip "QakBot Process Creation"
    
    Detects QakBot like process executions
    
    - **Effort:** intermediate

??? tip "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate

??? tip "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? tip "Raccine Uninstall"
    
    Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.
    
    - **Effort:** elementary

??? tip "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced

??? tip "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced

??? tip "STRRAT Scheduled Task"
    
    Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'
    
    - **Effort:** intermediate

??? tip "Schtasks Persistence With High Privileges"
    
    Detection of scheduled task with high privileges used by attacker for persistence.
    
    - **Effort:** elementary

??? tip "Schtasks Suspicious Parent"
    
    Detects schtasks started from suspicious and/or unusual processes.
    
    - **Effort:** intermediate

??? tip "Spyware Persistence Using Schtasks"
    
    Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).
    
    - **Effort:** intermediate

??? tip "SquirrelWaffle Malspam Execution Loading DLL"
    
    Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.
    
    - **Effort:** intermediate

??? tip "Suspicious Cmd.exe Command Line"
    
    Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.
    
    - **Effort:** advanced

??? tip "Suspicious Commands From MS SQL Server Shell"
    
    Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.
    
    - **Effort:** intermediate

??? tip "Suspicious Control Process"
    
    Detects suspicious execution of control.exe process when used to execute a DLL file.
    
    - **Effort:** advanced

??? tip "Suspicious DLL Loading By Ordinal"
    
    Detects suspicious DLL Loading by ordinal number in a non legitimate or rare folders. For example, Sofacy (APT28) used this technique to load their Trojan in a campaign of 2018.
    
    - **Effort:** intermediate

??? tip "Suspicious DNS Child Process"
    
    Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).
    
    - **Effort:** intermediate

??? tip "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** elementary

??? tip "Suspicious Finger Usage"
    
    Detects suspicious aged finger.exe tool execution often used in malware attacks nowadays. An attacker can use finger to silently retrieve a command, a script or a payload from a remote server. For example, the tool Darkfinger-C2 uses this technique to download files from the C2 channel.
    
    - **Effort:** intermediate

??? tip "Suspicious HWP Child Process"
    
    Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.
    
    - **Effort:** elementary

??? tip "Suspicious Mshta Execution"
    
    Detects suspicious mshta.exe execution patterns, either involving file polyglotism, remote file (http, ftp or ldap) or suspicious location. This technique is often used by threat actors.
    
    - **Effort:** intermediate

??? tip "Suspicious Mshta Execution From Wmi"
    
    Detects mshta executed by wmiprvse as parent. It has been used by TA505 with some malicious documents.
    
    - **Effort:** intermediate

??? tip "Suspicious Netsh DLL Persistence"
    
    Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
    
    - **Effort:** elementary

??? tip "Suspicious Network Args In Command Line"
    
    Detection on suspicious network arguments in processes command lines using HTTP schema with port 443.
    
    - **Effort:** intermediate

??? tip "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate

??? tip "Suspicious PowerShell Invocations - Specific"
    
    Detects suspicious PowerShell invocation command parameters
    
    - **Effort:** intermediate

??? tip "Suspicious Regsvr32 Execution"
    
    Detects suspicious regsvr32.exe executions, either regsvr32 registering a DLL in an unusual repository (temp/, appdata/ or public/), or regsvr32 executed by an unusual parent process, or regsvr32 executing an unusual process, or regsvr32 registering a media file and not a DLL (as seen in IcedID campaigns), or regsvr32 registering a ocx file in appdata/.
    
    - **Effort:** intermediate

??? tip "Suspicious Rundll32.exe Execution"
    
    The process rundll32.exe executes a newly dropped DLL with update /i in the command line. This specific technic was observed at least being used by the IcedID loading mechanism dubbed Gziploader.
    
    - **Effort:** intermediate

??? tip "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate

??? tip "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary

??? tip "Suspicious Windows Installer Execution"
    
    Detects suspicious execution of the Windows Installer service (msiexec.exe) which could be used to install a malicious MSI package hosted on a remote server.
    
    - **Effort:** intermediate

??? tip "Suspicious Windows Script Execution"
    
    Detects wscript.exe or cscript.exe executing a script in user directories (C:\ProgramData or C:\Users) with a .txt extension, which is very suspicious. It could strongly correspond to a malware dropper, as seen during SquirrelWaffle maldoc campaign.
    
    - **Effort:** intermediate

??? tip "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate

??? tip "Sysprep On AppData Folder"
    
    Detects suspicious Sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec). Sysprep is a Windows tool used to change Windows images from a generalized state to a specialized state, and then back to a generalized state. It can be used to remove all system-specific information and reset the computer.
    
    - **Effort:** intermediate

??? warning "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host
    
    - **Effort:** master

??? tip "WMI Install Of Binary"
    
    Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.
    
    - **Effort:** elementary

??? tip "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate

??? tip "WiFi Credentials Harvesting Using Netsh"
    
    Detects the harvesting of WiFi credentials using netsh.exe, used in particular by Agent Tesla (RAT) and Turla Mosquito (RAT)
    
    - **Effort:** elementary

??? tip "Windows Defender History Directory Deleted"
    
    Windows Defender history directory has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** elementary

??? tip "Windows Defender Signatures Removed With MpCmdRun"
    
    Detects attempts to remove Windows Defender Signatures using MpCmdRun legitimate Windows Defender executable. No signatures mean Windows Defender will be less effective (or completely useless depending on the option used).
    
    - **Effort:** elementary

??? warning "Windows Firewall Changes"
    
    Detects changes on Windows Firewall configuration
    
    - **Effort:** master

??? tip "Windows Update LolBins"
    
    This rule try to detect a suspicious behavior of wuauclt.exe (windows update client) that could be a lolbins. Wuauctl.exe could be used to execute a malicious program.
    
    - **Effort:** elementary

??? tip "Winword Document Droppers"
    
    Detects specific process characteristics of word document droppers. This techniques has been used by Maze ransomware operators.
    
    - **Effort:** elementary

??? tip "Winword wrong parent"
    
    Word is a well known Windows process used to read documents. Some malicious process could use it to run malicious code. The rule tries to detect winword.exe launched with a suspect parent process name.
    
    - **Effort:** advanced

??? tip "Wmic Process Call Creation"
    
    The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.
    
    - **Effort:** intermediate

??? tip "XCopy Suspicious Usage"
    
    Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.
    
    - **Effort:** advanced

??? tip "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate
