# Built-in detection rules, EventIDs and EventProviders relations
SEKOIA.IO provides built-in detection rules to illuminate intrusions, adversarial behaviours and suspicious activity escalation chains so you can immediately take steps to remediate. Built-in rules can be customized to your context and according to your security posture.
This page aims at helping partners & customers in having their detection coverage by knowing which Event IDs and [Event Providers](https://learn.microsoft.com/en-us/windows/win32/etw/providing-events) are used by rule. **Please note this was retrieved automatically from our tests samples when generating attacks that triggered the rules. It might not be exhaustive and concerns mostly Windows-related rules.** _Last update on 2023-09-05_

The colors of the EventIDs in this page should be interpreted as follow:

  - <span style='color:#B60016'>Red</span>: This EventID is not logged by default on a Windows 10+ or Windows Server 2016+ machine.
  - <span style='color:#D89462'>Orange</span>: This EventID is logged by default on a Windows 10+ or Windows Server 2016+ machine but upgrading its configuration would greatly help detection. For instance, the EventID 4688 is logged by default, but logging the command line is incredibly helpful for the rules since almost 50% of our rules use command line for detection (usually showed as EventID 1 in this page).
  - <span style='color:#6a18a0'>Purple</span>: This EventID is logged by default if you have Windows Defender activated.
  - <span style='color:#5865d3'>Blue</span>: This EventID is only logged if you have Sysmon. **Our rules will have a master Effort Level if the recommended Sysmon Configuration is not enough and needs to be modified. Please be aware that a modification of Sysmon Configuration can greatly increase events logging in your network, which SEKOIA.IO can't know about and therefore is not responsible for that.**

## Rules x Effort Level x EventIDs x Event Providers
| Rule Name | Effort Level | EventIDs | Event Providers |
| --------- | ------------ | -------- | --------------- |
| Usage Of Sysinternals Tools | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS New Country | master | 98 |  |
| Svchost DLL Search Order Hijack | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| SCM Database Privileged Operation | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4674' style='color: inherit;'>4674</a></span> | Microsoft-Windows-Security-Auditing |
| User Account Deleted | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4743' style='color: inherit;'>4743</a></span> | Microsoft-Windows-Security-Auditing |
| Network Share Discovery | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Abusing Azure Browser SSO | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Disable Using Registry | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Admin Share Access | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5140' style='color: inherit;'>5140</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Malware Persistence Registry Key | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) MCAS Inbox Hiding | master | 98 |  |
| Microsoft Defender Antivirus History Deleted | master | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1013</a></span> | Microsoft-Windows-Windows Defender |
| Process Hollowing Detection | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>25</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Microsoft Defender Antivirus Exclusion Command | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMI DLL Loaded Via Office | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Suspicious New Printer Ports In Registry | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Account Added To A Security Enabled Group | master | <span style="color:#D89462">4728</span> | Microsoft-Windows-Security-Auditing |
| List Shadow Copies | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Protected Storage Service Access | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| CVE-2021-34527 - PrintNightmare - Suspicious Actions From Spoolsv | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Execution From Suspicious Folder | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Process Herpaderping | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>25</a></span> | Microsoft-Windows-Sysmon |
| Narrator Feedback-Hub Persistence | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Potential RDP Connection To Non-Domain Host | master | <span style="color:#B60016">8001</span> | Microsoft-Windows-NTLM |
| PowerShell Malicious PowerShell Commandlets | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| AD Privileged Users Or Groups Reconnaissance | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4661' style='color: inherit;'>4661</a></span> | Microsoft-Windows-Security-Auditing |
| Advanced IP Scanner | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| In-memory PowerShell | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| DNS ServerLevelPluginDll Installation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Configuration Changed | master | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5007</a></span> | Microsoft-Windows-Windows Defender |
| Registry Checked For Lanmanserver DisableCompression Parameter | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Failed Logon Source From Public IP Addresses | master | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a> | Microsoft-Windows-Security-Auditing |
| Netsh Port Opening | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Key Linking | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| AD User Enumeration | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Windows Firewall Changes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DNS Server Error Failed Loading The ServerLevelPluginDLL | master | 150, 770, 771 | Microsoft-Windows-DNS-Server-Service |
| WMIC Loading Scripting Libraries | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Office Creating Suspicious File | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| User Couldn't Call A Privileged Service LsaRegisterLogonProcess | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4673' style='color: inherit;'>4673</a></span> | Microsoft-Windows-Security-Auditing |
| Data Compressed With Rar | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious PsExec Execution | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious Access To Sensitive File Extensions | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Putty Sessions Listing | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon |
| Stop Backup Services | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Disable Security Events Logging Adding Reg Key MiniNt | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| xWizard Execution | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Admin User RDP Remote Logon | master | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| FoggyWeb Backdoor DLL Loading | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Sysmon Windows File Block Executable | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>27</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Exclusion Configuration | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5007</a></span> | Microsoft-Windows-Sysmon, Microsoft-Windows-Windows Defender |
| CVE-2017-11882 Microsoft Office Equation Editor Vulnerability | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| Windows Defender Deactivation Using PowerShell Script | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Microsoft 365 (Office 365) MCAS Repeated Failed Login | master | 98 |  |
| Microsoft 365 Device Code Authentication | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> |  |
| Cobalt Strike Named Pipes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| SCM Database Handle Failure | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| Autorun Keys Modification | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span> | Microsoft-Windows-Sysmon |
| Remote Registry Management Using Reg Utility | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Webshell Creation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Sysmon |
| LSASS Memory Dump | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| TOR Usage Generic Rule | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| File Or Folder Permissions Modifications | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rubeus Register New Logon Process | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4611' style='color: inherit;'>4611</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) MCAS Risky IP | master | 98 |  |
| LSASS Access From Non System Account | master | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Credential Dumping-Tools Common Named Pipes | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DLL Loaded Via Office Applications | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| FromBase64String Command Line | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Account Removed From A Security Enabled Group | master | <span style="color:#D89462">4729</span> | Microsoft-Windows-Security-Auditing |
| Net.exe User Account Creation | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys | master | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Privileged AD Builtin Group Modified | master | <span style="color:#D89462">4727</span>, <span style="color:#D89462">4728</span>, <span style="color:#D89462">4729</span>, <span style="color:#D89462">4730</span>, <span style="color:#D89462">4754</span>, <span style="color:#D89462">4756</span>, <span style="color:#D89462">4757</span>, <span style="color:#D89462">4758</span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4764' style='color: inherit;'>4764</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) MCAS Repeated Delete | master | 98 |  |
| User Account Created | master | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) MCAS Detection Velocity | master | 98 |  |
| Telegram Bot API Request | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| Alternate PowerShell Hosts Pipe | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| Legitimate Process Execution From Unusual Folder | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Sysmon |
| Account Tampering - Suspicious Failed Logon Reasons | advanced | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4776' style='color: inherit;'>4776</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious Control Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Winword wrong parent | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| RDP Session Discovery | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rubeus Tool Command-line | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Change Default File Association | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Hiding Files With Attrib.exe | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Netsh Allow Command | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell - NTFS Alternate Data Stream | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| WMI Event Subscription | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>19</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>20</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>21</a></span> | Microsoft-Windows-Sysmon |
| Cmd.exe Used To Run Reconnaissance Commands | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Cmd.exe Command Line | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Csrss Wrong Parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Outbound Kerberos Connection | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5156' style='color: inherit;'>5156</a></span> | Microsoft-Windows-Security-Auditing |
| Lateral Movement - Remote Named Pipe | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft Defender for Office 365 Low Severity AIR Alert Handled Automatically | advanced | 64 |  |
| Malicious PowerShell Keywords | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Unsigned Image Loaded Into LSASS Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Dynwrapx Module Loading | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Webshell Execution W3WP Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious Nishang PowerShell Commandlets | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Python Opening Ports | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5154' style='color: inherit;'>5154</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious PROCEXP152.sys File Created In Tmp | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| External Disk Drive Or USB Storage Device | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-6416' style='color: inherit;'>6416</a></span> | Microsoft-Windows-Security-Auditing |
| PowerShell EncodedCommand | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Winlogon wrong parent | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PrinterPorts Creation (CVE-2020-1048) | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| New Service Creation | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| WMI Persistence Script Event Consumer File Write | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Adexplorer Usage | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious XOR Encoded PowerShell Command Line | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Rclone Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerView commandlets 1 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Windows DNS Queries | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| Active Directory Replication from Non Machine Account | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Svchost Wrong Parent | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| Active Directory Replication User Backdoor | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious PowerShell Keywords | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Suspicious ADSI-Cache Usage By Unknown Tool | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Control Panel Items | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Logon Scripts (UserInitMprLogonScript) | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Tampering Detected | advanced | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1127</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>2013</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5001</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5010</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5012</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>5101</a></span> | Microsoft-Windows-Windows Defender |
| PowerShell Data Compressed | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Disabled IE Security Features | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| NTDS.dit File In Suspicious Directory | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2017-0261 Or CVE-2017-0262 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| RDP Sensitive Settings Changed | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| AccCheckConsole Executing Dll | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Domain Trust Created Or Removed | advanced | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4706' style='color: inherit;'>4706</a></span>, <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4707' style='color: inherit;'>4707</a></span> | Microsoft-Windows-Security-Auditing |
| PsExec Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Sysmon, Service Control Manager |
| Mimikatz LSASS Memory Access | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| PowerView commandlets 2 | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Load Of dbghelp/dbgcore DLL From Suspicious Process | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| XCopy Suspicious Usage | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CreateRemoteThread Common Process Injection | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>8</a></span> | Microsoft-Windows-Sysmon |
| Default Encoding To UTF-8 PowerShell | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Powershell AMSI Bypass | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Microsoft Office Product Spawning Windows Shell | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Taskhost or Taskhostw Suspicious Child Found | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Remote Service Activity Via SVCCTL Named Pipe | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Domain Group And Permission Enumeration | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Rare Logonui Child Found | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exfiltration And Tunneling Tools Execution | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Metasploit PSExec Service Creation | advanced | <span style="color:#B60016">7045</span> | Service Control Manager |
| PowerShell Invoke-Obfuscation Obfuscated IEX Invocation | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Powershell Web Request | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| SAM Registry Hive Handle Request | advanced | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious desktop.ini Action | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Search Order Hijacking | advanced | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Remote Privileged Group Enumeration | advanced | 4799 |  |
| PowerShell Execution Via Rundll32 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| IIS Module Installation Using AppCmd | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Desktopimgdownldr Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Restoration Abuse | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MavInject Process Injection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Audio Capture via PowerShell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| BazarLoader Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Lsass Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Malware Protection Engine Crash | intermediate | 1000 | Application Error |
| Microsoft Defender Antivirus Disable Services | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| MalwareBytes Uninstallation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Usage Of Procdump With Common Arguments | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Windows Script Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMIC Command To Determine The Antivirus | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Mshta Execution From Wmi | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Mshta Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Remote Enumeration of Lateral Movement Groups | intermediate | 4799 | Microsoft-Windows-Security-Auditing |
| Wmic Service Call | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Capture a network trace with netsh.exe | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| SolarWinds Wrong Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Specific | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Phosphorus Domain Controller Discovery | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| User Added to Local Administrators | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4732' style='color: inherit;'>4732</a></span> | Microsoft-Windows-Security-Auditing |
| Copy Of Legitimate System32 Executable | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Network Sniffing Windows | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Microsoft-Windows-Sysmon |
| SOCKS Tunneling Tool | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Impacket Secretsdump.py Tool | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| DHCP Server Error Failed Loading the CallOut DLL | intermediate | 1031, 1032, 1033, 1034 | Microsoft-Windows-DHCP-Server |
| Password Change On Directory Service Restore Mode (DSRM) Account | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4794' style='color: inherit;'>4794</a></span> | Microsoft-Windows-Security-Auditing |
| PowerShell Download From URL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Formbook File Creation DB1 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| WCE wceaux.dll Creation | intermediate | 30 | Microsoft-Windows-Kernel-File |
| Exchange Server Creating Unusual Files | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Suspicious SAM Dump | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>16</a></span> | Microsoft-Windows-Kernel-General |
| Microsoft Defender Antivirus Set-MpPreference Base64 Encoded | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| SolarWinds Suspicious File Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Exchange Server Spawning Suspicious Processes | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Powershell Winlogon Helper DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Hostname | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Disable .NET ETW Through COMPlus_ETWEnabled | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Denied Access To Remote Desktop | intermediate | 4825 | Microsoft-Windows-Security-Auditing |
| DNS Exfiltration and Tunneling Tools Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Registry Key Used By Some Old Agent Tesla Samples | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Ryuk Ransomware Persistence Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Disable SecurityHealth | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Spoolsv Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DC Shadow via Service Principal Name (SPN) creation | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4742' style='color: inherit;'>4742</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Taskhost Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Cred Dump Tools Dropped Files | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Userinit Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Pandemic Windows Implant | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Netsh Program Allowed With Suspicious Location | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Qakbot Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Data Compressed With Rar With Password | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Finger Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Commonly Used Commands To Stop Services And Remove Backups | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Secure Deletion With SDelete | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4658' style='color: inherit;'>4658</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| MOFComp Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Creation or Modification of a GPO Scheduled Task | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Microsoft 365 (Office 365) Malware Uploaded On SharePoint | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span> |  |
| Sliver DNS Beaconing | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>22</a></span> | Microsoft-Windows-Sysmon |
| Formbook Hijacked Process Command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Powershell UploadString Function | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Windows Installer Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Wmiprvse Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Email Forwarding To Consumer Email Address | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| New DLL Added To AppCertDlls Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Successful Overpass The Hash Attempt | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Suspicious Taskkill Command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DLL Loading By Ordinal | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| LSASS Memory Dump File Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| CertOC Loading Dll | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| GPO Executable Delivery | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Searchprotocolhost Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Non-Legitimate Executable Using AcceptEula Parameter | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process, Microsoft-Windows-Kernel-Process |
| Network Connection Via Certutil | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| Rare Lsass Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Explorer Process Executing HTA File | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Possible RottenPotato Attack | intermediate | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Venom Multi-hop Proxy agent detection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| MMC Spawning Windows Shell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Remote Task Creation Via ATSVC Named Pipe | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| Suspicious Driver Loaded | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Generic | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspect Svchost Memory Access | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Cmd File Copy Command To Network Share | intermediate | 30 | Microsoft-Windows-Kernel-File |
| Eventlog Cleared | intermediate | 517, <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-1102' style='color: inherit;'>1102</a> | Microsoft-Windows-Eventlog |
| Wsmprovhost Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Wininit Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Rundll32.exe Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Scheduled Task Creation | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| Active Directory Delegate To KRBTGT Service | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738' style='color: inherit;'>4738</a></span> | Microsoft-Windows-Security-Auditing |
| RDP Port Change Using Powershell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| DHCP Callout DLL Installation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Schtasks Suspicious Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Office Spawning Script | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Threat Detected | intermediate | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1006</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1007</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1008</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1015</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1117</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1118</a></span>, <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1119</a></span>, 1125, 1126 | Microsoft-Windows-Windows Defender |
| Transfering Files With Credential Data Via Network Shares | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145' style='color: inherit;'>5145</a></span> | Microsoft-Windows-Security-Auditing |
| DCSync Attack | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| New Or Renamed User Account With '$' In Attribute 'SamAccountName' | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Grabbing Sensitive Hives Via Reg Utility | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NjRat Registry Changes | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) AtpDetection | intermediate | 47 |  |
| Credential Dumping Tools Service Execution | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| Active Directory User Backdoors | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| COM Hijack Via Sdclt | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| StoneDrill Service Install | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| Possible Replay Attack | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4649' style='color: inherit;'>4649</a></span> | Microsoft-Windows-Security-Auditing |
| Bloodhound and Sharphound Tools Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Clear EventLogs Through CommandLine | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Sysprep On AppData Folder | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Hijack Legit RDP Session To Move Laterally | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| CMSTP UAC Bypass via COM Object Access | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Commands From MS SQL Server Shell | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| OneNote Embedded File | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Password Dumper Activity On LSASS | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span> | Microsoft-Windows-Security-Auditing |
| DPAPI Domain Backup Key Extraction | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Exploiting SetupComplete.cmd CVE-2019-1378 | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NTDS.dit File Interaction Through Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Koadic Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Cmdkey Cached Credentials Recon | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DLL Load via LSASS Registry Key | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>12</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| SquirrelWaffle Malspam Execution Loading DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus Disable Scheduled Tasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Netsh RDP Port Opening | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Gpscript Suspicious Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Inhibit System Recovery Deleting Backups | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Exfiltration Domain In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Mshta Suspicious Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| MS Office Product Spawning Exe in User Dir | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Email Forwarding To Email Address With Rare TLD | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| OceanLotus Registry Activity | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Spyware Persistence Using Schtasks | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Werfault DLL Injection | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Backup Catalog Deleted | intermediate | 524 | Microsoft-Windows-Backup |
| Suspicious Network Args In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process, Microsoft-Windows-Sysmon |
| Suspicious DNS Child Process | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Searchindexer Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious LDAP-Attributes Used | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136' style='color: inherit;'>5136</a></span> | Microsoft-Windows-Security-Auditing |
| Netsh Allowed Python Program | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| STRRAT Scheduled Task | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Scripting In A WMI Consumer | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>20</a></span> | Microsoft-Windows-Sysmon |
| QakBot Process Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| XSL Script Processing And SquiblyTwo Attack | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Malicious Named Pipe | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| UAC Bypass Using Fodhelper | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Disable Windows Defender Credential Guard | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Outlook Child Process | intermediate | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688' style='color: inherit;'>4688</a></span> | Microsoft-Windows-Security-Auditing |
| NlTest Usage | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Csrss Child Found | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious DLL side loading from ProgramData | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 Low Severity AIR Alert Requires Action | intermediate | 64 |  |
| Chafer (APT 39) Activity | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Detection of default Mimikatz banner | intermediate | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| WMIC Uninstall Product | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exchange Mailbox Export | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| ETW Tampering | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 (Office 365) Malware Uploaded On OneDrive | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span> |  |
| Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Suspicious certutil command | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MSBuild Abuse | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>3</a></span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Ngrok Process Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Winrshost Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| KeePass Config XML In Command-Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMImplant Hack Tool | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| NetNTLM Downgrade Attack | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4657' style='color: inherit;'>4657</a></span> | Microsoft-Windows-Sysmon |
| Python HTTP Server | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| MMC20 Lateral Movement | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Process Requiring DLL Starts Without DLL | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Logonui Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerCat Function Loading | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Suspicious Regsvr32 Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| NetSh Used To Disable Windows Firewall | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| HackTools Suspicious Process Names In Command Line | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| High Privileges Network Share Removal | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Lsass Access Through WinRM | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| TUN/TAP Driver Installation | intermediate | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Trickbot Malware Activity | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CMSTP Execution | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Wmic Process Call Creation | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Smss Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Taskhostw Wrong Parent | intermediate | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| DHCP Server Loaded the CallOut DLL | intermediate | 1033 |  |
| Antivirus Relevant File Paths Alerts | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Turla Named Pipes | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span> | Microsoft-Windows-Sysmon |
| WiFi Credentials Harvesting Using Netsh | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Disable Task Manager Through Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Schtasks Persistence With High Privileges | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Exploited CVE-2020-10189 Zoho ManageEngine | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Leviathan Registry Key Activity | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| RTLO Character | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Meterpreter or Cobalt Strike Getsystem Service Installation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>17</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon, Service Control Manager |
| DNS Tunnel Technique From MuddyWater | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| UAC Bypass via Event Viewer | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Smbexec.py Service Installation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>6</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Credential Dumping By LaZagne | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>10</a></span> | Microsoft-Windows-Sysmon |
| Cobalt Strike Default Beacons Names | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| AdFind Usage | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Registry Manipulation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Windows Credential Editor Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Outlook Registry Access | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Empire Monkey Activity | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| AD Object WriteDAC Access | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662' style='color: inherit;'>4662</a></span> | Microsoft-Windows-Security-Auditing |
| Debugging Software Deactivation | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Security Support Provider (SSP) Added to LSA Configuration | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| HackTools Suspicious Process Names | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Microsoft-Windows-Sysmon |
| SysKey Registry Keys Access | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656' style='color: inherit;'>4656</a></span>, <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663' style='color: inherit;'>4663</a></span> | Microsoft-Windows-Security-Auditing |
| Sticky Key Like Backdoor Usage | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Netsh RDP Port Forwarding | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Suspicious Inbox Rule | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| Suncrypt Parameters | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Process Memory Dump Using Rdrleakdiag | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| APT29 Fake Google Update Service Install | elementary | <span style="color:#B60016">7045</span> | Service Control Manager |
| RedMimicry Winnti Playbook Dropped File | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| ICacls Granting Access To All | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Domain Trust Discovery Through LDAP | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Antivirus Password Dumper Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Mustang Panda Dropper | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| RYUK Ransomeware - martinstevens Username | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Wdigest Enable UseLogonCredential | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Mshta JavaScript Execution | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| TrustedInstaller Impersonation | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Copying Sensitive Files With Credential Data | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| IcedID Execution Using Excel | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell AMSI Deactivation Bypass Using .NET Reflection | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| PasswordDump SecurityXploded Tool | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft 365 Email Forwarding To Privacy Email Address | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> |  |
| Office Application Startup Office Test | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Lazarus Loaders | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Impacket Wmiexec Module | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Downgrade Attack | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Invoke-TheHash Commandlets | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Microsoft Defender Antivirus Signatures Removed With MpCmdRun | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Createdump | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Kernel-Process |
| Antivirus Exploitation Framework Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| Exploit For CVE-2015-1641 | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Windows Update LolBins | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious VBS Execution Parameter | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Netsh DLL Persistence | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| PowerShell Credential Prompt | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| WMI Persistence Command Line Event Consumer | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span> | Microsoft-Windows-Sysmon |
| Phorpiex Process Masquerading | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Equation Group DLL_U Load | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Ryuk Ransomware Command Line | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Office Startup Add-In | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Phorpiex DriveMgr Command | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Headless Web Browser Execution To Download File | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Kernel-Process |
| Disable Workstation Lock | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Comsvcs | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| WMI Install Of Binary | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| CVE-2019-0708 Scan | elementary | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625' style='color: inherit;'>4625</a> | Microsoft-Windows-Security-Auditing |
| Active Directory Database Dump Via Ntdsutil | elementary | 325 | ESENT |
| Antivirus Web Shell Detection | elementary | <span style="color:#6a18a0"><a href='https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide' style='color: inherit;'>1116</a></span> | Microsoft-Windows-Windows Defender |
| RDP Login From Localhost | elementary | <a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624' style='color: inherit;'>4624</a> | Microsoft-Windows-Security-Auditing |
| Malspam Execution Registering Malicious DLL | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Cobalt Strike Default Service Creation Usage | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Elise Backdoor | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Ursnif Registry Key | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Blue Mockingbird Malware | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Dllhost Wrong Parent | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Raccine Uninstall | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Mimikatz Basic Commands | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Phosphorus (APT35) Exchange Discovery | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Microsoft Entra ID (Azure AD) Domain Trust Modification | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>8</a></span> |  |
| Winword Document Droppers | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Double Extension | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>5</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 Medium Severity AIR Alert | elementary | 64 |  |
| UAC Bypass Via Sdclt | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| Suspicious HWP Child Process | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender for Office 365 High Severity AIR Alert | elementary | 64 |  |
| OneNote Suspicious Children Process | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>15</a></span> | Microsoft-Windows-Sysmon |
| Explorer Wrong Parent | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Malicious Service Installations | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697' style='color: inherit;'>4697</a></span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Dumpert LSASS Process Dumper | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>7</a></span>, <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>11</a></span> | Microsoft-Windows-Sysmon |
| Suspicious Windows ANONYMOUS LOGON Local Account Created | elementary | <span style="color:#D89462"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720' style='color: inherit;'>4720</a></span> | Microsoft-Windows-Security-Auditing |
| Copying Browser Files With Credentials | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Microsoft Defender Antivirus History Directory Deleted | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Sysmon |
| Msdt (Follina) File Browse Process Execution | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| FlowCloud Malware | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>13</a></span> | Microsoft-Windows-Sysmon |
| SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory | elementary | <span style="color:#B60016"><a href='https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4704' style='color: inherit;'>4704</a></span> | Microsoft-Windows-Security-Auditing |
| Audit CVE Event | elementary | <span style="color:#5865d3"><a href='https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events' style='color: inherit;'>1</a></span> | Microsoft-Windows-Audit-CVE |

## EventIDs occurences in rules
| EventID | Number of rules concerned | Percentage of rules concerned (Total rules: 431) |
| ------- | ------------------------- | ------------------------------------------------------ |
| 1 | 216 | 50.12 % |
| 13 | 44 | 10.21 % |
| 4104 | 42 | 9.74 % |
| 11 | 18 | 4.18 % |
| 7 | 15 | 3.48 % |
| 5145 | 11 | 2.55 % |
| 7045 | 11 | 2.55 % |
| 5 | 9 | 2.09 % |
| 4656 | 8 | 1.86 % |
| 17 | 6 | 1.39 % |
| 98 | 6 | 1.39 % |
| 15 | 6 | 1.39 % |
| 4697 | 6 | 1.39 % |
| 10 | 6 | 1.39 % |
| 4662 | 6 | 1.39 % |
| 4663 | 6 | 1.39 % |
| 1116 | 5 | 1.16 % |
| 4688 | 5 | 1.16 % |
| 4624 | 5 | 1.16 % |
| 5136 | 5 | 1.16 % |
| 3 | 5 | 1.16 % |
| 64 | 4 | 0.93 % |
| 22 | 3 | 0.7 % |
| 4625 | 3 | 0.7 % |
| 6 | 3 | 0.7 % |
| 4103 | 3 | 0.7 % |
| 4720 | 3 | 0.7 % |
| 12 | 3 | 0.7 % |
| 4799 | 2 | 0.46 % |
| 1033 | 2 | 0.46 % |
| 25 | 2 | 0.46 % |
| 20 | 2 | 0.46 % |
| 30 | 2 | 0.46 % |
| 4728 | 2 | 0.46 % |
| 5007 | 2 | 0.46 % |
| 8 | 2 | 0.46 % |
| 4729 | 2 | 0.46 % |
| 1000 | 1 | 0.23 % |
| 4776 | 1 | 0.23 % |
| 4674 | 1 | 0.23 % |
| 4743 | 1 | 0.23 % |
| 4732 | 1 | 0.23 % |
| 5140 | 1 | 0.23 % |
| 1032 | 1 | 0.23 % |
| 1034 | 1 | 0.23 % |
| 1031 | 1 | 0.23 % |
| 4794 | 1 | 0.23 % |
| 1013 | 1 | 0.23 % |
| 19 | 1 | 0.23 % |
| 21 | 1 | 0.23 % |
| 16 | 1 | 0.23 % |
| 4825 | 1 | 0.23 % |
| 5156 | 1 | 0.23 % |
| 4742 | 1 | 0.23 % |
| 8001 | 1 | 0.23 % |
| 4658 | 1 | 0.23 % |
| 5154 | 1 | 0.23 % |
| 4661 | 1 | 0.23 % |
| 6416 | 1 | 0.23 % |
| 517 | 1 | 0.23 % |
| 1102 | 1 | 0.23 % |
| 4738 | 1 | 0.23 % |
| 770 | 1 | 0.23 % |
| 771 | 1 | 0.23 % |
| 150 | 1 | 0.23 % |
| 4673 | 1 | 0.23 % |
| 1125 | 1 | 0.23 % |
| 1126 | 1 | 0.23 % |
| 1006 | 1 | 0.23 % |
| 1007 | 1 | 0.23 % |
| 1008 | 1 | 0.23 % |
| 1015 | 1 | 0.23 % |
| 1117 | 1 | 0.23 % |
| 1118 | 1 | 0.23 % |
| 1119 | 1 | 0.23 % |
| 47 | 1 | 0.23 % |
| 1127 | 1 | 0.23 % |
| 5001 | 1 | 0.23 % |
| 5101 | 1 | 0.23 % |
| 5010 | 1 | 0.23 % |
| 5012 | 1 | 0.23 % |
| 2013 | 1 | 0.23 % |
| 4649 | 1 | 0.23 % |
| 4706 | 1 | 0.23 % |
| 4707 | 1 | 0.23 % |
| 27 | 1 | 0.23 % |
| 325 | 1 | 0.23 % |
| 524 | 1 | 0.23 % |
| 4611 | 1 | 0.23 % |
| 4657 | 1 | 0.23 % |
| 4754 | 1 | 0.23 % |
| 4756 | 1 | 0.23 % |
| 4757 | 1 | 0.23 % |
| 4758 | 1 | 0.23 % |
| 4727 | 1 | 0.23 % |
| 4730 | 1 | 0.23 % |
| 4764 | 1 | 0.23 % |
| 4704 | 1 | 0.23 % |

## EventProviders occurences in rules
| EventProvider | Number of rules concerned | Percentage of rules concerned (Total rules: 431) |
| ------- | ------------------------- | ------------------------------------------------------ |
| Microsoft-Windows-Sysmon | 289 | 67.05 % |
| Microsoft-Windows-Security-Auditing | 66 | 15.31 % |
| Microsoft-Windows-PowerShell | 45 | 10.44 % |
| Service Control Manager | 11 | 2.55 % |
| Kernel-Process | 10 | 2.32 % |
| Microsoft-Windows-Windows Defender | 9 | 2.09 % |
| Microsoft-Windows-Kernel-File | 2 | 0.46 % |
| Application Error | 1 | 0.23 % |
| Microsoft-Windows-DHCP-Server | 1 | 0.23 % |
| Microsoft-Windows-Kernel-General | 1 | 0.23 % |
| Microsoft-Windows-NTLM | 1 | 0.23 % |
| Microsoft-Windows-Kernel-Process | 1 | 0.23 % |
| Microsoft-Windows-Eventlog | 1 | 0.23 % |
| Microsoft-Windows-DNS-Server-Service | 1 | 0.23 % |
| ESENT | 1 | 0.23 % |
| Microsoft-Windows-Backup | 1 | 0.23 % |
| Microsoft-Windows-Audit-CVE | 1 | 0.23 % |

## EffortLevel x EventIDs
| Effort Level | EventIDs | Number of related rules | Percentage of related rules (Total rules: 431 |
| ------------ | -------- | ----------------------- | ------------------------------------------------------- |
| master | 1, 10, 1013, 11, 12, 13, 15, 150, 17, 25, 27, 3, 4104, 4611, 4624, 4625, 4656, 4661, 4662, 4663, 4673, 4674, 4720, 4727, 4728, 4729, 4730, 4743, 4754, 4756, 4757, 4758, 4764, 5007, 5140, 5145, 7, 770, 771, 8001, 98 | 76 | 17.63 % |
| advanced | 1, 10, 11, 1127, 13, 15, 17, 19, 20, 2013, 21, 22, 4104, 4625, 4656, 4662, 4688, 4706, 4707, 4776, 4799, 5, 5001, 5010, 5012, 5101, 5136, 5145, 5154, 5156, 64, 6416, 7, 7045, 8 | 73 | 16.94 % |
| intermediate | 1, 10, 1000, 1006, 1007, 1008, 1015, 1031, 1032, 1033, 1034, 11, 1102, 1116, 1117, 1118, 1119, 1125, 1126, 12, 13, 15, 16, 17, 20, 22, 3, 30, 4103, 4104, 4624, 4649, 4656, 4657, 4658, 4662, 4663, 4688, 4697, 47, 4720, 4732, 4738, 4742, 4794, 4799, 4825, 5, 5136, 5145, 517, 524, 6, 64, 7, 7045 | 184 | 42.69 % |
| elementary | 1, 10, 11, 1116, 13, 15, 17, 325, 4103, 4104, 4624, 4625, 4656, 4662, 4663, 4697, 4704, 4720, 5, 6, 64, 7, 7045, 8 | 98 | 22.74 % |