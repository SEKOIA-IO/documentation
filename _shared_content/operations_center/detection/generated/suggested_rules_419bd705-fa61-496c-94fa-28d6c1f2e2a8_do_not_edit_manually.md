## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Broadcom/Symantec Endpoint Security** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Broadcom/Symantec Endpoint Security on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_419bd705-fa61-496c-94fa-28d6c1f2e2a8_do_not_edit_manually.json){ .md-button }
??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate

??? abstract "Interactive Terminal Spawned via Python"
    
    Identifies when a terminal (tty) is spawned via Python. Attackers may upgrade a simple reverse shell to a fully interactive tty after obtaining initial access to a host.
    
    - **Effort:** advanced

??? abstract "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? abstract "Phorpiex Process Masquerading"
    
    Detects specific process executable path used by the Phorpiex botnet to masquerade its system process network activity. It looks for a pattern of a system process executable name that is not legitimate and running from a folder that is created via a random algorithm 13-15 numbers long.
    
    - **Effort:** elementary

??? abstract "Python Exfiltration Tools"
    
    Python has some built-in modules or library that could be installed and later be used as exflitration tool by an attacker
    
    - **Effort:** advanced

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "SELinux Disabling"
    
    An attacker can disable SELinux to make workstation or server compromise easier as it disables several protections.
    
    - **Effort:** intermediate

??? abstract "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** elementary

??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? abstract "Symantec EPP Event Blocked"
    
    Symantec EPP blocked an action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master

??? abstract "Symantec EPP Event Cleaned"
    
    Symantec EPP had cleaned action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master

??? abstract "Symantec EPP Event Quarantined"
    
    Symantec EPP had a quarantined action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master

??? abstract "Symantec EPP Event Terminate"
    
    Symantec EPP had a process terminate action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master

??? abstract "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host
    
    - **Effort:** master

??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced
