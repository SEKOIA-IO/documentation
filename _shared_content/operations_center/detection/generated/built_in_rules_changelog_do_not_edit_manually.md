Changelog _last update on 2024-01-15_

## Changelog

### Windows Registry Persistence COM Search Order Hijacking
  - 11/01/2024 - minor - Adding filtering for some FPs
    
### HarfangLab EDR Process Execution Blocked (HL-AI engine)
  - 10/01/2024 - major - Account for all blocks instead of only "Startup blocked". Rule name explicitly mentions HL-AI engine.
    
### Legitimate Process Execution From Unusual Folder
  - 04/01/2024 - major - Rework filter selection with contains instead of re modifier
    
### Grabbing Sensitive Hives Via Reg Utility
  - 02/01/2024 - minor - Rule was improved to have broader detection and filters were added.
    
### Suspicious Driver Loaded
  - 02/01/2024 - minor - improve selection to avoid FP
    
### SolarWinds Wrong Child Process
  - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs
    
### Windows Registry Persistence COM Key Linking
  - 14/12/2023 - minor - Exclude common legitimate processes
    
### Linux Binary Masquerading
  - 12/12/2023 - minor - extend regex to macth more cases
    
### BITSAdmin Download
  - 06/12/2023 - minor - Adding key words to increase detection.
    
### Microsoft 365 Sign-in With No User Agent
  - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
    
### HTA Infection Chains
  - 30/11/2023 - minor - Update pattern with new lolbin
    
### NjRat Registry Changes
  - 29/11/2023 - minor - Update regex pattern to insensitive case
    
### WMImplant Hack Tool
  - 29/11/2023 - minor - Added a selection to filter some false positives.
    
### PowerShell Download From URL
  - 29/11/2023 - minor - Added a filter to the rule as some false positives were observed.
    
### Netsh Program Allowed With Suspicious Location
  - 29/11/2023 - minor - Update regex pattern to insensitive case
    
### RDP Login From Localhost
  - 24/11/2023 - minor - Effort level changed to advanced.
    
### Suspicious Regsvr32 Execution
  - 23/11/2023 - major - Extended detection and added filter
    
### TOR Usage Generic Rule
  - 22/11/2023 - minor - Adding filter to improve rule.
    
### Suspicious Double Extension
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    
### WiFi Credentials Harvesting Using Netsh
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.
    
### AD Object WriteDAC Access
  - 21/11/2023 - minor - Rule's effort level has been changed to advanced as legitimate administrator actions can trigger the rule.
    
### PowerShell Credential Prompt
  - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    
### WAF Block Rule
  - 15/11/2023 - minor - Adding support for Ubika
    
### AWS CloudTrail Remove Flow logs
  - 15/11/2023 - minor - Changing effort level.
    
### AWS CloudTrail GuardDuty Detector Deleted
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### NTDS.dit File Interaction Through Command Line
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### ETW Tampering
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### Cobalt Strike Default Beacons Names
  - 08/11/2023 - minor - Added filter to reduce false positives
    
### Denied Access To Remote Desktop
  - 19/10/2023 - minor - Minor change in selection to reduce false positives.
    
### CMSTP Execution
  - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.
    
### Domain Trust Discovery Through LDAP
  - 19/10/2023 - minor - improve filter to reduce false positives
    
### Suspicious Windows Script Execution
  - 19/10/2023 - major - Review of the rule to reduce false positives.
    
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
    
### Login Brute-Force Successful
  - 06/10/2023 - minor - renaming and tunn filters to limit False Positive
    
### PowerView commandlets 2
  - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    
### Suspicious Regasm Regsvcs Usage
  - 27/09/2023 - major - Rule creation
    
### UAC Bypass via Event Viewer
  - 21/09/2023 - minor - Improve filter to reduce false positives
    
### Suspicious Rundll32.exe Execution
  - 21/09/2023 - minor - Extend to some usage without dll filename
    
### Svchost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Taskhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Spoolsv Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Taskhostw Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Gpscript Suspicious Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wmiprvse Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Logonui Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Smss Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Searchprotocolhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Lsass Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Explorer Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wininit Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winlogon wrong parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Userinit Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wsmprovhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Opening Of a Password File
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winword wrong parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Dllhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Csrss Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winrshost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Searchindexer Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Suspicious Network Args In Command Line
  - 10/08/2023 - major - Added a list of suspicious processes to drastically reduce false positives.
    
### MS Office Product Spawning Exe in User Dir
  - 10/08/2023 - minor - Rule modified and filter added to reduce false positives.
    
### Okta User Logged In Multiple Applications
  - 07/08/2023 - major - Switching type from event_count to value_count | Adding Target in order to match only on different Apps
    
### Microsoft Defender Antivirus Exclusion Configuration
  - 07/08/2023 - major - Considering the amount of false positives the rule effort has been changed to master. Furthermore a filter has been added.
    
### Microsoft Defender Antivirus Tampering Detected
  - 07/08/2023 - minor - Rule effort changed from intermediate to advanced considering the number of false positives observed.
    
### Potential LokiBot User-Agent
  - 04/08/2023 - minor - Added a condition to only match on internal IP as source
    
### Suspicious Windows DNS Queries
  - 02/08/2023 - minor - Added a new field and filters to reduce false positives.
    
### Account Tampering - Suspicious Failed Logon Reasons
  - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    
### Wmic Process Call Creation
  - 01/08/2023 - major - Rewritten as a regex to reduce false positives
    
### Correlation Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Privileged AD Builtin Group Modified
  - 10/07/2023 - minor - Added AD groups and change to effort master.
    
### Rclone Process
  - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Mimikatz LSASS Memory Access
  - 21/06/2023 - minor - Whitelisted lsm.exe that triggered too many false positives.
    
### Msdt (Follina) File Browse Process Execution
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### HackTools Suspicious Process Names In Command Line
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Socat Relaying Socket
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Socat Reverse Shell Detection
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL
  - 13/06/2023 - minor - Adding private IPs as sources
    
### Suspicious Cmd.exe Command Line
  - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
    
### Suspicious PowerShell Invocations - Specific
  - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.
    
### Internet Scanner Target
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Internet Scanner
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Audio Capture via PowerShell
  - 18/04/2023 - minor - Use more specific patterns to fix false positives.
    
### Remote Privileged Group Enumeration
  - 18/04/2023 - minor - Exclude events from the Local System session that cause false positives.
    
### Mimikatz Basic Commands
  - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### LSASS Memory Dump
  - 06/04/2023 - minor - Rule effort has been upgraded to master considering the number of different false positives the rule can trigger.
    
### Active Directory User Backdoors
  - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
    
### Suspicious PowerShell Invocations - Generic
  - 28/03/2023 - minor - Excluded some commonly observed false positives.
    
### Adexplorer Usage
  - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
    
### Windows Update LolBins
  - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.
    
### SentinelOne EDR User Logged In To The Management Console
  - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    
### Login Brute-Force Successful On AzureAD From Single IP Address
  - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    
### ISO LNK Infection Chain
  - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
    
### Suspicious certutil command
  - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
    
### OneNote Embedded File
  - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
    
### Write To File In Systemd
  - 04/01/2023 - minor - Added filter to reduce false positives.
    