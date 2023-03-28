Changelog _last update on 2023-03-28_

## Changelog

### Suspicious PowerShell Invocations - Generic
  - 28/03/2023 - minor - Excluded some commonly observed false positives.
    
### Adexplorer Usage
  - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
    
### SentinelOne User Logged In To The Management Console
  - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    
### Login Brute-Force Successful On AzureAD From Single IP Address
  - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    
### LNK Malware Chain
  - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
    
### OneNote Embedded File
  - 20/02/2023 - minor - Adding the .chm and .wsf file extensions for a file opened from a OneNote.
    
### Suspicious certutil command
  - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
    
### OneNote Embedded File
  - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
    