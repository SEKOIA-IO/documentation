# Built-in detection rules, EventIDs and EventProviders relations
SEKOIA.IO provides built-in detection rules to illuminate intrusions, adversarial behaviours and suspicious activity escalation chains so you can immediately take steps to remediate. Built-in rules can be customized to your context and according to your security posture.
This page aims at helping partners & customers in having their detection coverage by knowing which Event IDs and [Event Providers](https://learn.microsoft.com/en-us/windows/win32/etw/providing-events) are used by rule. **Please note this was retrieved automatically from our tests samples when generating attacks that triggered the rules. It might not be exhaustive and concerns mostly Windows-related rules.** _Last update on 2024-01-15_

The colors of the EventIDs in this page should be interpreted as follow:

  - <span style='color:#B60016'>Red</span>: This EventID is not logged by default on a Windows 10+ or Windows Server 2016+ machine.
  - <span style='color:#D89462'>Orange</span>: This EventID is logged by default on a Windows 10+ or Windows Server 2016+ machine but upgrading its configuration would greatly help detection. For instance, the EventID 4688 is logged by default, but logging the command line is incredibly helpful for the rules since almost 50% of our rules use command line for detection (usually showed as EventID 1 in this page).
  - <span style='color:#6a18a0'>Purple</span>: This EventID is logged by default if you have Windows Defender activated.
  - <span style='color:#5865d3'>Blue</span>: This EventID is only logged if you have Sysmon. **Our rules will have a master Effort Level if the recommended Sysmon Configuration is not enough and needs to be modified. Please be aware that a modification of Sysmon Configuration can greatly increase events logging in your network, which SEKOIA.IO can't know about and therefore is not responsible for that.**

## Rules x Effort Level x EventIDs x Event Providers
| Rule Name | Effort Level | EventIDs | Event Providers |
| --------- | ------------ | -------- | --------------- |
| Microsoft Office Creating Suspicious File | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| CVE-2017-11882 Microsoft Office Equation Editor Vulnerability | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| Stop Backup Services | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Remote Registry Management Using Reg Utility | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Cobalt Strike Named Pipes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| AD Privileged Users Or Groups Reconnaissance | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4661' style='color: inherit;'>4661</a></span> | Microsoft-Windows-Security-Auditing |
| Svchost DLL Search Order Hijack | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS New Country | master | 98 |  |
| AD User Enumeration | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| LSASS Memory Dump | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Netsh Port Opening | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CVE-2021-34527 - PrintNightmare - Suspicious Actions From Spoolsv | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Account Removed From A Security Enabled Group | master | <span style="color:#D89462">4729</span> | Microsoft-Windows-Security-Auditing |
| Microsoft Defender Antivirus Disable Using Registry | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| SCM Database Privileged Operation | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4674' style='color: inherit;'>4674</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) MCAS Repeated Failed Login | master | 98 |  |
| DNS Server Error Failed Loading The ServerLevelPluginDLL | master | 150, 770, 771 | Microsoft-Windows-DNS-Server-Service |
| Suspicious PsExec Execution | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| List Shadow Copies | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Execution From Suspicious Folder | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS Inbox Hiding | master | 98 |  |
| Failed Logon Source From Public IP Addresses | master | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a> | Microsoft-Windows-Security-Auditing |
| User Account Deleted | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4743' style='color: inherit;'>4743</a></span> | Microsoft-Windows-Security-Auditing |
| LSASS Access From Non System Account | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Process Hollowing Detection | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>25</a></span> | Microsoft-Windows-Sysmon |
| Autorun Keys Modification | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Microsoft Defender Antivirus Exclusion Command | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DNS ServerLevelPluginDll Installation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Exclusion Configuration | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5007</a></span> | Microsoft-Windows-Sysmon, Microsoft-Windows-Windows Defender |
| xWizard Execution | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Potential RDP Connection To Non-Domain Host | master | <span style="color:#B60016">8001</span> | Microsoft-Windows-NTLM |
| Registry Checked For Lanmanserver DisableCompression Parameter | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| User Account Created | master | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Malware Persistence Registry Key | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Configuration Changed | master | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5007</a></span> | Microsoft-Windows-Windows Defender |
| Sysmon Windows File Block Executable | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>27</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Device Code Authentication | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> |  |
| Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Windows Defender Deactivation Using PowerShell Script | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| File Or Folder Permissions Modifications | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious PowerShell Commandlets | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Windows Registry Persistence COM Key Linking | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Admin User RDP Remote Logon | master | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Narrator Feedback-Hub Persistence | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| User Couldn't Call A Privileged Service LsaRegisterLogonProcess | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4673' style='color: inherit;'>4673</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) MCAS Repeated Delete | master | 98 |  |
| Admin Share Access | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5140' style='color: inherit;'>5140</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious DLL Loaded Via Office Applications | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Process Herpaderping | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>25</a></span> | Microsoft-Windows-Sysmon |
| Putty Sessions Listing | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS Risky IP | master | 98 |  |
| FoggyWeb Backdoor DLL Loading | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| In-memory PowerShell | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Access To Sensitive File Extensions | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Webshell Creation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Sysmon |
| Privileged AD Builtin Group Modified | master | <span style="color:#D89462">4727</span>, <span style="color:#D89462">4728</span>, <span style="color:#D89462">4729</span>, <span style="color:#D89462">4730</span>, <span style="color:#D89462">4754</span>, <span style="color:#D89462">4756</span>, <span style="color:#D89462">4757</span>, <span style="color:#D89462">4758</span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4764' style='color: inherit;'>4764</a></span> | Microsoft-Windows-Security-Auditing |
| Account Added To A Security Enabled Group | master | <span style="color:#D89462">4728</span> | Microsoft-Windows-Security-Auditing |
| WMI DLL Loaded Via Office | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| SCM Database Handle Failure | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| FromBase64String Command Line | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS Detection Velocity | master | 98 |  |
| Microsoft 365 (Office 365) Potential Ransomware Activity Detected | master | 40 |  |
| Windows Firewall Changes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| TOR Usage Generic Rule | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| WMIC Loading Scripting Libraries | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Remote Monitoring and Management Software - AnyDesk | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Kernel-Process, Microsoft-Windows-DNS-Client |
| NjRat Registry Changes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Credential Dumping-Tools Common Named Pipes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Advanced IP Scanner | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious New Printer Ports In Registry | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Net.exe User Account Creation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Network Share Discovery | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Rubeus Register New Logon Process | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4611' style='color: inherit;'>4611</a></span> | Microsoft-Windows-Security-Auditing |
| Usage Of Sysinternals Tools | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Protected Storage Service Access | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Abusing Azure Browser SSO | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus History Deleted | master | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1013</a></span> | Microsoft-Windows-Windows Defender |
| Disable Security Events Logging Adding Reg Key MiniNt | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Wininit Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Logonui Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| AccCheckConsole Executing Dll | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Suspicious ADSI-Cache Usage By Unknown Tool | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Csrss Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Lateral Movement - Remote Named Pipe | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Disabled IE Security Features | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Adexplorer Usage | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| XCopy Suspicious Usage | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Regsvr32 Execution | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Remote Service Activity Via SVCCTL Named Pipe | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft Windows Active Directory Module Commandlets | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Userinit Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Control Panel Items | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NTDS.dit File In Suspicious Directory | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Taskhost or Taskhostw Suspicious Child Found | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Default Encoding To UTF-8 PowerShell | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious Nishang PowerShell Commandlets | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Hiding Files With Attrib.exe | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Active Directory Replication User Backdoor | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Spoolsv Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Download From URL | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Certify Or Certipy | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Lsass Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Active Directory Replication from Non Machine Account | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Metasploit PSExec Service Creation | advanced | <span style="color:#B60016">7045</span> | Service Control Manager |
| Powershell Web Request | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Alternate PowerShell Hosts Pipe | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Dllhost Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Unsigned Image Loaded Into LSASS Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| New Service Creation | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Microsoft Office Product Spawning Windows Shell | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious XOR Encoded PowerShell Command Line | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| WiFi Credentials Harvesting Using Netsh | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Winrshost Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rclone Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Tampering Detected | advanced | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1127</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>2013</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5001</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5010</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5012</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5101</a></span> | Microsoft-Windows-Windows Defender |
| PowerShell Credential Prompt | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| PowerView commandlets 1 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Account Tampering - Suspicious Failed Logon Reasons | advanced | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4776' style='color: inherit;'>4776</a></span> | Microsoft-Windows-Security-Auditing |
| RDP Session Discovery | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Domain Group And Permission Enumeration | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PsExec Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Sysmon, Service Control Manager |
| SAM Registry Hive Handle Request | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| Taskhostw Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMI Event Subscription | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>19</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>20</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>21</a></span> | Microsoft-Windows-Sysmon |
| Winlogon wrong parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Python Opening Ports | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5154' style='color: inherit;'>5154</a></span> | Microsoft-Windows-Security-Auditing |
| Wmiprvse Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| AutoIt3 Execution From Suspicious Folder | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Winword wrong parent | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| Legitimate Process Execution From Unusual Folder | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Sysmon |
| Telegram Bot API Request | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| PowerShell - NTFS Alternate Data Stream | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| PowerShell EncodedCommand | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| AzureEdge in Command Line | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| PowerShell Data Compressed | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Cmd.exe Command Line | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2017-0261 Or CVE-2017-0262 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Permission Discovery Via Wmic | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Dynwrapx Module Loading | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Credentials Extraction | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Powershell AMSI Bypass | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Cmd.exe Used To Run Reconnaissance Commands | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Outbound Kerberos Connection | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5156' style='color: inherit;'>5156</a></span> | Microsoft-Windows-Security-Auditing |
| Taskhost Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Mimikatz LSASS Memory Access | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Keywords | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Svchost Modification | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Smss Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 Low Severity AIR Alert Handled Automatically | advanced | 64 |  |
| Webshell Execution W3WP Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Domain Trust Created Or Removed | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4706' style='color: inherit;'>4706</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4707' style='color: inherit;'>4707</a></span> | Microsoft-Windows-Security-Auditing |
| PowerShell Invoke-Obfuscation Obfuscated IEX Invocation | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Explorer Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| RDP Login From Localhost | advanced | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Suspicious Double Extension | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Control Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Wsmprovhost Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exfiltration And Tunneling Tools Execution | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Searchindexer Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PROCEXP152.sys File Created In Tmp | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| AD Object WriteDAC Access | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious Regasm Regsvcs Usage | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Netsh Allow Command | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rare Logonui Child Found | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Search Order Hijacking | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Load Of dbghelp/dbgcore DLL From Suspicious Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| CreateRemoteThread Common Process Injection | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>8</a></span> | Microsoft-Windows-Sysmon |
| PowerView commandlets 2 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| RDP Sensitive Settings Changed | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Netsh Program Allowed With Suspicious Location | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Change Default File Association | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rubeus Tool Command-line | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PrinterPorts Creation (CVE-2020-1048) | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| ACLight Discovering Privileged Accounts | advanced | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Suspicious desktop.ini Action | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| WMI Persistence Script Event Consumer File Write | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Logon Scripts (UserInitMprLogonScript) | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Svchost Wrong Parent | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious Windows DNS Queries | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| Malicious PowerShell Keywords | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| External Disk Drive Or USB Storage Device | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-6416' style='color: inherit;'>6416</a></span> | Microsoft-Windows-Security-Auditing |
| Adidnsdump Enumeration | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Kernel-File, Microsoft-Windows-Security-Auditing |
| Remote Privileged Group Enumeration | advanced | 4799 |  |
| SquirrelWaffle Malspam Execution Loading DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Koadic Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Disable .NET ETW Through COMPlus_ETWEnabled | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspect Svchost Memory Access | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Finger Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMIC Command To Determine The Antivirus | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| COM Hijack Via Sdclt | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Process Requiring DLL Starts Without DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Ngrok Process Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DLL side loading from ProgramData | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Desktopimgdownldr Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Commands From MS SQL Server Shell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Creation or Modification of a GPO Scheduled Task | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| MSBuild Abuse | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| Mshta Suspicious Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| High Privileges Network Share Removal | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Sysprep On AppData Folder | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Sliver DNS Beaconing | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Taskkill Command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Capture a network trace with netsh.exe | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CertOC Loading Dll | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Suspicious Outlook Child Process | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| CMSTP Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CMSTP UAC Bypass via COM Object Access | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DHCP Server Error Failed Loading the CallOut DLL | intermediate | 1031, 1032, 1033, 1034 | Microsoft-Windows-DHCP-Server |
| Chafer (APT 39) Activity | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| BazarLoader Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| IIS Module Installation Using AppCmd | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Password Dumper Activity On LSASS | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| Pandemic Windows Implant | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| XSL Script Processing And SquiblyTwo Attack | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Csrss Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DNS Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Lsass Access Through WinRM | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| DHCP Callout DLL Installation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Exchange Server Spawning Suspicious Processes | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) AtpDetection | intermediate | 47 |  |
| KeePass Config XML In Command-Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Commonly Used Commands To Stop Services And Remove Backups | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) Malware Uploaded On SharePoint | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span> |  |
| DLL Load via LSASS Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| WMIC Uninstall Product | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Denied Access To Remote Desktop | intermediate | 4825 | Microsoft-Windows-Security-Auditing |
| Non-Legitimate Executable Using AcceptEula Parameter | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process, Microsoft-Windows-Kernel-Process |
| Remote Task Creation Via ATSVC Named Pipe | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft Malware Protection Engine Crash | intermediate | 1000 | Application Error |
| Powershell Winlogon Helper DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Specific | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| TUN/TAP Driver Installation | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| SolarWinds Suspicious File Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 Low Severity AIR Alert Requires Action | intermediate | 64 |  |
| UAC Bypass via Event Viewer | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Generic | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Explorer Process Executing HTA File | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMImplant Hack Tool | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Active Directory User Backdoors | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) Malware Uploaded On OneDrive | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span> |  |
| Suspicious Windows Installer Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| LSASS Memory Dump File Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Execution Via Rundll32 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Gpscript Suspicious Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Set-MpPreference Base64 Encoded | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Password Change On Directory Service Restore Mode (DSRM) Account | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4794' style='color: inherit;'>4794</a></span> | Microsoft-Windows-Security-Auditing |
| Network Sniffing Windows | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Microsoft-Windows-Sysmon |
| Cmdkey Cached Credentials Recon | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Possible RottenPotato Attack | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Spyware Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Impacket Secretsdump.py Tool | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Cred Dump Tools Dropped Files | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Hostname | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Suspicious Cmd File Copy Command To Network Share | intermediate | 30 | Microsoft-Windows-Kernel-File |
| Microsoft Defender Antivirus Disable Scheduled Tasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Successful Overpass The Hash Attempt | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| STRRAT Scheduled Task | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Threat Detected | intermediate | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1006</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1007</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1008</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1015</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1117</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1118</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1119</a></span>, 1125, 1126 | Microsoft-Windows-Windows Defender |
| Suspicious Mshta Execution From Wmi | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MS Office Product Spawning Exe in User Dir | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Cobalt Strike Default Beacons Names | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| RDP Port Change Using Powershell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Clear EventLogs Through CommandLine | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NetNTLM Downgrade Attack | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4657' style='color: inherit;'>4657</a></span> | Microsoft-Windows-Sysmon |
| StoneDrill Service Install | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| HackTools Suspicious Process Names In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Disable SecurityHealth | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| NetSh Used To Disable Windows Firewall | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Qakbot Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Wmic Process Call Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Remote Enumeration of Lateral Movement Groups | intermediate | 4799 | Microsoft-Windows-Security-Auditing |
| Python HTTP Server | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Werfault DLL Injection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| MMC20 Lateral Movement | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Rundll32.exe Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process, Microsoft-Windows-Sysmon |
| PowerCat Function Loading | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Inhibit System Recovery Deleting Backups | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| DPAPI Domain Backup Key Extraction | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Netsh RDP Port Opening | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exchange Server Creating Unusual Files | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Suspicious SAM Dump | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>16</a></span> | Microsoft-Windows-Kernel-General |
| Schtasks Suspicious Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Network Args In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process, Microsoft-Windows-Sysmon |
| OneNote Embedded File | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Venom Multi-hop Proxy agent detection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Backup Catalog Deleted | intermediate | 524 | Microsoft-Windows-Backup |
| DNS Exfiltration and Tunneling Tools Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Usage Of Procdump With Common Arguments | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Scripting In A WMI Consumer | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>20</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Mshta Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Disable Windows Defender Credential Guard | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Grabbing Sensitive Hives Via Reg Utility | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process, Microsoft-Windows-Sysmon |
| Copy Of Legitimate System32 Executable | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Searchprotocolhost Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Network Connection Via Certutil | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| New DLL Added To AppCertDlls Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Restoration Abuse | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| ETW Tampering | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| OceanLotus Registry Activity | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Formbook File Creation DB1 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Email Forwarding To Consumer Email Address | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| Exploiting SetupComplete.cmd CVE-2019-1378 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Scheduled Task Creation | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| DC Shadow via Service Principal Name (SPN) creation | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4742' style='color: inherit;'>4742</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Exfiltration Domain In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Data Compressed With Rar With Password | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Phosphorus Domain Controller Discovery | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SolarWinds Wrong Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Email Forwarding To Email Address With Rare TLD | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| New Or Renamed User Account With '$' In Attribute 'SamAccountName' | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious certutil command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Detection of default Mimikatz banner | intermediate | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| MavInject Process Injection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Ryuk Ransomware Persistence Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Possible Replay Attack | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4649' style='color: inherit;'>4649</a></span> | Microsoft-Windows-Security-Auditing |
| Hijack Legit RDP Session To Move Laterally | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| NlTest Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious LDAP-Attributes Used | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| MMC Spawning Windows Shell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Formbook Hijacked Process Command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Windows Script Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Suspicious Driver Loaded | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Exchange Mailbox Export | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| UAC Bypass Using Fodhelper | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| DCSync Attack | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| WCE wceaux.dll Creation | intermediate | 30 | Microsoft-Windows-Kernel-File |
| Eventlog Cleared | intermediate | 517, <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-1102' style='color: inherit;'>1102</a> | Microsoft-Windows-Eventlog |
| Malicious Named Pipe | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Wmic Service Call | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Transfering Files With Credential Data Via Network Shares | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Netsh Allowed Python Program | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Bloodhound and Sharphound Tools Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MalwareBytes Uninstallation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Active Directory Delegate To KRBTGT Service | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738' style='color: inherit;'>4738</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft Office Spawning Script | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| QakBot Process Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| User Added to Local Administrators | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4732' style='color: inherit;'>4732</a></span> | Microsoft-Windows-Security-Auditing |
| SOCKS Tunneling Tool | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MOFComp Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NTDS.dit File Interaction Through Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Audio Capture via PowerShell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Rare Lsass Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Disable Services | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Powershell UploadString Function | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Trickbot Malware Activity | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DLL Loading By Ordinal | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Credential Dumping Tools Service Execution | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| Secure Deletion With SDelete | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4658' style='color: inherit;'>4658</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Registry Key Used By Some Old Agent Tesla Samples | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| GPO Executable Delivery | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| DHCP Server Loaded the CallOut DLL | intermediate | 1033 |  |
| Outlook Registry Access | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Registry Manipulation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 High Severity AIR Alert | elementary | 64 |  |
| Audit CVE Event | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Audit-CVE |
| Turla Named Pipes | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Netsh RDP Port Forwarding | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Malspam Execution Registering Malicious DLL | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Mustang Panda Dropper | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| IcedID Execution Using Excel | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Invoke-TheHash Commandlets | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4704' style='color: inherit;'>4704</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 Email Forwarding To Privacy Email Address | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| Wdigest Enable UseLogonCredential | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| APT29 Fake Google Update Service Install | elementary | <span style="color:#B60016">7045</span> | Service Control Manager |
| Malicious Service Installations | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Suspicious VBS Execution Parameter | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| SysKey Registry Keys Access | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Smbexec.py Service Installation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| CVE-2019-0708 Scan | elementary | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a> | Microsoft-Windows-Security-Auditing |
| Phosphorus (APT35) Exchange Discovery | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Ryuk Ransomware Command Line | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Debugging Software Deactivation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Windows Update LolBins | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Mshta JavaScript Execution | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Mimikatz Basic Commands | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Suspicious Netsh DLL Persistence | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Raccine Uninstall | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Winword Document Droppers | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Disable Task Manager Through Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| WMI Persistence Command Line Event Consumer | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Office Startup Add-In | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Copying Sensitive Files With Credential Data | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| ICacls Granting Access To All | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Empire Monkey Activity | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Active Directory Shadow Credentials | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Netsh Port Forwarding | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exploited CVE-2020-10189 Zoho ManageEngine | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Cobalt Strike Default Service Creation Usage | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| PowerShell Downgrade Attack | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| OneNote Suspicious Children Process | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| WMI Install Of Binary | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Sign-in With No User Agent | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> |  |
| Ursnif Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Copying Browser Files With Credentials | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DNS Tunnel Technique From MuddyWater | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Credential Dumping By LaZagne | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Comsvcs | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Antivirus Web Shell Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| RTLO Character | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Windows Credential Editor Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 Medium Severity AIR Alert | elementary | 64 |  |
| Office Application Startup Office Test | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Entra ID (Azure AD) Domain Trust Modification | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>8</a></span> |  |
| Active Directory Database Dump Via Ntdsutil | elementary | 325 | ESENT |
| Blue Mockingbird Malware | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suncrypt Parameters | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Leviathan Registry Key Activity | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| HackTools Suspicious Names | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Kernel-File, Microsoft-Windows-Sysmon |
| FlowCloud Malware | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2015-1641 | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Antivirus Relevant File Paths Alerts | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Microsoft Defender Antivirus Signatures Removed With MpCmdRun | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Domain Trust Discovery Through LDAP | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-REDACTED-Security-Auditing, Microsoft-Windows-Sysmon |
| Phorpiex Process Masquerading | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| TrustedInstaller Impersonation | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| PasswordDump SecurityXploded Tool | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Phorpiex DriveMgr Command | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Windows ANONYMOUS LOGON Local Account Created | elementary | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Disable Workstation Lock | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Dropped File | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Sticky Key Like Backdoor Usage | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Security Support Provider (SSP) Added to LSA Configuration | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Impacket Wmiexec Module | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| UAC Bypass Via Sdclt | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Meterpreter or Cobalt Strike Getsystem Service Installation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon, Service Control Manager |
| Microsoft 365 Suspicious Inbox Rule | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| Microsoft Defender Antivirus History Directory Deleted | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| AdFind Usage | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell AMSI Deactivation Bypass Using .NET Reflection | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Msdt (Follina) File Browse Process Execution | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Schtasks Persistence With High Privileges | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Antivirus Password Dumper Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Dumpert LSASS Process Dumper | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Rdrleakdiag | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| RYUK Ransomeware - martinstevens Username | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Lazarus Loaders | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Createdump | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Elise Backdoor | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Equation Group DLL_U Load | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious HWP Child Process | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Antivirus Exploitation Framework Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Suspicious Headless Web Browser Execution To Download File | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |

## EventIDs occurences in rules
| EventID | Number of rules concerned | Percentage of rules concerned (Total rules: 445) |
| ------- | ------------------------- | ------------------------------------------------------ |
| 1 | 218 | 48.99 % |
| 13 | 45 | 10.11 % |
| 4104 | 43 | 9.66 % |
| 11 | 20 | 4.49 % |
| 7 | 15 | 3.37 % |
| 5 | 15 | 3.37 % |
| 5145 | 11 | 2.47 % |
| 7045 | 11 | 2.47 % |
| 4656 | 8 | 1.8 % |
| 4688 | 7 | 1.57 % |
| 15 | 7 | 1.57 % |
| 3 | 6 | 1.35 % |
| 10 | 6 | 1.35 % |
| 17 | 6 | 1.35 % |
| 4697 | 6 | 1.35 % |
| 98 | 6 | 1.35 % |
| 4663 | 6 | 1.35 % |
| 4662 | 6 | 1.35 % |
| 5136 | 6 | 1.35 % |
| 4624 | 5 | 1.12 % |
| 1116 | 5 | 1.12 % |
| 64 | 4 | 0.9 % |
| 22 | 4 | 0.9 % |
| 4103 | 4 | 0.9 % |
| 6 | 3 | 0.67 % |
| 4625 | 3 | 0.67 % |
| 12 | 3 | 0.67 % |
| 4720 | 3 | 0.67 % |
| 1033 | 2 | 0.45 % |
| 4729 | 2 | 0.45 % |
| 25 | 2 | 0.45 % |
| 5007 | 2 | 0.45 % |
| 30 | 2 | 0.45 % |
| 20 | 2 | 0.45 % |
| 8 | 2 | 0.45 % |
| 4799 | 2 | 0.45 % |
| 4728 | 2 | 0.45 % |
| 4704 | 1 | 0.22 % |
| 1032 | 1 | 0.22 % |
| 1034 | 1 | 0.22 % |
| 1031 | 1 | 0.22 % |
| 4661 | 1 | 0.22 % |
| 4674 | 1 | 0.22 % |
| 770 | 1 | 0.22 % |
| 771 | 1 | 0.22 % |
| 150 | 1 | 0.22 % |
| 47 | 1 | 0.22 % |
| 4825 | 1 | 0.22 % |
| 4743 | 1 | 0.22 % |
| 1000 | 1 | 0.22 % |
| 8001 | 1 | 0.22 % |
| 4794 | 1 | 0.22 % |
| 1127 | 1 | 0.22 % |
| 5001 | 1 | 0.22 % |
| 5101 | 1 | 0.22 % |
| 5010 | 1 | 0.22 % |
| 5012 | 1 | 0.22 % |
| 2013 | 1 | 0.22 % |
| 27 | 1 | 0.22 % |
| 4776 | 1 | 0.22 % |
| 19 | 1 | 0.22 % |
| 21 | 1 | 0.22 % |
| 5154 | 1 | 0.22 % |
| 4673 | 1 | 0.22 % |
| 1125 | 1 | 0.22 % |
| 1126 | 1 | 0.22 % |
| 1006 | 1 | 0.22 % |
| 1007 | 1 | 0.22 % |
| 1008 | 1 | 0.22 % |
| 1015 | 1 | 0.22 % |
| 1117 | 1 | 0.22 % |
| 1118 | 1 | 0.22 % |
| 1119 | 1 | 0.22 % |
| 5140 | 1 | 0.22 % |
| 4657 | 1 | 0.22 % |
| 325 | 1 | 0.22 % |
| 16 | 1 | 0.22 % |
| 5156 | 1 | 0.22 % |
| 524 | 1 | 0.22 % |
| 4754 | 1 | 0.22 % |
| 4756 | 1 | 0.22 % |
| 4757 | 1 | 0.22 % |
| 4758 | 1 | 0.22 % |
| 4727 | 1 | 0.22 % |
| 4730 | 1 | 0.22 % |
| 4764 | 1 | 0.22 % |
| 4706 | 1 | 0.22 % |
| 4707 | 1 | 0.22 % |
| 40 | 1 | 0.22 % |
| 4742 | 1 | 0.22 % |
| 4649 | 1 | 0.22 % |
| 517 | 1 | 0.22 % |
| 1102 | 1 | 0.22 % |
| 4738 | 1 | 0.22 % |
| 4732 | 1 | 0.22 % |
| 4611 | 1 | 0.22 % |
| 4658 | 1 | 0.22 % |
| 1013 | 1 | 0.22 % |
| 6416 | 1 | 0.22 % |

## EventProviders occurences in rules
| EventProvider | Number of rules concerned | Percentage of rules concerned (Total rules: 445) |
| ------- | ------------------------- | ------------------------------------------------------ |
| Microsoft-Windows-Sysmon | 290 | 65.17 % |
| Microsoft-Windows-Security-Auditing | 68 | 15.28 % |
| Microsoft-Windows-PowerShell | 47 | 10.56 % |
| Kernel-Process | 19 | 4.27 % |
| Service Control Manager | 11 | 2.47 % |
| Microsoft-Windows-Windows Defender | 9 | 2.02 % |
| Microsoft-Windows-Kernel-File | 4 | 0.9 % |
| Microsoft-Windows-Audit-CVE | 1 | 0.22 % |
| Microsoft-Windows-DHCP-Server | 1 | 0.22 % |
| Microsoft-Windows-DNS-Server-Service | 1 | 0.22 % |
| Microsoft-Windows-Kernel-Process | 1 | 0.22 % |
| Application Error | 1 | 0.22 % |
| Microsoft-Windows-NTLM | 1 | 0.22 % |
| ESENT | 1 | 0.22 % |
| Microsoft-Windows-Kernel-General | 1 | 0.22 % |
| Microsoft-Windows-Backup | 1 | 0.22 % |
| Microsoft-REDACTED-Security-Auditing | 1 | 0.22 % |
| Microsoft-Windows-DNS-Client | 1 | 0.22 % |
| Microsoft-Windows-Eventlog | 1 | 0.22 % |

## EffortLevel x EventIDs
| Effort Level | EventIDs | Number of related rules | Percentage of related rules (Total rules: 445 |
| ------------ | -------- | ----------------------- | ------------------------------------------------------- |
| master | 1, 10, 1013, 11, 12, 13, 15, 150, 17, 22, 25, 27, 3, 40, 4104, 4611, 4624, 4625, 4656, 4661, 4662, 4663, 4673, 4674, 4720, 4727, 4728, 4729, 4730, 4743, 4754, 4756, 4757, 4758, 4764, 5007, 5140, 5145, 7, 770, 771, 8001, 98 | 78 | 17.53 % |
| advanced | 1, 10, 11, 1127, 13, 15, 17, 19, 20, 2013, 21, 22, 3, 4103, 4104, 4624, 4625, 4656, 4662, 4688, 4706, 4707, 4776, 4799, 5, 5001, 5010, 5012, 5101, 5136, 5145, 5154, 5156, 64, 6416, 7, 7045, 8 | 106 | 23.82 % |
| intermediate | 1, 10, 1000, 1006, 1007, 1008, 1015, 1031, 1032, 1033, 1034, 11, 1102, 1116, 1117, 1118, 1119, 1125, 1126, 12, 13, 15, 16, 17, 20, 22, 3, 30, 4103, 4104, 4624, 4649, 4656, 4657, 4658, 4662, 4663, 4688, 4697, 47, 4720, 4732, 4738, 4742, 4794, 4799, 4825, 5, 5136, 5145, 517, 524, 6, 64, 7, 7045 | 169 | 37.98 % |
| elementary | 1, 10, 11, 1116, 13, 15, 17, 325, 4103, 4104, 4625, 4656, 4663, 4688, 4697, 4704, 4720, 5, 5136, 6, 64, 7, 7045, 8 | 92 | 20.67 % |