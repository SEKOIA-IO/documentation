## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Microsoft Entra ID / Azure AD**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Microsoft Entra ID / Azure AD on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.json){ .md-button }
??? abstract "Microsoft Entra ID (Azure AD) Abnormal Token"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Microsoft Entra ID (Azure AD) Anonymous IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? abstract "Microsoft Entra ID (Azure AD) Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Domain Trust Modification"
    
    Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Confirm the added or modified target domain/URL is legitimate administrator behavior.
    
    - **Effort:** elementary

??? abstract "Microsoft Entra ID (Azure AD) Impossible Travel"
    
    Detects when Microsoft Entra ID (Azure AD) identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Leaked Credentials"
    
    Detects when Microsoft Entra ID (Azure AD) identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) MFA Method Change"
    
    This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Malicious IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Microsoft Entra ID (Azure AD) Password Spray"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure"
    
    Detects self-service password reset in failure for various reasons (except licence or policy ones)
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Sign-in From Unlikely Country"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Suspicious Browser"
    
    Detects when Microsoft Entra ID (Azure AD) identifies suspicious sign-in activity across multiple tenants from different countries in the same browser. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Suspicious IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies a suspicious IP address. An IP address is considered suspicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Microsoft Entra ID (Azure AD) Suspicious Inbox Forwarding"
    
    Detects when Microsoft Entra ID (Azure AD) identifies suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Microsoft Entra ID (Azure AD) Threat Intelligence"
    
    Detects when Microsoft Entra ID (Azure AD) identifies a sign-in activity that is unusual for the given user or is consistent with known attack patterns based on Microsoft's internal and external threat intelligence sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Microsoft Entra ID (Azure AD) Token Issuer Anomaly"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that The SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? abstract "Microsoft Entra ID (Azure AD) Unfamiliar Features"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins with characteristics that deviate from past sign-in properties. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
