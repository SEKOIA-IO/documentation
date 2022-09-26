## Suggested Built-in Rules

This integration enables the following built-in detection rules. Use the Rules Catalog to customize and adapt these to your security posture.


??? tip "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? tip "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate

??? tip "Interactive Terminal Spawned via Python"
    
    Identifies when a terminal (tty) is spawned via Python. Attackers may upgrade a simple reverse shell to a fully interactive tty after obtaining initial access to a host.
    
    - **Effort:** advanced

??? tip "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? tip "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? tip "Phorpiex Process Masquerading"
    
    Detects specific process executable path used by the Phorpiex botnet to masquerade its system process network activity. It looks for a pattern of a system process executable name that is not legitimate and running from a folder that is created via a random algorithm 13-15 numbers long.
    
    - **Effort:** elementary

??? tip "Python Exfiltration Tools"
    
    Python has some built-in modules or library that could be installed and later be used as exflitration tool by an attacker
    
    - **Effort:** advanced

??? tip "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? tip "SELinux Disabling"
    
    An attacker can disable SELinux to make workstation or server compromise easier as it disables several protections.
    
    - **Effort:** intermediate

??? tip "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** elementary

??? tip "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced

??? warning "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host
    
    - **Effort:** master

??? tip "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced
