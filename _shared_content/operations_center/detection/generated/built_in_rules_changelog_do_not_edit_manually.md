Changelog _last update on 2025-08-13_

## Changelog

### Correlation PowerShell Suspicious DLL Loading
  - 18/08/2025 - minor - Add filter to reduce false positives
    
### Potential Azure AD Phishing Page (Adversary-in-the-Middle)
  - 13/08/2025 - minor - Exclude additional legitimate domains and common benign positives.
    
### CrowdStrike Falcon Intrusion Detection Informational Severity EppDetection
  - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values
    
### CrowdStrike Falcon Intrusion Detection High Severity EppDetection
  - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values
    
### CrowdStrike Falcon Intrusion Detection Medium Severity EppDetection
  - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values
    
### CrowdStrike Falcon Intrusion Detection EppDetection
  - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values
    
### CrowdStrike Falcon Intrusion Detection Low Severity EppDetection
  - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values
    
### Download Files From Non-Legitimate TLDs
  - 05/08/2025 - minor - Improve filter to avoid false positives
    
### Download Files From Suspicious TLDs
  - 28/07/2025 - major - Improve filter and similarity strategy.
    
### Darktrace Threat Visualizer Model Breach Suspicious Activity
  - 02/07/2025 - minor - Update similarity
    
### Darktrace Threat Visualizer Model Breach Critical Activity
  - 02/07/2025 - minor - Update similarity
    
### Gatewatcher AionIQ V103 Retrohunt
  - 30/06/2025 - minor - Changing similarity on threat name.
    
### WMImplant Hack Tool
  - 26/06/2025 - major - Pattern updated to avoid false positives and effort level changed to be coherent.
    
### Powershell Web Request
  - 23/06/2025 - minor - improve filter
    
### Sekoia.io Endpoint Agent Stopped
  - 16/05/2025 - minor - Changing effort level.
    
### Varonis Data Security Network Low Severity Alert
  - 14/05/2025 - major - Fix pattern where severity level was missing
    
### Protected Storage Service Access
  - 09/05/2025 - minor - Adding similarity to regroup alerts.
    
### Microsoft Defender Antivirus Exclusion Configuration
  - 09/05/2025 - minor - Adding similarity to regroup alerts.
    
### Windows Suspicious Scheduled Task Creation
  - 24/04/2025 - minor - Adding similarity strategy.
    
### Capture a network trace with netsh.exe
  - 24/04/2025 - minor - Adding similarity strategy and filters to reduce false positives and changing effort level.
    
### Antivirus Relevant File Paths Alerts
  - 22/04/2025 - major - Change effort level and similarity strategy
    
### Usage Of Procdump With Common Arguments
  - 22/04/2025 - minor - Added filter to reduce false positives and change effort level.
    
### Commonly Used Commands To Stop Services And Remove Backups
  - 14/04/2025 - major - Reviewing pattern and condition to reduce false positives, adding similarity strategy and changing effort level.
    
### Suspicious DLL Loading By Ordinal
  - 14/04/2025 - minor - Adding similarity.
    
### Microsoft 365 Sign-in With No User Agent
  - 10/04/2025 - minor - Exclude more error codes to reduce false positives
    
### Entra ID Password Compromised By Known Credential Testing Tool
  - 09/04/2025 - minor - Add more correlation IDs, change similarity strategy to user.id to workaround email capitalisation inconsistencies.
    
### HTML Smuggling Suspicious Usage
  - 08/04/2025 - minor - Change effort level and add filter to reduce false positives.
    
### PowerView commandlets 1
  - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.
    
### PowerView commandlets 2
  - 07/04/2025 - minor - Changed similarity strategy and effort level.
    
### WithSecure Elements Warning Severity
  - 07/04/2025 - minor - Similarity strategy changed to avoid too much grouping
    
### Remote Enumeration Of Lateral Movement Groups
  - 02/04/2025 - minor - Use chained correlation to group alerts by source account.
    
### MMC Spawning Windows Shell
  - 26/03/2025 - minor - Adding similarity and changing effort level.
    
### Suspicious Windows Installer Execution
  - 25/03/2025 - major - Adding many filters and a similarity strategy. Effort was also updated to master.
    
### Successful Overpass The Hash Attempt
  - 25/03/2025 - minor - Changing pattern, adding similarity and changing effort level.
    
### Disable Windows Defender Credential Guard
  - 24/03/2025 - minor - Adding similarity and changing effort level.
    
### Write To File In Systemd
  - 24/03/2025 - major - Added filter to reduce false positives, change effort and add similarity strategy.
    
### Network Connection Via Certutil
  - 21/03/2025 - major - Review rule to reduce false positives and increases detection scope.
    
### Pandemic Windows Implant
  - 20/03/2025 - major - Rule's effort level has been changed to master, similarity and filter added.
    
### Powershell UploadString Function
  - 20/03/2025 - major - Change effort level and add filter to reduce false positives
    
### NetSh Used To Disable Windows Firewall
  - 20/03/2025 - minor - Adding similarity and change effort level.
    
### Microsoft Entra ID (Azure AD) Unfamiliar Features
  - 20/03/2025 - major - Change effort level
    
### Searchprotocolhost Child Found
  - 17/03/2025 - major - Rule changed to effort master, and filter added to reduce false positives.
    
### Microsoft Entra ID (Azure AD) Domain Trust Modification
  - 14/03/2025 - minor - Rule's pattern update following o365 parser change
    
### Address Space Layout Randomization (ASLR) Alteration
  - 14/03/2025 - minor - Excluded some commonly observed false positives.
    
### CMSTP UAC Bypass via COM Object Access
  - 13/03/2025 - minor - Adding filters to reduce false positives and adding similarity.
    
### TrustedInstaller Impersonation
  - 13/03/2025 - major - Adding filters to reduce false positives and adding similarity.
    
### Powershell Winlogon Helper DLL
  - 13/03/2025 - major - Adding new filter and similarity strategy to reduce false positives. Changing effort level.
    
### Suspicious PowerShell Invocations - Generic
  - 13/03/2025 - major - Change effort and excluded some commonly observed false positives.
    
### Palo Alto Cortex XDR (EDR) Alert Not Blocked (High Severity)
  - 10/03/2025 - minor - Update severity to match the severity level from the editor
    
### Palo Alto Cortex XDR (EDR) Alert Not Blocked (Medium Severity)
  - 10/03/2025 - minor - Update severity to match the severity level from the editor
    
### Palo Alto Cortex XDR (EDR) Alert Not Blocked (Low Severity)
  - 10/03/2025 - minor - Update severity to match the severity level from the editor
    
### Okta Suspicious Use of a Session Cookie
  - 03/03/2025 - minor - Improve detection pattern group-by, value field and timespan, update rule name
    
### Entra ID Sign-In Via Known AiTM Phishing Kit (Sneaky 2FA)
  - 25/02/2025 - major - Update the indicator.
    
### Taskhost or Taskhostw Suspicious Child Found
  - 13/02/2025 - minor - Adding new filters to reduce false positives.
    
### Authentication Impossible Travel
  - 04/02/2025 - major - Excluding Microsoft 365 format to avoid false positives
    
### Correlation Jumpcloud User Logged In From Multiple Countries
  - 03/02/2025 - minor - Update pattern to ECS field only
    
### Login Brute-Force Successful On Jumpcloud Portal
  - 03/02/2025 - minor - Update pattern to ECS field only
    
### Login Brute-Force Successful On Jumpcloud Workstation
  - 03/02/2025 - minor - Update pattern to ECS field only
    
### Login Brute-Force On Fortinet Firewall From Internet
  - 03/02/2025 - minor - Update pattern to ECS field only and intake format
    
### Login Brute-Force Successful Linux
  - 03/02/2025 - minor - Update pattern to ECS field only
    
### PowerShell Malicious Nishang PowerShell Commandlets
  - 31/01/2025 - major - update keywords to improve detection coverage and remove false positives
    
### SOCKS Tunneling Tool
  - 30/01/2025 - minor - Similarity strategy was modified to have more relevant alerts.
    
### Microsoft Windows Active Directory Module Commandlets
  - 30/01/2025 - minor - Adding filters to reduce false positives.
    
### Gatewatcher AionIQ V103 Malcore
  - 27/01/2025 - minor - Changing field and adding filter to reduce false positives.
    
### Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure
  - 20/01/2025 - minor - Update pattern to ECS field and specific intake field
    
### Tenable Identity Exposure / Alsid High Severity Alert
  - 20/01/2025 - minor - Removing event fields to use the smart description
    
### Tenable Identity Exposure / Alsid Critical Severity Alert
  - 20/01/2025 - minor - Removing event fields to use the smart description
    
### Correlation Potential DNS Tunnel
  - 20/01/2025 - major - Update regex pattern to improve detection, decrease count number, and add more filters to avoid false positives
    
### Fortigate Firewall Successful External Login
  - 20/01/2025 - minor - Update pattern to ECS field only
    
### Potential DNS Tunnel
  - 20/01/2025 - major - Update regex pattern to improve detection, and add more filters to avoid false positives
    
### Fortigate Firewall Login In Failure
  - 20/01/2025 - minor - Update pattern to ECS field only
    
### Brute-Force On Fortinet Firewall Login
  - 20/01/2025 - minor - Update pattern to ECS field and add intake field format
    
### File and Directory Permissions Modification
  - 20/01/2025 - minor - Update pattern to ECS field only
    
### Python Offensive Tools and Packages
  - 20/01/2025 - major - Rule's pattern changed to reduce false positives.
    
### Setuid Or Setgid Usage
  - 20/01/2025 - minor - Update pattern to ECS field only
    
### Write To File In Sudoers.d Folder
  - 20/01/2025 - minor - Update pattern to ECS field only
    
### Rare Logonui Child Found
  - 17/01/2025 - minor - Adding filter to reduce false positives.
    
### Socat Reverse Shell Detection
  - 17/01/2025 - major - Complete rewrite of the rule to reduce false positives.
    
### Socat Relaying Socket
  - 17/01/2025 - major - Significant rewrite of the rule to reduce false positives.
    
### Autorun Keys Modification
  - 16/01/2025 - minor - Added filters to reduce false positives.
    
### AWS CloudTrail KMS CMK Key Deleted
  - 16/01/2025 - minor - Similarity strategy was changed to have better alerts grouping.
    
### HarfangLab EDR Process Execution Blocked (HL-AI engine)
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Suspicious Process Behavior Has Been Detected
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Medium Threat
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Hlai Engine Detection
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Low Level Rule Detection
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR High Level Rule Detection
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Medium Level Rule Detection
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR High Threat
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Critical Threat
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Low Threat
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### HarfangLab EDR Critical Level Rule Detection
  - 16/01/2025 - minor - Adding format field to improve rules mapping
    
### Phishing Detected By Vade For M365 And Not Blocked
  - 16/01/2025 - minor - Adding filter to reduce false positives.
    
### SecurityScorecard Vulnerability Assessment Scanner New Issues
  - 15/01/2025 - minor - Adding format field to improve rules mapping
    
### Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)
  - 23/12/2024 - major - Update the indicators.
    
### Csrss Child Found
  - 16/12/2024 - minor - Improve pattern mandatory fields and add filter to reduce false positives
    
### Sign-In Via Known AiTM Phishing Kit
  - 12/12/2024 - minor - Update the selections to use a more appropriate ECS field. The rule now matches on more intakes. The name of the rule has been modified as well.
    
### HackTools Suspicious Names
  - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    
### Login Brute-Force Successful On AzureAD From Single IP Address
  - 28/11/2024 - minor - Adding error codes as filters to reduce false positives.
    
### Suspicious Cmd.exe Command Line
  - 27/11/2024 - minor - Adding new filters to reduce false positives.
    
### Alternate PowerShell Hosts Pipe
  - 25/11/2024 - minor - improve filter to avoid false positives.
    
### Suspicious Email Attachment Received
  - 14/11/2024 - major - Adding new file extension and new condition to make the rule broader as it can now match on more intakes.
    
### CVE-2019-0604 SharePoint
  - 04/11/2024 - minor - Added filter to reduce false positives
    
### Csrss Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
    
### Svchost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
    
### Suspicious Mshta Execution
  - 17/10/2024 - minor - Adding similarity_strategy
    
### Taskhost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
    
### Wininit Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.
    
### Searchindexer Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
    
### Spoolsv Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
    
### Winrshost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
    
### Logonui Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
    
### Mshta Suspicious Child Process
  - 17/10/2024 - minor - Adding similarity_strategy and enforce selection
    
### Dllhost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.
    
### Searchprotocolhost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
    
### Winlogon wrong parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
    
### Wsmprovhost Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
    
### Smss Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
    
### Lsass Wrong Parent
  - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.
    
### Taskhostw Wrong Parent
  - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
    
### Suspicious Download Links From Legitimate Services
  - 15/10/2024 - minor - Adding filter to reduce false positives.
    
### Microsoft IIS Module Installation
  - 10/10/2024 - major - Adding new commands with powershell and changing effort level.
    
### NlTest Usage
  - 10/10/2024 - minor - Adding new elements and filters to increase detection and reduce false positives.
    
### Web Application Launching Shell
  - 10/10/2024 - major - Adding new elements and filters to increase detection and reduce false positives.
    
### Interactive Terminal Spawned via Python
  - 02/10/2024 - major - Rule's pattern changed
    
### Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)
  - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
    
### Suspicious URL Requested By Curl Or Wget Commands
  - 23/09/2024 - major - Fixed an issue with the detection pattern.
    
### ZIP LNK Infection Chain
  - 19/09/2024 - minor - File paths added to filter some false positives.
    
### Microsoft Office Product Spawning Windows Shell
  - 13/09/2024 - major - Adding filters to reduce false positives and updated the effort level to master as it is a rule highly dependent on the environment.
    
### Microsoft Defender XDR Cloud App Security Alert
  - 13/09/2024 - major - Update service name value following Microsoft change
    
### Microsoft Defender XDR Alert
  - 13/09/2024 - major - Update service name value following Microsoft change
    
### DCSync Attack
  - 05/09/2024 - minor - Changing name of elements.
    
### Correlation Multi Service Disable
  - 21/08/2024 - minor - Adding a space to reduce false positives.
    
### Microsoft Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data
  - 13/08/2024 - minor - Added filter to reduce false positives
    
### Veeam Backup & Replication Malware Detection
  - 13/08/2024 - major - Restrict to only one type of event following customer feedback
    
### Wdigest Enable UseLogonCredential
  - 08/08/2024 - major - Rule's pattern field changed and pattern improved to cause less false positives.
    
### RSA SecurID Failed Authentification
  - 08/08/2024 - minor - Group-by values were changed to avoid having too much alerts.
    
### Credential Dump Tools Related Files
  - 07/08/2024 - major - Effort level was changed. Rule pattern initial field was changed to be ECS compliant and match on more intakes. A process was excluded and a filter was added, both to avoid generating too much false positives.
    
### Rclone Process
  - 05/08/2024 - major - Edited pattern of the rule to reduce false positives.
    
### Impacket Addcomputer
  - 05/08/2024 - major - improve selection to extend detection
    
### Suspicious Outbound Kerberos Connection
  - 05/08/2024 - major - Rule reworked to match more intakes and have less false positives (filters were added).
    
### TOR Usage Generic Rule
  - 02/08/2024 - minor - Small pattern to change to match only the real tags related to TOR.
    
### PowerShell Malicious PowerShell Commandlets
  - 26/07/2024 - minor - Removing tools relationships as it was inaccurate
    
### AWS CloudTrail EC2 Subnet Deleted
  - 22/07/2024 - minor - Update action field for ECS one
    
### Microsoft Entra ID (Azure AD) Malicious IP
  - 16/07/2024 - minor - Change similarity strategy.
    
### Audit CVE Event
  - 15/07/2024 - major - review filter and improve similarity
    
### Account Removed From A Security Enabled Group
  - 12/07/2024 - minor - Add similarity strategy
    
### Account Added To A Security Enabled Group
  - 12/07/2024 - minor - add similarity strategy
    
### User Account Created
  - 12/07/2024 - minor - Changing similarity strategy.
    
### Anomaly Bruteforce - User Enumeration
  - 12/07/2024 - major - improce coverage, enforce filter and change effort
    
### Shadow Copies
  - 11/07/2024 - minor - Adding new elements to detect and adding filter to reduce false positives.
    
### Dynamic Linker Hijacking From Environment Variable
  - 11/07/2024 - minor - Added filter to reduce false positvives
    
### Compress Data for Exfiltration via Archiver
  - 09/07/2024 - major - Reviewing detection to reduce false positives.
    
### Microsoft Defender Antivirus Disable Scheduled Tasks
  - 04/07/2024 - minor - Adding new commands to increase detection.
    
### Anomaly Internal Port Connection
  - 04/07/2024 - minor - Reviewing query.
    
### Suspicious Kerberos Ticket
  - 03/07/2024 - major - Add filter to cover a second case to improve rule coverage
    
### Disable Task Manager Through Registry Key
  - 25/06/2024 - major - Fix pattern selection
    
### Suspicious Driver Loaded
  - 25/06/2024 - minor - fix pattern following ECS parsing update
    
### Sticky Key Like Backdoor Usage
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Malware Persistence Registry Key
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs
    
### UAC Bypass Using Fodhelper
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### OceanLotus Registry Activity
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Security Support Provider (SSP) Added to LSA Configuration
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Disable Workstation Lock
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Leviathan Registry Key Activity
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Usage Of Sysinternals Tools
  - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    
### Google Workspace Password Change
  - 20/06/2024 - minor - Adding new element to increase detection.
    
### Google Workspace External Sharing
  - 20/06/2024 - minor - Adding new elements to increase detection.
    
### Scam Detected By Vade For M365 And Not Blocked
  - 18/06/2024 - minor - Adding filter when whitelisted.
    
### Anomaly Possible Sysvol Dump
  - 13/06/2024 - minor - Adding fields to be displayed in alerts.
    
### Process Memory Dump Using Comsvcs
  - 13/06/2024 - minor - Adding similarity strategy and changing effort level.
    
### PowerShell AMSI Deactivation Bypass Using .NET Reflection
  - 13/06/2024 - minor - Changing effort level and adding similarity strategy to regroup alerts.
    
### Anomaly Secret Store Access
  - 12/06/2024 - minor - Adding new fields to be displayed in alerts.
    
### Google Workspace Anomaly File Downloads
  - 12/06/2024 - minor - Changing effort level and adding field to alert.
    
### Anomaly New PowerShell Remote Session
  - 11/06/2024 - minor - Adding fields to be displayed in the alert.
    
### Anomaly Multiple Host Port Scan
  - 11/06/2024 - minor - Adding fields to be displayed in the alert and changing effort level.
    
### NjRat Registry Changes
  - 07/06/2024 - major - Update pattern to reduce false positives
    
### Outgoing Bytes Peak
  - 28/05/2024 - major - On Fortinet Fortigate intakes, events other than 0000000013 are now ignored.
    
### Suspicious PowerShell Keywords
  - 23/05/2024 - minor - Added filter to reduce false positives and new suspicious keywords.
    
### Login Brute-Force On Sekoia.io
  - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
    
### Google Workspace Admin Creation
  - 22/05/2024 - minor - Adding new element to increase detection.
    
### Password Reset Error Brute-Force On AzureAD
  - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
    
### Stop Backup Services
  - 16/05/2024 - minor - add pattern to extend and improve detection
    
### Suspicious desktop.ini Action
  - 30/04/2024 - major - Adding some filters
    
### Microsoft 365 Email Forwarding To Consumer Email Address
  - 22/04/2024 - minor - Add zohomail.com
    
### Discovery Commands Correlation
  - 16/04/2024 - minor - Adding new elements to increase detection.
    
### OneNote Suspicious Children Process
  - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.
    
### SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory
  - 04/04/2024 - major - Rule's pattern field changed
    
### Failed Logon Followed By A Success From Public IP Addresses
  - 04/04/2024 - major - Rule's pattern field changed
    
### DHCP Server Loaded the CallOut DLL
  - 04/04/2024 - major - Rule's pattern field changed
    
### Account Tampering - Suspicious Failed Logon Reasons
  - 04/04/2024 - major - Rule's pattern field changed
    
### User Couldn't Call A Privileged Service LsaRegisterLogonProcess
  - 04/04/2024 - major - Rule's pattern field changed
    
### CVE-2019-0708 Scan
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious Hostname
  - 04/04/2024 - major - Rule's pattern field changed
    
### User Account Deleted
  - 04/04/2024 - major - Rule's pattern field changed
    
### SAM Registry Hive Handle Request
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious PsExec Execution
  - 04/04/2024 - major - Rule's pattern field changed
    
### Credential Dumping By LaZagne
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious LDAP-Attributes Used
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious SAM Dump
  - 04/04/2024 - major - Rule's pattern field changed
    
### User Added to Local Administrators
  - 04/04/2024 - major - Rule's pattern field changed
    
### Successful Brute Force Login From Internet
  - 04/04/2024 - major - Rule's pattern field changed
    
### DNS Server Error Failed Loading The ServerLevelPluginDLL
  - 04/04/2024 - major - Rule's pattern field changed
    
### External Disk Drive Or USB Storage Device
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious Access To Sensitive File Extensions
  - 04/04/2024 - major - Rule's pattern field changed
    
### DPAPI Domain Backup Key Extraction
  - 04/04/2024 - major - Rule's pattern field changed
    
### Secure Deletion With SDelete
  - 04/04/2024 - major - Rule's pattern field changed
    
### Remote Registry Management Using Reg Utility
  - 04/04/2024 - major - Rule's pattern field changed
    
### WMI Event Subscription
  - 04/04/2024 - major - Rule's pattern field changed
    
### Webshell Creation
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspicious Windows ANONYMOUS LOGON Local Account Created
  - 04/04/2024 - major - Rule's pattern field changed
    
### Remote Service Activity Via SVCCTL Named Pipe
  - 04/04/2024 - major - Rule's pattern field changed
    
### Suspect Svchost Memory Access
  - 04/04/2024 - major - Rule's pattern field changed
    
### TUN/TAP Driver Installation
  - 04/04/2024 - major - Rule's pattern field changed
    
### Microsoft Malware Protection Engine Crash
  - 04/04/2024 - major - Rule's pattern field changed
    
### RDP Login From Localhost
  - 04/04/2024 - major - Rule's pattern field changed
    
### MSBuild Abuse
  - 04/04/2024 - major - Rule's pattern field changed
    
### Remote Privileged Group Enumeration
  - 04/04/2024 - major - Rule's pattern field changed
    
### SysKey Registry Keys Access
  - 04/04/2024 - major - Rule's pattern field changed
    
### SCM Database Handle Failure
  - 04/04/2024 - major - Rule's pattern field changed
    
### DHCP Server Error Failed Loading the CallOut DLL
  - 04/04/2024 - major - Rule's pattern field changed
    
### Cloudflare WAF Correlation Alerts
  - 28/03/2024 - minor - Rule effort was updated to master
    
### WAF Correlation Block Multiple Destinations
  - 28/03/2024 - minor - Rule effort was updated to master
    
### WAF Correlation Block actions
  - 28/03/2024 - minor - Rule effort was updated to master
    
### Netskope Admin Audit High Severity
  - 28/03/2024 - minor - Rule effort was updated to master
    
### Netskope DLP Alert
  - 28/03/2024 - minor - Rule effort was updated to master
    
### Netskope Alerts Compliance
  - 28/03/2024 - minor - Rule effort was updated to master
    
### Active Directory Replication User Backdoor
  - 26/03/2024 - major - Rule's pattern field changed
    
### Admin User RDP Remote Logon
  - 26/03/2024 - major - Rule's pattern field changed
    
### Python Opening Ports
  - 26/03/2024 - major - Rule's pattern field changed
    
### Password Dumper Activity On LSASS
  - 26/03/2024 - major - Rule's pattern field changed
    
### Microsoft Defender Antivirus Configuration Changed
  - 26/03/2024 - major - Rule's pattern field changed
    
### Computer Account Deleted
  - 26/03/2024 - major - Rule's pattern field changed
    
### Active Directory Database Dump Via Ntdsutil
  - 26/03/2024 - major - Rule's pattern field changed
    
### AD Privileged Users Or Groups Reconnaissance
  - 26/03/2024 - major - Rule's pattern field changed
    
### Possible RottenPotato Attack
  - 26/03/2024 - major - Rule's pattern field changed
    
### Impacket Secretsdump.py Tool
  - 26/03/2024 - major - Rule's pattern field changed
    
### LSASS Memory Dump
  - 26/03/2024 - major - Rule's pattern field changed
    
### Lateral Movement Remote Named Pipe
  - 26/03/2024 - minor - Filter was improved to reduce false positives
    
### Domain Trust Created Or Removed
  - 26/03/2024 - major - Rule's pattern field changed
    
### Creation or Modification of a GPO Scheduled Task
  - 26/03/2024 - major - Rule's pattern field changed
    
### Smbexec.py Service Installation
  - 26/03/2024 - major - Rule's pattern field changed
    
### Microsoft Defender Antivirus Threat Detected
  - 26/03/2024 - major - Rule's pattern field changed
    
### Malware Outbreak
  - 26/03/2024 - major - Rule's pattern field changed
    
### Detection of default Mimikatz banner
  - 26/03/2024 - major - Rule's pattern field changed
    
### NetNTLM Downgrade Attack
  - 26/03/2024 - major - Rule's pattern field changed
    
### Cobalt Strike Default Service Creation Usage
  - 26/03/2024 - major - Rule's pattern field changed
    
### Legitimate Process Execution From Unusual Folder
  - 26/03/2024 - major - Rule's pattern field changed
    
### Potential RDP Connection To Non-Domain Host
  - 26/03/2024 - major - Rule's pattern field changed
    
### Microsoft Defender Antivirus Tampering Detected
  - 26/03/2024 - major - Rule's pattern field changed
    
### Password Change On Directory Service Restore Mode (DSRM) Account
  - 26/03/2024 - major - Rule's pattern field changed
    
### Backup Catalog Deleted
  - 26/03/2024 - major - Rule's pattern field changed
    
### DC Shadow via Service Principal Name (SPN) creation
  - 26/03/2024 - major - Rule's pattern field changed
    
### CVE-2017-11882 Microsoft Office Equation Editor Vulnerability
  - 26/03/2024 - major - Rule's pattern field changed
    
### Process Herpaderping
  - 26/03/2024 - major - Rule's pattern field changed
    
### APT29 Fake Google Update Service Install
  - 26/03/2024 - major - Rule's pattern field changed
    
### Process Hollowing Detection
  - 26/03/2024 - major - Rule's pattern field changed
    
### Bloodhound and Sharphound Tools Usage
  - 26/03/2024 - minor - Adapted the rule to remove false positives.
    
### Active Directory Replication from Non Machine Account
  - 26/03/2024 - major - Rule's pattern field changed
    
### Admin Share Access
  - 26/03/2024 - major - Rule's pattern field changed
    
### Putty Sessions Listing
  - 26/03/2024 - major - Rule's pattern field changed
    
### Active Directory Delegate To KRBTGT Service
  - 26/03/2024 - major - Rule's pattern field changed
    
### Microsoft Defender Antivirus History Deleted
  - 26/03/2024 - major - Rule's pattern field changed
    
### PsExec Process
  - 26/03/2024 - major - Rule's pattern field changed
    
### Possible Replay Attack
  - 26/03/2024 - major - Rule's pattern field changed
    
### Eventlog Cleared
  - 26/03/2024 - major - Rule's pattern field changed
    
### Mimikatz LSASS Memory Access
  - 26/03/2024 - major - Rule's pattern field changed
    
### Privileged AD Builtin Group Modified
  - 26/03/2024 - major - Rule's pattern field changed
    
### Active Directory User Backdoors
  - 26/03/2024 - major - Rule's pattern field changed
    
### LSASS Access From Non System Account
  - 26/03/2024 - major - Rule's pattern field changed
    
### Dynwrapx Module Loading
  - 26/03/2024 - major - Rule's pattern field changed
    
### Malicious Service Installations
  - 26/03/2024 - major - Rule's pattern field changed
    
### AD User Enumeration
  - 26/03/2024 - major - Rule's pattern field changed
    
### Denied Access To Remote Desktop
  - 26/03/2024 - major - Rule's pattern field changed
    
### StoneDrill Service Install
  - 26/03/2024 - major - Rule's pattern field changed
    
### Chafer (APT 39) Activity
  - 26/03/2024 - major - Rule's pattern field changed
    
### Impacket Wmiexec Module
  - 22/03/2024 - minor - improve filter to extand detection
    
### Microsoft Entra ID (Azure AD) Successful Password Spraying From Single IP Address
  - 22/03/2024 - major - More precise list of error codes for success and failure to reduce false positives.
    
### Microsoft Entra ID (Azure AD) Login Failed Brute-Force From Single IP Address
  - 22/03/2024 - major - More precise list of error codes to reduce false positives.
    
### Remote Task Creation Via ATSVC Named Pipe
  - 21/03/2024 - minor - change filter to ACL hex value
    
### Gpscript Suspicious Parent
  - 19/03/2024 - major - Added filter to reduce false positives
    
### Microsoft 365 Suspicious Inbox Rule
  - 13/03/2024 - minor - Add another suspicious folder.
    
### Listing Systemd Environment
  - 06/03/2024 - minor - Effort level was adapted according to the observed hits for the rule
    
### Exfiltration Domain
  - 29/02/2024 - minor - enforce detection by adding tag
    
### WMIC Command To Determine The Antivirus
  - 28/02/2024 - minor - Adding a new usage of wmic.
    
### Outlook Registry Access
  - 19/02/2024 - minor - Effort level was adapted according to the observed hits for the rule
    
### Non-Legitimate Executable Using AcceptEula Parameter
  - 19/02/2024 - minor - Update filter and effort level according to the observed hits for the rule.
    
### MS Office Product Spawning Exe in User Dir
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Microsoft Defender Antivirus Disabled Base64 Encoded
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Netsh Port Forwarding
  - 15/02/2024 - minor - Added filter to reduce false positives
    
### AWS GuardDuty High Severity Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Sekoia.io EICAR Detection
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### AWS CloudTrail GuardDuty Detector Deleted
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Okta Phishing Detection with FastPass Origin Check
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Microsoft Defender for Office 365 High Severity AIR Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### AWS GuardDuty Medium Severity Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Microsoft Defender for Office 365 Low Severity AIR Alert Handled Automatically
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Microsoft Defender for Office 365 Low Severity AIR Alert Requires Action
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### AWS CloudTrail GuardDuty Detector Suspended
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Okta MFA Disabled
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Microsoft Defender for Office 365 Medium Severity AIR Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Mitigation Report Kill Success
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Custom Rule Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Login Failed Brute-Force On SentinelOne EDR Management Console
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Trend Micro Apex One Malware Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR SSO User Added
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection Medium Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Identity Protection Detection Low Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Detected (Suspicious)
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Mitigation Report Quarantine Failed
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection Informational Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Malicious Threat Not Mitigated
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection Critical Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Mitigation Report Remediate Success
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Identity Protection Detection Critical Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Identity Protection Detection Medium Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Trend Micro Apex One Data Loss Prevention Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Identity Protection Detection Informational Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### WithSecure Elements Critical Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Login Brute-Force Successful On SentinelOne EDR Management Console
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection Low Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Detected (Malicious)
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Trend Micro Apex One Intrusion Detection Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### SentinelOne EDR Threat Mitigation Report Quarantine Success
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Identity Protection Detection High Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CrowdStrike Falcon Intrusion Detection High Severity
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Cybereason EDR Malware Detection
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### Cybereason EDR Alert
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### CVE-2021-21985 VMware vCenter
  - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    
### WMIC Uninstall Product
  - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)
    
### High Privileges Network Share Removal
  - 02/02/2024 - major - changing current pattern and adding another one
    
### Inhibit System Recovery Deleting Backups
  - 31/01/2024 - minor - Improve selection filter
    
### Suspicious Process Requiring DLL Starts Without DLL
  - 22/01/2024 - minor - Added filter to reduce false positives
    
### Suspicious CodePage Switch with CHCP
  - 16/01/2024 - minor - Rename rule to fit with behavior
    
### Windows Registry Persistence COM Search Order Hijacking
  - 11/01/2024 - minor - Adding filtering for some FPs
    
### Grabbing Sensitive Hives Via Reg Utility
  - 02/01/2024 - minor - Rule was improved to have broader detection and filters were added.
    
### SolarWinds Wrong Child Process
  - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs
    
### Windows Registry Persistence COM Key Linking
  - 14/12/2023 - minor - Exclude common legitimate processes
    
### Linux Binary Masquerading
  - 12/12/2023 - minor - extend regex to macth more cases
    
### BITSAdmin Download
  - 06/12/2023 - minor - Adding key words to increase detection.
    
### HTA Infection Chains
  - 30/11/2023 - minor - Update pattern with new lolbin
    
### PowerShell Download From URL
  - 29/11/2023 - minor - Added a filter to the rule as some false positives were observed.
    
### Netsh Program Allowed With Suspicious Location
  - 29/11/2023 - minor - Update regex pattern to insensitive case
    
### Suspicious Regsvr32 Execution
  - 23/11/2023 - major - Extended detection and added filter
    
### Suspicious Double Extension
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    
### AD Object WriteDAC Access
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as legitimate administrator actions can trigger the rule.
    
### WiFi Credentials Harvesting Using Netsh
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.
    
### PowerShell Credential Prompt
  - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    
### AWS CloudTrail Remove Flow logs
  - 15/11/2023 - minor - Changing effort level.
    
### WAF Block Rule
  - 15/11/2023 - minor - Adding support for Ubika
    
### NTDS.dit File Interaction Through Command Line
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### Cobalt Strike Default Beacons Names
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### ETW Tampering
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### Suspicious Windows Script Execution
  - 19/10/2023 - major - Review of the rule to reduce false positives.
    
### CMSTP Execution
  - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.
    
### Domain Trust Discovery Through LDAP
  - 19/10/2023 - minor - improve filter to reduce false positives
    
### Transfering Files With Credential Data Via Network Shares
  - 17/10/2023 - minor - Improve selection to reduce false positives
    
### AdFind Usage
  - 12/10/2023 - minor - Slight change to a condition in order to reduce false positives.
    
### Microsoft 365 (Office 365) Mass Download By A Single User
  - 09/10/2023 - major - Fix field names to match the current parser.
    
### Microsoft 365 (Office 365) Potential Ransomware Activity Detected
  - 09/10/2023 - major - Fix field names to match the current parser.
    
### Microsoft 365 (Office 365) Unusual Volume Of File Deletion
  - 09/10/2023 - major - Fix field names to match the current parser.
    
### Suspicious Regasm Regsvcs Usage
  - 27/09/2023 - major - Rule creation
    
### UAC Bypass via Event Viewer
  - 21/09/2023 - minor - Improve filter to reduce false positives
    
### Suspicious Rundll32.exe Execution
  - 21/09/2023 - minor - Extend to some usage without dll filename
    
### Opening Of a Password File
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Suspicious Network Args In Command Line
  - 10/08/2023 - major - Added a list of suspicious processes to drastically reduce false positives.
    
### Okta User Logged In Multiple Applications
  - 07/08/2023 - major - Switching type from event_count to value_count | Adding Target in order to match only on different Apps
    
### Discord Suspicious Download
  - 05/08/2023 - minor - Added filters for commonly observed files extensions.
    
### Potential LokiBot User-Agent
  - 04/08/2023 - minor - Added a condition to only match on internal IP as source
    
### Suspicious Windows DNS Queries
  - 02/08/2023 - minor - Added a new field and filters to reduce false positives.
    
### Wmic Process Call Creation
  - 01/08/2023 - major - Rewritten as a regex to reduce false positives
    
### Msdt (Follina) File Browse Process Execution
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### HackTools Suspicious Process Names In Command Line
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL
  - 13/06/2023 - minor - Adding private IPs as sources
    
### Suspicious PowerShell Invocations - Specific
  - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.
    
### Internet Scanner Target
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Internet Scanner
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Audio Capture via PowerShell
  - 18/04/2023 - minor - Use more specific patterns to fix false positives.
    
### Mimikatz Basic Commands
  - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### Adexplorer Usage
  - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
    
### Windows Update LolBins
  - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.
    
### SentinelOne EDR User Logged In To The Management Console
  - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    
### ISO LNK Infection Chain
  - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
    
### Suspicious certutil command
  - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
    
### OneNote Embedded File
  - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
    