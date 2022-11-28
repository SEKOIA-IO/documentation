## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Windows** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Windows on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_9281438c-f7c3-4001-9bcc-45fd108ba1be_do_not_edit_manually.json){ .md-button }
??? abstract "AD Object WriteDAC Access"
    
    Detects WRITE_DAC access to a domain object. This requires Windows Event ID 4662.
    
    - **Effort:** elementary

??? abstract "AD Privileged Users Or Groups Reconnaissance"
    
    Detect privileged users or groups reconnaissance based on 4661 Event ID and known privileged users or groups SIDs. If the user account name is not a known admin it is suspicious.
    
    - **Effort:** master

??? abstract "AD User Enumeration"
    
    Detects access to a domain user from a non-machine account. This requires Windows Security Event ID 4662 and could be triggered by some administrators configuring new users.
    
    - **Effort:** master

??? abstract "APT29 Fake Google Update Service Install"
    
    This method detects malicious services mentioned in APT29 report by FireEye. The legitimate path for the Google update service is C:\Program Files (x86)\Google\Update\GoogleUpdate.exe so the service names and executable locations used by APT29 are specific enough to be detected in log files.
    
    - **Effort:** elementary

??? abstract "Abusing Azure Browser SSO"
    
    Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Account Tampering - Suspicious Failed Logon Reasons"
    
    This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.
    
    - **Effort:** advanced

??? abstract "Active Directory Database Dump Via Ntdsutil"
    
    Detects the dump of ntdis.dit database by using the utility ntdsutil.exe. NTDS.dit database stores Active Directory data, including passwords hashes for all users in the domain.
    
    - **Effort:** elementary

??? abstract "Active Directory Delegate To KRBTGT Service"
    
    Detects potential persistence installation from an already compromised administrator domain account. The attacker will create a TGT and abuse a service account with the constrained delegation and update it with the krbtgt service. The detection relies on the Event ID 4738.
    
    - **Effort:** intermediate

??? abstract "Active Directory Replication User Backdoor"
    
    Backdooring domain object to grant the rights associated with DCSync to regular user or machine account, this technics is often used to give ResetPassword or WriteMembers or DCSync permission(s) for persistency on a domain. 
    
    - **Effort:** advanced

??? abstract "Active Directory Replication from Non Machine Account"
    
    Detects potential abuse of Active Directory Replication Service (ADRS) from a non machine account to request credentials. It requires a configuration step where the legit service account should be added to the exclusion list.
    
    - **Effort:** advanced

??? abstract "Active Directory User Backdoors"
    
    Detects scenarios where the attacker controls another user or computer account without having to use their credentials.
    
    - **Effort:** intermediate

??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? abstract "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
    - **Effort:** advanced

??? abstract "Admin Share Access"
    
    Detects access to $ADMIN share. The advanced audit policy setting "Object Access > Audit File Share" must be configured for Success/Failure. Also be very cautious to previously check if this is not commonly used by your administrators as to remotely manage your computers.
    
    - **Effort:** master

??? abstract "Admin User RDP Remote Logon"
    
    Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.
    
    - **Effort:** master

??? abstract "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master

??? abstract "Alternate PowerShell Hosts Pipe"
    
    Detects alternate PowerShell hosts potentially bypassing detections looking for powershell.exe. Prerequisites are logging for PipeEvents in Sysmon config
    
    - **Effort:** advanced

??? abstract "Antivirus Exploitation Framework Detection"
    
    Detects a highly relevant Antivirus alert that reports an exploitation framework. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary

??? abstract "Antivirus Password Dumper Detection"
    
    Detects a highly relevant Antivirus alert that reports a password dumper. This detection relies on Windows Defender events logs. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary

??? abstract "Antivirus Relevant File Paths Alerts"
    
    Detects an Antivirus alert in a highly relevant file path or with a relevant file name. This is only based on Windows Defender events.
    
    - **Effort:** elementary

??? abstract "Antivirus Web Shell Detection"
    
    Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary

??? abstract "Audio Capture via PowerShell"
    
    Detects audio capture via PowerShell Cmdlet
    
    - **Effort:** intermediate

??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability
    
    - **Effort:** elementary

??? abstract "Autorun Keys Modification"
    
    Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "BITSAdmin Download"
    
    Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.
    
    - **Effort:** advanced

??? abstract "Backup Catalog Deleted"
    
    The rule detects when the Backup Catalog has been deleted. It means the administrators will not be able to access any backups that were created earlier to perform recoveries. This is often being done using the wbadmin.exe tool.
    
    - **Effort:** intermediate

??? abstract "BazarLoader Persistence Using Schtasks"
    
    Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.
    
    - **Effort:** intermediate

??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate

??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary

??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate

??? abstract "CMSTP UAC Bypass via COM Object Access"
    
    Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects
    
    - **Effort:** intermediate

??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using sdclt.exe .
    
    - **Effort:** intermediate

??? abstract "CVE-2017-11882 Microsoft Office Equation Editor Vulnerability"
    
    Detects the exploitation of CVE-2017-11882 vulnerability. The Microsoft Office Equation Editor has no reason to do a network request or drop an executable file. This requires a sysmon configuration with file and network events.
    
    - **Effort:** master

??? abstract "CVE-2019-0708 Scan"
    
    Detects the use of a scanner that discovers targets vulnerable to CVE-2019-0708 RDP RCE aka BlueKeep.
    
    - **Effort:** elementary

??? abstract "CVE-2021-34527 - PrintNightmare - Suspicious Actions From Spoolsv"
    
    Detects suspicious image loads and file creations from the spoolsv process which could be a sign of an attacker trying to exploit the PrintNightmare vulnerability, CVE-2021-34527. A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. This works as well as a Local Privilege escalation vulnerability. To fully work the rule requires to log for Loaded DLLs and File Creations, which can be done respectively using the Sysmon's event IDs 7 and 11.
    
    - **Effort:** master

??? abstract "Capture a network trace with netsh.exe"
    
    Detects capture a network trace via netsh.exe trace functionality
    
    - **Effort:** intermediate

??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate

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

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** elementary

??? abstract "Cobalt Strike Default Service Creation Usage"
    
    Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.
    
    - **Effort:** elementary

??? abstract "Cobalt Strike Named Pipes"
    
    Detects the pipes established by Cobalt Strike to allow a communication between its beacons.
    
    - **Effort:** master

??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate

??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced

??? abstract "Copying Sensitive Files With Credential Data"
    
    Detects copy of files with well-known filenames (sensitive files with credential data) using esentutl. This requires Windows Security event log with the Detailed File Share logging policy enabled.
    
    - **Effort:** elementary

??? abstract "CreateRemoteThread Common Process Injection"
    
    Detects a possible process injection through CreateRemoteThread() which is spotted by EventID 8 from Sysmon and several EDRs. This rule has a list of process commonly being injected by the attackers that should be updated regularly.
    
    - **Effort:** advanced

??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate

??? abstract "Cred Dump Tools Dropped Files"
    
    Process with well-known names (parts of credential dump software or files produced by them) creation.
    
    - **Effort:** intermediate

??? abstract "Credential Dumping By LaZagne"
    
    Detects LSASS process access by LaZagne for credential dumping. 
    
    - **Effort:** elementary

??? abstract "Credential Dumping Tools Service Execution"
    
    Detects well-known credential dumping tools execution via service execution
    
    - **Effort:** intermediate

??? abstract "Credential Dumping-Tools Common Named Pipes"
    
    Detects well-known credential dumping tools execution via specific named pipes. Prerequisites: Logging for PipeEvents is needed in Sysmon config
    
    - **Effort:** master

??? abstract "Csrss Child Found"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.
    
    - **Effort:** intermediate

??? abstract "Csrss Wrong Parent"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** advanced

??? abstract "DC Shadow via Service Principal Name (SPN) creation"
    
    Detects DCShadow via new Service Principal Name (SPN) creation 
    
    - **Effort:** intermediate

??? abstract "DCSync Attack"
    
    Detects DCSync attack, it is highly likely that the post-exploitation tool Mimikatz was executed.
    
    - **Effort:** intermediate

??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate

??? abstract "DHCP Server Error Failed Loading the CallOut DLL"
    
    This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.
    
    - **Effort:** intermediate

??? abstract "DHCP Server Loaded the CallOut DLL"
    
    This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.
    
    - **Effort:** intermediate

??? abstract "DLL Load via LSASS Registry Key"
    
    Detects a method to load DLL via LSASS process using an undocumented Registry key. Prerequisites are logging for Registry events. This can be done with Sysmon events 12, 13 and 14 and monitor `SYSTEM\CurrentControlSet\Services`.
    
    - **Effort:** intermediate

??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate

??? abstract "DNS Server Error Failed Loading The ServerLevelPluginDLL"
    
    This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.
    
    - **Effort:** master

??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master

??? abstract "DNS Tunnel Technique From MuddyWater"
    
    Detecting DNS Tunnel Activity For Muddywater intrusion set. This is the loading of a specific DLL from an Excel macro which is detected.
    
    - **Effort:** elementary

??? abstract "DPAPI Domain Backup Key Extraction"
    
    Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers
    
    - **Effort:** intermediate

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

??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate

??? abstract "Detection of default Mimikatz banner"
    
    Detection of default Mimikatz banner in powershell events
    
    - **Effort:** intermediate

??? abstract "Disable .NET ETW Through COMPlus_ETWEnabled"
    
    Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.
    
    - **Effort:** intermediate

??? abstract "Disable Security Events Logging Adding Reg Key MiniNt"
    
    Detects the addition of a key 'MiniNt' to the registry. Upon a reboot, Windows Event Log service will stopped write events.  Prerequisites: Logging for Registry events for this specific registry key is needed in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master

??? abstract "Disable Task Manager Through Registry Key"
    
    Detects commands used to disable the Windows Task Manager by modifying the proper registry key in order to impair security tools. This technique is used by the Agent Tesla RAT, among others.
    
    - **Effort:** elementary

??? abstract "Disable Windows Defender Credential Guard"
    
    Detects registry keys being changed to disable Windows Defender Credential Guard. The rule requires to log Registry Keys modifications or creations, which can be done using Sysmon Event IDs 12,13 and 14.
    
    - **Effort:** intermediate

??? abstract "Disable Workstation Lock"
    
    Registry change in order to disable the ability to lock the computer by using CTRL+ALT+DELETE or CTRL+L. This registry key does not exist by default. Its creation is suspicious and the value set to "1" means an activation. It has been used by FatalRAT, but other attacker/malware could probably use it. This rule needs Windows Registry changes (add,modification,deletion) logging which can be done through Sysmon Event IDs 12,13,14.
    
    - **Effort:** elementary

??? abstract "Disabled IE Security Features"
    
    Detects from the command lines or the registry, changes that indicate unwanted modifications to registry keys that disable important Internet Explorer security features. This has been used by attackers during Operation Ke3chang.
    
    - **Effort:** advanced

??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate

??? abstract "Dllhost Wrong Parent"
    
    Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** elementary

??? abstract "Domain Group And Permission Enumeration"
    
    Detects adversaries attempts to find domain-level groups and permission settings. Commands such as net group /domain of the Net utility can list domain-level groups The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Wizard Spider, FIN6, and other groups used net in their campaigns.
    
    - **Effort:** advanced

??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced

??? abstract "Domain Trust Discovery Through LDAP"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. "trustedDomain" which is detected here is a Microsoft Active Directory ObjectClass Type that represents a domain that is trusted by, or trusting, the local AD DOMAIN. Several tools are using LDAP queries in the end to get the information (DSQuery, sometimes ADFind as well, etc.)
    
    - **Effort:** elementary

??? abstract "Dumpert LSASS Process Dumper"
    
    Detects the use of Dumpert process dumper, which dumps the lsass.exe process memory
    
    - **Effort:** elementary

??? abstract "Dynwrapx Module Loading"
    
    Detects the loading of DynamicWrapperX (Dynwrapx). It is used by some malware in their infection chain and could help to detect its usage from vbs/wscript/cscript scripts. This is based on Microsoft Windows Sysmon events (Event ID 7).
    
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

??? abstract "Eventlog Cleared"
    
    Some threat groups tend to delete local EventLogs (Security being the most common one to be deleted) using certain utilities. The EventID 517 is old and 1102 should be used for this instead on newer Windows versions.
    
    - **Effort:** intermediate

??? abstract "Exchange Mailbox Export"
    
    Detection of a standard Exchange Mailbox export, which stores all mails from a user in a pst file.
    
    - **Effort:** intermediate

??? abstract "Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data"
    
    Detects PowerShell SnapIn command line, often used with Get-Mailbox to export Exchange mailbox data.
    
    - **Effort:** intermediate

??? abstract "Exchange Server Creating Unusual Files"
    
    Look for Microsoft Exchange Server’s Unified Messaging service creating non-standard content on disk, which could indicate web shells or other malicious content, suggesting exploitation of CVE-2021-26858 vulnerability
    
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

??? abstract "Exploited CVE-2020-10189 Zoho ManageEngine"
    
    Detects the exploitation of Zoho ManageEngine Desktop Central Java Deserialization vulnerability reported as CVE-2020-10189
    
    - **Effort:** elementary

??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378
    
    - **Effort:** intermediate

??? abstract "Explorer Process Executing HTA File"
    
    Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.
    
    - **Effort:** intermediate

??? abstract "Explorer Wrong Parent"
    
    Detects suspicious spawning of explorer.exe process created by the rundll32.exe or regsvr32.exe. This behaviour is abnormal. Malware injecting itself into the explorer.exe process is quite common, in order to evade process-based defenses.
    
    - **Effort:** elementary

??? abstract "External Disk Drive Or USB Storage Device"
    
    Detects external diskdrives or plugged in USB device.
    
    - **Effort:** advanced

??? abstract "Failed Logon Source From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The sekoia.tags are used to filter internal Ipv4 addresses (10.0.0.0/8 172.16.0.0/12 127.0.0.0/8 169.254.0.0/16 192.168.0.0/16).
    
    - **Effort:** master

??? abstract "File Or Folder Permissions Modifications"
    
    Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.
    
    - **Effort:** master

??? abstract "FlowCloud Malware"
    
    Detects FlowCloud malware from threat group TA410. This requires Windows Event registry logging.
    
    - **Effort:** elementary

??? abstract "FoggyWeb Backdoor DLL Loading"
    
    Detects DLL image load activity as used by the threat group NOBELIUM with the FoggyWeb backdoor loader. The prerequisite is to log Loaded DLLs images, which can be done through the Sysmon Event ID 7 (DLL image loaded by process).
    
    - **Effort:** master

??? abstract "Formbook File Creation DB1"
    
    Detects specific file creation (Users\*\AppData\Local\Temp\DB1) to store data to exfiltrate (Formbook behavior). Logging for Sysmon event 11 is usually used for this detection. 
    
    - **Effort:** intermediate

??? abstract "Formbook Hijacked Process Command"
    
    Detects process hijacked by Formbook malware which executes specific commands to delete the dropper or copy browser credentials to the database before sending them to the C2.
    
    - **Effort:** intermediate

??? abstract "FromBase64String Command Line"
    
    Detects suspicious FromBase64String expressions in command line arguments
    
    - **Effort:** master

??? abstract "GitLab CVE-2021-22205"
    
    Detects GitLab vulnerability CVE-2021-22205 exploitation success. It allows an attacker to do some remote code execution with user git. The HTTP return code 422 indicates a successfull exploitation.
    
    - **Effort:** intermediate

??? abstract "Gpscript Suspicious Parent"
    
    Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.
    
    - **Effort:** intermediate

??? abstract "Grabbing Sensitive Hives Via Reg Utility"
    
    Detects dump of SAM, System or Security hives using reg.exe utility. Adversaries may attempt to dump these Windows Registry to retrieve password hashes and access credentials.
    
    - **Effort:** intermediate

??? abstract "HackTools Suspicious Process Names"
    
    Detects the default process name of several HackTools. This rule is here for quickwins as it obviously has many blind spots.
    
    - **Effort:** elementary

??? abstract "Hiding Files With Attrib.exe"
    
    Detects usage of attrib.exe to hide files from users.
    
    - **Effort:** advanced

??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate

??? abstract "ICacls Granting Access To All"
    
    Detects suspicious icacls command granting access to all, used by the ransomware Ryuk to delete every access-based restrictions on files and directories. ICacls is a built-in Windows command to interact with the Discretionary Access Control Lists (DACLs) which can grand adversaries higher permissions on specific files and folders.
    
    - **Effort:** elementary

??? abstract "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary

??? abstract "Impacket Secretsdump.py Tool"
    
    Detects credential dumping via secretdump of impacket suite.
    
    - **Effort:** intermediate

??? abstract "Impacket Wmiexec Module"
    
    Detection of impacket's wmiexec example, used by attackers to execute commands remotely.
    
    - **Effort:** elementary

??? abstract "In-memory PowerShell"
    
    Detects loading of essential DLL used by PowerShell, but not by the process powershell.exe. Detects meterpreter's "load powershell" extension and tool such PowerShDll.
    
    - **Effort:** master

??? abstract "Information Stealer Downloading Legitimate Third-Party DLLs"
    
    Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc. 
    
    - **Effort:** intermediate

??? abstract "Inhibit System Recovery Deleting Backups"
    
    Detects adversaries attempts to delete backups or inhibit system recovery. This rule relies on differents known techniques using Windows events logs from Sysmon (ID 1), and PowerShell (ID 4103, 4104).
    
    - **Effort:** intermediate

??? abstract "Invoke-TheHash Commandlets"
    
    Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.
    
    - **Effort:** elementary

??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate

??? abstract "Koadic Execution"
    
    Detects command line parameters used by Koadic hack tool
    
    - **Effort:** intermediate

??? abstract "LSASS Access From Non System Account"
    
    Detects LSASS Access from Non System Account (e.g. Mimikatz)
    
    - **Effort:** master

??? abstract "LSASS Memory Dump"
    
    Detects process accessing LSASS memory which is typical for credentials dumping tools
    
    - **Effort:** intermediate

??? abstract "LSASS Memory Dump File Creation"
    
    LSASS memory dump creation using operating systems utilities. Procdump will use process name in output file if no name is specified.
    
    - **Effort:** intermediate

??? abstract "Lateral Movement - Remote Named Pipe"
    
    Detects lateral movement and remote exec using named pipe over network. This requires Windows Security event logging with the File Share enable policy.
    
    - **Effort:** advanced

??? abstract "Lazarus Loaders"
    
    Detects different loaders used by the Lazarus Group APT
    
    - **Effort:** elementary

??? abstract "Legitimate Process Execution From Unusual Folder"
    
    Detects the execution of a legitimate, windows built-in process name from an unusual / suspicious folder. Legitimate folders are c:\windows\system32\, \SystemRoot\system32\, c:\windows\syswow64\ and c:\windows\winsxs\. Many malwares/attackers use legitimate names to masquerade but if they are not Administrator yet, they often can't write file into these legitimate folders.
    
    - **Effort:** advanced

??? abstract "Leviathan Registry Key Activity"
    
    Detects registry key used by Leviathan APT in Malaysian focused campaign.
    
    - **Effort:** elementary

??? abstract "List Shadow Copies"
    
    Detects command line used to list shadow copies. An adversary may attempt to get information on shadow volumes to perform deletion or extract password hashes from the ntds.dit file. This rule requires command line logging or Windows PowerShell events (4104).
    
    - **Effort:** master

??? abstract "Load Of dbghelp/dbgcore DLL From Suspicious Process"
    
    Detects the load of dbghelp/dbgcore DLL (used to make memory dumps) by suspicious processes. Many tools import dbghelp.dll and / or dbgcore.dll to use the MiniDumpWriteDump function. As an example, SilentTrynity C2 Framework has a module that leverages this API to dump the contents of Lsass.exe and transfer it over the network back to the attacker's machine. Dumpert from OUTFLANK also uses this.
    
    - **Effort:** advanced

??? abstract "Local Account Created"
    
    Detects local user creation on windows servers, which shouldn't happen in an Active Directory environment. Apply this on your windows server logs and not on your DC logs. One default account `defaultuser0` is excluded as only used during Windows set-up. This detection use Security Event ID 4720. 
    
    - **Effort:** master

??? abstract "Local Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master

??? abstract "Logon Scripts (UserInitMprLogonScript)"
    
    Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.
    
    - **Effort:** advanced

??? abstract "Logonui Wrong Parent"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** intermediate

??? abstract "Lsass Access Through WinRM"
    
    Detects the access of LSASS.exe process through Windows Remote Management (WinRM) protocol. This is often done using Invoke-Mimikatz -ComputerName command, which uses PSRemoting and therefore WinRM. However, this is not limited to the Mimikatz threat and can be done by other tools as well. This rule needs Process Access monitoring, which can be done using Sysmon's event ID 10.
    
    - **Effort:** intermediate

??? abstract "Lsass Wrong Parent"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** intermediate

??? abstract "MMC Spawning Windows Shell"
    
    Detects a Windows command line executable started from MMC process
    
    - **Effort:** intermediate

??? abstract "MMC20 Lateral Movement"
    
    Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe.
    
    - **Effort:** intermediate

??? abstract "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate

??? abstract "MS Office Product Spawning Exe in User Dir"
    
    Detects an executable in the users directory started from Microsoft Word, Excel, Powerpoint, Publisher or Visio. This is a common technique used by attackers with documents embedding macros. It requires Windows command line logging events.
    
    - **Effort:** intermediate

??? abstract "MSBuild Abuse"
    
    Detection of MSBuild uses by attackers to infect an host. Focuses on XML compilation which is a Metasploit payload, and on connections made by this process which is unusual.
    
    - **Effort:** intermediate

??? abstract "Malicious Named Pipe"
    
    Detects the creation of a named pipe used by known malware. Prerequisites are logging for PipeEvents in Sysmon config (Event ID 17 and 18).
    
    - **Effort:** intermediate

??? abstract "Malicious Service Installations"
    
    Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.
    
    - **Effort:** elementary

??? abstract "Malspam Execution Registering Malicious DLL"
    
    Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).
    
    - **Effort:** elementary

??? abstract "Malware Outbreak"
    
    Spots a peak of malware detection by windows defender on this perimeter. 
    
    - **Effort:** advanced

??? abstract "Malware Persistence Registry Key"
    
    Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.
    
    - **Effort:** master

??? abstract "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate

??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate

??? abstract "Metasploit PSExec Service Creation"
    
    Detects Metasploit service creation when using the PSExec module. The ImagePath here is usually a malicious command line using powershell.exe and/or cmd.exe.
    
    - **Effort:** advanced

??? abstract "Meterpreter or Cobalt Strike Getsystem Service Installation"
    
    Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting some of the techniques being used (technique 1,2 and 5).
    
    - **Effort:** elementary

??? abstract "Microsoft Malware Protection Engine Crash"
    
    Detects a crash of the Microsoft Malware Protection Engine process (MsMpEng.exe), which is suspicious and could be related to an attacker disabling the Windows protection.
    
    - **Effort:** intermediate

??? abstract "Microsoft Office Creating Suspicious File"
    
    Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.
    
    - **Effort:** intermediate

??? abstract "Microsoft Office Product Spawning Windows Shell"
    
    Detects a Windows command or scripting interpreter executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware.
    
    - **Effort:** advanced

??? abstract "Microsoft Office Spawning Script"
    
    Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 
    
    - **Effort:** intermediate

??? abstract "Microsoft Office Startup Add-In"
    
    Detects add-ins that load when Microsoft Word or Excel starts (.wll/.xll are simply .dll fit for Word or Excel). The rule requires File Creation logging to work, which can be done using Sysmon Event ID 11.
    
    - **Effort:** elementary

??? abstract "Mimikatz Basic Commands"
    
    Detects Mimikatz most popular commands. 
    
    - **Effort:** elementary

??? abstract "Mimikatz LSASS Memory Access"
    
    Detection of in-memory Mimikatz by focusing on processes opening the Local Security Authority (Lsass.exe) process and reading the memory contents of it. This probably means that Mimikatz has been executed on the host, meaning the attacker already has high privileges and is looking to dump credentials, most likely for lateral movement or privilege escalation purposes.
    
    - **Effort:** intermediate

??? abstract "Msdt (Follina) File Browse Process Execution"
    
    Detects various Follina vulnerability exploitation techniques. This is based on the Compatability Troubleshooter which is abused to do code execution.
    
    - **Effort:** elementary

??? abstract "Mshta JavaScript Execution"
    
    Identifies suspicious mshta.exe commands that execute JavaScript supplied as a command line argument.
    
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

??? abstract "Narrator Feedback-Hub Persistence"
    
    The Windows 10 Narrator's Feedback-Hub registry key has been modified which could be done by an attacker for persistence purposes. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13). Careful since the SwiftOnSecurity Sysmon's configuration needs to be changed to log for this specifically.
    
    - **Effort:** master

??? abstract "Net.exe User Account Creation"
    
    Identifies creation of local users via the net.exe command
    
    - **Effort:** master

??? abstract "NetNTLM Downgrade Attack"
    
    Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.
    
    - **Effort:** intermediate

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

??? abstract "Netsh Program Allowed With Suspicious Location"
    
    Detects Netsh commands that allow a suspcious application location on Windows Firewall, seen on kasidet worm. Last part of the existing rule (commandline startwith) was not added to this rule because it is not relevant.
    
    - **Effort:** intermediate

??? abstract "Netsh RDP Port Forwarding"
    
    Detects netsh commands that configure a port forwarding of port 3389 used for RDP. This is commonly used by attackers during lateralization on windows environments.
    
    - **Effort:** elementary

??? abstract "Netsh RDP Port Opening"
    
    Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent Malware
    
    - **Effort:** intermediate

??? abstract "Network Connection Via Certutil"
    
    Identifies certutil.exe making a network connection. Adversaries could abuse certutil.exe to download a certificate, or malware, from a remote URL. The rule excludes private IP addresses and IPV6. This requires Sysmon logging.
    
    - **Effort:** intermediate

??? abstract "Network Share Discovery"
    
    Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. File sharing over a Windows network occurs over the SMB protocol. This technique is frequently leveraged by threat actors such as APT32, APT41, Wizard Spider. But also, through the use of some malware such as Cobalt Strike, Empire, PlugX and Ramsay.
    
    - **Effort:** master

??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate

??? abstract "New DLL Added To AppCertDlls Registry Key"
    
    Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "New Or Renamed User Account With '$' In Attribute 'SamAccountName'"
    
    Detects possible bypass EDR and SIEM via abnormal user account name.
    
    - **Effort:** intermediate

??? abstract "New Service Creation"
    
    Detects creation of a new service from command line
    
    - **Effort:** advanced

??? abstract "Ngrok Process Execution"
    
    Detects possible Ngrok execution, which can be used by attacker for RDP tunneling. 
    
    - **Effort:** intermediate

??? abstract "NjRat Registry Changes"
    
    Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.
    
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

??? abstract "Office Application Startup Office Test"
    
    Detects the addition of office test registry that allows a user to specify an arbitrary DLL that will be executed everytime an Office application is started. An adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system.
    
    - **Effort:** elementary

??? abstract "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** elementary

??? abstract "Pandemic Windows Implant"
    
    Detects Pandemic Windows Implant through registry keys or specific command lines. Prerequisites: Logging for Registry events is needed, which can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "Password Dumper Activity On LSASS"
    
    Detects process handle on LSASS process with certain access mask and object type SAM_DOMAIN
    
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

??? abstract "Phosphorus (APT35) Exchange Discovery"
    
    According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about its the environment of compromised Microsoft Exchange servers. The command is the following: Get-Recipient | Select Name -ExpandProperty EmailAddresses -first 1 | Select SmtpAddress |  ft -hidetableheaders
    
    - **Effort:** elementary

??? abstract "Phosphorus Domain Controller Discovery"
    
    According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about the Domain Controller. The command is the following: "powershell.exe" /c Get-WMIObject Win32_NTDomain | findstr DomainController
    
    - **Effort:** intermediate

??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate

??? abstract "Possible RottenPotato Attack"
    
    Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.
    
    - **Effort:** intermediate

??? abstract "Potential RDP Connection To Non-Domain Host"
    
    Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.
    
    - **Effort:** master

??? abstract "PowerCat Function Loading"
    
    Detect a basic execution of PowerCat. PowerCat is a PowerShell function allowing to do basic connections, file transfer, shells, relays, generate payloads.
    
    - **Effort:** intermediate

??? abstract "PowerShell - NTFS Alternate Data Stream"
    
    Detects writing data into NTFS alternate data streams from PowerShell. Needs Script Block Logging (Event ID 4104)
    
    - **Effort:** advanced

??? abstract "PowerShell AMSI Deactivation Bypass Using .NET Reflection"
    
    Detects Request to amsiInitFailed that can be used to disable AMSI (Antimalware Scan Interface) Scanning. More information about Antimalware Scan Interface https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal.
    
    - **Effort:** elementary

??? abstract "PowerShell Credential Prompt"
    
    Detects PowerShell calling a credential prompt (using PromptForCredential) ex: $Credential = $host.ui.PromptForCredential("Need credentials", "Please enter your user name and password.", "", "NetBiosUserName") The same result can be obtained by using the Get-Credential function but detecting it will trigger a lot of FP
    
    - **Effort:** elementary

??? abstract "PowerShell Data Compressed"
    
    Detects data compression through a PowerShell command (could be used by an adversary for exfiltration)
    
    - **Effort:** advanced

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

??? abstract "PowerShell Invoke Expression With Registry"
    
    Detects keywords from well-known PowerShell techniques to get registry key values
    
    - **Effort:** advanced

??? abstract "PowerShell Invoke-Obfuscation Obfuscated IEX Invocation"
    
    Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-Obfuscation framework
    
    - **Effort:** advanced

??? abstract "PowerShell Malicious Nishang PowerShell Commandlets"
    
    Detects Commandlet names and arguments from the Nishang exploitation framework
    
    - **Effort:** advanced

??? abstract "PowerShell Malicious PowerShell Commandlets"
    
    Detects Commandlet names from well-known PowerShell exploitation frameworks (PowerSploit...)
    
    - **Effort:** master

??? abstract "PowerShell Malicious PowerShell Keywords"
    
    Detects keywords from well-known PowerShell exploitation frameworks
    
    - **Effort:** intermediate

??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced

??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced

??? abstract "Powershell Web Request"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell
    
    - **Effort:** advanced

??? abstract "Powershell Winlogon Helper DLL"
    
    Detects modifications to the Winlogon Registry keys, which may cause Winlogon to load and execute malicious DLLs and/or executables.
    
    - **Effort:** intermediate

??? abstract "Privilege Escalation Awesome Scripts (PEAS)"
    
    Detect PEAS privileges escalation scripts and binaries
    
    - **Effort:** elementary

??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** advanced

??? abstract "Process Herpaderping"
    
    Detection of process herpaderping using Sysmon Event ID 25. It detects that an image has been locked for access. Several processes have been excluded to avoid FPs.
    
    - **Effort:** master

??? abstract "Process Hollowing Detection"
    
    Detection of process hollowing using Sysmon Event ID 25. It detects that an image has been replaced in a process memory.
    
    - **Effort:** master

??? abstract "Process Memory Dump Using Comsvcs"
    
    Detects the use of comsvcs in command line to dump a specific proces memory. This techinique is widlely used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary

??? abstract "Protected Storage Service Access"
    
    Detects access to a protected_storage service over the network. It could identify potential abuse of DPAPI to extract domain backup keys from Domain Controllers.
    
    - **Effort:** master

??? abstract "PsExec Process"
    
    Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 
    
    - **Effort:** advanced

??? abstract "Putty Sessions Listing"
    
    Detects attempts to list Putty sessions through registry. To fully work, this rule requires to log registry accesses, which can be done with the Windows Event ID 4656 or 4663 but for that specific configuration is needed.
    
    - **Effort:** master

??? abstract "Python HTTP Server"
    
    Detects command used to start a Simple HTTP server in Python. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate

??? abstract "Python Opening Ports"
    
    Detects when the Windows Filtering Platform has permitted Python.exe to listen on a port for incoming connections. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else. 
    
    - **Effort:** advanced

??? abstract "QakBot Process Creation"
    
    Detects QakBot like process executions
    
    - **Effort:** intermediate

??? abstract "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate

??? abstract "RDP Login From Localhost"
    
    Detects RDP login from localhost source address, which may be a tunnelled login to bypass network restrictions.
    
    - **Effort:** elementary

??? abstract "RDP Port Change Using Powershell"
    
    Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 
    
    - **Effort:** intermediate

??? abstract "RDP Sensitive Settings Changed"
    
    Detects changes to RDP terminal service sensitive settings. Logging for registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** advanced

??? abstract "RDP Session Discovery"
    
    Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.
    
    - **Effort:** advanced

??? abstract "RUN Registry Key Created From Suspicious Folder"
    
    Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** advanced

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "Raccine Uninstall"
    
    Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.
    
    - **Effort:** elementary

??? abstract "Rare Logonui Child Found"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.
    
    - **Effort:** advanced

??? abstract "Rare Lsass Child Found"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate

??? abstract "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced

??? abstract "RedMimicry Winnti Playbook Dropped File"
    
    Detects actions caused by the RedMimicry Winnti playbook
    
    - **Effort:** elementary

??? abstract "RedMimicry Winnti Playbook Registry Manipulation"
    
    Detects actions caused by the RedMimicry Winnti playbook. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary

??? abstract "Registry Checked For Lanmanserver DisableCompression Parameter"
    
    Detects registry access for Lanmanserver\Parameters. The check of the value DisableCompression could be a sign of an attack trying to exploit SMBGhost vulnerability (CVE-2020-0796). 
    
    - **Effort:** master

??? abstract "Registry Key Used By Some Old Agent Tesla Samples"
    
    Detects potential use of the RUN registry key to execute some Agent Tesla samples at boot. Prerequisites are to log for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys"
    
    Detects persistence registry keys. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "Remote Registry Management Using Reg Utility"
    
    Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.
    
    - **Effort:** master

??? abstract "Remote Service Activity Via SVCCTL Named Pipe"
    
    Detects remote service activity via remote access to the svcctl named pipe
    
    - **Effort:** advanced

??? abstract "Remote Task Creation Via ATSVC Named Pipe"
    
    Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.
    
    - **Effort:** intermediate

??? abstract "Rubeus Register New Logon Process"
    
    Detects potential use of Rubeus through registering a new logon process. This rule needs the EventID 4611, which can be configured through Group Policies (Audit Security System Extension)
    
    - **Effort:** master

??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced

??? abstract "Ryuk Ransomware Command Line"
    
    Detects Ryuk Ransomware - Command lines stop services.
    
    - **Effort:** elementary

??? abstract "Ryuk Ransomware Persistence Registry Key"
    
    Detects registry key used by the Ryuk ransomware in two ways, either the Sysmon registry events, or the command line (reg add).
    
    - **Effort:** intermediate

??? abstract "SAM Registry Hive Handle Request"
    
    Detects handles requested to SAM registry hive
    
    - **Effort:** advanced

??? abstract "SCM Database Handle Failure"
    
    Detects non-system users failing to get a handle of the SCM database.
    
    - **Effort:** master

??? abstract "SCM Database Privileged Operation"
    
    Detects non-system users performing privileged operation on the SCM database
    
    - **Effort:** master

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

??? abstract "SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory"
    
    Detects the SeEnableDelegationPrivilege right in Active Directory granted to a user of a computer, it would allow control of other AD user objects
    
    - **Effort:** elementary

??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** intermediate

??? abstract "Searchprotocolhost Child Found"
    
    SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate

??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** intermediate

??? abstract "Secure Deletion With SDelete"
    
    Detects renaming of file while deletion with SDelete tool. SDelete is a tool that permits to securely delete files by overwriting them (no recovery possible). Few threat actors are using it to delete traces of their malware.
    
    - **Effort:** intermediate

??? abstract "Security Support Provider (SSP) Added to LSA Configuration"
    
    Detects the addition of a SSP to the registry. This is commonly used for persistence. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows. Logging for Registry events is needed for this rule to work (this can be done through Sysmon EventIDs 12 and 13).
    
    - **Effort:** elementary

??? abstract "Sliver DNS Beaconing"
    
    Detects suspicious DNS queries known from Sliver beaconing 
    
    - **Effort:** intermediate

??? abstract "Smbexec.py Service Installation"
    
    Detects the use of smbexec.py tool by detecting a specific service installation
    
    - **Effort:** elementary

??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** intermediate

??? abstract "SolarWinds Suspicious File Creation"
    
    Detects SolarWinds process creating a file with a suspicious extension. The process solarwinds.businesslayerhost.exe created an unexpected file whose extension is ".exe", ".ps1", ".jpg", ".png" or ".dll".
    
    - **Effort:** intermediate

??? abstract "SolarWinds Wrong Child Process"
    
    Detects SolarWinds process starting an unusual child process. The process solarwinds.businesslayerhost.exe created an unexepected child process which doesn't correspond to the legitimate ones.
    
    - **Effort:** intermediate

??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
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

??? abstract "StoneDrill Service Install"
    
    This method detects a service install of the malicious Microsoft Network Realtime Inspection Service service described in StoneDrill report by Kaspersky 
    
    - **Effort:** intermediate

??? abstract "Stop Backup Services"
    
    Detects adversaries attempts to stop backups services or disable Windows previous files versions feature. This could be related to ransomware operators or legit administrators. This rule relies Windows command line logging and registry logging, and PowerShell (ID 4103, 4104).
    
    - **Effort:** master

??? abstract "Successful Overpass The Hash Attempt"
    
    Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash behavior of e.g Mimikatz's sekurlsa::pth module.
    
    - **Effort:** intermediate

??? abstract "Suncrypt Parameters"
    
    Detects SunCrypt ransomware's parameters, most of which are unique.
    
    - **Effort:** elementary

??? abstract "Suspect Svchost Memory Access"
    
    Detects suspect access to svchost process memory such as that used by Invoke-Phantom (v1.0) to kill the winRM windows event logging service.
    
    - **Effort:** intermediate

??? abstract "Suspicious ADSI-Cache Usage By Unknown Tool"
    
    Detects the usage of ADSI (LDAP) operations by tools. This may also detect tools like LDAPFragger. It needs file monitoring capabilities (Sysmon Event ID 11 with .sch file creation logging).
    
    - **Effort:** advanced

??? abstract "Suspicious Access To Sensitive File Extensions"
    
    Detects known sensitive file extensions accessed on a network share. This activity could possibly correspond to a malicious one (removing backup, reading sensitive files, etc.).
    
    - **Effort:** master

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

??? abstract "Suspicious DLL Loaded Via Office Applications"
    
    Detects suspicious DLL being loaded by an Microsoft Office Product. Considered as suspects are some .NET DLLs, clr.dll, GAC DLL, DSParse (Active Directoryi services API) or Kerberos DLLs which may be loaded by MS Office processes when executing a potentially malicious macro. The prerequisite is to log the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master

??? abstract "Suspicious DLL Loading By Ordinal"
    
    Detects suspicious DLL Loading by ordinal number in a non legitimate or rare folders. For example, Sofacy (APT28) used this technique to load their Trojan in a campaign of 2018.
    
    - **Effort:** intermediate

??? abstract "Suspicious DLL side loading from ProgramData"
    
    Detects suspicious DLL side-loading from C:\ProgramData where the DLL is not signed.
    
    - **Effort:** intermediate

??? abstract "Suspicious DNS Child Process"
    
    Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).
    
    - **Effort:** intermediate

??? abstract "Suspicious Desktopimgdownldr Execution"
    
    Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.
    
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

??? abstract "Suspicious Hostname"
    
    Detects suspicious hostnames such as ones with kali in it, to detect kali linux default hosts, but also other hostnames commonly used in attacks. List can be improved according to the environment.
    
    - **Effort:** intermediate

??? abstract "Suspicious LDAP-Attributes Used"
    
    Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies. Careful as the 5136 is only on domain controllers and needs to be activated through the Group Policy.
    
    - **Effort:** intermediate

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
    
    Detection on suspicious network arguments in processes command lines using HTTP schema with port 443.
    
    - **Effort:** intermediate

??? abstract "Suspicious New Printer Ports In Registry"
    
    Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14). 
    
    - **Effort:** master

??? abstract "Suspicious Outbound Kerberos Connection"
    
    Detects suspicious outbound network activity via kerberos default port indicating possible lateral movement or first stage PrivEsc via delegation.
    
    - **Effort:** advanced

??? abstract "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate

??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? abstract "Suspicious PowerShell Invocations - Generic"
    
    Detects suspicious PowerShell invocation command parameters through command line logging or ScriptBlock Logging.
    
    - **Effort:** intermediate

??? abstract "Suspicious PowerShell Invocations - Specific"
    
    Detects suspicious PowerShell invocation command parameters
    
    - **Effort:** intermediate

??? abstract "Suspicious PowerShell Keywords"
    
    Detects keywords that could indicate the use of some PowerShell exploitation framework
    
    - **Effort:** advanced

??? abstract "Suspicious PrinterPorts Creation (CVE-2020-1048)"
    
    Detects new commands that add new printer port which point to suspicious file
    
    - **Effort:** advanced

??? abstract "Suspicious Process Requiring DLL Starts Without DLL"
    
    Detects potential process injection and hollowing on processes that usually require a DLL to be launched, but are launched without any argument. 
    
    - **Effort:** intermediate

??? abstract "Suspicious PsExec Execution"
    
    Detects execution of PsExec, different from the Sysinternals one. This rule helps to filter out the noise if PsExec is used for legit purposes or if attacker uses a different PsExec client other than Sysinternals one. The prerequisite is to log the Event ID 5145 (by setting "Audit Policy > Object Access > Audit Detailed File Share" to Success/Failure).
    
    - **Effort:** master

??? abstract "Suspicious Regsvr32 Execution"
    
    Detects suspicious regsvr32.exe executions, either regsvr32 registering a DLL in an unusual repository (temp/, appdata/ or public/), or regsvr32 executed by an unusual parent process, or regsvr32 executing an unusual process, or regsvr32 registering a media file and not a DLL (as seen in IcedID campaigns), or regsvr32 registering a ocx file in appdata/.
    
    - **Effort:** intermediate

??? abstract "Suspicious Rundll32.exe Execution"
    
    The process rundll32.exe executes a newly dropped DLL with update /i in the command line. This specific technic was observed at least being used by the IcedID loading mechanism dubbed Gziploader.
    
    - **Effort:** intermediate

??? abstract "Suspicious SAM Dump"
    
    Detects suspicious SAM dump to AppData repository, as cause by QuarksPwDump and other password dumpers. Logging for Microsoft-Windows-Kernel-General Event ID 16 or Sysmon Event ID 11 is needed.
    
    - **Effort:** intermediate

??? abstract "Suspicious Scheduled Task Creation"
    
    Detects suspicious scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 
    
    - **Effort:** intermediate

??? abstract "Suspicious Scripting In A WMI Consumer"
    
    Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.
    
    - **Effort:** intermediate

??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate

??? abstract "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary

??? abstract "Suspicious Windows ANONYMOUS LOGON Local Account Created"
    
    Detects the creation of suspicious accounts simliar to ANONYMOUS LOGON, such as using additional spaces. Created as a covering detection for attackers trying to created an ANONYMOUS LOGON account as it is an account named used in internal Windows events and frequently filtered by attackers.
    
    - **Effort:** elementary

??? abstract "Suspicious Windows DNS Queries"
    
    Detects a suspicious Windows command-line process making a DNS query via known abuse text paste web services. This is based on Microsoft Windows Sysmon events (Event ID 22).
    
    - **Effort:** advanced

??? abstract "Suspicious Windows Defender Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master

??? abstract "Suspicious Windows Installer Execution"
    
    Detects suspicious execution of the Windows Installer service (msiexec.exe) which could be used to install a malicious MSI package hosted on a remote server.
    
    - **Effort:** intermediate

??? abstract "Suspicious Windows Script Execution"
    
    Detects wscript.exe or cscript.exe executing a script in user directories (C:\ProgramData or C:\Users) with a .txt extension, which is very suspicious. It could strongly correspond to a malware dropper, as seen during SquirrelWaffle maldoc campaign.
    
    - **Effort:** intermediate

??? abstract "Suspicious XOR Encoded PowerShell Command Line"
    
    Detects suspicious powershell process which includes bxor command, alternative obfuscation  method to b64 encoded commands.
    
    - **Effort:** advanced

??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate

??? abstract "Suspicious desktop.ini Action"
    
    Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.
    
    - **Effort:** advanced

??? abstract "Svchost DLL Search Order Hijack"
    
    Detects svchost process hijacking through DLL loading. IKEEXT and SessionEnv service, as they call LoadLibrary on files that do not exist within C:\Windows\System32\ by default. An attacker can place their malicious logic within the PROCESS_ATTACH block of their library and restart the aforementioned services "svchost.exe -k netsvcs" to gain code execution on a remote machine.
    
    - **Effort:** master

??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** advanced

??? abstract "SysKey Registry Keys Access"
    
    Detects handle requests and access operations to specific registry keys to calculate the SysKey. The SysKey allows to decrypt Security Account Mannager (SAM) database entries (from registry or hive) and get NTLM, and sometimes LM hashes of local accounts passwords. Adversaries can calculate the Syskey by using RegOpenKeyEx/RegQueryInfoKey API calls to query the appropriate class info and values from the HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\JD, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Skew1, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\GBG, and HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Data keys.
    
    - **Effort:** elementary

??? abstract "Sysmon Windows File Block Executable"
    
    Sysmon has blocked an executable file from being written to the disk. This could be a malicious binary to investigate.  
    
    - **Effort:** master

??? abstract "Sysprep On AppData Folder"
    
    Detects suspicious Sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec). Sysprep is a Windows tool used to change Windows images from a generalized state to a specialized state, and then back to a generalized state. It can be used to remove all system-specific information and reset the computer.
    
    - **Effort:** intermediate

??? abstract "TUN/TAP Driver Installation"
    
    Detects the installation of the TUN or TAP driver service, this activity could be related to data exfiltration using tunneling techniques. The TUN/TAP Windows Adapter is a network driver that enables some VPN providers to facilitate a VPN connection to their server. TUN/TAP driver is only used by specific VPNs (e.g. OpenVPN, Wireguard), not by thoses based on IKE protocols (e.g. IPsec).
    
    - **Effort:** intermediate

??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** intermediate

??? abstract "Taskhost or Taskhostw Suspicious Child Found"
    
    Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.
    
    - **Effort:** advanced

??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** intermediate

??? abstract "Transfering Files With Credential Data Via Network Shares"
    
    Detects file transfer of sensitive files which contain credential data using network shares.
    
    - **Effort:** intermediate

??? abstract "Trickbot Malware Activity"
    
    Detects Trickbot malware process tree pattern in which rundll32.exe is parent of wermgr.exe
    
    - **Effort:** intermediate

??? abstract "Turla Named Pipes"
    
    Detects a named pipe used by Turla group samples. Prerequisites: Logging for PipeEvents is needed in Sysmon config
    
    - **Effort:** elementary

??? abstract "UAC Bypass Using Fodhelper"
    
    Detects UAC bypass method using Fodhelper after setting the proper registry key, used in particular by Agent Tesla (RAT) or more recently by Earth Luscas. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate

??? abstract "UAC Bypass Via Sdclt"
    
    Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)
    
    - **Effort:** elementary

??? abstract "UAC Bypass via Event Viewer"
    
    Detects UAC bypass method using Windows event viewer. 
    
    - **Effort:** elementary

??? abstract "Unsigned Image Loaded Into LSASS Process"
    
    Loading unsigned image (DLL, EXE) into LSASS process. To activate this rule you need to monitor loaded images into the LSASS process, this can be done with SYSMON Event ID 7.
    
    - **Effort:** advanced

??? abstract "Ursnif Registry Key"
    
    Detects a new registry key created by Ursnif malware. The rule requires to log for Registry Events, which can be done using SYsmon's Event IDs 12,13 and 14.
    
    - **Effort:** elementary

??? abstract "Usage Of Procdump With Common Arguments"
    
    Detects the usage of Procdump sysinternals tool with some common arguments and followed by common patterns.
    
    - **Effort:** intermediate

??? abstract "Usage Of Sysinternals Tools"
    
    Detects the usage of Sysinternals Tools due to accepteula key being added to Registry. The rule detects it either from the command line usage or from the regsitry events. For the later prerequisite is logging for registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master

??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** intermediate

??? abstract "User Couldn't Call A Privileged Service LsaRegisterLogonProcess"
    
    The LsaRegisterLogonProcess function verifies that the application making the function call is a logon process by checking that it has the SeTcbPrivilege privilege set. Possible Rubeus tries to get a handle to LSA. This rule requires to log the Event ID 4673, which can be done by updating the Audit Policy.
    
    - **Effort:** master

??? abstract "Userinit Wrong Parent"
    
    Userinit.exe is a key process in the Windows operating system. On boot-up it manages the different start up sequences needed, such as establishing network connection and starting up the Windows shell. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** intermediate

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate

??? abstract "WMI DLL Loaded Via Office"
    
    Detects Windows Management Instrumentation (WMI) DLL loaded via Office process. This activity may correspond to VBA macro executing WMI commands, which is highly suspicious. The prerequisite is to log Loaded DLLs images, which can be done with the Sysmon Event ID 7 (DLL image loaded by process).
    
    - **Effort:** master

??? abstract "WMI Event Subscription"
    
    Detects creation of WMI event subscription persistence method 
    
    - **Effort:** advanced

??? abstract "WMI Install Of Binary"
    
    Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.
    
    - **Effort:** elementary

??? abstract "WMI Persistence Command Line Event Consumer"
    
    Detects WMI command line event consumers.
    
    - **Effort:** elementary

??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced

??? abstract "WMIC Command To Determine The Antivirus"
    
    Detects WMIC command to determine the antivirus on a system, characteristic of the ZLoader malware (and possibly others)
    
    - **Effort:** intermediate

??? abstract "WMIC Loading Scripting Libraries"
    
    Detects threat actors proxy executing code and bypassing application controls by leveraging wmic and the `/FORMAT` argument switch to download and execute an XSL file (i.e js, vbs, etc).   The rule requires to log Loaded DLLs to work properly, which can be done using Sysmon Event ID 7.
    
    - **Effort:** master

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
    
    Detects the harvesting of WiFi credentials using netsh.exe, used in particular by Agent Tesla (RAT) and Turla Mosquito (RAT)
    
    - **Effort:** elementary

??? abstract "Windows Credential Editor Registry Key"
    
    Detects the use of Windows Credential Editor (WCE). Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary

??? abstract "Windows Defender Configuration Changed"
    
    Detects when an feature configuration change is made to Microsoft Windows Defender (enabling or disabling real-time protection, etc.)
    
    - **Effort:** master

??? abstract "Windows Defender Deactivation Using PowerShell Script"
    
    Detects attempts to deactivate Windows Defender with PowerShell using ScriptBlockLogging.
    
    - **Effort:** master

??? abstract "Windows Defender Disabled"
    
    The rule detects attempts to deactivate/disable Windows Defender through command line or registry. To fully use this rule Windows Registry logging is needed. This can be done for instance using Sysmon with Event IDs 12,13 and 14 (and adding the correct path in its configuration).
    
    - **Effort:** intermediate

??? abstract "Windows Defender Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line.
    
    - **Effort:** elementary

??? abstract "Windows Defender Exclusion Configuration"
    
    Detects when an exclusion configuration change is made to Microsoft Windows Defender (adding either a path or process bypass)
    
    - **Effort:** elementary

??? abstract "Windows Defender History Deleted"
    
    Windows Defender history has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** master

??? abstract "Windows Defender History Directory Deleted"
    
    Windows Defender history directory has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** elementary

??? abstract "Windows Defender Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender scan and updates. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate

??? abstract "Windows Defender Signatures Removed With MpCmdRun"
    
    Detects attempts to remove Windows Defender Signatures using MpCmdRun legitimate Windows Defender executable. No signatures mean Windows Defender will be less effective (or completely useless depending on the option used).
    
    - **Effort:** elementary

??? abstract "Windows Defender Tampering Detected"
    
    Detection of Windows Defender Tampering, from definitions' deletion to deactivation of parts or all of Defender.
    
    - **Effort:** intermediate

??? abstract "Windows Defender Threat Detected"
    
    Detection of a windows defender alert indicating the presence of potential malware
    
    - **Effort:** intermediate

??? abstract "Windows Firewall Changes"
    
    Detects changes on Windows Firewall configuration
    
    - **Effort:** master

??? abstract "Windows Registry Persistence COM Key Linking"
    
    Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.
    
    - **Effort:** master

??? abstract "Windows Registry Persistence COM Search Order Hijacking"
    
    Detects potential COM object hijacking leveraging the COM Search Order. Logging for Registry events is needed, it can be done with Sysmon's Event IDs 12 and 13.
    
    - **Effort:** advanced

??? abstract "Windows Update LolBins"
    
    This rule try to detect a suspicious behavior of wuauclt.exe (windows update client) that could be a lolbins. Wuauctl.exe could be used to execute a malicious program.
    
    - **Effort:** elementary

??? abstract "Wininit Wrong Parent"
    
    Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** intermediate

??? abstract "Winlogon wrong parent"
    
    Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** advanced

??? abstract "Winrshost Wrong Parent"
    
    Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.
    
    - **Effort:** intermediate

??? abstract "Winword Document Droppers"
    
    Detects specific process characteristics of word document droppers. This techniques has been used by Maze ransomware operators.
    
    - **Effort:** elementary

??? abstract "Winword wrong parent"
    
    Word is a well known Windows process used to read documents. Some malicious process could use it to run malicious code. The rule tries to detect winword.exe launched with a suspect parent process name.
    
    - **Effort:** advanced

??? abstract "Wmic Process Call Creation"
    
    The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.
    
    - **Effort:** intermediate

??? abstract "Wmiprvse Wrong Parent"
    
    Detects if the Wmiprvse process was executed by a non-legitimate parent process. The wmiprvse.exe process (wmiprvse stands for Microsoft Windows Management Instrumentation) is a generic process for managing clients on Windows. It is initialized the first time a client application connects and allows you to monitor system resources. This requires Windows command line logging.
    
    - **Effort:** intermediate

??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** intermediate

??? abstract "XCopy Suspicious Usage"
    
    Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.
    
    - **Effort:** advanced

??? abstract "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate
