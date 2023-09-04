Changelog _last update on 2023-09-04_

## Changelog

### Searchindexer Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Taskhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Opening Of a Password File
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Csrss Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Smss Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winword wrong parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Spoolsv Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Explorer Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Userinit Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Lsass Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wmiprvse Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wininit Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Dllhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Logonui Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winrshost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Wsmprovhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Gpscript Suspicious Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Winlogon wrong parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Taskhostw Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Searchprotocolhost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Svchost Wrong Parent
  - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    
### Windows Registry Persistence COM Search Order Hijacking
  - 16/08/2023 - minor - Adding filtering for some FPs
    
### MS Office Product Spawning Exe in User Dir
  - 10/08/2023 - minor - Rule modified and filter added to reduce false positives.
    
### Suspicious Network Args In Command Line
  - 10/08/2023 - major - Added a list of suspicious processes to drastically reduce false positives.
    
### Okta User Logged In Multiple Applications
  - 07/08/2023 - major - Switching type from event_count to value_count | Adding Target in order to match only on different Apps
    
### Microsoft Defender Antivirus Tampering Detected
  - 07/08/2023 - minor - Rule effort changed from intermediate to advanced considering the number of false positives observed.
    
### Microsoft Defender Antivirus Exclusion Configuration
  - 07/08/2023 - major - Considering the amount of false positives the rule effort has been changed to master. Furthermore a filter has been added.
    
### Potential LokiBot User-Agent
  - 04/08/2023 - minor - Added a condition to only match on internal IP as source
    
### Suspicious Windows DNS Queries
  - 02/08/2023 - minor - Added a new field and filters to reduce false positives.
    
### Wmic Process Call Creation
  - 01/08/2023 - major - Rewritten as a regex to reduce false positives
    
### Account Tampering - Suspicious Failed Logon Reasons
  - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    
### Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Correlation Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Privileged AD Builtin Group Modified
  - 10/07/2023 - minor - Added AD groups and change to effort master.
    
### Rclone Process
  - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Mimikatz LSASS Memory Access
  - 21/06/2023 - minor - Whitelisted lsm.exe that triggered too many false positives.
    
### HackTools Suspicious Process Names In Command Line
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Msdt (Follina) File Browse Process Execution
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Socat Relaying Socket
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Socat Reverse Shell Detection
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### SolarWinds Wrong Child Process
  - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
    
### Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL
  - 13/06/2023 - minor - Adding private IPs as sources
    
### Suspicious Cmd.exe Command Line
  - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
    
### PowerShell Download From URL
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### WMImplant Hack Tool
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### Suspicious PowerShell Invocations - Specific
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### Internet Scanner Target
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Internet Scanner
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Audio Capture via PowerShell
  - 18/04/2023 - minor - Use more specific patterns to fix false positives.
    
### Remote Privileged Group Enumeration
  - 18/04/2023 - minor - Exclude events from the Local System session that cause false positives.
    
### Active Directory User Backdoors
  - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
    
### Mimikatz Basic Commands
  - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### LSASS Memory Dump
  - 06/04/2023 - minor - Rule effort has been upgraded to master considering the number of different false positives the rule can trigger.
    
### Suspicious PowerShell Invocations - Generic
  - 28/03/2023 - minor - Excluded some commonly observed false positives.
    
### Adexplorer Usage
  - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
    
### SentinelOne EDR User Logged In To The Management Console
  - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    
### Windows Update LolBins
  - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.
    
### Login Brute-Force Successful On AzureAD From Single IP Address
  - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    
### LNK Malware Chain
  - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
    
### Suspicious certutil command
  - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
    
### OneNote Embedded File
  - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
    