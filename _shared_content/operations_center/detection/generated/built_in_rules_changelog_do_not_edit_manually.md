Changelog _last update on 2023-08-01_

## Changelog

### Account Tampering - Suspicious Failed Logon Reasons
  - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    
### Correlation Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Potential DNS Tunnel
  - 19/07/2023 - major - New regex pattern and new filters.
    
### Privileged AD Builtin Group Modified
  - 10/07/2023 - minor - Added AD groups and change to effort master.
    
### Userinit Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Csrss Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Dllhost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Wsmprovhost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Taskhost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Searchprotocolhost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Wininit Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Svchost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Explorer Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Lsass Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Smss Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Searchindexer Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Taskhostw Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Spoolsv Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Wmiprvse Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Logonui Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Winword wrong parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Winrshost Wrong Parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Winlogon wrong parent
  - 04/07/2023 - major - Added filter to reduce false positives
    
### Opening Of a Password File
  - 03/07/2023 - minor - Added french words for the command lines.
    
### Rclone Process
  - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Mimikatz LSASS Memory Access
  - 21/06/2023 - minor - Whitelisted lsm.exe that triggered too many false positives.
    
### HackTools Suspicious Process Names In Command Line
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Msdt (Follina) File Browse Process Execution
  - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### SolarWinds Wrong Child Process
  - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
    
### Socat Relaying Socket
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Socat Reverse Shell Detection
  - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    
### Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL
  - 13/06/2023 - minor - Adding private IPs as sources
    
### Suspicious Cmd.exe Command Line
  - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
    
### Suspicious PowerShell Invocations - Specific
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### WMImplant Hack Tool
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### PowerShell Download From URL
  - 26/05/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### Internet Scanner Target
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Internet Scanner
  - 28/04/2023 - minor - Support for standard ECS FW fields
    
### Audio Capture via PowerShell
  - 18/04/2023 - minor - Use more specific patterns to fix false positives.
    
### Remote Privileged Group Enumeration
  - 18/04/2023 - minor - Exclude events from the Local System session that cause false positives.
    
### LSASS Memory Dump
  - 06/04/2023 - minor - Rule effort has been upgraded to master considering the number of different false positives the rule can trigger.
    
### Active Directory User Backdoors
  - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
    
### Mimikatz Basic Commands
  - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
    
### Suspicious PowerShell Invocations - Generic
  - 28/03/2023 - minor - Excluded some commonly observed false positives.
    
### Adexplorer Usage
  - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
    
### Windows Update LolBins
  - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.
    
### SentinelOne User Logged In To The Management Console
  - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    
### Login Brute-Force Successful On AzureAD From Single IP Address
  - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    
### LNK Malware Chain
  - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
    
### Suspicious certutil command
  - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
    
### OneNote Embedded File
  - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
    