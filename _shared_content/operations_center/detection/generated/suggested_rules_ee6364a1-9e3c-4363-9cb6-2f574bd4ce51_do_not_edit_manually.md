## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Panda Security Aether** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Panda Security Aether on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_ee6364a1-9e3c-4363-9cb6-2f574bd4ce51_do_not_edit_manually.json){ .md-button }
??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced

??? abstract "Failed Logon Source From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The sekoia.tags are used to filter internal Ipv4 addresses (10.0.0.0/8 172.16.0.0/12 127.0.0.0/8 169.254.0.0/16 192.168.0.0/16).
    
    - **Effort:** master

??? abstract "Local Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "Smbexec.py Service Installation"
    
    Detects the use of smbexec.py tool by detecting a specific service installation
    
    - **Effort:** elementary
