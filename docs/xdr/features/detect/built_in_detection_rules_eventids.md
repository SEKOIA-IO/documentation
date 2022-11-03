---
show:
  - navigation
---

# Built-in detection rules, EventIDs and EventProviders relations

SEKOIA.IO provides built-in detection rules to illuminate intrusions, adversarial behaviours and suspicious activity escalation chains so you can immediately take steps to remediate. Built-in rules can be customized to your context and according to your security posture.

This page aims at helping partners & customers in having their detection coverage by knowing which Event IDs and [Event Providers](https://learn.microsoft.com/en-us/windows/win32/etw/providing-events) are used by rule. **Please note this was retrieved automatically from our tests samples when generating attacks that triggered the rules. It might not be exhaustive and concerns mostly Windows-related rules**


The colors in this page should be interpreted as follow:

  - For the EventIDs:
      * <span style='color:#B60016'>Red</span>: This EventID is not logged by default on a Windows 10+ or Windows Server 2016+ machine.
      * <span style='color:#D89462'>Orange</span>: This EventID is logged by default on a Windows 10+ or Windows Server 2016+ machine but upgrading its configuration would greatly help detection. For instance, the EventID 4688 is logged by default, but logging the command line is incredibly helpful for the rules since almost 50% of our rules use command line for detection (usually showed as EventID 1 in this page).
      * <span style='color:#6a18a0'>Purple</span>: This EventID is logged by default if you have Windows Defender activated.
      * <span style='color:#5865d3'>Blue</span>: This EventID is only logged if you have Sysmon. **Our rules will have a master Effort Level if the recommended Sysmon Configuration is not enough and needs to be modified. Please be aware that a modification of Sysmon Configuration can greatly increase events logging in your network, which SEKOIA.IO can't know about and therefore is not responsible for that.**

## Rules x Effort Level x EventIDs x Event Providers
| Rule Name | Effort Level | EventIDs | Event Providers |
| --------- | ------------ | -------- | --------------- |
| PowerShell Malicious PowerShell Commandlets | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Putty Sessions Listing | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span>, <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon |
| FoggyWeb Backdoor DLL Loading | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender History Deleted | master | <span style="color:#6a18a0">[1013](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Svchost DLL Search Order Hijack | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Rubeus Register New Logon Process | master | <span style="color:#B60016">[4611](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4611)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious DLL Loaded Via Office Applications | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious PsExec Execution | master | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Account Removed From A Security Enabled Group | master | <span style="color:#D89462">4729</span> | Microsoft-Windows-Security-Auditing |
| Netsh Port Opening | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| In-memory PowerShell | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Failed Logon Source From Public IP Addresses | master | [4625](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) | Microsoft-Windows-Security-Auditing |
| TOR Usage Generic Rule | master | <span style="color:#5865d3">[3](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Configuration Changed | master | <span style="color:#6a18a0">[5007](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Office 365 MCAS New Country | master | 98 |  |
| Registry Checked For Lanmanserver DisableCompression Parameter | master | <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Security-Auditing |
| DNS ServerLevelPluginDll Installation | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Advanced IP Scanner | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Network Share Discovery | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Usage Of Sysinternals Tools | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| LSASS Access From Non System Account | master | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span>, <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Security-Auditing |
| Local Account Deleted | master | [4726](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4726), <span style="color:#B60016">[4743](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4743)</span> | Microsoft-Windows-Security-Auditing |
| Protected Storage Service Access | master | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Admin Share Access | master | <span style="color:#B60016">[5140](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5140)</span>, <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Inbox Hiding | master | 98 |  |
| Office 365 MCAS Repeated Failed Login | master | 98 |  |
| WMIC Loading Scripting Libraries | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Autorun Keys Modification | master | <span style="color:#5865d3">[12](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DNS Server Error Failed Loading The ServerLevelPluginDLL | master | 150, 770, 771 | Microsoft-Windows-DNS-Server-Service |
| Disable Security Events Logging Adding Reg Key MiniNt | master | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Firewall Changes | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Webshell Creation | master | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span>, <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Sysmon |
| List Shadow Copies | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Sysmon Windows File Block Executable | master | <span style="color:#5865d3">[27](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| AD User Enumeration | master | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span> | Microsoft-Windows-Security-Auditing |
| WMI DLL Loaded Via Office | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Credential Dumping-Tools Common Named Pipes | master | <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Account Added To A Security Enabled Group | master | <span style="color:#D89462">4728</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Detection Velocity | master | 98 |  |
| Office 365 MCAS Repeated Delete | master | 98 |  |
| Local Account Created | master | <span style="color:#D89462">[4720](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)</span> | Microsoft-Windows-Security-Auditing |
| Potential RDP Connection To Non-Domain Host | master | <span style="color:#B60016">8001</span> | Microsoft-Windows-NTLM |
| Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys | master | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Access To Sensitive File Extensions | master | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Cobalt Strike Named Pipes | master | <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| User Couldn't Call A Privileged Service LsaRegisterLogonProcess | master | <span style="color:#B60016">[4673](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4673)</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Risky IP | master | 98 |  |
| CVE-2017-11882 Microsoft Office Equation Editor Vulnerability | master | <span style="color:#5865d3">[3](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Key Linking | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| SCM Database Handle Failure | master | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span> | Microsoft-Windows-Security-Auditing |
| Abusing Azure Browser SSO | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Admin User RDP Remote Logon | master | [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) | Microsoft-Windows-Security-Auditing |
| Suspicious New Printer Ports In Registry | master | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Remote Registry Management Using Reg Utility | master | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| SCM Database Privileged Operation | master | <span style="color:#B60016">[4674](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4674)</span> | Microsoft-Windows-Security-Auditing |
| Net.exe User Account Creation | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Narrator Feedback-Hub Persistence | master | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| CVE-2021-34527 - PrintNightmare - Suspicious Actions From Spoolsv | master | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| File Or Folder Permissions Modifications | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Stop Backup Services | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Deactivation Using PowerShell Script | master | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Process Herpaderping | master | <span style="color:#5865d3">[25](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Malware Persistence Registry Key | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| AD Privileged Users Or Groups Reconnaissance | master | <span style="color:#B60016">[4661](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4661)</span> | Microsoft-Windows-Security-Auditing |
| FromBase64String Command Line | master | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Process Hollowing Detection | master | <span style="color:#5865d3">[25](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Outbound Kerberos Connection | advanced | <span style="color:#B60016">[5156](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5156)</span> | Microsoft-Windows-Security-Auditing |
| PowerShell Invoke-Obfuscation Obfuscated IEX Invocation | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Remote Service Activity Via SVCCTL Named Pipe | advanced | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Exfiltration And Tunneling Tools Execution | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Alternate PowerShell Hosts Pipe | advanced | <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Powershell Web Request | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Active Directory Replication from Non Machine Account | advanced | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span> | Microsoft-Windows-Security-Auditing |
| Rare Logonui Child Found | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Logon Scripts (UserInitMprLogonScript) | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious desktop.ini Action | advanced | <span style="color:#5865d3">[15](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Winlogon wrong parent | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious XOR Encoded PowerShell Command Line | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Control Panel Items | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Taskhost or Taskhostw Suspicious Child Found | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Netsh Allow Command | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Metasploit PSExec Service Creation | advanced | <span style="color:#B60016">7045</span> | Service Control Manager |
| Default Encoding To UTF-8 PowerShell | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Rubeus Tool Command-line | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Domain Group And Permission Enumeration | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Active Directory Replication User Backdoor | advanced | <span style="color:#B60016">[5136](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136)</span> | Microsoft-Windows-Security-Auditing |
| Csrss Wrong Parent | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious PrinterPorts Creation (CVE-2020-1048) | advanced | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| XCopy Suspicious Usage | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Python Opening Ports | advanced | <span style="color:#B60016">[5154](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5154)</span> | Microsoft-Windows-Security-Auditing |
| Telegram Bot API Request | advanced | <span style="color:#5865d3">[22](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious PROCEXP152.sys File Created In Tmp | advanced | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Legitimate Process Execution From Unusual Folder | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[5](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">[4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)</span> | Microsoft-Windows-Sysmon |
| CreateRemoteThread Common Process Injection | advanced | <span style="color:#5865d3">[8](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Data Compressed | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Dynwrapx Module Loading | advanced | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows DNS Queries | advanced | <span style="color:#5865d3">[22](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Product Spawning Windows Shell | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Control Process | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious Nishang PowerShell Commandlets | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| External Disk Drive Or USB Storage Device | advanced | <span style="color:#B60016">[6416](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-6416)</span> | Microsoft-Windows-Security-Auditing |
| Load Of dbghelp/dbgcore DLL From Suspicious Process | advanced | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerView commandlets 2 | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| PowerView commandlets 1 | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| WMI Event Subscription | advanced | <span style="color:#5865d3">[19](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[20](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[21](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| NTDS.dit File In Suspicious Directory | advanced | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Lateral Movement - Remote Named Pipe | advanced | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Domain Trust Created Or Removed | advanced | <span style="color:#D89462">[4706](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4706)</span>, <span style="color:#D89462">[4707](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4707)</span> | Microsoft-Windows-Security-Auditing |
| Winword wrong parent | advanced | <span style="color:#D89462">[4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)</span> | Microsoft-Windows-Security-Auditing |
| Unsigned Image Loaded Into LSASS Process | advanced | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Search Order Hijacking | advanced | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMI Persistence Script Event Consumer File Write | advanced | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Privileged AD Builtin Group Modified | advanced | <span style="color:#D89462">4727</span>, <span style="color:#D89462">4728</span>, <span style="color:#D89462">4729</span>, <span style="color:#D89462">4730</span>, <span style="color:#D89462">4754</span>, <span style="color:#D89462">4756</span>, <span style="color:#D89462">4757</span>, <span style="color:#D89462">4758</span>, <span style="color:#D89462">[4764](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4764)</span> | Microsoft-Windows-Security-Auditing |
| PsExec Process | advanced | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Sysmon, Service Control Manager |
| Disabled IE Security Features | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Change Default File Association | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Rclone Process | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RDP Sensitive Settings Changed | advanced | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Adexplorer Usage | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| New Service Creation | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Account Tampering - Suspicious Failed Logon Reasons | advanced | [4625](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625), <span style="color:#B60016">[4776](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4776)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious PowerShell Keywords | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SAM Registry Hive Handle Request | advanced | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious ADSI-Cache Usage By Unknown Tool | advanced | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Cmd.exe Used To Run Reconnaissance Commands | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Cmd.exe Command Line | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Hiding Files With Attrib.exe | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RDP Session Discovery | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2017-0261 Or CVE-2017-0262 | advanced | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell - NTFS Alternate Data Stream | advanced | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Svchost Wrong Parent | advanced | <span style="color:#D89462">[4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Finger Usage | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious DLL Loading By Ordinal | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Clear EventLogs Through CommandLine | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Taskhostw Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Scripting In A WMI Consumer | intermediate | <span style="color:#5865d3">[20](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows Installer Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Wmic Process Call Creation | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Active Directory User Backdoors | intermediate | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span>, <span style="color:#B60016">[5136](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Windows Script Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| ETW Tampering | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Password Dumper Activity On LSASS | intermediate | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span> | Microsoft-Windows-Security-Auditing |
| Transfering Files With Credential Data Via Network Shares | intermediate | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| MS Office Product Spawning Exe in User Dir | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Powershell Winlogon Helper DLL | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| SquirrelWaffle Malspam Execution Loading DLL | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Office 365 Malware Uploaded On SharePoint | intermediate | <span style="color:#5865d3">[6](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> |  |
| NTDS.dit File Interaction Through Command Line | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Grabbing Sensitive Hives Via Reg Utility | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| LSASS Memory Dump | intermediate | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Credential Dumping Tools Service Execution | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| NjRat Registry Changes | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[12](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Koadic Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Mshta Execution From Wmi | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Hostname | intermediate | [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) | Microsoft-Windows-Security-Auditing |
| StoneDrill Service Install | intermediate | <span style="color:#B60016">7045</span> | Service Control Manager |
| MMC20 Lateral Movement | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Possible Replay Attack | intermediate | <span style="color:#B60016">[4649](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4649)</span> | Microsoft-Windows-Security-Auditing |
| Hijack Legit RDP Session To Move Laterally | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Audio Capture via PowerShell | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious LDAP-Attributes Used | intermediate | <span style="color:#B60016">[5136](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136)</span> | Microsoft-Windows-Security-Auditing |
| DPAPI Domain Backup Key Extraction | intermediate | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span> | Microsoft-Windows-Security-Auditing |
| Backup Catalog Deleted | intermediate | 524 | Microsoft-Windows-Backup |
| Exchange Server Spawning Suspicious Processes | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Disable Windows Defender Credential Guard | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| MSBuild Abuse | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[3](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Office 365 Malware Uploaded On OneDrive | intermediate | <span style="color:#5865d3">[6](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> |  |
| Suspicious PowerShell Invocations - Generic | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exchange Mailbox Export | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| MMC Spawning Windows Shell | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Denied Access To Remote Desktop | intermediate | 4825 | Microsoft-Windows-Security-Auditing |
| QakBot Process Creation | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Ngrok Process Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WCE wceaux.dll Creation | intermediate | 30 | Microsoft-Windows-Kernel-File |
| Qakbot Persistence Using Schtasks | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Impacket Secretsdump.py Tool | intermediate | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Suspect Svchost Memory Access | intermediate | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Explorer Process Executing HTA File | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Specific | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DC Shadow via Service Principal Name (SPN) creation | intermediate | <span style="color:#D89462">[4742](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4742)</span>, <span style="color:#B60016">[5136](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136)</span> | Microsoft-Windows-Security-Auditing |
| DHCP Server Error Failed Loading the CallOut DLL | intermediate | 1031, 1032, 1033, 1034 | Microsoft-Windows-DHCP-Server |
| Data Compressed With Rar With Password | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Lsass Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| NetSh Used To Disable Windows Firewall | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Wmiprvse Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exploiting SetupComplete.cmd CVE-2019-1378 | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Formbook Hijacked Process Command | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Creation or Modification of a GPO Scheduled Task | intermediate | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| LSASS Memory Dump File Creation | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| New Or Renamed User Account With '$' In Attribute 'SamAccountName' | intermediate | <span style="color:#D89462">[4720](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)</span> | Microsoft-Windows-Security-Auditing |
| Userinit Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Outlook Child Process | intermediate | <span style="color:#D89462">[4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)</span> | Microsoft-Windows-Security-Auditing |
| Netsh RDP Port Opening | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Network Connection Via Certutil | intermediate | <span style="color:#5865d3">[3](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Password Change On Directory Service Restore Mode (DSRM) Account | intermediate | <span style="color:#D89462">[4794](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4794)</span> | Microsoft-Windows-Security-Auditing |
| Successful Overpass The Hash Attempt | intermediate | [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) | Microsoft-Windows-Security-Auditing |
| Suspicious Taskkill Command | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| OceanLotus Registry Activity | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Remote Task Creation Via ATSVC Named Pipe | intermediate | <span style="color:#B60016">[5145](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)</span> | Microsoft-Windows-Security-Auditing |
| Capture a network trace with netsh.exe | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Rundll32.exe Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Logonui Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Wininit Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Netsh Allowed Python Program | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Network Args In Command Line | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Cred Dump Tools Dropped Files | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RDP Port Change Using Powershell | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| BazarLoader Persistence Using Schtasks | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMIC Command To Determine The Antivirus | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Ryuk Ransomware Persistence Registry Key | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Mimikatz LSASS Memory Access | intermediate | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Spoolsv Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Formbook File Creation DB1 | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Lsass Access Through WinRM | intermediate | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Registry Key Used By Some Old Agent Tesla Samples | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| NlTest Usage | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Detection of default Mimikatz banner | intermediate | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Taskhost Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| TUN/TAP Driver Installation | intermediate | <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Suspicious Regsvr32 Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious PowerShell Keywords | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Possible RottenPotato Attack | intermediate | [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) | Microsoft-Windows-Security-Auditing |
| Sysprep On AppData Folder | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Netsh Program Allowed With Suspicious Location | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| MalwareBytes Uninstallation | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| STRRAT Scheduled Task | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious SAM Dump | intermediate | <span style="color:#5865d3">[16](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Kernel-General |
| Exchange Server Creating Unusual Files | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Csrss Child Found | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Pandemic Windows Implant | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerCat Function Loading | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| COM Hijack Via Sdclt | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| DCSync Attack | intermediate | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span> | Microsoft-Windows-Security-Auditing |
| Cmdkey Cached Credentials Recon | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Spawning Script | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Eventlog Cleared | intermediate | 517, [1102](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-1102) | Microsoft-Windows-Eventlog |
| Suspicious Driver Loaded | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Commonly Used Commands To Stop Services And Remove Backups | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DLL Load via LSASS Registry Key | intermediate | <span style="color:#5865d3">[12](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Sliver DNS Beaconing | intermediate | <span style="color:#5865d3">[22](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| CMSTP Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Child Found | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| SolarWinds Suspicious File Creation | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Wsmprovhost Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Python HTTP Server | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Inhibit System Recovery Deleting Backups | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Scheduled Task Creation | intermediate | <span style="color:#D89462">[4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)</span> | Microsoft-Windows-Security-Auditing |
| Office 365 AtpDetection | intermediate | 47 |  |
| PowerShell Execution Via Rundll32 | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Creating Suspicious File | intermediate | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| MavInject Process Injection | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| CMSTP UAC Bypass via COM Object Access | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Desktopimgdownldr Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious certutil command | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Process Requiring DLL Starts Without DLL | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Active Directory Delegate To KRBTGT Service | intermediate | <span style="color:#D89462">[4738](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4738)</span> | Microsoft-Windows-Security-Auditing |
| DNS Exfiltration and Tunneling Tools Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Chafer (APT 39) Activity | intermediate | <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Microsoft Malware Protection Engine Crash | intermediate | 1000 | Application Error |
| Rare Lsass Child Found | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Trickbot Malware Activity | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Network Sniffing Windows | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[5](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| New DLL Added To AppCertDlls Registry Key | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious DLL side loading from ProgramData | intermediate | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Secure Deletion With SDelete | intermediate | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span>, <span style="color:#B60016">[4658](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4658)</span>, <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Security-Auditing |
| Searchindexer Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| XSL Script Processing And SquiblyTwo Attack | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Bloodhound and Sharphound Tools Usage | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| MOFComp Execution | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Schtasks Suspicious Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Disable .NET ETW Through COMPlus_ETWEnabled | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Tampering Detected | intermediate | <span style="color:#6a18a0">[1127](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[2013](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[5001](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[5010](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[5012](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[5101](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Suspicious DNS Child Process | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Malicious Named Pipe | intermediate | <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Download From URL | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| UAC Bypass Using Fodhelper | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Winrshost Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Smss Wrong Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| User Added to Local Administrators | intermediate | <span style="color:#D89462">[4732](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4732)</span> | Microsoft-Windows-Security-Auditing |
| NetNTLM Downgrade Attack | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">[4657](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4657)</span> | Microsoft-Windows-Sysmon |
| Gpscript Suspicious Parent | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Commands From MS SQL Server Shell | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMImplant Hack Tool | intermediate | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SolarWinds Wrong Child Process | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| KeePass Config XML In Command-Line | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DHCP Callout DLL Installation | intermediate | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMIC Uninstall Product | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Threat Detected | intermediate | <span style="color:#6a18a0">[1006](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1007](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1008](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1015](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1116](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1117](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1118](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span>, <span style="color:#6a18a0">[1119](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Spyware Persistence Using Schtasks | intermediate | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DHCP Server Loaded the CallOut DLL | intermediate | 1033 |  |
| Antivirus Password Dumper Detection | elementary | <span style="color:#6a18a0">[1116](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Mustang Panda Dropper | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Malicious Service Installations | elementary | <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Cobalt Strike Default Service Creation Usage | elementary | <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Winword Document Droppers | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Malspam Execution Registering Malicious DLL | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender History Directory Deleted | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Double Extension | elementary | <span style="color:#5865d3">[5](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Equation Group DLL_U Load | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PasswordDump SecurityXploded Tool | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Disabled Base64 Encoded | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Netsh RDP Port Forwarding | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Turla Named Pipes | elementary | <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Registry Manipulation | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| DNS Tunnel Technique From MuddyWater | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| APT29 Fake Google Update Service Install | elementary | <span style="color:#B60016">7045</span> | Service Control Manager |
| Explorer Wrong Parent | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Disable Task Manager Through Registry Key | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| UAC Bypass Via Sdclt | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Startup Add-In | elementary | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exploited CVE-2020-10189 Zoho ManageEngine | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Ursnif Registry Key | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory | elementary | <span style="color:#B60016">[4704](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4704)</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Netsh DLL Persistence | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| CVE-2019-0708 Scan | elementary | [4625](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) | Microsoft-Windows-Security-Auditing |
| WiFi Credentials Harvesting Using Netsh | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2015-1641 | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Smbexec.py Service Installation | elementary | <span style="color:#5865d3">[6](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Disable Workstation Lock | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Debugging Software Deactivation | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Credential Prompt | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Mshta JavaScript Execution | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Elise Backdoor | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious VBS Execution Parameter | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| FlowCloud Malware | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Schtasks Persistence With High Privileges | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| UAC Bypass via Event Viewer | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Sticky Key Like Backdoor Usage | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RYUK Ransomeware - martinstevens Username | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Security Support Provider (SSP) Added to LSA Configuration | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Phorpiex DriveMgr Command | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Audit CVE Event | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Audit-CVE |
| Invoke-TheHash Commandlets | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Antivirus Exploitation Framework Detection | elementary | <span style="color:#6a18a0">[1116](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| RDP Login From Localhost | elementary | [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) | Microsoft-Windows-Security-Auditing |
| Lazarus Loaders | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| SysKey Registry Keys Access | elementary | <span style="color:#B60016">[4656](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4656)</span>, <span style="color:#B60016">[4663](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4663)</span> | Microsoft-Windows-Security-Auditing |
| Copying Sensitive Files With Credential Data | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Update LolBins | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Signatures Removed With MpCmdRun | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Leviathan Registry Key Activity | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows ANONYMOUS LOGON Local Account Created | elementary | <span style="color:#D89462">[4720](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)</span> | Microsoft-Windows-Security-Auditing |
| Meterpreter or Cobalt Strike Getsystem Service Installation | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[17](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#B60016">[4697](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon, Service Control Manager |
| Dumpert LSASS Process Dumper | elementary | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Defender Exclusion Configuration | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#6a18a0">[5007](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Sysmon, Microsoft-Windows-Windows Defender |
| Mimikatz Basic Commands | elementary | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Cobalt Strike Default Beacons Names | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[15](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell Downgrade Attack | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Outlook Registry Access | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| AdFind Usage | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Domain Trust Discovery Through LDAP | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Empire Monkey Activity | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMI Persistence Command Line Event Consumer | elementary | <span style="color:#5865d3">[7](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Antivirus Web Shell Detection | elementary | <span style="color:#6a18a0">[1116](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Office Application Startup Office Test | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Msdt (Follina) File Browse Process Execution | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Phorpiex Process Masquerading | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| WMI Install Of Binary | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| ICacls Granting Access To All | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Credential Dumping By LaZagne | elementary | <span style="color:#5865d3">[10](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Comsvcs | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Suspicious HWP Child Process | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| IcedID Execution Using Excel | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Dllhost Wrong Parent | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Ryuk Ransomware Command Line | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Dropped File | elementary | <span style="color:#5865d3">[11](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Blue Mockingbird Malware | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Windows Credential Editor Registry Key | elementary | <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Raccine Uninstall | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| PowerShell AMSI Deactivation Bypass Using .NET Reflection | elementary | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Wdigest Enable UseLogonCredential | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#5865d3">[13](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span> | Microsoft-Windows-Sysmon |
| Antivirus Relevant File Paths Alerts | elementary | <span style="color:#6a18a0">[1116](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)</span> | Microsoft-Windows-Windows Defender |
| Suncrypt Parameters | elementary | <span style="color:#5865d3">[1](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#events)</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| AD Object WriteDAC Access | elementary | <span style="color:#B60016">[4662](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4662)</span> | Microsoft-Windows-Security-Auditing |

## EventIDs occurences in rules

| EventID | Number of rules concerned | Percentage of rules concerned (Total rules: 376) |
| ------- | ------------------------- | ------------------------------------------------------ |
| 1 | 185 | 49.2 % |
| 13 | 44 | 11.7 % |
| 4104 | 33 | 8.78 % |
| 11 | 17 | 4.52 % |
| 7 | 14 | 3.72 % |
| 5145 | 11 | 2.93 % |
| 7045 | 11 | 2.93 % |
| 4656 | 8 | 2.13 % |
| 4663 | 6 | 1.6 % |
| 4662 | 6 | 1.6 % |
| 4697 | 6 | 1.6 % |
| 17 | 6 | 1.6 % |
| 10 | 6 | 1.6 % |
| 98 | 6 | 1.6 % |
| 1116 | 5 | 1.33 % |
| 4624 | 5 | 1.33 % |
| 4688 | 5 | 1.33 % |
| 5136 | 4 | 1.06 % |
| 3 | 4 | 1.06 % |
| 5 | 3 | 0.8 % |
| 4625 | 3 | 0.8 % |
| 6 | 3 | 0.8 % |
| 12 | 3 | 0.8 % |
| 22 | 3 | 0.8 % |
| 4720 | 3 | 0.8 % |
| 4103 | 3 | 0.8 % |
| 20 | 2 | 0.53 % |
| 4729 | 2 | 0.53 % |
| 15 | 2 | 0.53 % |
| 5007 | 2 | 0.53 % |
| 1033 | 2 | 0.53 % |
| 4728 | 2 | 0.53 % |
| 25 | 2 | 0.53 % |
| 5156 | 1 | 0.27 % |
| 1013 | 1 | 0.27 % |
| 4611 | 1 | 0.27 % |
| 4649 | 1 | 0.27 % |
| 524 | 1 | 0.27 % |
| 4726 | 1 | 0.27 % |
| 4743 | 1 | 0.27 % |
| 4825 | 1 | 0.27 % |
| 30 | 1 | 0.27 % |
| 5154 | 1 | 0.27 % |
| 5140 | 1 | 0.27 % |
| 4742 | 1 | 0.27 % |
| 1032 | 1 | 0.27 % |
| 1034 | 1 | 0.27 % |
| 1031 | 1 | 0.27 % |
| 8 | 1 | 0.27 % |
| 4704 | 1 | 0.27 % |
| 4794 | 1 | 0.27 % |
| 770 | 1 | 0.27 % |
| 771 | 1 | 0.27 % |
| 150 | 1 | 0.27 % |
| 6416 | 1 | 0.27 % |
| 27 | 1 | 0.27 % |
| 19 | 1 | 0.27 % |
| 21 | 1 | 0.27 % |
| 16 | 1 | 0.27 % |
| 4706 | 1 | 0.27 % |
| 4707 | 1 | 0.27 % |
| 517 | 1 | 0.27 % |
| 1102 | 1 | 0.27 % |
| 8001 | 1 | 0.27 % |
| 4754 | 1 | 0.27 % |
| 4756 | 1 | 0.27 % |
| 4757 | 1 | 0.27 % |
| 4758 | 1 | 0.27 % |
| 4727 | 1 | 0.27 % |
| 4730 | 1 | 0.27 % |
| 4764 | 1 | 0.27 % |
| 47 | 1 | 0.27 % |
| 4673 | 1 | 0.27 % |
| 4738 | 1 | 0.27 % |
| 1000 | 1 | 0.27 % |
| 4658 | 1 | 0.27 % |
| 4776 | 1 | 0.27 % |
| 4674 | 1 | 0.27 % |
| 1127 | 1 | 0.27 % |
| 5001 | 1 | 0.27 % |
| 5101 | 1 | 0.27 % |
| 5010 | 1 | 0.27 % |
| 5012 | 1 | 0.27 % |
| 2013 | 1 | 0.27 % |
| 4732 | 1 | 0.27 % |
| 4661 | 1 | 0.27 % |
| 4657 | 1 | 0.27 % |
| 1006 | 1 | 0.27 % |
| 1007 | 1 | 0.27 % |
| 1008 | 1 | 0.27 % |
| 1015 | 1 | 0.27 % |
| 1117 | 1 | 0.27 % |
| 1118 | 1 | 0.27 % |
| 1119 | 1 | 0.27 % |

## EventProviders occurences in rules

| EventProvider | Number of rules concerned | Percentage of rules concerned (Total rules: 376) |
| ------- | ------------------------- | ------------------------------------------------------ |
| Microsoft-Windows-Sysmon | 262 | 69.68 % |
| Microsoft-Windows-Security-Auditing | 64 | 17.02 % |
| Microsoft-Windows-PowerShell | 36 | 9.57 % |
| Service Control Manager | 11 | 2.93 % |
| Microsoft-Windows-Windows Defender | 9 | 2.39 % |
| Microsoft-Windows-Backup | 1 | 0.27 % |
| Microsoft-Windows-Kernel-File | 1 | 0.27 % |
| Microsoft-Windows-DHCP-Server | 1 | 0.27 % |
| Microsoft-Windows-DNS-Server-Service | 1 | 0.27 % |
| Microsoft-Windows-Audit-CVE | 1 | 0.27 % |
| Microsoft-Windows-Kernel-General | 1 | 0.27 % |
| Microsoft-Windows-Eventlog | 1 | 0.27 % |
| Microsoft-Windows-NTLM | 1 | 0.27 % |
| Application Error | 1 | 0.27 % |

## EffortLevel x EventIDs

| Effort Level | EventIDs | Number of related rules | Percentage of related rules (Total rules: 376 |
| ------------ | -------- | ----------------------- | ------------------------------------------------------- |
| master | 1, 1013, 11, 12, 13, 150, 17, 25, 27, 3, 4104, 4611, 4624, 4625, 4656, 4661, 4662, 4663, 4673, 4674, 4720, 4726, 4728, 4729, 4743, 5007, 5140, 5145, 7, 770, 771, 8001, 98 | 66 | 17.55 % |
| advanced | 1, 10, 11, 13, 15, 17, 19, 20, 21, 22, 4104, 4625, 4656, 4662, 4688, 4706, 4707, 4727, 4728, 4729, 4730, 4754, 4756, 4757, 4758, 4764, 4776, 5, 5136, 5145, 5154, 5156, 6416, 7, 7045, 8 | 65 | 17.29 % |
| intermediate | 1, 10, 1000, 1006, 1007, 1008, 1015, 1031, 1032, 1033, 1034, 11, 1102, 1116, 1117, 1118, 1119, 1127, 12, 13, 16, 17, 20, 2013, 22, 3, 30, 4103, 4104, 4624, 4649, 4656, 4657, 4658, 4662, 4663, 4688, 4697, 47, 4720, 4732, 4738, 4742, 4794, 4825, 5, 5001, 5010, 5012, 5101, 5136, 5145, 517, 524, 6, 7, 7045 | 161 | 42.82 % |
| elementary | 1, 10, 11, 1116, 13, 15, 17, 4103, 4104, 4624, 4625, 4656, 4662, 4663, 4697, 4704, 4720, 5, 5007, 6, 7, 7045 | 84 | 22.34 % |


