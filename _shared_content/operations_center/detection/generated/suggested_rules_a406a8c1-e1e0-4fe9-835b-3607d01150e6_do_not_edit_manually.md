## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Netwrix Auditor** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Netwrix Auditor on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_a406a8c1-e1e0-4fe9-835b-3607d01150e6_do_not_edit_manually.json){ .md-button }
??? abstract "NTDS.dit File In Suspicious Directory"
    
    The file NTDS.dit is supposed to be located mainly in C:\Windows\NTDS. The rule checks whether the file is in a legitimate directory or not (through file creation events). This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** advanced

??? abstract "OneNote Embedded File"
    
    Detects creation or uses of OneNote embedded files with unusual extensions.  
    
    - **Effort:** intermediate

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate

??? abstract "Webshell Creation"
    
    Detects possible webshell file creation. It requires File Creation monitoring, which can be done using Sysmon's Event ID 11. However the recommended SwiftOnSecurity configuration does not fully cover the needs for this rule, it needs to be updated with the proper file names extensions.
    
    - **Effort:** master
