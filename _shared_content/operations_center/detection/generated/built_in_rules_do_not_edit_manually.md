Rules catalog includes **977 built-in detection rules** ([_last update on 2024-11-29_](rules_changelog.md)).
## Reconnaissance
**Gather Victim Identity Information**

??? abstract "Anomaly Possible Sysvol Dump"
    
    The rule detects abnormally high access to sysvol files.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 08/04/2024 - minor - change field name on query
        - 13/06/2024 - minor - Adding fields to be displayed in alerts.
            
**Gather Victim Network Information**

??? abstract "ACLight Discovering Privileged Accounts"
    
    Detects use of ACLight tool. This tool aims to discover privileged accounts by scanning the network.
    
    - **Effort:** advanced
    
??? abstract "Adidnsdump Enumeration"
    
    Detects use of the tool adidnsdump for enumeration and discovering DNS records.
    
    - **Effort:** advanced
    
??? abstract "Gatewatcher AionIQ V103 Network Behavior Analytics"
    
    Detects when network behavior analytics were requested.
    
    - **Effort:** master
    
??? abstract "Internet Scanner"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/04/2023 - minor - Support for standard ECS FW fields
            
??? abstract "Internet Scanner Target"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/04/2023 - minor - Support for standard ECS FW fields
            
??? abstract "Microsoft Windows Active Directory Module Commandlets"
    
    Detects use of commandlets linked to the AD Module.
    
    - **Effort:** advanced
    
??? abstract "Remote System Discovery Via Telnet"
    
    Detects use of the protocol telnet to access information.
    
    - **Effort:** advanced
    
??? abstract "System Network Connections Discovery"
    
    Detects system network connections discovery via powershell and cmd.
    
    - **Effort:** advanced
    
**Gather Victim Host Information**

??? abstract "DNS Query For Iplookup"
    
    Detects dns query of observables tagged as iplookup.
    
    - **Effort:** master
    
??? abstract "Wmic Suspicious Commands"
    
    Detects suspicious commands used by the process wmic to get informations on the system.
    
    - **Effort:** advanced
    
**Active Scanning**

??? abstract "Anomaly Fortigate IPS Alert Peak"
    
    The rule detects abnormally high number of Fortigate IPS alert
    
    - **Effort:** master
    
??? abstract "Bitsight SPM Material Vulnerability"
    
    Bitsight SPM has raised a material vulnerability finding
    
    - **Effort:** master
    
??? abstract "Bitsight SPM Minor Vulnerability"
    
    Bitsight SPM has raised a minor vulnerability finding
    
    - **Effort:** master
    
??? abstract "Bitsight SPM Moderate Vulnerability"
    
    Bitsight SPM has raised a moderate vulnerability finding
    
    - **Effort:** master
    
??? abstract "Bitsight SPM Severe Vulnerability"
    
    Bitsight SPM has raised a severe vulnerability finding
    
    - **Effort:** master
    
??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).
    
    - **Effort:** intermediate
    
??? abstract "Cloudflare HTTP Requests Rule Block Or Drop"
    
    Detects when one of Cloudflare Web Application Firewall (WAF) Managed rule blocked or dropped an HTTP request. It requires only Cloudflare HTTP requests logs.
    
    - **Effort:** master
    
??? abstract "Cloudflare WAF Correlation Alerts"
    
    Detection of multiple alerts (more than 5) triggered by the same source by Cloudflare detection rules
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "ExtraHop Reveal(x) 360 Intrusion Detection Critical Severity"
    
    ExtraHop Reveal(x) 360 raised an intrusion detection alert with critical severity.
    
    - **Effort:** master
    
??? abstract "ExtraHop Reveal(x) 360 Intrusion Detection High Severity"
    
    ExtraHop Reveal(x) 360 raised an intrusion detection alert with high severity.
    
    - **Effort:** master
    
??? abstract "Fastly Next-Gen WAF Audit Threat Alert"
    
    Forward a threat detection made by Fastly Next-Gen WAF Audit Logs
    
    - **Effort:** master
    
??? abstract "Fortigate IPS Critical Alert"
    
    Fortigate intrusion detection alert with critical severity.
    
    - **Effort:** master
    
??? abstract "Fortigate IPS High Severity Alert"
    
    Fortigate intrusion detection alert with high severity.
    
    - **Effort:** master
    
??? abstract "Internet Scanner"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/04/2023 - minor - Support for standard ECS FW fields
            
??? abstract "Internet Scanner Target"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address. This could be a very noisy rule, so be careful to check your detection perimeter before activation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/04/2023 - minor - Support for standard ECS FW fields
            
??? abstract "Veeam Backup & Replication Malware Detection"
    
    Veeam Backup & Replication has detected some malware related activity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/08/2024 - major - Restrict to only one type of event following customer feedback
            
??? abstract "WAF Block Rule"
    
    Detects when one of WAF rule blocked an HTTP request 
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/11/2023 - minor - Adding support for Ubika
            
??? abstract "WAF Correlation Block Multiple Destinations"
    
    Detection of multiple block actions (more than 10) by the Web Application Firewall (WAF) triggered by the same source to mutliple destinations
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "WAF Correlation Block actions"
    
    Detection of multiple block actions (more than 30) triggered by the same source by WAF detection rules
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
**Phishing for Information**

??? abstract "Gatewatcher AionIQ V103 Active CTI"
    
    Detects whan an event related to CTI is raised by Gatewatcher V103. An attacker may be gathering information with this event.
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ V103 Retrohunt"
    
    Detects when a retrohunt event is raised by GatewatcherV103.
    
    - **Effort:** master
    
## Resource Development
**Acquire Infrastructure**

??? abstract "Login Brute-Force Successful On ArubaOS Switch"
    
    A user has attempted to login several times (brute-force) on ArubaOS switch and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On AzureAD From Single IP Address"
    
    A user has attempted to login several times (brute-force) on AzureAD and succeeded to login, all from the same source IP address and in a timerange of 5 minutes.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
        - 16/08/2024 - minor - The error code 50078 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
        - 14/10/2024 - minor - The error codes 70043, 50173, 70008, 700082, 9002341 have been excluded as they are not related to login failures that we want to detect and caused several false positives.
        - 28/11/2024 - minor - Adding error codes as filters to reduce false positives.
            
??? abstract "Login Brute-Force Successful On Jumpcloud Portal"
    
    A user has attempted to login several times (brute-force) on Jumpcloud Portal and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Jumpcloud Workstation"
    
    A user has attempted to login several times (brute-force) on Jumpcloud monitored workstations (windows, linux, mac) and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Okta"
    
    A user has attempted to login several times (brute-force) on Okta and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Rubycat PROVE IT"
    
    A user has attempted to login several times (brute-force) through Rubycat PROVE IT protected devices and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On WatchGuard Firebox"
    
    A user has attempted to login several times (brute-force) on WatchGuard Firebox and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Microsoft Entra ID (Azure AD) Abnormal Token"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Anonymous IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced
    
??? abstract "Microsoft Entra ID (Azure AD) Impossible Travel"
    
    Detects when Microsoft Entra ID (Azure AD) identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Leaked Credentials"
    
    Detects when Microsoft Entra ID (Azure AD) identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Login Failed Brute-Force From Single IP Address"
    
    A user has attempted to login several times (brute-force) on AzureAD and failed every time, all from the same source IP address and in a timerange of 5 minutes.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/03/2024 - major - More precise list of error codes to reduce false positives.
            
??? abstract "Microsoft Entra ID (Azure AD) Malicious IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/07/2024 - minor - Change similarity strategy.
            
??? abstract "Microsoft Entra ID (Azure AD) Password Spray"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Sign-in From Unlikely Country"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Successful Password Spraying From Single IP Address"
    
    An IP address performed several failed logins on multiple users to then have a successful login on one of them. Note that even if the sign-in was blocked by MFA (error 50074/50076/50158) or conditional access (error 50097/53003), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/03/2024 - major - More precise list of error codes for success and failure to reduce false positives.
            
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
    
??? abstract "Okta MFA Brute-Force Successful"
    
    A user has attempted to login several times (brute-force) on Okta and succeeded to login by spamming MFA.
    
    - **Effort:** advanced
    
**Compromise Infrastructure**

??? abstract "Login Brute-Force Successful On ArubaOS Switch"
    
    A user has attempted to login several times (brute-force) on ArubaOS switch and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On AzureAD From Single IP Address"
    
    A user has attempted to login several times (brute-force) on AzureAD and succeeded to login, all from the same source IP address and in a timerange of 5 minutes.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
        - 16/08/2024 - minor - The error code 50078 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
        - 14/10/2024 - minor - The error codes 70043, 50173, 70008, 700082, 9002341 have been excluded as they are not related to login failures that we want to detect and caused several false positives.
        - 28/11/2024 - minor - Adding error codes as filters to reduce false positives.
            
??? abstract "Login Brute-Force Successful On Jumpcloud Portal"
    
    A user has attempted to login several times (brute-force) on Jumpcloud Portal and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Jumpcloud Workstation"
    
    A user has attempted to login several times (brute-force) on Jumpcloud monitored workstations (windows, linux, mac) and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Okta"
    
    A user has attempted to login several times (brute-force) on Okta and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On Rubycat PROVE IT"
    
    A user has attempted to login several times (brute-force) through Rubycat PROVE IT protected devices and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force Successful On WatchGuard Firebox"
    
    A user has attempted to login several times (brute-force) on WatchGuard Firebox and succeeded to login.
    
    - **Effort:** advanced
    
??? abstract "Microsoft Entra ID (Azure AD) Abnormal Token"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Anonymous IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** advanced
    
??? abstract "Microsoft Entra ID (Azure AD) Impossible Travel"
    
    Detects when Microsoft Entra ID (Azure AD) identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Leaked Credentials"
    
    Detects when Microsoft Entra ID (Azure AD) identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Login Failed Brute-Force From Single IP Address"
    
    A user has attempted to login several times (brute-force) on AzureAD and failed every time, all from the same source IP address and in a timerange of 5 minutes.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/03/2024 - major - More precise list of error codes to reduce false positives.
            
??? abstract "Microsoft Entra ID (Azure AD) Malicious IP"
    
    Detects when Microsoft Entra ID (Azure AD) identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/07/2024 - minor - Change similarity strategy.
            
??? abstract "Microsoft Entra ID (Azure AD) Password Spray"
    
    Detects when Microsoft Entra ID (Azure AD) indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Sign-in From Unlikely Country"
    
    Detects when Microsoft Entra ID (Azure AD) identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Successful Password Spraying From Single IP Address"
    
    An IP address performed several failed logins on multiple users to then have a successful login on one of them. Note that even if the sign-in was blocked by MFA (error 50074/50076/50158) or conditional access (error 50097/53003), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/03/2024 - major - More precise list of error codes for success and failure to reduce false positives.
            
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
    
??? abstract "Okta MFA Brute-Force Successful"
    
    A user has attempted to login several times (brute-force) on Okta and succeeded to login by spamming MFA.
    
    - **Effort:** advanced
    
**Compromise Accounts**

??? abstract "Cisco Identity Services Engine Configuration Changed"
    
    Cisco Identity Services Engine (ISE) has detected a device configuration changed (Added, Changed or Deleted). This should be reviewed in order to check if this an expected admin action.
    
    - **Effort:** master
    
??? abstract "Correlation Jumpcloud User Logged In From Multiple Countries"
    
    Detection of login events from multiple countries on Jumpcloud portal.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender for Office 365 High Severity AIR Alert"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a High severity alert triggers an automated investigation, such as when a potentially malicious URL click was detected, or when a user is restricted from sending email.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender for Office 365 Medium Severity AIR Alert"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Medium severity alert triggers an automated investigation, such as when suspicious email sending patterns are detected from an account.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Okta Reuse Device Token"
    
    Detection of the reusing of Device Token.
    
    - **Effort:** intermediate
    
??? abstract "Okta User Logged In From Multiple Countries"
    
    Detection of login events from multiple countries.
    
    - **Effort:** intermediate
    
??? abstract "Okta User Logged In Multiple Applications"
    
    Detection of login events on multiple application.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 07/08/2023 - major - Switching type from event_count to value_count | Adding Target in order to match only on different Apps
            
??? abstract "Varonis Data Security Email Alert"
    
    Varonis Data Security has raised an alert related to a supervised email account.
    
    - **Effort:** master
    
??? abstract "Varonis Data Security Network Alert"
    
    Varonis Data Security has raised an alert related to a network rule
    
    - **Effort:** master
    
**Obtain Capabilities**

??? abstract "Cyberwatch Detection Critical Vulnerability"
    
    Cyberwatch Detection has detected an asset with a critical vulnerability 
    
    - **Effort:** master
    
??? abstract "ESET Protect Vulnerability Exploitation Attempt"
    
    Detects when an attempt is made to exploit a vulnerability.
    
    - **Effort:** master
    
??? abstract "Elevated Shell Launched By Browser"
    
    Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.
    
    - **Effort:** master
    
??? abstract "Privilege Escalation Awesome Scripts (PEAS)"
    
    Detect PEAS privileges escalation scripts and binaries
    
    - **Effort:** elementary
    
## Initial Access
**Valid Accounts**

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - add similarity strategy
            
??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - Add similarity strategy
            
??? abstract "Account Tampering - Suspicious Failed Logon Reasons"
    
    This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Admin User RDP Remote Logon"
    
    Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Authentication Impossible Travel"
    
    Detects impossible travel when performing authentication from a source IP address, grouped by username.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/07/2024 - major - review filter to avoid false positive
            
??? abstract "Broadcom Edge Secure Web Gateway High Threat"
    
    Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.
    
    - **Effort:** master
    
??? abstract "Brute-Force On Fortinet Firewall Login"
    
    Spots many failed attempts to log on an administration interface.
    
    - **Effort:** master
    
??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Minor change in selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Fortigate Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Account Suspended"
    
    Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Added"
    
    Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Authorized"
    
    Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Attack Warning"
    
    Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".
    
    - **Effort:** intermediate
    
??? abstract "Google Workspace Account Warning"
    
    Detects a suspicious login, leaked password, or account disabled following suspicious activity.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Creation"
    
    Detects when an admin is created or when his role is changed.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Adding new element to increase detection.
            
??? abstract "Google Workspace Suspicious Login"
    
    Detects a suspicious login reported by google.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force On Firewall"
    
    Detects successful access to administration console of a firewall after several failure.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force On FreeRadius"
    
    A user has attempted to login several times (brute-force) with error then one success.
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force On Sekoia.io"
    
    Detects successful access to Sekoia.io after several failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "Microsoft 365 Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)
    
    - **Effort:** master
    
??? abstract "Netskope Admin Audit"
    
    Audit events for admin activites, from Logins to policies' changes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "Okta Many Passwords Reset Attempt"
    
    This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.
    
    - **Effort:** advanced
    
??? abstract "Okta Suspicious Activity Reported"
    
    Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.
    
    - **Effort:** advanced
    
??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** master
    
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
**Replication Through Removable Media**

??? abstract "External Disk Drive Or USB Storage Device"
    
    Detects external diskdrives or plugged in USB device.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**External Remote Services**

??? abstract "Anomaly New PowerShell Remote Session"
    
    Detects when PowerShell remote sessions are created in a short amount of time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/06/2024 - minor - Adding fields to be displayed in the alert.
            
??? abstract "Datadome Protection Intrusion Detection"
    
    Detects when Datadome protection raises an alert linked to intrusion. Datadome is used against fraud and bots.
    
    - **Effort:** master
    
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "SecurityScorecard Vulnerability Assessment Scanner New Issues"
    
    Raises an alert when SecurityScorecard Vulnerability Assessment Scanner find new issues.
    
    - **Effort:** master
    
??? abstract "Trend Micro Apex One Intrusion Detection Alert"
    
    Trend Micro Apex One has raised an alert for an intrusion detection.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trend Micro Cloud One High Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a high severity level.
    
    - **Effort:** master
    
??? abstract "Trend Micro Cloud One Low Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a low severity level.
    
    - **Effort:** master
    
??? abstract "Trend Micro Cloud One Medium Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a medium severity level.
    
    - **Effort:** master
    
**Exploit Public-Facing Application**

??? abstract "CVE-2018-11776 Apache Struts2"
    
    Apache Struts versions 2.3 to 2.3.34 and 2.5 to 2.5.16 suffer from possible Remote Code Execution when alwaysSelectFullNamespace is true (either by user or a plugin like Convention Plugin) and then: results are used with no namespace and in same time, its upper package have no or wildcard namespace and similar to results, same possibility when using url tag which doesn't have value and action set and in same time, its upper package have no or wildcard namespace.
    
    - **Effort:** intermediate
    
??? abstract "CVE-2018-13379 Fortinet Exploit"
    
    Detects the successful exploitation of the Fortinet FortiOS CVE-2018-13379. This CVE is one of the most exploited CVEs since 2018. It is exploited by APT threat actors as well as cybercriminals. The exploitation of this CVE lead an unauthenticated user to get full access to FortiOS system file through SSL VPN via specially crafted HTTP resource requests. The exploit read /dev/cmdb/sslvpn_websession file, that contains login and passwords in (clear/text). An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects FortiOS 5.6.3 to 5.6.7 and FortiOS 6.0.0 to 6.0.4.
    
    - **Effort:** advanced
    
??? abstract "CVE-2019-0604 SharePoint"
    
    Detects the exploitation of the SharePoint vulnerability (CVE-2019-0604).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/11/2024 - minor - Added filter to reduce false positives
            
??? abstract "CVE-2019-11510 Pulse Secure Exploit"
    
    Detects the successful exploitation of the Pulse Secure vulnerability CVE-2019-11510. This CVE is one of the most exploited CVEs since 2019. It is exploited by diverse threat actors, leading sometimes in ransomware deployement among these groups: Maze, Conti, Egregor, DoppelPaymer, NetWalker and REvil. But also APT actors such as APT29. The exploitation of this CVE allows a remote, unauthenticated attacker to compromise a vulnerable VPN server. The attacker may be able to gain access to all active users and their plain-text credentials. It may also be possible for the attacker to execute arbitrary commands on each VPN client as it successfully connects to the VPN server. The exploit reads /etc/passwd file to get access to login and passwords in (clear/text). An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects 8.1R15.1, 8.2 before 8.2R12.1, 8.3 before 8.3R7.1, and 9.0 before 9.0R3.4 products.
    
    - **Effort:** elementary
    
??? abstract "CVE-2019-19781 Citrix NetScaler (ADC)"
    
    Detects CVE-2019-19781 exploitation attempt against Citrix NetScaler (ADC), Application Delivery Controller and Citrix Gateway Attack.
    
    - **Effort:** elementary
    
??? abstract "CVE-2019-2725 Oracle Weblogic Exploit"
    
    Detects the successful exploitation of a deserialization vulnerability in Oracle Weblogic Server, CVE-2019-2725. This vulnerability affects versions 10.X and 12.1.3 of WebLogic that have the components wls9_async_response.war and wls-wsat.war enabled. It is a remote code execution which can be exploited without authentication via HTTP. An HTTP response status code = 202, means the target is vulnerable, the analyst then has to look in depth to check if a webshell has been uploaded or something else has been done.
    
    - **Effort:** elementary
    
??? abstract "CVE-2020-0688 Microsoft Exchange Server Exploit"
    
    Detects the exploitation of CVE-2020-0688. The POC exploit a .NET serialization vulnerability in the Exchange Control Panel (ECP) web page. The vulnerability is due to Microsoft Exchange Server not randomizing the keys on a per-installation basis resulting in them using the same validationKey and decryptionKey values. With knowledge of these, values an attacker can craft a special viewstate to use an OS command to be executed by NT_AUTHORITY\SYSTEM using .NET deserialization. To exploit this vulnerability, an attacker needs to leverage the credentials of an account it had already compromised to authenticate to OWA.
    
    - **Effort:** elementary
    
??? abstract "CVE-2020-1147 SharePoint"
    
    Detection of SharePoint vulnerability CVE-2020-1147.
    
    - **Effort:** advanced
    
??? abstract "CVE-2020-14882 Oracle WebLogic Server"
    
    Detects the exploitation of the Oracle WebLogic Server vulnerability (CVE-2020-16952).
    
    - **Effort:** advanced
    
??? abstract "CVE-2020-17530 Apache Struts RCE"
    
    Detects the exploitation of the Apache Struts RCE vulnerability (CVE-2020-17530).
    
    - **Effort:** intermediate
    
??? abstract "CVE-2020-5902 F5 BIG-IP Exploitation Attempts"
    
    Detects the exploitation attempt of the vulnerability found in F5 BIG-IP and described in CVE-2020-5902.
    
    - **Effort:** elementary
    
??? abstract "CVE-2021-20021 SonicWall Unauthenticated Administrator Access"
    
    Detects the exploitation of SonicWall Unauthenticated Admin Access.
    
    - **Effort:** advanced
    
??? abstract "CVE-2021-21972 VMware vCenter"
    
    The vSphere Client (HTML5) contains a remote code execution vulnerability in a vCenter Server plugin. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.x before 7.0 U1c, 6.7 before 6.7 U3l and 6.5 before 6.5 U3n) and VMware Cloud Foundation (4.x before 4.2 and 3.x before 3.10.1.2). POST request on the following PATH "/ui/vropspluginui/rest/services/uploadova". If in response body (500) the words it has "uploadFile", that means the vCenter is available to accept files via POST without any restrictions.
    
    - **Effort:** intermediate
    
??? abstract "CVE-2021-21985 VMware vCenter"
    
    The VMware vSphere Client (HTML5) contains a remote code execution vulnerability due to lack of input validation in the Virtual SAN Health Check plug-in which is enabled by default in vCenter Server. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.0 before 7.0 U2b, 6.7 before 6.7 U3n and 6.5 before 6.5 U3p) and VMware Cloud Foundation (4.x before 4.2.1 and 3.x before 3.10.2.1).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CVE-2021-22123 Fortinet FortiWeb OS Command Injection"
    
    Detects Fortinet FortiWeb OS Command Injection (August 2021) vulnerability exploitation attempt. A remote, authenticated attacker can execute arbitrary commands on the system hosting a vulnerable FortiWeb WAF by sending a POST request with the command in the name field. At the time of writing this rule, it would appear that the request would respond in code 500 for a successful exploitation attempt.
    
    - **Effort:** advanced
    
??? abstract "CVE-2021-22893 Pulse Connect Secure RCE Vulnerability"
    
    Detects potential exploitation of the authentication by-pass vulnerability that can allow an unauthenticated user to perform remote arbitrary file execution on the Pulse Connect Secure gateway. It is highly recommended to apply the Pulse Secure mitigations and seach for indicators of compromise on affected servers if you are in doubt over the integrity of your Pulse Connect Secure product.
    
    - **Effort:** intermediate
    
??? abstract "CVE-2021-22986 F5 BIG-IP iControl REST Unauthenticated RCE"
    
    Detects successful exploitation of the F5 BIG-IP vulnerability CVE-2021-22986.
    
    - **Effort:** elementary
    
??? abstract "CVE-2021-26855 Exchange SSRF"
    
    Detects the exploitation of ProyxLogon vulerability on Exchange servers.
    
    - **Effort:** advanced
    
??? abstract "CVE-2021-34527 PrintNightmare Suspicious Actions From Spoolsv"
    
    Detects suspicious image loads and file creations from the spoolsv process which could be a sign of an attacker trying to exploit the PrintNightmare vulnerability, CVE-2021-34527. A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. This works as well as a Local Privilege escalation vulnerability. To fully work the rule requires to log for Loaded DLLs and File Creations, which can be done respectively using the Sysmon's event IDs 7 and 11.
    
    - **Effort:** master
    
??? abstract "CVE-2021-41773 Apache 2.4.49 Path Traversal"
    
    Detects successful exploitation of the Apache Path Traversal CVE-2021-41773.
    
    - **Effort:** advanced
    
??? abstract "CVE-2021-43798 Grafana Directory Traversal"
    
    Grafana version 8.x has a 0day arbitrary file read (with no fix yet) based on a directory traversal vulnerability
    
    - **Effort:** intermediate
    
??? abstract "Exploited CVE-2020-10189 Zoho ManageEngine"
    
    Detects the exploitation of Zoho ManageEngine Desktop Central Java Deserialization vulnerability reported as CVE-2020-10189.
    
    - **Effort:** elementary
    
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "GitLab CVE-2021-22205"
    
    Detects GitLab vulnerability CVE-2021-22205 exploitation success. It allows an attacker to do some remote code execution with user git. The HTTP return code 422 indicates a successfull exploitation.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious DNS Child Process"
    
    Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).
    
    - **Effort:** intermediate
    
**Hardware Additions**

??? abstract "External Disk Drive Or USB Storage Device"
    
    Detects external diskdrives or plugged in USB device.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Phishing**

??? abstract "Cisco ESA Suspicious Email With Attachment"
    
    Detects an email with an attachment, from a sender tagged as suspect, detected by either the Antivirus or the Advanced Malware Protection (AMP) engine and delivered to the recipient
    
    - **Effort:** advanced
    
??? abstract "Cisco Umbrella Threat Detected"
    
    Cisco Umbrella has detected a malicious traffic categorized as malware, phishing or adware.
    
    - **Effort:** intermediate
    
??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master
    
??? abstract "Download Files From Suspicious TLDs"
    
    Detects download of certain file types from hosts in suspicious TLDs
    
    - **Effort:** master
    
??? abstract "ESET Protect Malware"
    
    Detects when Eset Protect tagged an event as linked to a malware with infected files.
    
    - **Effort:** master
    
??? abstract "Google Workspace Blocked Sender"
    
    Detects when a user is blocked by google workspace.
    
    - **Effort:** advanced
    
??? abstract "Malware Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message.
    
    - **Effort:** master
    
??? abstract "Malware Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message and didn't delete it.
    
    - **Effort:** advanced
    
??? abstract "Microsoft 365 (Office 365) Anti-Phishing Policy Deletion"
    
    Detects when the anti-phishing policy is removed from Microsoft 365 (Office 365). By default, Microsoft 365 (Office 365) includes built-in features that help protect users from phishing attacks. This policy specifies the phishing protections to enable or disable, and the actions to apply options.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Anti-Phishing Rule Deletion"
    
    Detects the deactivation of the anti-phishing rule from Microsoft 365 (Office 365). The anti-phishing rule specifies the priority and recipient filters (who the policy applies to) for an anti-phish policy.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) AtpDetection"
    
    Detects when an AtpDetection (Advanced Threat Protection) event from the Office365 ThreatIntelligence service is raised. AtpDetection is a service which secures emails, attachments, and files by scanning them for threats.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) DLP Policy Removed"
    
    Detects when a DLP (Data Loss Prevention) policy is removed in Microsoft 365 (Office 365). DLP policies defines which resources can be shared and with whom, preventing sensitive information from being leaked.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Detection Velocity"
    
    Detects when Microsoft Cloud App Security identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Inbox Hiding"
    
    Detects when Microsoft Cloud App Security identifies that a suspicious inbox rule was set on a user’s inbox. This may indicate that the user account is compromised, and that the mailbox is being used to distribute spam and malware in your organization. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS New Country"
    
    Detects when Microsoft Cloud App Security identifies a sign-in from a country where it has never connected. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Repeated Delete"
    
    Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Repeated Failed Login"
    
    Detects when Microsoft Cloud App Security identifies a large number of failed login attempts which may indicate a brute-force attempt. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Risky IP"
    
    Detects when Microsoft Cloud App Security identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MailBoxAuditBypassAssociation Option Implementation"
    
    Detects the implementation of a MailBoxAuditBypassAssociation option in Microsoft 365 (Office 365). This option is used when you configure a user or computer account to bypass mailbox audit logging, access or actions taken by the user or computer account to any mailbox isn't logged.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Filter Policy Removed"
    
    Detects when a malware policy has been deleted in Microsoft 365 (Office 365). A malware filter policy is used to alert administrators that an internal user sent a message that contained malware.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Filter Rule Deletion"
    
    Detects when a malware filter rule has been deleted in Microsoft 365 (Office 365). The malware filter rule specifies the priority and recipient filters (who the policy applies to) for a malware filter policy.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Uploaded On OneDrive"
    
    Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to OneDrive. Attackers can use this method to propagate through the network.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) Malware Uploaded On SharePoint"
    
    Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to SharePoint. Attackers can use this method to propagate through the network.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) Mass Download By A Single User"
    
    Identifies when Microsoft Cloud App Security reports that a single user performs more than 50 downloads within 1 minute.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft 365 (Office 365) Potential Ransomware Activity Detected"
    
    Detects when Microsoft Cloud App Security reports that a user has uploaded files to the cloud that might be infected with ransomware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft 365 (Office 365) Safe Attachment Rule Disabled"
    
    Detects when the safe attachment rule has been deleted in Microsoft 365 (Office 365). Safe Attachments is a feature in Microsoft Defender for Microsoft 365 (Office 365) that opens email attachments in a special hypervisor environment to detect malicious activity.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Safelinks Disabled"
    
    Detects when a safelink rule has been deleted in Microsoft 365 (Office 365). Safe Links is a feature in Defender for Microsoft 365 (Office 365) that provides URL scanning and rewriting of inbound email messages in mail flow, and time-of-click verification of URLs and links in email messages and other locations.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Unusual Volume Of File Deletion"
    
    Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft 365 Security and Compliance Center High Severity Alert"
    
    A security or compliance-related alert of high severity was raised, based on the policies of the tenant. This rule can be very noisy depending on the configuration of the tenant. Alert filters are likely required. In addition, most alerts don't include any context, and are only useful if the analysts have access to the Microsoft portals to investigate.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 Security and Compliance Center Medium Severity Alert"
    
    A security or compliance-related alert of medium severity was raised, based on the policies of the tenant. This rule can be very noisy depending on the configuration of the tenant. Alert filters are likely required. In addition, most alerts don't include any context, and are only useful if the analysts have access to the Microsoft portals to investigate.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender for Office 365 High Severity AIR Alert"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a High severity alert triggers an automated investigation, such as when a potentially malicious URL click was detected, or when a user is restricted from sending email.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender for Office 365 Low Severity AIR Alert Handled Automatically"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Low or Informational severity alert triggered an automated investigation, and remediation was conducted automatically. Low and Informational alerts include when an email is reported by a user, or when a malicious email is removed after delivery.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender for Office 365 Low Severity AIR Alert Requires Action"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Low or Informational severity alert triggered an automated investigation, and remediation actions need to be approved or conducted. Low and Informational alerts include when an email is reported by a user, or when a malicious email is removed after delivery.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender for Office 365 Medium Severity AIR Alert"
    
    Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Medium severity alert triggers an automated investigation, such as when suspicious email sending patterns are detected from an account.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses"
    
    Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.
    
    - **Effort:** intermediate
    
??? abstract "Okta Phishing Detection with FastPass Origin Check"
    
    Okta's FastPass prevents known phishing sites.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Phishing Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a phishing attempt.
    
    - **Effort:** master
    
??? abstract "Phishing Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365 has detected a phishing attempt and didn't move it to junk folder.
    
    - **Effort:** advanced
    
??? abstract "Possible Malicious File Double Extension"
    
    Detects request to potential malicious file with double extension
    
    - **Effort:** elementary
    
??? abstract "Proofpoint TAP Email Classified As Malware But Allowed"
    
    An email was classified as malware with a threat score greater than 0 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.
    
    - **Effort:** advanced
    
??? abstract "Proofpoint TAP Email Classified As Phishing But Allowed"
    
    An email was classified as phishing with a threat score greater than 50 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.
    
    - **Effort:** advanced
    
??? abstract "Proofpoint TAP Email Classified As Spam But Allowed"
    
    An email was classified as spam with a threat score greater than 50 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.
    
    - **Effort:** advanced
    
??? abstract "RDP Configuration File From Mail Process"
    
    Detects RDP configuration file being created or executed by a Mail-related process like Outlook. RDP configuration file will allow, when opened, an user to connect to the configured server easily. Attackers use this to trick victims in order to get a shared drive and potentially retrieve the data from that drive, but also drop a malicious file on the drive to establish persistence. Using RDP can also expose the victim's credential and clipboard data on some cases.
    
    - **Effort:** advanced
    
??? abstract "Retarus Email Security Threat Detected (CxO Or Patient Zero Detection)"
    
    Cx0 fraud and Patient Zero Detection alerts detected by Retarus Email Security. CxO Fraud Detection uses algorithms that identify from-spoofing and domain-spoofing, to detect falsified sender addresses (e.g. from high level executives - CEO, CFO...). Patient Zero Detection® uses a digital fingerprint to identify emails containing malware that have already been delivered.
    
    - **Effort:** advanced
    
??? abstract "Retarus Email Security Threat Detected (MultiScan)"
    
    Antivirus MultiScan alerts detected by Retarus Email Security. AntiVirus MultiScan automatically scans incoming and outgoing emails and file attachments for viruses with up to four virus scanners and uses heuristic analysis to protect from unknown malware.
    
    - **Effort:** intermediate
    
??? abstract "Retarus Email Security Threat Detected (Sandboxing)"
    
    Sandboxing alerts detected by Retarus Email Security. Sandboxing subjects specific file attachments to an in-depth analysis. Retarus uses a sandboxing solution from the specialized and highly respected third-party provider Palo Alto Networks for this advanced threat assessment. Emails identified as infected are either deleted or quarantined, and the intended recipient is notified.
    
    - **Effort:** elementary
    
??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
    
??? abstract "Scam Detected By Vade For M365"
    
    Vade Secure product Vade for M365, has detected a scam e-mail.
    
    - **Effort:** master
    
??? abstract "Scam Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365, has detected a scam e-mail and didn't block it.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 18/06/2024 - minor - Adding filter when whitelisted.
            
??? abstract "Spam Detected By Vade For M365"
    
    Vade Secure product Vade for M365, has detected a spam e-mail.
    
    - **Effort:** master
    
??? abstract "Spam Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365, has detected a spam e-mail and didn't block it.
    
    - **Effort:** advanced
    
??? abstract "Spearphishing (CEO Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with CEO fraud thematic. Impersonation of CEO or senior management members requesting urgent money transfer, usually on an unknown RIB.
    
    - **Effort:** master
    
??? abstract "Spearphishing (Gift Cards Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spear-phishing attempt with gift-cards fraud thematic. Executive impersonation requesting a money transfer to set up gift-cards for employees. Confidentiality and discretion are usually implied.
    
    - **Effort:** master
    
??? abstract "Spearphishing (Initial Contact Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with initial contact fraud thematic. Do not contains any malicious content or specific actions other than a request to reply to the email. “Are you available?”. The main goal is to incite a reply that could register the sending address as a known and legitimate address.
    
    - **Effort:** master
    
??? abstract "Spearphishing (Lawyer Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with lawyer fraud thematic. Impersonation of lawyers and lawyers' firms. The main goal is to make sure the victims will not raise awareness around them. Confidentiality restrictions are implied.
    
    - **Effort:** master
    
??? abstract "Spearphishing (W2 Fraud) Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a spearphishing attempt with W2 fraud thematic. Executive or HR impersonation phishing for social security numbers or tax identification numbers. Collected data are generally used for identity theft schemes.
    
    - **Effort:** master
    
??? abstract "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
            
??? abstract "Suspicious Download Links From Legitimate Services"
    
    Detects users clicking on Google docs links to download suspicious files. This technique was used a lot by Bazar Loader in the past.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 13/06/2024 - minor - Adding similarity strategy and changing effort level.
        - 15/10/2024 - minor - Adding filter to reduce false positives.
            
??? abstract "Suspicious Email Attachment Received"
    
    Detects email containing a suspicious file as an attachment, based on its extension.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/04/2024 - minor - Update email from field to latest parser format
        - 14/11/2024 - major - Adding new file extension and new condition to make the rule broader as it can now match on more intakes.
            
??? abstract "Suspicious Hangul Word Processor Child Process"
    
    Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate
    
## Execution
**Windows Management Instrumentation**

??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary
    
??? abstract "Impacket Wmiexec Module"
    
    Detection of impacket's wmiexec example, used by attackers to execute commands remotely.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 22/03/2024 - minor - improve filter to extand detection
            
??? abstract "Invoke-TheHash Commandlets"
    
    Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Mshta Execution From Wmi"
    
    Detects mshta executed by wmiprvse as parent. It has been used by TA505 with some malicious documents.
    
    - **Effort:** intermediate
    
??? abstract "WMI DLL Loaded Via Office"
    
    Detects Windows Management Instrumentation (WMI) DLL loaded via Office process. This activity may correspond to VBA macro executing WMI commands, which is highly suspicious. The prerequisite is to log Loaded DLLs images, which can be done with the Sysmon Event ID 7 (DLL image loaded by process).
    
    - **Effort:** master
    
??? abstract "WMI Fingerprint Commands"
    
    Detects attacker fingerprint activities based on the correlation of specific WMIC commands. This has been observed with Aurora malware.
    
    - **Effort:** intermediate
    
??? abstract "WMI Install Of Binary"
    
    Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.
    
    - **Effort:** elementary
    
??? abstract "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)
            
??? abstract "WMImplant Hack Tool"
    
    WMImplant is a powershell framework used by attacker for reconnaissance and exfiltration, this rule attempts to detect WMimplant arguments and invokes commands. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 29/11/2023 - minor - Added a selection to filter some false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Wmic Process Call Creation"
    
    The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 01/08/2023 - major - Rewritten as a regex to reduce false positives
            
??? abstract "Wmic Service Call"
    
    Detects either remote or local code execution using wmic tool.
    
    - **Effort:** intermediate
    
??? abstract "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate
    
**Scheduled Task/Job**

??? abstract "BazarLoader Persistence Using Schtasks"
    
    Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.
    
    - **Effort:** intermediate
    
??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary
    
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cron Files Alteration"
    
    Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace App Script Scheduled Task"
    
    Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.
    
    - **Effort:** advanced
    
??? abstract "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate
    
??? abstract "Remote Task Creation Via ATSVC Named Pipe"
    
    Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/03/2024 - minor - change filter to ACL hex value
            
??? abstract "STRRAT Scheduled Task"
    
    Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'
    
    - **Effort:** intermediate
    
??? abstract "Schtasks Persistence With High Privileges"
    
    Detection of scheduled task with high privileges used by attacker for persistence.
    
    - **Effort:** elementary
    
??? abstract "Schtasks Suspicious Parent"
    
    Detects schtasks started from suspicious and/or unusual processes.
    
    - **Effort:** intermediate
    
??? abstract "Spyware Persistence Using Schtasks"
    
    Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Scheduled Task Creation"
    
    Detects suspicious scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 
    
    - **Effort:** intermediate
    
??? abstract "Windows Suspicious Scheduled Task Creation"
    
    The rule identify creation of new scheduled task who run suspicious or dangerous command
    
    - **Effort:** intermediate
    
**Command and Scripting Interpreter**

??? abstract "AWS CloudTrail EC2 Startup Script Changed"
    
    Detects changes to the EC2 instance startup script. The shell script will be executed as root/SYSTEM everytime the specific instances are booted up.
    
    - **Effort:** intermediate
    
??? abstract "AWS GuardDuty High Severity Alert"
    
    GuardDuty has detected a threat with a high severity level. A High severity level indicates that the resource in question (an EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "AWS GuardDuty Low Severity Alert"
    
    GuardDuty has detected a threat with a low severity level. A low severity level indicates attempted suspicious activity that did not compromise your network, for example, a port scan or a failed intrusion attempt.
    
    - **Effort:** master
    
??? abstract "AWS GuardDuty Medium Severity Alert"
    
    GuardDuty has detected a threat with a medium severity level. A Medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Alternate PowerShell Hosts Pipe"
    
    Detects alternate PowerShell hosts potentially bypassing detections looking for powershell.exe. Prerequisites are logging for PipeEvents in Sysmon config.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
        - 25/11/2024 - minor - improve filter to avoid false positives.
            
??? abstract "Aspnet Compiler"
    
    Detects the starts of aspnet compiler.
    
    - **Effort:** advanced
    
??? abstract "AutoIt3 Execution From Suspicious Folder"
    
    Detects AutoIt3 execution from an unusual/suspicious folder. Legitimate folders are "Program Files" and "AppData\\Local". AutoIt3.exe is a legitimate process used to execute AutoIt program files, which are used by legitimate software, custom scripts, but also malware. Finding AutoIt3 execution from unusual/suspicious folder can help detect malware activities, such as DarkGate execution. The detection rule can be tailored to your environment and your use of AutoIt3 by filtering out folder's execution of legitimate applications or scripts.
    
    - **Effort:** advanced
    
??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - minor - Adapted the rule to remove false positives.
            
??? abstract "Correlation Linux Decode And Exec"
    
    A Base64 string has been decoded and executed through a pipe. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "Correlation Supicious Powershell Drop and Exec"
    
    Detects a PowerShell process that download and exec a payload
    
    - **Effort:** intermediate
    
??? abstract "CrowdStrike Falcon Identity Protection Detection Critical Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection High Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Informational Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Low Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Medium Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Critical Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection High Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Informational Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Low Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Medium Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Cybereason EDR Alert"
    
    Cybereason EDR telemetry has raised an alert
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Cybereason EDR Malware Detection"
    
    Cybereason EDR telemetry has detected a malware
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate
    
??? abstract "Default Encoding To UTF-8 PowerShell"
    
    Detects PowerShell encoding to UTF-8, which is used by Sliver implants. The command line just sets the default encoding to UTF-8 in PowerShell.
    
    - **Effort:** advanced
    
??? abstract "Default User www data User Compromised"
    
    User www_data by default cannot log and use a shell, any syscall of type execve induce user compromise
    
    - **Effort:** master
    
??? abstract "Detection of default Mimikatz banner"
    
    Detection of default Mimikatz banner in powershell events
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Elise Backdoor"
    
    Detects Elise backdoor activity as used by Lotus Blossom
    
    - **Effort:** elementary
    
??? abstract "Exploited CVE-2020-10189 Zoho ManageEngine"
    
    Detects the exploitation of Zoho ManageEngine Desktop Central Java Deserialization vulnerability reported as CVE-2020-10189.
    
    - **Effort:** elementary
    
??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate
    
??? abstract "FromBase64String Command Line"
    
    Detects suspicious FromBase64String expressions in command line arguments.
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ V103 Shellcode Detect"
    
    Detects when a suspicious shellcode is used.
    
    - **Effort:** master
    
??? abstract "Generic-reverse-shell-oneliner"
    
    To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using shell commands
    
    - **Effort:** intermediate
    
??? abstract "In-memory PowerShell"
    
    Detects loading of essential DLL used by PowerShell, but not by the process powershell.exe. Detects meterpreter's "load powershell" extension and tool such PowerShDll.
    
    - **Effort:** master
    
??? abstract "Interactive Terminal Spawned via Python"
    
    Identifies when a terminal (tty) is spawned via Python. Attackers may upgrade a simple reverse shell to a fully interactive tty after obtaining initial access to a host.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 02/10/2024 - major - Rule's pattern changed
            
??? abstract "Invoke-TheHash Commandlets"
    
    Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.
    
    - **Effort:** elementary
    
??? abstract "Lazarus Loaders"
    
    Detects different loaders used by the Lazarus Group APT
    
    - **Effort:** elementary
    
??? abstract "Linux Bash Reverse Shell"
    
    To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using shell commands
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force Successful On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Login Failed Brute-Force On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Malicious PowerShell Keywords"
    
    Detects keywords from well-known PowerShell exploitation frameworks
    
    - **Effort:** advanced
    
??? abstract "Malspam Execution Registering Malicious DLL"
    
    Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).
    
    - **Effort:** elementary
    
??? abstract "Malware Outbreak"
    
    Spots a peak of malware detection by windows defender on this perimeter.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line or scripts.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender Antivirus Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender through command line or PowerShell scripts. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Threat Detected"
    
    Detection of a windows defender alert indicating the presence of potential malware
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender XDR Alert"
    
    Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Cloud App Security Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Endpoint Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender XDR Office 365 Alert"
    
    Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Microsoft Office Creating Suspicious File"
    
    Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.
    
    - **Effort:** master
    
??? abstract "Microsoft Office Spawning Script"
    
    Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 
    
    - **Effort:** intermediate
    
??? abstract "Mshta Suspicious Child Process"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 17/10/2024 - minor - Adding similarity_strategy and enforce selection
            
??? abstract "Mustang Panda Dropper"
    
    Detects specific process parameters as used by Mustang Panda droppers
    
    - **Effort:** elementary
    
??? abstract "Okta Security Threat Detected"
    
    Detects when a security threat is detected in Okta.
    
    - **Effort:** intermediate
    
??? abstract "Phorpiex DriveMgr Command"
    
    Detects specific command used by the Phorpiex botnet to execute a copy of the loader during its self-spreading stage. As described by Microsoft, this behavior is unique and easily identifiable due to the use of folders named with underscores "__" and the PE name "DriveMgr.exe".
    
    - **Effort:** elementary
    
??? abstract "PowerShell Commands Invocation"
    
    Detects the execution to invoke a powershell command. This was used in an intrusion using Gootloader to access Mimikatz.
    
    - **Effort:** advanced
    
??? abstract "PowerShell Credential Prompt"
    
    Detects PowerShell calling a credential prompt (using PromptForCredential), like $Credential = $host.ui.PromptForCredential("Need credentials", "Please enter your user name and password.", "", "NetBiosUserName"). The same result can be obtained by using the Get-Credential function but detecting it will trigger a lot of FP.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
            
??? abstract "PowerShell Downgrade Attack"
    
    Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0
    
    - **Effort:** elementary
    
??? abstract "PowerShell Download From URL"
    
    Detects a Powershell process that contains download commands in its command line string.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.
        - 29/11/2023 - minor - Added a filter to the rule as some false positives were observed.
            
??? abstract "PowerShell EncodedCommand"
    
    Detects popular file extensions in commands obfuscated in base64 run through the EncodedCommand option.
    
    - **Effort:** advanced
    
??? abstract "PowerShell Invoke Expression With Registry"
    
    Detects keywords from well-known PowerShell techniques to get registry key values
    
    - **Effort:** advanced
    
??? abstract "PowerShell Invoke-Obfuscation Obfuscated IEX Invocation"
    
    Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-Obfuscation framework
    
    - **Effort:** advanced
    
??? abstract "PowerShell Malicious Nishang PowerShell Commandlets"
    
    Detects Commandlet names and arguments from the Nishang exploitation framework.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/07/2024 - minor - Removing tools relationships as it was inaccurate
        - 27/08/2024 - minor - improve filter to avoid false positive
            
??? abstract "PowerShell Malicious PowerShell Commandlets"
    
    Detects Commandlet names from well-known PowerShell exploitation frameworks (PowerSploit...).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/01/2024 - minor - Adding exclusion pattern and selection commandlet
        - 26/07/2024 - minor - Removing tools relationships as it was inaccurate
            
??? abstract "PowerShell NTFS Alternate Data Stream"
    
    Detects writing data into NTFS alternate data streams from PowerShell. Needs Script Block Logging (Event ID 4104)
    
    - **Effort:** advanced
    
??? abstract "Powershell Web Request"
    
    Detects the use of various web request methods executed remotely via Windows PowerShell.
    
    - **Effort:** advanced
    
??? abstract "Python Offensive Tools and Packages"
    
    Track installation and usage of offensive python packages and project that are used for lateral movement
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 02/10/2024 - major - Rule's pattern changed
            
??? abstract "QakBot Process Creation"
    
    Detects QakBot like process executions
    
    - **Effort:** intermediate
    
??? abstract "Raw Reverse Shell"
    
    To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using sh and or bash commands
    
    - **Effort:** master
    
??? abstract "Screenconnect Remote Execution"
    
    Detect cmd or powershell remote execution cmdline via ScreenConnect
    
    - **Effort:** intermediate
    
??? abstract "Sekoia.io EICAR Detection"
    
    Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Agent Disabled"
    
    A SentinelOne EDR agent has been disabled according to SentinelOne logs.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR Custom Rule Alert"
    
    A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively"
    
    A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Not Mitigated"
    
    A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR SSO User Added"
    
    A SSO User was added.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Malicious)"
    
    A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Suspicious)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Kill Success"
    
    A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Failed"
    
    A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Success"
    
    A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Remediate Success"
    
    A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR User Failed To Log In To The Management Console"
    
    A user has failed to log in to the management console.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR User Logged In To The Management Console"
    
    A user has logged in to the management console.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
            
??? abstract "Socat Relaying Socket"
    
    Socat is a linux tool used to relay local socket or internal network connection, this technics is often used by attacker to bypass security equipment such as firewall
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "Socat Reverse Shell Detection"
    
    Socat is a linux tool used to relay or open reverse shell that is often used by attacker to bypass security equipment.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "SquirrelWaffle Malspam Execution Loading DLL"
    
    Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Cmd.exe Command Line"
    
    Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
        - 22/11/2024 - major - Adding new elements for detection and filters.
        - 27/11/2024 - minor - Adding new filters to reduce false positives.
            
??? abstract "Suspicious CodePage Switch with CHCP"
    
    Detects a code page switch in command line
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/01/2024 - minor - Rename rule to fit with behavior
            
??? abstract "Suspicious DLL Loaded Via Office Applications"
    
    Detects suspicious DLL being loaded by an Microsoft Office Product. Considered as suspects are some .NET DLLs, clr.dll, GAC DLL, DSParse (Active Directoryi services API) or Kerberos DLLs which may be loaded by MS Office processes when executing a potentially malicious macro. The prerequisite is to log the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
??? abstract "Suspicious File Name"
    
    Detects suspicious file name possibly linked to malicious tool.
    
    - **Effort:** advanced
    
??? abstract "Suspicious Microsoft Defender Antivirus Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master
    
??? abstract "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious PowerShell Invocations - Generic"
    
    Detects suspicious PowerShell invocation command parameters through command line logging or ScriptBlock Logging.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 28/03/2023 - minor - Excluded some commonly observed false positives.
            
??? abstract "Suspicious PowerShell Invocations - Specific"
    
    Detects suspicious PowerShell invocation command parameters.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.
            
??? abstract "Suspicious PowerShell Keywords"
    
    Detects keywords that could indicate the use of some PowerShell exploitation framework.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 23/05/2024 - minor - Added filter to reduce false positives and new suspicious keywords.
            
??? abstract "Suspicious PrinterPorts Creation (CVE-2020-1048)"
    
    Detects new commands that add new printer port which point to suspicious file
    
    - **Effort:** advanced
    
??? abstract "Suspicious Scripting In A WMI Consumer"
    
    Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Windows Script Execution"
    
    Detects wscript.exe or cscript.exe executing a script in user directories (C:\ProgramData or C:\Users) with a .txt extension, which is very suspicious. It could strongly correspond to a malware dropper, as seen during SquirrelWaffle maldoc campaign.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - major - Review of the rule to reduce false positives.
            
??? abstract "Suspicious XOR Encoded PowerShell Command Line"
    
    Detects suspicious powershell process which includes bxor command, alternative obfuscation  method to b64 encoded commands.
    
    - **Effort:** advanced
    
??? abstract "Sysprep On AppData Folder"
    
    Detects suspicious Sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec). Sysprep is a Windows tool used to change Windows images from a generalized state to a specialized state, and then back to a generalized state. It can be used to remove all system-specific information and reset the computer.
    
    - **Effort:** intermediate
    
??? abstract "TEHTRIS EDR Alert"
    
    Tehtris EDR telemetry has raised an alert.
    
    - **Effort:** master
    
??? abstract "Trend Micro Apex One Data Loss Prevention Alert"
    
    Trend Micro Apex One has raised an alert for data loss prevention.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trend Micro Apex One Malware Alert"
    
    Trend Micro Apex One has detected a malware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trickbot Malware Activity"
    
    Detects Trickbot malware process tree pattern in which rundll32.exe is parent of wermgr.exe.
    
    - **Effort:** intermediate
    
??? abstract "Turla Named Pipes"
    
    Detects a named pipe used by Turla group samples. Prerequisites: Logging for PipeEvents is needed in Sysmon config
    
    - **Effort:** elementary
    
??? abstract "Venom Multi-hop Proxy agent detection"
    
    Detects Venom Multi-hop Proxy agent.
    
    - **Effort:** intermediate
    
??? abstract "WMI DLL Loaded Via Office"
    
    Detects Windows Management Instrumentation (WMI) DLL loaded via Office process. This activity may correspond to VBA macro executing WMI commands, which is highly suspicious. The prerequisite is to log Loaded DLLs images, which can be done with the Sysmon Event ID 7 (DLL image loaded by process).
    
    - **Effort:** master
    
??? abstract "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)
            
??? abstract "WMImplant Hack Tool"
    
    WMImplant is a powershell framework used by attacker for reconnaissance and exfiltration, this rule attempts to detect WMimplant arguments and invokes commands. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 29/11/2023 - minor - Added a selection to filter some false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Web Application Launching Shell"
    
    Detects when a web application launches a shell.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/10/2024 - major - Adding new elements and filters to increase detection and reduce false positives.
            
??? abstract "WithSecure Elements Critical Severity"
    
    WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "WithSecure Elements Warning Severity"
    
    Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).
    
    - **Effort:** master
    
??? abstract "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate
    
??? abstract "Zscaler ZIA Malicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
??? abstract "Zscaler ZIA Suspicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
**Scripting**

??? abstract "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary
    
**Rundll32**

??? abstract "PowerShell Execution Via Rundll32"
    
    Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified
    
    - **Effort:** intermediate
    
**PowerShell**

??? abstract "In-memory PowerShell"
    
    Detects loading of essential DLL used by PowerShell, but not by the process powershell.exe. Detects meterpreter's "load powershell" extension and tool such PowerShDll.
    
    - **Effort:** master
    
**Shared Modules**

??? abstract "FoggyWeb Backdoor DLL Loading"
    
    Detects DLL image load activity as used by the threat group NOBELIUM with the FoggyWeb backdoor loader. The prerequisite is to log Loaded DLLs images, which can be done through the Sysmon Event ID 7 (DLL image loaded by process).
    
    - **Effort:** master
    
**CMSTP**

??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.
            
??? abstract "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate
    
**Exploitation for Client Execution**

??? abstract "Antivirus Exploitation Framework Detection"
    
    Detects a highly relevant Antivirus alert that reports an exploitation framework. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
??? abstract "Antivirus Password Dumper Detection"
    
    Detects a highly relevant Antivirus alert that reports a password dumper. This detection relies on Windows Defender events logs. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
??? abstract "Antivirus Relevant File Paths Alerts"
    
    Detects an Antivirus alert in a highly relevant file path or with a relevant file name. This is only based on Windows Defender events.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master
    
??? abstract "Download Files From Suspicious TLDs"
    
    Detects download of certain file types from hosts in suspicious TLDs
    
    - **Effort:** master
    
??? abstract "Exploit For CVE-2015-1641"
    
    Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641
    
    - **Effort:** elementary
    
??? abstract "Msdt (Follina) File Browse Process Execution"
    
    Detects various Follina vulnerability exploitation techniques. This is based on the Compatability Troubleshooter which is abused to do code execution.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 14/10/2024 - minor - Added filter to the rule to reduce false positives.
        - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "Suspicious Hangul Word Processor Child Process"
    
    Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.
    
    - **Effort:** elementary
    
??? abstract "Suspicious New Printer Ports In Registry"
    
    Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
**User Execution**

??? abstract "AWS GuardDuty High Severity Alert"
    
    GuardDuty has detected a threat with a high severity level. A High severity level indicates that the resource in question (an EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "AWS GuardDuty Low Severity Alert"
    
    GuardDuty has detected a threat with a low severity level. A low severity level indicates attempted suspicious activity that did not compromise your network, for example, a port scan or a failed intrusion attempt.
    
    - **Effort:** master
    
??? abstract "AWS GuardDuty Medium Severity Alert"
    
    GuardDuty has detected a threat with a medium severity level. A Medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Alert High Severity Sesame it Jizo NDR"
    
    Detects a high severity alert raised by SesameIT.
    
    - **Effort:** master
    
??? abstract "Broadcom/Symantec Endpoint Security Event Blocked"
    
    Broadcom/Symantec Endpoint Security blocked an action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master
    
??? abstract "Broadcom/Symantec Endpoint Security Event Cleaned"
    
    Broadcom/Symantec Endpoint Security had cleaned action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master
    
??? abstract "Broadcom/Symantec Endpoint Security Event Quarantined"
    
    Broadcom/Symantec Endpoint Security had a quarantined action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master
    
??? abstract "Broadcom/Symantec Endpoint Security Event Terminate"
    
    Broadcom/Symantec Endpoint Security had a process terminate action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.
    
    - **Effort:** master
    
??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 20/09/2024 - minor - Added new filters to reduce false positives.
        - 27/05/2024 - minor - Added new filters to reduce false positives.
        - 21/11/2023 - minor - Added new filters to reduce false positives.
        - 08/11/2023 - minor - Added filter to reduce false positives
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Critical Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection High Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Informational Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Low Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Medium Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Critical Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection High Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Informational Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Low Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Medium Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Cybereason EDR Alert"
    
    Cybereason EDR telemetry has raised an alert
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Cybereason EDR Malware Detection"
    
    Cybereason EDR telemetry has detected a malware
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Darktrace Threat Visualizer Model Breach Critical Activity"
    
    Darktrace Threat Visualizer has detected a network critical activity related to one supervised device
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 12/11/2024 - minor - Update name, description, similarity and severity
            
??? abstract "Darktrace Threat Visualizer Model Breach Suspicious Activity"
    
    Darktrace Threat Visualizer has detected a network critical activity related to one supervised device
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 12/11/2024 - minor - Update name, description, similarity and severity
            
??? abstract "Darktrace Threat Visualizer Threat Critical Alert"
    
    Darktrace Threat Visualizer has raised a threat critical alert related to one supervised device
    
    - **Effort:** master
    
??? abstract "Darktrace Threat Visualizer Threat Suspicious Alert"
    
    Darktrace Threat Visualizer has raised a threat suspicious alert related to one supervised device
    
    - **Effort:** master
    
??? abstract "Download Files From Non-Legitimate TLDs"
    
    Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.
    
    - **Effort:** master
    
??? abstract "Download Files From Suspicious TLDs"
    
    Detects download of certain file types from hosts in suspicious TLDs
    
    - **Effort:** master
    
??? abstract "ESET Protect Intrusion Detection"
    
    Detects when the solution ESET Protect detects an intrusion.
    
    - **Effort:** master
    
??? abstract "EfficientIP SOLIDServer Suspicious Behavior"
    
    Detects when EfficientIP SOLIDServer forwards a suspicious behavior related to an IP.
    
    - **Effort:** master
    
??? abstract "Exploit For CVE-2015-1641"
    
    Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641
    
    - **Effort:** elementary
    
??? abstract "Explorer Process Executing HTA File"
    
    Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.
    
    - **Effort:** intermediate
    
??? abstract "Gatewatcher AionIQ V103 Malcore"
    
    Detects a malcore alert by Gatewatcher AionIQ V103 related to documents with passwords.
    
    - **Effort:** master
    
??? abstract "Google Workspace Anomaly File Downloads"
    
    Detects a large number of file downloads.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 12/06/2024 - minor - Changing effort level and adding field to alert.
            
??? abstract "HTA Infection Chains"
    
    Detect the creation of a ZIP file and an HTA file as it is often used in infection chains. Furthermore it also detects the use of suspicious processes launched by explorer.exe combined with the creation of an HTA file, since it is also often used in infection chains (LNK - HTA for instance).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 20/09/2024 - minor - File paths added to filter some false positives.
        - 19/09/2024 - minor - File paths added to filter some false positives.
        - 30/11/2023 - minor - Update pattern with new lolbin
            
??? abstract "HarfangLab EDR Critical Level Rule Detection"
    
    HarfangLab EDR has raised an alert based on a critical level rule (not using hlai engine)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/05/2024 - minor - Added filter to exclude threat dataset
            
??? abstract "HarfangLab EDR Critical Threat"
    
    HarfangLab EDR detected a threat with a critical level. This detection by the EDR is based on several detection rules.
    
    - **Effort:** master
    
??? abstract "HarfangLab EDR High Level Rule Detection"
    
    HarfangLab EDR has raised an alert based on a high level rule (not using hlai engine)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/05/2024 - minor - Added filter to exclude threat dataset
            
??? abstract "HarfangLab EDR High Threat"
    
    HarfangLab EDR detected a threat with a high level. This detection by the EDR is based on several detection rules.
    
    - **Effort:** master
    
??? abstract "HarfangLab EDR Hlai Engine Detection"
    
    HarfangLab EDR has raised an alert based on its hlai engine
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "HarfangLab EDR Low Level Rule Detection"
    
    HarfangLab EDR has raised an alert based on a low level rule (not using hlai engine)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/05/2024 - minor - Added filter to exclude threat dataset
            
??? abstract "HarfangLab EDR Low Threat"
    
    HarfangLab EDR detected a threat with a low level. This detection by the EDR is based on several detection rules.
    
    - **Effort:** master
    
??? abstract "HarfangLab EDR Medium Level Rule Detection"
    
    HarfangLab EDR has raised an alert based on a medium level rule (not using hlai engine)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/05/2024 - minor - Added filter to exclude threat dataset
            
??? abstract "HarfangLab EDR Medium Threat"
    
    HarfangLab EDR detected a threat with a medium level. This detection by the EDR is based on several detection rules.
    
    - **Effort:** master
    
??? abstract "HarfangLab EDR Process Execution Blocked (HL-AI engine)"
    
    HarfangLab EDR's machine learning malware detection module (HL-AI) has detected a suspicious binary and blocked its execution. To know more on what caused this alert, you should check the value of the process name and the concerned computer and user.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/01/2024 - major - Account for all blocks instead of only "Startup blocked". Rule name explicitly mentions HL-AI engine.
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "HarfangLab EDR Suspicious Process Behavior Has Been Detected"
    
    HarfangLab EDR has detected a suspicious process behavior based on its detection rule. Check the rule name and description for more information.
    
    - **Effort:** master
    
??? abstract "ISO LNK Infection Chain"
    
    Detection of an ISO (or any other similar archive file) downloaded file, followed by a child-process of explorer, which is characteristic of an infection using an ISO containing an LNK file. For events with `host.name`.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 25/11/2024 - minor - Updating filter on file change and deletion
        - 18/11/2024 - minor - Updating filter on file change and deletion
        - 09/10/2024 - minor - File paths added to filter some false positives.
        - 20/09/2024 - minor - File paths added to filter some false positives.
        - 19/09/2024 - minor - File paths added to filter some false positives.
        - 18/09/2023 - minor - File paths added to filter some false positives.
        - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe
            
??? abstract "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary
    
??? abstract "Lacework Cloud Security Critical Severity Alert"
    
    Detects when a critical alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security High Severity Alert"
    
    Detects when a high alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security Low Severity Alert"
    
    Detects when a low alert severity is raised by Lacework. This severity level might indicates a change in configuration that could be malicious or not.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security Medium Severity Alert"
    
    Detects when a medium alert severity is raised by Lacework. This severity level might indicates a suspicious activity such as new source from user connection.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force Successful On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Login Failed Brute-Force On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "MS Office Product Spawning Exe in User Dir"
    
    Detects an executable in the users directory started from Microsoft Word, Excel, Powerpoint, Publisher or Visio. This is a common technique used by attackers with documents embedding macros. It requires Windows command line logging events.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/08/2023 - minor - Rule modified and filter added to reduce false positives.
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Malspam Execution Registering Malicious DLL"
    
    Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).
    
    - **Effort:** elementary
    
??? abstract "Malware Detected By Vade For M365"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message.
    
    - **Effort:** master
    
??? abstract "Malware Detected By Vade For M365 And Not Blocked"
    
    Vade Secure product Vade for M365 has detected a malware contained in the message and didn't delete it.
    
    - **Effort:** advanced
    
??? abstract "Malware Outbreak"
    
    Spots a peak of malware detection by windows defender on this perimeter.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft 365 (Office 365) Anti-Phishing Policy Deletion"
    
    Detects when the anti-phishing policy is removed from Microsoft 365 (Office 365). By default, Microsoft 365 (Office 365) includes built-in features that help protect users from phishing attacks. This policy specifies the phishing protections to enable or disable, and the actions to apply options.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Anti-Phishing Rule Deletion"
    
    Detects the deactivation of the anti-phishing rule from Microsoft 365 (Office 365). The anti-phishing rule specifies the priority and recipient filters (who the policy applies to) for an anti-phish policy.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) AtpDetection"
    
    Detects when an AtpDetection (Advanced Threat Protection) event from the Office365 ThreatIntelligence service is raised. AtpDetection is a service which secures emails, attachments, and files by scanning them for threats.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) DLP Policy Removed"
    
    Detects when a DLP (Data Loss Prevention) policy is removed in Microsoft 365 (Office 365). DLP policies defines which resources can be shared and with whom, preventing sensitive information from being leaked.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Detection Velocity"
    
    Detects when Microsoft Cloud App Security identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Inbox Hiding"
    
    Detects when Microsoft Cloud App Security identifies that a suspicious inbox rule was set on a user’s inbox. This may indicate that the user account is compromised, and that the mailbox is being used to distribute spam and malware in your organization. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS New Country"
    
    Detects when Microsoft Cloud App Security identifies a sign-in from a country where it has never connected. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Repeated Delete"
    
    Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Repeated Failed Login"
    
    Detects when Microsoft Cloud App Security identifies a large number of failed login attempts which may indicate a brute-force attempt. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MCAS Risky IP"
    
    Detects when Microsoft Cloud App Security identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) MailBoxAuditBypassAssociation Option Implementation"
    
    Detects the implementation of a MailBoxAuditBypassAssociation option in Microsoft 365 (Office 365). This option is used when you configure a user or computer account to bypass mailbox audit logging, access or actions taken by the user or computer account to any mailbox isn't logged.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Filter Policy Removed"
    
    Detects when a malware policy has been deleted in Microsoft 365 (Office 365). A malware filter policy is used to alert administrators that an internal user sent a message that contained malware.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Filter Rule Deletion"
    
    Detects when a malware filter rule has been deleted in Microsoft 365 (Office 365). The malware filter rule specifies the priority and recipient filters (who the policy applies to) for a malware filter policy.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Malware Uploaded On OneDrive"
    
    Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to OneDrive. Attackers can use this method to propagate through the network.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) Malware Uploaded On SharePoint"
    
    Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to SharePoint. Attackers can use this method to propagate through the network.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 (Office 365) Mass Download By A Single User"
    
    Identifies when Microsoft Cloud App Security reports that a single user performs more than 50 downloads within 1 minute.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft 365 (Office 365) Potential Ransomware Activity Detected"
    
    Detects when Microsoft Cloud App Security reports that a user has uploaded files to the cloud that might be infected with ransomware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft 365 (Office 365) Safe Attachment Rule Disabled"
    
    Detects when the safe attachment rule has been deleted in Microsoft 365 (Office 365). Safe Attachments is a feature in Microsoft Defender for Microsoft 365 (Office 365) that opens email attachments in a special hypervisor environment to detect malicious activity.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Safelinks Disabled"
    
    Detects when a safelink rule has been deleted in Microsoft 365 (Office 365). Safe Links is a feature in Defender for Microsoft 365 (Office 365) that provides URL scanning and rewriting of inbound email messages in mail flow, and time-of-click verification of URLs and links in email messages and other locations.
    
    - **Effort:** master
    
??? abstract "Microsoft 365 (Office 365) Unusual Volume Of File Deletion"
    
    Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/10/2023 - major - Fix field names to match the current parser.
            
??? abstract "Microsoft Defender Antivirus Threat Detected"
    
    Detection of a windows defender alert indicating the presence of potential malware
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender XDR Alert"
    
    Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Cloud App Security Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Endpoint Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender XDR Office 365 Alert"
    
    Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Microsoft Office Creating Suspicious File"
    
    Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.
    
    - **Effort:** master
    
??? abstract "Microsoft Office Product Spawning Windows Shell"
    
    Detects a Windows command or scripting interpreter executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 23/01/2024 - minor - Adding elements to increase detection and filters to reduce false positives.
        - 13/09/2024 - major - Adding filters to reduce false positives and updated the effort level to master as it is a rule highly dependent on the environment.
            
??? abstract "Microsoft Office Spawning Script"
    
    Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 
    
    - **Effort:** intermediate
    
??? abstract "Okta Security Threat Detected"
    
    Detects when a security threat is detected in Okta.
    
    - **Effort:** intermediate
    
??? abstract "Palo Alto Cortex XDR (EDR) Alert Not Blocked (High Severity)"
    
    A Palo Alto Cortex XDR (EDR) agent has raised an alert of high severity that was not blocked.
    
    - **Effort:** master
    
??? abstract "Palo Alto Cortex XDR (EDR) Alert Not Blocked (Low Severity)"
    
    A Palo Alto Cortex XDR (EDR) agent has raised an alert of low severity that was not blocked.
    
    - **Effort:** master
    
??? abstract "Palo Alto Cortex XDR (EDR) Alert Not Blocked (Medium Severity)"
    
    A Palo Alto Cortex XDR (EDR) agent has raised an alert of medium severity that was not blocked.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR Agent Disabled"
    
    A SentinelOne EDR agent has been disabled according to SentinelOne logs.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR Custom Rule Alert"
    
    A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively"
    
    A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Not Mitigated"
    
    A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR SSO User Added"
    
    A SSO User was added.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Malicious)"
    
    A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Suspicious)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Kill Success"
    
    A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Failed"
    
    A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Success"
    
    A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Remediate Success"
    
    A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR User Failed To Log In To The Management Console"
    
    A user has failed to log in to the management console.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR User Logged In To The Management Console"
    
    A user has logged in to the management console.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
            
??? abstract "Sophos EDR Application Blocked"
    
    Sophos EDR detected a potentially malicious application and blocked it.
    
    - **Effort:** master
    
??? abstract "Sophos EDR Application Detected"
    
    Sophos EDR detected a potentially malicious application.
    
    - **Effort:** master
    
??? abstract "Sophos EDR CorePUA Clean"
    
    Sophos EDR detected a potentially unwanted application and cleaned it.
    
    - **Effort:** master
    
??? abstract "Sophos EDR CorePUA Detection"
    
    Sophos EDR detected a potentially unwanted application.
    
    - **Effort:** master
    
??? abstract "SquirrelWaffle Malspam Execution Loading DLL"
    
    Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.
    
    - **Effort:** intermediate
    
??? abstract "Stormshield Ses Critical Block"
    
    Stormshield Endpoint Security block execution with critical severity
    
    - **Effort:** master
    
??? abstract "Stormshield Ses Critical Not Block"
    
    Stormshield Endpoint Security detect threat with critical severity that was not blocked
    
    - **Effort:** master
    
??? abstract "Stormshield Ses Emergency Block"
    
    Stormshield Endpoint Security block execution with emergency severity
    
    - **Effort:** master
    
??? abstract "Suspicious DLL Loaded Via Office Applications"
    
    Detects suspicious DLL being loaded by an Microsoft Office Product. Considered as suspects are some .NET DLLs, clr.dll, GAC DLL, DSParse (Active Directoryi services API) or Kerberos DLLs which may be loaded by MS Office processes when executing a potentially malicious macro. The prerequisite is to log the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
??? abstract "Suspicious Outlook Child Process"
    
    Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.
    
    - **Effort:** intermediate
    
??? abstract "Sysmon Windows File Block Executable"
    
    Sysmon has blocked an executable file from being written to the disk. This could be a malicious binary to investigate.  
    
    - **Effort:** master
    
??? abstract "TEHTRIS EDR Alert"
    
    Tehtris EDR telemetry has raised an alert.
    
    - **Effort:** master
    
??? abstract "Trend Micro Apex One Data Loss Prevention Alert"
    
    Trend Micro Apex One has raised an alert for data loss prevention.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trend Micro Apex One Malware Alert"
    
    Trend Micro Apex One has detected a malware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Vectra General Threat Detection"
    
    Vectra Cognito detected a potential threat. This is a very generic rule to raise as much alerts as possible from Vectra detections however RECONNAISSANCE and INFO categories have been removed to avoid spamming.
    
    - **Effort:** master
    
??? abstract "Winword Document Droppers"
    
    Detects specific process characteristics of word document droppers. This techniques has been used by Maze ransomware operators.
    
    - **Effort:** elementary
    
??? abstract "WithSecure Elements Critical Severity"
    
    WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "WithSecure Elements Warning Severity"
    
    Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).
    
    - **Effort:** master
    
??? abstract "ZIP LNK Infection Chain"
    
    Detection of an ZIP download followed by a child-process of explorer, followed by multiple Windows processes.This is widely used as an infection chain mechanism.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 18/11/2024 - minor - Filter modified to avoid some false positives.
        - 19/09/2024 - minor - File paths added to filter some false positives.
            
??? abstract "Zscaler ZIA Malicious Threat"
    
    Zscaler Internet Access has detected a network traffic as malicious
    
    - **Effort:** master
    
??? abstract "Zscaler ZIA Malicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
??? abstract "Zscaler ZIA Suspicious Threat"
    
    Zscaler Internet Access has detected a network traffic as malicious
    
    - **Effort:** master
    
??? abstract "Zscaler ZIA Suspicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
**System Services**

??? abstract "Check Point Harmony Mobile Application Forbidden"
    
    Detects when someone attempts to access/use a forbidden application.
    
    - **Effort:** master
    
??? abstract "Correlation Impacket Smbexec"
    
    This rule detects the execution of smbexec via the relevant share pattern name 
    
    - **Effort:** elementary
    
??? abstract "Credential Dumping Tools Service Execution"
    
    Detects well-known credential dumping tools execution via service execution
    
    - **Effort:** intermediate
    
??? abstract "CrowdStrike Falcon Identity Protection Detection Critical Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection High Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Informational Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Low Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Identity Protection Detection Medium Severity"
    
    CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Critical Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection High Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Informational Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Low Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "CrowdStrike Falcon Intrusion Detection Medium Severity"
    
    CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Csrss Child Found"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Csrss Wrong Parent"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Cybereason EDR Alert"
    
    Cybereason EDR telemetry has raised an alert
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Cybereason EDR Malware Detection"
    
    Cybereason EDR telemetry has detected a malware
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Dllhost Wrong Parent"
    
    Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.
            
??? abstract "Exfiltration Via Pscp"
    
    Detects the use of pscp which is a file sharing services.
    
    - **Effort:** advanced
    
??? abstract "Gpscript Suspicious Parent"
    
    Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
            
??? abstract "Login Brute-Force Successful On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Login Failed Brute-Force On SentinelOne EDR Management Console"
    
    A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Logonui Wrong Parent"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 07/06/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Lsass Wrong Parent"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.
            
??? abstract "Malicious Service Installations"
    
    Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Malware Outbreak"
    
    Spots a peak of malware detection by windows defender on this perimeter.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Metasploit PSExec Service Creation"
    
    Detects Metasploit service creation when using the PSExec module. The ImagePath here is usually a malicious command line using powershell.exe and/or cmd.exe.
    
    - **Effort:** advanced
    
??? abstract "Microsoft Defender Antivirus Threat Detected"
    
    Detection of a windows defender alert indicating the presence of potential malware
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender XDR Alert"
    
    Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Cloud App Security Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/09/2024 - major - Update service name value following Microsoft change
            
??? abstract "Microsoft Defender XDR Endpoint Alert"
    
    Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender XDR Office 365 Alert"
    
    Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.
    
    - **Effort:** master
    
??? abstract "Okta Security Threat Detected"
    
    Detects when a security threat is detected in Okta.
    
    - **Effort:** intermediate
    
??? abstract "OneNote Suspicious Children Process"
    
    In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.
            
??? abstract "PsExec Process"
    
    Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Rare Logonui Child Found"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.
    
    - **Effort:** advanced
    
??? abstract "Rare Lsass Child Found"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Searchprotocolhost Child Found"
    
    SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 12/03/2024 - minor - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "SentinelOne EDR Agent Disabled"
    
    A SentinelOne EDR agent has been disabled according to SentinelOne logs.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR Custom Rule Alert"
    
    A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively"
    
    A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Malicious Threat Not Mitigated"
    
    A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR SSO User Added"
    
    A SSO User was added.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Malicious)"
    
    A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Detected (Suspicious)"
    
    A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Kill Success"
    
    A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Failed"
    
    A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Quarantine Success"
    
    A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR Threat Mitigation Report Remediate Success"
    
    A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "SentinelOne EDR User Failed To Log In To The Management Console"
    
    A user has failed to log in to the management console.
    
    - **Effort:** master
    
??? abstract "SentinelOne EDR User Logged In To The Management Console"
    
    A user has logged in to the management console.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
            
??? abstract "Smbexec.py Service Installation"
    
    Detects the use of smbexec.py tool by detecting a specific service installation
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 05/04/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "SolarWinds Suspicious File Creation"
    
    Detects SolarWinds process creating a file with a suspicious extension. The process solarwinds.businesslayerhost.exe created an unexpected file whose extension is ".exe", ".ps1", ".jpg", ".png" or ".dll".
    
    - **Effort:** intermediate
    
??? abstract "SolarWinds Wrong Child Process"
    
    Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
        - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs
            
??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
            
??? abstract "Suspicious Commands From MS SQL Server Shell"
    
    Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious DNS Child Process"
    
    Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).
    
    - **Effort:** intermediate
    
??? abstract "Suspicious PsExec Execution"
    
    Detects execution of PsExec, different from the Sysinternals one. This rule helps to filter out the noise if PsExec is used for legit purposes or if attacker uses a different PsExec client other than Sysinternals one. The prerequisite is to log the Event ID 5145 (by setting "Audit Policy > Object Access > Audit Detailed File Share" to Success/Failure).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - minor - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 31/01/2024 - minor - Adding filters to reduce false positives
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
            
??? abstract "TEHTRIS EDR Alert"
    
    Tehtris EDR telemetry has raised an alert.
    
    - **Effort:** master
    
??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Taskhost or Taskhostw Suspicious Child Found"
    
    Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
            
??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "Trend Micro Apex One Data Loss Prevention Alert"
    
    Trend Micro Apex One has raised an alert for data loss prevention.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trend Micro Apex One Malware Alert"
    
    Trend Micro Apex One has detected a malware.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Usage Of Procdump With Common Arguments"
    
    Detects the usage of Procdump sysinternals tool with some common arguments and followed by common patterns.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/01/2024 - minor - Added filter to reduce false positives.
            
??? abstract "Usage Of Sysinternals Tools"
    
    Detects the usage of Sysinternals Tools due to accepteula key being added to Registry. The rule detects it either from the command line usage or from the regsitry events. For the later prerequisite is logging for registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "WMI Persistence Command Line Event Consumer"
    
    Detects WMI command line event consumers.
    
    - **Effort:** elementary
    
??? abstract "Windows Suspicious Service Creation"
    
    Detects the creation of a new suspicious service - attacker could use MSRPC to create a remote service
    
    - **Effort:** intermediate
    
??? abstract "Windows Update LolBins"
    
    This rule try to detect a suspicious behavior of wuauclt.exe (windows update client) that could be a lolbins. Wuauctl.exe could be used to execute a malicious program.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.
            
??? abstract "Wininit Wrong Parent"
    
    Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.
            
??? abstract "Winlogon wrong parent"
    
    Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
            
??? abstract "Winrshost Wrong Parent"
    
    Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "WithSecure Elements Critical Severity"
    
    WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "WithSecure Elements Warning Severity"
    
    Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).
    
    - **Effort:** master
    
??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 25/10/2023 - minor - Adding filter to reduce false positives.
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Zscaler ZIA Malicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
??? abstract "Zscaler ZIA Suspicious Threat Outbreak"
    
    Spots a peak of malicious threat detection by Zscaler ZIA
    
    - **Effort:** master
    
**Deploy Container**

??? abstract "Docker Escape Bind Mount"
    
    Catch Docker escape via mount escape followed by chroot 
    
    - **Effort:** intermediate
    
## Persistence
**Boot or Logon Initialization Scripts**

??? abstract "Logon Scripts (UserInitMprLogonScript)"
    
    Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.
    
    - **Effort:** advanced
    
**Scheduled Task/Job**

??? abstract "BazarLoader Persistence Using Schtasks"
    
    Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.
    
    - **Effort:** intermediate
    
??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary
    
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cron Files Alteration"
    
    Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace App Script Scheduled Task"
    
    Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.
    
    - **Effort:** advanced
    
??? abstract "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate
    
??? abstract "Remote Task Creation Via ATSVC Named Pipe"
    
    Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/03/2024 - minor - change filter to ACL hex value
            
??? abstract "STRRAT Scheduled Task"
    
    Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'
    
    - **Effort:** intermediate
    
??? abstract "Schtasks Persistence With High Privileges"
    
    Detection of scheduled task with high privileges used by attacker for persistence.
    
    - **Effort:** elementary
    
??? abstract "Schtasks Suspicious Parent"
    
    Detects schtasks started from suspicious and/or unusual processes.
    
    - **Effort:** intermediate
    
??? abstract "Spyware Persistence Using Schtasks"
    
    Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Scheduled Task Creation"
    
    Detects suspicious scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 
    
    - **Effort:** intermediate
    
??? abstract "Windows Suspicious Scheduled Task Creation"
    
    The rule identify creation of new scheduled task who run suspicious or dangerous command
    
    - **Effort:** intermediate
    
**Registry Run Keys / Startup Folder**

??? abstract "Malware Persistence Registry Key"
    
    Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs
            
**Valid Accounts**

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - add similarity strategy
            
??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - Add similarity strategy
            
??? abstract "Account Tampering - Suspicious Failed Logon Reasons"
    
    This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Admin User RDP Remote Logon"
    
    Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Authentication Impossible Travel"
    
    Detects impossible travel when performing authentication from a source IP address, grouped by username.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/07/2024 - major - review filter to avoid false positive
            
??? abstract "Broadcom Edge Secure Web Gateway High Threat"
    
    Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.
    
    - **Effort:** master
    
??? abstract "Brute-Force On Fortinet Firewall Login"
    
    Spots many failed attempts to log on an administration interface.
    
    - **Effort:** master
    
??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Minor change in selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Fortigate Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Account Suspended"
    
    Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Added"
    
    Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Authorized"
    
    Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Attack Warning"
    
    Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".
    
    - **Effort:** intermediate
    
??? abstract "Google Workspace Account Warning"
    
    Detects a suspicious login, leaked password, or account disabled following suspicious activity.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Creation"
    
    Detects when an admin is created or when his role is changed.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Adding new element to increase detection.
            
??? abstract "Google Workspace Suspicious Login"
    
    Detects a suspicious login reported by google.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force On Firewall"
    
    Detects successful access to administration console of a firewall after several failure.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force On FreeRadius"
    
    A user has attempted to login several times (brute-force) with error then one success.
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force On Sekoia.io"
    
    Detects successful access to Sekoia.io after several failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "Microsoft 365 Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)
    
    - **Effort:** master
    
??? abstract "Netskope Admin Audit"
    
    Audit events for admin activites, from Logins to policies' changes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "Okta Many Passwords Reset Attempt"
    
    This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.
    
    - **Effort:** advanced
    
??? abstract "Okta Suspicious Activity Reported"
    
    Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.
    
    - **Effort:** advanced
    
??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** master
    
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
**Account Manipulation**

??? abstract "AWS CloudTrail IAM Failed User Creation"
    
    Detects an attemp to create a user account where the result is an explicit denied.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Password Policy Updated"
    
    Detects an update to the password policy. This could be an attempt to lower accounts security level.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Policy Changed"
    
    Detects change on AWS IAM Policy
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail Root ConsoleLogin"
    
    Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Attempt"
    
    Detects when a request in success or failure is made to transfer a domain name to an other AWS account
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Lock Disabled"
    
    Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.
    
    - **Effort:** elementary
    
??? abstract "Active Directory Delegate To KRBTGT Service"
    
    Detects potential persistence installation from an already compromised administrator domain account. The attacker will create a TGT and abuse a service account with the constrained delegation and update it with the krbtgt service. The detection relies on the Event ID 4738.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory Replication User Backdoor"
    
    Backdooring domain object to grant the rights associated with DCSync to regular user or machine account, this technics is often used to give ResetPassword or WriteMembers or DCSync permission(s) for persistency on a domain.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/10/2024 - major - Update pattern to avoid false positives and change rule effort
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory User Backdoors"
    
    Detects scenarios where the attacker controls another user or computer account without having to use their credentials.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Add User to Privileged Group"
    
    Add user in a potential privileged group which can be used to elevate privileges on the system.
    
    - **Effort:** advanced
    
??? abstract "Enabling Restricted Admin Mode"
    
    Detects when the restricted admin mode is enabled.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Modification"
    
    Detects when an admin is modified.
    
    - **Effort:** master
    
??? abstract "Google Workspace Domain Delegation"
    
    Detects when a domain delegation is granted.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure"
    
    Detects self-service password reset in failure for various reasons (except licence or policy ones)
    
    - **Effort:** master
    
??? abstract "Mimikatz Basic Commands"
    
    Detects Mimikatz most popular commands. 
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
            
??? abstract "Okta Admin Privilege Granted"
    
    Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.
    
    - **Effort:** advanced
    
??? abstract "Okta Application deleted"
    
    An application has been delete on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta Application modified"
    
    An application has been updated on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta User Account Deactivated"
    
    A user account has been deactivated in Okta.
    
    - **Effort:** master
    
??? abstract "Okta User Impersonation Access"
    
    A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.
    
    - **Effort:** advanced
    
??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/07/2023 - minor - Added AD groups and change to effort master.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "SSH Authorized Key Alteration"
    
    The file authorized_keys is used by SSH server to identify SSH keys that are authorized to connect to the host, alteration of one of those files might indicate a user compromision.
    
    - **Effort:** advanced
    
??? abstract "SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory"
    
    Detects the SeEnableDelegationPrivilege right in Active Directory granted to a user of a computer, it would allow control of other AD user objects
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Varonis Many Accounts Disabled"
    
    This rule identifies a high number of account disabled.
    
    - **Effort:** master
    
**Web Shell**

??? abstract "Antivirus Web Shell Detection"
    
    Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
**Component Object Model Hijacking**

??? abstract "Windows Registry Persistence COM Key Linking"
    
    Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 14/12/2023 - minor - Exclude common legitimate processes
            
**Authentication Package**

??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
**External Remote Services**

??? abstract "Anomaly New PowerShell Remote Session"
    
    Detects when PowerShell remote sessions are created in a short amount of time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/06/2024 - minor - Adding fields to be displayed in the alert.
            
??? abstract "Datadome Protection Intrusion Detection"
    
    Detects when Datadome protection raises an alert linked to intrusion. Datadome is used against fraud and bots.
    
    - **Effort:** master
    
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "SecurityScorecard Vulnerability Assessment Scanner New Issues"
    
    Raises an alert when SecurityScorecard Vulnerability Assessment Scanner find new issues.
    
    - **Effort:** master
    
??? abstract "Trend Micro Apex One Intrusion Detection Alert"
    
    Trend Micro Apex One has raised an alert for an intrusion detection.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Trend Micro Cloud One High Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a high severity level.
    
    - **Effort:** master
    
??? abstract "Trend Micro Cloud One Low Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a low severity level.
    
    - **Effort:** master
    
??? abstract "Trend Micro Cloud One Medium Intrusion"
    
    Detects when Trend Micro EDR raised an alert for an intrusion with a medium severity level.
    
    - **Effort:** master
    
**Create Account**

??? abstract "AWS Persistence By Creating KeyPair And SecurityGroup"
    
    Attackers can use AWS credentials to create a KeyPair and a SecurityGroup to have continuous access to the AWS account.
    
    - **Effort:** master
    
??? abstract "CVE-2021-20021 SonicWall Unauthenticated Administrator Access"
    
    Detects the exploitation of SonicWall Unauthenticated Admin Access.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace User Creation"
    
    Detects when a new user is created.
    
    - **Effort:** master
    
??? abstract "Impacket Addcomputer"
    
    Detects suspicious computer account creation based on impacket default pattern
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 05/08/2024 - major - improve selection to extend detection
            
??? abstract "Net.exe User Account Creation"
    
    Identifies creation of local users via the net.exe command
    
    - **Effort:** master
    
??? abstract "Okta User Account Created"
    
    A user account has been created in Okta.
    
    - **Effort:** master
    
??? abstract "Suspicious URL Requested By Curl Or Wget Commands"
    
    Correlation rule aiming to be multi-source to detect URL with suspicious files extensions (seen on a network level by proxies or firewalls) being requested by curl or wget processes (seen on a host level).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 23/09/2024 - major - Fixed an issue with the detection pattern.
            
??? abstract "Suspicious Windows ANONYMOUS LOGON Local Account Created"
    
    Detects the creation of suspicious accounts simliar to ANONYMOUS LOGON, such as using additional spaces. Created as a covering detection for attackers trying to created an ANONYMOUS LOGON account as it is an account named used in internal Windows events and frequently filtered by attackers.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "User Account Created"
    
    Detects user creation on windows servers, which shouldn't happen in an Active Directory environment. Apply this on your windows server logs and not on your DC logs. One default account `defaultuser0` is excluded as only used during Windows set-up. This detection use Security Event ID 4720. 
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
        - 10/07/2024 - minor - Adding filter and new elements to reduce false positives.
        - 12/07/2024 - minor - Changing similarity strategy.
            
**Office Application Startup**

??? abstract "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary
    
??? abstract "Microsoft Office Startup Add-In"
    
    Detects add-ins that load when Microsoft Word or Excel starts (.wll/.xll are simply .dll fit for Word or Excel). The rule requires File Creation logging to work, which can be done using Sysmon Event ID 11.
    
    - **Effort:** elementary
    
??? abstract "Office Application Startup Office Test"
    
    Detects the addition of office test registry that allows a user to specify an arbitrary DLL that will be executed everytime an Office application is started. An adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system.
    
    - **Effort:** elementary
    
**Browser Extensions**

??? abstract "Malicious Browser Extensions"
    
    Detects browser extensions being loaded with the --load-extension and -base-url options, which works on Chromium-based browsers. We are looking for potentially malicious browser extensions. These extensions can get access to informations.
    
    - **Effort:** advanced
    
**BITS Jobs**

??? abstract "BITSAdmin Download"
    
    Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 06/12/2023 - minor - Adding key words to increase detection.
            
**Traffic Signaling**

??? abstract "Binary List Tcp"
    
    A binary is trying to list TCP connections. The prerequisites are to enable monitoring of the open and openat syscalls using Auditbeat.
    
    - **Effort:** advanced
    
**Server Software Component**

??? abstract "Antivirus Web Shell Detection"
    
    Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
??? abstract "CVE-2021-34473 ProxyShell Attempt"
    
    Detects CVE-2021-34473 ProxyShell attempt against Microsoft Exchange Server, Remote Code Execution Vulnerability.
    
    - **Effort:** advanced
    
??? abstract "Default User www data User Compromised"
    
    User www_data by default cannot log and use a shell, any syscall of type execve induce user compromise
    
    - **Effort:** master
    
??? abstract "Exchange Server Spawning Suspicious Processes"
    
    Look for Microsoft Exchange Server’s Unified Messaging service spawning suspicious sub-processes, suggesting exploitation of CVE-2021-26857 vulnerability.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Exchange Server Creating Unusual Files"
    
    Look for Microsoft Exchange Server’s Unified Messaging service creating non-standard content on disk, which could indicate web shells or other malicious content, suggesting exploitation of CVE-2021-26858 vulnerability
    
    - **Effort:** intermediate
    
??? abstract "Microsoft IIS Module Installation"
    
    Detects the installation of a new IIS module from the command line. It can used used to backdoor an IIS/OWA/Sharepoint server.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 10/10/2024 - major - Adding new commands with powershell and changing effort level.
            
??? abstract "PowerCat Function Loading"
    
    Detect a basic execution of PowerCat. PowerCat is a PowerShell function allowing to do basic connections, file transfer, shells, relays, generate payloads.
    
    - **Effort:** intermediate
    
??? abstract "ProxyShell Microsoft Exchange Suspicious Paths"
    
    Detects suspicious calls to Microsoft Exchange resources, in locations related to webshells observed in campaigns using this vulnerability.
    
    - **Effort:** elementary
    
??? abstract "Webshell Creation"
    
    Detects possible webshell file creation. It requires File Creation monitoring, which can be done using Sysmon's Event ID 11. However the recommended SwiftOnSecurity configuration does not fully cover the needs for this rule, it needs to be updated with the proper file names extensions.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Create or Modify System Process**

??? abstract "APT29 Fake Google Update Service Install"
    
    This method detects malicious services mentioned in APT29 report by FireEye. The legitimate path for the Google update service is C:\Program Files (x86)\Google\Update\GoogleUpdate.exe so the service names and executable locations used by APT29 are specific enough to be detected in log files.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cobalt Strike Default Service Creation Usage"
    
    Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Csrss Child Found"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Csrss Wrong Parent"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Dllhost Wrong Parent"
    
    Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.
            
??? abstract "Gpscript Suspicious Parent"
    
    Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
            
??? abstract "Logonui Wrong Parent"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 07/06/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Lsass Wrong Parent"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.
            
??? abstract "Malicious Service Installations"
    
    Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "New Service Creation"
    
    Detects creation of a new service from command line
    
    - **Effort:** advanced
    
??? abstract "OneNote Suspicious Children Process"
    
    In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.
            
??? abstract "Rare Logonui Child Found"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.
    
    - **Effort:** advanced
    
??? abstract "Rare Lsass Child Found"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Searchprotocolhost Child Found"
    
    SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 12/03/2024 - minor - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 05/04/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "SolarWinds Wrong Child Process"
    
    Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
        - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs
            
??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
            
??? abstract "StoneDrill Service Install"
    
    This method detects a service install of the malicious Microsoft Network Realtime Inspection Service service described in StoneDrill report by Kaspersky 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Commands From MS SQL Server Shell"
    
    Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.
    
    - **Effort:** intermediate
    
??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - minor - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 31/01/2024 - minor - Adding filters to reduce false positives
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
            
??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Taskhost or Taskhostw Suspicious Child Found"
    
    Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
            
??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "WMI Persistence Command Line Event Consumer"
    
    Detects WMI command line event consumers.
    
    - **Effort:** elementary
    
??? abstract "Wininit Wrong Parent"
    
    Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.
            
??? abstract "Winlogon wrong parent"
    
    Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
            
??? abstract "Winrshost Wrong Parent"
    
    Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 25/10/2023 - minor - Adding filter to reduce false positives.
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
**Event Triggered Execution**

??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.
    
    - **Effort:** intermediate
    
??? abstract "Change Default File Association"
    
    When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.
    
    - **Effort:** advanced
    
??? abstract "Component Object Model Hijacking"
    
    Detects component object model hijacking. An attacker can establish persistence with COM objects.
    
    - **Effort:** advanced
    
??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced
    
??? abstract "HTML Smuggling Suspicious Usage"
    
    Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.
    
    - **Effort:** intermediate
    
??? abstract "New DLL Added To AppCertDlls Registry Key"
    
    Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys"
    
    Detects persistence registry keys. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master
    
??? abstract "Sticky Key Like Backdoor Usage"
    
    Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Suspicious Netsh DLL Persistence"
    
    Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Scripting In A WMI Consumer"
    
    Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.
    
    - **Effort:** intermediate
    
??? abstract "WMI Event Subscription"
    
    Detects creation of WMI event subscription persistence method 
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced
    
**Boot or Logon Autostart Execution**

??? abstract "Autorun Keys Modification"
    
    Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master
    
??? abstract "DLL Load via LSASS Registry Key"
    
    Detects a method to load DLL via LSASS process using an undocumented Registry key. Prerequisites are logging for Registry events. This can be done with Sysmon events 12, 13 and 14 and monitor `SYSTEM\CurrentControlSet\Services`.
    
    - **Effort:** intermediate
    
??? abstract "Kernel Module Alteration"
    
    Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. The prerequisites are to enable monitoring of the finit_module, init_module, delete_module syscalls using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Leviathan Registry Key Activity"
    
    Detects registry key used by Leviathan APT in Malaysian focused campaign.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Malware Persistence Registry Key"
    
    Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs
            
??? abstract "Narrator Feedback-Hub Persistence"
    
    The Windows 10 Narrator's Feedback-Hub registry key has been modified which could be done by an attacker for persistence purposes. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13). Careful since the SwiftOnSecurity Sysmon's configuration needs to be changed to log for this specifically.
    
    - **Effort:** master
    
??? abstract "NjRat Registry Changes"
    
    Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/11/2023 - minor - Update regex pattern to insensitive case
        - 07/06/2024 - major - Update pattern to reduce false positives
            
??? abstract "Njrat Registry Values"
    
    Detects specifis registry values that are related to njRat usage.
    
    - **Effort:** intermediate
    
??? abstract "Powershell Winlogon Helper DLL"
    
    Detects modifications to the Winlogon Registry keys, which may cause Winlogon to load and execute malicious DLLs and/or executables.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "RUN Registry Key Created From Suspicious Folder"
    
    Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** advanced
    
??? abstract "Registry Key Used By Some Old Agent Tesla Samples"
    
    Detects potential use of the RUN registry key to execute some Agent Tesla samples at boot. Prerequisites are to log for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
??? abstract "Security Support Provider (SSP) Added to LSA Configuration"
    
    Detects the addition of a SSP to the registry. This is commonly used for persistence. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows. Logging for Registry events is needed for this rule to work (this can be done through Sysmon EventIDs 12 and 13).
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Suspicious desktop.ini Action"
    
    Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 30/04/2024 - major - Adding some filters
            
??? abstract "Svchost Modification"
    
    Detects the modification of svchost in the registry.
    
    - **Effort:** advanced
    
**Modify Authentication Process**

??? abstract "1Password EPM MFA Disable"
    
    Detects when the MFA for 1Password is disabled.
    
    - **Effort:** master
    
??? abstract "Active Directory Shadow Credentials"
    
    Detects alternative credentials material adding. Attackers can abuse msDS-KeyCredentialLink and create a key pair to obtain a persistent and stealthy access to the target user or computer.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace MFA changed"
    
    Detects when the settings for the MFA are modified.
    
    - **Effort:** master
    
??? abstract "Google Workspace Password Change"
    
    Detects when a password is changed. An attacker can perform this action to impact the availability of the account.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/06/2024 - minor - Adding new element to increase detection.
            
??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) MFA Method Change"
    
    This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.
    
    - **Effort:** master
    
**Hijack Execution Flow**

??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate
    
??? abstract "DHCP Server Error Failed Loading the CallOut DLL"
    
    This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DHCP Server Loaded the CallOut DLL"
    
    This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS Server Error Failed Loading The ServerLevelPluginDLL"
    
    This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/07/2024 - minor - Added filter to reduce false positvives
            
??? abstract "Elevated Shell Launched By Browser"
    
    Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.
    
    - **Effort:** master
    
??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate
    
??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate
    
??? abstract "Linux Shared Lib Injection Via Ldso Preload"
    
    Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process
    
    - **Effort:** intermediate
    
??? abstract "Suspicious DLL side loading from ProgramData"
    
    Detects suspicious DLL side-loading from C:\ProgramData where the DLL is not signed.
    
    - **Effort:** intermediate
    
??? abstract "Svchost DLL Search Order Hijack"
    
    Detects svchost process hijacking through DLL loading. IKEEXT and SessionEnv service, as they call LoadLibrary on files that do not exist within C:\Windows\System32\ by default. An attacker can place their malicious logic within the PROCESS_ATTACH block of their library and restart the aforementioned services "svchost.exe -k netsvcs" to gain code execution on a remote machine.
    
    - **Effort:** master
    
??? abstract "Werfault DLL Injection"
    
    Werfault DLL search order look first in the current file, which lets an attacker use th legitimate exe to run its own DLL.  
    
    - **Effort:** intermediate
    
??? abstract "Windows Registry Persistence COM Search Order Hijacking"
    
    Detects potential COM object hijacking leveraging the COM Search Order. Logging for Registry events is needed, it can be done with Sysmon's Event IDs 12 and 13.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 11/01/2024 - minor - Adding filtering for some FPs
            
## Privilege Execution
**Boot or Logon Initialization Scripts**

??? abstract "Logon Scripts (UserInitMprLogonScript)"
    
    Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.
    
    - **Effort:** advanced
    
**Scheduled Task/Job**

??? abstract "BazarLoader Persistence Using Schtasks"
    
    Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.
    
    - **Effort:** intermediate
    
??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary
    
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cron Files Alteration"
    
    Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace App Script Scheduled Task"
    
    Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.
    
    - **Effort:** advanced
    
??? abstract "Qakbot Persistence Using Schtasks"
    
    Detects possible Qakbot persistence using schtasks.
    
    - **Effort:** intermediate
    
??? abstract "Remote Task Creation Via ATSVC Named Pipe"
    
    Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/03/2024 - minor - change filter to ACL hex value
            
??? abstract "STRRAT Scheduled Task"
    
    Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'
    
    - **Effort:** intermediate
    
??? abstract "Schtasks Persistence With High Privileges"
    
    Detection of scheduled task with high privileges used by attacker for persistence.
    
    - **Effort:** elementary
    
??? abstract "Schtasks Suspicious Parent"
    
    Detects schtasks started from suspicious and/or unusual processes.
    
    - **Effort:** intermediate
    
??? abstract "Spyware Persistence Using Schtasks"
    
    Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Scheduled Task Creation"
    
    Detects suspicious scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 
    
    - **Effort:** intermediate
    
??? abstract "Windows Suspicious Scheduled Task Creation"
    
    The rule identify creation of new scheduled task who run suspicious or dangerous command
    
    - **Effort:** intermediate
    
**Process Injection**

??? abstract "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate
    
??? abstract "Cobalt Strike Named Pipes"
    
    Detects the pipes established by Cobalt Strike to allow a communication between its beacons.
    
    - **Effort:** master
    
??? abstract "CreateRemoteThread Common Process Injection"
    
    Detects a possible process injection through CreateRemoteThread() which is spotted by EventID 8 from Sysmon and several EDRs. This rule has a list of process commonly being injected by the attackers that should be updated regularly.
    
    - **Effort:** advanced
    
??? abstract "Daspren Parad Malicious Behavior"
    
    Detects when Daspren Parad kills a process with a malicious behavior.
    
    - **Effort:** master
    
??? abstract "Dynwrapx Module Loading"
    
    Detects the loading of DynamicWrapperX (Dynwrapx). It is used by some malware in their infection chain and could help to detect its usage from vbs/wscript/cscript scripts. This is based on Microsoft Windows Sysmon events (Event ID 7).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Malicious Named Pipe"
    
    Detects the creation of a named pipe used by known malware. Prerequisites are logging for PipeEvents in Sysmon config (Event ID 17 and 18).
    
    - **Effort:** intermediate
    
??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate
    
??? abstract "Process Herpaderping"
    
    Detection of process herpaderping using Sysmon Event ID 25. It detects that an image has been locked for access. Several processes have been excluded to avoid FPs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Process Hollowing Detection"
    
    Detection of process hollowing using Sysmon Event ID 25. It detects that an image has been replaced in a process memory.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 12/03/2024 - minor - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 05/04/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
            
??? abstract "Suspicious Process Requiring DLL Starts Without DLL"
    
    Detects potential process injection and hollowing on processes that usually require a DLL to be launched, but are launched without any argument. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/01/2024 - minor - Added filter to reduce false positives
            
??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - minor - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 31/01/2024 - minor - Adding filters to reduce false positives
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
            
??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 25/10/2023 - minor - Adding filter to reduce false positives.
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
**Exploitation for Privilege Escalation**

??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
??? abstract "CVE-2021-4034 Polkit's pkexec"
    
    Detection of Polkit's pkexec exploit
    
    - **Effort:** intermediate
    
??? abstract "Certify Or Certipy"
    
    Detects the use of certify and certipy which are two different tools used to enumerate and abuse Active Directory Certificate Services.
    
    - **Effort:** advanced
    
??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate
    
??? abstract "Okta Admin Privilege Granted"
    
    Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.
    
    - **Effort:** advanced
    
??? abstract "Suspicious New Printer Ports In Registry"
    
    Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
**Valid Accounts**

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - add similarity strategy
            
??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - Add similarity strategy
            
??? abstract "Account Tampering - Suspicious Failed Logon Reasons"
    
    This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Admin User RDP Remote Logon"
    
    Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Authentication Impossible Travel"
    
    Detects impossible travel when performing authentication from a source IP address, grouped by username.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/07/2024 - major - review filter to avoid false positive
            
??? abstract "Broadcom Edge Secure Web Gateway High Threat"
    
    Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.
    
    - **Effort:** master
    
??? abstract "Brute-Force On Fortinet Firewall Login"
    
    Spots many failed attempts to log on an administration interface.
    
    - **Effort:** master
    
??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Minor change in selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Fortigate Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Account Suspended"
    
    Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Added"
    
    Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Authorized"
    
    Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Attack Warning"
    
    Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".
    
    - **Effort:** intermediate
    
??? abstract "Google Workspace Account Warning"
    
    Detects a suspicious login, leaked password, or account disabled following suspicious activity.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Creation"
    
    Detects when an admin is created or when his role is changed.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Adding new element to increase detection.
            
??? abstract "Google Workspace Suspicious Login"
    
    Detects a suspicious login reported by google.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force On Firewall"
    
    Detects successful access to administration console of a firewall after several failure.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force On FreeRadius"
    
    A user has attempted to login several times (brute-force) with error then one success.
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force On Sekoia.io"
    
    Detects successful access to Sekoia.io after several failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "Microsoft 365 Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)
    
    - **Effort:** master
    
??? abstract "Netskope Admin Audit"
    
    Audit events for admin activites, from Logins to policies' changes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "Okta Many Passwords Reset Attempt"
    
    This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.
    
    - **Effort:** advanced
    
??? abstract "Okta Suspicious Activity Reported"
    
    Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.
    
    - **Effort:** advanced
    
??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** master
    
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
**Account Manipulation**

??? abstract "AWS CloudTrail IAM Failed User Creation"
    
    Detects an attemp to create a user account where the result is an explicit denied.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Password Policy Updated"
    
    Detects an update to the password policy. This could be an attempt to lower accounts security level.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Policy Changed"
    
    Detects change on AWS IAM Policy
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail Root ConsoleLogin"
    
    Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Attempt"
    
    Detects when a request in success or failure is made to transfer a domain name to an other AWS account
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Lock Disabled"
    
    Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.
    
    - **Effort:** elementary
    
??? abstract "Active Directory Delegate To KRBTGT Service"
    
    Detects potential persistence installation from an already compromised administrator domain account. The attacker will create a TGT and abuse a service account with the constrained delegation and update it with the krbtgt service. The detection relies on the Event ID 4738.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory Replication User Backdoor"
    
    Backdooring domain object to grant the rights associated with DCSync to regular user or machine account, this technics is often used to give ResetPassword or WriteMembers or DCSync permission(s) for persistency on a domain.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/10/2024 - major - Update pattern to avoid false positives and change rule effort
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory User Backdoors"
    
    Detects scenarios where the attacker controls another user or computer account without having to use their credentials.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Add User to Privileged Group"
    
    Add user in a potential privileged group which can be used to elevate privileges on the system.
    
    - **Effort:** advanced
    
??? abstract "Enabling Restricted Admin Mode"
    
    Detects when the restricted admin mode is enabled.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Modification"
    
    Detects when an admin is modified.
    
    - **Effort:** master
    
??? abstract "Google Workspace Domain Delegation"
    
    Detects when a domain delegation is granted.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure"
    
    Detects self-service password reset in failure for various reasons (except licence or policy ones)
    
    - **Effort:** master
    
??? abstract "Mimikatz Basic Commands"
    
    Detects Mimikatz most popular commands. 
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
            
??? abstract "Okta Admin Privilege Granted"
    
    Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.
    
    - **Effort:** advanced
    
??? abstract "Okta Application deleted"
    
    An application has been delete on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta Application modified"
    
    An application has been updated on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta User Account Deactivated"
    
    A user account has been deactivated in Okta.
    
    - **Effort:** master
    
??? abstract "Okta User Impersonation Access"
    
    A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.
    
    - **Effort:** advanced
    
??? abstract "Password Change On Directory Service Restore Mode (DSRM) Account"
    
    The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/07/2023 - minor - Added AD groups and change to effort master.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "SSH Authorized Key Alteration"
    
    The file authorized_keys is used by SSH server to identify SSH keys that are authorized to connect to the host, alteration of one of those files might indicate a user compromision.
    
    - **Effort:** advanced
    
??? abstract "SeEnableDelagationPrivilege Granted To User Or Machine In Active Directory"
    
    Detects the SeEnableDelegationPrivilege right in Active Directory granted to a user of a computer, it would allow control of other AD user objects
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Varonis Many Accounts Disabled"
    
    This rule identifies a high number of account disabled.
    
    - **Effort:** master
    
**Web Shell**

??? abstract "Antivirus Web Shell Detection"
    
    Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
**Access Token Manipulation**

??? abstract "Jumpcloud Api Key Updated"
    
    An API Token has been updated on Jumplcoud portal.
    
    - **Effort:** advanced
    
??? abstract "Meterpreter or Cobalt Strike Getsystem Service Installation"
    
    Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting some of the techniques being used (technique 1,2 and 5).
    
    - **Effort:** elementary
    
??? abstract "Okta API Token created"
    
    A new API Token has been created on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta API Token revoked"
    
    A new API Token has been deleted on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Possible RottenPotato Attack"
    
    Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
**Domain or Tenant Policy Modification**

??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "ESET Protect Set Policy"
    
    Detects when a new policy is set or removed.
    
    - **Effort:** master
    
??? abstract "GPO Executable Delivery"
    
    Detects MSI binaries run through GPOs.
    
    - **Effort:** intermediate
    
??? abstract "Jumpcloud Policy Modified"
    
    Detects when a Jumpcloud policy is modified.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Domain Trust Modification"
    
    Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Confirm the added or modified target domain/URL is legitimate administrator behavior.
    
    - **Effort:** elementary
    
??? abstract "Okta Policy Modified or Deleted"
    
    Detects when an Okta policy is modified or deleted.
    
    - **Effort:** advanced
    
??? abstract "Okta Policy Rule Modified or Deleted"
    
    Detects when an Okta Policy Rule is Modified or Deleted.
    
    - **Effort:** advanced
    
??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/07/2023 - minor - Added AD groups and change to effort master.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Tenable Identity Exposure / Alsid Critical Severity Alert"
    
    Tenable Identity Exposure / Alsid raised a critical severity alert.
    
    - **Effort:** master
    
??? abstract "Tenable Identity Exposure / Alsid High Severity Alert"
    
    Tenable Identity Exposure / Alsid raised an alert.
    
    - **Effort:** master
    
**Create or Modify System Process**

??? abstract "APT29 Fake Google Update Service Install"
    
    This method detects malicious services mentioned in APT29 report by FireEye. The legitimate path for the Google update service is C:\Program Files (x86)\Google\Update\GoogleUpdate.exe so the service names and executable locations used by APT29 are specific enough to be detected in log files.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cobalt Strike Default Service Creation Usage"
    
    Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Csrss Child Found"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Csrss Wrong Parent"
    
    The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Dllhost Wrong Parent"
    
    Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.
            
??? abstract "Gpscript Suspicious Parent"
    
    Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
            
??? abstract "Logonui Wrong Parent"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 07/06/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Lsass Wrong Parent"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.
            
??? abstract "Malicious Service Installations"
    
    Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "New Service Creation"
    
    Detects creation of a new service from command line
    
    - **Effort:** advanced
    
??? abstract "OneNote Suspicious Children Process"
    
    In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.
            
??? abstract "Rare Logonui Child Found"
    
    Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.
    
    - **Effort:** advanced
    
??? abstract "Rare Lsass Child Found"
    
    Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Searchprotocolhost Child Found"
    
    SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.
    
    - **Effort:** intermediate
    
??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 12/03/2024 - minor - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 05/04/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "SolarWinds Wrong Child Process"
    
    Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
        - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs
            
??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
            
??? abstract "StoneDrill Service Install"
    
    This method detects a service install of the malicious Microsoft Network Realtime Inspection Service service described in StoneDrill report by Kaspersky 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Commands From MS SQL Server Shell"
    
    Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.
    
    - **Effort:** intermediate
    
??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - minor - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 31/01/2024 - minor - Adding filters to reduce false positives
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
            
??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Taskhost or Taskhostw Suspicious Child Found"
    
    Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
            
??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "WMI Persistence Command Line Event Consumer"
    
    Detects WMI command line event consumers.
    
    - **Effort:** elementary
    
??? abstract "Wininit Wrong Parent"
    
    Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.
            
??? abstract "Winlogon wrong parent"
    
    Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
            
??? abstract "Winrshost Wrong Parent"
    
    Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 25/10/2023 - minor - Adding filter to reduce false positives.
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
**Event Triggered Execution**

??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.
    
    - **Effort:** intermediate
    
??? abstract "Change Default File Association"
    
    When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.
    
    - **Effort:** advanced
    
??? abstract "Component Object Model Hijacking"
    
    Detects component object model hijacking. An attacker can establish persistence with COM objects.
    
    - **Effort:** advanced
    
??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced
    
??? abstract "HTML Smuggling Suspicious Usage"
    
    Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.
    
    - **Effort:** intermediate
    
??? abstract "New DLL Added To AppCertDlls Registry Key"
    
    Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys"
    
    Detects persistence registry keys. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master
    
??? abstract "Sticky Key Like Backdoor Usage"
    
    Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Suspicious Netsh DLL Persistence"
    
    Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Scripting In A WMI Consumer"
    
    Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.
    
    - **Effort:** intermediate
    
??? abstract "WMI Event Subscription"
    
    Detects creation of WMI event subscription persistence method 
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "WMI Persistence Script Event Consumer File Write"
    
    Detects file writes through WMI script event consumer.
    
    - **Effort:** advanced
    
**Boot or Logon Autostart Execution**

??? abstract "Autorun Keys Modification"
    
    Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** master
    
??? abstract "DLL Load via LSASS Registry Key"
    
    Detects a method to load DLL via LSASS process using an undocumented Registry key. Prerequisites are logging for Registry events. This can be done with Sysmon events 12, 13 and 14 and monitor `SYSTEM\CurrentControlSet\Services`.
    
    - **Effort:** intermediate
    
??? abstract "Kernel Module Alteration"
    
    Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. The prerequisites are to enable monitoring of the finit_module, init_module, delete_module syscalls using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Leviathan Registry Key Activity"
    
    Detects registry key used by Leviathan APT in Malaysian focused campaign.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Malware Persistence Registry Key"
    
    Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs
            
??? abstract "Narrator Feedback-Hub Persistence"
    
    The Windows 10 Narrator's Feedback-Hub registry key has been modified which could be done by an attacker for persistence purposes. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13). Careful since the SwiftOnSecurity Sysmon's configuration needs to be changed to log for this specifically.
    
    - **Effort:** master
    
??? abstract "NjRat Registry Changes"
    
    Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/11/2023 - minor - Update regex pattern to insensitive case
        - 07/06/2024 - major - Update pattern to reduce false positives
            
??? abstract "Njrat Registry Values"
    
    Detects specifis registry values that are related to njRat usage.
    
    - **Effort:** intermediate
    
??? abstract "Powershell Winlogon Helper DLL"
    
    Detects modifications to the Winlogon Registry keys, which may cause Winlogon to load and execute malicious DLLs and/or executables.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "RUN Registry Key Created From Suspicious Folder"
    
    Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).
    
    - **Effort:** advanced
    
??? abstract "Registry Key Used By Some Old Agent Tesla Samples"
    
    Detects potential use of the RUN registry key to execute some Agent Tesla samples at boot. Prerequisites are to log for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
??? abstract "Security Support Provider (SSP) Added to LSA Configuration"
    
    Detects the addition of a SSP to the registry. This is commonly used for persistence. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows. Logging for Registry events is needed for this rule to work (this can be done through Sysmon EventIDs 12 and 13).
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Suspicious desktop.ini Action"
    
    Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 30/04/2024 - major - Adding some filters
            
??? abstract "Svchost Modification"
    
    Detects the modification of svchost in the registry.
    
    - **Effort:** advanced
    
**Abuse Elevation Control Mechanism**

??? abstract "CMSTP UAC Bypass via COM Object Access"
    
    Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 28/05/2024 - minor - Add pattern to filter to improve coverage
            
??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.
    
    - **Effort:** intermediate
    
??? abstract "Citrix NetScaler (ADC) Actions Blocked"
    
    This rule aims to detect a large amount of actions blocked performed from the same source.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace Bypass 2FA"
    
    Detects when user tries to bypass the 2FA.
    
    - **Effort:** master
    
??? abstract "HTML Smuggling Suspicious Usage"
    
    Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.
    
    - **Effort:** intermediate
    
??? abstract "Linux Capabilities Discovery"
    
    Linux capabilities are special attributes in the Linux kernel that grant processes and binary executables specific privileges that are normally reserved for processes whose effective user ID is 0 (The root user, and only the root user, has UID 0). This rule aims to detect discovery of such capabilities on the Linux system. The prerequisites are to enable monitoring of the execve and getxattr syscalls using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "Okta User Impersonation Access"
    
    A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.
    
    - **Effort:** advanced
    
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Setuid Or Setgid Usage"
    
    Detects the usage of a setuid or a setgid. The prerequisites are to enable monitoring of the setuid and setgid syscalls using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
??? abstract "UAC Bypass Using Fodhelper"
    
    Detects UAC bypass method using Fodhelper after setting the proper registry key, used in particular by Agent Tesla (RAT) or more recently by Earth Luscas. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "UAC Bypass Via Sdclt"
    
    Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)
    
    - **Effort:** elementary
    
??? abstract "UAC Bypass via Event Viewer"
    
    Detects UAC bypass method using Windows event viewer. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Improve filter to reduce false positives and clarified the rule pattern.
        - 21/09/2023 - minor - Improve filter to reduce false positives
            
??? abstract "Unusual Process Executed in Temporary Directory"
    
    Identifies processes running in a temporary folder. This is sometimes done by adversaries to hide malware. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.
    
    - **Effort:** master
    
**Hijack Execution Flow**

??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate
    
??? abstract "DHCP Server Error Failed Loading the CallOut DLL"
    
    This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DHCP Server Loaded the CallOut DLL"
    
    This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS Server Error Failed Loading The ServerLevelPluginDLL"
    
    This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/07/2024 - minor - Added filter to reduce false positvives
            
??? abstract "Elevated Shell Launched By Browser"
    
    Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.
    
    - **Effort:** master
    
??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate
    
??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate
    
??? abstract "Linux Shared Lib Injection Via Ldso Preload"
    
    Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process
    
    - **Effort:** intermediate
    
??? abstract "Suspicious DLL side loading from ProgramData"
    
    Detects suspicious DLL side-loading from C:\ProgramData where the DLL is not signed.
    
    - **Effort:** intermediate
    
??? abstract "Svchost DLL Search Order Hijack"
    
    Detects svchost process hijacking through DLL loading. IKEEXT and SessionEnv service, as they call LoadLibrary on files that do not exist within C:\Windows\System32\ by default. An attacker can place their malicious logic within the PROCESS_ATTACH block of their library and restart the aforementioned services "svchost.exe -k netsvcs" to gain code execution on a remote machine.
    
    - **Effort:** master
    
??? abstract "Werfault DLL Injection"
    
    Werfault DLL search order look first in the current file, which lets an attacker use th legitimate exe to run its own DLL.  
    
    - **Effort:** intermediate
    
??? abstract "Windows Registry Persistence COM Search Order Hijacking"
    
    Detects potential COM object hijacking leveraging the COM Search Order. Logging for Registry events is needed, it can be done with Sysmon's Event IDs 12 and 13.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 11/01/2024 - minor - Adding filtering for some FPs
            
**Escape to Host**

??? abstract "Docker Escape Bind Mount"
    
    Catch Docker escape via mount escape followed by chroot 
    
    - **Effort:** intermediate
    
## Defense Evasion
**Obfuscated Files or Information**

??? abstract "OneNote Embedded File"
    
    Detects creation or uses of OneNote embedded files with unusual extensions.  
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 20/02/2023 - minor - Adding the .chm and .wsf file extensions for a file opened from a OneNote.
        - 09/02/2023 - minor - Adding other suspicious file extensions (.cmd, .img, .iso, .msi, .vhd, .vhdx) for file opened from a OneNote.
            
??? abstract "PowerShell EncodedCommand"
    
    Detects popular file extensions in commands obfuscated in base64 run through the EncodedCommand option.
    
    - **Effort:** advanced
    
??? abstract "PowerShell Invoke-Obfuscation Obfuscated IEX Invocation"
    
    Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-Obfuscation framework
    
    - **Effort:** advanced
    
??? abstract "Secure Deletion With SDelete"
    
    Detects renaming of file while deletion with SDelete tool. SDelete is a tool that permits to securely delete files by overwriting them (no recovery possible). Few threat actors are using it to delete traces of their malware.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious XOR Encoded PowerShell Command Line"
    
    Detects suspicious powershell process which includes bxor command, alternative obfuscation  method to b64 encoded commands.
    
    - **Effort:** advanced
    
**Masquerading**

??? abstract "AutoIt3 Execution From Suspicious Folder"
    
    Detects AutoIt3 execution from an unusual/suspicious folder. Legitimate folders are "Program Files" and "AppData\\Local". AutoIt3.exe is a legitimate process used to execute AutoIt program files, which are used by legitimate software, custom scripts, but also malware. Finding AutoIt3 execution from unusual/suspicious folder can help detect malware activities, such as DarkGate execution. The detection rule can be tailored to your environment and your use of AutoIt3 by filtering out folder's execution of legitimate applications or scripts.
    
    - **Effort:** advanced
    
??? abstract "Copy Of Legitimate System32 Executable"
    
    A script has copied a System32 executable.
    
    - **Effort:** intermediate
    
??? abstract "Execution From Suspicious Folder"
    
    Detects a suspicious execution from an uncommon folder
    
    - **Effort:** master
    
??? abstract "Exploit For CVE-2017-0261 Or CVE-2017-0262"
    
    Detects Winword starting uncommon sub process FLTLDR.exe as used in exploits for CVE-2017-0261 and CVE-2017-0262 through command line or PowerShell script. This is a very basic detection method relying on the rare usage of EPS files from Winword.
    
    - **Effort:** advanced
    
??? abstract "Formbook Hijacked Process Command"
    
    Detects process hijacked by Formbook malware which executes specific commands to delete the dropper or copy browser credentials to the database before sending them to the C2.
    
    - **Effort:** intermediate
    
??? abstract "Legitimate Process Execution From Unusual Folder"
    
    Detects the execution of a legitimate, windows built-in process name from an unusual / suspicious folder. Legitimate folders are c:\windows\system32\, \SystemRoot\system32\, c:\windows\syswow64\ and c:\windows\winsxs\. Many malwares/attackers use legitimate names to masquerade but if they are not Administrator yet, they often can't write file into these legitimate folders.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/01/2024 - minor - Extending filter to avoid FPs
        - 04/01/2024 - major - Rework filter selection with contains instead of re modifier
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Linux Binary Masquerading"
    
    Attackers could rename legitimate system bin to evade security mechanisme. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 12/12/2023 - minor - extend regex to macth more cases
            
??? abstract "New Or Renamed User Account With '$' In Attribute 'SamAccountName'"
    
    Detects possible bypass EDR and SIEM via abnormal user account name.
    
    - **Effort:** intermediate
    
??? abstract "Non-Legitimate Executable Using AcceptEula Parameter"
    
    Detects accepteula in command line with non-legitimate executable name. Some attackers are masquerading SysInternals tools with decoy names to prevent detection.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 19/02/2024 - minor - Update filter and effort level according to the observed hits for the rule.
            
??? abstract "Phorpiex Process Masquerading"
    
    Detects specific process executable path used by the Phorpiex botnet to masquerade its system process network activity. It looks for a pattern of a system process executable name that is not legitimate and running from a folder that is created via a random algorithm 13-15 numbers long.
    
    - **Effort:** elementary
    
??? abstract "Possible Malicious File Double Extension"
    
    Detects request to potential malicious file with double extension
    
    - **Effort:** elementary
    
??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary
    
??? abstract "Suspicious Cmd File Copy Command To Network Share"
    
    Copy suspicious files through Windows cmd prompt to network share
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Cmd.exe Command Line"
    
    Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
        - 22/11/2024 - major - Adding new elements for detection and filters.
        - 27/11/2024 - minor - Adding new filters to reduce false positives.
            
??? abstract "Unsigned Driver Loaded From Suspicious Location"
    
    Detects when a driver is unsigned and loaded from a suspicious directory.
    
    - **Effort:** advanced
    
**Process Injection**

??? abstract "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate
    
??? abstract "Cobalt Strike Named Pipes"
    
    Detects the pipes established by Cobalt Strike to allow a communication between its beacons.
    
    - **Effort:** master
    
??? abstract "CreateRemoteThread Common Process Injection"
    
    Detects a possible process injection through CreateRemoteThread() which is spotted by EventID 8 from Sysmon and several EDRs. This rule has a list of process commonly being injected by the attackers that should be updated regularly.
    
    - **Effort:** advanced
    
??? abstract "Daspren Parad Malicious Behavior"
    
    Detects when Daspren Parad kills a process with a malicious behavior.
    
    - **Effort:** master
    
??? abstract "Dynwrapx Module Loading"
    
    Detects the loading of DynamicWrapperX (Dynwrapx). It is used by some malware in their infection chain and could help to detect its usage from vbs/wscript/cscript scripts. This is based on Microsoft Windows Sysmon events (Event ID 7).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Malicious Named Pipe"
    
    Detects the creation of a named pipe used by known malware. Prerequisites are logging for PipeEvents in Sysmon config (Event ID 17 and 18).
    
    - **Effort:** intermediate
    
??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate
    
??? abstract "Process Herpaderping"
    
    Detection of process herpaderping using Sysmon Event ID 25. It detects that an image has been locked for access. Several processes have been excluded to avoid FPs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Process Hollowing Detection"
    
    Detection of process hollowing using Sysmon Event ID 25. It detects that an image has been replaced in a process memory.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Searchindexer Wrong Parent"
    
    Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Searchprotocolhost Wrong Parent"
    
    Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 12/03/2024 - minor - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Smss Wrong Parent"
    
    Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 05/04/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake
            
??? abstract "Spoolsv Wrong Parent"
    
    Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.
            
??? abstract "Suspicious Process Requiring DLL Starts Without DLL"
    
    Detects potential process injection and hollowing on processes that usually require a DLL to be launched, but are launched without any argument. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/01/2024 - minor - Added filter to reduce false positives
            
??? abstract "Svchost Wrong Parent"
    
    Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/07/2023 - minor - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 31/01/2024 - minor - Adding filters to reduce false positives
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.
            
??? abstract "Taskhost Wrong Parent"
    
    Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
??? abstract "Taskhostw Wrong Parent"
    
    Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.
            
??? abstract "Wsmprovhost Wrong Parent"
    
    Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
        - 04/07/2023 - major - Added filter to reduce false positives
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
        - 25/10/2023 - minor - Adding filter to reduce false positives.
        - 19/03/2024 - major - Added filter to reduce false positives
        - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.
            
**Scripting**

??? abstract "Suspicious VBS Execution Parameter"
    
    Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.
    
    - **Effort:** elementary
    
**Indicator Removal**

??? abstract "AWS CloudTrail KMS CMK Key Deleted"
    
    Detects when a CMK is deleted or scheduled for deletion
    
    - **Effort:** advanced
    
??? abstract "Clear EventLogs Through CommandLine"
    
    Detects a command that clears event logs which could indicate an attempt from an attacker to erase its previous traces.
    
    - **Effort:** intermediate
    
??? abstract "Compression Followed By Suppression"
    
    Detects when a file is compressed and deleted.
    
    - **Effort:** advanced
    
??? abstract "Cookies Deletion"
    
    Detects when cookies are deleted by a suspicious process.
    
    - **Effort:** master
    
??? abstract "ETW Tampering"
    
    Detects a command that clears or disables any ETW Trace log which could indicate a logging evasion
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 08/11/2023 - minor - Added filter to reduce false positives
            
??? abstract "Erase Shell History"
    
    Malware and attacker try to reduce their fingerprints on compromised host by deleting shell history.
    
    - **Effort:** advanced
    
??? abstract "Eventlog Cleared"
    
    Some threat groups tend to delete local EventLogs (Security being the most common one to be deleted) using certain utilities. The EventID 517 is old and 1102 should be used for this instead on newer Windows versions.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "High Privileges Network Share Removal"
    
    Detects high privileges shares being deleted with the net share command.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/02/2024 - major - changing current pattern and adding another one
            
??? abstract "Microsoft Defender Antivirus History Deleted"
    
    Windows Defender history has been deleted. Could be an attempt by an attacker to remove its traces.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender Antivirus History Directory Deleted"
    
    Windows Defender history directory has been deleted. This could be an attempt by an attacker to remove its traces.
    
    - **Effort:** elementary
    
??? abstract "Microsoft Defender Antivirus Tampering Detected"
    
    Detection of Windows Defender Tampering, from definitions' deletion to deactivation of parts or all of Defender.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 07/08/2023 - minor - Rule effort changed from intermediate to advanced considering the number of false positives observed.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Secure Deletion With SDelete"
    
    Detects renaming of file while deletion with SDelete tool. SDelete is a tool that permits to securely delete files by overwriting them (no recovery possible). Few threat actors are using it to delete traces of their malware.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Valid Accounts**

??? abstract "Account Added To A Security Enabled Group"
    
    Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - add similarity strategy
            
??? abstract "Account Removed From A Security Enabled Group"
    
    Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 12/07/2024 - minor - Add similarity strategy
            
??? abstract "Account Tampering - Suspicious Failed Logon Reasons"
    
    This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Admin User RDP Remote Logon"
    
    Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Authentication Impossible Travel"
    
    Detects impossible travel when performing authentication from a source IP address, grouped by username.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/07/2024 - major - review filter to avoid false positive
            
??? abstract "Broadcom Edge Secure Web Gateway High Threat"
    
    Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.
    
    - **Effort:** master
    
??? abstract "Brute-Force On Fortinet Firewall Login"
    
    Spots many failed attempts to log on an administration interface.
    
    - **Effort:** master
    
??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Minor change in selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Failed Logon Followed By A Success From Public IP Addresses"
    
    A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/05/2024 - major - Adding new field and switching to correlation rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Fortigate Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Account Suspended"
    
    Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Added"
    
    Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Application Authorized"
    
    Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.
    
    - **Effort:** master
    
??? abstract "Google Cloud Audit Logs Attack Warning"
    
    Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".
    
    - **Effort:** intermediate
    
??? abstract "Google Workspace Account Warning"
    
    Detects a suspicious login, leaked password, or account disabled following suspicious activity.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace Admin Creation"
    
    Detects when an admin is created or when his role is changed.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Adding new element to increase detection.
            
??? abstract "Google Workspace Suspicious Login"
    
    Detects a suspicious login reported by google.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force On Firewall"
    
    Detects successful access to administration console of a firewall after several failure.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force On FreeRadius"
    
    A user has attempted to login several times (brute-force) with error then one success.
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force On Sekoia.io"
    
    Detects successful access to Sekoia.io after several failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "Microsoft 365 Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.
    
    - **Effort:** master
    
??? abstract "Microsoft Entra ID (Azure AD) Device Code Authentication"
    
    Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)
    
    - **Effort:** master
    
??? abstract "Netskope Admin Audit"
    
    Audit events for admin activites, from Logins to policies' changes.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "Okta Many Passwords Reset Attempt"
    
    This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.
    
    - **Effort:** advanced
    
??? abstract "Okta Suspicious Activity Reported"
    
    Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.
    
    - **Effort:** advanced
    
??? abstract "Okta Unauthorized Access to App"
    
    An user tries to access an unauthorized application.
    
    - **Effort:** master
    
??? abstract "User Added to Local Administrators"
    
    Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 04/04/2024 - major - Rule's pattern field changed
            
**Rundll32**

??? abstract "PowerShell Execution Via Rundll32"
    
    Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified
    
    - **Effort:** intermediate
    
**Modify Registry**

??? abstract "Blue Mockingbird Malware"
    
    Attempts to detect system changes made by Blue Mockingbird
    
    - **Effort:** elementary
    
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate
    
??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Disable .NET ETW Through COMPlus_ETWEnabled"
    
    Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.
    
    - **Effort:** intermediate
    
??? abstract "Disable Security Events Logging Adding Reg Key MiniNt"
    
    Detects the addition of a key 'MiniNt' to the registry. Upon a reboot, Windows Event Log service will stopped write events.  Prerequisites: Logging for Registry events for this specific registry key is needed in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Disable Workstation Lock"
    
    Registry change in order to disable the ability to lock the computer by using CTRL+ALT+DELETE or CTRL+L. This registry key does not exist by default. Its creation is suspicious and the value set to "1" means an activation. It has been used by FatalRAT, but other attacker/malware could probably use it. This rule needs Windows Registry changes (add,modification,deletion) logging which can be done through Sysmon Event IDs 12,13,14.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "Disabling SmartScreen Via Registry"
    
    Detects when a user disables smartscreen.
    
    - **Effort:** elementary
    
??? abstract "FlowCloud Malware"
    
    Detects FlowCloud malware from threat group TA410. This requires Windows Event registry logging.
    
    - **Effort:** elementary
    
??? abstract "LanManServer Registry Modify"
    
    Detects when the LanManServer registry sub-key MaxMpxCt is modified. An attacker can modified this value to increase the maximum number of outstanding client requests supported. 
    
    - **Effort:** elementary
    
??? abstract "NetNTLM Downgrade Attack"
    
    Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "OceanLotus Registry Activity"
    
    Detects registry keys created in OceanLotus (also known as APT32) attack. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "RDP Port Change Using Powershell"
    
    Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 
    
    - **Effort:** intermediate
    
??? abstract "RDP Sensitive Settings Changed"
    
    Detects changes to RDP terminal service sensitive settings. Logging for registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** advanced
    
??? abstract "RedMimicry Winnti Playbook Registry Manipulation"
    
    Detects actions caused by the RedMimicry Winnti playbook. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary
    
??? abstract "Remote Registry Management Using Reg Utility"
    
    Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Desktopimgdownldr Execution"
    
    Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious New Printer Ports In Registry"
    
    Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Ursnif Registry Key"
    
    Detects a new registry key created by Ursnif malware. The rule requires to log for Registry Events, which can be done using SYsmon's Event IDs 12,13 and 14.
    
    - **Effort:** elementary
    
??? abstract "Wdigest Enable UseLogonCredential"
    
    Detects modification of the Windows Registry value of HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential. This technique is used to extract passwords in clear-text using WDigest. The rule requires to log for Registry Events, which can be done using Sysmon Event IDs 12, 13 and 14.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 08/08/2024 - major - Rule's pattern field changed and pattern improved to cause less false positives.
            
**Component Object Model Hijacking**

??? abstract "Windows Registry Persistence COM Key Linking"
    
    Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 14/12/2023 - minor - Exclude common legitimate processes
            
**Trusted Developer Utilities Proxy Execution**

??? abstract "MSBuild Abuse"
    
    Detection of MSBuild uses by attackers to infect an host. Focuses on XML compilation which is a Metasploit payload, and on connections made by this process which is unusual.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Access Token Manipulation**

??? abstract "Jumpcloud Api Key Updated"
    
    An API Token has been updated on Jumplcoud portal.
    
    - **Effort:** advanced
    
??? abstract "Meterpreter or Cobalt Strike Getsystem Service Installation"
    
    Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting some of the techniques being used (technique 1,2 and 5).
    
    - **Effort:** elementary
    
??? abstract "Okta API Token created"
    
    A new API Token has been created on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Okta API Token revoked"
    
    A new API Token has been deleted on Okta SSO.
    
    - **Effort:** advanced
    
??? abstract "Possible RottenPotato Attack"
    
    Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
**Deobfuscate/Decode Files or Information**

??? abstract "Correlation Linux Decode And Exec"
    
    A Base64 string has been decoded and executed through a pipe. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "FromBase64String Command Line"
    
    Detects suspicious FromBase64String expressions in command line arguments.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender Antivirus Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line or scripts.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender Antivirus Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender through command line or PowerShell scripts. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Microsoft Defender Antivirus Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master
    
??? abstract "Suspicious Mshta Execution"
    
    Detects suspicious mshta.exe execution patterns, either involving file polyglotism, remote file (http, ftp or ldap) or suspicious location. This technique is often used by threat actors.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 17/10/2024 - minor - Adding similarity_strategy
            
??? abstract "Suspicious XOR Encoded PowerShell Command Line"
    
    Detects suspicious powershell process which includes bxor command, alternative obfuscation  method to b64 encoded commands.
    
    - **Effort:** advanced
    
??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
            
**CMSTP**

??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.
            
??? abstract "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate
    
**BITS Jobs**

??? abstract "BITSAdmin Download"
    
    Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 06/12/2023 - minor - Adding key words to increase detection.
            
**Indirect Command Execution**

??? abstract "CVE 2022-1292"
    
    The c_rehash script does not properly sanitise shell metacharacters to prevent command injection. This script is distributed by some operating systems in a manner where it is automatically executed. On such operating systems, an attacker could execute arbitrary commands with the privileges of the script.
    
    - **Effort:** advanced
    
??? abstract "Successful Brute Force Login From Internet"
    
    Detects a spike of failed login followed by a success one from Internet for a given source and target
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Traffic Signaling**

??? abstract "Binary List Tcp"
    
    A binary is trying to list TCP connections. The prerequisites are to enable monitoring of the open and openat syscalls using Auditbeat.
    
    - **Effort:** advanced
    
**Rogue Domain Controller**

??? abstract "DC Shadow via Service Principal Name (SPN) creation"
    
    Detects DCShadow via new Service Principal Name (SPN) creation 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
**Exploitation for Defense Evasion**

??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
??? abstract "Microsoft Malware Protection Engine Crash"
    
    Detects a crash of the Microsoft Malware Protection Engine process (MsMpEng.exe), which is suspicious and could be related to an attacker disabling the Windows protection.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "SharePoint Authenticated SSRF"
    
    Detects succesful SSRF from an authenticated SharePoint user.
    
    - **Effort:** elementary
    
**System Binary Proxy Execution**

??? abstract "AccCheckConsole Executing Dll"
    
    Detects suspicious LOLBIN AccCheckConsole execution with parameters as used to load an arbitrary DLL.
    
    - **Effort:** advanced
    
??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.
            
??? abstract "CMSTP UAC Bypass via COM Object Access"
    
    Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 28/05/2024 - minor - Add pattern to filter to improve coverage
            
??? abstract "CVE-2017-11882 Microsoft Office Equation Editor Vulnerability"
    
    Detects the exploitation of CVE-2017-11882 vulnerability. The Microsoft Office Equation Editor has no reason to do a network request or drop an executable file. This requires a sysmon configuration with file and network events.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "CertOC Loading Dll"
    
    Detects when a user installs certificates by using CertOC.exe to loads the target DLL file.
    
    - **Effort:** intermediate
    
??? abstract "Control Panel Items"
    
    Detects the malicious use of a control panel item
    
    - **Effort:** advanced
    
??? abstract "Dynwrapx Module Loading"
    
    Detects the loading of DynamicWrapperX (Dynwrapx). It is used by some malware in their infection chain and could help to detect its usage from vbs/wscript/cscript scripts. This is based on Microsoft Windows Sysmon events (Event ID 7).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Empire Monkey Activity"
    
    Detects EmpireMonkey APT reported Activity
    
    - **Effort:** elementary
    
??? abstract "Equation Group DLL_U Load"
    
    Detects a specific tool and export used by EquationGroup
    
    - **Effort:** elementary
    
??? abstract "Explorer Process Executing HTA File"
    
    Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.
    
    - **Effort:** intermediate
    
??? abstract "IcedID Execution Using Excel"
    
    Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 
    
    - **Effort:** elementary
    
??? abstract "MOFComp Execution"
    
    Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.
    
    - **Effort:** intermediate
    
??? abstract "Malspam Execution Registering Malicious DLL"
    
    Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).
    
    - **Effort:** elementary
    
??? abstract "MavInject Process Injection"
    
    Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)
    
    - **Effort:** intermediate
    
??? abstract "Mshta JavaScript Execution"
    
    Identifies suspicious mshta.exe commands that execute JavaScript supplied as a command line argument.
    
    - **Effort:** elementary
    
??? abstract "PowerShell Execution Via Rundll32"
    
    Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified
    
    - **Effort:** intermediate
    
??? abstract "SquirrelWaffle Malspam Execution Loading DLL"
    
    Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Control Process"
    
    Detects suspicious execution of control.exe process when used to execute a DLL file.
    
    - **Effort:** advanced
    
??? abstract "Suspicious DLL Loading By Ordinal"
    
    Detects suspicious DLL Loading by ordinal number in a non legitimate or rare folders. For example, Sofacy (APT28) used this technique to load their Trojan in a campaign of 2018.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Desktopimgdownldr Execution"
    
    Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Mshta Execution"
    
    Detects suspicious mshta.exe execution patterns, either involving file polyglotism, remote file (http, ftp or ldap) or suspicious location. This technique is often used by threat actors.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 17/10/2024 - minor - Adding similarity_strategy
            
??? abstract "Suspicious Regasm Regsvcs Usage"
    
    catch abuse of regsvcs and regasm lolbin by attacker
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/09/2023 - major - Rule creation
            
??? abstract "Suspicious Regsvr32 Execution"
    
    Detects suspicious regsvr32.exe executions, either regsvr32 registering a DLL in an unusual repository (temp/, appdata/ or public/), or regsvr32 executed by an unusual parent process, or regsvr32 executing an unusual process, or regsvr32 registering a media file and not a DLL (as seen in IcedID campaigns), or regsvr32 registering a ocx file in appdata/.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 23/11/2023 - major - Extended detection and added filter
            
??? abstract "Suspicious Rundll32.exe Execution"
    
    The process rundll32.exe executes a newly dropped DLL with update /i in the command line. This specific technic was observed at least being used by the IcedID loading mechanism dubbed Gziploader.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/09/2023 - minor - Extend to some usage without dll filename
            
??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Windows Installer Execution"
    
    Detects suspicious execution of the Windows Installer service (msiexec.exe) which could be used to install a malicious MSI package hosted on a remote server.
    
    - **Effort:** intermediate
    
??? abstract "xWizard Execution"
    
    Detects the execution of Xwizard tool with specific arguments which utilized to run custom class properties.
    
    - **Effort:** master
    
**XSL Script Processing**

??? abstract "WMIC Loading Scripting Libraries"
    
    Detects threat actors proxy executing code and bypassing application controls by leveraging wmic and the `/FORMAT` argument switch to download and execute an XSL file (i.e js, vbs, etc).   The rule requires to log Loaded DLLs to work properly, which can be done using Sysmon Event ID 7.
    
    - **Effort:** master
    
??? abstract "XSL Script Processing And SquiblyTwo Attack"
    
    Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.
    
    - **Effort:** intermediate
    
**File and Directory Permissions Modification**

??? abstract "AD Object WriteDAC Access"
    
    Detects WRITE_DAC access to a domain object. This requires Windows Event ID 4662.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Rule's effort level has been changed to advanced as legitimate administrator actions can trigger the rule.
            
??? abstract "File Or Folder Permissions Modifications"
    
    Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files.
    
    - **Effort:** master
    
??? abstract "File and Directory Permissions Modification"
    
    Detects the use of chmod to give high level permissions to file that might be binary files. The prerequisites are to enable monitoring of the fchmodat, chmod and fchmod syscalls using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "ICacls Granting Access To All"
    
    Detects suspicious icacls command granting access to all, used by the ransomware Ryuk to delete every access-based restrictions on files and directories. ICacls is a built-in Windows command to interact with the Discretionary Access Control Lists (DACLs) which can grand adversaries higher permissions on specific files and folders.
    
    - **Effort:** elementary
    
??? abstract "Linux Remove Immutable Attribute"
    
    Adversaries may used chattr utility to alter file and folder attributes to control sudden operations like the deletion and modification of files.
    
    - **Effort:** intermediate
    
**Domain or Tenant Policy Modification**

??? abstract "Creation or Modification of a GPO Scheduled Task"
    
    Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Domain Trust Created Or Removed"
    
    A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "ESET Protect Set Policy"
    
    Detects when a new policy is set or removed.
    
    - **Effort:** master
    
??? abstract "GPO Executable Delivery"
    
    Detects MSI binaries run through GPOs.
    
    - **Effort:** intermediate
    
??? abstract "Jumpcloud Policy Modified"
    
    Detects when a Jumpcloud policy is modified.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) Domain Trust Modification"
    
    Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Confirm the added or modified target domain/URL is legitimate administrator behavior.
    
    - **Effort:** elementary
    
??? abstract "Okta Policy Modified or Deleted"
    
    Detects when an Okta policy is modified or deleted.
    
    - **Effort:** advanced
    
??? abstract "Okta Policy Rule Modified or Deleted"
    
    Detects when an Okta Policy Rule is Modified or Deleted.
    
    - **Effort:** advanced
    
??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/07/2023 - minor - Added AD groups and change to effort master.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Tenable Identity Exposure / Alsid Critical Severity Alert"
    
    Tenable Identity Exposure / Alsid raised a critical severity alert.
    
    - **Effort:** master
    
??? abstract "Tenable Identity Exposure / Alsid High Severity Alert"
    
    Tenable Identity Exposure / Alsid raised an alert.
    
    - **Effort:** master
    
**Abuse Elevation Control Mechanism**

??? abstract "CMSTP UAC Bypass via COM Object Access"
    
    Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 28/05/2024 - minor - Add pattern to filter to improve coverage
            
??? abstract "COM Hijack Via Sdclt"
    
    Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.
    
    - **Effort:** intermediate
    
??? abstract "Citrix NetScaler (ADC) Actions Blocked"
    
    This rule aims to detect a large amount of actions blocked performed from the same source.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace Bypass 2FA"
    
    Detects when user tries to bypass the 2FA.
    
    - **Effort:** master
    
??? abstract "HTML Smuggling Suspicious Usage"
    
    Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.
    
    - **Effort:** intermediate
    
??? abstract "Linux Capabilities Discovery"
    
    Linux capabilities are special attributes in the Linux kernel that grant processes and binary executables specific privileges that are normally reserved for processes whose effective user ID is 0 (The root user, and only the root user, has UID 0). This rule aims to detect discovery of such capabilities on the Linux system. The prerequisites are to enable monitoring of the execve and getxattr syscalls using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "Okta User Impersonation Access"
    
    A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.
    
    - **Effort:** advanced
    
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Setuid Or Setgid Usage"
    
    Detects the usage of a setuid or a setgid. The prerequisites are to enable monitoring of the setuid and setgid syscalls using Auditbeat.
    
    - **Effort:** intermediate
    
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
??? abstract "UAC Bypass Using Fodhelper"
    
    Detects UAC bypass method using Fodhelper after setting the proper registry key, used in particular by Agent Tesla (RAT) or more recently by Earth Luscas. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
            
??? abstract "UAC Bypass Via Sdclt"
    
    Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)
    
    - **Effort:** elementary
    
??? abstract "UAC Bypass via Event Viewer"
    
    Detects UAC bypass method using Windows event viewer. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Improve filter to reduce false positives and clarified the rule pattern.
        - 21/09/2023 - minor - Improve filter to reduce false positives
            
??? abstract "Unusual Process Executed in Temporary Directory"
    
    Identifies processes running in a temporary folder. This is sometimes done by adversaries to hide malware. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.
    
    - **Effort:** master
    
**Use Alternate Authentication Material**

??? abstract "Abusing Azure Browser SSO"
    
    Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
??? abstract "Potential RDP Connection To Non-Domain Host"
    
    Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced
    
??? abstract "Successful Overpass The Hash Attempt"
    
    Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash behavior of e.g Mimikatz's sekurlsa::pth module.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
**Subvert Trust Controls**

??? abstract "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master
    
??? abstract "Microsoft Intune Non-Compliant Device"
    
    Detects Microsoft Intune reporting a device in a non-compliant state. This can indicate either a misconfiguration in Intune or a change of configuration on said device.
    
    - **Effort:** advanced
    
??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
            
**Modify Authentication Process**

??? abstract "1Password EPM MFA Disable"
    
    Detects when the MFA for 1Password is disabled.
    
    - **Effort:** master
    
??? abstract "Active Directory Shadow Credentials"
    
    Detects alternative credentials material adding. Attackers can abuse msDS-KeyCredentialLink and create a key pair to obtain a persistent and stealthy access to the target user or computer.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace MFA changed"
    
    Detects when the settings for the MFA are modified.
    
    - **Effort:** master
    
??? abstract "Google Workspace Password Change"
    
    Detects when a password is changed. An attacker can perform this action to impact the availability of the account.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/06/2024 - minor - Adding new element to increase detection.
            
??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) MFA Method Change"
    
    This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.
    
    - **Effort:** master
    
**Impair Defenses**

??? abstract "AMSI Deactivation Using Registry Key"
    
    The rule detects attempts to deactivate/disable the AMSI provider by deleting the associated registry key.
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail Config DeleteConfigurationRecorder"
    
    Detects when the Configuration Recorder was deleted. The configuration recorder is used to detect changes in your resource configurations and capture these changes as configuration items.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Config Disable Channel/Recorder"
    
    Detects AWS Config Service disabling channel or recorder
    
    - **Effort:** elementary
    
??? abstract "AWS CloudTrail Disable MFA"
    
    Detects a user disabling the multi factor authentication mechanism for its account. It could be a sign of malicious activity.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail EC2 Security Group Modified"
    
    Detects when an AWS EC2 security group has been modified
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail EventBridge Rule Disabled Or Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting or disabling EventBridge rules
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail GuardDuty Detector Deleted"
    
    Detects when an attacker is trying to evade defenses by deleting a GuardDuty detector
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 08/11/2023 - minor - Added filter to reduce false positives
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "AWS CloudTrail GuardDuty Detector Suspended"
    
    Detects the suspension of the GuardDuty service
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "AWS CloudTrail GuardDuty Disruption"
    
    Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts against malicious IPs
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM AWSCompromisedKeyQuarantineV2"
    
    Detects when AWS CloudTrail detected an AWS Access Key that was compromised, and then quarantined by AWS. This could indicate for instance that the private key was found on a GitHub public repository.
    
    - **Effort:** elementary
    
??? abstract "AWS CloudTrail IAM AddClientIDToOpenIDConnectProvider"
    
    Detects the addition of a Client ID to an existing identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM ChangePassword"
    
    Detects when an IAM user wants to change its password.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail IAM CreateOpenIDConnectProvider"
    
    Detects the creation of an IAM entity to describe an identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM CreateSAMLProvider"
    
    Detects when an IAM user creates a SAML provider, which could allow third-party connection and therefore could be used by attackers.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM DeleteOpenIDConnectProvider"
    
    Detects the deletion of an IAM entity to describe an identity provider that supports OpenID Connect.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM DeleteSAMLProvider"
    
    Detects when an IAM user deletes a SAML provider, which could be performed by attackers to cover their tracks.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM RemoveClientIDFromOpenIDConnectProvider"
    
    Detects when a Client ID is removed from an identity provider that supports OpenID Connect. Could be used by attackers for sabotage or to cover their tracks.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM UpdateOpenIDConnectProviderThumbprint"
    
    Detects the update of a ThumbPrint from an identity provider that supports OpenID Connect. This could be a sign of an attacker adding a trusted certificate.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM UpdateSAMLProvider"
    
    Detects when an IAM user updates a SAML provider. Attackers could perform that to be stealthy by adding a third-party connection into an existing SAML provider.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Important Change"
    
    Detects disabling, deleting and updating of a Trail source which could be done by some attackers trying to masquerade their activity.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail Remove Flow logs"
    
    Detects when an attacker is removing Flow Logs to cover their tracks
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/11/2023 - minor - Changing effort level.
            
??? abstract "Address Space Layout Randomization (ASLR) Alteration"
    
    ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it
    
    - **Effort:** intermediate
    
??? abstract "Clear EventLogs Through CommandLine"
    
    Detects a command that clears event logs which could indicate an attempt from an attacker to erase its previous traces.
    
    - **Effort:** intermediate
    
??? abstract "Debugging Software Deactivation"
    
    Deactivation of some debugging softwares using taskkill command. It was observed being used by Ransomware operators.
    
    - **Effort:** elementary
    
??? abstract "Disable .NET ETW Through COMPlus_ETWEnabled"
    
    Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.
    
    - **Effort:** intermediate
    
??? abstract "Disable Security Events Logging Adding Reg Key MiniNt"
    
    Detects the addition of a key 'MiniNt' to the registry. Upon a reboot, Windows Event Log service will stopped write events.  Prerequisites: Logging for Registry events for this specific registry key is needed in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Disable Task Manager Through Registry Key"
    
    Detects commands used to disable the Windows Task Manager by modifying the proper registry key in order to impair security tools. This technique is used by the Agent Tesla RAT, among others.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
        - 25/06/2024 - major - Fix pattern selection
            
??? abstract "Disable Windows Defender Credential Guard"
    
    Detects registry keys being changed to disable Windows Defender Credential Guard. The rule requires to log Registry Keys modifications or creations, which can be done using Sysmon Event IDs 12,13 and 14.
    
    - **Effort:** intermediate
    
??? abstract "Disabled IE Security Features"
    
    Detects from the command lines or the registry, changes that indicate unwanted modifications to registry keys that disable important Internet Explorer security features. This has been used by attackers during Operation Ke3chang.
    
    - **Effort:** advanced
    
??? abstract "Disabled Service"
    
    Service disabling can be abused by attacker to deny security mecanisms (eg: firewall, EDR, ect) and it is also often used by cryptominer to exploit as much RAM & CPU as possible on infected host. The prerequisites are to enable monitoring of the truncate, rename and unlink syscalls using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Dism Disabling Windows Defender"
    
    Detects windows defender disabled by dism.
    
    - **Effort:** advanced
    
??? abstract "ETW Tampering"
    
    Detects a command that clears or disables any ETW Trace log which could indicate a logging evasion
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 08/11/2023 - minor - Added filter to reduce false positives
            
??? abstract "FLTMC command usage"
    
    Detects the use of fltmc to list and load/unload a filter driver.
    
    - **Effort:** advanced
    
??? abstract "Fail2ban Unban IP"
    
    An IP was ubaned by Fail2ban. It could be use to allow malicous traffic.
    
    - **Effort:** advanced
    
??? abstract "GitHub Delete Action"
    
    Detects a Delete/Destroy action in GitHub audit logs.
    
    - **Effort:** advanced
    
??? abstract "GitHub Dependabot Or Vulnerability Alerts Disabled"
    
    Detects dependabot or vulnerability alerts being disabled. Dependabot performs a scan to detect insecure dependencies, and sends Dependabot alerts.
    
    - **Effort:** advanced
    
??? abstract "GitHub High Risk Configuration Disabled"
    
    Detects a configuration being disabled in GitHub. It detects only configuration judged as highly risky if disabled. An organization should adapt this rule according to its environment.
    
    - **Effort:** advanced
    
??? abstract "GitHub New Organization Member"
    
    Detects when a member is added or invited to a GitHub organization.
    
    - **Effort:** advanced
    
??? abstract "GitHub Outside Collaborator Detected"
    
    Detects an outside collaborator being removed or having its permissions changed.
    
    - **Effort:** advanced
    
??? abstract "Google Cloud Audit Logs Trusted Domain Added"
    
    Detects when a domain name is added to Google Workspace Trusted Domain. This could be used by an attacker to bypass some security controls or just be a legit admin action.
    
    - **Effort:** intermediate
    
??? abstract "Loss Of Parsing"
    
    Spots the loss of events parsing by Sekoia.io, could indicate a loss of valid events flow. The strategy is to focus on less frequent event to limit the impact of the skewness in the count distribution law.
    
    - **Effort:** master
    
??? abstract "MalwareBytes Uninstallation"
    
    Detects command line being used by attackers to uninstall Malwarebytes.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Configuration Changed"
    
    Detects when an feature configuration change is made to Microsoft Windows Defender (enabling or disabling real-time protection, etc.)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender Antivirus Disable Scheduled Tasks"
    
    The rule detects attempts to deactivate/disable Windows Defender scheduled tasks via command line or PowerShell scripts.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/07/2024 - minor - Adding new commands to increase detection.
            
??? abstract "Microsoft Defender Antivirus Disable SecurityHealth"
    
    The rule detects attempts to deactivate/disable Windows Defender SecurityHealth through command line, PowerShell scripts, and registry. To fully use this rule Windows Registry logging is recommended.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Disable Services"
    
    The rule detects attempts to deactivate/disable Windows Defender through command line and registry.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Disable Using Registry"
    
    The rule detects attempts to deactivate/disable Microsoft Defender Antivirus using registry modification via command line or PowerShell scripts.
    
    - **Effort:** master
    
??? abstract "Microsoft Defender Antivirus Disabled Base64 Encoded"
    
    Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line or scripts.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Microsoft Defender Antivirus Exclusion Configuration"
    
    Detects when an exclusion configuration change is made to Microsoft Windows Defender (adding either a path or process bypass)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 07/08/2023 - major - Considering the amount of false positives the rule effort has been changed to master. Furthermore a filter has been added.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Defender Antivirus Restoration Abuse"
    
    The rule detects attempts to abuse Windows Defender file restoration tool. The Windows Defender process is allowed to write files in its own protected directory. This functionality can be used by a threat actor to overwrite Windows Defender files in order to prevent it from running correctly or use Windows Defender to execute a malicious DLL.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Set-MpPreference Base64 Encoded"
    
    Detects changes of preferences for Windows Defender through command line or PowerShell scripts. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Defender Antivirus Signatures Removed With MpCmdRun"
    
    Detects attempts to remove Windows Defender Signatures using MpCmdRun legitimate Windows Defender executable. No signatures mean Windows Defender will be less effective (or completely useless depending on the option used).
    
    - **Effort:** elementary
    
??? abstract "Microsoft Defender Antivirus Tampering Detected"
    
    Detection of Windows Defender Tampering, from definitions' deletion to deactivation of parts or all of Defender.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 07/08/2023 - minor - Rule effort changed from intermediate to advanced considering the number of false positives observed.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Microsoft Intune Policy Change"
    
    Detects edits, deletions or creations made to an organization Microsoft Intune policies.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Malware Protection Engine Crash"
    
    Detects a crash of the Microsoft Malware Protection Engine process (MsMpEng.exe), which is suspicious and could be related to an attacker disabling the Windows protection.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "NetNTLM Downgrade Attack"
    
    Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "NetSh Used To Disable Windows Firewall"
    
    Detects NetSh commands used to disable the Windows Firewall
    
    - **Effort:** intermediate
    
??? abstract "Netsh Allow Command"
    
    Netsh command line to allow a program to pass through firewall.
    
    - **Effort:** advanced
    
??? abstract "Netsh Allowed Python Program"
    
    Detects netsh command that performs modification on Firewall rules to allow the program python.exe. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate
    
??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Added filter to reduce false positives
            
??? abstract "Netsh Port Opening"
    
    Detects netsh commands that opens a specific port. Can be used by malware or attackers for lateralisation/exfiltration (e.g. SMB/RDP opening).
    
    - **Effort:** master
    
??? abstract "Netsh Program Allowed With Suspicious Location"
    
    Detects Netsh commands that allow a suspcious application location on Windows Firewall, seen on kasidet worm. Last part of the existing rule (commandline startwith) was not added to this rule because it is not relevant.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 29/11/2023 - minor - Update regex pattern to insensitive case
            
??? abstract "Netsh RDP Port Forwarding"
    
    Detects netsh commands that configure a port forwarding of port 3389 used for RDP. This is commonly used by attackers during lateralization on windows environments.
    
    - **Effort:** elementary
    
??? abstract "Netsh RDP Port Opening"
    
    Detects netsh commands that opens the port 3389 used for RDP, used in Sarwent Malware.
    
    - **Effort:** intermediate
    
??? abstract "Okta Blacklist Manipulations"
    
    Detects when some manipulation are done in blacklist configurations.
    
    - **Effort:** intermediate
    
??? abstract "Okta MFA Disabled"
    
    A MFA has beed disabled in Okta SSO. This is a common behavior to gain permanent access over a system.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
            
??? abstract "Okta Network Zone Deactivated"
    
    Detects attempts to deactivate an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** advanced
    
??? abstract "Okta Network Zone Deleted"
    
    Detects attempts to delete an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** advanced
    
??? abstract "Okta Network Zone Modified"
    
    Detects attempts to modify an Okta network zone. Okta network zones can be configured to limit or restrict access to a network based on IP addresses or geolocations. An adversary may attempt to modify, delete, or deactivate an Okta network zone in order to remove or weaken an organization's security controls.
    
    - **Effort:** intermediate
    
??? abstract "Okta Security Threat Configuration Updated"
    
    Detects when the threat configuration has been updated in Okta.
    
    - **Effort:** intermediate
    
??? abstract "Package Manager Alteration"
    
    Package manager (eg: apt, yum) can be altered to install malicious software. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.
    
    - **Effort:** advanced
    
??? abstract "PowerShell AMSI Deactivation Bypass Using .NET Reflection"
    
    Detects Request to amsiInitFailed that can be used to disable AMSI (Antimalware Scan Interface) Scanning. More information about Antimalware Scan Interface https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 13/06/2024 - minor - Changing effort level and adding similarity strategy to regroup alerts.
            
??? abstract "Powershell AMSI Bypass"
    
    This rule aims to detect attempts to bypass AMSI in powershell using specific techniques.
    
    - **Effort:** advanced
    
??? abstract "Process Anti Debug Checking"
    
    Entries in /proc/self/status are used by malware to checks if current process is being debug. The prerequisites are to enable monitoring of the openat, openat2, open and open_by_handle_at syscalls using Auditbeat.
    
    - **Effort:** master
    
??? abstract "Python Opening Ports"
    
    Detects when the Windows Filtering Platform has permitted Python.exe to listen on a port for incoming connections. This activity is most likely related to the deployment of a Python server or an application that needs to communicate over a network. Threat actors could use it for data extraction, hosting a webshell or else. 
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Raccine Uninstall"
    
    Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.
    
    - **Effort:** elementary
    
??? abstract "Rubycat PROVEIT Admin Service Modified"
    
    Rubycat PROVEIT has detected a service modification that could require some review if not expected.
    
    - **Effort:** master
    
??? abstract "SELinux Disabling"
    
    An attacker can disable SELinux to make workstation or server compromise easier as it disables several protections.
    
    - **Effort:** intermediate
    
??? abstract "Suspect Svchost Memory Access"
    
    Detects suspect access to svchost process memory such as that used by Invoke-Phantom (v1.0) to kill the winRM windows event logging service.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Driver Loaded"
    
    Checks the registry key for suspicious driver names that are vulnerable most of the time and loaded in a specific location by the KDU tool from hfiref0x. Some drivers are used by several SysInternals tools, which should have been whitelisted in the filter condition. The driver named "DBUtilDrv2" has been removed as it caused too many false positives unfortunately. It can be added under "drv_name" if more coverage is wanted. This rule needs registry key monitoring (can be done with Sysmon Event IDs 12,13 and 14).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/01/2024 - minor - improve selection to avoid FP
        - 21/05/2024 - major - editing pattern to avoid FP
        - 25/06/2024 - minor - fix pattern following ECS parsing update
            
??? abstract "Suspicious Microsoft Defender Antivirus Exclusion Command"
    
    Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.
    
    - **Effort:** master
    
??? abstract "Suspicious PROCEXP152.sys File Created In Tmp"
    
    Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder. This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU. Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.
    
    - **Effort:** advanced
    
??? abstract "TrustedInstaller Impersonation"
    
    The rule detects attempts to impersonate TrustedInstaller. TrustedInstaller rights could allow a threat actor to delete or modify protected file or create/delete/modify files in protected folders. This technique is used by threat actors to disable Windows Defender.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 05/08/2023 - major - Filters were added to reduce false positives and effort level was modified.
            
??? abstract "WMIC Uninstall Product"
    
    Detects products being uninstalled using WMIC command.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)
            
??? abstract "Windows Defender Deactivation Using PowerShell Script"
    
    Detects attempts to deactivate Windows Defender with PowerShell using ScriptBlockLogging.
    
    - **Effort:** master
    
??? abstract "Windows Firewall Changes"
    
    Detects changes on Windows Firewall configuration
    
    - **Effort:** master
    
**Hide Artifacts**

??? abstract "Hiding Files With Attrib.exe"
    
    Detects usage of attrib.exe to hide files from users.
    
    - **Effort:** advanced
    
??? abstract "Linux Suspicious Nohup Exec"
    
    Detects suspicious usage of nohup which could be leveraged by an attacker to keep a process running or break out from restricted environments
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 Suspicious Inbox Rule"
    
    Business Email Compromise threat actors often create inbox rules to forward, hide, or delete emails containing sensitive information. This rule detects common caracteristics of malicious inbox rules.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 13/03/2024 - minor - Add another suspicious folder.
            
??? abstract "PowerShell NTFS Alternate Data Stream"
    
    Detects writing data into NTFS alternate data streams from PowerShell. Needs Script Block Logging (Event ID 4104)
    
    - **Effort:** advanced
    
??? abstract "Suspicious Headless Web Browser Execution To Download File"
    
    Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.
    
    - **Effort:** elementary
    
**Hijack Execution Flow**

??? abstract "DHCP Callout DLL Installation"
    
    Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).
    
    - **Effort:** intermediate
    
??? abstract "DHCP Server Error Failed Loading the CallOut DLL"
    
    This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DHCP Server Loaded the CallOut DLL"
    
    This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS Server Error Failed Loading The ServerLevelPluginDLL"
    
    This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "DNS ServerLevelPluginDll Installation"
    
    Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).
    
    - **Effort:** master
    
??? abstract "Dynamic Linker Hijacking From Environment Variable"
    
    LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/07/2024 - minor - Added filter to reduce false positvives
            
??? abstract "Elevated Shell Launched By Browser"
    
    Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.
    
    - **Effort:** master
    
??? abstract "Exploiting SetupComplete.cmd CVE-2019-1378"
    
    Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.
    
    - **Effort:** intermediate
    
??? abstract "Hijack Legit RDP Session To Move Laterally"
    
    Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.
    
    - **Effort:** intermediate
    
??? abstract "Linux Shared Lib Injection Via Ldso Preload"
    
    Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process
    
    - **Effort:** intermediate
    
??? abstract "Suspicious DLL side loading from ProgramData"
    
    Detects suspicious DLL side-loading from C:\ProgramData where the DLL is not signed.
    
    - **Effort:** intermediate
    
??? abstract "Svchost DLL Search Order Hijack"
    
    Detects svchost process hijacking through DLL loading. IKEEXT and SessionEnv service, as they call LoadLibrary on files that do not exist within C:\Windows\System32\ by default. An attacker can place their malicious logic within the PROCESS_ATTACH block of their library and restart the aforementioned services "svchost.exe -k netsvcs" to gain code execution on a remote machine.
    
    - **Effort:** master
    
??? abstract "Werfault DLL Injection"
    
    Werfault DLL search order look first in the current file, which lets an attacker use th legitimate exe to run its own DLL.  
    
    - **Effort:** intermediate
    
??? abstract "Windows Registry Persistence COM Search Order Hijacking"
    
    Detects potential COM object hijacking leveraging the COM Search Order. Logging for Registry events is needed, it can be done with Sysmon's Event IDs 12 and 13.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 11/01/2024 - minor - Adding filtering for some FPs
            
**Modify Cloud Compute Infrastructure**

??? abstract "AWS CloudTrail EC2 CreateVPC"
    
    Detects when a VPC is created.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail EC2 Subnet Deleted"
    
    Detects when an attacker is destroying an EC2 subnet.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 22/07/2024 - minor - Update action field for ECS one
            
??? abstract "AWS CloudTrail ECS Cluster Deleted"
    
    Detects when an attacker is destroying an AWS ECS Cluster
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Failed User Creation"
    
    Detects an attemp to create a user account where the result is an explicit denied.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Password Policy Updated"
    
    Detects an update to the password policy. This could be an attempt to lower accounts security level.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail IAM Policy Changed"
    
    Detects change on AWS IAM Policy
    
    - **Effort:** master
    
??? abstract "AWS CloudTrail Root ConsoleLogin"
    
    Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Attempt"
    
    Detects when a request in success or failure is made to transfer a domain name to an other AWS account
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail Route 53 Domain Transfer Lock Disabled"
    
    Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.
    
    - **Effort:** elementary
    
??? abstract "AWS CloudTrail S3 Bucket Replication"
    
    Detects a replication rule being enable for a given S3 bucket: it could provide an attacker a way to exfiltrate data.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security Critical Severity Alert"
    
    Detects when a critical alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security High Severity Alert"
    
    Detects when a high alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security Low Severity Alert"
    
    Detects when a low alert severity is raised by Lacework. This severity level might indicates a change in configuration that could be malicious or not.
    
    - **Effort:** master
    
??? abstract "Lacework Cloud Security Medium Severity Alert"
    
    Detects when a medium alert severity is raised by Lacework. This severity level might indicates a suspicious activity such as new source from user connection.
    
    - **Effort:** master
    
**Network Boundary Bridging**

??? abstract "Loss Of Parsing"
    
    Spots the loss of events parsing by Sekoia.io, could indicate a loss of valid events flow. The strategy is to focus on less frequent event to limit the impact of the skewness in the count distribution law.
    
    - **Effort:** master
    
??? abstract "SharePoint Authenticated SSRF"
    
    Detects succesful SSRF from an authenticated SharePoint user.
    
    - **Effort:** elementary
    
**Deploy Container**

??? abstract "Docker Escape Bind Mount"
    
    Catch Docker escape via mount escape followed by chroot 
    
    - **Effort:** intermediate
    
**Reflective Code Loading**

??? abstract "Linux Fileless Execution"
    
    Process image resolved to memfd syscall. Could be used by adversaries to hide malware
    
    - **Effort:** intermediate
    
## Credential Access
**OS Credential Dumping**

??? abstract "Active Directory Database Dump Via Ntdsutil"
    
    Detects the dump of ntdis.dit database by using the utility ntdsutil.exe. NTDS.dit database stores Active Directory data, including passwords hashes for all users in the domain.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory Replication from Non Machine Account"
    
    Detects potential abuse of Active Directory Replication Service (ADRS) from a non machine account to request credentials. It requires a configuration step where the legit service account should be added to the exclusion list.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cmdkey Cached Credentials Recon"
    
    Detects usage of cmdkey to look for cached credentials.
    
    - **Effort:** intermediate
    
??? abstract "Copying Browser Files With Credentials"
    
    Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.
    
    - **Effort:** elementary
    
??? abstract "Copying Sensitive Files With Credential Data"
    
    Detects copy of files with well-known filenames (sensitive files with credential data) using esentutl. This requires Windows Security event log with the Detailed File Share logging policy enabled.
    
    - **Effort:** elementary
    
??? abstract "Credential Dump Tools Related Files"
    
    Detects processes or file names related to credential dumping tools and the dropped files they generate by default.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 07/08/2024 - major - Effort level was changed. Rule pattern initial field was changed to be ECS compliant and match on more intakes. A process was excluded and a filter was added, both to avoid generating too much false positives.
            
??? abstract "Credential Dumping By LaZagne"
    
    Detects LSASS process access by LaZagne for credential dumping. 
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Credential Dumping Tools Service Execution"
    
    Detects well-known credential dumping tools execution via service execution
    
    - **Effort:** intermediate
    
??? abstract "Credential Dumping-Tools Common Named Pipes"
    
    Detects well-known credential dumping tools execution via specific named pipes. Prerequisites: Logging for PipeEvents is needed in Sysmon config
    
    - **Effort:** master
    
??? abstract "DCSync Attack"
    
    Detects DCSync attack, it is highly likely that the post-exploitation tool Mimikatz was executed.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
        - 05/09/2024 - minor - Changing name of elements.
            
??? abstract "DPAPI Domain Backup Key Extraction"
    
    Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Dumpert LSASS Process Dumper"
    
    Detects the use of Dumpert process dumper, which dumps the lsass.exe process memory
    
    - **Effort:** elementary
    
??? abstract "Grabbing Sensitive Hives Via Reg Utility"
    
    Detects dump of SAM, System or Security hives using reg.exe utility. Adversaries may attempt to dump these Windows Registry to retrieve password hashes and access credentials.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/01/2024 - minor - Rule was improved to have broader detection and filters were added.
            
??? abstract "HackTools Suspicious Names"
    
    Quick-win rule to detect the default process names or file names of several HackTools.
    
    - **Effort:** elementary
    
??? abstract "HackTools Suspicious Process Names In Command Line"
    
    Detects the default process name of several HackTools and also check in command line. This rule is here for quickwins as it obviously has many blind spots.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 10/06/2024 - minor - Added filter to the rule to reduce false positives.
        - 19/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "Impacket Secretsdump.py Tool"
    
    Detects credential dumping via secretdump of impacket suite.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "LSASS Access From Non System Account"
    
    Detects LSASS Access from Non System Account (e.g. Mimikatz)
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "LSASS Memory Dump"
    
    Detects process accessing LSASS memory which is typical for credentials dumping tools. The rule requires Sysmon EventID 10 to work as it is based on the GrantedAccess mask.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Rule effort has been upgraded to master considering the number of different false positives the rule can trigger.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "LSASS Memory Dump File Creation"
    
    LSASS memory dump creation using operating systems utilities. Procdump will use process name in output file if no name is specified.
    
    - **Effort:** intermediate
    
??? abstract "Load Of dbghelp/dbgcore DLL From Suspicious Process"
    
    Detects the load of dbghelp/dbgcore DLL (used to make memory dumps) by suspicious processes. Many tools import dbghelp.dll and / or dbgcore.dll to use the MiniDumpWriteDump function. As an example, SilentTrynity C2 Framework has a module that leverages this API to dump the contents of Lsass.exe and transfer it over the network back to the attacker's machine. Dumpert from OUTFLANK also uses this.
    
    - **Effort:** advanced
    
??? abstract "Lsass Access Through WinRM"
    
    Detects the access of LSASS.exe process through Windows Remote Management (WinRM) protocol. This is often done using Invoke-Mimikatz -ComputerName command, which uses PSRemoting and therefore WinRM. However, this is not limited to the Mimikatz threat and can be done by other tools as well. This rule needs Process Access monitoring, which can be done using Sysmon's event ID 10.
    
    - **Effort:** intermediate
    
??? abstract "Main Memory Dumping"
    
    Attacker might want to leverage their permission on the system or steal authentication tokens to third parties software, website, etc. To do so, attacker might try to dump main memory of computer. The prerequisites are to enable monitoring of the openat and open syscalls using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Malicious Service Installations"
    
    Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Mimikatz Basic Commands"
    
    Detects Mimikatz most popular commands. 
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.
            
??? abstract "Mimikatz LSASS Memory Access"
    
    Detection of in-memory Mimikatz by focusing on processes opening the Local Security Authority (Lsass.exe) process and reading the memory contents of it. This probably means that Mimikatz has been executed on the host, meaning the attacker already has high privileges and is looking to dump credentials, most likely for lateral movement or privilege escalation purposes. The rule requires Sysmon EventID 10 to work as it is based on the GrantedAccess mask.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 06/04/2023 - minor - Whitelisted another SourceImage as it triggered too many false positives.
        - 21/06/2023 - minor - Whitelisted lsm.exe that triggered too many false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "NTDS.dit File In Suspicious Directory"
    
    The file NTDS.dit is supposed to be located mainly in C:\Windows\NTDS. The rule checks whether the file is in a legitimate directory or not (through file creation events). This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** advanced
    
??? abstract "NTDS.dit File Interaction Through Command Line"
    
    Detects interaction with the file NTDS.dit through command line. This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 08/11/2023 - minor - Added filter to reduce false positives
            
??? abstract "NetNTLM Downgrade Attack"
    
    Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Password Dumper Activity On LSASS"
    
    Detects process handle on LSASS process with certain access mask and object type SAM_DOMAIN
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Process Memory Dump Using Comsvcs"
    
    Detects the use of comsvcs in command line to dump a specific process memory. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Filter improved to reduce false positives. On the other hand, some selections were added to improve detection.
        - 10/04/2024 - minor - Rule description was changed due to some mistakes
        - 13/06/2024 - minor - Adding similarity strategy and changing effort level.
            
??? abstract "Process Memory Dump Using Createdump"
    
    Detects the use of createdump.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary
    
??? abstract "Process Memory Dump Using Rdrleakdiag"
    
    Detects the use of rdrleakdiag.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.
    
    - **Effort:** elementary
    
??? abstract "Process Memory Dumping From proc Filesystem"
    
    Attacker might want to leverage their permission on the system or steal authentication to third parties software, website, etc.. To do so, attacker might try to dump memory of interesting process, for instance ftp-server or web server to dig for authentication login and password. The prerequisites are to enable monitoring of the openat and open syscalls using Auditbeat.
    
    - **Effort:** master
    
??? abstract "Process Trace Alteration"
    
    PTrace syscall provides a means by which one process ("tracer") may observe and control the execution of another process ("tracee") and examine and change the tracee's memory and registers. Attacker might want to abuse ptrace functionnality to analyse memory process. It requires to be admin or set ptrace_scope to 0 to allow all user to trace any process.
    
    - **Effort:** advanced
    
??? abstract "RedMimicry Winnti Playbook Dropped File"
    
    Detects actions caused by the RedMimicry Winnti playbook
    
    - **Effort:** elementary
    
??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced
    
??? abstract "SAM Registry Hive Handle Request"
    
    Detects handles requested to SAM registry hive
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious CommandLine Lsassy Pattern"
    
    Detects the characteristic lsassy loop used to identify lsass PIDs
    
    - **Effort:** intermediate
    
??? abstract "Suspicious SAM Dump"
    
    Detects suspicious SAM dump to AppData repository, as cause by QuarksPwDump and other password dumpers. Logging for Microsoft-Windows-Kernel-General Event ID 16 or Sysmon Event ID 11 is needed.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Transfering Files With Credential Data Via Network Shares"
    
    Detects file transfer of sensitive files which contain credential data using network shares.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 17/10/2023 - minor - Improve selection to reduce false positives
            
??? abstract "Unsigned Image Loaded Into LSASS Process"
    
    Loading unsigned image (DLL, EXE) into LSASS process. To activate this rule you need to monitor loaded images into the LSASS process, this can be done with SYSMON Event ID 7.
    
    - **Effort:** advanced
    
??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
    
??? abstract "Wdigest Enable UseLogonCredential"
    
    Detects modification of the Windows Registry value of HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential. This technique is used to extract passwords in clear-text using WDigest. The rule requires to log for Registry Events, which can be done using Sysmon Event IDs 12, 13 and 14.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 08/08/2024 - major - Rule's pattern field changed and pattern improved to cause less false positives.
            
??? abstract "Windows Credential Editor Registry Key"
    
    Detects the use of Windows Credential Editor (WCE). Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** elementary
    
??? abstract "Write To File In Sudoers.d Folder"
    
    A user tried to write something to a file in /etc/sudoers.d. It can be used to elevate privilege related to sudo and make it persistent. The prerequisites are to enable monitoring of the openat syscall using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Write To File In Systemd"
    
    A user tried to write something to a file in /etc/systemd/system. This repository contains services that are run at start. It can be used to run a malicious programm at start with high privileges. The prerequisites are to enable monitoring of the execve openat using Auditbeat.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/10/2023 - minor - Added filter to reduce false positives.
        - 04/01/2023 - minor - Added filter to reduce false positives.
            
**Network Sniffing**

??? abstract "Capture a network trace with netsh.exe"
    
    Detects capture a network trace via netsh.exe trace functionality
    
    - **Effort:** intermediate
    
??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced
    
??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate
    
??? abstract "WiFi Credentials Harvesting Using Netsh"
    
    Detects the harvesting of WiFi credentials using netsh.exe.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.
            
**Brute Force**

??? abstract "1Password EPM Brute Force"
    
    Detects multiple failed login followed by a success from the same user.
    
    - **Effort:** master
    
??? abstract "Anomaly Bruteforce - User Enumeration"
    
    The rule detects abnormally high number of TGT failed or NTLM authent failed associate to error code username don't exist who could indicate user enumeration
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 09/04/2024 - major - change field on aggregation
        - 13/06/2024 - minor - Adding fields to be displayed in alerts.
        - 12/07/2024 - major - improce coverage, enforce filter and change effort
            
??? abstract "Anomaly Bruteforce Disabled Users"
    
    The rule detects abnormally high number of TGT failed or NTLM authent failed associate to error code account disabled who could indicate a brute force attack
    
    - **Effort:** advanced
    
??? abstract "Authentication Impossible Travel"
    
    Detects impossible travel when performing authentication from a source IP address, grouped by username.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/07/2024 - major - review filter to avoid false positive
            
??? abstract "Brute Force WALLIX Bastion"
    
    Detects a successful login after many failed attempts by the same user.
    
    - **Effort:** master
    
??? abstract "Brute-Force On Fortinet Firewall Login"
    
    Spots many failed attempts to log on an administration interface.
    
    - **Effort:** master
    
??? abstract "Correlation Internal Kerberos Password Spraying"
    
    Detect multiple Kerberos authentication failed on several account from one source
    
    - **Effort:** master
    
??? abstract "Correlation Internal Ntlm Password Spraying"
    
    Detect multiple NTLM authentication failed on several account from one source
    
    - **Effort:** master
    
??? abstract "Entra ID Password Compromised By Known Credential Testing Tool"
    
    Detects a sign-in that has a correlation ID known to be used by malicious credential testing scripts. Note that even if the sign-in was blocked by MFA (error 50074) or device authentication (error 50097), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 05/03/2024 - minor - Rule name error was fixed
        - 09/04/2024 - minor - Error code 500532 added
        - 16/04/2024 - minor - Add more correlation IDs and error code 50052
            
??? abstract "Fortigate Firewall Login In Failure"
    
    Detects failed login attemps on firewall administration rule. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "Fortigate Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master
    
??? abstract "FreeRADIUS Failed Authentication"
    
    A failed authentication was logged by FreeRADIUS 
    
    - **Effort:** advanced
    
??? abstract "Google Workspace Login Brute-Force"
    
    Detects when a user failed to login multiple times before a successful login.
    
    - **Effort:** master
    
??? abstract "Login Brute-Force On Firewall"
    
    Detects successful access to administration console of a firewall after several failure.
    
    - **Effort:** advanced
    
??? abstract "Login Brute-Force On FreeRadius"
    
    A user has attempted to login several times (brute-force) with error then one success.
    
    - **Effort:** intermediate
    
??? abstract "Login Brute-Force On Sekoia.io"
    
    Detects successful access to Sekoia.io after several failure.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "Login Brute-Force Successful"
    
    A user has attempted to login several times (brute-force) and succeeded to login.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 06/10/2023 - minor - renaming and tunn filters to limit False Positive
            
??? abstract "Password Change Brute-Force On AzureAD"
    
    A change of password has failed on Azure Active Directory, 5 times for the same user
    
    - **Effort:** intermediate
    
??? abstract "Password Reset Error Brute-Force On AzureAD"
    
    A reset of password has failed on Azure Active Directory, 5 times within the same entity.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.
            
??? abstract "RSA SecurID Failed Authentification"
    
    Detects many failed attempts to authenticate followed by a successfull login for a super admin account.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 08/08/2024 - minor - Group-by values were changed to avoid having too much alerts.
            
??? abstract "Successful Brute Force Login From Internet"
    
    Detects a spike of failed login followed by a success one from Internet for a given source and target
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Multi-Factor Authentication Interception**

??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit"
    
    Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.
    
    - **Effort:** elementary
    
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 09/08/2024 - major - Update the indicator.
        - 25/09/2024 - major - Rename the rule, update the indicators.
            
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
            
??? abstract "EvilProxy Phishing Domain"
    
    Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 Sign-in With No User Agent"
    
    Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
            
??? abstract "Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses"
    
    Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.
    
    - **Effort:** intermediate
    
??? abstract "Okta MFA Bypass Attempt"
    
    A bypass of MFA may have been attempted.
    
    - **Effort:** intermediate
    
??? abstract "Potential Azure AD Phishing Page (Adversary-in-the-Middle)"
    
    Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
            
**Forced Authentication**

??? abstract "Correlation Suspicious Authentication Coercer Behavior"
    
    Detect a possible NTLM Relay attack combine with authent coerce
    
    - **Effort:** intermediate
    
**Exploitation for Credential Access**

??? abstract "Abusing Azure Browser SSO"
    
    Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
**Steal Application Access Token**

??? abstract "Abusing Azure Browser SSO"
    
    Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
**Steal Web Session Cookie**

??? abstract "Copying Browser Files With Credentials"
    
    Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.
    
    - **Effort:** elementary
    
**Unsecured Credentials**

??? abstract "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter
            
??? abstract "Container Credential Access"
    
    Adversaries could abuse containers tools to obtain credential like Kubernetes secret or Kubernetes service account access token
    
    - **Effort:** intermediate
    
??? abstract "Credentials Extraction"
    
    This rule aims to detect the use of a specific command to access some credentials without using mimikatz or another tool.
    
    - **Effort:** advanced
    
??? abstract "Google Cloud Audit Logs 2FA Disabled"
    
    Detects when Google Cloud Audit Logs notify the 2FA deactivation for a user account.
    
    - **Effort:** intermediate
    
??? abstract "Linux Suspicious Search"
    
    Adversaries may search for private key on compromised systems
    
    - **Effort:** intermediate
    
??? abstract "Opening Of a Password File"
    
    Command line detection of common office software opening some password related file. It could be a security breach if an unauthorized user access it.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 07/10/2024 - minor - Modified similarity strategy.
        - 21/03/2024 - minor - Adding similarity strategy to reduce alerts creation.
        - 22/01/2024 - minor - Removing a file extension to allow broader detection.
        - 16/11/2023 - minor - Changing effort level and adding filter to reduce false positives.
        - 03/07/2023 - minor - Added french words for the command lines.
        - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
            
??? abstract "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 02/04/2024 - major - Updating the pattern and adding filter selection
        - 19/02/2024 - minor - Effort level was adapted according to the observed hits for the rule
            
??? abstract "Remote Registry Management Using Reg Utility"
    
    Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "XCopy Suspicious Usage"
    
    Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.
    
    - **Effort:** advanced
    
**Credentials from Password Stores**

??? abstract "1Password EPM Grant Access Vault"
    
    Detects when a group is granted access to a 1Password vault.
    
    - **Effort:** master
    
??? abstract "Anomaly Secret Store Access"
    
    The rule detects abnormally high access to secrets store folder
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 08/04/2024 - minor - change field name on query
        - 12/06/2024 - minor - Adding new fields to be displayed in alerts.
            
??? abstract "Credential Harvesting Via Vaultcmd.exe"
    
    Detects when the process vaultcmd is used for credential harvesting.
    
    - **Effort:** advanced
    
??? abstract "Credentials Extraction"
    
    This rule aims to detect the use of a specific command to access some credentials without using mimikatz or another tool.
    
    - **Effort:** advanced
    
??? abstract "Information Stealer Downloading Legitimate Third-Party DLLs"
    
    Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.
    
    - **Effort:** intermediate
    
??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary
    
**Modify Authentication Process**

??? abstract "1Password EPM MFA Disable"
    
    Detects when the MFA for 1Password is disabled.
    
    - **Effort:** master
    
??? abstract "Active Directory Shadow Credentials"
    
    Detects alternative credentials material adding. Attackers can abuse msDS-KeyCredentialLink and create a key pair to obtain a persistent and stealthy access to the target user or computer.
    
    - **Effort:** elementary
    
??? abstract "Google Workspace MFA changed"
    
    Detects when the settings for the MFA are modified.
    
    - **Effort:** master
    
??? abstract "Google Workspace Password Change"
    
    Detects when a password is changed. An attacker can perform this action to impact the availability of the account.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/06/2024 - minor - Adding new element to increase detection.
            
??? abstract "KeePass Config XML In Command-Line"
    
    Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Entra ID (Azure AD) MFA Method Change"
    
    This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.
    
    - **Effort:** master
    
**Adversary-in-the-Middle**

??? abstract "Correlation Suspicious Authentication Coercer Behavior"
    
    Detect a possible NTLM Relay attack combine with authent coerce
    
    - **Effort:** intermediate
    
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit"
    
    Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.
    
    - **Effort:** elementary
    
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 09/08/2024 - major - Update the indicator.
        - 25/09/2024 - major - Rename the rule, update the indicators.
            
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
            
??? abstract "EvilProxy Phishing Domain"
    
    Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 Sign-in With No User Agent"
    
    Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
            
??? abstract "Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses"
    
    Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.
    
    - **Effort:** intermediate
    
??? abstract "Possible RottenPotato Attack"
    
    Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Potential Azure AD Phishing Page (Adversary-in-the-Middle)"
    
    Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
            
**Steal or Forge Kerberos Tickets**

??? abstract "Kerberos Pre-Auth Disabled in UAC"
    
    The rule identify a change performed on a domain user object that disables Kerberos Pre-Authentication
    
    - **Effort:** elementary
    
??? abstract "Possible Replay Attack"
    
    This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Rubeus Register New Logon Process"
    
    Detects potential use of Rubeus through registering a new logon process. This rule needs the EventID 4611, which can be configured through Group Policies (Audit Security System Extension)
    
    - **Effort:** master
    
??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced
    
??? abstract "Suspicious Kerberos Ticket"
    
    Detect suspicious Kerberos ticket based on on their parameters which suggest that it could be forged.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 03/07/2024 - major - Add filter to cover a second case to improve rule coverage
            
??? abstract "Suspicious Outbound Kerberos Connection"
    
    Detects suspicious outbound network activity via kerberos default port indicating possible lateral movement or first stage PrivEsc via delegation.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
        - 05/08/2024 - major - Rule reworked to match more intakes and have less false positives (filters were added).
            
??? abstract "Suspicious TGS requests (Kerberoasting)"
    
    The rule aims at detecting the Kerberoasting technique, when an attacker requests TGS in order to crack them offline. Toease its task, the attacker requests tickets with weak encryption (such as RC4_HMAC_MD5). The rule therefore detects when an user is requesting 5 TGS for different users in 5 minutes.
    
    - **Effort:** advanced
    
??? abstract "User Couldn't Call A Privileged Service LsaRegisterLogonProcess"
    
    The LsaRegisterLogonProcess function verifies that the application making the function call is a logon process by checking that it has the SeTcbPrivilege privilege set. Possible Rubeus tries to get a handle to LSA. This rule requires to log the Event ID 4673, which can be done by updating the Audit Policy.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Steal or Forge Authentication Certificates**

??? abstract "Suspicious Certificate Request-adcs Abuse"
    
    Detects when a new certificate is requested or granted against Active Directory Certificate Services (AD CS) using a Subject Alternative Name (SAN)
    
    - **Effort:** elementary
    
??? abstract "Suspicious Kerberos Ticket"
    
    Detect suspicious Kerberos ticket based on on their parameters which suggest that it could be forged.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 03/07/2024 - major - Add filter to cover a second case to improve rule coverage
            
## Discovery
**System Service Discovery**

??? abstract "Anomaly Internal RDP"
    
    Detects uncompleted attempts to connect to a Remote Desktop Protocol (RDP) session.
    
    - **Effort:** master
    
??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "SCM Database Handle Failure"
    
    Detects non-system users failing to get a handle of the SCM database.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "SCM Database Privileged Operation"
    
    Detects non-system users performing privileged operation on the SCM database
    
    - **Effort:** master
    
**Query Registry**

??? abstract "Putty Sessions Listing"
    
    Detects attempts to list Putty sessions through registry. To fully work, this rule requires to log registry accesses, which can be done with the Windows Event ID 4656 or 4663 but for that specific configuration is needed.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Remote Registry Management Using Reg Utility"
    
    Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Taskkill Command"
    
    Detects rare taskkill command being used. It could be related to Baby Shark malware.
    
    - **Effort:** intermediate
    
??? abstract "SysKey Registry Keys Access"
    
    Detects handle requests and access operations to specific registry keys to calculate the SysKey. The SysKey allows to decrypt Security Account Mannager (SAM) database entries (from registry or hive) and get NTLM, and sometimes LM hashes of local accounts passwords. Adversaries can calculate the Syskey by using RegOpenKeyEx/RegQueryInfoKey API calls to query the appropriate class info and values from the HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\JD, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Skew1, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\GBG, and HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Data keys.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**System Network Configuration Discovery**

??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/04/2024 - minor - Adding new elements to increase detection.
            
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Headless Web Browser Execution To Download File"
    
    Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.
    
    - **Effort:** elementary
    
**Remote System Discovery**

??? abstract "Anomaly Internal Ping"
    
    Detects internal ping with uncomplete connection on internal network.
    
    - **Effort:** master
    
??? abstract "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced
    
??? abstract "Openfiles Usage"
    
    Detects when the command openfiles, to get information on files opened remotely, is used.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
**System Owner/User Discovery**

??? abstract "RDP Session Discovery"
    
    Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.
    
    - **Effort:** advanced
    
**Network Sniffing**

??? abstract "Capture a network trace with netsh.exe"
    
    Detects capture a network trace via netsh.exe trace functionality
    
    - **Effort:** intermediate
    
??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced
    
??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate
    
??? abstract "WiFi Credentials Harvesting Using Netsh"
    
    Detects the harvesting of WiFi credentials using netsh.exe.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.
            
**Network Service Discovery**

??? abstract "Advanced IP Scanner"
    
    Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.
    
    - **Effort:** master
    
??? abstract "Anomaly Internal Port Connection"
    
    Detects multiple scan of different ports on internal network.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 12/06/2024 - minor - Adding field to be displayed in the alerts and changing the query.
        - 04/07/2024 - minor - Reviewing query.
            
??? abstract "Anomaly Multiple Host Port Scan"
    
    Detects multiple port scan from/to a private address, excluding DNS.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/06/2024 - minor - Adding fields to be displayed in the alert and changing effort level.
            
**System Network Connections Discovery**

??? abstract "Broadcom Edge Secure Web Gateway Anomaly TCP Denied"
    
    Detects a high number of connection TCP denied.
    
    - **Effort:** master
    
??? abstract "Cmd.exe Used To Run Reconnaissance Commands"
    
    Detects command lines with suspicious args
    
    - **Effort:** advanced
    
??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/04/2024 - minor - Adding new elements to increase detection.
            
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
**Permission Groups Discovery**

??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - minor - Adapted the rule to remove false positives.
            
??? abstract "Domain Group And Permission Enumeration"
    
    Detects adversaries attempts to find domain-level groups and permission settings. Commands such as net group /domain of the Net utility can list domain-level groups The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Wizard Spider, FIN6, and other groups used net in their campaigns.
    
    - **Effort:** advanced
    
??? abstract "Gpresult Usage"
    
    Detects when an account uses gpresult to get information on gpo.
    
    - **Effort:** advanced
    
??? abstract "Permission Discovery Via Wmic"
    
    Detects discovery of permission on local groups via the tool wmic.
    
    - **Effort:** advanced
    
**System Information Discovery**

??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/04/2024 - minor - Adding new elements to increase detection.
            
??? abstract "Listing Systemd Environment"
    
    Detects a listing of systemd environment variables. This command could be used to do reconnaissance on a compromised host.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 06/03/2024 - minor - Effort level was adapted according to the observed hits for the rule
            
??? abstract "Shadow Copies"
    
    Detects command line used to create and list shadow copies. An adversary may attempt to get information on shadow volumes to perform deletion or extract password hashes from the ntds.dit file. This rule requires command line logging or Windows PowerShell events (4104).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 11/07/2024 - minor - Adding new elements to detect and adding filter to reduce false positives.
            
??? abstract "Suspicious Headless Web Browser Execution To Download File"
    
    Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.
    
    - **Effort:** elementary
    
??? abstract "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host.
    
    - **Effort:** master
    
??? abstract "WMI Fingerprint Commands"
    
    Detects attacker fingerprint activities based on the correlation of specific WMIC commands. This has been observed with Aurora malware.
    
    - **Effort:** intermediate
    
**File and Directory Discovery**

??? abstract "Netskope DLP Alert"
    
    Detects DLP alerts which are not allowed.  
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
**Account Discovery**

??? abstract "AD Privileged Users Or Groups Reconnaissance"
    
    Detect privileged users or groups reconnaissance based on 4661 Event ID and known privileged users or groups SIDs. If the user account name is not a known admin it is suspicious.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "AD User Enumeration"
    
    Detects access to a domain user from a non-machine account. This requires Windows Security Event ID 4662 and could be triggered by some administrators configuring new users.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Active Directory Data Export Using Csvde"
    
    Detects the use of Csvde, a command-line tool from Windows Server that can be used to export Active Directory data to CSV files. This export doesn't include password hashes, but can be used as a discovery tool to enumerate users, machines and group memberships.
    
    - **Effort:** elementary
    
??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - minor - Adapted the rule to remove false positives.
            
??? abstract "Discovery Commands Correlation"
    
    Detects some frequent discovery commands used by some ransomware operators.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 16/04/2024 - minor - Adding new elements to increase detection.
            
??? abstract "Phosphorus (APT35) Exchange Discovery"
    
    According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about its the environment of compromised Microsoft Exchange servers. The command is the following: Get-Recipient | Select Name -ExpandProperty EmailAddresses -first 1 | Select SmtpAddress |  ft -hidetableheaders
    
    - **Effort:** elementary
    
??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Reconnaissance Commands Activities"
    
    Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.
    
    - **Effort:** intermediate
    
??? abstract "Remote Enumeration Of Lateral Movement Groups"
    
    Detects remote session lists the member of four local groups relevant to lateral movement. This behavior is common in Active Directory mapping tools such as SharpHound.
    
    - **Effort:** intermediate
    
??? abstract "Remote Privileged Group Enumeration"
    
    Detects remote listing of local privileged group. Potential false positives, which should justify alert filters, are service accounts and administrators doing maintenance.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 18/04/2023 - minor - Exclude events from the Local System session that cause false positives.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Shell PID Injection"
    
    Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.
    
    - **Effort:** intermediate
    
**Network Share Discovery**

??? abstract "Netscan Share Access Artefact"
    
    Detects netscan artefact on windows network share - indicate network share discovery.
    
    - **Effort:** intermediate
    
??? abstract "Network Share Discovery"
    
    Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. File sharing over a Windows network occurs over the SMB protocol. This technique is frequently leveraged by threat actors such as APT32, APT41, Wizard Spider. But also, through the use of some malware such as Cobalt Strike, Empire, PlugX and Ramsay.
    
    - **Effort:** master
    
??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
**Domain Trust Discovery**

??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 12/10/2023 - minor - Slight change to a condition in order to reduce false positives.
            
??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - minor - Adapted the rule to remove false positives.
            
??? abstract "Domain Trust Discovery Through LDAP"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. "trustedDomain" which is detected here is a Microsoft Active Directory ObjectClass Type that represents a domain that is trusted by, or trusting, the local AD DOMAIN. Several tools are using LDAP queries in the end to get the information (DSQuery, sometimes ADFind as well, etc.)
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 19/10/2023 - minor - improve filter to reduce false positives
            
??? abstract "NlTest Usage"
    
    Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. These command lines were observed in numerous attacks, but also sometimes from legitimate administrators for debugging purposes. The rule does not cover very basics commands but rather the ones that are interesting for attackers to gather information on a domain.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 10/10/2024 - minor - Adding new elements and filters to increase detection and reduce false positives.
            
??? abstract "Phosphorus Domain Controller Discovery"
    
    According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about the Domain Controller. The command is the following: "powershell.exe" /c Get-WMIObject Win32_NTDomain | findstr DomainController
    
    - **Effort:** intermediate
    
??? abstract "PowerView commandlets 1"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
??? abstract "PowerView commandlets 2"
    
    Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Trickbot Malware Activity"
    
    Detects Trickbot malware process tree pattern in which rundll32.exe is parent of wermgr.exe.
    
    - **Effort:** intermediate
    
**Software Discovery**

??? abstract "WMIC Command To Determine The Antivirus"
    
    Detects WMIC command to determine the antivirus on a system, characteristic of the ZLoader malware (and possibly others)
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 28/02/2024 - minor - Adding a new usage of wmic.
            
**Cloud Service Discovery**

??? abstract "AWS Suspicious Discovery Commands"
    
    Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.
    
    - **Effort:** master
    
??? abstract "AzureEdge in Command Line"
    
    Detects use of azureedge in the command line.
    
    - **Effort:** advanced
    
**Cloud Infrastructure Discovery**

??? abstract "AWS Suspicious Discovery Commands"
    
    Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.
    
    - **Effort:** master
    
**System Location Discovery**

??? abstract "Language Discovery"
    
    Detects when a user makes a query on the language of the system.
    
    - **Effort:** advanced
    
**Cloud Storage Object Discovery**

??? abstract "AWS Suspicious Discovery Commands"
    
    Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.
    
    - **Effort:** master
    
## Lateral Movement
**Remote Services**

??? abstract "AWS CloudTrail EC2 CreateKeyPair"
    
    Detects when a key pair is created. Usually, SendSSHPublicKey is used afterwards to push the created key to an EC2 instance in order to be able to establish a connection to that instance.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail EC2 DeleteKeyPair"
    
    Detects when a specific key pair is deleted. This means the public key was removed from EC2.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail EC2 Enable Serial Console Access"
    
    Detects when the EC2 serial console access feature is enabled. This could abused by some attackers to avoid network detection when accessing to EC2 instances.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail EC2 Instance Connect SendSSHPublicKey"
    
    Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a connection to the console using SSH.
    
    - **Effort:** advanced
    
??? abstract "AWS CloudTrail EC2 Instance Connect SendSerialConsoleSSHPublicKey"
    
    Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a serial connection to the console using SSH.
    
    - **Effort:** advanced
    
??? abstract "Admin Share Access"
    
    Detects access to $ADMIN share. The advanced audit policy setting "Object Access > Audit File Share" must be configured for Success/Failure. Also be very cautious to previously check if this is not commonly used by your administrators as to remotely manage your computers.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cobalt Strike Default Service Creation Usage"
    
    Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Correlation Impacket Smbexec"
    
    This rule detects the execution of smbexec via the relevant share pattern name 
    
    - **Effort:** elementary
    
??? abstract "Denied Access To Remote Desktop"
    
    Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 19/10/2023 - minor - Minor change in selection to reduce false positives.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Lateral Movement Remote Named Pipe"
    
    Detects lateral movement and remote exec using named pipe over network. This requires Windows Security event logging with the File Share enable policy.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 12/06/2024 - minor - Fix filter selection
        - 03/04/2024 - major - Rule's pattern field changed
        - 26/03/2024 - minor - Filter was improved to reduce false positives
            
??? abstract "Lsass Access Through WinRM"
    
    Detects the access of LSASS.exe process through Windows Remote Management (WinRM) protocol. This is often done using Invoke-Mimikatz -ComputerName command, which uses PSRemoting and therefore WinRM. However, this is not limited to the Mimikatz threat and can be done by other tools as well. This rule needs Process Access monitoring, which can be done using Sysmon's event ID 10.
    
    - **Effort:** intermediate
    
??? abstract "MMC Spawning Windows Shell"
    
    Detects a Windows command line executable started from MMC process
    
    - **Effort:** intermediate
    
??? abstract "MMC20 Lateral Movement"
    
    Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe.
    
    - **Effort:** intermediate
    
??? abstract "Protected Storage Service Access"
    
    Detects access to a protected_storage service over the network. It could identify potential abuse of DPAPI to extract domain backup keys from Domain Controllers.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "RDP Login From Localhost"
    
    Detects RDP login from localhost source address, which may be a tunnelled login to bypass network restrictions.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 24/11/2023 - minor - Effort level changed to advanced.
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "RDP Port Change Using Powershell"
    
    Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 
    
    - **Effort:** intermediate
    
??? abstract "Remote Service Activity Via SVCCTL Named Pipe"
    
    Detects remote service activity via remote access to the svcctl named pipe
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/03/2024 - minor - change filter to ACL hex value and adapt effort
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Smbexec.py Service Installation"
    
    Detects the use of smbexec.py tool by detecting a specific service installation
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
**Replication Through Removable Media**

??? abstract "External Disk Drive Or USB Storage Device"
    
    Detects external diskdrives or plugged in USB device.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Exploitation of Remote Services**

??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
??? abstract "CVE-2019-0708 Scan"
    
    Detects the use of a scanner that discovers targets vulnerable to CVE-2019-0708 RDP RCE aka BlueKeep.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "ESET Protect Remote Action"
    
    Detects when different remote commands are performed on the same hostname is a short amount of time.
    
    - **Effort:** master
    
??? abstract "Registry Checked For Lanmanserver DisableCompression Parameter"
    
    Detects registry access for Lanmanserver\Parameters. The check of the value DisableCompression could be a sign of an attack trying to exploit SMBGhost vulnerability (CVE-2020-0796).
    
    - **Effort:** master
    
**Use Alternate Authentication Material**

??? abstract "Abusing Azure Browser SSO"
    
    Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 
    
    - **Effort:** master
    
??? abstract "Potential RDP Connection To Non-Domain Host"
    
    Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Rubeus Tool Command-line"
    
    Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.
    
    - **Effort:** advanced
    
??? abstract "Successful Overpass The Hash Attempt"
    
    Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash behavior of e.g Mimikatz's sekurlsa::pth module.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
## Collection
**Data from Local System**

??? abstract "AWS CloudTrail EC2 VM Export Failure"
    
    Detects attempt to export an AWS EC2 instance. A VM Export might indicate an attempt to extract information from an instance.
    
    - **Effort:** intermediate
    
??? abstract "Formbook File Creation DB1"
    
    Detects specific file creation (Users\*\AppData\Local\Temp\DB1) to store data to exfiltrate (Formbook behavior). Logging for Sysmon event 11 is usually used for this detection. 
    
    - **Effort:** intermediate
    
??? abstract "Information Stealer Downloading Legitimate Third-Party DLLs"
    
    Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data"
    
    Detects PowerShell SnapIn command line or PowerShell script, often used with Get-Mailbox to export Exchange mailbox data.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 13/08/2024 - minor - Added filter to reduce false positives
            
??? abstract "Ntfsinfo Usage"
    
    Detects when the command ntfsinfo is used. An attacker can access to information on the volume from NTFS and have a directory dump of NTFS files.
    
    - **Effort:** advanced
    
**Data from Network Shared Drive**

??? abstract "RDP Configuration File From Mail Process"
    
    Detects RDP configuration file being created or executed by a Mail-related process like Outlook. RDP configuration file will allow, when opened, an user to connect to the configured server easily. Attackers use this to trick victims in order to get a shared drive and potentially retrieve the data from that drive, but also drop a malicious file on the drive to establish persistence. Using RDP can also expose the victim's credential and clipboard data on some cases.
    
    - **Effort:** advanced
    
??? abstract "Suspicious Access To Sensitive File Extensions"
    
    Detects known sensitive file extensions accessed on a network share. This activity could possibly correspond to a malicious one (removing backup, reading sensitive files, etc.).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Email Attachment Received"
    
    Detects email containing a suspicious file as an attachment, based on its extension.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 15/04/2024 - minor - Update email from field to latest parser format
        - 14/11/2024 - major - Adding new file extension and new condition to make the rule broader as it can now match on more intakes.
            
**Data Staged**

??? abstract "CVE-2021-20023 SonicWall Arbitrary File Read"
    
    Detects Arbitrary File Read, which can be used with other vulnerabilities as a mean to obtain outputs generated by attackers, or sensitive data.
    
    - **Effort:** advanced
    
**Email Collection**

??? abstract "Entra ID Consent Attempt to Suspicious OAuth Application"
    
    Detects an attempt to authorize account access to an OAuth application commonly used in business email compromise (BEC) attacks. Investigate the source IP address: unusual countries, RDP hosts and VPN providers are likely indicators of malicious activity.
    
    - **Effort:** elementary
    
??? abstract "Exchange Mailbox Export"
    
    Detection of a standard Exchange Mailbox export, which stores all mails from a user in a pst file, from command line or PowerShell script.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Custom Gmail Route"
    
    Detects when a custom Gmail route is added or modified. This could be abused by attackers to exfiltrate data.
    
    - **Effort:** advanced
    
??? abstract "Google Cloud Audit Logs Email Forwarding"
    
    Detects when an out of domain email forwarding is enabled on Google Cloud.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace Email Forwarding"
    
    Detects when a user enables email forwarding out of the domain
    
    - **Effort:** advanced
    
??? abstract "Microsoft 365 Email Forwarding To Consumer Email Address"
    
    An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (most common consumer email services).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 22/04/2024 - minor - Add zohomail.com
            
??? abstract "Microsoft 365 Email Forwarding To Email Address With Rare TLD"
    
    An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (less common top-level domain).
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 Email Forwarding To Privacy Email Address"
    
    An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (most common privacy email services).
    
    - **Effort:** elementary
    
??? abstract "Outlook Registry Access"
    
    Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 02/04/2024 - major - Updating the pattern and adding filter selection
        - 19/02/2024 - minor - Effort level was adapted according to the observed hits for the rule
            
**Audio Capture**

??? abstract "Audio Capture via PowerShell"
    
    Detects audio capture via PowerShell Cmdlet
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 18/04/2023 - minor - Use more specific patterns to fix false positives.
            
**Data from Cloud Storage**

??? abstract "Netskope DLP Alert"
    
    Detects DLP alerts which are not allowed.  
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
**Adversary-in-the-Middle**

??? abstract "Correlation Suspicious Authentication Coercer Behavior"
    
    Detect a possible NTLM Relay attack combine with authent coerce
    
    - **Effort:** intermediate
    
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit"
    
    Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.
    
    - **Effort:** elementary
    
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 09/08/2024 - major - Update the indicator.
        - 25/09/2024 - major - Rename the rule, update the indicators.
            
??? abstract "Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)"
    
    Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
            
??? abstract "EvilProxy Phishing Domain"
    
    Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.
    
    - **Effort:** intermediate
    
??? abstract "Microsoft 365 Sign-in With No User Agent"
    
    Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
            
??? abstract "Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses"
    
    Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.
    
    - **Effort:** intermediate
    
??? abstract "Possible RottenPotato Attack"
    
    Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Potential Azure AD Phishing Page (Adversary-in-the-Middle)"
    
    Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
            
**Archive Collected Data**

??? abstract "Compress Data for Exfiltration via Archiver"
    
    Detects data compressed by specific tools.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 09/07/2024 - major - Reviewing detection to reduce false positives.
            
??? abstract "Data Compressed With Rar"
    
    An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program.
    
    - **Effort:** master
    
??? abstract "Data Compressed With Rar With Password"
    
    An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program. This is a more specific one for rar where the arguments allow to encrypt both file data and headers with a given password.
    
    - **Effort:** intermediate
    
??? abstract "PowerShell Data Compressed"
    
    Detects data compression through a PowerShell command (could be used by an adversary for exfiltration).
    
    - **Effort:** advanced
    
## Command and Control
**Data Obfuscation**

??? abstract "Suspicious ADSI-Cache Usage By Unknown Tool"
    
    Detects the usage of ADSI (LDAP) operations by tools. This may also detect tools like LDAPFragger. It needs file monitoring capabilities (Sysmon Event ID 11 with .sch file creation logging).
    
    - **Effort:** advanced
    
??? abstract "Suspicious LDAP-Attributes Used"
    
    Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies. Careful as the 5136 is only on domain controllers and needs to be activated through the Group Policy.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Application Layer Protocol**

??? abstract "Bazar Loader DGA (Domain Generation Algorithm)"
    
    Detects Bazar Loader domains based on the Bazar Loader DGA
    
    - **Effort:** elementary
    
??? abstract "Cato Networks SASE High Risk Alert"
    
    Cato Networks SASE intrusion detection has detected a high risk alert.
    
    - **Effort:** master
    
??? abstract "Chafer (APT 39) Activity"
    
    Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Cloudflare Gateway DNS Query Allowed to Malicious Domain"
    
    A DNS query to a domain categorized by Cloudflare Gateway as malicious was allowed because no blocking policy is configured.
    
    - **Effort:** master
    
??? abstract "Cloudflare Gateway DNS Query Blocked to Malicious Domain"
    
    A DNS query to a domain categorized by Cloudflare Gateway as malicious was blocked by policy.
    
    - **Effort:** master
    
??? abstract "Cloudflare Gateway HTTP File Blocked By Anti-Virus Scan"
    
    Cloudflare Gateway allows admins to enable Anti-Virus (AV) scanning of files that are uploaded or downloaded by users as the file passes through Gateway. AV scanning of files requires organizations to enable Proxy mode under Settings > Network > Layer 7 Firewall. TLS decryption is also recommended to enable inspection of HTTPS traffic.
    
    - **Effort:** advanced
    
??? abstract "Cobalt Strike DNS Beaconing"
    
    Detects suspicious DNS queries known from Cobalt Strike beacons. The threshold is more than 50 suspicious DNS requests to avoid false positives.
    
    - **Effort:** advanced
    
??? abstract "Cobalt Strike HTTP Default GET beaconing"
    
    Detects GET HTTP queries from known Cobalt Strike beacons (source code 4.3)
    
    - **Effort:** advanced
    
??? abstract "Cobalt Strike HTTP Default POST Beaconing"
    
    Detects POST HTTP queries from known Cobalt Strike beacons (source code 4.3)
    
    - **Effort:** advanced
    
??? abstract "Correlation Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 19/07/2023 - major - New regex pattern and new filters.
            
??? abstract "Covenant Default HTTP Beaconing"
    
    Detects potential Covenant communications through the user-agent and specific urls
    
    - **Effort:** intermediate
    
??? abstract "CrowdStrike Falcon Mobile Detection Critical Severity"
    
    CrowdStrike Falcon for Mobile raised an alert with critical severity
    
    - **Effort:** master
    
??? abstract "CrowdStrike Falcon Mobile Detection High Severity"
    
    CrowdStrike Falcon for Mobile raised an alert with high severity
    
    - **Effort:** master
    
??? abstract "CrowdStrike Falcon Mobile Detection Informational Severity"
    
    CrowdStrike Falcon for Mobile raised an alert with informational severity
    
    - **Effort:** master
    
??? abstract "CrowdStrike Falcon Mobile Detection Low Severity"
    
    CrowdStrike Falcon for Mobile raised an alert with low severity
    
    - **Effort:** master
    
??? abstract "CrowdStrike Falcon Mobile Detection Medium Severity"
    
    CrowdStrike Falcon for Mobile raised an alert with medium severity
    
    - **Effort:** master
    
??? abstract "Cryptomining"
    
    Detection of domain names potentially related to cryptomining activities.
    
    - **Effort:** master
    
??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate
    
??? abstract "DNS Tunnel Technique From MuddyWater"
    
    Detecting DNS Tunnel Activity For Muddywater intrusion set. This is the loading of a specific DLL from an Excel macro which is detected.
    
    - **Effort:** elementary
    
??? abstract "Detect requests to Konni C2 servers"
    
    This rule detects requests to Konni C2 servers. These patterns come from an analysis done in 2022, September.
    
    - **Effort:** elementary
    
??? abstract "Dynamic DNS Contacted"
    
    Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.
    
    - **Effort:** master
    
??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced
    
??? abstract "FoggyWeb HTTP Default GET/POST Requests"
    
    Detects GET or POST request pattern observed within the first FoggyWeb campaign detected by Microsoft.
    
    - **Effort:** advanced
    
??? abstract "Google Workspace External Sharing"
    
    Detects a large number of external sharing.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 20/06/2024 - minor - Adding new elements to increase detection.
            
??? abstract "Koadic MSHTML Command"
    
    Detects Koadic payload using MSHTML module
    
    - **Effort:** intermediate
    
??? abstract "LokiBot Default C2 URL"
    
    Detects default C2 URL for trojan LokiBot
    
    - **Effort:** elementary
    
??? abstract "Many Downloads From Several Binaries"
    
    Threat Actors might use all the binaries to download the payload to make sure at least one is present on the target. The prerequisites are to enable monitoring of the connect syscall using Auditbeat.
    
    - **Effort:** advanced
    
??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate
    
??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary
    
??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary
    
??? abstract "Potential LokiBot User-Agent"
    
    Detects potential LokiBot communications through the user-agent
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/08/2023 - minor - Added a condition to only match on internal IP as source
            
??? abstract "Python HTTP Server"
    
    Detects command used to start a Simple HTTP server in Python. Threat actors could use it for data extraction, hosting a webshell or else.
    
    - **Effort:** intermediate
    
??? abstract "Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL"
    
    Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 13/06/2023 - minor - Adding private IPs as sources
            
??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
    
??? abstract "Sliver DNS Beaconing"
    
    Detects suspicious DNS queries known from Sliver beaconing 
    
    - **Effort:** intermediate
    
??? abstract "Suspicious LDAP-Attributes Used"
    
    Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies. Careful as the 5136 is only on domain controllers and needs to be activated through the Group Policy.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious Windows DNS Queries"
    
    Detects a suspicious Windows command-line process making a DNS query via known abuse text paste web services. This is based on Microsoft Windows Sysmon events (Event ID 22).
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 02/08/2023 - minor - Added a new field and filters to reduce false positives.
            
??? abstract "Trellix Network Security Threat Blocked"
    
    Trellix Network Security has detected a malicious traffic and blocked it.
    
    - **Effort:** master
    
??? abstract "Trellix Network Security Threat Notified"
    
    Trellix Network Security has detected a malicious traffic and raised an alert.
    
    - **Effort:** master
    
??? abstract "TrevorC2 HTTP Communication"
    
    Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 
    
    - **Effort:** elementary
    
**Proxy**

??? abstract "Microsoft 365 Authenticated Activity From Tor IP Address"
    
    Detects authenticated Microsoft 365 activity from an IP address associated with Tor.
    
    - **Effort:** advanced
    
??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Added filter to reduce false positives
            
??? abstract "Suspicious Hostname"
    
    Detects suspicious hostnames such as ones with kali in it, to detect kali linux default hosts, but also other hostnames commonly used in attacks. List can be improved according to the environment.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
??? abstract "Suspicious TOR Gateway"
    
    Detects suspicious TOR gateways. Gateways are often used by the victim to pay and decrypt the encrypted files without installing TOR. Tor intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** advanced
    
??? abstract "TOR Usage"
    
    Detects TOR usage, based on the IP address and the destination port (filtered on NTP). TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master
    
??? abstract "TOR Usage Generic Rule"
    
    Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/01/2024 - minor - Modifying filter to improve rule.
        - 22/11/2023 - minor - Adding filter to improve rule.
        - 02/08/2024 - minor - Small pattern to change to match only the real tags related to TOR.
            
**Web Service**

??? abstract "Discord Suspicious Download"
    
    Discord is a messaging application. It allows users to create their own communities to share messages and attachments. Those attachments have little to no overview and can be downloaded by almost anyone, which has been abused by attackers to host malicious payloads.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 05/08/2023 - minor - Added filters for commonly observed files extensions.
            
??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced
    
**Ingress Tool Transfer**

??? abstract "Cloudflare Gateway HTTP File Blocked By Anti-Virus Scan"
    
    Cloudflare Gateway allows admins to enable Anti-Virus (AV) scanning of files that are uploaded or downloaded by users as the file passes through Gateway. AV scanning of files requires organizations to enable Proxy mode under Settings > Network > Layer 7 Firewall. TLS decryption is also recommended to enable inspection of HTTPS traffic.
    
    - **Effort:** advanced
    
??? abstract "Information Stealer Downloading Legitimate Third-Party DLLs"
    
    Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.
    
    - **Effort:** intermediate
    
??? abstract "Network Connection Via Certutil"
    
    Identifies certutil.exe making a network connection. Adversaries could abuse certutil.exe to download a certificate, or malware, from a remote URL. The rule excludes private IP addresses and IPV6. This requires Sysmon logging.
    
    - **Effort:** intermediate
    
??? abstract "Pandemic Windows Implant"
    
    Detects Pandemic Windows Implant through registry keys or specific command lines. Prerequisites: Logging for Registry events is needed, which can be done in the Sysmon configuration (events 12 and 13).
    
    - **Effort:** intermediate
    
??? abstract "Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL"
    
    Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 13/06/2023 - minor - Adding private IPs as sources
            
??? abstract "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
        - 05/08/2024 - major - Edited pattern of the rule to reduce false positives.
            
??? abstract "Suspicious Desktopimgdownldr Execution"
    
    Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Finger Usage"
    
    Detects suspicious aged finger.exe tool execution often used in malware attacks nowadays. An attacker can use finger to silently retrieve a command, a script or a payload from a remote server. For example, the tool Darkfinger-C2 uses this technique to download files from the C2 channel.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Headless Web Browser Execution To Download File"
    
    Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.
    
    - **Effort:** elementary
    
??? abstract "Suspicious URI Used In A Lazarus Campaign"
    
    Detects suspicious requests to a specific URI, usually on an .asp page. The website is often compromised.
    
    - **Effort:** intermediate
    
??? abstract "Suspicious certutil command"
    
    Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.
            
**Data Encoding**

??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate
    
**Traffic Signaling**

??? abstract "Binary List Tcp"
    
    A binary is trying to list TCP connections. The prerequisites are to enable monitoring of the open and openat syscalls using Auditbeat.
    
    - **Effort:** advanced
    
**Remote Access Software**

??? abstract "Antivirus Exploitation Framework Detection"
    
    Detects a highly relevant Antivirus alert that reports an exploitation framework. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
??? abstract "Antivirus Password Dumper Detection"
    
    Detects a highly relevant Antivirus alert that reports a password dumper. This detection relies on Windows Defender events logs. This is based on Windows Defender logs (Event ID 1116 and 1117).
    
    - **Effort:** elementary
    
??? abstract "Antivirus Relevant File Paths Alerts"
    
    Detects an Antivirus alert in a highly relevant file path or with a relevant file name. This is only based on Windows Defender events.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Remote Access Tool Domain"
    
    Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).
    
    - **Effort:** master
    
??? abstract "Remote Monitoring and Management Software - AnyDesk"
    
    Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool AnyDesk.
    
    - **Effort:** master
    
??? abstract "Remote Monitoring and Management Software - Atera"
    
    Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool Atera.
    
    - **Effort:** master
    
??? abstract "Suspicious Activity Using Quick Assist"
    
    Detects when a chat is created (abusing Quick Assist feature) with a user external to the domain, which has been observed as a some phishing attemp by ransomware groups.
    
    - **Effort:** elementary
    
**Dynamic Resolution**

??? abstract "Gatewatcher AionIQ V103 Dga Detect"
    
    Detects when an event related to dga is raised by gatewatcher. An attacker can use this to generate a new domain for C2.
    
    - **Effort:** master
    
**Non-Standard Port**

??? abstract "RDP Port Change Using Powershell"
    
    Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 
    
    - **Effort:** intermediate
    
??? abstract "Suspicious Network Args In Command Line"
    
    Detection on some commonly observed suspicious processes command lines using HTTP schema with port 443.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 10/08/2023 - major - Added a list of suspicious processes to drastically reduce false positives.
            
**Protocol Tunneling**

??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced
    
??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Added filter to reduce false positives
            
??? abstract "Ngrok Process Execution"
    
    Detects possible Ngrok execution, which can be used by attacker for RDP tunneling.
    
    - **Effort:** intermediate
    
??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/06/2023 - minor - Filter some domains to reduce false positives.
        - 19/07/2023 - major - New regex pattern and new filters.
            
??? abstract "SOCKS Tunneling Tool"
    
    Detects the usage of a SOCKS tunneling tool, often used by threat actors. These tools often use the socks5 commandline argument, however socks4 can sometimes be used as well. Unfortunately, socks alone (without any number) triggered too many false positives. 
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 20/06/2024 - minor - Added filter to reduce false positives
            
??? abstract "SSH Port Binding"
    
    When a user uses SSH tunneling in Linux, the sshd process binds sockets to communicate with the client machine via a ssh tunnel. With SSH tunneling, the SSH server can be used as a getaway to access internal systems. The traffic will seem to be coming from the SSH server whereas it only acts as a relay for an attacker. By using this technique, an attacker can successfully bypass external firewall rules. This rule is the most basic one (compared to the other one - SSH Tunnel), however it can detect the -D option in the ssh command if the machine is the client. This rule will detect the port binding (port 6010) when X11 forwarding is used. It will detect -R (server side), -D (client side) -X (server side), -Y (server side) and -L (client side) port binding.
    
    - **Effort:** advanced
    
??? abstract "SSH Tunnel Traffic"
    
    When a user creates and uses a SSH tunnel in Linux, the sshd process opens sockets to communicate with other machines or ports. With SSH tunneling, the SSH server can be used as a getaway to access internal systems. The traffic will seem to be coming from the SSH server whereas it only acts as a relay for an attacker. By using this technique, an attacker can successfully bypass external firewall rules and gain foothold to your network, allowing him to scan,hunt and attack your internal systems. This rule includes a filter on port 22, this filter is created to avoid false positive when a user is connecting via ssh. If you do not use port 22 for your machines, please create an alert filter.
    
    - **Effort:** advanced
    
??? abstract "SSH X11 Forwarding"
    
    When a user creates and uses SSH X11 Forwarding in Linux, the sshd process opens sockets to communicate with the client machine via a ssh tunnel. X11 forwarding is used to deport graphic programs on the client side.
    
    - **Effort:** advanced
    
??? abstract "Socat Relaying Socket"
    
    Socat is a linux tool used to relay local socket or internal network connection, this technics is often used by attacker to bypass security equipment such as firewall
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "Socat Reverse Shell Detection"
    
    Socat is a linux tool used to relay or open reverse shell that is often used by attacker to bypass security equipment.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
            
??? abstract "Venom Multi-hop Proxy agent detection"
    
    Detects Venom Multi-hop Proxy agent.
    
    - **Effort:** intermediate
    
## Exfiltration
**Automated Exfiltration**

??? abstract "AWS CloudTrail RDS Change Master Password"
    
    Detects the change of database master password. It may be a part of data exfiltration.
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail RDS Public DB Restore"
    
    Detects the recovery of a new public database instance from a snapshot. It may be a part of data exfiltration.
    
    - **Effort:** intermediate
    
??? abstract "Python Exfiltration Tools"
    
    Python has some built-in modules or library that could be installed and later be used as exflitration tool by an attacker
    
    - **Effort:** advanced
    
**Scheduled Transfer**

??? abstract "Gatewatcher AionIQ V103 Malicious Powershell Detect"
    
    Detects malicious powershell by Gatewatcher V103.
    
    - **Effort:** master
    
**Exfiltration Over C2 Channel**

??? abstract "Claroty xDome Network Threat Detection Alert"
    
    Claroty xDome has raised an network threat detection alert.
    
    - **Effort:** master
    
??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced
    
??? abstract "Forcepoint Secure Web Gateway Compromised Websites"
    
    Forcepoint Secure Web Gateway has detected an access to an IP/domain tagged as compromised. Even if it has been blocked, it could be interesting to investigate the source asset.
    
    - **Effort:** master
    
??? abstract "Forcepoint Secure Web Gateway Malicious Websites"
    
    Forcepoint Secure Web Gateway has detected an access to an IP/domain tagged as malicious. Even if it has been blocked, it could be interesting to investigate the source asset.
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ Malware Alert"
    
    Forward malware information reported by Gatewatcher AionIQ  
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ Network Alert"
    
    Forward network alerts reported by Gatewatcher AionIQ  
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ V103 Beacon Detect"
    
    Detects a suspicious beacon.
    
    - **Effort:** master
    
??? abstract "Gatewatcher AionIQ V103 Sigflow Alert"
    
    Detects a sigflow alert by Gatewatcher AionIQ V103.
    
    - **Effort:** master
    
??? abstract "Netsh Port Forwarding"
    
    Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 15/02/2024 - minor - Added filter to reduce false positives
            
??? abstract "Netskope Alert"
    
    Forward alerts reported by Netskope.  
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 28/03/2024 - minor - Rule effort was updated to master
            
??? abstract "Remote File Copy"
    
    Detects the use of remote tools that copy files from or to remote systems
    
    - **Effort:** master
    
??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
    
**Exfiltration Over Alternative Protocol**

??? abstract "1Password EPM Share Externally"
    
    Detects when an item from 1Password is shared externally.
    
    - **Effort:** master
    
??? abstract "DNS Exfiltration and Tunneling Tools Execution"
    
    Well-known DNS exfiltration tools execution
    
    - **Effort:** intermediate
    
??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/02/2024 - minor - enforce detection by adding tag
            
??? abstract "Exfiltration Domain In Command Line"
    
    Detects commands containing a domain linked to http exfiltration.
    
    - **Effort:** intermediate
    
??? abstract "Potential DNS Tunnel"
    
    Detects domain name which is longer than 95 characters. Long domain names are distinctive of DNS tunnels.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 22/06/2023 - minor - Filter some domains to reduce false positives.
        - 19/07/2023 - major - New regex pattern and new filters.
            
??? abstract "Powershell UploadString Function"
    
    Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host.
    
    - **Effort:** intermediate
    
??? abstract "TUN/TAP Driver Installation"
    
    Detects the installation of the TUN or TAP driver service, this activity could be related to data exfiltration using tunneling techniques. The TUN/TAP Windows Adapter is a network driver that enables some VPN providers to facilitate a VPN connection to their server. TUN/TAP driver is only used by specific VPNs (e.g. OpenVPN, Wireguard), not by thoses based on IKE protocols (e.g. IPsec).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Transfer Data to Cloud Account**

??? abstract "AWS CloudTrail EC2 VM Export Failure"
    
    Detects attempt to export an AWS EC2 instance. A VM Export might indicate an attempt to extract information from an instance.
    
    - **Effort:** intermediate
    
??? abstract "Google Cloud Audit Logs Drive Ownership Transferred"
    
    Detects when Drive/Docs user files ownership is transferred. The legit use case is when a user is being removed, but this could also be abused by an attacker for exfiltration.
    
    - **Effort:** advanced
    
**Exfiltration Over Web Service**

??? abstract "Exfiltration Domain"
    
    Detects traffic toward a domain flagged as a possible exfiltration vector.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 29/02/2024 - minor - enforce detection by adding tag
            
??? abstract "Exfiltration Domain In Command Line"
    
    Detects commands containing a domain linked to http exfiltration.
    
    - **Effort:** intermediate
    
??? abstract "Outgoing Bytes Peak"
    
    Spots outgoing bytes traffic peak to detect a data exfiltration.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 28/05/2024 - major - On Fortinet Fortigate intakes, events other than 0000000013 are now ignored.
            
??? abstract "Powershell UploadString Function"
    
    Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host.
    
    - **Effort:** intermediate
    
??? abstract "Rclone Process"
    
    Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.
    
    - **Effort:** advanced
    
    - **Changelog:**
    
        - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
        - 05/08/2024 - major - Edited pattern of the rule to reduce false positives.
            
## Impact
**Data Destruction**

??? abstract "AWS CloudTrail ECS Cluster Deleted"
    
    Detects when an attacker is destroying an AWS ECS Cluster
    
    - **Effort:** intermediate
    
??? abstract "AWS CloudTrail RDS DB Cluster/Instance Deleted"
    
    Detects when an attacker is destroying a RDS Cluster or Instance
    
    - **Effort:** advanced
    
??? abstract "Backup Catalog Deleted"
    
    The rule detects when the Backup Catalog has been deleted. It means the administrators will not be able to access any backups that were created earlier to perform recoveries. This is often being done using the wbadmin.exe tool.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate
    
??? abstract "Secure Deletion With SDelete"
    
    Detects renaming of file while deletion with SDelete tool. SDelete is a tool that permits to securely delete files by overwriting them (no recovery possible). Few threat actors are using it to delete traces of their malware.
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            
**Data Encrypted for Impact**

??? abstract "Gatewatcher AionIQ V103 Ransomware Detect"
    
    Detects when a ransomware is detected by gatewatcherV103.
    
    - **Effort:** master
    
??? abstract "Suncrypt Parameters"
    
    Detects SunCrypt ransomware's parameters, most of which are unique.
    
    - **Effort:** elementary
    
??? abstract "Varonis Many File Created and Deleted"
    
    This rule identifies a high number of file created and deleted on the same host. It is a typical ransomware behavior.
    
    - **Effort:** master
    
??? abstract "Varonis Massive Dowloads By A Single User"
    
    This rule identifies a high number of File dowloaded by a single user.
    
    - **Effort:** master
    
**Service Stop**

??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate
    
??? abstract "Correlation Multi Service Disable"
    
    The rule detects a high number of services stopped or de-activated in a short period of time.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/08/2024 - minor - Adding a space to reduce false positives.
            
??? abstract "Disabled Service"
    
    Service disabling can be abused by attacker to deny security mecanisms (eg: firewall, EDR, ect) and it is also often used by cryptominer to exploit as much RAM & CPU as possible on infected host. The prerequisites are to enable monitoring of the truncate, rename and unlink syscalls using Auditbeat.
    
    - **Effort:** advanced
    
**Inhibit System Recovery**

??? abstract "Commonly Used Commands To Stop Services And Remove Backups"
    
    Detects specific commands used regularly by ransomwares to stop services or remove backups
    
    - **Effort:** intermediate
    
??? abstract "Inhibit System Recovery Deleting Backups"
    
    Detects adversaries attempts to delete backups or inhibit system recovery. This rule relies on differents known techniques using Windows events logs from Sysmon (ID 1), and PowerShell (ID 4103, 4104).
    
    - **Effort:** intermediate
    
    - **Changelog:**
    
        - 31/01/2024 - minor - Improve selection filter
            
??? abstract "Stop Backup Services"
    
    Detects adversaries attempts to stop backups services or disable Windows previous files versions feature. This could be related to ransomware operators or legit administrators. This rule relies Windows command line logging and registry logging, and PowerShell (ID 4103, 4104).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
        - 16/05/2024 - minor - add pattern to extend and improve detection
            
??? abstract "Suncrypt Parameters"
    
    Detects SunCrypt ransomware's parameters, most of which are unique.
    
    - **Effort:** elementary
    
**Network Denial of Service**

??? abstract "Anomaly CloudFlare DDoS"
    
    Detects anomaly on volume of DNS events from CloudFlare logs.
    
    - **Effort:** master
    
**Endpoint Denial of Service**

??? abstract "Audit CVE Event"
    
    Detects events generated by Windows to indicate the exploitation of a known vulnerability.
    
    - **Effort:** elementary
    
    - **Changelog:**
    
        - 15/07/2024 - major - review filter and improve similarity
            
**System Shutdown/Reboot**

??? abstract "Rebooting"
    
    Detects when forcing a computer to shutdown.
    
    - **Effort:** master
    
**Account Access Removal**

??? abstract "Computer Account Deleted"
    
    Detects computer account deletion.
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "Google Workspace Admin Deletion"
    
    Detects when an admin is deleted or when his role is unassigned.
    
    - **Effort:** master
    
??? abstract "Google Workspace User Deletion"
    
    Detects when an user is deleted.
    
    - **Effort:** master
    
??? abstract "Google Workspace User Suspended"
    
    Detects when an user is suspended. An attacker can use this to remove an account used during the intrusion.
    
    - **Effort:** master
    
??? abstract "Jumpcloud Account Locked"
    
    A user has been locked on Jumpcloud portal.
    
    - **Effort:** intermediate
    
??? abstract "Okta User Account Locked"
    
    An user has been locked in Okta.
    
    - **Effort:** intermediate
    
??? abstract "Privileged AD Builtin Group Modified"
    
    Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 10/07/2023 - minor - Added AD groups and change to effort master.
        - 26/03/2024 - major - Rule's pattern field changed
            
??? abstract "User Account Deleted"
    
    Detects local user deletion
    
    - **Effort:** master
    
    - **Changelog:**
    
        - 04/04/2024 - major - Rule's pattern field changed
            