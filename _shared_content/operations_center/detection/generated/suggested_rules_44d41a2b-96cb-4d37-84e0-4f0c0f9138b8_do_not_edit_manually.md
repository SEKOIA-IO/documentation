## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Tenable Identity Exposure / Alsid**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Tenable Identity Exposure / Alsid on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_44d41a2b-96cb-4d37-84e0-4f0c0f9138b8_do_not_edit_manually.json){ .md-button }
??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master

??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master

??? abstract "Computer Account Deleted"
    
    Detects computer account deletion.
    
    - **Effort:** master

??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced

??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate

??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate

??? abstract "Potential RDP Connection To Non-Domain Host"
    
    Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.
    
    - **Effort:** master

??? abstract "Tenable Identity Exposure / Alsid Critical Severity Alert"
    
    Tenable Identity Exposure / Alsid raised a critical severity alert.
    
    - **Effort:** master

??? abstract "Tenable Identity Exposure / Alsid High Severity Alert"
    
    Tenable Identity Exposure / Alsid raised an alert.
    
    - **Effort:** master

??? abstract "User Account Created"
    
    Detects user creation on windows servers, which shouldn't happen in an Active Directory environment. Apply this on your windows server logs and not on your DC logs. One default account `defaultuser0` is excluded as only used during Windows set-up. This detection use Security Event ID 4720. 
    
    - **Effort:** master

??? abstract "User Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master
