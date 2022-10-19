# Built-in detection rules, EventIDs and EventProviders relations

SEKOIA.IO provides built-in detection rules to illuminate intrusions, adversarial behaviours and suspicious activity escalation chains so you can immediately take steps to remediate. Built-in rules can be customized to your context and according to your security posture.

This page aims at helping partners & customers in having their detection coverage by knowing which Event IDs and Event Providers are used by rule. **Please note this was retrieved automatically from our tests samples when generating attacks that triggered the rules. It might not be exhaustive and concerns mostly Windows-related rules**


The colors in this page should be interpreted as follow:

  - Effort Levels colors correspond to the one in the Operations Center.
  - For the EventIDs:
      * <span style='color:#B60016'>Red</span>: This EventID is not logged by default on a Windows 10+ or Windows Server 2016+ machine.
      * <span style='color:#D89462'>Orange</span>: This EventID is logged by default on a Windows 10+ or Windows Server 2016+ machine but upgrading its configuration would greatly help detection. For instance, the EventID 4688 is logged by default, but logging the command line is incredibly helpful for the rules since almost 50% of our rules use command line for detection (usually showed as EventID 1 in this page).
      * <span style='color:#6a18a0'>Purple</span>: This EventID is logged by default if you have Windows Defender activated.
      * <span style='color:#1cb238'>Green</span>: This EventID is only logged if you have Sysmon. **Our rules will have a master Effort Level if the recommended Sysmon Configuration is not enough and needs to be modified. Please be aware that a modification of Sysmon Configuration can greatly increase events logging in your network, which SEKOIA.IO can't know about and therefore is not responsible for that.**

## Rules x Effort Level x EventIDs x Event Providers
| Rule Name | Effort Level | EventIDs | Event Providers |
| --------- | ------------ | -------- | --------------- |
| PowerShell Malicious PowerShell Commandlets | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Putty Sessions Listing | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#B60016">4656</span>, <span style="color:#B60016">4663</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon |
| FoggyWeb Backdoor DLL Loading | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Windows Defender History Deleted | <span style='color:#B60016'>master</span> | <span style="color:#6a18a0">1013</span> | Microsoft-Windows-Windows Defender |
| Svchost DLL Search Order Hijack | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Rubeus Register New Logon Process | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4611</span> | Microsoft-Windows-Security-Auditing |
| Suspicious DLL Loaded Via Office Applications | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Suspicious PsExec Execution | <span style='color:#B60016'>master</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Account Removed From A Security Enabled Group | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4729</span> | Microsoft-Windows-Security-Auditing |
| Netsh Port Opening | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| In-memory PowerShell | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Failed Logon Source From Public IP Addresses | <span style='color:#B60016'>master</span> | 4625 | Microsoft-Windows-Security-Auditing |
| TOR Usage Generic Rule | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">3</span> | Microsoft-Windows-Sysmon |
| Windows Defender Configuration Changed | <span style='color:#B60016'>master</span> | <span style="color:#6a18a0">5007</span> | Microsoft-Windows-Windows Defender |
| Office 365 MCAS New Country | <span style='color:#B60016'>master</span> | 98 |  |
| Registry Checked For Lanmanserver DisableCompression Parameter | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4663</span> | Microsoft-Windows-Security-Auditing |
| DNS ServerLevelPluginDll Installation | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Advanced IP Scanner | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Network Share Discovery | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Usage Of Sysinternals Tools | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| LSASS Access From Non System Account | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4656</span>, <span style="color:#B60016">4663</span> | Microsoft-Windows-Security-Auditing |
| Local Account Deleted | <span style='color:#B60016'>master</span> | 4726, <span style="color:#B60016">4743</span> | Microsoft-Windows-Security-Auditing |
| Protected Storage Service Access | <span style='color:#B60016'>master</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Admin Share Access | <span style='color:#B60016'>master</span> | <span style="color:#B60016">5140</span>, <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Inbox Hiding | <span style='color:#B60016'>master</span> | 98 |  |
| Office 365 MCAS Repeated Failed Login | <span style='color:#B60016'>master</span> | 98 |  |
| WMIC Loading Scripting Libraries | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Autorun Keys Modification | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">12</span> | Microsoft-Windows-Sysmon |
| DNS Server Error Failed Loading The ServerLevelPluginDLL | <span style='color:#B60016'>master</span> | 150, 770, 771 | Microsoft-Windows-DNS-Server-Service |
| Disable Security Events Logging Adding Reg Key MiniNt | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Windows Firewall Changes | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Webshell Creation | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">11</span>, <span style="color:#B60016">4656</span>, <span style="color:#B60016">4663</span> | Microsoft-Windows-Sysmon |
| List Shadow Copies | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Sysmon Windows File Block Executable | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">27</span> | Microsoft-Windows-Sysmon |
| AD User Enumeration | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4662</span> | Microsoft-Windows-Security-Auditing |
| WMI DLL Loaded Via Office | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Credential Dumping-Tools Common Named Pipes | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">17</span> | Microsoft-Windows-Sysmon |
| Account Added To A Security Enabled Group | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4728</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Detection Velocity | <span style='color:#B60016'>master</span> | 98 |  |
| Office 365 MCAS Repeated Delete | <span style='color:#B60016'>master</span> | 98 |  |
| Local Account Created | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4720</span> | Microsoft-Windows-Security-Auditing |
| Potential RDP Connection To Non-Domain Host | <span style='color:#B60016'>master</span> | <span style="color:#B60016">8001</span> | Microsoft-Windows-NTLM |
| Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Suspicious Access To Sensitive File Extensions | <span style='color:#B60016'>master</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Cobalt Strike Named Pipes | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">17</span> | Microsoft-Windows-Sysmon |
| User Couldn't Call A Privileged Service LsaRegisterLogonProcess | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4673</span> | Microsoft-Windows-Security-Auditing |
| Office 365 MCAS Risky IP | <span style='color:#B60016'>master</span> | 98 |  |
| CVE-2017-11882 Microsoft Office Equation Editor Vulnerability | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">3</span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Key Linking | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| SCM Database Handle Failure | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4656</span> | Microsoft-Windows-Security-Auditing |
| Abusing Azure Browser SSO | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Admin User RDP Remote Logon | <span style='color:#B60016'>master</span> | 4624 | Microsoft-Windows-Security-Auditing |
| Suspicious New Printer Ports In Registry | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Remote Registry Management Using Reg Utility | <span style='color:#B60016'>master</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| SCM Database Privileged Operation | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4674</span> | Microsoft-Windows-Security-Auditing |
| Net.exe User Account Creation | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Narrator Feedback-Hub Persistence | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| CVE-2021-34527 - PrintNightmare - Suspicious Actions From Spoolsv | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">7</span>, <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| File Or Folder Permissions Modifications | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Stop Backup Services | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Windows Defender Deactivation Using PowerShell Script | <span style='color:#B60016'>master</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Process Herpaderping | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">25</span> | Microsoft-Windows-Sysmon |
| Malware Persistence Registry Key | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| AD Privileged Users Or Groups Reconnaissance | <span style='color:#B60016'>master</span> | <span style="color:#B60016">4661</span> | Microsoft-Windows-Security-Auditing |
| FromBase64String Command Line | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Process Hollowing Detection | <span style='color:#B60016'>master</span> | <span style="color:#1cb238">25</span> | Microsoft-Windows-Sysmon |
| Suspicious Outbound Kerberos Connection | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">5156</span> | Microsoft-Windows-Security-Auditing |
| PowerShell Invoke-Obfuscation Obfuscated IEX Invocation | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Remote Service Activity Via SVCCTL Named Pipe | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Exfiltration And Tunneling Tools Execution | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Alternate PowerShell Hosts Pipe | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">17</span> | Microsoft-Windows-Sysmon |
| Powershell Web Request | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Active Directory Replication from Non Machine Account | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">4662</span> | Microsoft-Windows-Security-Auditing |
| Rare Logonui Child Found | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Logon Scripts (UserInitMprLogonScript) | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Suspicious desktop.ini Action | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">15</span> | Microsoft-Windows-Sysmon |
| Winlogon wrong parent | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious XOR Encoded PowerShell Command Line | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Control Panel Items | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Taskhost or Taskhostw Suspicious Child Found | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Netsh Allow Command | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Metasploit PSExec Service Creation | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">7045</span> | Service Control Manager |
| Default Encoding To UTF-8 PowerShell | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Rubeus Tool Command-line | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Domain Group And Permission Enumeration | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Active Directory Replication User Backdoor | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">5136</span> | Microsoft-Windows-Security-Auditing |
| Csrss Wrong Parent | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious PrinterPorts Creation (CVE-2020-1048) | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| XCopy Suspicious Usage | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Python Opening Ports | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">5154</span> | Microsoft-Windows-Security-Auditing |
| Telegram Bot API Request | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">22</span> | Microsoft-Windows-Sysmon |
| Suspicious PROCEXP152.sys File Created In Tmp | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Legitimate Process Execution From Unusual Folder | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">5</span>, <span style="color:#D89462">4688</span> | Microsoft-Windows-Sysmon |
| CreateRemoteThread Common Process Injection | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">8</span> | Microsoft-Windows-Sysmon |
| PowerShell Data Compressed | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Dynwrapx Module Loading | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows DNS Queries | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">22</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Product Spawning Windows Shell | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Control Process | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious Nishang PowerShell Commandlets | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| External Disk Drive Or USB Storage Device | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">6416</span> | Microsoft-Windows-Security-Auditing |
| Load Of dbghelp/dbgcore DLL From Suspicious Process | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| PowerView commandlets 2 | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| PowerView commandlets 1 | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| WMI Event Subscription | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">19</span>, <span style="color:#1cb238">20</span>, <span style="color:#1cb238">21</span> | Microsoft-Windows-Sysmon |
| NTDS.dit File In Suspicious Directory | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Lateral Movement - Remote Named Pipe | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Domain Trust Created Or Removed | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4706</span>, <span style="color:#D89462">4707</span> | Microsoft-Windows-Security-Auditing |
| Winword wrong parent | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4688</span> | Microsoft-Windows-Security-Auditing |
| Unsigned Image Loaded Into LSASS Process | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Windows Registry Persistence COM Search Order Hijacking | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| WMI Persistence Script Event Consumer File Write | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Privileged AD Builtin Group Modified | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4727</span>, <span style="color:#D89462">4728</span>, <span style="color:#D89462">4729</span>, <span style="color:#D89462">4730</span>, <span style="color:#D89462">4754</span>, <span style="color:#D89462">4756</span>, <span style="color:#D89462">4757</span>, <span style="color:#D89462">4758</span>, <span style="color:#D89462">4764</span> | Microsoft-Windows-Security-Auditing |
| PsExec Process | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">13</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Sysmon, Service Control Manager |
| Disabled IE Security Features | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Change Default File Association | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Rclone Process | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| RDP Sensitive Settings Changed | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Adexplorer Usage | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| New Service Creation | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Account Tampering - Suspicious Failed Logon Reasons | <span style='color:#D89462'>advanced</span> | 4625, <span style="color:#B60016">4776</span> | Microsoft-Windows-Security-Auditing |
| Suspicious PowerShell Keywords | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SAM Registry Hive Handle Request | <span style='color:#D89462'>advanced</span> | <span style="color:#B60016">4656</span> | Microsoft-Windows-Security-Auditing |
| Suspicious ADSI-Cache Usage By Unknown Tool | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Cmd.exe Used To Run Reconnaissance Commands | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Cmd.exe Command Line | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Hiding Files With Attrib.exe | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| RDP Session Discovery | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2017-0261 Or CVE-2017-0262 | <span style='color:#D89462'>advanced</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PowerShell - NTFS Alternate Data Stream | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Svchost Wrong Parent | <span style='color:#D89462'>advanced</span> | <span style="color:#D89462">4688</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Finger Usage | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious DLL Loading By Ordinal | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Clear EventLogs Through CommandLine | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Taskhostw Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Scripting In A WMI Consumer | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">20</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows Installer Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Wmic Process Call Creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Active Directory User Backdoors | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4662</span>, <span style="color:#B60016">5136</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Windows Script Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| ETW Tampering | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Password Dumper Activity On LSASS | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4656</span> | Microsoft-Windows-Security-Auditing |
| Transfering Files With Credential Data Via Network Shares | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| MS Office Product Spawning Exe in User Dir | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Powershell Winlogon Helper DLL | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| SquirrelWaffle Malspam Execution Loading DLL | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Office 365 Malware Uploaded On SharePoint | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">6</span> |  |
| NTDS.dit File Interaction Through Command Line | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Grabbing Sensitive Hives Via Reg Utility | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| LSASS Memory Dump | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| Credential Dumping Tools Service Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">7045</span> | Service Control Manager |
| NjRat Registry Changes | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">12</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Koadic Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Mshta Execution From Wmi | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Hostname | <span style='color:#60BBD8'>intermediate</span> | 4624 | Microsoft-Windows-Security-Auditing |
| StoneDrill Service Install | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">7045</span> | Service Control Manager |
| MMC20 Lateral Movement | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Possible Replay Attack | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4649</span> | Microsoft-Windows-Security-Auditing |
| Hijack Legit RDP Session To Move Laterally | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Audio Capture via PowerShell | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious LDAP-Attributes Used | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">5136</span> | Microsoft-Windows-Security-Auditing |
| DPAPI Domain Backup Key Extraction | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4662</span> | Microsoft-Windows-Security-Auditing |
| Backup Catalog Deleted | <span style='color:#60BBD8'>intermediate</span> | 524 | Microsoft-Windows-Backup |
| Exchange Server Spawning Suspicious Processes | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Disable Windows Defender Credential Guard | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| MSBuild Abuse | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">3</span> | Microsoft-Windows-Sysmon |
| Office 365 Malware Uploaded On OneDrive | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">6</span> |  |
| Suspicious PowerShell Invocations - Generic | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Exchange Mailbox Export | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| MMC Spawning Windows Shell | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Denied Access To Remote Desktop | <span style='color:#60BBD8'>intermediate</span> | 4825 | Microsoft-Windows-Security-Auditing |
| QakBot Process Creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Ngrok Process Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| WCE wceaux.dll Creation | <span style='color:#60BBD8'>intermediate</span> | 30 | Microsoft-Windows-Kernel-File |
| Qakbot Persistence Using Schtasks | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Impacket Secretsdump.py Tool | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Suspect Svchost Memory Access | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| Explorer Process Executing HTA File | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious PowerShell Invocations - Specific | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| DC Shadow via Service Principal Name (SPN) creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4742</span>, <span style="color:#B60016">5136</span> | Microsoft-Windows-Security-Auditing |
| DHCP Server Error Failed Loading the CallOut DLL | <span style='color:#60BBD8'>intermediate</span> | 1031, 1032, 1033, 1034 | Microsoft-Windows-DHCP-Server |
| Data Compressed With Rar With Password | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Lsass Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| NetSh Used To Disable Windows Firewall | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Wmiprvse Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Exploiting SetupComplete.cmd CVE-2019-1378 | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Formbook Hijacked Process Command | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Creation or Modification of a GPO Scheduled Task | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| LSASS Memory Dump File Creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| New Or Renamed User Account With '$' In Attribute 'SamAccountName' | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4720</span> | Microsoft-Windows-Security-Auditing |
| Userinit Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Outlook Child Process | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4688</span> | Microsoft-Windows-Security-Auditing |
| Netsh RDP Port Opening | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Network Connection Via Certutil | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">3</span> | Microsoft-Windows-Sysmon |
| Password Change On Directory Service Restore Mode (DSRM) Account | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4794</span> | Microsoft-Windows-Security-Auditing |
| Successful Overpass The Hash Attempt | <span style='color:#60BBD8'>intermediate</span> | 4624 | Microsoft-Windows-Security-Auditing |
| Suspicious Taskkill Command | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| OceanLotus Registry Activity | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Remote Task Creation Via ATSVC Named Pipe | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">5145</span> | Microsoft-Windows-Security-Auditing |
| Capture a network trace with netsh.exe | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Rundll32.exe Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Logonui Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Wininit Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Netsh Allowed Python Program | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Network Args In Command Line | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Cred Dump Tools Dropped Files | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| RDP Port Change Using Powershell | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| BazarLoader Persistence Using Schtasks | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| WMIC Command To Determine The Antivirus | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Ryuk Ransomware Persistence Registry Key | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Mimikatz LSASS Memory Access | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| Spoolsv Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Formbook File Creation DB1 | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Lsass Access Through WinRM | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| Registry Key Used By Some Old Agent Tesla Samples | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| NlTest Usage | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Detection of default Mimikatz banner | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Taskhost Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| TUN/TAP Driver Installation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Suspicious Regsvr32 Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PowerShell Malicious PowerShell Keywords | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Possible RottenPotato Attack | <span style='color:#60BBD8'>intermediate</span> | 4624 | Microsoft-Windows-Security-Auditing |
| Sysprep On AppData Folder | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Netsh Program Allowed With Suspicious Location | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| MalwareBytes Uninstallation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| STRRAT Scheduled Task | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious SAM Dump | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">16</span> | Microsoft-Windows-Kernel-General |
| Exchange Server Creating Unusual Files | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Csrss Child Found | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Pandemic Windows Implant | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| PowerCat Function Loading | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| COM Hijack Via Sdclt | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| DCSync Attack | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4662</span> | Microsoft-Windows-Security-Auditing |
| Cmdkey Cached Credentials Recon | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Spawning Script | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Eventlog Cleared | <span style='color:#60BBD8'>intermediate</span> | 517, 1102 | Microsoft-Windows-Eventlog |
| Suspicious Driver Loaded | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Commonly Used Commands To Stop Services And Remove Backups | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| DLL Load via LSASS Registry Key | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">12</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Sliver DNS Beaconing | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">22</span> | Microsoft-Windows-Sysmon |
| CMSTP Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Child Found | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| SolarWinds Suspicious File Creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Wsmprovhost Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Python HTTP Server | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Inhibit System Recovery Deleting Backups | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Suspicious Scheduled Task Creation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4688</span> | Microsoft-Windows-Security-Auditing |
| Office 365 AtpDetection | <span style='color:#60BBD8'>intermediate</span> | 47 |  |
| PowerShell Execution Via Rundll32 | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Creating Suspicious File | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| MavInject Process Injection | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| CMSTP UAC Bypass via COM Object Access | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Desktopimgdownldr Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious certutil command | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Process Requiring DLL Starts Without DLL | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Active Directory Delegate To KRBTGT Service | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4738</span> | Microsoft-Windows-Security-Auditing |
| DNS Exfiltration and Tunneling Tools Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Chafer (APT 39) Activity | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Microsoft Malware Protection Engine Crash | <span style='color:#60BBD8'>intermediate</span> | 1000 | Application Error |
| Rare Lsass Child Found | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Trickbot Malware Activity | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Network Sniffing Windows | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">5</span> | Microsoft-Windows-Sysmon |
| New DLL Added To AppCertDlls Registry Key | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Suspicious DLL side loading from ProgramData | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Secure Deletion With SDelete | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#B60016">4656</span>, <span style="color:#B60016">4658</span>, <span style="color:#B60016">4663</span> | Microsoft-Windows-Security-Auditing |
| Searchindexer Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| XSL Script Processing And SquiblyTwo Attack | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Bloodhound and Sharphound Tools Usage | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| MOFComp Execution | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Schtasks Suspicious Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Disable .NET ETW Through COMPlus_ETWEnabled | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Windows Defender Tampering Detected | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#6a18a0">1127</span>, <span style="color:#6a18a0">2013</span>, <span style="color:#6a18a0">5001</span>, <span style="color:#6a18a0">5010</span>, <span style="color:#6a18a0">5012</span>, <span style="color:#6a18a0">5101</span> | Microsoft-Windows-Windows Defender |
| Suspicious DNS Child Process | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Malicious Named Pipe | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">17</span> | Microsoft-Windows-Sysmon |
| PowerShell Download From URL | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| UAC Bypass Using Fodhelper | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Winrshost Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Searchprotocolhost Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Smss Wrong Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| User Added to Local Administrators | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4732</span> | Microsoft-Windows-Security-Auditing |
| NetNTLM Downgrade Attack | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span>, <span style="color:#B60016">4657</span> | Microsoft-Windows-Sysmon |
| Gpscript Suspicious Parent | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Commands From MS SQL Server Shell | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| WMImplant Hack Tool | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| SolarWinds Wrong Child Process | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| KeePass Config XML In Command-Line | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| DHCP Callout DLL Installation | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| WMIC Uninstall Product | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Windows Defender Threat Detected | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#6a18a0">1006</span>, <span style="color:#6a18a0">1007</span>, <span style="color:#6a18a0">1008</span>, <span style="color:#6a18a0">1015</span>, <span style="color:#6a18a0">1116</span>, <span style="color:#6a18a0">1117</span>, <span style="color:#6a18a0">1118</span>, <span style="color:#6a18a0">1119</span> | Microsoft-Windows-Windows Defender |
| Spyware Persistence Using Schtasks | <span style='color:#60BBD8'>intermediate</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| DHCP Server Loaded the CallOut DLL | <span style='color:#60BBD8'>intermediate</span> | 1033 |  |
| Antivirus Password Dumper Detection | <span style='color:#5373E6'>elementary</span> | <span style="color:#6a18a0">1116</span> | Microsoft-Windows-Windows Defender |
| Mustang Panda Dropper | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Malicious Service Installations | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Cobalt Strike Default Service Creation Usage | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Service Control Manager |
| Winword Document Droppers | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Malspam Execution Registering Malicious DLL | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Windows Defender History Directory Deleted | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious Double Extension | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">5</span> | Microsoft-Windows-Sysmon |
| Equation Group DLL_U Load | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PasswordDump SecurityXploded Tool | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Windows Defender Disabled Base64 Encoded | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Netsh RDP Port Forwarding | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Turla Named Pipes | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">17</span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Registry Manipulation | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| DNS Tunnel Technique From MuddyWater | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| APT29 Fake Google Update Service Install | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">7045</span> | Service Control Manager |
| Explorer Wrong Parent | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Disable Task Manager Through Registry Key | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| UAC Bypass Via Sdclt | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Microsoft Office Startup Add-In | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Exploited CVE-2020-10189 Zoho ManageEngine | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Ursnif Registry Key | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4704</span> | Microsoft-Windows-Security-Auditing |
| Suspicious Netsh DLL Persistence | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| CVE-2019-0708 Scan | <span style='color:#5373E6'>elementary</span> | 4625 | Microsoft-Windows-Security-Auditing |
| WiFi Credentials Harvesting Using Netsh | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Exploit For CVE-2015-1641 | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Smbexec.py Service Installation | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">6</span>, <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Service Control Manager |
| Disable Workstation Lock | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Debugging Software Deactivation | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PowerShell Credential Prompt | <span style='color:#5373E6'>elementary</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Mshta JavaScript Execution | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Elise Backdoor | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious VBS Execution Parameter | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| FlowCloud Malware | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Schtasks Persistence With High Privileges | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| UAC Bypass via Event Viewer | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Sticky Key Like Backdoor Usage | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| RYUK Ransomeware - martinstevens Username | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Security Support Provider (SSP) Added to LSA Configuration | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Phorpiex DriveMgr Command | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Audit CVE Event | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Audit-CVE |
| Invoke-TheHash Commandlets | <span style='color:#5373E6'>elementary</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Antivirus Exploitation Framework Detection | <span style='color:#5373E6'>elementary</span> | <span style="color:#6a18a0">1116</span> | Microsoft-Windows-Windows Defender |
| RDP Login From Localhost | <span style='color:#5373E6'>elementary</span> | 4624 | Microsoft-Windows-Security-Auditing |
| Lazarus Loaders | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| SysKey Registry Keys Access | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4656</span>, <span style="color:#B60016">4663</span> | Microsoft-Windows-Security-Auditing |
| Copying Sensitive Files With Credential Data | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Windows Update LolBins | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Windows Defender Signatures Removed With MpCmdRun | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Leviathan Registry Key Activity | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Suspicious Windows ANONYMOUS LOGON Local Account Created | <span style='color:#5373E6'>elementary</span> | <span style="color:#D89462">4720</span> | Microsoft-Windows-Security-Auditing |
| Meterpreter or Cobalt Strike Getsystem Service Installation | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span>, <span style="color:#1cb238">17</span>, <span style="color:#B60016">4697</span>, <span style="color:#B60016">7045</span> | Microsoft-Windows-Security-Auditing, Microsoft-Windows-Sysmon, Service Control Manager |
| Dumpert LSASS Process Dumper | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">7</span>, <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Windows Defender Exclusion Configuration | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span>, <span style="color:#6a18a0">5007</span> | Microsoft-Windows-Sysmon, Microsoft-Windows-Windows Defender |
| Mimikatz Basic Commands | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4103</span> | Microsoft-Windows-PowerShell |
| Cobalt Strike Default Beacons Names | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">15</span> | Microsoft-Windows-Sysmon |
| PowerShell Downgrade Attack | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Outlook Registry Access | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| AdFind Usage | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Domain Trust Discovery Through LDAP | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Empire Monkey Activity | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| WMI Persistence Command Line Event Consumer | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">7</span> | Microsoft-Windows-Sysmon |
| Antivirus Web Shell Detection | <span style='color:#5373E6'>elementary</span> | <span style="color:#6a18a0">1116</span> | Microsoft-Windows-Windows Defender |
| Office Application Startup Office Test | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Msdt (Follina) File Browse Process Execution | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| Phorpiex Process Masquerading | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| WMI Install Of Binary | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| ICacls Granting Access To All | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Credential Dumping By LaZagne | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">10</span> | Microsoft-Windows-Sysmon |
| Process Memory Dump Using Comsvcs | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Suspicious HWP Child Process | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| IcedID Execution Using Excel | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Dllhost Wrong Parent | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Ryuk Ransomware Command Line | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| RedMimicry Winnti Playbook Dropped File | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">11</span> | Microsoft-Windows-Sysmon |
| Blue Mockingbird Malware | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| Windows Credential Editor Registry Key | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Raccine Uninstall | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span> | Microsoft-Windows-Sysmon |
| PowerShell AMSI Deactivation Bypass Using .NET Reflection | <span style='color:#5373E6'>elementary</span> | <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell |
| Wdigest Enable UseLogonCredential | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#1cb238">13</span> | Microsoft-Windows-Sysmon |
| Antivirus Relevant File Paths Alerts | <span style='color:#5373E6'>elementary</span> | <span style="color:#6a18a0">1116</span> | Microsoft-Windows-Windows Defender |
| Suncrypt Parameters | <span style='color:#5373E6'>elementary</span> | <span style="color:#1cb238">1</span>, <span style="color:#D89462">4104</span> | Microsoft-Windows-PowerShell, Microsoft-Windows-Sysmon |
| AD Object WriteDAC Access | <span style='color:#5373E6'>elementary</span> | <span style="color:#B60016">4662</span> | Microsoft-Windows-Security-Auditing |
**Total rules in the statistics below: 376**

## EventIDs occurence in rules:

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
**Total rules in the statistics below: 376**

## EventProviders occurence in rules:

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

## EffortLevel x EventIDs needed

| Effort Level | EventIDs | Number of related rules | Percentage of related rules (Total rules: 376 |
| ------------ | -------- | ----------------------- | ------------------------------------------------------- |
| master | 1, 1013, 11, 12, 13, 150, 17, 25, 27, 3, 4104, 4611, 4624, 4625, 4656, 4661, 4662, 4663, 4673, 4674, 4720, 4726, 4728, 4729, 4743, 5007, 5140, 5145, 7, 770, 771, 8001, 98 | 66 | 17.55 % |
| advanced | 1, 10, 11, 13, 15, 17, 19, 20, 21, 22, 4104, 4625, 4656, 4662, 4688, 4706, 4707, 4727, 4728, 4729, 4730, 4754, 4756, 4757, 4758, 4764, 4776, 5, 5136, 5145, 5154, 5156, 6416, 7, 7045, 8 | 65 | 17.29 % |
| intermediate | 1, 10, 1000, 1006, 1007, 1008, 1015, 1031, 1032, 1033, 1034, 11, 1102, 1116, 1117, 1118, 1119, 1127, 12, 13, 16, 17, 20, 2013, 22, 3, 30, 4103, 4104, 4624, 4649, 4656, 4657, 4658, 4662, 4663, 4688, 4697, 47, 4720, 4732, 4738, 4742, 4794, 4825, 5, 5001, 5010, 5012, 5101, 5136, 5145, 517, 524, 6, 7, 7045 | 161 | 42.82 % |
| elementary | 1, 10, 11, 1116, 13, 15, 17, 4103, 4104, 4624, 4625, 4656, 4662, 4663, 4697, 4704, 4720, 5, 5007, 6, 7, 7045 | 84 | 22.34 % |


