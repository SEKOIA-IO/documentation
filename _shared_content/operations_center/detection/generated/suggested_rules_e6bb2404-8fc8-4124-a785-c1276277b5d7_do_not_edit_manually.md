## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Okta System logs** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Okta System logs on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_e6bb2404-8fc8-4124-a785-c1276277b5d7_do_not_edit_manually.json){ .md-button }
??? abstract "Okta API Token created"
    
    A new API Token has been created on Okta SSO.
    
    - **Effort:** advanced

??? abstract "Okta API Token revoked"
    
    A new API Token has been deleted on Okta SSO.
    
    - **Effort:** advanced

??? abstract "Okta Admin Privilege Granted"
    
    Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.
    
    - **Effort:** advanced

??? abstract "Okta Application deleted"
    
    An application has been delete on Okta SSO.
    
    - **Effort:** advanced

??? abstract "Okta Application modified"
    
    An application has been updated on Okta SSO.
    
    - **Effort:** advanced

??? abstract "Okta Blacklist Manipulations"
    
    Detects when some manipulation are done in blacklist configurations.
    
    - **Effort:** intermediate

??? abstract "Okta MFA Disabled"
    
    A MFA has beed disabled in Okta SSO. This is a common behavior to gain permanent access over a system.
    
    - **Effort:** elementary

??? abstract "Okta Policy Modified or Deleted"
    
    Detects when an Okta policy is modified or deleted.
    
    - **Effort:** advanced

??? abstract "Okta Policy Rule Modified or Deleted"
    
    Detects when an Okta Policy Rule is Modified or Deleted.
    
    - **Effort:** advanced

??? abstract "Okta Security Threat Configuration Updated"
    
    Detects when the threat configuration has been updated in Okta.
    
    - **Effort:** intermediate

??? abstract "Okta Security Threat Detected"
    
    Detects when a security threat is detected in Okta.
    
    - **Effort:** intermediate

??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** intermediate

??? abstract "Okta User Account Locked"
    
    An user has been locked in Okta.
    
    - **Effort:** intermediate

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
