### Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Cisco Secure Access - File Events**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Cisco Secure Access - File Events on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_52093a43-6b0d-44d1-83b8-5d1a4f34265f_do_not_edit_manually.json){ .md-button }
??? abstract "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master

??? abstract "Certify Or Certipy"
    
    Detects the use of certify and certipy which are two different tools used to enumerate and abuse Active Directory Certificate Services.
    
    - **Effort:** advanced

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** intermediate

??? abstract "Credential Dump Tools Related Files"
    
    Detects processes or file names related to credential dumping tools and the dropped files they generate by default.
    
    - **Effort:** advanced

??? abstract "HackTools Suspicious Names"
    
    Quick-win rule to detect the default process names or file names of several HackTools.
    
    - **Effort:** advanced

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "Sekoia.io Activity Logs Rule Deactivation Bulk"
    
    Detects a massive rule deactivation observed threw Sekoia.io activity logs.
    
    - **Effort:** master

??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
