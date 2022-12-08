## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Azure Active Directory** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Azure Active Directory on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_19cd2ed6-f90c-47f7-a46b-974354a107bb_do_not_edit_manually.json){ .md-button }
??? abstract "Azure Active Directory Abnormal Token"
    
    Detects when Azure Active Directory indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Azure Active Directory Anonymous IP"
    
    Detects when Azure Active Directory identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? abstract "Azure Active Directory Impossible Travel"
    
    Detects when Azure Active Directory identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Azure Active Directory Leaked Credentials"
    
    Detects when Azure Active Directory identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Azure Active Directory Malicious IP"
    
    Detects when Azure Active Directory identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Azure Active Directory Password Spray"
    
    Detects when Azure Active Directory indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Azure Active Directory Self Service Password Reset In Failure"
    
    Detects self-service password reset in failure for various reasons (except licence or policy ones)
    
    - **Effort:** master

??? abstract "Azure Active Directory Sign-in From Unlikely Country"
    
    Detects when Azure Active Directory identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Azure Active Directory Suspicious Browser"
    
    Detects when Azure Active Directory identifies suspicious sign-in activity across multiple tenants from different countries in the same browser. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Azure Active Directory Suspicious IP"
    
    Detects when Azure Active Directory identifies a suspicious IP address. An IP address is considered suspicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Azure Active Directory Suspicious Inbox Forwarding"
    
    Detects when Azure Active Directory identifies suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? abstract "Azure Active Directory Threat Intelligence"
    
    Detects when Azure Active Directory identifies a sign-in activity that is unusual for the given user or is consistent with known attack patterns based on Microsoft's internal and external threat intelligence sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Azure Active Directory Token Issuer Anomaly"
    
    Detects when Azure Active Directory indicates that The SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? abstract "Azure Active Directory Unfamiliar Features"
    
    Detects when Azure Active Directory identifies sign-ins with characteristics that deviate from past sign-in properties. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? abstract "Covenant Default HTTP Beaconing"
    
    Detects potential Covenant communications through the user-agent and specific urls
    
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

??? abstract "TrevorC2 HTTP Communication"
    
    Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 
    
    - **Effort:** elementary
