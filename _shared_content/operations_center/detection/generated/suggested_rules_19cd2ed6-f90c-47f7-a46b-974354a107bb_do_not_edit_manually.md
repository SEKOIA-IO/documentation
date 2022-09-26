## Suggested Built-in Rules

This integration enables the following built-in detection rules. Use the Rules Catalog to customize and adapt these to your security posture.


??? tip "Azure Active Directory Abnormal Token"
    
    Detects when Azure Active Directory indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? tip "Azure Active Directory Anonymous IP"
    
    Detects when Azure Active Directory identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? warning "Azure Active Directory Impossible Travel"
    
    Detects when Azure Active Directory identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? warning "Azure Active Directory Leaked Credentials"
    
    Detects when Azure Active Directory identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? tip "Azure Active Directory Malicious IP"
    
    Detects when Azure Active Directory identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? tip "Azure Active Directory Password Spray"
    
    Detects when Azure Active Directory indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? warning "Azure Active Directory Self Service Password Reset In Failure"
    
    Detects self-service password reset in failure for various reasons (except licence or policy ones)
    
    - **Effort:** master

??? warning "Azure Active Directory Sign-in From Unlikely Country"
    
    Detects when Azure Active Directory identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? warning "Azure Active Directory Suspicious Browser"
    
    Detects when Azure Active Directory identifies suspicious sign-in activity across multiple tenants from different countries in the same browser. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? tip "Azure Active Directory Suspicious IP"
    
    Detects when Azure Active Directory identifies a suspicious IP address. An IP address is considered suspicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? warning "Azure Active Directory Suspicious Inbox Forwarding"
    
    Detects when Azure Active Directory identifies suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master

??? tip "Azure Active Directory Threat Intelligence"
    
    Detects when Azure Active Directory identifies a sign-in activity that is unusual for the given user or is consistent with known attack patterns based on Microsoft's internal and external threat intelligence sources. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? tip "Azure Active Directory Token Issuer Anomaly"
    
    Detects when Azure Active Directory indicates that The SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced

??? tip "Azure Active Directory Unfamiliar Features"
    
    Detects when Azure Active Directory identifies sign-ins with characteristics that deviate from past sign-in properties. To use this feature, you must have an Azure Active Directory Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate

??? tip "Covenant Default HTTP Beaconing"
    
    Detects potential Covenant communications through the user-agent and specific urls
    
    - **Effort:** intermediate

??? warning "Fortinet Firewall Login In Failure"
    
    Detects failed login attemps on firewall administration rule. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master

??? warning "Fortinet Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master

??? tip "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? tip "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? tip "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? tip "TrevorC2 HTTP Communication"
    
    Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 
    
    - **Effort:** elementary
