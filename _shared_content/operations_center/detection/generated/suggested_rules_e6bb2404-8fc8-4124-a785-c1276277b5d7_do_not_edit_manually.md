## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Okta**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Okta on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_e6bb2404-8fc8-4124-a785-c1276277b5d7_do_not_edit_manually.json){ .md-button }
??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

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

??? abstract "Okta MFA Bypass Attempt"
    
    A bypass of MFA may have been attempted.
    
    - **Effort:** intermediate

??? abstract "Okta MFA Disabled"
    
    A MFA has beed disabled in Okta SSO. This is a common behavior to gain permanent access over a system.
    
    - **Effort:** intermediate

??? abstract "Okta Network Zone Deactivated"
    
    Detects attempts to deactivate an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** advanced

??? abstract "Okta Network Zone Deleted"
    
    Detects attempts to delete an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** advanced

??? abstract "Okta Network Zone Modified"
    
    Detects attempts to modify an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** intermediate

??? abstract "Okta Phishing Detection with FastPass Origin Check"
    
    Okta's FastPass prevents known phishing sites.
    
    - **Effort:** intermediate

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

??? abstract "Okta Suspicious Activity Reported"
    
    Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.
    
    - **Effort:** advanced

??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** master

??? abstract "Okta User Account Created"
    
    An user account has been created in Okta.
    
    - **Effort:** master

??? abstract "Okta User Account Deactivated"
    
    An user account has been deactivated in Okta.
    
    - **Effort:** master

??? abstract "Okta User Account Locked"
    
    An user has been locked in Okta.
    
    - **Effort:** intermediate

??? abstract "Okta User Impersonation Access"
    
    A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.
    
    - **Effort:** advanced

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
