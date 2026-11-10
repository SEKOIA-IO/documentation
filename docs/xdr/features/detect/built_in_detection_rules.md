# Built-in detection rules

Sekoia.io provides built-in detection rules to illuminate intrusions, adversarial behaviours and suspicious activity escalation chains so you can immediately take steps to remediate. Built-in rules can be customized to your context and according to your security posture.

Please check the [dedicated FAQ page](../../FAQ/intelligence/Detection_qa.md) related to detection rule strategy.

For Windows-related rules, Sekoia.io automatically produces [this regularly updated list](built_in_detection_rules_eventids.md) of the needed EventIDs by rule but also globally as some statistics are provided.

<!-- include:_shared_content/operations_center/detection/generated/built_in_rules_do_not_edit_manually.md -->
Rules catalog includes **1124 built-in detection rules** ([_last update on 2026-11-09_](rules_changelog.md)).
## Reconnaissance
**Gather Victim Identity Information**

<details>
<summary>Anomaly Possible Sysvol Dump</summary>


The rule detects abnormally high access to sysvol files.

- **Effort:** master

- **Changelog:**

    - 08/04/2024 - minor - change field name on query
    - 13/06/2024 - minor - Adding fields to be displayed in alerts.

</details>
            
<details>
<summary>Flare Events Critical Severity Threat Exposure</summary>


Detects a high critical Flare exposure event from clear, deep, or dark web monitoring. This indicates a critical-risk threat indicator that requires rapid triage.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events High Severity Threat Exposure</summary>


Detects a high severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Informational Severity Threat Exposure</summary>


Detects a informational severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Leaked Credential With Password Exposure</summary>


Detects leaked credential events where a password is explicitly present in the exposure record, indicating elevated risk of account takeover.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Low Severity Threat Exposure</summary>


Detects a low severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Medium Severity Threat Exposure</summary>


Detects a medium severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
**Gather Victim Network Information**

<details>
<summary>ACLight Discovering Privileged Accounts</summary>


Detects use of ACLight tool. This tool aims to discover privileged accounts by scanning the network.

- **Effort:** advanced

</details>
    
<details>
<summary>Adidnsdump Enumeration</summary>


Detects use of the tool adidnsdump for enumeration and discovering DNS records.

- **Effort:** advanced

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Network Behavior Analytics High</summary>


Detects when network behavior analytics were requested with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Network Behavior Analytics Low</summary>


Detects when network behavior analytics were requested with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Network Behavior Analytics Medium</summary>


Detects when network behavior analytics were requested with a medium severity.

- **Effort:** master

</details>
    
<details>
<summary>Internet Scanner</summary>


Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP. This could be a very noisy rule, so be careful to check your detection perimeter before activation.

- **Effort:** master

- **Changelog:**

    - 28/04/2023 - minor - Support for standard ECS FW fields

</details>
            
<details>
<summary>Internet Scanner Target</summary>


Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address. This could be a very noisy rule, so be careful to check your detection perimeter before activation.

- **Effort:** master

- **Changelog:**

    - 28/04/2023 - minor - Support for standard ECS FW fields

</details>
            
<details>
<summary>Microsoft Windows Active Directory Module Commandlets</summary>


Detects use of commandlets linked to the AD Module.

- **Effort:** advanced

- **Changelog:**

    - 30/01/2025 - minor - Adding filters to reduce false positives.

</details>
            
<details>
<summary>Remote System Discovery Via Telnet</summary>


Detects use of the protocol telnet to access information.

- **Effort:** advanced

</details>
    
<details>
<summary>System Network Connections Discovery</summary>


Detects system network connections discovery via powershell and cmd.

- **Effort:** advanced

</details>
    
**Gather Victim Org Information**

<details>
<summary>Flare Events Suspicious Phishing Dark Web Chatter</summary>


Detects a Flare chat message event flagged with a sensitive content classification, indicating threat actor chatter on illicit channels referencing phishing material tied to the monitored organization.

- **Effort:** master

</details>
    
**Gather Victim Host Information**

<details>
<summary>DNS Query For Iplookup</summary>


Detects dns query of observables tagged as iplookup.

- **Effort:** master

</details>
    
<details>
<summary>Wmic Suspicious Commands</summary>


Detects suspicious commands used by the process wmic to get informations on the system.

- **Effort:** advanced

</details>
    
**Active Scanning**

<details>
<summary>Anomaly Fortigate IPS Alert Peak</summary>


The rule detects abnormally high number of Fortigate IPS alert

- **Effort:** master

</details>
    
<details>
<summary>Bitsight SPM Material Vulnerability</summary>


Bitsight SPM has raised a material vulnerability finding

- **Effort:** master

</details>
    
<details>
<summary>Bitsight SPM Minor Vulnerability</summary>


Bitsight SPM has raised a minor vulnerability finding

- **Effort:** master

</details>
    
<details>
<summary>Bitsight SPM Moderate Vulnerability</summary>


Bitsight SPM has raised a moderate vulnerability finding

- **Effort:** master

</details>
    
<details>
<summary>Bitsight SPM Severe Vulnerability</summary>


Bitsight SPM has raised a severe vulnerability finding

- **Effort:** master

</details>
    
<details>
<summary>Burp Suite Tool Detected</summary>


Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner).

- **Effort:** intermediate

</details>
    
<details>
<summary>Cloudflare HTTP Requests Rule Block Or Drop</summary>


Detects when one of Cloudflare Web Application Firewall (WAF) Managed rule blocked or dropped an HTTP request. It requires only Cloudflare HTTP requests logs.

- **Effort:** master

</details>
    
<details>
<summary>Cloudflare WAF Correlation Alerts</summary>


Detection of multiple alerts (more than 5) triggered by the same source by Cloudflare detection rules

- **Effort:** master

- **Changelog:**

    - 28/03/2024 - minor - Rule effort was updated to master

</details>
            
<details>
<summary>Correlation Fortigate Multi Alert From One Internal Ip</summary>


This rule detect an internal asset that targets a destination IP address with several threat

- **Effort:** master

</details>
    
<details>
<summary>Correlation Fortigate Multi Dest From One Internal Ip</summary>


This rule detect an internal asset that targets several destination IP address with the same threat

- **Effort:** master

</details>
    
<details>
<summary>ExtraHop Reveal(x) 360 Intrusion Detection Critical Severity</summary>


ExtraHop Reveal(x) 360 raised an intrusion detection alert with critical severity.

- **Effort:** master

</details>
    
<details>
<summary>ExtraHop Reveal(x) 360 Intrusion Detection High Severity</summary>


ExtraHop Reveal(x) 360 raised an intrusion detection alert with high severity.

- **Effort:** master

</details>
    
<details>
<summary>Fastly Next-Gen WAF Audit Threat Alert</summary>


Forward a threat detection made by Fastly Next-Gen WAF Audit Logs

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Fortigate IPS Critical Alert</summary>


Fortigate intrusion detection alert with critical severity.

- **Effort:** master

</details>
    
<details>
<summary>Fortigate IPS High Severity Alert</summary>


Fortigate intrusion detection alert with high severity.

- **Effort:** master

</details>
    
<details>
<summary>Internet Scanner</summary>


Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP. This could be a very noisy rule, so be careful to check your detection perimeter before activation.

- **Effort:** master

- **Changelog:**

    - 28/04/2023 - minor - Support for standard ECS FW fields

</details>
            
<details>
<summary>Internet Scanner Target</summary>


Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address. This could be a very noisy rule, so be careful to check your detection perimeter before activation.

- **Effort:** master

- **Changelog:**

    - 28/04/2023 - minor - Support for standard ECS FW fields

</details>
            
<details>
<summary>Varonis Data Security Intrusion Detection High Severity Alert</summary>


Varonis Data Security has raised a high severity alert for its intrusion detection engine.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Intrusion Detection Low Severity Alert</summary>


Varonis Data Security has raised a low severity alert for its intrusion detection engine.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Intrusion Detection Medium Severity Alert</summary>


Varonis Data Security has raised a medium severity alert for its intrusion detection engine.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Veeam Backup & Replication Malware Detection</summary>


Veeam Backup & Replication has detected some malware related activity

- **Effort:** master

- **Changelog:**

    - 13/08/2024 - major - Restrict to only one type of event following customer feedback

</details>
            
<details>
<summary>WAF Block Rule</summary>


Detects when one of WAF rule blocked an HTTP request. This rule often needs fine tuning according to the environment.

- **Effort:** master

- **Changelog:**

    - 15/11/2023 - minor - Adding support for Ubika
    - 04/03/2026 - major - Removing intakes from the rule to make it more generic and match all WAF products. The sources and description fields were updated accordingly.

</details>
            
<details>
<summary>WAF Correlation Block Multiple Destinations</summary>


Detection of multiple block actions (more than 10) by the Web Application Firewall (WAF) triggered by the same source to mutliple destinations

- **Effort:** master

- **Changelog:**

    - 28/03/2024 - minor - Rule effort was updated to master

</details>
            
<details>
<summary>WAF Correlation Block actions</summary>


Detection of multiple block actions (more than 30) triggered by the same source by WAF detection rules

- **Effort:** master

- **Changelog:**

    - 28/03/2024 - minor - Rule effort was updated to master

</details>
            
**Phishing for Information**

<details>
<summary>Flare Events Suspicious Phishing Dark Web Chatter</summary>


Detects a Flare chat message event flagged with a sensitive content classification, indicating threat actor chatter on illicit channels referencing phishing material tied to the monitored organization.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Active CTI High</summary>


Detects whan an event related to CTI is raised by Gatewatcher V103 with a high severity. An attacker may be gathering information with this event.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 06/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Active CTI Low</summary>


Detects when an event related to CTI is raised by Gatewatcher V103 with a low severity. An attacker may be gathering information with this event.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Active CTI Medium</summary>


Detects when an event related to CTI is raised by Gatewatcher V103 with a medium severity. An attacker may be gathering information with this event.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Retrohunt High</summary>


Detects when a retrohunt event is raised by GatewatcherV103 with a high severity.

- **Effort:** master

- **Changelog:**

    - 30/06/2025 - minor - Changing similarity on threat name.
    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Retrohunt Low</summary>


Detects when a retrohunt event with a low severity is raised by GatewatcherV103.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Retrohunt Medium</summary>


Detects when a retrohunt event with a medium severity is raised by GatewatcherV103.

- **Effort:** master

</details>
    
## Resource Development
**Acquire Infrastructure**

<details>
<summary>Login Brute-Force Successful On ArubaOS Switch</summary>


A user has attempted to login several times (brute-force) on ArubaOS switch and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On AzureAD From Single IP Address</summary>


A user has attempted to login several times (brute-force) on AzureAD and succeeded to login, all from the same source IP address and in a timerange of 5 minutes.

- **Effort:** advanced

- **Changelog:**

    - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    - 16/08/2024 - minor - The error code 50078 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    - 14/10/2024 - minor - The error codes 70043, 50173, 70008, 700082, 9002341 have been excluded as they are not related to login failures that we want to detect and caused several false positives.
    - 28/11/2024 - minor - Adding error codes as filters to reduce false positives.
    - 25/02/2026 - minor - Adding error code 500011 as filters to reduce false positives.
    - 01/06/2026 - minor - Adding error code as filters to reduce false positives.

</details>
            
<details>
<summary>Login Brute-Force Successful On Jumpcloud Portal</summary>


A user has attempted to login several times (brute-force) on Jumpcloud Portal and succeeded to login.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Login Brute-Force Successful On Jumpcloud Workstation</summary>


A user has attempted to login several times (brute-force) on Jumpcloud monitored workstations (windows, linux, mac) and succeeded to login.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Login Brute-Force Successful On Okta</summary>


A user has attempted to login several times (brute-force) on Okta and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On Rubycat PROVE IT</summary>


A user has attempted to login several times (brute-force) through Rubycat PROVE IT protected devices and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On WatchGuard Firebox</summary>


A user has attempted to login several times (brute-force) on WatchGuard Firebox and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Abnormal Token</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Anonymous IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** advanced

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Impossible Travel</summary>


Detects when Microsoft Entra ID (Azure AD) identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration
    - 29/10/2026 - minor - Rule riskEventType updated following Microsoft changes, the rule is now properly working again.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Leaked Credentials</summary>


Detects when Microsoft Entra ID (Azure AD) identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Login Failed Brute-Force From Single IP Address</summary>


A user has attempted to login several times (brute-force) on AzureAD and failed every time, all from the same source IP address and in a timerange of 5 minutes.

- **Effort:** advanced

- **Changelog:**

    - 22/03/2024 - major - More precise list of error codes to reduce false positives.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Malicious IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 16/07/2024 - minor - Change similarity strategy.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Password Spray</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Sign-in From Unlikely Country</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Successful Password Spraying From Single IP Address</summary>


An IP address performed several failed logins on multiple users to then have a successful login on one of them. Note that even if the sign-in was blocked by MFA (error 50074/50076/50158) or conditional access (error 50097/53003), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.

- **Effort:** advanced

- **Changelog:**

    - 22/03/2024 - major - More precise list of error codes for success and failure to reduce false positives.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious Browser</summary>


Detects when Microsoft Entra ID (Azure AD) identifies suspicious sign-in activity across multiple tenants from different countries in the same browser. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a suspicious IP address. An IP address is considered suspicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious Inbox Forwarding</summary>


Detects when Microsoft Entra ID (Azure AD) identifies suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Threat Intelligence</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a sign-in activity that is unusual for the given user or is consistent with known attack patterns based on Microsoft's internal and external threat intelligence sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Token Issuer Anomaly</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that The SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Unfamiliar Features</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins with characteristics that deviate from past sign-in properties. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 20/03/2025 - major - Change effort level
    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Okta MFA Brute-Force Successful</summary>


A user has attempted to login several times (brute-force) on Okta and succeeded to login by spamming MFA.

- **Effort:** advanced

</details>
    
**Compromise Infrastructure**

<details>
<summary>Login Brute-Force Successful On ArubaOS Switch</summary>


A user has attempted to login several times (brute-force) on ArubaOS switch and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On AzureAD From Single IP Address</summary>


A user has attempted to login several times (brute-force) on AzureAD and succeeded to login, all from the same source IP address and in a timerange of 5 minutes.

- **Effort:** advanced

- **Changelog:**

    - 23/03/2023 - minor - The error code 50076 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    - 16/08/2024 - minor - The error code 50078 has been excluded as it is not a specific error code related to a login failure that we want to detect and caused several false positives.
    - 14/10/2024 - minor - The error codes 70043, 50173, 70008, 700082, 9002341 have been excluded as they are not related to login failures that we want to detect and caused several false positives.
    - 28/11/2024 - minor - Adding error codes as filters to reduce false positives.
    - 25/02/2026 - minor - Adding error code 500011 as filters to reduce false positives.
    - 01/06/2026 - minor - Adding error code as filters to reduce false positives.

</details>
            
<details>
<summary>Login Brute-Force Successful On Jumpcloud Portal</summary>


A user has attempted to login several times (brute-force) on Jumpcloud Portal and succeeded to login.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Login Brute-Force Successful On Jumpcloud Workstation</summary>


A user has attempted to login several times (brute-force) on Jumpcloud monitored workstations (windows, linux, mac) and succeeded to login.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Login Brute-Force Successful On Okta</summary>


A user has attempted to login several times (brute-force) on Okta and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On Rubycat PROVE IT</summary>


A user has attempted to login several times (brute-force) through Rubycat PROVE IT protected devices and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Login Brute-Force Successful On WatchGuard Firebox</summary>


A user has attempted to login several times (brute-force) on WatchGuard Firebox and succeeded to login.

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Abnormal Token</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that there are abnormal characteristics in the token such as an unusual token lifetime or a token that is played from an unfamiliar location. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Anonymous IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** advanced

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Impossible Travel</summary>


Detects when Microsoft Entra ID (Azure AD) identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration
    - 29/10/2026 - minor - Rule riskEventType updated following Microsoft changes, the rule is now properly working again.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Leaked Credentials</summary>


Detects when Microsoft Entra ID (Azure AD) identifies that the user's valid credentials have been leaked. This sharing is typically done by posting publicly on the dark web, paste sites, or by trading and selling the credentials on the black market. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Login Failed Brute-Force From Single IP Address</summary>


A user has attempted to login several times (brute-force) on AzureAD and failed every time, all from the same source IP address and in a timerange of 5 minutes.

- **Effort:** advanced

- **Changelog:**

    - 22/03/2024 - major - More precise list of error codes to reduce false positives.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Malicious IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a malicious IP address. An IP address is considered malicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 16/07/2024 - minor - Change similarity strategy.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Password Spray</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that multiple usernames are attacked using common passwords in a unified brute force manner to gain unauthorized access. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Sign-in From Unlikely Country</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins originating from geographically distant locations, where at least one of the locations may also be atypical for the user, given past behavior. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Successful Password Spraying From Single IP Address</summary>


An IP address performed several failed logins on multiple users to then have a successful login on one of them. Note that even if the sign-in was blocked by MFA (error 50074/50076/50158) or conditional access (error 50097/53003), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.

- **Effort:** advanced

- **Changelog:**

    - 22/03/2024 - major - More precise list of error codes for success and failure to reduce false positives.

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious Browser</summary>


Detects when Microsoft Entra ID (Azure AD) identifies suspicious sign-in activity across multiple tenants from different countries in the same browser. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious IP</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a suspicious IP address. An IP address is considered suspicious based on high failure rates because of invalid credentials received from the IP address or other IP reputation sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Suspicious Inbox Forwarding</summary>


Detects when Microsoft Entra ID (Azure AD) identifies suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Threat Intelligence</summary>


Detects when Microsoft Entra ID (Azure AD) identifies a sign-in activity that is unusual for the given user or is consistent with known attack patterns based on Microsoft's internal and external threat intelligence sources. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft Entra ID (Azure AD) Token Issuer Anomaly</summary>


Detects when Microsoft Entra ID (Azure AD) indicates that The SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Unfamiliar Features</summary>


Detects when Microsoft Entra ID (Azure AD) identifies sign-ins with characteristics that deviate from past sign-in properties. To use this feature, you must have an Microsoft Entra ID (Azure AD) Premium P2 license (https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview-identity-protection).

- **Effort:** master

- **Changelog:**

    - 20/03/2025 - major - Change effort level
    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Okta MFA Brute-Force Successful</summary>


A user has attempted to login several times (brute-force) on Okta and succeeded to login by spamming MFA.

- **Effort:** advanced

</details>
    
**Compromise Accounts**

<details>
<summary>Cisco Identity Services Engine Configuration Changed</summary>


Cisco Identity Services Engine (ISE) has detected a device configuration changed (Added, Changed or Deleted). This should be reviewed in order to check if this an expected admin action.

- **Effort:** master

</details>
    
<details>
<summary>Correlation Jumpcloud User Logged In From Multiple Countries</summary>


Detection of login events from multiple countries on Jumpcloud portal.

- **Effort:** intermediate

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Microsoft Defender for Office 365 High Severity AIR Alert</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a High severity alert triggers an automated investigation, such as when a potentially malicious URL click was detected, or when a user is restricted from sending email.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Microsoft Defender for Office 365 Medium Severity AIR Alert</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Medium severity alert triggers an automated investigation, such as when suspicious email sending patterns are detected from an account.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Okta Suspicious Use of a Session Cookie</summary>


Suspicious use of a session cookie by detecting multiple client values (IP, User Agent, etc.) changing for the same Device Token associated with a specific user.

- **Effort:** intermediate

- **Changelog:**

    - 03/03/2025 - minor - Improve detection pattern group-by, value field and timespan, update rule name

</details>
            
<details>
<summary>Okta User Logged In From Multiple Countries</summary>


Detection of login events from multiple countries.

- **Effort:** intermediate

- **Changelog:**

    - 24/09/2025 - minor - Improving selection in order to reduce false positives

</details>
            
<details>
<summary>Okta User Logged In Multiple Applications</summary>


Detection of login events on multiple application.

- **Effort:** intermediate

- **Changelog:**

    - 07/08/2023 - major - Switching type from event_count to value_count | Adding Target in order to match only on different Apps

</details>
            
<details>
<summary>Varonis Data Security Email High Severity Alert</summary>


Varonis Data Security has raised a high severity alert related to a supervised email account.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Email Medium Severity Alert</summary>


Varonis Data Security has raised a medium severity alert related to a supervised email account.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Network High Severity Alert</summary>


Varonis Data Security has raised a high severity  alert related to a network rule

- **Effort:** master

- **Changelog:**

    - 06/10/2025 - minor - Update similarity strategy for more granularity
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Network Low Severity Alert</summary>


Varonis Data Security has raised a low severity alert related to a network rule

- **Effort:** master

- **Changelog:**

    - 14/05/2025 - major - Fix pattern where severity level was missing
    - 06/10/2025 - minor - Update similarity strategy for more granularity
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>Varonis Data Security Network Medium Severity Alert</summary>


Varonis Data Security has raised a medium severity alert related to a network rule

- **Effort:** master

- **Changelog:**

    - 06/10/2025 - minor - Update similarity strategy for more granularity
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
**Obtain Capabilities**

<details>
<summary>Cyberwatch Detection Critical Vulnerability</summary>


Cyberwatch Detection has detected an asset with a critical vulnerability 

- **Effort:** master

</details>
    
<details>
<summary>ESET Protect Vulnerability Exploitation Attempt</summary>


Detects when an attempt is made to exploit a vulnerability.

- **Effort:** master

</details>
    
<details>
<summary>Elevated Msiexec Via Repair Functionality</summary>


Detects when msiexec.exe is used with the repair functionality. The process gains elevated privileges. Attackers can use this to exploit the CVE-2024-38014.

- **Effort:** master

</details>
    
<details>
<summary>Elevated Shell Launched By Browser</summary>


Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.

- **Effort:** master

</details>
    
<details>
<summary>Privilege Escalation Awesome Scripts (PEAS)</summary>


Detect PEAS privileges escalation scripts and binaries

- **Effort:** elementary

</details>
    
## Initial Access
**Valid Accounts**

<details>
<summary>Account Added To A Security Enabled Group</summary>


Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - add similarity strategy

</details>
            
<details>
<summary>Account Removed From A Security Enabled Group</summary>


Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - Add similarity strategy

</details>
            
<details>
<summary>Account Tampering - Suspicious Failed Logon Reasons</summary>


This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.

- **Effort:** advanced

- **Changelog:**

    - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Admin User RDP Remote Logon</summary>


Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Authentication Impossible Travel</summary>


Detects impossible travel when performing authentication from a source IP address, grouped by user name. This could require some alert filtering for some user generic accounts, and known IP address range. Microsoft / Office 365 format is not covered by this rule.

- **Effort:** master

- **Changelog:**

    - 27/07/2024 - major - review filter to avoid false positives
    - 30/08/2024 - minor - improve filter to avoid false positives
    - 30/01/2025 - major - Pattern rework with ECS fields only and simple authentication success use case
    - 04/02/2025 - major - Excluding Microsoft 365 format to avoid false positives
    - 14/08/2025 - major - Excluding Wiz Audit Logs format to avoid false positives
    - 29/10/2026 - major - Excluding Entra ID following parser changes to avoid false positives. A dedicated rule for Entra ID exists and is called "Microsoft Entra ID (Azure AD) Impossible Travel".

</details>
            
<details>
<summary>Broadcom Edge Secure Web Gateway High Threat</summary>


Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.

- **Effort:** master

</details>
    
<details>
<summary>Brute-Force On Fortinet Firewall Login</summary>


Spots many failed attempts to log on an administration interface.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and add intake field format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Denied Access To Remote Desktop</summary>


Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.

- **Effort:** intermediate

- **Changelog:**

    - 19/10/2023 - minor - Minor change in selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Dscl Authonly</summary>


Detects the use of the command dscl with authonly used to verify the password of a user and for authentification. An attacker can abuse this command to gain credentials.

- **Effort:** advanced

</details>
    
<details>
<summary>Enable Root Account With Dsenableroot</summary>


Detects when root is enabled. Attackers can use this as a mean of persistence since root is disabled by default.

- **Effort:** elementary

</details>
    
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Flare Events Critical Severity Threat Exposure</summary>


Detects a high critical Flare exposure event from clear, deep, or dark web monitoring. This indicates a critical-risk threat indicator that requires rapid triage.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events High Severity Threat Exposure</summary>


Detects a high severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Informational Severity Threat Exposure</summary>


Detects a informational severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Leaked Credential With Password Exposure</summary>


Detects leaked credential events where a password is explicitly present in the exposure record, indicating elevated risk of account takeover.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Low Severity Threat Exposure</summary>


Detects a low severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Medium Severity Threat Exposure</summary>


Detects a medium severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Fortigate Firewall Successful External Login</summary>


Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Google Cloud Audit Logs Account Suspended</summary>


Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Added</summary>


Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Authorized</summary>


Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.

- **Effort:** master

</details>
    
<details>
<summary>Google Cloud Audit Logs Attack Warning</summary>


Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Workspace Account Warning</summary>


Detects a suspicious login, leaked password, or account disabled following suspicious activity.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace Admin Creation</summary>


Detects when an admin is created or when his role is changed.

- **Effort:** master

- **Changelog:**

    - 22/05/2024 - minor - Adding new element to increase detection.

</details>
            
<details>
<summary>Google Workspace Suspicious Login</summary>


Detects a suspicious login reported by google.

- **Effort:** master

</details>
    
<details>
<summary>Login Brute-Force On Fortinet Firewall From Internet</summary>


Detects successful access to administration console of a firewall after several failure from Internet.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only and intake format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Login Brute-Force On FreeRadius</summary>


A user has attempted to login several times (brute-force) with error then one success.

- **Effort:** intermediate

</details>
    
<details>
<summary>Login Brute-Force On Sekoia.io</summary>


Detects successful access to Sekoia.io after several failure.

- **Effort:** intermediate

- **Changelog:**

    - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.

</details>
            
<details>
<summary>Microsoft 365 Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)

- **Effort:** master

</details>
    
<details>
<summary>Netskope Admin Audit High Severity</summary>


Audit events detection for admin activites that differ from authentications, with high severity level according to Netskope.

- **Effort:** master

- **Changelog:**

    - 29/01/2025 - minor - Rework pattern for high severity events only and filter out authentication events.
    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Detected</summary>


Netskope identified a malware with a high severity (excluding Patient Zero here)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Patient Zero Detected</summary>


Netskope identified a malware as Patient Zero.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Potential Brute Force On Protected Applications</summary>


Detects potential brute force on Netskope protected applications with more than 10 failures in 5 minutes for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute Force On Protected Applications</summary>


Detects successful brute force on Netskope protected applications after more than 5 failures in 5 minutes and one success for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute-Force On Management Console</summary>


Detects successful access to Netskope management console after more than 10 failures in 5 minutes for the same user name.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Web Isolation On Suspicious Domain</summary>


Netskope identified a suspicious domain and triggered web sandboxing (RBI)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Okta Access To Admin Console Denied</summary>


Detects when an attempt was made to access the Okta Admin Console from an interactive user account but failed.

- **Effort:** master

</details>
    
<details>
<summary>Okta Many Passwords Reset Attempt</summary>


This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Suspicious Activity Reported</summary>


Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Unauthorized Access to App</summary>


An user tries to access an unauthorized application.

- **Effort:** master

</details>
    
<details>
<summary>User Added To Admin Group Via Cmd</summary>


Detects the use of different commands to add a user to an admin group.

- **Effort:** advanced

</details>
    
<details>
<summary>User Added to Local Administrators</summary>


Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 04/04/2024 - major - Rule's pattern field changed
    - 01/06/2026 - major - selection improvements to better align with the detection objective

</details>
            
**Replication Through Removable Media**

<details>
<summary>External Disk Drive Or USB Storage Device</summary>


Detects external diskdrives or plugged in USB device.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**External Remote Services**

<details>
<summary>Anomaly New PowerShell Remote Session</summary>


Detects when PowerShell remote sessions are created in a short amount of time.

- **Effort:** master

- **Changelog:**

    - 11/06/2024 - minor - Adding fields to be displayed in the alert.

</details>
            
<details>
<summary>Datadome Protection Intrusion Detection</summary>


Detects when Datadome protection raises an alert linked to intrusion. Datadome is used against fraud and bots.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>SecurityScorecard Vulnerability Assessment Scanner New Issues</summary>


Raises an alert when SecurityScorecard Vulnerability Assessment Scanner find new issues.

- **Effort:** master

- **Changelog:**

    - 15/01/2025 - minor - Adding format field to improve rules mapping
    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Intrusion Detection Alert</summary>


Trend Micro Apex One has raised an alert for an intrusion detection.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One High Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a high severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One Low Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a low severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One Medium Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a medium severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
**Exploit Public-Facing Application**

<details>
<summary>Akamai Guardicore Medium On-Prem Severity Security Incident</summary>


Akamai Guardicore has detected a medium severity security incident, indicating suspicious activity that warrants analyst review. This may include unusual lateral movement patterns, policy violations, or communication with suspicious but unconfirmed malicious endpoints.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem High Severity Security Incident</summary>


Akamai Guardicore has detected a high severity security incident, indicating a likely confirmed threat such as communication with a known malicious IP, active malware beaconing, or exploitation of a vulnerable asset. Immediate triage is required.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem Low Severity Security Incident</summary>


Akamai Guardicore has detected a low severity security incident, such as a connection attempt to an IP address with a bad reputation identified by the Guardicore Reputation Service.

- **Effort:** master

</details>
    
<details>
<summary>CVE-2018-11776 Apache Struts2</summary>


Apache Struts versions 2.3 to 2.3.34 and 2.5 to 2.5.16 suffer from possible Remote Code Execution when alwaysSelectFullNamespace is true (either by user or a plugin like Convention Plugin) and then: results are used with no namespace and in same time, its upper package have no or wildcard namespace and similar to results, same possibility when using url tag which doesn't have value and action set and in same time, its upper package have no or wildcard namespace.

- **Effort:** intermediate

</details>
    
<details>
<summary>CVE-2018-13379 Fortinet Exploit</summary>


Detects the successful exploitation of the Fortinet FortiOS CVE-2018-13379. This CVE is one of the most exploited CVEs since 2018. It is exploited by APT threat actors as well as cybercriminals. The exploitation of this CVE lead an unauthenticated user to get full access to FortiOS system file through SSL VPN via specially crafted HTTP resource requests. The exploit read /dev/cmdb/sslvpn_websession file, that contains login and passwords in (clear/text). An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects FortiOS 5.6.3 to 5.6.7 and FortiOS 6.0.0 to 6.0.4.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2019-0604 SharePoint</summary>


Detects the exploitation of the SharePoint vulnerability (CVE-2019-0604).

- **Effort:** advanced

- **Changelog:**

    - 04/11/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>CVE-2019-11510 Pulse Secure Exploit</summary>


Detects the successful exploitation of the Pulse Secure vulnerability CVE-2019-11510. This CVE is one of the most exploited CVEs since 2019. It is exploited by diverse threat actors, leading sometimes in ransomware deployement among these groups: Maze, Conti, Egregor, DoppelPaymer, NetWalker and REvil. But also APT actors such as APT29. The exploitation of this CVE allows a remote, unauthenticated attacker to compromise a vulnerable VPN server. The attacker may be able to gain access to all active users and their plain-text credentials. It may also be possible for the attacker to execute arbitrary commands on each VPN client as it successfully connects to the VPN server. The exploit reads /etc/passwd file to get access to login and passwords in (clear/text). An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects 8.1R15.1, 8.2 before 8.2R12.1, 8.3 before 8.3R7.1, and 9.0 before 9.0R3.4 products.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2019-19781 Citrix NetScaler (ADC)</summary>


Detects CVE-2019-19781 exploitation attempt against Citrix NetScaler (ADC), Application Delivery Controller and Citrix Gateway Attack.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2019-2725 Oracle Weblogic Exploit</summary>


Detects the successful exploitation of a deserialization vulnerability in Oracle Weblogic Server, CVE-2019-2725. This vulnerability affects versions 10.X and 12.1.3 of WebLogic that have the components wls9_async_response.war and wls-wsat.war enabled. It is a remote code execution which can be exploited without authentication via HTTP. An HTTP response status code = 202, means the target is vulnerable, the analyst then has to look in depth to check if a webshell has been uploaded or something else has been done.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2020-0688 Microsoft Exchange Server Exploit</summary>


Detects the exploitation of CVE-2020-0688. The POC exploit a .NET serialization vulnerability in the Exchange Control Panel (ECP) web page. The vulnerability is due to Microsoft Exchange Server not randomizing the keys on a per-installation basis resulting in them using the same validationKey and decryptionKey values. With knowledge of these, values an attacker can craft a special viewstate to use an OS command to be executed by NT_AUTHORITY\SYSTEM using .NET deserialization. To exploit this vulnerability, an attacker needs to leverage the credentials of an account it had already compromised to authenticate to OWA.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2020-1147 SharePoint</summary>


Detection of SharePoint vulnerability CVE-2020-1147.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2020-14882 Oracle WebLogic Server</summary>


Detects the exploitation of the Oracle WebLogic Server vulnerability (CVE-2020-16952).

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2020-17530 Apache Struts RCE</summary>


Detects the exploitation of the Apache Struts RCE vulnerability (CVE-2020-17530).

- **Effort:** intermediate

</details>
    
<details>
<summary>CVE-2020-5902 F5 BIG-IP Exploitation Attempts</summary>


Detects the exploitation attempt of the vulnerability found in F5 BIG-IP and described in CVE-2020-5902.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2021-20021 SonicWall Unauthenticated Administrator Access</summary>


Detects the exploitation of SonicWall Unauthenticated Admin Access.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2021-21972 VMware vCenter</summary>


The vSphere Client (HTML5) contains a remote code execution vulnerability in a vCenter Server plugin. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.x before 7.0 U1c, 6.7 before 6.7 U3l and 6.5 before 6.5 U3n) and VMware Cloud Foundation (4.x before 4.2 and 3.x before 3.10.1.2). POST request on the following PATH "/ui/vropspluginui/rest/services/uploadova". If in response body (500) the words it has "uploadFile", that means the vCenter is available to accept files via POST without any restrictions.

- **Effort:** intermediate

</details>
    
<details>
<summary>CVE-2021-21985 VMware vCenter</summary>


The VMware vSphere Client (HTML5) contains a remote code execution vulnerability due to lack of input validation in the Virtual SAN Health Check plug-in which is enabled by default in vCenter Server. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.0 before 7.0 U2b, 6.7 before 6.7 U3n and 6.5 before 6.5 U3p) and VMware Cloud Foundation (4.x before 4.2.1 and 3.x before 3.10.2.1).

- **Effort:** advanced

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CVE-2021-22123 Fortinet FortiWeb OS Command Injection</summary>


Detects Fortinet FortiWeb OS Command Injection (August 2021) vulnerability exploitation attempt. A remote, authenticated attacker can execute arbitrary commands on the system hosting a vulnerable FortiWeb WAF by sending a POST request with the command in the name field. At the time of writing this rule, it would appear that the request would respond in code 500 for a successful exploitation attempt.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2021-22893 Pulse Connect Secure RCE Vulnerability</summary>


Detects potential exploitation of the authentication by-pass vulnerability that can allow an unauthenticated user to perform remote arbitrary file execution on the Pulse Connect Secure gateway. It is highly recommended to apply the Pulse Secure mitigations and seach for indicators of compromise on affected servers if you are in doubt over the integrity of your Pulse Connect Secure product.

- **Effort:** intermediate

- **Changelog:**

    - 01/09/2025 - major - switch selection to regex to avoid false positive.

</details>
            
<details>
<summary>CVE-2021-22986 F5 BIG-IP iControl REST Unauthenticated RCE</summary>


Detects successful exploitation of the F5 BIG-IP vulnerability CVE-2021-22986.

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2021-26855 Exchange SSRF</summary>


Detects the exploitation of ProyxLogon vulerability on Exchange servers.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2021-34527 PrintNightmare Suspicious Actions From Spoolsv</summary>


Detects suspicious image loads and file creations from the spoolsv process which could be a sign of an attacker trying to exploit the PrintNightmare vulnerability, CVE-2021-34527. A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. This works as well as a Local Privilege escalation vulnerability. To fully work the rule requires to log for Loaded DLLs and File Creations, which can be done respectively using the Sysmon's event IDs 7 and 11.

- **Effort:** master

</details>
    
<details>
<summary>CVE-2021-41773 Apache 2.4.49 Path Traversal</summary>


Detects successful exploitation of the Apache Path Traversal CVE-2021-41773.

- **Effort:** advanced

</details>
    
<details>
<summary>CVE-2021-43798 Grafana Directory Traversal</summary>


Grafana version 8.x has a 0day arbitrary file read (with no fix yet) based on a directory traversal vulnerability

- **Effort:** intermediate

</details>
    
<details>
<summary>Exploited CVE-2020-10189 Zoho ManageEngine</summary>


Detects the exploitation of Zoho ManageEngine Desktop Central Java Deserialization vulnerability reported as CVE-2020-10189.

- **Effort:** elementary

</details>
    
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>GitLab CVE-2021-22205</summary>


Detects GitLab vulnerability CVE-2021-22205 exploitation success. It allows an attacker to do some remote code execution with user git. The HTTP return code 422 indicates a successfull exploitation.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious DNS Child Process</summary>


Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).

- **Effort:** intermediate

</details>
    
**Hardware Additions**

<details>
<summary>External Disk Drive Or USB Storage Device</summary>


Detects external diskdrives or plugged in USB device.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Phishing**

<details>
<summary>Advanced Threat Detected By Hornetsecurity 365 Total Protection</summary>


Hornetsecurity 365 Total Protection has detected an advanced threat from an e-mail.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cisco ESA Suspicious Email With Attachment</summary>


Detects an email with an attachment, from a sender tagged as suspect, detected by either the Antivirus or the Advanced Malware Protection (AMP) engine and delivered to the recipient

- **Effort:** advanced

</details>
    
<details>
<summary>Cisco Umbrella Threat Detected</summary>


Cisco Umbrella has detected a malicious traffic categorized as malware, phishing or adware.

- **Effort:** intermediate

</details>
    
<details>
<summary>Download Files From Non-Legitimate TLDs</summary>


Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 05/08/2025 - minor - Improve filter to avoid false positives
    - 06/10/2025 - minor - Improve filter to avoid false positives
    - 02/02/2026 - minor - Improved selection to avoid false positives by forcing the destination.ip field.

</details>
            
<details>
<summary>Download Files From Suspicious TLDs</summary>


Detects download of certain file types from hosts in suspicious TLDs

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 06/10/2025 - minor - Improve filter to reduce false positives.

</details>
            
<details>
<summary>ESET Protect Malware</summary>


Detects when Eset Protect tagged an event as linked to a malware with infected files.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Blocked Sender</summary>


Detects when a user is blocked by google workspace.

- **Effort:** advanced

</details>
    
<details>
<summary>Malware Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a malware contained in the message.

- **Effort:** master

</details>
    
<details>
<summary>Malware Detected By Vade For M365 And Not Blocked</summary>


Vade Secure product Vade for M365 has detected a malware contained in the message and didn't delete it.

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Anti-Phishing Policy Deletion</summary>


Detects when the anti-phishing policy is removed from Microsoft 365 (Office 365). By default, Microsoft 365 (Office 365) includes built-in features that help protect users from phishing attacks. This policy specifies the phishing protections to enable or disable, and the actions to apply options.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Anti-Phishing Rule Deletion</summary>


Detects the deactivation of the anti-phishing rule from Microsoft 365 (Office 365). The anti-phishing rule specifies the priority and recipient filters (who the policy applies to) for an anti-phish policy.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) AtpDetection</summary>


Detects when an AtpDetection (Advanced Threat Protection) event from the Office365 ThreatIntelligence service is raised. AtpDetection is a service which secures emails, attachments, and files by scanning them for threats.

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) DLP Policy Removed</summary>


Detects when a DLP (Data Loss Prevention) policy is removed in Microsoft 365 (Office 365). DLP policies defines which resources can be shared and with whom, preventing sensitive information from being leaked.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) MCAS Detection Velocity</summary>


Detects when Microsoft Cloud App Security identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Inbox Hiding</summary>


Detects when Microsoft Cloud App Security identifies that a suspicious inbox rule was set on a user’s inbox. This may indicate that the user account is compromised, and that the mailbox is being used to distribute spam and malware in your organization. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS New Country</summary>


Detects when Microsoft Cloud App Security identifies a sign-in from a country where it has never connected. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Repeated Delete</summary>


Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Repeated Failed Login</summary>


Detects when Microsoft Cloud App Security identifies a large number of failed login attempts which may indicate a brute-force attempt. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Risky IP</summary>


Detects when Microsoft Cloud App Security identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MailBoxAuditBypassAssociation Option Implementation</summary>


Detects the implementation of a MailBoxAuditBypassAssociation option in Microsoft 365 (Office 365). This option is used when you configure a user or computer account to bypass mailbox audit logging, access or actions taken by the user or computer account to any mailbox isn't logged.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Filter Policy Removed</summary>


Detects when a malware policy has been deleted in Microsoft 365 (Office 365). A malware filter policy is used to alert administrators that an internal user sent a message that contained malware.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Filter Rule Deletion</summary>


Detects when a malware filter rule has been deleted in Microsoft 365 (Office 365). The malware filter rule specifies the priority and recipient filters (who the policy applies to) for a malware filter policy.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Uploaded On OneDrive</summary>


Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to OneDrive. Attackers can use this method to propagate through the network.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Uploaded On SharePoint</summary>


Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to SharePoint. Attackers can use this method to propagate through the network.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Mass Download By A Single User</summary>


Identifies when Microsoft Cloud App Security reports that a single user performs more than 50 downloads within 1 minute.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft 365 (Office 365) Potential Ransomware Activity Detected</summary>


Detects when Microsoft Cloud App Security reports that a user has uploaded files to the cloud that might be infected with ransomware.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft 365 (Office 365) Safe Attachment Rule Disabled</summary>


Detects when the safe attachment rule has been deleted in Microsoft 365 (Office 365). Safe Attachments is a feature in Microsoft Defender for Microsoft 365 (Office 365) that opens email attachments in a special hypervisor environment to detect malicious activity.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Safelinks Disabled</summary>


Detects when a safelink rule has been deleted in Microsoft 365 (Office 365). Safe Links is a feature in Defender for Microsoft 365 (Office 365) that provides URL scanning and rewriting of inbound email messages in mail flow, and time-of-click verification of URLs and links in email messages and other locations.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Unusual Volume Of File Deletion</summary>


Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft 365 Security and Compliance Center High Severity Alert</summary>


A security or compliance-related alert of high severity was raised, based on the policies of the tenant. This rule can be very noisy depending on the configuration of the tenant. Alert filters are likely required. In addition, most alerts don't include any context, and are only useful if the analysts have access to the Microsoft portals to investigate.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 Security and Compliance Center Medium Severity Alert</summary>


A security or compliance-related alert of medium severity was raised, based on the policies of the tenant. This rule can be very noisy depending on the configuration of the tenant. Alert filters are likely required. In addition, most alerts don't include any context, and are only useful if the analysts have access to the Microsoft portals to investigate.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender for Office 365 High Severity AIR Alert</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a High severity alert triggers an automated investigation, such as when a potentially malicious URL click was detected, or when a user is restricted from sending email.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Microsoft Defender for Office 365 Low Severity AIR Alert Handled Automatically</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Low or Informational severity alert triggered an automated investigation, and remediation was conducted automatically. Low and Informational alerts include when an email is reported by a user, or when a malicious email is removed after delivery.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Microsoft Defender for Office 365 Low Severity AIR Alert Requires Action</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Low or Informational severity alert triggered an automated investigation, and remediation actions need to be approved or conducted. Low and Informational alerts include when an email is reported by a user, or when a malicious email is removed after delivery.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Microsoft Defender for Office 365 Medium Severity AIR Alert</summary>


Microsoft Defender for Office 365 includes the capability to run Automated investigation and response (AIR) actions. This rule detects when a Medium severity alert triggers an automated investigation, such as when suspicious email sending patterns are detected from an account.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses</summary>


Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.

- **Effort:** intermediate

- **Changelog:**

    - 01/06/2026 - minor - Adding more filter and review group-by clause to reduce false positives

</details>
            
<details>
<summary>Okta Phishing Detection with FastPass Origin Check</summary>


Okta's FastPass prevents known phishing sites.

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Phishing Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a phishing attempt.

- **Effort:** master

</details>
    
<details>
<summary>Phishing Detected By Vade For M365 And Not Blocked</summary>


Vade Secure product Vade for M365 has detected a phishing attempt from an email that is not whitelisted and didn't move the email to the junk folder.

- **Effort:** advanced

- **Changelog:**

    - 16/01/2025 - minor - Adding filter to reduce false positives.

</details>
            
<details>
<summary>Possible Malicious File Double Extension</summary>


Detects request to potential malicious file with double extension

- **Effort:** elementary

</details>
    
<details>
<summary>Proofpoint TAP Email Classified As Malware But Allowed</summary>


An email was classified as malware with a threat score greater than 0 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.

- **Effort:** master

- **Changelog:**

    - 01/06/2026 - major - Adding a new selection for "click" events as they do not have a threat score. Effort level adapted as well since this is now an integration rule.

</details>
            
<details>
<summary>Proofpoint TAP Email Classified As Phishing But Allowed</summary>


An email was classified as phishing with a threat score greater than 50 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.

- **Effort:** master

- **Changelog:**

    - 01/06/2026 - major - Adding a new selection for "click" events as they do not have a threat score. Effort level adapted as well since this is now an integration rule.

</details>
            
<details>
<summary>Proofpoint TAP Email Classified As Spam But Allowed</summary>


An email was classified as spam with a threat score greater than 50 by Proofpoint TAP but was not blocked. The threshold on the Threat Score has been defined to avoid a high amount of false positives.

- **Effort:** master

- **Changelog:**

    - 01/06/2026 - major - Adding a new selection for "click" events as they do not have a threat score. Effort level adapted as well since this is now an integration rule.

</details>
            
<details>
<summary>RDP Configuration File From Mail Process</summary>


Detects RDP configuration file being created or executed by a Mail-related process like Outlook. RDP configuration file will allow, when opened, an user to connect to the configured server easily. Attackers use this to trick victims in order to get a shared drive and potentially retrieve the data from that drive, but also drop a malicious file on the drive to establish persistence. Using RDP can also expose the victim's credential and clipboard data on some cases.

- **Effort:** advanced

</details>
    
<details>
<summary>Retarus Email Security Threat Detected (CxO Or Patient Zero Detection)</summary>


Cx0 fraud and Patient Zero Detection alerts detected by Retarus Email Security. CxO Fraud Detection uses algorithms that identify from-spoofing and domain-spoofing, to detect falsified sender addresses (e.g. from high level executives - CEO, CFO...). Patient Zero Detection® uses a digital fingerprint to identify emails containing malware that have already been delivered.

- **Effort:** advanced

</details>
    
<details>
<summary>Retarus Email Security Threat Detected (MultiScan)</summary>


Antivirus MultiScan alerts detected by Retarus Email Security. AntiVirus MultiScan automatically scans incoming and outgoing emails and file attachments for viruses with up to four virus scanners and uses heuristic analysis to protect from unknown malware.

- **Effort:** intermediate

</details>
    
<details>
<summary>Retarus Email Security Threat Detected (Sandboxing)</summary>


Sandboxing alerts detected by Retarus Email Security. Sandboxing subjects specific file attachments to an in-depth analysis. Retarus uses a sandboxing solution from the specialized and highly respected third-party provider Palo Alto Networks for this advanced threat assessment. Emails identified as infected are either deleted or quarantined, and the intended recipient is notified.

- **Effort:** elementary

</details>
    
<details>
<summary>SEKOIA.IO Intelligence Feed</summary>


Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.

- **Effort:** elementary

</details>
    
<details>
<summary>Scam Detected By Vade For M365</summary>


Vade Secure product Vade for M365, has detected a scam e-mail.

- **Effort:** master

</details>
    
<details>
<summary>Scam Detected By Vade For M365 And Not Blocked</summary>


Vade Secure product Vade for M365, has detected a scam e-mail and didn't block it.

- **Effort:** advanced

- **Changelog:**

    - 18/06/2024 - minor - Adding filter when whitelisted.

</details>
            
<details>
<summary>Spam Detected By Hornetsecurity 365 Total Protection</summary>


Hornetsecurity 365 Total Protection has detected a spam e-mail.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>Spam Detected By Vade For M365</summary>


Vade Secure product Vade for M365, has detected a spam e-mail.

- **Effort:** master

</details>
    
<details>
<summary>Spam Detected By Vade For M365 And Not Blocked</summary>


Vade Secure product Vade for M365, has detected a spam e-mail and didn't block it.

- **Effort:** advanced

</details>
    
<details>
<summary>Spearphishing (CEO Fraud) Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a spearphishing attempt with CEO fraud thematic. Impersonation of CEO or senior management members requesting urgent money transfer, usually on an unknown RIB.

- **Effort:** master

</details>
    
<details>
<summary>Spearphishing (Gift Cards Fraud) Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a spear-phishing attempt with gift-cards fraud thematic. Executive impersonation requesting a money transfer to set up gift-cards for employees. Confidentiality and discretion are usually implied.

- **Effort:** master

</details>
    
<details>
<summary>Spearphishing (Initial Contact Fraud) Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a spearphishing attempt with initial contact fraud thematic. Do not contains any malicious content or specific actions other than a request to reply to the email. “Are you available?”. The main goal is to incite a reply that could register the sending address as a known and legitimate address.

- **Effort:** master

</details>
    
<details>
<summary>Spearphishing (Lawyer Fraud) Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a spearphishing attempt with lawyer fraud thematic. Impersonation of lawyers and lawyers' firms. The main goal is to make sure the victims will not raise awareness around them. Confidentiality restrictions are implied.

- **Effort:** master

</details>
    
<details>
<summary>Spearphishing (W2 Fraud) Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a spearphishing attempt with W2 fraud thematic. Executive or HR impersonation phishing for social security numbers or tax identification numbers. Collected data are generally used for identity theft schemes.

- **Effort:** master

</details>
    
<details>
<summary>Suspicious Double Extension</summary>


Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns

- **Effort:** advanced

- **Changelog:**

    - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.

</details>
            
<details>
<summary>Suspicious Download Links From Legitimate Services</summary>


Detects users clicking on Google docs links to download suspicious files. This technique was used a lot by Bazar Loader in the past.

- **Effort:** intermediate

- **Changelog:**

    - 13/06/2024 - minor - Adding similarity strategy and changing effort level.
    - 15/10/2024 - minor - Adding filter to reduce false positives.
    - 06/01/2026 - minor - Update filter to reduce false positives.

</details>
            
<details>
<summary>Suspicious Email Attachment Received</summary>


Detects email containing a suspicious file as an attachment, based on its extension.

- **Effort:** advanced

- **Changelog:**

    - 27/03/2025 - minor - Adding new extension
    - 15/04/2024 - minor - Update email from field to latest parser format
    - 14/11/2024 - major - Adding new file extension and new condition to make the rule broader as it can now match on more intakes.

</details>
            
<details>
<summary>Suspicious Hangul Word Processor Child Process</summary>


Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Outlook Child Process</summary>


Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.

- **Effort:** intermediate

</details>
    
<details>
<summary>Threat Detected By Hornetsecurity 365 Total Protection</summary>


Hornetsecurity 365 Total Protection has detected a threat from an e-mail.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration

</details>
            
## Execution
**Windows Management Instrumentation**

<details>
<summary>Blue Mockingbird Malware</summary>


Attempts to detect system changes made by Blue Mockingbird

- **Effort:** elementary

</details>
    
<details>
<summary>Impacket Wmiexec Module</summary>


Detection of impacket's wmiexec example, used by attackers to execute commands remotely.

- **Effort:** elementary

- **Changelog:**

    - 22/03/2024 - minor - improve filter to extand detection

</details>
            
<details>
<summary>Invoke-TheHash Commandlets</summary>


Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Mshta Execution From Wmi</summary>


Detects mshta executed by wmiprvse as parent. It has been used by TA505 with some malicious documents.

- **Effort:** intermediate

</details>
    
<details>
<summary>Tactical RMM Installation</summary>


Detection of common Tactical RMM installation arguments that could be abused by some attackers.

- **Effort:** elementary

</details>
    
<details>
<summary>VSCode Tunnel Shell Exec</summary>


Using VSCode and its remote tunnel access feature to run a terminal and execute commands. This could be a legit use, but also has been observed being used by some attackers.

- **Effort:** advanced

</details>
    
<details>
<summary>WMI DLL Loaded Via Office</summary>


Detects Windows Management Instrumentation (WMI) DLL loaded via Office process. This activity may correspond to VBA macro executing WMI commands, which is highly suspicious. The prerequisite is to log Loaded DLLs images, which can be done with the Sysmon Event ID 7 (DLL image loaded by process).

- **Effort:** master

</details>
    
<details>
<summary>WMI Fingerprint Commands</summary>


Detects attacker fingerprint activities based on the correlation of specific WMIC commands. This has been observed with Aurora malware.

- **Effort:** advanced

- **Changelog:**

    - 19/08/2025 - major - Changing effort level.

</details>
            
<details>
<summary>WMI Install Of Binary</summary>


Detection of WMI used to install a binary on the host. It is often used by attackers as a signed binary to infect an host.

- **Effort:** elementary

</details>
    
<details>
<summary>WMIC Uninstall Product</summary>


Detects products being uninstalled using WMIC command.

- **Effort:** intermediate

- **Changelog:**

    - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)

</details>
            
<details>
<summary>WMImplant Hack Tool</summary>


WMImplant is a powershell framework used by attacker for reconnaissance and exfiltration, this rule attempts to detect WMimplant arguments and invokes commands. 

- **Effort:** advanced

- **Changelog:**

    - 29/11/2023 - minor - Added a selection to filter some false positives.
    - 26/03/2024 - major - Rule's pattern field changed.
    - 26/06/2025 - major - Pattern updated to avoid false positives and effort level changed to be coherent.

</details>
            
<details>
<summary>WerFaultSecure Abuse</summary>


Detect usage of the software vulnerability of WerFaultSecure to suspend the processes of EDRs, and bypass detection. It has been implemented in the tool EDR-Freeze.

- **Effort:** advanced

</details>
    
<details>
<summary>Windows Sandbox Start</summary>


Detection of Windows Sandbox started from the command line with a config file or interactively using a WSB file.

- **Effort:** master

</details>
    
<details>
<summary>Wmic Process Call Creation</summary>


The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. Although WMI is supposed to be an administration tool, it is wildy abused by threat actors. One of the reasons is WMI is quite stealthy. This rule detects the wmic command line launching a process on a remote or local host.

- **Effort:** intermediate

- **Changelog:**

    - 01/08/2023 - major - Rewritten as a regex to reduce false positives

</details>
            
<details>
<summary>Wmic Service Call</summary>


Detects either remote or local code execution using wmic tool.

- **Effort:** intermediate

</details>
    
<details>
<summary>XSL Script Processing And SquiblyTwo Attack</summary>


Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.

- **Effort:** intermediate

</details>
    
**Scheduled Task/Job**

<details>
<summary>BazarLoader Persistence Using Schtasks</summary>


Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>Blue Mockingbird Malware</summary>


Attempts to detect system changes made by Blue Mockingbird

- **Effort:** elementary

</details>
    
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Creation or Modification of a GPO Scheduled Task</summary>


Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cron Files Alteration</summary>


Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace App Script Scheduled Task</summary>


Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.

- **Effort:** advanced

</details>
    
<details>
<summary>Qakbot Persistence Using Schtasks</summary>


Detects possible Qakbot persistence using schtasks.

- **Effort:** intermediate

</details>
    
<details>
<summary>Remote Task Creation Via ATSVC Named Pipe</summary>


Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.

- **Effort:** intermediate

- **Changelog:**

    - 21/03/2024 - minor - change filter to ACL hex value

</details>
            
<details>
<summary>STRRAT Scheduled Task</summary>


Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'

- **Effort:** intermediate

</details>
    
<details>
<summary>Scheduled Task Creation By Non Privileged User</summary>


Detects scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 

- **Effort:** master

- **Changelog:**

    - 03/12/2025 - minor - Change rule effort level and update of rule name

</details>
            
<details>
<summary>Schtasks Persistence With High Privileges</summary>


Detection of scheduled task with high privileges used by attacker for persistence.

- **Effort:** elementary

</details>
    
<details>
<summary>Schtasks Suspicious Parent</summary>


Detects schtasks started from suspicious and/or unusual processes.

- **Effort:** intermediate

</details>
    
<details>
<summary>Spyware Persistence Using Schtasks</summary>


Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).

- **Effort:** intermediate

</details>
    
<details>
<summary>Windows Suspicious Scheduled Task Creation</summary>


The rule identify creation of new scheduled task who run suspicious commands.

- **Effort:** master

- **Changelog:**

    - 24/04/2025 - minor - Adding similarity strategy.
    - 03/12/2025 - major - Change rule effort level according to sigthings

</details>
            
**Command and Scripting Interpreter**

<details>
<summary>AWS CloudTrail EC2 Startup Script Changed</summary>


Detects changes to the EC2 instance startup script. The shell script will be executed as root/SYSTEM everytime the specific instances are booted up.

- **Effort:** intermediate

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>AWS GuardDuty High Severity Alert</summary>


GuardDuty has detected a threat with a high severity level. A High severity level indicates that the resource in question (an EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>AWS GuardDuty Low Severity Alert</summary>


GuardDuty has detected a threat with a low severity level. A low severity level indicates attempted suspicious activity that did not compromise your network, for example, a port scan or a failed intrusion attempt.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>AWS GuardDuty Medium Severity Alert</summary>


GuardDuty has detected a threat with a medium severity level. A Medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Alternate PowerShell Hosts Pipe</summary>


Detects alternate PowerShell hosts potentially bypassing detections looking for powershell.exe. Prerequisites are logging for PipeEvents in Sysmon config.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 25/11/2024 - minor - improve filter to avoid false positives.

</details>
            
<details>
<summary>Aspnet Compiler</summary>


Detects the starts of aspnet compiler.

- **Effort:** advanced

</details>
    
<details>
<summary>AutoIt3 Execution From Suspicious Folder</summary>


Detects AutoIt3 execution from an unusual/suspicious folder. Legitimate folders are "Program Files" and "AppData\\Local". AutoIt3.exe is a legitimate process used to execute AutoIt program files, which are used by legitimate software, custom scripts, but also malware. Finding AutoIt3 execution from unusual/suspicious folder can help detect malware activities, such as DarkGate execution. The detection rule can be tailored to your environment and your use of AutoIt3 by filtering out folder's execution of legitimate applications or scripts.

- **Effort:** advanced

</details>
    
<details>
<summary>Bitdefender GravityZone Endpoint Detection</summary>


Bitdefender GravityZone detected a malicious activity on an endpoint

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Bloodhound and Sharphound Tools Usage</summary>


Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.

- **Effort:** intermediate

- **Changelog:**

    - 29/08/2025 - minor - Filtering some command line false positives.
    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    - 26/03/2024 - minor - Adapted the rule to remove false positives.

</details>
            
<details>
<summary>Correlation Linux Decode And Exec</summary>


A Base64 string has been decoded and executed through a pipe. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.

- **Effort:** intermediate

</details>
    
<details>
<summary>Correlation Netcat Infection Chain</summary>


Detect netcat connection to download et execute payload via piped bash

- **Effort:** elementary

</details>
    
<details>
<summary>Correlation Supicious Powershell Drop and Exec</summary>


Detects a PowerShell process that download and exec a payload

- **Effort:** intermediate

- **Changelog:**

    - 09/10/2026 - minor - Rule improvement to detect more use cases

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Critical Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection High Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Informational Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Low Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Medium Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with the new EppDetectionSummaryEvent type.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 02/10/2025 - minor - Alert severity updated to match Crowdstrike's values and sekoia rule CrowdStrike Falcon Intrusion Detection High Severity
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>Cybereason EDR Alert</summary>


Cybereason EDR telemetry has raised an alert

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cybereason EDR Malware Detection</summary>


Cybereason EDR telemetry has detected a malware

- **Effort:** master

- **Changelog:**

    - 30/01/2026 - minor - Updating similarity to use malop id.
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>DNS Exfiltration and Tunneling Tools Execution</summary>


Well-known DNS exfiltration tools execution

- **Effort:** intermediate

</details>
    
<details>
<summary>Default Encoding To UTF-8 PowerShell</summary>


Detects PowerShell encoding to UTF-8, which is used by Sliver implants. The command line just sets the default encoding to UTF-8 in PowerShell.

- **Effort:** advanced

</details>
    
<details>
<summary>Default User www data User Compromised</summary>


User www_data by default cannot log and use a shell, any syscall of type execve induce user compromise

- **Effort:** master

</details>
    
<details>
<summary>Detection of default Mimikatz banner</summary>


Detection of default Mimikatz banner in powershell events

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Elise Backdoor</summary>


Detects Elise backdoor activity as used by Lotus Blossom

- **Effort:** elementary

</details>
    
<details>
<summary>Evil Winrm Modules Execution</summary>


This rule detects suspicious PowerShell activity consistent with the Evil-WinRM remote shell being executed via the Windows Remote Management host process

- **Effort:** intermediate

</details>
    
<details>
<summary>Exploited CVE-2020-10189 Zoho ManageEngine</summary>


Detects the exploitation of Zoho ManageEngine Desktop Central Java Deserialization vulnerability reported as CVE-2020-10189.

- **Effort:** elementary

</details>
    
<details>
<summary>Exploiting SetupComplete.cmd CVE-2019-1378</summary>


Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.

- **Effort:** intermediate

- **Changelog:**

    - 09/10/2025 - minor - Added filter for a new field to reduce false positvives.

</details>
            
<details>
<summary>FromBase64String Command Line</summary>


Detects suspicious FromBase64String expressions in command line arguments.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Shellcode Detect High</summary>


Detects when a suspicious shellcode is used with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Shellcode Detect Low</summary>


Detects when a suspicious shellcode is used with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Shellcode Detect Medium</summary>


Detects when a suspicious shellcode is used with a medium severity.

- **Effort:** master

</details>
    
<details>
<summary>Generic-reverse-shell-oneliner</summary>


To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using shell commands

- **Effort:** intermediate

</details>
    
<details>
<summary>In-memory PowerShell</summary>


Detects loading of essential DLL used by PowerShell, but not by the process powershell.exe. Detects meterpreter's "load powershell" extension and tool such PowerShDll.

- **Effort:** master

- **Changelog:**

    - 05/09/2025 - minor - Filter some FPs

</details>
            
<details>
<summary>Interactive Terminal Spawned via Python</summary>


Identifies when a terminal (tty) is spawned via Python. Attackers may upgrade a simple reverse shell to a fully interactive tty after obtaining initial access to a host.

- **Effort:** advanced

- **Changelog:**

    - 02/10/2024 - major - Rule's pattern changed

</details>
            
<details>
<summary>Invoke-TheHash Commandlets</summary>


Detects suspicious Invoke-TheHash PowerShell commandlet used for performing pass the hash WMI and SMB tasks.

- **Effort:** elementary

</details>
    
<details>
<summary>JS PowerShell Infection Chains</summary>


Detect JS script execution who run a PowerShell download and exec command_line

- **Effort:** intermediate

</details>
    
<details>
<summary>Lazarus Loaders</summary>


Detects different loaders used by the Lazarus Group APT

- **Effort:** elementary

</details>
    
<details>
<summary>Linux Bash Reverse Shell</summary>


To bypass some security equipement or for a sack of simplicity attackers can open raw reverse shell using shell commands

- **Effort:** intermediate

- **Changelog:**

    - 07/09/2026 - minor - Added filters to reduce false positives

</details>
            
<details>
<summary>Login Brute-Force Successful On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Login Failed Brute-Force On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Malicious PowerShell Keywords</summary>


Detects keywords from well-known PowerShell exploitation frameworks

- **Effort:** advanced

</details>
    
<details>
<summary>Malspam Execution Registering Malicious DLL</summary>


Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).

- **Effort:** elementary

</details>
    
<details>
<summary>Malware Outbreak</summary>


Spots a peak of malware detection by windows defender on this perimeter.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>MalwareBytes Uninstallation</summary>


Detects command line being used by attackers to uninstall Malwarebytes.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Defender Antivirus Disabled Base64 Encoded</summary>


Detects attempts to deactivate/disable Windows Defender through base64 encoded PowerShell command line or scripts.

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Microsoft Defender Antivirus Set-MpPreference Base64 Encoded</summary>


Detects changes of preferences for Windows Defender through command line or PowerShell scripts. Configure Windows Defender using base64-encoded commands is suspicious and could be related to malicious activities.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Defender Antivirus Threat Detected</summary>


Detection of a windows defender alert indicating the presence of potential malware

- **Effort:** advanced

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Microsoft Defender XDR (Graph API) Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (Graph API) Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender For Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (GraphAPI) Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR Alert</summary>


Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Cloud App Security Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.
    - 07/09/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Office 365 Alert</summary>


Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Office Creating Suspicious File</summary>


Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Office Spawning Script</summary>


Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 

- **Effort:** intermediate

</details>
    
<details>
<summary>Mshta Suspicious Child Process</summary>


Detects the use of various web request methods executed remotely via Windows PowerShell

- **Effort:** intermediate

- **Changelog:**

    - 17/10/2024 - minor - Adding similarity_strategy and enforce selection

</details>
            
<details>
<summary>Mustang Panda Dropper</summary>


Detects specific process parameters as used by Mustang Panda droppers

- **Effort:** elementary

</details>
    
<details>
<summary>Okta Security Threat Detected</summary>


Detects when a security threat is detected in Okta.

- **Effort:** intermediate

</details>
    
<details>
<summary>Palo Alto NGFW Threat Detection Critical</summary>


Palo Alto Next-Generation Firewall raised an alert for a threat detection with critical severity.

- **Effort:** master

</details>
    
<details>
<summary>Phorpiex DriveMgr Command</summary>


Detects specific command used by the Phorpiex botnet to execute a copy of the loader during its self-spreading stage. As described by Microsoft, this behavior is unique and easily identifiable due to the use of folders named with underscores "__" and the PE name "DriveMgr.exe".

- **Effort:** elementary

</details>
    
<details>
<summary>PowerShell Commands Invocation</summary>


Detects the execution to invoke a powershell command. This was used in an intrusion using Gootloader to access Mimikatz.

- **Effort:** advanced

</details>
    
<details>
<summary>PowerShell Credential Prompt</summary>


Detects PowerShell calling a credential prompt (using PromptForCredential), like $Credential = $host.ui.PromptForCredential("Need credentials", "Please enter your user name and password.", "", "NetBiosUserName"). The same result can be obtained by using the Get-Credential function but detecting it will trigger a lot of FP.

- **Effort:** advanced

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.

</details>
            
<details>
<summary>PowerShell Downgrade Attack</summary>


Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0

- **Effort:** elementary

</details>
    
<details>
<summary>PowerShell Download From URL</summary>


Detects a Powershell process that contains download commands in its command line string.

- **Effort:** advanced

- **Changelog:**

    - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.
    - 29/11/2023 - minor - Added a filter to the rule as some false positives were observed.

</details>
            
<details>
<summary>PowerShell EncodedCommand</summary>


Detects popular file extensions in commands obfuscated in base64 run through the EncodedCommand option.

- **Effort:** advanced

</details>
    
<details>
<summary>PowerShell Invoke Expression With Registry</summary>


Detects keywords from well-known PowerShell techniques to get registry key values

- **Effort:** advanced

</details>
    
<details>
<summary>PowerShell Invoke-Obfuscation Obfuscated IEX Invocation</summary>


Detects all variations of obfuscated powershell IEX invocation code generated by Invoke-Obfuscation framework

- **Effort:** advanced

</details>
    
<details>
<summary>PowerShell Malicious Nishang PowerShell Commandlets</summary>


Detects Commandlet names and arguments from the Nishang exploitation framework.

- **Effort:** advanced

- **Changelog:**

    - 26/07/2024 - minor - Removing tools relationships as it was inaccurate
    - 27/08/2024 - minor - improve filter to avoid false positive
    - 31/01/2025 - major - update keywords to improve detection coverage and remove false positives

</details>
            
<details>
<summary>PowerShell Malicious PowerShell Commandlets</summary>


Detects Commandlet names from well-known PowerShell exploitation frameworks (PowerSploit...).

- **Effort:** master

- **Changelog:**

    - 23/01/2024 - minor - Adding exclusion pattern and selection commandlet
    - 26/07/2024 - minor - Removing tools relationships as it was inaccurate

</details>
            
<details>
<summary>PowerShell NTFS Alternate Data Stream</summary>


Detects writing data into NTFS alternate data streams from PowerShell. Needs Script Block Logging (Event ID 4104)

- **Effort:** advanced

</details>
    
<details>
<summary>PowerShell Suspicious Context Changes</summary>


Detects some PowerShell context changes that could be used to create an interactive shell and bypass some security measures in terms of logging and execution.

- **Effort:** advanced

</details>
    
<details>
<summary>Powershell Web Request</summary>


Detects the use of various web request methods executed remotely via Windows PowerShell.

- **Effort:** master

- **Changelog:**

    - 06/06/2025 - major - Review heuristic and change level effort
    - 23/06/2025 - minor - improve filter
    - 13/05/2026 - minor - remove deprecated value in filter

</details>
            
<details>
<summary>Powershell Web Request And Windows Script</summary>


Detects the use of PowerShell web request method combined with Windows Script utilities. This has been observed being used by some malware loaders.

- **Effort:** intermediate

</details>
    
<details>
<summary>Python Offensive Tools and Packages</summary>


Track installation and usage of offensive python packages and project that are used for lateral movement.

- **Effort:** master

- **Changelog:**

    - 02/10/2024 - major - Rule's pattern changed
    - 20/01/2025 - major - Rule's pattern changed to reduce false positives.

</details>
            
<details>
<summary>QakBot Process Creation</summary>


Detects QakBot like process executions

- **Effort:** intermediate

</details>
    
<details>
<summary>Raw Reverse Shell</summary>


To bypass some security equipment or for a sack of simplicity attackers can open raw reverse shell using sh and or bash commands

- **Effort:** master

</details>
    
<details>
<summary>Screenconnect Remote Execution</summary>


Detect cmd or powershell remote execution cmdline via ScreenConnect

- **Effort:** intermediate

</details>
    
<details>
<summary>Sekoia.io EICAR Detection</summary>


Detects observables in Sekoia.io CTI tagged as EICAR, which are fake samples meant to test detection.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>SentinelOne EDR Agent Disabled</summary>


A SentinelOne EDR agent has been disabled according to SentinelOne logs.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Custom Rule Alert</summary>


A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively</summary>


A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Not Mitigated</summary>


A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR SSO User Added</summary>


A SSO User was added.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Malicious)</summary>


A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Suspicious)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Kill Success</summary>


A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Failed</summary>


A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Success</summary>


A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Remediate Success</summary>


A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Failed To Log In To The Management Console</summary>


A user has failed to log in to the management console.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Logged In To The Management Console</summary>


A user has logged in to the management console.

- **Effort:** master

- **Changelog:**

    - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Sigma Intelligence ErrTraffic PowerShell Command Line</summary>


Detects powershell script executed via ErrTraffic infection chain

- **Effort:** elementary

</details>
    
<details>
<summary>Socat Relaying Socket</summary>


Socat is a linux tool used to relay local socket or internal network connection, this technics is often used by attacker to bypass security equipment such as firewall

- **Effort:** advanced

- **Changelog:**

    - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 17/01/2025 - major - Significant rewrite of the rule to reduce false positives.

</details>
            
<details>
<summary>Socat Reverse Shell Detection</summary>


Socat is a linux tool used to relay or open reverse shell that is often used by attacker to bypass security equipment.

- **Effort:** elementary

- **Changelog:**

    - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 17/01/2025 - major - Complete rewrite of the rule to reduce false positives.

</details>
            
<details>
<summary>SquirrelWaffle Malspam Execution Loading DLL</summary>


Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Cmd.exe Command Line</summary>


Detection on suspicious cmd.exe command line seen being used by some attackers (e.g. Lazarus with Word macros). This requires Windows process command line logging.

- **Effort:** master

- **Changelog:**

    - 30/05/2023 - minor - Adding the Intellij IDEA to filter list
    - 22/11/2024 - major - Adding new elements for detection and filters.
    - 27/11/2024 - minor - Adding new filters to reduce false positives.

</details>
            
<details>
<summary>Suspicious CodePage Switch with CHCP</summary>


Detects a code page switch in command line

- **Effort:** intermediate

- **Changelog:**

    - 16/01/2024 - minor - Rename rule to fit with behavior

</details>
            
<details>
<summary>Suspicious DLL Loaded Via Office Applications</summary>


Detects suspicious DLL being loaded by an Microsoft Office Product. Considered as suspects are some .NET DLLs, clr.dll, GAC DLL, DSParse (Active Directoryi services API) or Kerberos DLLs which may be loaded by MS Office processes when executing a potentially malicious macro. The prerequisite is to log the Sysmon Event ID 7 (DLL image loaded by process). 

- **Effort:** master

</details>
    
<details>
<summary>Suspicious File Name</summary>


Detects suspicious file name possibly linked to malicious tool.

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious Microsoft Defender Antivirus Exclusion Command</summary>


Detects PowerShell commands aiming to exclude path, process, IP address, or extension from scheduled and real-time scanning. These commands can be used by attackers or malware to avoid being detected by Windows Defender. Depending on the environment and the installed software, this detection rule could raise false positives. We recommend customizing this rule by filtering legitimate processes that use Windows Defender exclusion command in your environment.

- **Effort:** master

</details>
    
<details>
<summary>Suspicious Outlook Child Process</summary>


Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious PowerShell Invocations - Generic</summary>


Detects suspicious PowerShell invocation command parameters through command line logging or ScriptBlock Logging.

- **Effort:** advanced

- **Changelog:**

    - 28/03/2023 - minor - Excluded some commonly observed false positives.
    - 13/03/2025 - major - Change effort and excluded some commonly observed false positives.
    - 14/08/2025 - minor - Excluded new paths to reduce false positives.

</details>
            
<details>
<summary>Suspicious PowerShell Invocations - Specific</summary>


Detects suspicious PowerShell invocation command parameters.

- **Effort:** intermediate

- **Changelog:**

    - 26/05/2023 - minor - Added a filter to the rule as some false positives were observed.

</details>
            
<details>
<summary>Suspicious PowerShell Keywords</summary>


Detects keywords that could indicate the use of some PowerShell exploitation framework.

- **Effort:** advanced

- **Changelog:**

    - 23/05/2024 - minor - Added filter to reduce false positives and new suspicious keywords.

</details>
            
<details>
<summary>Suspicious PrinterPorts Creation (CVE-2020-1048)</summary>


Detects new commands that add new printer port which point to suspicious file

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious Scripting In A WMI Consumer</summary>


Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Taskkill Command</summary>


Detects rare taskkill command being used. It could be related to Baby Shark malware.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious VBS Execution Parameter</summary>


Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Windows Script Execution</summary>


Detects wscript.exe or cscript.exe executing a script in user directories (C:\ProgramData or C:\Users) with a .txt extension, which is very suspicious. It could strongly correspond to a malware dropper, as seen during SquirrelWaffle maldoc campaign.

- **Effort:** intermediate

- **Changelog:**

    - 23/06/2025 - minor - Adding filter for false positives.
    - 19/10/2023 - major - Review of the rule to reduce false positives.

</details>
            
<details>
<summary>Suspicious XOR Encoded PowerShell Command Line</summary>


Detects suspicious powershell process which includes bxor command, alternative obfuscation  method to b64 encoded commands.

- **Effort:** advanced

</details>
    
<details>
<summary>Sysprep On AppData Folder</summary>


Detects suspicious Sysprep process start with AppData folder as target (as used by Trojan Syndicasec in Thrip report by Symantec). Sysprep is a Windows tool used to change Windows images from a generalized state to a specialized state, and then back to a generalized state. It can be used to remove all system-specific information and reset the computer.

- **Effort:** intermediate

</details>
    
<details>
<summary>TEHTRIS EDR Alert</summary>


Tehtris EDR telemetry has raised an alert.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Data Loss Prevention Alert</summary>


Trend Micro Apex One has raised an alert for data loss prevention.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Malware Alert</summary>


Trend Micro Apex One has detected a malware.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Critical Severity Alert</summary>


Detects when a critical alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Low Severity Alert</summary>


Detects when a low alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Medium Severity Alert</summary>


Detects when a medium alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench high Severity Alert</summary>


Detects when a high alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trickbot Malware Activity</summary>


Detects Trickbot malware process tree pattern in which rundll32.exe is parent of wermgr.exe.

- **Effort:** intermediate

</details>
    
<details>
<summary>Turla Named Pipes</summary>


Detects a named pipe used by Turla group samples. Prerequisites: Logging for PipeEvents is needed in Sysmon config

- **Effort:** elementary

</details>
    
<details>
<summary>Venom Multi-hop Proxy agent detection</summary>


Detects Venom Multi-hop Proxy agent.

- **Effort:** intermediate

</details>
    
<details>
<summary>WMI DLL Loaded Via Office</summary>


Detects Windows Management Instrumentation (WMI) DLL loaded via Office process. This activity may correspond to VBA macro executing WMI commands, which is highly suspicious. The prerequisite is to log Loaded DLLs images, which can be done with the Sysmon Event ID 7 (DLL image loaded by process).

- **Effort:** master

</details>
    
<details>
<summary>WMIC Uninstall Product</summary>


Detects products being uninstalled using WMIC command.

- **Effort:** intermediate

- **Changelog:**

    - 13/02/2024 - minor - Exclude non-Windows operating systems (false positives)

</details>
            
<details>
<summary>WMImplant Hack Tool</summary>


WMImplant is a powershell framework used by attacker for reconnaissance and exfiltration, this rule attempts to detect WMimplant arguments and invokes commands. 

- **Effort:** advanced

- **Changelog:**

    - 29/11/2023 - minor - Added a selection to filter some false positives.
    - 26/03/2024 - major - Rule's pattern field changed.
    - 26/06/2025 - major - Pattern updated to avoid false positives and effort level changed to be coherent.

</details>
            
<details>
<summary>Web Application Launching Shell</summary>


Detects when a web application launches a shell.

- **Effort:** master

- **Changelog:**

    - 10/10/2024 - major - Adding new elements and filters to increase detection and reduce false positives.

</details>
            
<details>
<summary>WithSecure Elements Critical Severity</summary>


WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>WithSecure Elements Warning Severity</summary>


Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).

- **Effort:** master

- **Changelog:**

    - 07/04/2025 - minor - Similarity strategy changed to avoid too much grouping
    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>XSL Script Processing And SquiblyTwo Attack</summary>


Detection of an attack where adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Another variation of this technique, dubbed "Squiblytwo", involves to invoke JScript or VBScript within an XSL file.

- **Effort:** intermediate

</details>
    
<details>
<summary>Zscaler ZIA Malicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
<details>
<summary>Zscaler ZIA Suspicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
**Scripting**

<details>
<summary>Suspicious VBS Execution Parameter</summary>


Detects suspicious VBS file execution with a specific parameter by cscript. It was observed in the Operation CloudHopper.

- **Effort:** elementary

</details>
    
**Rundll32**

<details>
<summary>PowerShell Execution Via Rundll32</summary>


Detects PowerShell Strings applied to rundll as seen in PowerShdll.dll Rule modified

- **Effort:** intermediate

</details>
    
**PowerShell**

<details>
<summary>In-memory PowerShell</summary>


Detects loading of essential DLL used by PowerShell, but not by the process powershell.exe. Detects meterpreter's "load powershell" extension and tool such PowerShDll.

- **Effort:** master

- **Changelog:**

    - 05/09/2025 - minor - Filter some FPs

</details>
            
**Trusted Developer Utilities Proxy Execution**

<details>
<summary>MSBuild Abuse</summary>


Detection of MSBuild uses by attackers to infect an host. Focuses on XML compilation which is a Metasploit payload.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Shared Modules**

<details>
<summary>FoggyWeb Backdoor DLL Loading</summary>


Detects DLL image load activity as used by the threat group NOBELIUM with the FoggyWeb backdoor loader. The prerequisite is to log Loaded DLLs images, which can be done through the Sysmon Event ID 7 (DLL image loaded by process).

- **Effort:** master

</details>
    
**CMSTP**

<details>
<summary>CMSTP Execution</summary>


Detects various indicators of Microsoft Connection Manager Profile Installer execution

- **Effort:** intermediate

- **Changelog:**

    - 19/10/2023 - minor - Slight change in selection to reduce false positives. Adding similarity.

</details>
            
<details>
<summary>MOFComp Execution</summary>


Detects rare usage of the Managed Object Format (MOF) compiler on Microsoft Windows. This could be abused by some attackers to load WMI classes.

- **Effort:** intermediate

</details>
    
**BITS Jobs**

<details>
<summary>BITSAdmin Download</summary>


Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.

- **Effort:** advanced

- **Changelog:**

    - 06/12/2023 - minor - Adding key words to increase detection.

</details>
            
**Exploitation for Client Execution**

<details>
<summary>Antivirus Exploitation Framework Detection</summary>


Detects a highly relevant Antivirus alert that reports an exploitation framework. This is based on Windows Defender logs (Event ID 1116 and 1117). 

- **Effort:** elementary

- **Changelog:**

    - 16/02/2026 - minor - Filtering out Event ID 1011 which caused false positives. The rule fired at the deletion of a quarantined file by Defender which was not the wanted behaviour.

</details>
            
<details>
<summary>Antivirus Password Dumper Detection</summary>


Detects a highly relevant Antivirus alert that reports a password dumper. This detection relies on Windows Defender events logs. This is based on Windows Defender logs (Event ID 1116 and 1117).

- **Effort:** elementary

</details>
    
<details>
<summary>Antivirus Relevant File Paths Alerts</summary>


Detects an Antivirus alert in a highly relevant file path or with a relevant file name. This is only based on Windows Defender events.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 26/03/2024 - major - Rule's pattern field changed
    - 22/04/2025 - major - Change effort level and similarity strategy

</details>
            
<details>
<summary>Audit CVE Event</summary>


Detects events generated by Windows to indicate the exploitation of a known vulnerability.

- **Effort:** elementary

- **Changelog:**

    - 15/07/2024 - major - review filter and improve similarity

</details>
            
<details>
<summary>Download Files From Non-Legitimate TLDs</summary>


Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 05/08/2025 - minor - Improve filter to avoid false positives
    - 06/10/2025 - minor - Improve filter to avoid false positives
    - 02/02/2026 - minor - Improved selection to avoid false positives by forcing the destination.ip field.

</details>
            
<details>
<summary>Download Files From Suspicious TLDs</summary>


Detects download of certain file types from hosts in suspicious TLDs

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 06/10/2025 - minor - Improve filter to reduce false positives.

</details>
            
<details>
<summary>Exploit For CVE-2015-1641</summary>


Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641

- **Effort:** elementary

</details>
    
<details>
<summary>Msdt (Follina) File Browse Process Execution</summary>


Detects various Follina vulnerability exploitation techniques. This is based on the Compatability Troubleshooter which is abused to do code execution.

- **Effort:** elementary

- **Changelog:**

    - 14/10/2024 - minor - Added filter to the rule to reduce false positives.
    - 19/06/2023 - minor - Added filter to the rule to reduce false positives.

</details>
            
<details>
<summary>Suspicious Hangul Word Processor Child Process</summary>


Detects suspicious Hangul Word Processor (HWP) child process that could indicate an exploitation as used by the Lazarus APT during the Operation Ghost Puppet (2018). This activity could correspond to a maldoc execution related to a .hwp file. Hangul is a proprietary word processing application that supports the Korean written language.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious New Printer Ports In Registry</summary>


Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
**User Execution**

<details>
<summary>AWS GuardDuty High Severity Alert</summary>


GuardDuty has detected a threat with a high severity level. A High severity level indicates that the resource in question (an EC2 instance or a set of IAM user sign-in credentials) is compromised and is actively being used for unauthorized purposes.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>AWS GuardDuty Low Severity Alert</summary>


GuardDuty has detected a threat with a low severity level. A low severity level indicates attempted suspicious activity that did not compromise your network, for example, a port scan or a failed intrusion attempt.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>AWS GuardDuty Medium Severity Alert</summary>


GuardDuty has detected a threat with a medium severity level. A Medium severity level indicates suspicious activity that deviates from normally observed behavior and, depending on your use case, may be indicative of a resource compromise.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Alert High Severity Sesame it Jizo NDR</summary>


Detects a high severity alert raised by SesameIT.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Bitdefender GravityZone Endpoint Detection</summary>


Bitdefender GravityZone detected a malicious activity on an endpoint

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Broadcom/Symantec Endpoint Security Event Blocked</summary>


Broadcom/Symantec Endpoint Security blocked an action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Broadcom/Symantec Endpoint Security Event Cleaned</summary>


Broadcom/Symantec Endpoint Security had cleaned action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Broadcom/Symantec Endpoint Security Event Quarantined</summary>


Broadcom/Symantec Endpoint Security had a quarantined action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Broadcom/Symantec Endpoint Security Event Terminate</summary>


Broadcom/Symantec Endpoint Security had a process terminate action. Careful when activating this rule, it generates lots of events that are not always relevant for detection.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cobalt Strike Default Beacons Names</summary>


Detects the default names of Cobalt Strike beacons / payloads.

- **Effort:** intermediate

- **Changelog:**

    - 13/08/2025 - minor - Added new filters to reduce false positives.
    - 20/09/2024 - minor - Added new filters to reduce false positives.
    - 27/05/2024 - minor - Added new filters to reduce false positives.
    - 21/11/2023 - minor - Added new filters to reduce false positives.
    - 08/11/2023 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Corelight Suricata High Severity IDS Alert</summary>


Detects a high severity Suricata IDS alert reported by a Corelight sensor (suricata_corelight log), indicating a likely network intrusion.

- **Effort:** master

</details>
    
<details>
<summary>Correlation PowerShell Suspicious DLL Loading</summary>


Detect some suspicious Windows DLL Loading where some PowerShell activity from the binary itself, followed by the same DLL process spawning other process. This is related to the usage of a PowerShell Named Pipe IPC from the DLL.

- **Effort:** intermediate

- **Changelog:**

    - 18/08/2025 - minor - Add filter to reduce false positives

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Critical Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection High Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Informational Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Low Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Medium Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with the new EppDetectionSummaryEvent type.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 02/10/2025 - minor - Alert severity updated to match Crowdstrike's values and sekoia rule CrowdStrike Falcon Intrusion Detection High Severity
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>Cybereason EDR Alert</summary>


Cybereason EDR telemetry has raised an alert

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cybereason EDR Malware Detection</summary>


Cybereason EDR telemetry has detected a malware

- **Effort:** master

- **Changelog:**

    - 30/01/2026 - minor - Updating similarity to use malop id.
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Darktrace Threat Visualizer Model Breach Critical Activity</summary>


Darktrace Threat Visualizer has detected a network critical activity related to one supervised device

- **Effort:** master

- **Changelog:**

    - 12/11/2024 - minor - Update name, description, similarity and severity
    - 02/07/2025 - minor - Update similarity
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Darktrace Threat Visualizer Model Breach Suspicious Activity</summary>


Darktrace Threat Visualizer has detected a network critical activity related to one supervised device

- **Effort:** master

- **Changelog:**

    - 12/11/2024 - minor - Update name, description, similarity and severity
    - 02/07/2025 - minor - Update similarity
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Darktrace Threat Visualizer Threat Critical Alert</summary>


Darktrace Threat Visualizer has raised a threat critical alert related to one supervised device

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Darktrace Threat Visualizer Threat Suspicious Alert</summary>


Darktrace Threat Visualizer has raised a threat suspicious alert related to one supervised device

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Download Files From Non-Legitimate TLDs</summary>


Detects file downloads from non-legitimate TLDs. Additional legitimates TLDs should be filtered according to the business habits.

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 05/08/2025 - minor - Improve filter to avoid false positives
    - 06/10/2025 - minor - Improve filter to avoid false positives
    - 02/02/2026 - minor - Improved selection to avoid false positives by forcing the destination.ip field.

</details>
            
<details>
<summary>Download Files From Suspicious TLDs</summary>


Detects download of certain file types from hosts in suspicious TLDs

- **Effort:** master

- **Changelog:**

    - 28/07/2025 - major - Improve filter and similarity strategy.
    - 06/10/2025 - minor - Improve filter to reduce false positives.

</details>
            
<details>
<summary>ESET Protect Intrusion Detection</summary>


Detects when the solution ESET Protect detects an intrusion.

- **Effort:** master

</details>
    
<details>
<summary>EfficientIP SOLIDServer Suspicious Behavior</summary>


Detects when EfficientIP SOLIDServer forwards a suspicious behavior related to an IP.

- **Effort:** master

</details>
    
<details>
<summary>Exploit For CVE-2015-1641</summary>


Detects Winword process starting uncommon sub process MicroScMgmt.exe as used in exploits for CVE-2015-1641

- **Effort:** elementary

</details>
    
<details>
<summary>Explorer Process Executing HTA File</summary>


Detects a suspicious execution of an HTA file by the explorer.exe process. This unusual activity was observed when running IcedID malspam.

- **Effort:** intermediate

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Malcore High</summary>


Detects a malcore alert by Gatewatcher AionIQ V103 with a high severity related to documents with passwords.

- **Effort:** master

- **Changelog:**

    - 24/01/2025 - minor - Adding filter to reduce false positives.
    - 27/01/2025 - minor - Changing field and adding filter to reduce false positives.
    - 05/03/2026 - minor - Update rule type to integration
    - 07/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Malcore Low</summary>


Detects a malcore alert by Gatewatcher AionIQ V103 with a low severity related to documents with passwords.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Malcore Medium</summary>


Detects a malcore alert by Gatewatcher AionIQ V103 with a medium severity related to documents with passwords.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Anomaly File Downloads</summary>


Detects a large number of file downloads.

- **Effort:** master

- **Changelog:**

    - 12/06/2024 - minor - Changing effort level and adding field to alert.

</details>
            
<details>
<summary>HTA Infection Chains</summary>


Detect the creation of a ZIP file and an HTA file as it is often used in infection chains. Furthermore it also detects the use of suspicious processes launched by explorer.exe combined with the creation of an HTA file, since it is also often used in infection chains (LNK - HTA for instance).

- **Effort:** advanced

- **Changelog:**

    - 04/12/2024 - minor - Event type fields and file paths added to filter some false positives, and effort level changed.
    - 20/09/2024 - minor - File paths added to filter some false positives.
    - 19/09/2024 - minor - File paths added to filter some false positives.
    - 30/11/2023 - minor - Update pattern with new lolbin

</details>
            
<details>
<summary>HarfangLab EDR Critical Level Rule Detection</summary>


HarfangLab EDR has raised an alert based on a critical level rule (not using hlai engine)

- **Effort:** master

- **Changelog:**

    - 23/05/2024 - minor - Added filter to exclude threat dataset
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Critical Threat</summary>


HarfangLab EDR detected a threat with a critical level. This detection by the EDR is based on several detection rules.

- **Effort:** master

- **Changelog:**

    - 23/12/2024 - minor - Change alert severity
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR High Level Rule Detection</summary>


HarfangLab EDR has raised an alert based on a high level rule (not using hlai engine)

- **Effort:** master

- **Changelog:**

    - 23/05/2024 - minor - Added filter to exclude threat dataset
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR High Threat</summary>


HarfangLab EDR detected a threat with a high level. This detection by the EDR is based on several detection rules.

- **Effort:** master

- **Changelog:**

    - 23/12/2024 - minor - Change alert severity
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Hlai Engine Detection</summary>


HarfangLab EDR has raised an alert based on its hlai engine

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Low Level Rule Detection</summary>


HarfangLab EDR has raised an alert based on a low level rule (not using hlai engine)

- **Effort:** master

- **Changelog:**

    - 23/05/2024 - minor - Added filter to exclude threat dataset
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Low Threat</summary>


HarfangLab EDR detected a threat with a low level. This detection by the EDR is based on several detection rules.

- **Effort:** master

- **Changelog:**

    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Medium Level Rule Detection</summary>


HarfangLab EDR has raised an alert based on a medium level rule (not using hlai engine)

- **Effort:** master

- **Changelog:**

    - 23/05/2024 - minor - Added filter to exclude threat dataset
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Medium Threat</summary>


HarfangLab EDR detected a threat with a medium level. This detection by the EDR is based on several detection rules.

- **Effort:** master

- **Changelog:**

    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Process Execution Blocked (HL-AI engine)</summary>


HarfangLab EDR's machine learning malware detection module (HL-AI) has detected a suspicious binary and blocked its execution. To know more on what caused this alert, you should check the value of the process name and the concerned computer and user.

- **Effort:** master

- **Changelog:**

    - 10/01/2024 - major - Account for all blocks instead of only "Startup blocked". Rule name explicitly mentions HL-AI engine.
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>HarfangLab EDR Suspicious Process Behavior Has Been Detected</summary>


HarfangLab EDR has detected a suspicious process behavior based on its detection rule. Check the rule name and description for more information.

- **Effort:** master

- **Changelog:**

    - 16/01/2025 - minor - Adding format field to improve rules mapping
    - 12/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>ISO LNK Infection Chain</summary>


Detection of an ISO (or any other similar archive file) downloaded file, followed by a child-process of explorer, which is characteristic of an infection using an ISO containing an LNK file. For events with `host.name`.

- **Effort:** master

- **Changelog:**

    - 20/03/2025 - major - Change effort level
    - 18/03/2025 - minor - File path exclusion added to filter some false positives.
    - 17/01/2025 - minor - Cmdline exclusion added to filter some false positives.
    - 25/11/2024 - minor - Updating filter on file change and deletion
    - 18/11/2024 - minor - Updating filter on file change and deletion
    - 09/10/2024 - minor - File paths added to filter some false positives.
    - 20/09/2024 - minor - File paths added to filter some false positives.
    - 19/09/2024 - minor - File paths added to filter some false positives.
    - 18/09/2023 - minor - File paths added to filter some false positives.
    - 13/03/2023 - minor - Extended the list of suspicious process names being spawned from explorer.exe

</details>
            
<details>
<summary>IcedID Execution Using Excel</summary>


Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 

- **Effort:** elementary

</details>
    
<details>
<summary>Lacework Cloud Security Critical Severity Alert</summary>


Detects when a critical alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Lacework Cloud Security High Severity Alert</summary>


Detects when a high alert severity is raised by Lacework. This severity level might indicates a suspicious change in configuration or policy violation.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Lacework Cloud Security Low Severity Alert</summary>


Detects when a low alert severity is raised by Lacework. This severity level might indicates a change in configuration that could be malicious or not.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Lacework Cloud Security Medium Severity Alert</summary>


Detects when a medium alert severity is raised by Lacework. This severity level might indicates a suspicious activity such as new source from user connection.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Login Brute-Force Successful On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Login Failed Brute-Force On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>MS Office Product Spawning Exe in User Dir</summary>


Detects an executable in the users directory started from Microsoft Word, Excel, Powerpoint, Publisher or Visio. This is a common technique used by attackers with documents embedding macros. It requires Windows command line logging events.

- **Effort:** master

- **Changelog:**

    - 10/08/2023 - minor - Rule modified and filter added to reduce false positives.
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Malspam Execution Registering Malicious DLL</summary>


Detects the creation of a file in the C:\Datop folder, or DLL registering a file in the C:\Datop folder. Files located in the Datop folder are very characteristic of malspam execution related to Qakbot or SquirrelWaffle. Prerequisites are Logging for File Creation events, which can be done in the Sysmon configuration (events 11), for the first part of the pattern (TargetFilename).

- **Effort:** elementary

</details>
    
<details>
<summary>Malware Detected By Vade For M365</summary>


Vade Secure product Vade for M365 has detected a malware contained in the message.

- **Effort:** master

</details>
    
<details>
<summary>Malware Detected By Vade For M365 And Not Blocked</summary>


Vade Secure product Vade for M365 has detected a malware contained in the message and didn't delete it.

- **Effort:** advanced

</details>
    
<details>
<summary>Malware Outbreak</summary>


Spots a peak of malware detection by windows defender on this perimeter.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Microsoft 365 (Office 365) Anti-Phishing Policy Deletion</summary>


Detects when the anti-phishing policy is removed from Microsoft 365 (Office 365). By default, Microsoft 365 (Office 365) includes built-in features that help protect users from phishing attacks. This policy specifies the phishing protections to enable or disable, and the actions to apply options.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Anti-Phishing Rule Deletion</summary>


Detects the deactivation of the anti-phishing rule from Microsoft 365 (Office 365). The anti-phishing rule specifies the priority and recipient filters (who the policy applies to) for an anti-phish policy.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) AtpDetection</summary>


Detects when an AtpDetection (Advanced Threat Protection) event from the Office365 ThreatIntelligence service is raised. AtpDetection is a service which secures emails, attachments, and files by scanning them for threats.

- **Effort:** intermediate

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) DLP Policy Removed</summary>


Detects when a DLP (Data Loss Prevention) policy is removed in Microsoft 365 (Office 365). DLP policies defines which resources can be shared and with whom, preventing sensitive information from being leaked.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) MCAS Detection Velocity</summary>


Detects when Microsoft Cloud App Security identifies two user activities (a single or multiple sessions) originating from geographically distant locations within a time period shorter than the time it would have taken the user to travel from the first location to the second. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Inbox Hiding</summary>


Detects when Microsoft Cloud App Security identifies that a suspicious inbox rule was set on a user’s inbox. This may indicate that the user account is compromised, and that the mailbox is being used to distribute spam and malware in your organization. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS New Country</summary>


Detects when Microsoft Cloud App Security identifies a sign-in from a country where it has never connected. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Repeated Delete</summary>


Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Repeated Failed Login</summary>


Detects when Microsoft Cloud App Security identifies a large number of failed login attempts which may indicate a brute-force attempt. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MCAS Risky IP</summary>


Detects when Microsoft Cloud App Security identifies sign-ins from a risky IP address, for example, using an anonymous browser or VPN. To use this feature, you must have an Microsoft 365 (Office 365) E5 license (https://docs.microsoft.com/en-us/defender-cloud-apps/get-started?culture=fr-fr&country=FR).

- **Effort:** master

- **Changelog:**

    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Microsoft 365 (Office 365) MailBoxAuditBypassAssociation Option Implementation</summary>


Detects the implementation of a MailBoxAuditBypassAssociation option in Microsoft 365 (Office 365). This option is used when you configure a user or computer account to bypass mailbox audit logging, access or actions taken by the user or computer account to any mailbox isn't logged.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Filter Policy Removed</summary>


Detects when a malware policy has been deleted in Microsoft 365 (Office 365). A malware filter policy is used to alert administrators that an internal user sent a message that contained malware.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Filter Rule Deletion</summary>


Detects when a malware filter rule has been deleted in Microsoft 365 (Office 365). The malware filter rule specifies the priority and recipient filters (who the policy applies to) for a malware filter policy.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Uploaded On OneDrive</summary>


Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to OneDrive. Attackers can use this method to propagate through the network.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Malware Uploaded On SharePoint</summary>


Detects when Microsoft 365 (Office 365) identifies a malicious file uploaded to SharePoint. Attackers can use this method to propagate through the network.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Mass Download By A Single User</summary>


Identifies when Microsoft Cloud App Security reports that a single user performs more than 50 downloads within 1 minute.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft 365 (Office 365) Potential Ransomware Activity Detected</summary>


Detects when Microsoft Cloud App Security reports that a user has uploaded files to the cloud that might be infected with ransomware.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft 365 (Office 365) Safe Attachment Rule Disabled</summary>


Detects when the safe attachment rule has been deleted in Microsoft 365 (Office 365). Safe Attachments is a feature in Microsoft Defender for Microsoft 365 (Office 365) that opens email attachments in a special hypervisor environment to detect malicious activity.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Safelinks Disabled</summary>


Detects when a safelink rule has been deleted in Microsoft 365 (Office 365). Safe Links is a feature in Defender for Microsoft 365 (Office 365) that provides URL scanning and rewriting of inbound email messages in mail flow, and time-of-click verification of URLs and links in email messages and other locations.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft 365 (Office 365) Unusual Volume Of File Deletion</summary>


Detects when Microsoft Cloud App Security identifies that a user has deleted an unusually large volume of files.

- **Effort:** master

- **Changelog:**

    - 09/10/2023 - major - Fix field names to match the current parser.

</details>
            
<details>
<summary>Microsoft Defender Antivirus Threat Detected</summary>


Detection of a windows defender alert indicating the presence of potential malware

- **Effort:** advanced

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Microsoft Defender For Identity High Severity Alert</summary>


Microsoft Defender For Identity raised an alert as High severity. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender For Identity Low Severity Alert</summary>


Microsoft Defender For Identity raised an alert as Low severity. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender For Identity Medium Severity Alert</summary>


Microsoft Defender For Identity raised an alert as Medium severity. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (Graph API) Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (Graph API) Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender For Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (GraphAPI) Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR Alert</summary>


Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Cloud App Security Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.
    - 07/09/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Office 365 Alert</summary>


Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Office Creating Suspicious File</summary>


Detects Microsoft Office process (word, excel, powerpoint) creating a suspicious file which corresponds to a script or an executable. This behavior highly corresponds to an executed macro which loads an installation script or a malware payload. The rule requires to log for File Creations to work properly, which can be done through Sysmon Event ID 11.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Office Product Spawning Windows Shell</summary>


Detects a Windows command or scripting interpreter executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware.

- **Effort:** master

- **Changelog:**

    - 20/12/2024 - minor - Adding minor filter on a process parent name.
    - 23/01/2024 - minor - Adding elements to increase detection and filters to reduce false positives.
    - 13/09/2024 - major - Adding filters to reduce false positives and updated the effort level to master as it is a rule highly dependent on the environment.
    - 10/10/2025 - minor - Adding parent process command line as a newly displayed field in the alert.

</details>
            
<details>
<summary>Microsoft Office Spawning Script</summary>


Detects Microsoft Office process (word, excel, powerpoint) spawning wscript.exe or cscript.exe. This typically indicates the parent process launched a malicious macro, or run an exploit. This infection vector is very common and could lead to the deployment of harmful malware. 

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Sentinel High Severity New Alert</summary>


Microsoft Sentinel raised an High severity new alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Sentinel Low Severity New Alert</summary>


Microsoft Sentinel raised an Low severity new alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Sentinel Medium Severity New Alert</summary>


Microsoft Sentinel raised an Medium severity new alert.

- **Effort:** master

</details>
    
<details>
<summary>Mimecast Email Security Malicious QRCode Not Denied</summary>


Detects a malicious qrcode in an email not denied by Mimecast.

- **Effort:** master

</details>
    
<details>
<summary>Mimecast Email Security Spam Not Denied</summary>


Detects when a spam has been detected by Mimecast and was not denied.

- **Effort:** master

</details>
    
<details>
<summary>Mimecast Email Security Virus Not Denied</summary>


Detects when a virus signature has been detected by Mimecast and was not denied.

- **Effort:** master

</details>
    
<details>
<summary>Okta Security Threat Detected</summary>


Detects when a security threat is detected in Okta.

- **Effort:** intermediate

</details>
    
<details>
<summary>Palo Alto Cortex XDR (EDR) Alert (Critical Severity)</summary>


A Palo Alto Cortex XDR (EDR) agent has raised an alert of critical severity (only DETECTED and not SCANNED status).

- **Effort:** master

</details>
    
<details>
<summary>Palo Alto Cortex XDR (EDR) Alert Not Blocked (High Severity)</summary>


A Palo Alto Cortex XDR (EDR) agent has raised an alert of high severity that was not blocked.

- **Effort:** master

- **Changelog:**

    - 10/03/2025 - minor - Update severity to match the severity level from the editor
    - 25/02/2026 - minor - Update rule type to integration
    - 04/03/2026 - minor - Similarity strategy updated to caseID

</details>
            
<details>
<summary>Palo Alto Cortex XDR (EDR) Alert Not Blocked (Low Severity)</summary>


A Palo Alto Cortex XDR (EDR) agent has raised an alert of low severity that was not blocked.

- **Effort:** master

- **Changelog:**

    - 10/03/2025 - minor - Update severity to match the severity level from the editor
    - 25/02/2026 - minor - Update rule type to integration
    - 04/03/2026 - minor - Similarity strategy updated to caseID

</details>
            
<details>
<summary>Palo Alto Cortex XDR (EDR) Alert Not Blocked (Medium Severity)</summary>


A Palo Alto Cortex XDR (EDR) agent has raised an alert of medium severity that was not blocked.

- **Effort:** master

- **Changelog:**

    - 10/03/2025 - minor - Update severity to match the severity level from the editor
    - 25/02/2026 - minor - Update rule type to integration
    - 04/03/2026 - minor - Similarity strategy updated to caseID

</details>
            
<details>
<summary>Palo Alto NGFW Threat Detection Critical</summary>


Palo Alto Next-Generation Firewall raised an alert for a threat detection with critical severity.

- **Effort:** master

</details>
    
<details>
<summary>Registry Value Changed Via Windows Run Dialog</summary>


Detects when a user enters a suspicious url command in the windows run dialog. Could be linked to ClickFix. For this rule, you will need to add auditing permissions to this specific key and enable audit registry.

- **Effort:** master

</details>
    
<details>
<summary>SentinelOne EDR Agent Disabled</summary>


A SentinelOne EDR agent has been disabled according to SentinelOne logs.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Custom Rule Alert</summary>


A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively</summary>


A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Not Mitigated</summary>


A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR SSO User Added</summary>


A SSO User was added.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Malicious)</summary>


A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Suspicious)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Kill Success</summary>


A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Failed</summary>


A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Success</summary>


A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Remediate Success</summary>


A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Failed To Log In To The Management Console</summary>


A user has failed to log in to the management console.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Logged In To The Management Console</summary>


A user has logged in to the management console.

- **Effort:** master

- **Changelog:**

    - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Sigma Intelligence Pangolin8RAT Working Directory File Artifacts</summary>


Detects access to filesystem artifacts associated with Pangolin8RAT.

- **Effort:** intermediate

</details>
    
<details>
<summary>Sigma Intelligence Windows DRILLAPP Malware</summary>


Sigma RULE to detect DrillAPP or other malicious launch of edge to disable security measures and abuse permissions.

- **Effort:** intermediate

</details>
    
<details>
<summary>Sophos EDR Application Blocked</summary>


Sophos EDR detected a potentially malicious application and blocked it.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Sophos EDR Application Detected</summary>


Sophos EDR detected a potentially malicious application.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Sophos EDR CorePUA Clean</summary>


Sophos EDR detected a potentially unwanted application and cleaned it.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Sophos EDR CorePUA Detection</summary>


Sophos EDR detected a potentially unwanted application.

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SquirrelWaffle Malspam Execution Loading DLL</summary>


Detects cscript running suspicious command to load a DLL. This behavior has been detected in SquirrelWaffle campaign.

- **Effort:** intermediate

</details>
    
<details>
<summary>Stormshield Ses Critical Block</summary>


Stormshield Endpoint Security block execution with critical severity

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Stormshield Ses Critical Not Block</summary>


Stormshield Endpoint Security detect threat with critical severity that was not blocked

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Stormshield Ses Emergency Block</summary>


Stormshield Endpoint Security block execution with emergency severity

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Suricata Attempted Administrator Privilege Gain High Severity Alert</summary>


Detects a high severity alert triggered from Suricata Attempted Administrator Privilege Gain category.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Suricata Exploit Kit Activity Detected High Severity Alert</summary>


Detects a high severity alert triggered from Suricata Exploit Kit Activity Detected category.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Suricata Web Application Attack High Severity Alert</summary>


Detects a high severity alert triggered from Suricata Web Application Attack category.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Suspicious DLL Loaded Via Office Applications</summary>


Detects suspicious DLL being loaded by an Microsoft Office Product. Considered as suspects are some .NET DLLs, clr.dll, GAC DLL, DSParse (Active Directoryi services API) or Kerberos DLLs which may be loaded by MS Office processes when executing a potentially malicious macro. The prerequisite is to log the Sysmon Event ID 7 (DLL image loaded by process). 

- **Effort:** master

</details>
    
<details>
<summary>Suspicious Outlook Child Process</summary>


Detects suspicious child processes of Microsoft Outlook. These child processes are often associated with spearphishing activity.

- **Effort:** intermediate

</details>
    
<details>
<summary>Sysmon Windows File Block Executable</summary>


Sysmon has blocked an executable file from being written to the disk. This could be a malicious binary to investigate.  

- **Effort:** master

</details>
    
<details>
<summary>TEHTRIS EDR Alert</summary>


Tehtris EDR telemetry has raised an alert.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Data Loss Prevention Alert</summary>


Trend Micro Apex One has raised an alert for data loss prevention.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Malware Alert</summary>


Trend Micro Apex One has detected a malware.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Critical Severity Alert</summary>


Detects when a critical alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Low Severity Alert</summary>


Detects when a low alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Medium Severity Alert</summary>


Detects when a medium alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench high Severity Alert</summary>


Detects when a high alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Vectra General Threat Detection</summary>


Vectra Cognito detected a potential threat. This is a very generic rule to raise as much alerts as possible from Vectra detections however RECONNAISSANCE and INFO categories have been removed to avoid spamming.

- **Effort:** master

- **Changelog:**

    - 06/10/2025 - minor - Update sources link
    - 12/11/2025 - minor - Update rule type to integration

</details>
            
<details>
<summary>Winword Document Droppers</summary>


Detects specific process characteristics of word document droppers. This techniques has been used by Maze ransomware operators.

- **Effort:** elementary

</details>
    
<details>
<summary>WithSecure Elements Critical Severity</summary>


WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>WithSecure Elements Warning Severity</summary>


Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).

- **Effort:** master

- **Changelog:**

    - 07/04/2025 - minor - Similarity strategy changed to avoid too much grouping
    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>ZIP LNK Infection Chain</summary>


Detection of an ZIP download followed by a child-process of explorer, followed by multiple Windows processes.This is widely used as an infection chain mechanism.

- **Effort:** advanced

- **Changelog:**

    - 18/11/2024 - minor - Filter modified to avoid some false positives.
    - 19/09/2024 - minor - File paths added to filter some false positives.

</details>
            
<details>
<summary>Zscaler ZIA Malicious Threat</summary>


Zscaler Internet Access has detected a network traffic as malicious

- **Effort:** master

</details>
    
<details>
<summary>Zscaler ZIA Malicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
<details>
<summary>Zscaler ZIA Suspicious Threat</summary>


Zscaler Internet Access has detected a network traffic as malicious

- **Effort:** master

</details>
    
<details>
<summary>Zscaler ZIA Suspicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
**System Services**

<details>
<summary>Bitdefender GravityZone Endpoint Detection</summary>


Bitdefender GravityZone detected a malicious activity on an endpoint

- **Effort:** master

- **Changelog:**

    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Check Point Harmony Mobile Application Forbidden</summary>


Detects when someone attempts to access/use a forbidden application.

- **Effort:** master

</details>
    
<details>
<summary>Correlation Impacket Smbexec</summary>


This rule detects the execution of smbexec via the relevant share pattern name 

- **Effort:** elementary

</details>
    
<details>
<summary>Credential Dumping Tools Service Execution</summary>


Detects well-known credential dumping tools execution via service execution

- **Effort:** intermediate

</details>
    
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Critical Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection High Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Informational Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Low Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Identity Protection Detection Medium Severity</summary>


CrowdStrike Falcon raised an alert for an Identity-based detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Critical Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with critical severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with the new EppDetectionSummaryEvent type.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection High Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with high severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 02/10/2025 - minor - Alert severity updated to match Crowdstrike's values and sekoia rule CrowdStrike Falcon Intrusion Detection High Severity
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Informational Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with informational severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Low Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with low severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>CrowdStrike Falcon Intrusion Detection Medium Severity EppDetection</summary>


CrowdStrike Falcon agent raised an alert for an intrusion detection with medium severity with the new EppDetectionSummaryEvent.

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration
    - 05/08/2025 - minor - Alert severity updated to match Crowdstrike's values

</details>
            
<details>
<summary>Csrss Child Found</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.

- **Effort:** advanced

- **Changelog:**

    - 23/12/2025 - minor - Rule was moved to advanced effort level considering the number of alerts and addtional filters were added.
    - 16/12/2024 - minor - Improve pattern mandatory fields and add filter to reduce false positives

</details>
            
<details>
<summary>Csrss Wrong Parent</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Cybereason EDR Alert</summary>


Cybereason EDR telemetry has raised an alert

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cybereason EDR Malware Detection</summary>


Cybereason EDR telemetry has detected a malware

- **Effort:** master

- **Changelog:**

    - 30/01/2026 - minor - Updating similarity to use malop id.
    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Dllhost Wrong Parent</summary>


Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.

</details>
            
<details>
<summary>Exfiltration Via Pscp</summary>


Detects the use of pscp which is a file sharing services.

- **Effort:** advanced

</details>
    
<details>
<summary>Gpscript Suspicious Parent</summary>


Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.

- **Effort:** intermediate

- **Changelog:**

    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Login Brute-Force Successful On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and succeeded to login.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Login Failed Brute-Force On SentinelOne EDR Management Console</summary>


A user has attempted to login several times (brute-force) on the SentinelOne EDR Management Console and failed every time.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>Logonui Wrong Parent</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 07/06/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Lsass Wrong Parent</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.

</details>
            
<details>
<summary>Malicious Service Installations</summary>


Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Malware Outbreak</summary>


Spots a peak of malware detection by windows defender on this perimeter.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Metasploit PSExec Service Creation</summary>


Detects Metasploit service creation when using the PSExec module. The ImagePath here is usually a malicious command line using powershell.exe and/or cmd.exe.

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft Defender Antivirus Threat Detected</summary>


Detection of a windows defender alert indicating the presence of potential malware

- **Effort:** advanced

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Microsoft Defender XDR (Graph API) Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (Graph API) Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender For Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR (GraphAPI) Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Defender XDR Alert</summary>


Microsoft Defender XDR has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Cloud App Security Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Cloud App Security. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 13/09/2024 - major - Update service name value following Microsoft change
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.
    - 07/09/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Data Loss Prevention Alert</summary>


Microsoft Defender XDR has raised an alert for Data Loss Prevention. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Endpoint Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Defender for Endpoint. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Entra ID Protection Alert</summary>


Microsoft Defender XDR has raised an alert for Microsoft Entra ID Protection. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 12/11/2025 - minor - Update rule type to integration
    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Microsoft Defender XDR Office 365 Alert</summary>


Microsoft Defender XDR for Office 365 has raised an alert. The alert info and evidence events are grouped with the similarity into the same Sekoia.io alert.

- **Effort:** master

- **Changelog:**

    - 03/06/2026 - major - Added a new condition to match only on alerts to avoid false positives.

</details>
            
<details>
<summary>Mshta Command From A Scheduled Task</summary>


Detects when an attacker leverage the Microsoft Windows Scheduled task feature to run the mshta.exe process. This is a common usage of a living-off-the-land binary, frequently abused for malicous purposes and not common nowadays in IT administration.

- **Effort:** intermediate

</details>
    
<details>
<summary>Okta Security Threat Detected</summary>


Detects when a security threat is detected in Okta.

- **Effort:** intermediate

</details>
    
<details>
<summary>OneNote Suspicious Children Process</summary>


In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.

- **Effort:** advanced

- **Changelog:**

    - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.

</details>
            
<details>
<summary>Palo Alto NGFW Threat Detection Critical</summary>


Palo Alto Next-Generation Firewall raised an alert for a threat detection with critical severity.

- **Effort:** master

</details>
    
<details>
<summary>PsExec Process</summary>


Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Rare Logonui Child Found</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.

- **Effort:** advanced

- **Changelog:**

    - 17/01/2025 - minor - Adding filter to reduce false positives.

</details>
            
<details>
<summary>Rare Lsass Child Found</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.

- **Effort:** intermediate

</details>
    
<details>
<summary>Searchindexer Wrong Parent</summary>


Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Searchprotocolhost Child Found</summary>


SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 17/03/2025 - major - Rule changed to effort master, and filter added to reduce false positives.

</details>
            
<details>
<summary>Searchprotocolhost Wrong Parent</summary>


Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 12/03/2024 - minor - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>SentinelOne EDR Agent Disabled</summary>


A SentinelOne EDR agent has been disabled according to SentinelOne logs.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Custom Rule Alert</summary>


A SentinelOne EDR agent has detected a threat related to a Custom Rule and raised an alert for it.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Detected And Mitigated Preemptively</summary>


A SentinelOne EDR agent has detected a malicious threat which has been mitigated preemptively, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Malicious Threat Not Mitigated</summary>


A SentinelOne EDR agent has detected a threat but did not mitigate it, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR SSO User Added</summary>


A SSO User was added.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Suspicious Threat Not Mitigated (Medium Confidence)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious) but did not mitigate it. This is all defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Malicious)</summary>


A SentinelOne EDR agent has detected a threat with a high confidence level (malicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Detected (Suspicious)</summary>


A SentinelOne EDR agent has detected a threat with a medium confidence level (suspicious).

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration
    - 24/07/2026 - minor - Update rule similarity to threatId.

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Kill Success</summary>


A SentinelOne EDR agent has detected and killed a threat (usually kills the malicious process), defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Failed</summary>


A SentinelOne EDR agent has failed to quarantine a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Quarantine Success</summary>


A SentinelOne EDR agent has detected and quarantined a threat with success, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR Threat Mitigation Report Remediate Success</summary>


A SentinelOne EDR agent has remediated a threat, defined by the action.type field's value.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Failed To Log In To The Management Console</summary>


A user has failed to log in to the management console.

- **Effort:** master

- **Changelog:**

    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>SentinelOne EDR User Logged In To The Management Console</summary>


A user has logged in to the management console.

- **Effort:** master

- **Changelog:**

    - 24/03/2023 - minor - Adjusting displayed columns when the rule triggers an alert. Now timestamp and username will be displayed.
    - 02/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Smbexec.py Service Installation</summary>


Detects the use of smbexec.py tool by detecting a specific service installation

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Smss Wrong Parent</summary>


Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 05/04/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>SolarWinds Suspicious File Creation</summary>


Detects SolarWinds process creating a file with a suspicious extension. The process solarwinds.businesslayerhost.exe created an unexpected file whose extension is ".exe", ".ps1", ".jpg", ".png" or ".dll".

- **Effort:** intermediate

</details>
    
<details>
<summary>SolarWinds Wrong Child Process</summary>


Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.

- **Effort:** intermediate

- **Changelog:**

    - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
    - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs

</details>
            
<details>
<summary>Spoolsv Wrong Parent</summary>


Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.

</details>
            
<details>
<summary>Suspicious Commands From MS SQL Server Shell</summary>


Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious DNS Child Process</summary>


Detects suspicious processes spawned by the dns.exe process. It could be a great indication of the exploitation of the DNS RCE bug reported in CVE-2020-1350 (SIGRED).

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious PsExec Execution</summary>


Detects execution of PsExec, different from the Sysinternals one. This rule helps to filter out the noise if PsExec is used for legit purposes or if attacker uses a different PsExec client other than Sysinternals one. The prerequisite is to log the Event ID 5145 (by setting "Audit Policy > Object Access > Audit Detailed File Share" to Success/Failure).

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Svchost Wrong Parent</summary>


Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - minor - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 31/01/2024 - minor - Adding filters to reduce false positives
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.

</details>
            
<details>
<summary>TEHTRIS EDR Alert</summary>


Tehtris EDR telemetry has raised an alert.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Taskhost Wrong Parent</summary>


Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Taskhost or Taskhostw Suspicious Child Found</summary>


Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
    - 13/02/2025 - minor - Adding new filters to reduce false positives.

</details>
            
<details>
<summary>Taskhostw Wrong Parent</summary>


Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>Trend Micro Apex One Data Loss Prevention Alert</summary>


Trend Micro Apex One has raised an alert for data loss prevention.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Malware Alert</summary>


Trend Micro Apex One has detected a malware.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Critical Severity Alert</summary>


Detects when a critical alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Low Severity Alert</summary>


Detects when a low alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench Medium Severity Alert</summary>


Detects when a medium alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Vision One Workbench high Severity Alert</summary>


Detects when a high alert severity is raised by Trend Micro Vision One Workbench.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Usage Of Procdump With Common Arguments</summary>


Detects the usage of Procdump sysinternals tool with some common arguments and followed by common patterns.

- **Effort:** advanced

- **Changelog:**

    - 15/01/2024 - minor - Added filter to reduce false positives.
    - 22/04/2025 - minor - Added filter to reduce false positives and change effort level.

</details>
            
<details>
<summary>Usage Of Sysinternals Tools</summary>


Detects the usage of Sysinternals Tools due to accepteula key being added to Registry. The rule detects it either from the command line usage or from the regsitry events. For the later prerequisite is logging for registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** master

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>WMI Persistence Command Line Event Consumer</summary>


Detects WMI command line event consumers.

- **Effort:** elementary

</details>
    
<details>
<summary>Windows Suspicious Service Creation</summary>


Detects the creation of a new suspicious service - attacker could use MSRPC to create a remote service

- **Effort:** intermediate

- **Changelog:**

    - 28/10/2025 - minor - improve detection by adding pattern

</details>
            
<details>
<summary>Windows Update LolBins</summary>


This rule try to detect a suspicious behavior of wuauclt.exe (windows update client) that could be a lolbins. Wuauctl.exe could be used to execute a malicious program.

- **Effort:** elementary

- **Changelog:**

    - 24/03/2023 - minor - The legitimate DLL UpdateDeploymentProvider.dll is now excluded from the rule as it triggered several false positives.

</details>
            
<details>
<summary>Wininit Wrong Parent</summary>


Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.

</details>
            
<details>
<summary>Winlogon wrong parent</summary>


Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
    - 27/10/2026 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Winrshost Wrong Parent</summary>


Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>WithSecure Elements Critical Severity</summary>


WithSecure Elements has several modules. One constant is the severity of a raised event, which can be critical and therefore interesting to look at.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.

</details>
            
<details>
<summary>WithSecure Elements Warning Severity</summary>


Detects when WithSecure Elements raised an event with a warning (and is not blocked or quarantined).

- **Effort:** master

- **Changelog:**

    - 07/04/2025 - minor - Similarity strategy changed to avoid too much grouping
    - 18/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Wsmprovhost Wrong Parent</summary>


Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 25/10/2023 - minor - Adding filter to reduce false positives.
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Zscaler ZIA Malicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
<details>
<summary>Zscaler ZIA Suspicious Threat Outbreak</summary>


Spots a peak of malicious threat detection by Zscaler ZIA

- **Effort:** master

</details>
    
**Hijack Execution Flow**

<details>
<summary>DHCP Callout DLL Installation</summary>


Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).

- **Effort:** intermediate

</details>
    
<details>
<summary>DHCP Server Error Failed Loading the CallOut DLL</summary>


This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>DHCP Server Loaded the CallOut DLL</summary>


This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded. This would indicate a succesful attack against DHCP service allowing to disrupt the service or alter the integrity of the responses.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>DNS Server Error Failed Loading The ServerLevelPluginDLL</summary>


This rule detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded. This requires the dedicated Windows event provider Microsoft-Windows-DNS-Server-Service.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>DNS ServerLevelPluginDll Installation</summary>


Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
<details>
<summary>Dynamic Linker Hijacking From Environment Variable</summary>


LD_PRELOAD and LD_LIBRARY_PATH are environment variables used by the Operating System at the runtime to load shared objects (library.ies) when executing a new process, attacker can overwrite this variable to attempts a privileges escalation.

- **Effort:** master

- **Changelog:**

    - 11/07/2024 - minor - Added filter to reduce false positvives

</details>
            
<details>
<summary>Elevated Msiexec Via Repair Functionality</summary>


Detects when msiexec.exe is used with the repair functionality. The process gains elevated privileges. Attackers can use this to exploit the CVE-2024-38014.

- **Effort:** master

</details>
    
<details>
<summary>Elevated Shell Launched By Browser</summary>


Detects when openwith.exe is launched with privileges followed by a browser launching an elevated shell. Related to the CVE-2024-38014.

- **Effort:** master

</details>
    
<details>
<summary>Exploiting SetupComplete.cmd CVE-2019-1378</summary>


Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.

- **Effort:** intermediate

- **Changelog:**

    - 09/10/2025 - minor - Added filter for a new field to reduce false positvives.

</details>
            
<details>
<summary>Hijack Legit RDP Session To Move Laterally</summary>


Identifies suspicious file creations in the startup folder of a remote system. An adversary could abuse this to move laterally by dropping a malicious script or executable that will be executed after a reboot or user logon.

- **Effort:** intermediate

</details>
    
<details>
<summary>Linux Ldpreload Modification</summary>


Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process

- **Effort:** intermediate

</details>
    
<details>
<summary>Linux Shared Lib Injection Via Ldso Preload</summary>


Detect ld.so.preload modification for shared lib injection, technique used by attackers to load arbitrary code into process

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious DLL side loading from ProgramData</summary>


Detects suspicious DLL side-loading from C:\ProgramData where the DLL is not signed.

- **Effort:** intermediate

</details>
    
<details>
<summary>Svchost DLL Search Order Hijack</summary>


Detects svchost process hijacking through DLL loading. IKEEXT and SessionEnv service, as they call LoadLibrary on files that do not exist within C:\Windows\System32\ by default. An attacker can place their malicious logic within the PROCESS_ATTACH block of their library and restart the aforementioned services "svchost.exe -k netsvcs" to gain code execution on a remote machine.

- **Effort:** master

</details>
    
<details>
<summary>Werfault DLL Injection</summary>


Werfault DLL search order look first in the current file, which lets an attacker use th legitimate exe to run its own DLL.  

- **Effort:** intermediate

</details>
    
<details>
<summary>Windows Registry Persistence COM Search Order Hijacking</summary>


Detects potential COM object hijacking leveraging the COM Search Order. Logging for Registry events is needed, it can be done with Sysmon's Event IDs 12 and 13. Alert filters are highly encouraged for such kind of rule.

- **Effort:** master

- **Changelog:**

    - 11/01/2024 - minor - Adding filtering for some FPs
    - 18/08/2025 - major - Effort level moved to master. Pattern changed to enhance the detection scope. Filters were added to reduce false positives.

</details>
            
**Deploy Container**

<details>
<summary>Docker Escape Bind Mount</summary>


Catch Docker escape via mount escape followed by chroot 

- **Effort:** intermediate

</details>
    
**Cloud Administration Command**

<details>
<summary>WIZ Issues Critical Alert Raised</summary>


Detects when a critical alert from WIZ Issues is raised.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
## Persistence
**Boot or Logon Initialization Scripts**

<details>
<summary>Logon Scripts (UserInitMprLogonScript)</summary>


Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.

- **Effort:** advanced

</details>
    
<details>
<summary>Startup Item Created</summary>


Detects when a item is added to the startup directory. An attacker can use this establish persistence.

- **Effort:** intermediate

</details>
    
**Scheduled Task/Job**

<details>
<summary>BazarLoader Persistence Using Schtasks</summary>


Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>Blue Mockingbird Malware</summary>


Attempts to detect system changes made by Blue Mockingbird

- **Effort:** elementary

</details>
    
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Creation or Modification of a GPO Scheduled Task</summary>


Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cron Files Alteration</summary>


Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace App Script Scheduled Task</summary>


Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.

- **Effort:** advanced

</details>
    
<details>
<summary>Qakbot Persistence Using Schtasks</summary>


Detects possible Qakbot persistence using schtasks.

- **Effort:** intermediate

</details>
    
<details>
<summary>Remote Task Creation Via ATSVC Named Pipe</summary>


Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.

- **Effort:** intermediate

- **Changelog:**

    - 21/03/2024 - minor - change filter to ACL hex value

</details>
            
<details>
<summary>STRRAT Scheduled Task</summary>


Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'

- **Effort:** intermediate

</details>
    
<details>
<summary>Scheduled Task Creation By Non Privileged User</summary>


Detects scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 

- **Effort:** master

- **Changelog:**

    - 03/12/2025 - minor - Change rule effort level and update of rule name

</details>
            
<details>
<summary>Schtasks Persistence With High Privileges</summary>


Detection of scheduled task with high privileges used by attacker for persistence.

- **Effort:** elementary

</details>
    
<details>
<summary>Schtasks Suspicious Parent</summary>


Detects schtasks started from suspicious and/or unusual processes.

- **Effort:** intermediate

</details>
    
<details>
<summary>Spyware Persistence Using Schtasks</summary>


Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).

- **Effort:** intermediate

</details>
    
<details>
<summary>Windows Suspicious Scheduled Task Creation</summary>


The rule identify creation of new scheduled task who run suspicious commands.

- **Effort:** master

- **Changelog:**

    - 24/04/2025 - minor - Adding similarity strategy.
    - 03/12/2025 - major - Change rule effort level according to sigthings

</details>
            
**Registry Run Keys / Startup Folder**

<details>
<summary>Malware Persistence Registry Key</summary>


Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.

- **Effort:** master

- **Changelog:**

    - 30/09/2025 - minor - Update selection to improve detection
    - 28/08/2025 - minor - Filter some FPs on key values
    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs

</details>
            
**Valid Accounts**

<details>
<summary>Account Added To A Security Enabled Group</summary>


Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - add similarity strategy

</details>
            
<details>
<summary>Account Removed From A Security Enabled Group</summary>


Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - Add similarity strategy

</details>
            
<details>
<summary>Account Tampering - Suspicious Failed Logon Reasons</summary>


This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.

- **Effort:** advanced

- **Changelog:**

    - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Admin User RDP Remote Logon</summary>


Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Authentication Impossible Travel</summary>


Detects impossible travel when performing authentication from a source IP address, grouped by user name. This could require some alert filtering for some user generic accounts, and known IP address range. Microsoft / Office 365 format is not covered by this rule.

- **Effort:** master

- **Changelog:**

    - 27/07/2024 - major - review filter to avoid false positives
    - 30/08/2024 - minor - improve filter to avoid false positives
    - 30/01/2025 - major - Pattern rework with ECS fields only and simple authentication success use case
    - 04/02/2025 - major - Excluding Microsoft 365 format to avoid false positives
    - 14/08/2025 - major - Excluding Wiz Audit Logs format to avoid false positives
    - 29/10/2026 - major - Excluding Entra ID following parser changes to avoid false positives. A dedicated rule for Entra ID exists and is called "Microsoft Entra ID (Azure AD) Impossible Travel".

</details>
            
<details>
<summary>Broadcom Edge Secure Web Gateway High Threat</summary>


Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.

- **Effort:** master

</details>
    
<details>
<summary>Brute-Force On Fortinet Firewall Login</summary>


Spots many failed attempts to log on an administration interface.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and add intake field format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Denied Access To Remote Desktop</summary>


Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.

- **Effort:** intermediate

- **Changelog:**

    - 19/10/2023 - minor - Minor change in selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Dscl Authonly</summary>


Detects the use of the command dscl with authonly used to verify the password of a user and for authentification. An attacker can abuse this command to gain credentials.

- **Effort:** advanced

</details>
    
<details>
<summary>Enable Root Account With Dsenableroot</summary>


Detects when root is enabled. Attackers can use this as a mean of persistence since root is disabled by default.

- **Effort:** elementary

</details>
    
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Flare Events Critical Severity Threat Exposure</summary>


Detects a high critical Flare exposure event from clear, deep, or dark web monitoring. This indicates a critical-risk threat indicator that requires rapid triage.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events High Severity Threat Exposure</summary>


Detects a high severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Informational Severity Threat Exposure</summary>


Detects a informational severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Leaked Credential With Password Exposure</summary>


Detects leaked credential events where a password is explicitly present in the exposure record, indicating elevated risk of account takeover.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Low Severity Threat Exposure</summary>


Detects a low severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Medium Severity Threat Exposure</summary>


Detects a medium severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Fortigate Firewall Successful External Login</summary>


Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Google Cloud Audit Logs Account Suspended</summary>


Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Added</summary>


Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Authorized</summary>


Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.

- **Effort:** master

</details>
    
<details>
<summary>Google Cloud Audit Logs Attack Warning</summary>


Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Workspace Account Warning</summary>


Detects a suspicious login, leaked password, or account disabled following suspicious activity.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace Admin Creation</summary>


Detects when an admin is created or when his role is changed.

- **Effort:** master

- **Changelog:**

    - 22/05/2024 - minor - Adding new element to increase detection.

</details>
            
<details>
<summary>Google Workspace Suspicious Login</summary>


Detects a suspicious login reported by google.

- **Effort:** master

</details>
    
<details>
<summary>Login Brute-Force On Fortinet Firewall From Internet</summary>


Detects successful access to administration console of a firewall after several failure from Internet.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only and intake format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Login Brute-Force On FreeRadius</summary>


A user has attempted to login several times (brute-force) with error then one success.

- **Effort:** intermediate

</details>
    
<details>
<summary>Login Brute-Force On Sekoia.io</summary>


Detects successful access to Sekoia.io after several failure.

- **Effort:** intermediate

- **Changelog:**

    - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.

</details>
            
<details>
<summary>Microsoft 365 Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)

- **Effort:** master

</details>
    
<details>
<summary>Netskope Admin Audit High Severity</summary>


Audit events detection for admin activites that differ from authentications, with high severity level according to Netskope.

- **Effort:** master

- **Changelog:**

    - 29/01/2025 - minor - Rework pattern for high severity events only and filter out authentication events.
    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Detected</summary>


Netskope identified a malware with a high severity (excluding Patient Zero here)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Patient Zero Detected</summary>


Netskope identified a malware as Patient Zero.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Potential Brute Force On Protected Applications</summary>


Detects potential brute force on Netskope protected applications with more than 10 failures in 5 minutes for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute Force On Protected Applications</summary>


Detects successful brute force on Netskope protected applications after more than 5 failures in 5 minutes and one success for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute-Force On Management Console</summary>


Detects successful access to Netskope management console after more than 10 failures in 5 minutes for the same user name.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Web Isolation On Suspicious Domain</summary>


Netskope identified a suspicious domain and triggered web sandboxing (RBI)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Okta Access To Admin Console Denied</summary>


Detects when an attempt was made to access the Okta Admin Console from an interactive user account but failed.

- **Effort:** master

</details>
    
<details>
<summary>Okta Many Passwords Reset Attempt</summary>


This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Suspicious Activity Reported</summary>


Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Unauthorized Access to App</summary>


An user tries to access an unauthorized application.

- **Effort:** master

</details>
    
<details>
<summary>User Added To Admin Group Via Cmd</summary>


Detects the use of different commands to add a user to an admin group.

- **Effort:** advanced

</details>
    
<details>
<summary>User Added to Local Administrators</summary>


Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 04/04/2024 - major - Rule's pattern field changed
    - 01/06/2026 - major - selection improvements to better align with the detection objective

</details>
            
**Account Manipulation**

<details>
<summary>AWS CloudTrail IAM Failed User Creation</summary>


Detects an attemp to create a user account where the result is an explicit denied.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail IAM Password Policy Updated</summary>


Detects an update to the password policy. This could be an attempt to lower accounts security level.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail IAM Policy Changed</summary>


Detects change on AWS IAM Policy

- **Effort:** master

</details>
    
<details>
<summary>AWS CloudTrail Root ConsoleLogin</summary>


Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail Route 53 Domain Transfer Attempt</summary>


Detects when a request in success or failure is made to transfer a domain name to an other AWS account

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail Route 53 Domain Transfer Lock Disabled</summary>


Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.

- **Effort:** elementary

</details>
    
<details>
<summary>Active Directory Delegate To KRBTGT Service</summary>


Detects potential persistence installation from an already compromised administrator domain account. The attacker will create a TGT and abuse a service account with the constrained delegation and update it with the krbtgt service. The detection relies on the Event ID 4738.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory Replication User Backdoor</summary>


Backdooring domain object to grant the rights associated with DCSync to regular user or machine account, this technics is often used to give ResetPassword or WriteMembers or DCSync permission(s) for persistency on a domain.

- **Effort:** intermediate

- **Changelog:**

    - 15/10/2024 - major - Update pattern to avoid false positives and change rule effort
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory User Backdoors</summary>


Detects scenarios where the attacker controls another user or computer account without having to use their credentials.

- **Effort:** intermediate

- **Changelog:**

    - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Add User to Privileged Group</summary>


Add user in a potential privileged group which can be used to elevate privileges on the system.

- **Effort:** advanced

</details>
    
<details>
<summary>Enabling Restricted Admin Mode</summary>


Detects when the restricted admin mode is enabled.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace Admin Modification</summary>


Detects when an admin is modified.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Domain Delegation</summary>


Detects when a domain delegation is granted.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure</summary>


Detects self-service password reset in failure for various reasons (except licence or policy ones)

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and specific intake field

</details>
            
<details>
<summary>Mimikatz Basic Commands</summary>


Detects Mimikatz most popular commands. 

- **Effort:** elementary

- **Changelog:**

    - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.

</details>
            
<details>
<summary>Okta Admin Privilege Granted</summary>


Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Application deleted</summary>


An application has been delete on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Application modified</summary>


An application has been updated on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta User Account Deactivated</summary>


A user account has been deactivated in Okta.

- **Effort:** master

</details>
    
<details>
<summary>Okta User Impersonation Access</summary>


A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.

- **Effort:** advanced

</details>
    
<details>
<summary>Password Change On Directory Service Restore Mode (DSRM) Account</summary>


The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Privileged AD Builtin Group Modified</summary>


Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).

- **Effort:** master

- **Changelog:**

    - 10/07/2023 - minor - Added AD groups and change to effort master.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>SSH Authorized Key Alteration</summary>


The file authorized_keys is used by SSH server to identify SSH keys that are authorized to connect to the host, alteration of one of those files might indicate a user compromision.

- **Effort:** advanced

</details>
    
<details>
<summary>SeEnableDelegationPrivilege Granted To User Or Machine In Active Directory</summary>


Detects the SeEnableDelegationPrivilege right in Active Directory granted to a user of a computer, it would allow control of other AD user objects

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 04/03/2026 - minor - Fix small typo in rule name.

</details>
            
<details>
<summary>User Added to Local Administrators</summary>


Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 04/04/2024 - major - Rule's pattern field changed
    - 01/06/2026 - major - selection improvements to better align with the detection objective

</details>
            
<details>
<summary>Varonis Many Accounts Disabled</summary>


This rule identifies a high number of account disabled.

- **Effort:** master

</details>
    
**Web Shell**

<details>
<summary>Antivirus Web Shell Detection</summary>


Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).

- **Effort:** elementary

</details>
    
**Modify Registry**

<details>
<summary>Blue Mockingbird Malware</summary>


Attempts to detect system changes made by Blue Mockingbird

- **Effort:** elementary

</details>
    
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>DHCP Callout DLL Installation</summary>


Detects the installation of a Callout DLL via CalloutDlls and CalloutEnabled parameter in Registry, which can be used to execute code in context of the DHCP server (restart required).

- **Effort:** intermediate

</details>
    
<details>
<summary>DNS ServerLevelPluginDll Installation</summary>


Detects the installation of a plugin DLL via ServerLevelPluginDll parameter in Windows Registry or in command line, which can be used to execute code in context of the DNS server (restart required). To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
<details>
<summary>Disable .NET ETW Through COMPlus_ETWEnabled</summary>


Detects potential adversaries stopping ETW providers recording loaded .NET assemblies. Prerequisites are logging for Registry events or logging command line parameters (both is better). Careful for registry events, if SwiftOnSecurity's SYSMON default configuration is used, you will need to update the configuration to include the .NETFramework registry key path. Same issue with Windows 4657 EventID logging, the registry path must be specified.

- **Effort:** intermediate

</details>
    
<details>
<summary>Disable Security Events Logging Adding Reg Key MiniNt</summary>


Detects the addition of a key 'MiniNt' to the registry. Upon a reboot, Windows Event Log service will stopped write events.  Prerequisites: Logging for Registry events for this specific registry key is needed in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
<details>
<summary>Disable Workstation Lock</summary>


Registry change in order to disable the ability to lock the computer by using CTRL+ALT+DELETE or CTRL+L. This registry key does not exist by default. Its creation is suspicious and the value set to "1" means an activation. It has been used by FatalRAT, but other attacker/malware could probably use it. This rule needs Windows Registry changes (add,modification,deletion) logging which can be done through Sysmon Event IDs 12,13,14.

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Disabling SmartScreen Via Registry</summary>


Detects when a user disables smartscreen.

- **Effort:** elementary

</details>
    
<details>
<summary>FlowCloud Malware</summary>


Detects FlowCloud malware from threat group TA410. This requires Windows Event registry logging.

- **Effort:** elementary

</details>
    
<details>
<summary>LanManServer Registry Modify</summary>


Detects when the LanManServer registry sub-key MaxMpxCt is modified. An attacker can modified this value to increase the maximum number of outstanding client requests supported. 

- **Effort:** elementary

</details>
    
<details>
<summary>NetNTLM Downgrade Attack</summary>


Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>OceanLotus Registry Activity</summary>


Detects registry keys created in OceanLotus (also known as APT32) attack. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>RDP Port Change Using Powershell</summary>


Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 

- **Effort:** intermediate

</details>
    
<details>
<summary>RDP Sensitive Settings Changed</summary>


Detects changes to RDP terminal service sensitive settings. Logging for registry events is needed in the Sysmon configuration (events 12 and 13).

- **Effort:** advanced

</details>
    
<details>
<summary>RedMimicry Winnti Playbook Registry Manipulation</summary>


Detects actions caused by the RedMimicry Winnti playbook. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).

- **Effort:** elementary

</details>
    
<details>
<summary>Remote Registry Management Using Reg Utility</summary>


Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Desktopimgdownldr Execution</summary>


Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious New Printer Ports In Registry</summary>


Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
<details>
<summary>Ursnif Registry Key</summary>


Detects a new registry key created by Ursnif malware. The rule requires to log for Registry Events, which can be done using SYsmon's Event IDs 12,13 and 14.

- **Effort:** elementary

</details>
    
<details>
<summary>Wdigest Enable UseLogonCredential</summary>


Detects modification of the Windows Registry value of HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential. This technique is used to extract passwords in clear-text using WDigest. The rule requires to log for Registry Events, which can be done using Sysmon Event IDs 12, 13 and 14.

- **Effort:** elementary

- **Changelog:**

    - 08/08/2024 - major - Rule's pattern field changed and pattern improved to cause less false positives.

</details>
            
<details>
<summary>Windows Defender Logging Modification Via Registry</summary>


Detects when the logging for defender is disabled in the registry.

- **Effort:** elementary

</details>
    
**Component Object Model Hijacking**

<details>
<summary>Windows Registry Persistence COM Key Linking</summary>


Detects COM object hijacking via TreatAs subkey. Logging for Registry events is needed in the Sysmon configuration with this kind of rule `<TargetObject name="testr12" condition="end with">\TreatAs\(Default)</TargetObject>`.

- **Effort:** master

- **Changelog:**

    - 14/12/2023 - minor - Exclude common legitimate processes

</details>
            
**Authentication Package**

<details>
<summary>Shell PID Injection</summary>


Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.

- **Effort:** intermediate

</details>
    
**External Remote Services**

<details>
<summary>Anomaly New PowerShell Remote Session</summary>


Detects when PowerShell remote sessions are created in a short amount of time.

- **Effort:** master

- **Changelog:**

    - 11/06/2024 - minor - Adding fields to be displayed in the alert.

</details>
            
<details>
<summary>Datadome Protection Intrusion Detection</summary>


Detects when Datadome protection raises an alert linked to intrusion. Datadome is used against fraud and bots.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>SecurityScorecard Vulnerability Assessment Scanner New Issues</summary>


Raises an alert when SecurityScorecard Vulnerability Assessment Scanner find new issues.

- **Effort:** master

- **Changelog:**

    - 15/01/2025 - minor - Adding format field to improve rules mapping
    - 09/09/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Apex One Intrusion Detection Alert</summary>


Trend Micro Apex One has raised an alert for an intrusion detection.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One High Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a high severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One Low Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a low severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Trend Micro Cloud One Medium Intrusion</summary>


Detects when Trend Micro EDR raised an alert for an intrusion with a medium severity level.

- **Effort:** master

- **Changelog:**

    - 25/02/2026 - minor - Update rule type to integration

</details>
            
**Create Account**

<details>
<summary>AWS Persistence By Creating KeyPair And SecurityGroup</summary>


Attackers can use AWS credentials to create a KeyPair and a SecurityGroup to have continuous access to the AWS account.

- **Effort:** master

</details>
    
<details>
<summary>CVE-2021-20021 SonicWall Unauthenticated Administrator Access</summary>


Detects the exploitation of SonicWall Unauthenticated Admin Access.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace User Creation</summary>


Detects when a new user is created.

- **Effort:** master

</details>
    
<details>
<summary>Impacket Addcomputer</summary>


Detects suspicious computer account creation based on impacket default pattern

- **Effort:** intermediate

- **Changelog:**

    - 05/08/2024 - major - improve selection to extend detection

</details>
            
<details>
<summary>Net.exe User Account Creation</summary>


Identifies creation of local users via the net.exe command

- **Effort:** master

</details>
    
<details>
<summary>Okta User Account Created</summary>


A user account has been created in Okta.

- **Effort:** master

</details>
    
<details>
<summary>Suspicious URL Requested By Curl Or Wget Commands</summary>


Correlation rule aiming to be multi-source to detect URL with suspicious files extensions (seen on a network level by proxies or firewalls) being requested by curl or wget processes (seen on a host level).

- **Effort:** advanced

- **Changelog:**

    - 23/09/2024 - major - Fixed an issue with the detection pattern.

</details>
            
<details>
<summary>Suspicious Windows ANONYMOUS LOGON Local Account Created</summary>


Detects the creation of suspicious accounts simliar to ANONYMOUS LOGON, such as using additional spaces. Created as a covering detection for attackers trying to created an ANONYMOUS LOGON account as it is an account named used in internal Windows events and frequently filtered by attackers.

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>User Account Created</summary>


Detects user creation on windows servers, which shouldn't happen in an Active Directory environment. Apply this on your windows server logs and not on your DC logs. One default account `defaultuser0` is excluded as only used during Windows set-up. This detection use Security Event ID 4720. 

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 10/07/2024 - minor - Adding filter and new elements to reduce false positives.
    - 12/07/2024 - minor - Changing similarity strategy.

</details>
            
**Office Application Startup**

<details>
<summary>IcedID Execution Using Excel</summary>


Detects Excel spawning a process (rundll32 or wmic) running suspicious command-line. This behaviour could correspond to IcedID activity. 

- **Effort:** elementary

</details>
    
<details>
<summary>Microsoft Office Startup Add-In</summary>


Detects add-ins that load when Microsoft Word or Excel starts (.wll/.xll are simply .dll fit for Word or Excel). The rule requires File Creation logging to work, which can be done using Sysmon Event ID 11.

- **Effort:** elementary

</details>
    
<details>
<summary>Office Application Startup Office Test</summary>


Detects the addition of office test registry that allows a user to specify an arbitrary DLL that will be executed everytime an Office application is started. An adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised system.

- **Effort:** elementary

</details>
    
<details>
<summary>Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting</summary>


Detects the modification of Outlook setting "LoadMacroProviderOnBoot" which if enabled allows the automatic loading of any configured VBA project/module. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

</details>
    
**Software Extensions**

<details>
<summary>Malicious Browser Extensions</summary>


Detects browser extensions being loaded with the --load-extension and -base-url options, which works on Chromium-based browsers. We are looking for potentially malicious browser extensions. These extensions can get access to informations.

- **Effort:** advanced

</details>
    
**BITS Jobs**

<details>
<summary>BITSAdmin Download</summary>


Detects command to download file using BITSAdmin, a built-in tool in Windows. This technique is used by several threat actors to download scripts or payloads on infected system.

- **Effort:** advanced

- **Changelog:**

    - 06/12/2023 - minor - Adding key words to increase detection.

</details>
            
**Traffic Signaling**

<details>
<summary>Binary List Tcp</summary>


A binary is trying to list TCP connections. The prerequisites are to enable monitoring of the open and openat syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
**Server Software Component**

<details>
<summary>Antivirus Web Shell Detection</summary>


Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).

- **Effort:** elementary

</details>
    
<details>
<summary>CVE-2021-34473 ProxyShell Attempt</summary>


Detects CVE-2021-34473 ProxyShell attempt against Microsoft Exchange Server, Remote Code Execution Vulnerability.

- **Effort:** advanced

</details>
    
<details>
<summary>Default User www data User Compromised</summary>


User www_data by default cannot log and use a shell, any syscall of type execve induce user compromise

- **Effort:** master

</details>
    
<details>
<summary>Exchange Server Spawning Suspicious Processes</summary>


Look for Microsoft Exchange Server’s Unified Messaging service spawning suspicious sub-processes, suggesting exploitation of CVE-2021-26857 vulnerability.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Exchange Server Creating Unusual Files</summary>


Look for Microsoft Exchange Server’s Unified Messaging service creating non-standard content on disk, which could indicate web shells or other malicious content, suggesting exploitation of CVE-2021-26858 vulnerability

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft IIS Module Installation</summary>


Detects the installation of a new IIS module from the command line. It can used used to backdoor an IIS/OWA/Sharepoint server.

- **Effort:** advanced

- **Changelog:**

    - 10/10/2024 - major - Adding new commands with powershell and changing effort level.

</details>
            
<details>
<summary>PowerCat Function Loading</summary>


Detect a basic execution of PowerCat. PowerCat is a PowerShell function allowing to do basic connections, file transfer, shells, relays, generate payloads.

- **Effort:** intermediate

</details>
    
<details>
<summary>ProxyShell Microsoft Exchange Suspicious Paths</summary>


Detects suspicious calls to Microsoft Exchange resources, in locations related to webshells observed in campaigns using this vulnerability.

- **Effort:** elementary

</details>
    
<details>
<summary>Webshell Creation</summary>


Detects possible webshell file creation. It requires File Creation monitoring, which can be done using Sysmon's Event ID 11. However the recommended SwiftOnSecurity configuration does not fully cover the needs for this rule, it needs to be updated with the proper file names extensions.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Create or Modify System Process**

<details>
<summary>APT29 Fake Google Update Service Install</summary>


This method detects malicious services mentioned in APT29 report by FireEye. The legitimate path for the Google update service is C:\Program Files (x86)\Google\Update\GoogleUpdate.exe so the service names and executable locations used by APT29 are specific enough to be detected in log files.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cobalt Strike Default Service Creation Usage</summary>


Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Csrss Child Found</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.

- **Effort:** advanced

- **Changelog:**

    - 23/12/2025 - minor - Rule was moved to advanced effort level considering the number of alerts and addtional filters were added.
    - 16/12/2024 - minor - Improve pattern mandatory fields and add filter to reduce false positives

</details>
            
<details>
<summary>Csrss Wrong Parent</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Dllhost Wrong Parent</summary>


Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.

</details>
            
<details>
<summary>Gpscript Suspicious Parent</summary>


Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.

- **Effort:** intermediate

- **Changelog:**

    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Logonui Wrong Parent</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 07/06/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Lsass Wrong Parent</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.

</details>
            
<details>
<summary>Malicious Service Installations</summary>


Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Mshta Command From A Scheduled Task</summary>


Detects when an attacker leverage the Microsoft Windows Scheduled task feature to run the mshta.exe process. This is a common usage of a living-off-the-land binary, frequently abused for malicous purposes and not common nowadays in IT administration.

- **Effort:** intermediate

</details>
    
<details>
<summary>New Service Creation</summary>


Detects creation of a new service from command line

- **Effort:** advanced

</details>
    
<details>
<summary>OneNote Suspicious Children Process</summary>


In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.

- **Effort:** advanced

- **Changelog:**

    - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.

</details>
            
<details>
<summary>Rare Logonui Child Found</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.

- **Effort:** advanced

- **Changelog:**

    - 17/01/2025 - minor - Adding filter to reduce false positives.

</details>
            
<details>
<summary>Rare Lsass Child Found</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.

- **Effort:** intermediate

</details>
    
<details>
<summary>Searchindexer Wrong Parent</summary>


Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Searchprotocolhost Child Found</summary>


SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 17/03/2025 - major - Rule changed to effort master, and filter added to reduce false positives.

</details>
            
<details>
<summary>Searchprotocolhost Wrong Parent</summary>


Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 12/03/2024 - minor - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Smss Wrong Parent</summary>


Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 05/04/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>SolarWinds Wrong Child Process</summary>


Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.

- **Effort:** intermediate

- **Changelog:**

    - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
    - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs

</details>
            
<details>
<summary>Spoolsv Wrong Parent</summary>


Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.

</details>
            
<details>
<summary>StoneDrill Service Install</summary>


This method detects a service install of the malicious Microsoft Network Realtime Inspection Service service described in StoneDrill report by Kaspersky 

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Commands From MS SQL Server Shell</summary>


Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.

- **Effort:** intermediate

</details>
    
<details>
<summary>Svchost Wrong Parent</summary>


Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - minor - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 31/01/2024 - minor - Adding filters to reduce false positives
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.

</details>
            
<details>
<summary>Taskhost Wrong Parent</summary>


Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Taskhost or Taskhostw Suspicious Child Found</summary>


Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
    - 13/02/2025 - minor - Adding new filters to reduce false positives.

</details>
            
<details>
<summary>Taskhostw Wrong Parent</summary>


Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>WMI Persistence Command Line Event Consumer</summary>


Detects WMI command line event consumers.

- **Effort:** elementary

</details>
    
<details>
<summary>Wininit Wrong Parent</summary>


Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.

</details>
            
<details>
<summary>Winlogon wrong parent</summary>


Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
    - 27/10/2026 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Winrshost Wrong Parent</summary>


Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>Wsmprovhost Wrong Parent</summary>


Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 25/10/2023 - minor - Adding filter to reduce false positives.
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
**Event Triggered Execution**

<details>
<summary>COM Hijack Via Sdclt</summary>


Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.

- **Effort:** intermediate

</details>
    
<details>
<summary>Change Default File Association</summary>


When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

- **Effort:** advanced

</details>
    
<details>
<summary>Component Object Model Hijacking</summary>


Detects component object model hijacking. An attacker can establish persistence with COM objects.

- **Effort:** advanced

</details>
    
<details>
<summary>Control Panel Items</summary>


Detects the malicious use of a control panel item

- **Effort:** advanced

</details>
    
<details>
<summary>HTML Smuggling Suspicious Usage</summary>


Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.

- **Effort:** advanced

- **Changelog:**

    - 08/04/2025 - minor - Change effort level and add filter to reduce false positives.

</details>
            
<details>
<summary>New DLL Added To AppCertDlls Registry Key</summary>


Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting</summary>


Detects the modification of Outlook setting "LoadMacroProviderOnBoot" which if enabled allows the automatic loading of any configured VBA project/module. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

</details>
    
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys</summary>


Detects persistence registry keys. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

</details>
    
<details>
<summary>Sticky Key Like Backdoor Usage</summary>


Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Suspicious Netsh DLL Persistence</summary>


Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Scripting In A WMI Consumer</summary>


Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.

- **Effort:** intermediate

</details>
    
<details>
<summary>WMI Event Subscription</summary>


Detects creation of WMI event subscription persistence method 

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>WMI Persistence Script Event Consumer File Write</summary>


Detects file writes through WMI script event consumer.

- **Effort:** advanced

</details>
    
**Boot or Logon Autostart Execution**

<details>
<summary>Autorun Keys Modification</summary>


Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** master

- **Changelog:**

    - 16/01/2025 - minor - Added filters to reduce false positives.

</details>
            
<details>
<summary>DLL Load via LSASS Registry Key</summary>


Detects a method to load DLL via LSASS process using an undocumented Registry key. Prerequisites are logging for Registry events. This can be done with Sysmon events 12, 13 and 14 and monitor `SYSTEM\CurrentControlSet\Services`.

- **Effort:** intermediate

</details>
    
<details>
<summary>Kernel Module Alteration</summary>


Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. The prerequisites are to enable monitoring of the finit_module, init_module, delete_module syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
<details>
<summary>Leviathan Registry Key Activity</summary>


Detects registry key used by Leviathan APT in Malaysian focused campaign.

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Linux Suspicious Auto-start Desktop Shortcut Execution</summary>


This detection rule identifies a suspicious process start from an graphical env process which may indicate the use of a malicious .desktop shortcut.

- **Effort:** intermediate

</details>
    
<details>
<summary>Malware Persistence Registry Key</summary>


Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.

- **Effort:** master

- **Changelog:**

    - 30/09/2025 - minor - Update selection to improve detection
    - 28/08/2025 - minor - Filter some FPs on key values
    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs

</details>
            
<details>
<summary>Microsoft Office Macro Security Registry Modifications</summary>


Detects registry changes allowing an attacker to make Microsoft Office products runs Macros without warning. Events are collected either from ETW/Sysmon/EDR depending of the integration.

- **Effort:** master

</details>
    
<details>
<summary>Narrator Feedback-Hub Persistence</summary>


The Windows 10 Narrator's Feedback-Hub registry key has been modified which could be done by an attacker for persistence purposes. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13). Careful since the SwiftOnSecurity Sysmon's configuration needs to be changed to log for this specifically.

- **Effort:** master

</details>
    
<details>
<summary>NjRat Registry Changes</summary>


Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.

- **Effort:** master

- **Changelog:**

    - 29/11/2023 - minor - Update regex pattern to insensitive case
    - 07/06/2024 - major - Update pattern to reduce false positives

</details>
            
<details>
<summary>Njrat Registry Values</summary>


Detects specifis registry values that are related to njRat usage.

- **Effort:** intermediate

</details>
    
<details>
<summary>Powershell Suspicious Startup Shortcut Persistence</summary>


Detects Powershell writing Startup shortcuts for persistence.

- **Effort:** master

</details>
    
<details>
<summary>Powershell Winlogon Helper DLL</summary>


Detects modifications to the Winlogon Registry keys, which may cause Winlogon to load and execute malicious DLLs and/or executables.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 13/03/2025 - major - Adding new filter and similarity strategy to reduce false positives. Changing effort level.

</details>
            
<details>
<summary>RUN Registry Key Created From Suspicious Folder</summary>


Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).

- **Effort:** advanced

</details>
    
<details>
<summary>Registry Key Used By Some Old Agent Tesla Samples</summary>


Detects potential use of the RUN registry key to execute some Agent Tesla samples at boot. Prerequisites are to log for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

</details>
    
<details>
<summary>Security Support Provider (SSP) Added to LSA Configuration</summary>


Detects the addition of a SSP to the registry. This is commonly used for persistence. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows. Logging for Registry events is needed for this rule to work (this can be done through Sysmon EventIDs 12 and 13).

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Sigma Intelligence Nanocore Persistence Key</summary>


Nanocore artefacts detection

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious desktop.ini Action</summary>


Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.

- **Effort:** advanced

- **Changelog:**

    - 06/01/2026 - minor - Adding some filters
    - 30/04/2024 - minor - Adding some filters

</details>
            
<details>
<summary>Svchost Modification</summary>


Detects the modification of svchost in the registry.

- **Effort:** advanced

</details>
    
**Modify Authentication Process**

<details>
<summary>1Password EPM MFA Disable</summary>


Detects when the MFA for 1Password is disabled.

- **Effort:** master

</details>
    
<details>
<summary>Active Directory Shadow Credentials</summary>


Detects alternative credentials material adding. Attackers can abuse msDS-KeyCredentialLink and create a key pair to obtain a persistent and stealthy access to the target user or computer.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace MFA changed</summary>


Detects when the settings for the MFA are modified.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Password Change</summary>


Detects when a password is changed. An attacker can perform this action to impact the availability of the account.

- **Effort:** master

- **Changelog:**

    - 20/06/2024 - minor - Adding new element to increase detection.

</details>
            
<details>
<summary>KeePass Config XML In Command-Line</summary>


Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) MFA Method Change</summary>


This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.

- **Effort:** master

</details>
    
## Privilege Execution
**Boot or Logon Initialization Scripts**

<details>
<summary>Logon Scripts (UserInitMprLogonScript)</summary>


Detects creation or execution of UserInitMprLogonScript persistence method. The rule requires to log for process command lines and registry creations or update, which can be done using Sysmon Event IDs 1, 12, 13 and 14.

- **Effort:** advanced

</details>
    
<details>
<summary>Startup Item Created</summary>


Detects when a item is added to the startup directory. An attacker can use this establish persistence.

- **Effort:** intermediate

</details>
    
**Scheduled Task/Job**

<details>
<summary>BazarLoader Persistence Using Schtasks</summary>


Detects possible BazarLoader persistence using schtasks. BazarLoader will create a Scheduled Task using a specific command line to establish its persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>Blue Mockingbird Malware</summary>


Attempts to detect system changes made by Blue Mockingbird

- **Effort:** elementary

</details>
    
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Creation or Modification of a GPO Scheduled Task</summary>


Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cron Files Alteration</summary>


Cron Files and Cron Directory alteration used by attacker for persistency or privilege escalation. To ensure full performance on this rule, `auditbeat` intake must be configure with the module `file_integrity` containing path mentionned in the pattern.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace App Script Scheduled Task</summary>


Detects when a scheduled task is launched by Google App Script. This product is used to create scripts and integrate applications within Google Workspace.

- **Effort:** advanced

</details>
    
<details>
<summary>Qakbot Persistence Using Schtasks</summary>


Detects possible Qakbot persistence using schtasks.

- **Effort:** intermediate

</details>
    
<details>
<summary>Remote Task Creation Via ATSVC Named Pipe</summary>


Detects remote task creation via at.exe or API interacting with ATSVC Named Pipe. This requires Windows Security event logging with the File Share policy.

- **Effort:** intermediate

- **Changelog:**

    - 21/03/2024 - minor - change filter to ACL hex value

</details>
            
<details>
<summary>STRRAT Scheduled Task</summary>


Detect STRRAT when it achieves persistence by creating a scheduled task. STRRAT is a Java-based stealer and remote backdoor, it establishes persistence using this specific command line: 'cmd /c schtasks /create /sc minute /mo 30 /tn Skype /tr "C:\Users\Admin\AppData\Roaming\SAMPLENAME.jar"'

- **Effort:** intermediate

</details>
    
<details>
<summary>Scheduled Task Creation By Non Privileged User</summary>


Detects scheduled task creation, either executed by a non-system user or a user who is not administrator (the user ID is not S-1-5-18 or S-1-5-18-*). This detection rule doesn't match Sysmon EventID 1 because the user SID is always set to S-1-5-18. 

- **Effort:** master

- **Changelog:**

    - 03/12/2025 - minor - Change rule effort level and update of rule name

</details>
            
<details>
<summary>Schtasks Persistence With High Privileges</summary>


Detection of scheduled task with high privileges used by attacker for persistence.

- **Effort:** elementary

</details>
    
<details>
<summary>Schtasks Suspicious Parent</summary>


Detects schtasks started from suspicious and/or unusual processes.

- **Effort:** intermediate

</details>
    
<details>
<summary>Spyware Persistence Using Schtasks</summary>


Detects possible Agent Tesla or Formbook persistence using schtasks. The name of the scheduled task used by these malware is very specific (Updates/randomstring).

- **Effort:** intermediate

</details>
    
<details>
<summary>Windows Suspicious Scheduled Task Creation</summary>


The rule identify creation of new scheduled task who run suspicious commands.

- **Effort:** master

- **Changelog:**

    - 24/04/2025 - minor - Adding similarity strategy.
    - 03/12/2025 - major - Change rule effort level according to sigthings

</details>
            
**Process Injection**

<details>
<summary>Address Space Layout Randomization (ASLR) Alteration</summary>


ASLR is a security feature used by the Operating System to mitigate memory exploit, attacker might want to disable it

- **Effort:** intermediate

- **Changelog:**

    - 14/03/2025 - minor - Excluded some commonly observed false positives.

</details>
            
<details>
<summary>Cobalt Strike Named Pipes</summary>


Detects the pipes established by Cobalt Strike to allow a communication between its beacons.

- **Effort:** master

</details>
    
<details>
<summary>CreateRemoteThread Common Process Injection</summary>


Detects a possible process injection through CreateRemoteThread() which is spotted by EventID 8 from Sysmon and several EDRs. This rule has a list of process commonly being injected by the attackers that should be updated regularly.

- **Effort:** advanced

</details>
    
<details>
<summary>Daspren Parad Malicious Behavior</summary>


Detects when Daspren Parad kills a process with a malicious behavior.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Dynwrapx Module Loading</summary>


Detects the loading of DynamicWrapperX (Dynwrapx). It is used by some malware in their infection chain and could help to detect its usage from vbs/wscript/cscript scripts. This is based on Microsoft Windows Sysmon events (Event ID 7).

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Malicious Named Pipe</summary>


Detects the creation of a named pipe used by known malware. Prerequisites are logging for PipeEvents in Sysmon config (Event ID 17 and 18).

- **Effort:** intermediate

</details>
    
<details>
<summary>MavInject Process Injection</summary>


Detects process injection using the signed Windows tool Mavinject32.exe (which is a LOLBAS)

- **Effort:** intermediate

</details>
    
<details>
<summary>Mshta Command From A Scheduled Task</summary>


Detects when an attacker leverage the Microsoft Windows Scheduled task feature to run the mshta.exe process. This is a common usage of a living-off-the-land binary, frequently abused for malicous purposes and not common nowadays in IT administration.

- **Effort:** intermediate

</details>
    
<details>
<summary>Process Herpaderping</summary>


Detection of process herpaderping using Sysmon Event ID 25. It detects that an image has been locked for access. Several processes have been excluded to avoid FPs.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Process Hollowing Detection</summary>


Detection of process hollowing using Sysmon Event ID 25. It detects that an image has been replaced in a process memory.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Searchindexer Wrong Parent</summary>


Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Searchprotocolhost Wrong Parent</summary>


Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 12/03/2024 - minor - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Smss Wrong Parent</summary>


Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 05/04/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Spoolsv Wrong Parent</summary>


Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.

</details>
            
<details>
<summary>Suspicious Process Requiring DLL Starts Without DLL</summary>


Detects potential process injection and hollowing on processes that usually require a DLL to be launched, but are launched without any argument. 

- **Effort:** intermediate

- **Changelog:**

    - 22/01/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Svchost Wrong Parent</summary>


Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - minor - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 31/01/2024 - minor - Adding filters to reduce false positives
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.

</details>
            
<details>
<summary>Taskhost Wrong Parent</summary>


Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Taskhostw Wrong Parent</summary>


Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>Wsmprovhost Wrong Parent</summary>


Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 25/10/2023 - minor - Adding filter to reduce false positives.
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
**Exploitation for Privilege Escalation**

<details>
<summary>Audit CVE Event</summary>


Detects events generated by Windows to indicate the exploitation of a known vulnerability.

- **Effort:** elementary

- **Changelog:**

    - 15/07/2024 - major - review filter and improve similarity

</details>
            
<details>
<summary>CVE-2021-4034 Polkit's pkexec</summary>


Detection of Polkit's pkexec exploit

- **Effort:** intermediate

</details>
    
<details>
<summary>Certify Or Certipy</summary>


Detects the use of certify and certipy which are two different tools used to enumerate and abuse Active Directory Certificate Services.

- **Effort:** advanced

</details>
    
<details>
<summary>Exploiting SetupComplete.cmd CVE-2019-1378</summary>


Detects exploitation attempts of privilege escalation vulnerability via SetupComplete.cmd and PartnerSetupComplete.cmd described in CVE-2019-1378.

- **Effort:** intermediate

- **Changelog:**

    - 09/10/2025 - minor - Added filter for a new field to reduce false positvives.

</details>
            
<details>
<summary>Okta Admin Privilege Granted</summary>


Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious New Printer Ports In Registry</summary>


Detects a suspicious printer port creation in Registry that could be an attempt to exploit CVE-2020-1048. The CVE-2020-1048 consists in gaining persistence, privilege by abusing a flaw in the Print Spooler service to execute a payload whose path is stored in the registry key. To fully use this rule, prerequesites are logging for Registry events in the Sysmon configuration (events 12, 13 and 14).

- **Effort:** master

</details>
    
**Valid Accounts**

<details>
<summary>Account Added To A Security Enabled Group</summary>


Detection in order to investigate who has added a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4728)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - add similarity strategy

</details>
            
<details>
<summary>Account Removed From A Security Enabled Group</summary>


Detection in order to investigate who has removed a specific Domain User in Domain Admins or Group Policy Creator Owners (Security event 4729)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 12/07/2024 - minor - Add similarity strategy

</details>
            
<details>
<summary>Account Tampering - Suspicious Failed Logon Reasons</summary>


This method uses uncommon error codes on failed logons to determine suspicious activity and tampering with accounts that have been disabled or somehow restricted. Depending on the network environment some failed logons Status can be added to the list.

- **Effort:** advanced

- **Changelog:**

    - 01/08/2023 - minor - Similarity strategy for the rule has changed and is now based on the user.target.name field.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Admin User RDP Remote Logon</summary>


Detects remote login through Remote Desktop Protocol (RDP) by Administrator user depending on internal pattern. Check before activation the identifiable administrators usernames (pattern or special unique character ("Admin*") to adapt and add some filtering.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Authentication Impossible Travel</summary>


Detects impossible travel when performing authentication from a source IP address, grouped by user name. This could require some alert filtering for some user generic accounts, and known IP address range. Microsoft / Office 365 format is not covered by this rule.

- **Effort:** master

- **Changelog:**

    - 27/07/2024 - major - review filter to avoid false positives
    - 30/08/2024 - minor - improve filter to avoid false positives
    - 30/01/2025 - major - Pattern rework with ECS fields only and simple authentication success use case
    - 04/02/2025 - major - Excluding Microsoft 365 format to avoid false positives
    - 14/08/2025 - major - Excluding Wiz Audit Logs format to avoid false positives
    - 29/10/2026 - major - Excluding Entra ID following parser changes to avoid false positives. A dedicated rule for Entra ID exists and is called "Microsoft Entra ID (Azure AD) Impossible Travel".

</details>
            
<details>
<summary>Broadcom Edge Secure Web Gateway High Threat</summary>


Detects when a high threat is detected by Broadcom Edge Secure Web Gateway.

- **Effort:** master

</details>
    
<details>
<summary>Brute-Force On Fortinet Firewall Login</summary>


Spots many failed attempts to log on an administration interface.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and add intake field format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Denied Access To Remote Desktop</summary>


Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.

- **Effort:** intermediate

- **Changelog:**

    - 19/10/2023 - minor - Minor change in selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Dscl Authonly</summary>


Detects the use of the command dscl with authonly used to verify the password of a user and for authentification. An attacker can abuse this command to gain credentials.

- **Effort:** advanced

</details>
    
<details>
<summary>Enable Root Account With Dsenableroot</summary>


Detects when root is enabled. Attackers can use this as a mean of persistence since root is disabled by default.

- **Effort:** elementary

</details>
    
<details>
<summary>Failed Logon Followed By A Success From Public IP Addresses</summary>


A login from a public IP can indicate a misconfigured firewall or network boundary. The detection look for 5 or more failed attemps followed by a successfull one. The sekoia.tags are used to filter internal Ipv4 addresses.

- **Effort:** master

- **Changelog:**

    - 29/05/2024 - major - Adding new field and switching to correlation rule.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Flare Events Critical Severity Threat Exposure</summary>


Detects a high critical Flare exposure event from clear, deep, or dark web monitoring. This indicates a critical-risk threat indicator that requires rapid triage.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events High Severity Threat Exposure</summary>


Detects a high severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Informational Severity Threat Exposure</summary>


Detects a informational severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Leaked Credential With Password Exposure</summary>


Detects leaked credential events where a password is explicitly present in the exposure record, indicating elevated risk of account takeover.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Low Severity Threat Exposure</summary>


Detects a low severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Medium Severity Threat Exposure</summary>


Detects a medium severity Flare exposure event from clear, deep, or dark web monitoring.

- **Effort:** master

</details>
    
<details>
<summary>Fortigate Firewall Successful External Login</summary>


Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Google Cloud Audit Logs Account Suspended</summary>


Detects when Google Cloud Audit Logs notify a user account suspended for a suspicious activity

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Added</summary>


Detects when an application is added to Google Workspace Domain. This should be an expected change made by an administrator and need to be checked.

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Application Authorized</summary>


Detects when an application is authorized to access a Google user account. An exception is currently made for GMAIL because of the large number of hits.

- **Effort:** master

</details>
    
<details>
<summary>Google Cloud Audit Logs Attack Warning</summary>


Detects when Google Cloud Audit Logs notify an attack warning such as the famous "Government-backed attack".

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Workspace Account Warning</summary>


Detects a suspicious login, leaked password, or account disabled following suspicious activity.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace Admin Creation</summary>


Detects when an admin is created or when his role is changed.

- **Effort:** master

- **Changelog:**

    - 22/05/2024 - minor - Adding new element to increase detection.

</details>
            
<details>
<summary>Google Workspace Suspicious Login</summary>


Detects a suspicious login reported by google.

- **Effort:** master

</details>
    
<details>
<summary>Login Brute-Force On Fortinet Firewall From Internet</summary>


Detects successful access to administration console of a firewall after several failure from Internet.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only and intake format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Login Brute-Force On FreeRadius</summary>


A user has attempted to login several times (brute-force) with error then one success.

- **Effort:** intermediate

</details>
    
<details>
<summary>Login Brute-Force On Sekoia.io</summary>


Detects successful access to Sekoia.io after several failure.

- **Effort:** intermediate

- **Changelog:**

    - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.

</details>
            
<details>
<summary>Microsoft 365 Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.). Note: if you collect Entra ID SignInLogs, the rule "Microsoft Entra ID (Azure AD) Device Code Authentication" is a better equivalent to this rule.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Device Code Authentication</summary>


Authentication via a device code is designed for use with input constrained devices. This method can however be abused, particularly in social engineering attacks. Whitelisting based on the organisation's practices is likely required to make this rule useful (e.g. excluding the public IP ranges of the organisation, excluding authentications attempt from managed devices, etc.)

- **Effort:** master

</details>
    
<details>
<summary>Netskope Admin Audit High Severity</summary>


Audit events detection for admin activites that differ from authentications, with high severity level according to Netskope.

- **Effort:** master

- **Changelog:**

    - 29/01/2025 - minor - Rework pattern for high severity events only and filter out authentication events.
    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Detected</summary>


Netskope identified a malware with a high severity (excluding Patient Zero here)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Malware Patient Zero Detected</summary>


Netskope identified a malware as Patient Zero.

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netskope Potential Brute Force On Protected Applications</summary>


Detects potential brute force on Netskope protected applications with more than 10 failures in 5 minutes for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute Force On Protected Applications</summary>


Detects successful brute force on Netskope protected applications after more than 5 failures in 5 minutes and one success for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute-Force On Management Console</summary>


Detects successful access to Netskope management console after more than 10 failures in 5 minutes for the same user name.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Web Isolation On Suspicious Domain</summary>


Netskope identified a suspicious domain and triggered web sandboxing (RBI)

- **Effort:** master

- **Changelog:**

    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Okta Access To Admin Console Denied</summary>


Detects when an attempt was made to access the Okta Admin Console from an interactive user account but failed.

- **Effort:** master

</details>
    
<details>
<summary>Okta Many Passwords Reset Attempt</summary>


This rule identifies a high number of Okta user password reset or account unlock attempts. An adversary may attempt to obtain unauthorized access to Okta user accounts using these methods and attempt to blend in with normal activity in their target's environment and evade detection.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Suspicious Activity Reported</summary>


Detects when a user reports suspicious activity for their Okta account. These events should be investigated, as they can help security teams identify when an adversary is attempting to gain access to their network.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Unauthorized Access to App</summary>


An user tries to access an unauthorized application.

- **Effort:** master

</details>
    
<details>
<summary>User Added To Admin Group Via Cmd</summary>


Detects the use of different commands to add a user to an admin group.

- **Effort:** advanced

</details>
    
<details>
<summary>User Added to Local Administrators</summary>


Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 04/04/2024 - major - Rule's pattern field changed
    - 01/06/2026 - major - selection improvements to better align with the detection objective

</details>
            
**Account Manipulation**

<details>
<summary>AWS CloudTrail IAM Failed User Creation</summary>


Detects an attemp to create a user account where the result is an explicit denied.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail IAM Password Policy Updated</summary>


Detects an update to the password policy. This could be an attempt to lower accounts security level.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail IAM Policy Changed</summary>


Detects change on AWS IAM Policy

- **Effort:** master

</details>
    
<details>
<summary>AWS CloudTrail Root ConsoleLogin</summary>


Detects a login with a root account on AWS portal. It is a best practice to avoid root account usage for daily tasks and to create an IAM admin user.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail Route 53 Domain Transfer Attempt</summary>


Detects when a request in success or failure is made to transfer a domain name to an other AWS account

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail Route 53 Domain Transfer Lock Disabled</summary>


Detects when the transfer lock feature is disabled on a domain name handled by AWS Route 53 service.

- **Effort:** elementary

</details>
    
<details>
<summary>Active Directory Delegate To KRBTGT Service</summary>


Detects potential persistence installation from an already compromised administrator domain account. The attacker will create a TGT and abuse a service account with the constrained delegation and update it with the krbtgt service. The detection relies on the Event ID 4738.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory Replication User Backdoor</summary>


Backdooring domain object to grant the rights associated with DCSync to regular user or machine account, this technics is often used to give ResetPassword or WriteMembers or DCSync permission(s) for persistency on a domain.

- **Effort:** intermediate

- **Changelog:**

    - 15/10/2024 - major - Update pattern to avoid false positives and change rule effort
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory User Backdoors</summary>


Detects scenarios where the attacker controls another user or computer account without having to use their credentials.

- **Effort:** intermediate

- **Changelog:**

    - 06/04/2023 - minor - Removed a selection as it triggered too many false positives, and the detection was not part of the main goal of this rule.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Add User to Privileged Group</summary>


Add user in a potential privileged group which can be used to elevate privileges on the system.

- **Effort:** advanced

</details>
    
<details>
<summary>Enabling Restricted Admin Mode</summary>


Detects when the restricted admin mode is enabled.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace Admin Modification</summary>


Detects when an admin is modified.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Domain Delegation</summary>


Detects when a domain delegation is granted.

- **Effort:** master

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Self Service Password Reset In Failure</summary>


Detects self-service password reset in failure for various reasons (except licence or policy ones)

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and specific intake field

</details>
            
<details>
<summary>Mimikatz Basic Commands</summary>


Detects Mimikatz most popular commands. 

- **Effort:** elementary

- **Changelog:**

    - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.

</details>
            
<details>
<summary>Okta Admin Privilege Granted</summary>


Administrator privilege granted to an user or account. This can be privilege escalation, persistance over system or account takedown.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Application deleted</summary>


An application has been delete on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Application modified</summary>


An application has been updated on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta User Account Deactivated</summary>


A user account has been deactivated in Okta.

- **Effort:** master

</details>
    
<details>
<summary>Okta User Impersonation Access</summary>


A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.

- **Effort:** advanced

</details>
    
<details>
<summary>Password Change On Directory Service Restore Mode (DSRM) Account</summary>


The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers. Attackers may change the password to gain persistence.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Privileged AD Builtin Group Modified</summary>


Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).

- **Effort:** master

- **Changelog:**

    - 10/07/2023 - minor - Added AD groups and change to effort master.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>SSH Authorized Key Alteration</summary>


The file authorized_keys is used by SSH server to identify SSH keys that are authorized to connect to the host, alteration of one of those files might indicate a user compromision.

- **Effort:** advanced

</details>
    
<details>
<summary>SeEnableDelegationPrivilege Granted To User Or Machine In Active Directory</summary>


Detects the SeEnableDelegationPrivilege right in Active Directory granted to a user of a computer, it would allow control of other AD user objects

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 04/03/2026 - minor - Fix small typo in rule name.

</details>
            
<details>
<summary>User Added to Local Administrators</summary>


Detects when user accounts are added which could be legitimate activity or a sign of privilege escalation activity, Potential False-Positives Legitimate administrative activity WinRM clients

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 04/04/2024 - major - Rule's pattern field changed
    - 01/06/2026 - major - selection improvements to better align with the detection objective

</details>
            
<details>
<summary>Varonis Many Accounts Disabled</summary>


This rule identifies a high number of account disabled.

- **Effort:** master

</details>
    
**Web Shell**

<details>
<summary>Antivirus Web Shell Detection</summary>


Detects a highly relevant Antivirus alert that reports a web shell. This is based on Windows Defender logs (Event ID 1116 and 1117).

- **Effort:** elementary

</details>
    
**Access Token Manipulation**

<details>
<summary>Correlation Priv Esc Via Remote Thread</summary>


Detect a process that obtains system privilege via a remote thread

- **Effort:** intermediate

</details>
    
<details>
<summary>Jumpcloud Api Key Updated</summary>


An API Token has been updated on Jumplcoud portal.

- **Effort:** advanced

</details>
    
<details>
<summary>Meterpreter or Cobalt Strike Getsystem Service Installation</summary>


Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting some of the techniques being used (technique 1,2 and 5).

- **Effort:** elementary

</details>
    
<details>
<summary>Okta API Token created</summary>


A new API Token has been created on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta API Token revoked</summary>


A new API Token has been deleted on Okta SSO.

- **Effort:** advanced

</details>
    
<details>
<summary>Possible RottenPotato Attack</summary>


Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Shell PID Injection</summary>


Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.

- **Effort:** intermediate

</details>
    
**Domain or Tenant Policy Modification**

<details>
<summary>Creation or Modification of a GPO Scheduled Task</summary>


Detects lateral movement using GPO scheduled task, often used to deploy ransomware at scale. This rule is based on the EventID 5145 which is specific to Windows Servers. The advanced audit policy setting Object Access > Audit Detailed File Share must be configured for Success/Failure.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Domain Trust Created Or Removed</summary>


A trust was created or removed to a domain. An attacker could perform that in order to do lateral movement easily between domains or shutdown the ability of two domains to communicate.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>ESET Protect Set Policy</summary>


Detects when a new policy is set or removed.

- **Effort:** master

</details>
    
<details>
<summary>GPO Executable Delivery</summary>


Detects MSI binaries run through GPOs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Jumpcloud Policy Modified</summary>


Detects when a Jumpcloud policy is modified.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) Domain Trust Modification</summary>


Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Confirm the added or modified target domain/URL is legitimate administrator behavior.

- **Effort:** elementary

- **Changelog:**

    - 14/03/2025 - minor - Rule's pattern update following o365 parser change

</details>
            
<details>
<summary>Okta Policy Modified or Deleted</summary>


Detects when an Okta policy is modified or deleted.

- **Effort:** advanced

</details>
    
<details>
<summary>Okta Policy Rule Modified or Deleted</summary>


Detects when an Okta Policy Rule is Modified or Deleted.

- **Effort:** advanced

</details>
    
<details>
<summary>Privileged AD Builtin Group Modified</summary>


Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).

- **Effort:** master

- **Changelog:**

    - 10/07/2023 - minor - Added AD groups and change to effort master.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Tenable Identity Exposure / Alsid Critical Severity Alert</summary>


Tenable Identity Exposure / Alsid raised a critical severity alert.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Removing event fields to use the smart description
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Tenable Identity Exposure / Alsid High Severity Alert</summary>


Tenable Identity Exposure / Alsid raised an alert.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Removing event fields to use the smart description
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
**Create or Modify System Process**

<details>
<summary>APT29 Fake Google Update Service Install</summary>


This method detects malicious services mentioned in APT29 report by FireEye. The legitimate path for the Google update service is C:\Program Files (x86)\Google\Update\GoogleUpdate.exe so the service names and executable locations used by APT29 are specific enough to be detected in log files.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cobalt Strike Default Service Creation Usage</summary>


Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Csrss Child Found</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This process  should not create a child process or it is very rare.

- **Effort:** advanced

- **Changelog:**

    - 23/12/2025 - minor - Rule was moved to advanced effort level considering the number of alerts and addtional filters were added.
    - 16/12/2024 - minor - Improve pattern mandatory fields and add filter to reduce false positives

</details>
            
<details>
<summary>Csrss Wrong Parent</summary>


The csrss.exe process (csrss stands for Client / Server Runtime Subsystem) is a generic Windows process used to manage windows and Windows graphics. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Dllhost Wrong Parent</summary>


Dllhost.exe is a process belonging to Microsoft Windows Operating System. The dllhost.exe file manages DLL based applications. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Some filters on parent process names were also added to reduce false positives.

</details>
            
<details>
<summary>Gpscript Suspicious Parent</summary>


Gpscript defines GPO scripts for users and applies them to login / logout sessions. This rule checks if the parent of this process is the supposed one (svchost) or not.

- **Effort:** intermediate

- **Changelog:**

    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Logonui Wrong Parent</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It doesn't only make it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 07/06/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Lsass Wrong Parent</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This rule checks if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - The rule has been reworked for a specific intake to allow our customers to activate the rule for this intake which was not the case before.

</details>
            
<details>
<summary>Malicious Service Installations</summary>


Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Mshta Command From A Scheduled Task</summary>


Detects when an attacker leverage the Microsoft Windows Scheduled task feature to run the mshta.exe process. This is a common usage of a living-off-the-land binary, frequently abused for malicous purposes and not common nowadays in IT administration.

- **Effort:** intermediate

</details>
    
<details>
<summary>New Service Creation</summary>


Detects creation of a new service from command line

- **Effort:** advanced

</details>
    
<details>
<summary>OneNote Suspicious Children Process</summary>


In January 2023, a peak of attacks using .one files was observed in the wild. This rule tries to detect the effect of such attempts using this technique.

- **Effort:** advanced

- **Changelog:**

    - 15/04/2024 - minor - Changing effort level and adding new filters to reduce false positives.

</details>
            
<details>
<summary>Rare Logonui Child Found</summary>


Logonui.exe is a file associated with the Logon user interface. The login user interface is an essential part of the Windows operating system. It not only makes it easy for the user to log in to the PC but also determines whether the user has logged in and logged out correctly and makes it easy to switch between users. This process could create a child process but it is very rare and could be a signal of some process injection.

- **Effort:** advanced

- **Changelog:**

    - 17/01/2025 - minor - Adding filter to reduce false positives.

</details>
            
<details>
<summary>Rare Lsass Child Found</summary>


Lsass ensures the identification of users (domain users or local users). Domain users are identified based on information in the Active Directory. Local users are identified based on information from the Security Account Manager (SAM) local database. This process should not create a child process or it is very rare.

- **Effort:** intermediate

</details>
    
<details>
<summary>Searchindexer Wrong Parent</summary>


Detects if the Search Indexer was executed by a non-legitimate parent process. Search Indexer is the Windows service that handles indexing of your files for Windows Search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Searchprotocolhost Child Found</summary>


SearchProtocolHost.exe is part of the Windows Indexing Service, an application that indexes files from the local drive making them easier to search. This is a crucial part of the Windows operating system. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 17/03/2025 - major - Rule changed to effort master, and filter added to reduce false positives.

</details>
            
<details>
<summary>Searchprotocolhost Wrong Parent</summary>


Detects if the Search Protocol Host process was executed by a non-legitimate parent process. Search Protocol Host is part of the Windows Indexing Service, a service indexing files on the local drive making them easier to search.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 12/03/2024 - minor - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>Smss Wrong Parent</summary>


Detects if the Smss process was executed by a non-legitimate parent process. Session Manager Subsystem (smss) process is a component of the Microsoft Windows NT family of operating systems.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 05/04/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake

</details>
            
<details>
<summary>SolarWinds Wrong Child Process</summary>


Detects SolarWinds process starting an unusual child process. Process solarwinds.businesslayerhost.exe and solarwinds.businesslayerhostx64.exe created an unexepected child process which doesn't correspond to the legitimate ones.

- **Effort:** intermediate

- **Changelog:**

    - 14/06/2023 - major - Reworking of the rule after many FPs and a more suitable Elastic rule
    - 22/12/2023 - minor - Adding a child process name to the filter list to avoid some FPs

</details>
            
<details>
<summary>Spoolsv Wrong Parent</summary>


Detects if the Spoolsv process was executed by a non-legitimate parent process. Printer Spooler Service (Spoolsv) process is responsible for managing spooled print/fax jobs.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Added some new filters as well to reduce false positives.

</details>
            
<details>
<summary>StoneDrill Service Install</summary>


This method detects a service install of the malicious Microsoft Network Realtime Inspection Service service described in StoneDrill report by Kaspersky 

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Commands From MS SQL Server Shell</summary>


Detection of some shell commmands run from a cmd executed by Microsoft MS SQL Server. It could be a sign of xp_cmdshell allowed on the MS-SQL server.

- **Effort:** intermediate

</details>
    
<details>
<summary>Svchost Wrong Parent</summary>


Detects if the svchost.exe process was executed by a non-legitimate parent process. Svchost (Service Host Process) is a generic host process name for services that run from dynamic-link libraries (DLLs).

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - minor - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 31/01/2024 - minor - Adding filters to reduce false positives
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter has also been added to reduce false positives.

</details>
            
<details>
<summary>Taskhost Wrong Parent</summary>


Detects if the Taskhost process was executed by a non-legitimate parent process. Taskhost is the process of the Windows Task Manager which lists the processes that are currently running on the computer system.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
<details>
<summary>Taskhost or Taskhostw Suspicious Child Found</summary>


Task Host manages pop-up windows when users try to close them in a Windows environment. Taskhost.exe triggers the host process for the task. Task Host is a Windows process designed to alert users when dialog boxes close. It is usually launched when restarting and shutting down a PC, and checks if all programs have been properly closed. This process should not create a child process or it is very rare.

- **Effort:** master

- **Changelog:**

    - 13/08/2024 - minor - Adding elements to filter to reduce false positives and changing effort level.
    - 13/02/2025 - minor - Adding new filters to reduce false positives.

</details>
            
<details>
<summary>Taskhostw Wrong Parent</summary>


Detects if the Taskhostw process was executed by a non-legitimate parent process. Taskhostw is a software component of Windows service start manager, it starts DLL-based Windows services when the computer boots up.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>WMI Persistence Command Line Event Consumer</summary>


Detects WMI command line event consumers.

- **Effort:** elementary

</details>
    
<details>
<summary>Wininit Wrong Parent</summary>


Windows Boot is a background application launcher for the Windows operating system. Wininit.exe is responsible for performing the Windows initialization process. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. A filter was also added to reduce false positives.

</details>
            
<details>
<summary>Winlogon wrong parent</summary>


Winlogon.exe is a process that performs the Windows login management function, handling user login and logout in Windows. You see this process in action whenever the operating system asks you for your username and password. It is also responsible for loading user profiles after login, this supports automated login (when relevant) and keyboard and mouse inactivity monitoring to decide when to invoke the screen saver. This rule analyse if the parent of this process is a legitimate one or not.

- **Effort:** master

- **Changelog:**

    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filter was also added to reduce false positives.
    - 27/10/2026 - major - Added filter to reduce false positives

</details>
            
<details>
<summary>Winrshost Wrong Parent</summary>


Detects if the Winrshosts process was executed by a non-legitimate parent process The winrshost.exe is a Host Process for WinRM's Remote Shell plugin.

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake. Filters were also added to reduce false positives.

</details>
            
<details>
<summary>Wsmprovhost Wrong Parent</summary>


Detects if the Wsmprovhost process was executed by a non-legitimate parent process. The PowerShell host wsmprovhost.exe is a proxy process executed remotely through PowerShell when using Windows Remote Management (WinRM).

- **Effort:** master

- **Changelog:**

    - 20/11/2023 - minor - Rule's effort level has been changed to advanced as it was too dependent on the environment.
    - 04/07/2023 - major - Added filter to reduce false positives
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation
    - 25/10/2023 - minor - Adding filter to reduce false positives.
    - 19/03/2024 - major - Added filter to reduce false positives
    - 17/10/2024 - major - Removed a filter on a specific intake, the rule now works fine for every intake.

</details>
            
**Event Triggered Execution**

<details>
<summary>COM Hijack Via Sdclt</summary>


Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.

- **Effort:** intermediate

</details>
    
<details>
<summary>Change Default File Association</summary>


When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

- **Effort:** advanced

</details>
    
<details>
<summary>Component Object Model Hijacking</summary>


Detects component object model hijacking. An attacker can establish persistence with COM objects.

- **Effort:** advanced

</details>
    
<details>
<summary>Control Panel Items</summary>


Detects the malicious use of a control panel item

- **Effort:** advanced

</details>
    
<details>
<summary>HTML Smuggling Suspicious Usage</summary>


Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.

- **Effort:** advanced

- **Changelog:**

    - 08/04/2025 - minor - Change effort level and add filter to reduce false positives.

</details>
            
<details>
<summary>New DLL Added To AppCertDlls Registry Key</summary>


Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Logging for Registry events is needed in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting</summary>


Detects the modification of Outlook setting "LoadMacroProviderOnBoot" which if enabled allows the automatic loading of any configured VBA project/module. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

</details>
    
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Registry Persistence Using 'Image File Execution' And 'SilentProcessExit' Keys</summary>


Detects persistence registry keys. Logging for Registry events is needed, it can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

</details>
    
<details>
<summary>Sticky Key Like Backdoor Usage</summary>


Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Suspicious Netsh DLL Persistence</summary>


Detects persitence via netsh helper. Netsh interacts with other operating system components using dynamic-link library (DLL) files. Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Scripting In A WMI Consumer</summary>


Detects suspicious scripting in WMI Event Consumers. The rule requires to log WMI Consumers, which can be done through Sysmon's Event IDs 20 and 21.

- **Effort:** intermediate

</details>
    
<details>
<summary>WMI Event Subscription</summary>


Detects creation of WMI event subscription persistence method 

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>WMI Persistence Script Event Consumer File Write</summary>


Detects file writes through WMI script event consumer.

- **Effort:** advanced

</details>
    
**Boot or Logon Autostart Execution**

<details>
<summary>Autorun Keys Modification</summary>


Detects modification of autostart extensibility point (ASEP) in registry. Prerequisites are Logging for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** master

- **Changelog:**

    - 16/01/2025 - minor - Added filters to reduce false positives.

</details>
            
<details>
<summary>DLL Load via LSASS Registry Key</summary>


Detects a method to load DLL via LSASS process using an undocumented Registry key. Prerequisites are logging for Registry events. This can be done with Sysmon events 12, 13 and 14 and monitor `SYSTEM\CurrentControlSet\Services`.

- **Effort:** intermediate

</details>
    
<details>
<summary>Kernel Module Alteration</summary>


Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. The prerequisites are to enable monitoring of the finit_module, init_module, delete_module syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
<details>
<summary>Leviathan Registry Key Activity</summary>


Detects registry key used by Leviathan APT in Malaysian focused campaign.

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Linux Suspicious Auto-start Desktop Shortcut Execution</summary>


This detection rule identifies a suspicious process start from an graphical env process which may indicate the use of a malicious .desktop shortcut.

- **Effort:** intermediate

</details>
    
<details>
<summary>Malware Persistence Registry Key</summary>


Detects registry key used by several malware, especially Formbook spyware in two ways, either the Sysmon registry events, or the commands line.

- **Effort:** master

- **Changelog:**

    - 30/09/2025 - minor - Update selection to improve detection
    - 28/08/2025 - minor - Filter some FPs on key values
    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance, and filter some FPs

</details>
            
<details>
<summary>Microsoft Office Macro Security Registry Modifications</summary>


Detects registry changes allowing an attacker to make Microsoft Office products runs Macros without warning. Events are collected either from ETW/Sysmon/EDR depending of the integration.

- **Effort:** master

</details>
    
<details>
<summary>Narrator Feedback-Hub Persistence</summary>


The Windows 10 Narrator's Feedback-Hub registry key has been modified which could be done by an attacker for persistence purposes. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13). Careful since the SwiftOnSecurity Sysmon's configuration needs to be changed to log for this specifically.

- **Effort:** master

</details>
    
<details>
<summary>NjRat Registry Changes</summary>


Detects changes for the RUN registry key which happen when a victim is infected by NjRAT. Please note that even if NjRat is well-known for the behavior the rule catches, the rule is a bit larger and could catch other malwares.

- **Effort:** master

- **Changelog:**

    - 29/11/2023 - minor - Update regex pattern to insensitive case
    - 07/06/2024 - major - Update pattern to reduce false positives

</details>
            
<details>
<summary>Njrat Registry Values</summary>


Detects specifis registry values that are related to njRat usage.

- **Effort:** intermediate

</details>
    
<details>
<summary>Powershell Suspicious Startup Shortcut Persistence</summary>


Detects Powershell writing Startup shortcuts for persistence.

- **Effort:** master

</details>
    
<details>
<summary>Powershell Winlogon Helper DLL</summary>


Detects modifications to the Winlogon Registry keys, which may cause Winlogon to load and execute malicious DLLs and/or executables.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 13/03/2025 - major - Adding new filter and similarity strategy to reduce false positives. Changing effort level.

</details>
            
<details>
<summary>RUN Registry Key Created From Suspicious Folder</summary>


Detects the suspicious RUN keys created by software located in Download or temporary Outlook/Internet Explorer directories. Prerequisites are logging for Registry events, which can be done with Sysmon (events 12 and 13).

- **Effort:** advanced

</details>
    
<details>
<summary>Registry Key Used By Some Old Agent Tesla Samples</summary>


Detects potential use of the RUN registry key to execute some Agent Tesla samples at boot. Prerequisites are to log for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

</details>
    
<details>
<summary>Security Support Provider (SSP) Added to LSA Configuration</summary>


Detects the addition of a SSP to the registry. This is commonly used for persistence. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows. Logging for Registry events is needed for this rule to work (this can be done through Sysmon EventIDs 12 and 13).

- **Effort:** elementary

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>Sigma Intelligence Nanocore Persistence Key</summary>


Nanocore artefacts detection

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious desktop.ini Action</summary>


Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.

- **Effort:** advanced

- **Changelog:**

    - 06/01/2026 - minor - Adding some filters
    - 30/04/2024 - minor - Adding some filters

</details>
            
<details>
<summary>Svchost Modification</summary>


Detects the modification of svchost in the registry.

- **Effort:** advanced

</details>
    
**Abuse Elevation Control Mechanism**

<details>
<summary>CMSTP UAC Bypass via COM Object Access</summary>


Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects

- **Effort:** intermediate

- **Changelog:**

    - 28/05/2024 - minor - Add pattern to selection to improve coverage
    - 13/03/2025 - minor - Adding filters to reduce false positives and adding similarity.

</details>
            
<details>
<summary>COM Hijack Via Sdclt</summary>


Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute', to bypass UAC using 'sdclt.exe'.

- **Effort:** intermediate

</details>
    
<details>
<summary>Citrix NetScaler (ADC) Actions Blocked</summary>


This rule aims to detect a large amount of actions blocked performed from the same source.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace Bypass 2FA</summary>


Detects when user tries to bypass the 2FA.

- **Effort:** master

</details>
    
<details>
<summary>HTML Smuggling Suspicious Usage</summary>


Based on several samples from different botnets, this rule aims at detecting HTML infection chain by looking for HTML created files followed by suspicious files being executed.

- **Effort:** advanced

- **Changelog:**

    - 08/04/2025 - minor - Change effort level and add filter to reduce false positives.

</details>
            
<details>
<summary>Linux Capabilities Discovery</summary>


Linux capabilities are special attributes in the Linux kernel that grant processes and binary executables specific privileges that are normally reserved for processes whose effective user ID is 0 (The root user, and only the root user, has UID 0). This rule aims to detect discovery of such capabilities on the Linux system. The prerequisites are to enable monitoring of the execve and getxattr syscalls using Auditbeat.

- **Effort:** intermediate

</details>
    
<details>
<summary>Okta User Impersonation Access</summary>


A user has initiated a session impersonation granting them access to the environment with the permissions of the user they are impersonating. This would likely indicate Okta administrative access and should only ever occur if requested and expected.

- **Effort:** advanced

</details>
    
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Setuid Or Setgid Usage</summary>


Detects the usage of a setuid or a setgid. The prerequisites are to enable monitoring of the setuid and setgid syscalls using Auditbeat.

- **Effort:** intermediate

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Shell PID Injection</summary>


Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>UAC Bypass Using Fodhelper</summary>


Detects UAC bypass method using Fodhelper after setting the proper registry key, used in particular by Agent Tesla (RAT) or more recently by Earth Luscas. Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** intermediate

- **Changelog:**

    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance

</details>
            
<details>
<summary>UAC Bypass Via Sdclt</summary>


Detects changes to HKCU\Software\Classes\exefile\shell\runas\command\isolatedCommand by an attacker in order to bypass User Account Control (UAC)

- **Effort:** elementary

</details>
    
<details>
<summary>UAC Bypass via Event Viewer</summary>


Detects UAC bypass method using Windows event viewer. 

- **Effort:** intermediate

- **Changelog:**

    - 21/11/2023 - minor - Improve filter to reduce false positives and clarified the rule pattern.
    - 21/09/2023 - minor - Improve filter to reduce false positives

</details>
            
<details>
<summary>Unusual Process Executed in Temporary Directory</summary>


Identifies processes running in a temporary folder. This is sometimes done by adversaries to hide malware. The prerequisites are to enable monitoring of the execve syscall using Auditbeat.

- **Effort:** master

- **Changelog:**

    - 09/10/2025 - minor - Added filter to reduce false positvives.

</details>
            
**Escape to Host**

<details>
<summary>Docker Escape Bind Mount</summary>


Catch Docker escape via mount escape followed by chroot 

- **Effort:** intermediate

</details>
    
## Defense Evasion
## Credential Access
**OS Credential Dumping**

<details>
<summary>Active Directory Database Dump Via Ntdsutil</summary>


Detects the dump of ntdis.dit database by using the utility ntdsutil.exe. NTDS.dit database stores Active Directory data, including passwords hashes for all users in the domain.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory Replication from Non Machine Account</summary>


Detects potential abuse of Active Directory Replication Service (ADRS) from a non machine account to request credentials. It requires a configuration step where the legit service account should be added to the exclusion list.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 03/09/2026 - major - Effort level and severity changed.

</details>
            
<details>
<summary>Cmdkey Cached Credentials Recon</summary>


Detects usage of cmdkey to look for cached credentials.

- **Effort:** intermediate

</details>
    
<details>
<summary>Copying Browser Files With Credentials</summary>


Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.

- **Effort:** elementary

</details>
    
<details>
<summary>Copying Sensitive Files With Credential Data</summary>


Detects copy of files with well-known filenames (sensitive files with credential data) using esentutl. This requires Windows Security event log with the Detailed File Share logging policy enabled.

- **Effort:** elementary

</details>
    
<details>
<summary>Credential Dump Tools Related Files</summary>


Detects processes or file names related to credential dumping tools and the dropped files they generate by default.

- **Effort:** advanced

- **Changelog:**

    - 07/08/2024 - major - Effort level was changed. Rule pattern initial field was changed to be ECS compliant and match on more intakes. A process was excluded and a filter was added, both to avoid generating too much false positives.

</details>
            
<details>
<summary>Credential Dumping By LaZagne</summary>


Detects LSASS process access by LaZagne for credential dumping. 

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Credential Dumping Tools Service Execution</summary>


Detects well-known credential dumping tools execution via service execution

- **Effort:** intermediate

</details>
    
<details>
<summary>Credential Dumping-Tools Common Named Pipes</summary>


Detects well-known credential dumping tools execution via specific named pipes. Prerequisites: Logging for PipeEvents is needed in Sysmon config

- **Effort:** master

</details>
    
<details>
<summary>DCSync Attack</summary>


Detects DCSync attack, it is highly likely that the post-exploitation tool Mimikatz was executed.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 05/09/2024 - minor - Changing name of elements.
    - 03/09/2026 - major - Effort level and severity changed.

</details>
            
<details>
<summary>DPAPI Domain Backup Key Extraction</summary>


Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Dumpert LSASS Process Dumper</summary>


Detects the use of Dumpert process dumper, which dumps the lsass.exe process memory

- **Effort:** elementary

</details>
    
<details>
<summary>Grabbing Sensitive Hives Via Reg Utility</summary>


Detects dump of SAM, System or Security hives using reg.exe utility. Adversaries may attempt to dump these Windows Registry to retrieve password hashes and access credentials.

- **Effort:** master

- **Changelog:**

    - 20/03/2025 - major - Effort level changed, similarity strategy added, and filters improved to reduce false positives.
    - 02/01/2024 - minor - Rule was improved to have broader detection and filters were added.

</details>
            
<details>
<summary>HackTools Suspicious Names</summary>


Quick-win rule to detect the default process names or file names of several HackTools.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2025 - major - Change effort level and added filters.
    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.

</details>
            
<details>
<summary>HackTools Suspicious Process Names In Command Line</summary>


Detects the default process name of several HackTools and also check in command line. This rule is here for quickwins as it obviously has many blind spots.

- **Effort:** intermediate

- **Changelog:**

    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    - 10/06/2024 - minor - Added filter to the rule to reduce false positives.
    - 19/06/2023 - minor - Added filter to the rule to reduce false positives.

</details>
            
<details>
<summary>Impacket Secretsdump.py Tool</summary>


Detects credential dumping via secretdump of impacket suite.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>LSASS Access From Non System Account</summary>


Detects LSASS Access from Non System Account (e.g. Mimikatz)

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>LSASS Memory Dump</summary>


Detects process accessing LSASS memory which is typical for credentials dumping tools. The rule requires Sysmon EventID 10 to work as it is based on the GrantedAccess mask.

- **Effort:** master

- **Changelog:**

    - 06/04/2023 - minor - Rule effort has been upgraded to master considering the number of different false positives the rule can trigger.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>LSASS Memory Dump File Creation</summary>


LSASS memory dump creation using operating systems utilities. Procdump will use process name in output file if no name is specified.

- **Effort:** intermediate

</details>
    
<details>
<summary>Load Of dbghelp/dbgcore DLL From Suspicious Process</summary>


Detects the load of dbghelp/dbgcore DLL (used to make memory dumps) by suspicious processes. Many tools import dbghelp.dll and / or dbgcore.dll to use the MiniDumpWriteDump function. As an example, SilentTrynity C2 Framework has a module that leverages this API to dump the contents of Lsass.exe and transfer it over the network back to the attacker's machine. Dumpert from OUTFLANK also uses this.

- **Effort:** advanced

</details>
    
<details>
<summary>Lsass Access Through WinRM</summary>


Detects the access of LSASS.exe process through Windows Remote Management (WinRM) protocol. This is often done using Invoke-Mimikatz -ComputerName command, which uses PSRemoting and therefore WinRM. However, this is not limited to the Mimikatz threat and can be done by other tools as well. This rule needs Process Access monitoring, which can be done using Sysmon's event ID 10.

- **Effort:** intermediate

</details>
    
<details>
<summary>Main Memory Dumping</summary>


Attacker might want to leverage their permission on the system or steal authentication tokens to third parties software, website, etc. To do so, attacker might try to dump main memory of computer. The prerequisites are to enable monitoring of the openat and open syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
<details>
<summary>Malicious Service Installations</summary>


Generic and known malicious service installation that appear in cases of lateral movement, credential dumping and other suspicious activity. It detects the use of PAExec, Wannacry commonly used malicious service, APT29 known malicious service name and net user service file name which is known as a sign of persistence.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Mimikatz Basic Commands</summary>


Detects Mimikatz most popular commands. 

- **Effort:** elementary

- **Changelog:**

    - 06/04/2023 - minor - Added a filter to the rule as many false positives were observed.

</details>
            
<details>
<summary>Mimikatz LSASS Memory Access</summary>


Detection of in-memory Mimikatz by focusing on processes opening the Local Security Authority (Lsass.exe) process and reading the memory contents of it. This probably means that Mimikatz has been executed on the host, meaning the attacker already has high privileges and is looking to dump credentials, most likely for lateral movement or privilege escalation purposes. The rule requires Sysmon EventID 10 to work as it is based on the GrantedAccess mask.

- **Effort:** advanced

- **Changelog:**

    - 06/04/2023 - minor - Whitelisted another SourceImage as it triggered too many false positives.
    - 21/06/2023 - minor - Whitelisted lsm.exe that triggered too many false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 23/09/2025 - minor - Adding filters to avoid false positives.

</details>
            
<details>
<summary>NTDS.dit File In Suspicious Directory</summary>


The file NTDS.dit is supposed to be located mainly in C:\Windows\NTDS. The rule checks whether the file is in a legitimate directory or not (through file creation events). This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.

- **Effort:** advanced

</details>
    
<details>
<summary>NTDS.dit File Interaction Through Command Line</summary>


Detects interaction with the file NTDS.dit through command line. This is usually really suspicious and could indicate an attacker trying copy the file to then look for users password hashes.

- **Effort:** intermediate

- **Changelog:**

    - 08/11/2023 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>NetNTLM Downgrade Attack</summary>


Detects changes in Windows Registry key (LMCompatibilityLevel, NTLMMinClientSec or RestrictSendingNTLMTraffic) which can lead to NetNTLM downgrade attack. The rule requires to log registry keys creation or update, it can be done using Sysmon's Event ID 12,13 and 14.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Password Dumper Activity On LSASS</summary>


Detects process handle on LSASS process with certain access mask and object type SAM_DOMAIN

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Process Memory Dump Using Comsvcs</summary>


Detects the use of comsvcs in command line to dump a specific process memory. This technique is used by attackers for privilege escalation and pivot.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Filter improved to reduce false positives. On the other hand, some selections were added to improve detection.
    - 10/04/2024 - minor - Rule description was changed due to some mistakes
    - 13/06/2024 - minor - Adding similarity strategy and changing effort level.

</details>
            
<details>
<summary>Process Memory Dump Using Createdump</summary>


Detects the use of createdump.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.

- **Effort:** elementary

</details>
    
<details>
<summary>Process Memory Dump Using Rdrleakdiag</summary>


Detects the use of rdrleakdiag.exe in command line to dump the memory of a process. This technique is used by attackers for privilege escalation and pivot.

- **Effort:** elementary

</details>
    
<details>
<summary>Process Memory Dumping From proc Filesystem</summary>


Attacker might want to leverage their permission on the system or steal authentication to third parties software, website, etc.. To do so, attacker might try to dump memory of interesting process, for instance ftp-server or web server to dig for authentication login and password. The prerequisites are to enable monitoring of the openat and open syscalls using Auditbeat.

- **Effort:** master

</details>
    
<details>
<summary>Process Trace Alteration</summary>


PTrace syscall provides a means by which one process ("tracer") may observe and control the execution of another process ("tracee") and examine and change the tracee's memory and registers. Attacker might want to abuse ptrace functionnality to analyse memory process. It requires to be admin or set ptrace_scope to 0 to allow all user to trace any process.

- **Effort:** advanced

</details>
    
<details>
<summary>RedMimicry Winnti Playbook Dropped File</summary>


Detects actions caused by the RedMimicry Winnti playbook

- **Effort:** elementary

</details>
    
<details>
<summary>Rubeus Tool Command-line</summary>


Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.

- **Effort:** advanced

</details>
    
<details>
<summary>SAM Registry Hive Handle Request</summary>


Detects handles requested to SAM registry hive

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious CommandLine Lsassy Pattern</summary>


Detects the characteristic lsassy loop used to identify lsass PIDs

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious SAM Dump</summary>


Detects suspicious SAM dump to AppData repository, as cause by QuarksPwDump and other password dumpers. Logging for Microsoft-Windows-Kernel-General Event ID 16 or Sysmon Event ID 11 is needed.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Transferring Files With Credential Data Via Network Shares</summary>


Detects file transfer of sensitive files which contain credential data using network shares.

- **Effort:** intermediate

- **Changelog:**

    - 17/10/2023 - minor - Improve selection to reduce false positives
    - 04/03/2023 - minor - Fixed small typos.

</details>
            
<details>
<summary>Unsigned Image Loaded Into LSASS Process</summary>


Loading unsigned image (DLL, EXE) into LSASS process. To activate this rule you need to monitor loaded images into the LSASS process, this can be done with SYSMON Event ID 7.

- **Effort:** advanced

</details>
    
<details>
<summary>WCE wceaux.dll Creation</summary>


Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.

- **Effort:** intermediate

</details>
    
<details>
<summary>Wdigest Enable UseLogonCredential</summary>


Detects modification of the Windows Registry value of HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential. This technique is used to extract passwords in clear-text using WDigest. The rule requires to log for Registry Events, which can be done using Sysmon Event IDs 12, 13 and 14.

- **Effort:** elementary

- **Changelog:**

    - 08/08/2024 - major - Rule's pattern field changed and pattern improved to cause less false positives.

</details>
            
<details>
<summary>Windows Credential Editor Registry Key</summary>


Detects the use of Windows Credential Editor (WCE). Prerequisites are logging for Registry events in the Sysmon configuration (events 12 and 13).

- **Effort:** elementary

</details>
    
<details>
<summary>Write To File In Sudoers.d Folder</summary>


A user tried to write something to a file in /etc/sudoers.d. It can be used to elevate privilege related to sudo and make it persistent. The prerequisites are to enable monitoring of the openat syscall using Auditbeat.

- **Effort:** advanced

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>Write To File In Systemd</summary>


A user tried to write something to a file in /etc/systemd/system. This repository contains services that are run at start. It can be used to run a malicious programm at start with high privileges. The prerequisites are to enable monitoring of the execve openat using Auditbeat.

- **Effort:** advanced

- **Changelog:**

    - 26/10/2023 - minor - Added filter to reduce false positives.
    - 04/01/2023 - minor - Added filter to reduce false positives.
    - 20/01/2025 - minor - Update pattern to ECS field only and filter some false positives.
    - 24/03/2025 - major - Added filter to reduce false positives, change effort and add similarity strategy.

</details>
            
**Network Sniffing**

<details>
<summary>Capture a network trace with netsh.exe</summary>


Detects capture a network trace via netsh.exe trace functionality

- **Effort:** advanced

- **Changelog:**

    - 24/04/2025 - minor - Adding similarity strategy and filters to reduce false positives and changing effort level.

</details>
            
<details>
<summary>Network Sniffing</summary>


List of common tools used for network packages sniffing

- **Effort:** advanced

</details>
    
<details>
<summary>Network Sniffing Windows</summary>


Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

- **Effort:** intermediate

</details>
    
<details>
<summary>WiFi Credentials Harvesting Using Netsh</summary>


Detects the harvesting of WiFi credentials using netsh.exe.

- **Effort:** advanced

- **Changelog:**

    - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.

</details>
            
**Input Capture**

<details>
<summary>AppleScript Password Prompt</summary>


Detects when a prompt is displayed to gain credentials. This technique is used by MacOS malware to obtain the user's password.

- **Effort:** advanced

</details>
    
**Brute Force**

<details>
<summary>1Password EPM Brute Force</summary>


Detects multiple failed login followed by a success from the same user.

- **Effort:** master

</details>
    
<details>
<summary>Anomaly Bruteforce - User Enumeration</summary>


The rule detects abnormally high number of TGT failed or NTLM authent failed associate to error code username don't exist who could indicate user enumeration

- **Effort:** advanced

- **Changelog:**

    - 09/04/2024 - major - change field on aggregation
    - 13/06/2024 - minor - Adding fields to be displayed in alerts.
    - 12/07/2024 - major - improce coverage, enforce filter and change effort

</details>
            
<details>
<summary>Anomaly Bruteforce Disabled Users</summary>


The rule detects abnormally high number of TGT failed or NTLM authent failed associate to error code account disabled who could indicate a brute force attack

- **Effort:** advanced

</details>
    
<details>
<summary>Authentication Impossible Travel</summary>


Detects impossible travel when performing authentication from a source IP address, grouped by user name. This could require some alert filtering for some user generic accounts, and known IP address range. Microsoft / Office 365 format is not covered by this rule.

- **Effort:** master

- **Changelog:**

    - 27/07/2024 - major - review filter to avoid false positives
    - 30/08/2024 - minor - improve filter to avoid false positives
    - 30/01/2025 - major - Pattern rework with ECS fields only and simple authentication success use case
    - 04/02/2025 - major - Excluding Microsoft 365 format to avoid false positives
    - 14/08/2025 - major - Excluding Wiz Audit Logs format to avoid false positives
    - 29/10/2026 - major - Excluding Entra ID following parser changes to avoid false positives. A dedicated rule for Entra ID exists and is called "Microsoft Entra ID (Azure AD) Impossible Travel".

</details>
            
<details>
<summary>Brute Force WALLIX Bastion</summary>


Detects a successful login after many failed attempts by the same user.

- **Effort:** master

</details>
    
<details>
<summary>Brute-Force On Fortinet Firewall Login</summary>


Spots many failed attempts to log on an administration interface.

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field and add intake field format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Correlation Internal Kerberos Password Spraying</summary>


Detect multiple Kerberos authentication failed on several account from one source

- **Effort:** master

</details>
    
<details>
<summary>Correlation Internal Ntlm Password Spraying</summary>


Detect multiple NTLM authentication failed on several account from one source

- **Effort:** master

</details>
    
<details>
<summary>Entra ID Password Compromised By Known Credential Testing Tool</summary>


Detects a sign-in that has a correlation ID known to be used by malicious credential testing scripts. Note that even if the sign-in was blocked by MFA (error 50074) or device authentication (error 50097), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.

- **Effort:** elementary

- **Changelog:**

    - 05/03/2024 - minor - Rule name error was fixed
    - 09/04/2024 - minor - Error code 500532 added
    - 16/04/2024 - minor - Add more correlation IDs and error code 50052
    - 03/01/2025 - minor - Add more correlation IDs
    - 09/04/2025 - minor - Add more correlation IDs, change similarity strategy to user.id to workaround email capitalisation inconsistencies.

</details>
            
<details>
<summary>Entra ID Password Compromised Via Seamless SSO Credential Testing</summary>


Detects a sign-in using the Entra ID Seamless SSO `usernamemixed` endpoint. This endpoint is rarely used legitimately, and often abused by credential testing tools. Note that even if the sign-in was blocked by MFA (error 50074) or device authentication (error 50097), these verifications only occur after the correct password was submitted. The account's password must still be considered compromised, and be changed.

- **Effort:** elementary

</details>
    
<details>
<summary>Fortigate Firewall Login In Failure</summary>


Detects failed login attemps on firewall administration rule. Prerequisites, check that the firewall logs format corresponds to the rule

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Fortigate Firewall Successful External Login</summary>


Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule

- **Effort:** master

- **Changelog:**

    - 20/01/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>FreeRADIUS Failed Authentication</summary>


A failed authentication was logged by FreeRADIUS 

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace Login Brute-Force</summary>


Detects when a user failed to login multiple times before a successful login.

- **Effort:** master

</details>
    
<details>
<summary>Login Brute-Force On Fortinet Firewall From Internet</summary>


Detects successful access to administration console of a firewall after several failure from Internet.

- **Effort:** advanced

- **Changelog:**

    - 03/02/2025 - minor - Update pattern to ECS field only and intake format
    - 15/10/2025 - minor - Update pattern to match intake format change

</details>
            
<details>
<summary>Login Brute-Force On FreeRadius</summary>


A user has attempted to login several times (brute-force) with error then one success.

- **Effort:** intermediate

</details>
    
<details>
<summary>Login Brute-Force On Sekoia.io</summary>


Detects successful access to Sekoia.io after several failure.

- **Effort:** intermediate

- **Changelog:**

    - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.

</details>
            
<details>
<summary>Login Brute-Force Successful Linux</summary>


A user has attempted to login several times (brute-force) and succeeded to login on the linux monitored endpoint.

- **Effort:** advanced

- **Changelog:**

    - 06/10/2023 - minor - renaming and tunn filters to limit False Positive
    - 03/02/2025 - minor - Update pattern to ECS field only

</details>
            
<details>
<summary>MokN High Threat Bait Attempt</summary>


Detects when MokN raises a high threat bait login attempt.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Potential Brute Force On Protected Applications</summary>


Detects potential brute force on Netskope protected applications with more than 10 failures in 5 minutes for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute Force On Protected Applications</summary>


Detects successful brute force on Netskope protected applications after more than 5 failures in 5 minutes and one success for the same user name and application.

- **Effort:** master

</details>
    
<details>
<summary>Netskope Successful Brute-Force On Management Console</summary>


Detects successful access to Netskope management console after more than 10 failures in 5 minutes for the same user name.

- **Effort:** master

</details>
    
<details>
<summary>Password Change Brute-Force On AzureAD</summary>


A change of password has failed on Azure Active Directory, 5 times for the same user

- **Effort:** intermediate

</details>
    
<details>
<summary>Password Reset Error Brute-Force On AzureAD</summary>


A reset of password has failed on Azure Active Directory, 5 times within the same entity.

- **Effort:** intermediate

- **Changelog:**

    - 22/05/2024 - minor - Switch the group-by clause to a sekoiaio uuid field.

</details>
            
<details>
<summary>RSA SecurID Failed Authentification</summary>


Detects many failed attempts to authenticate followed by a successfull login for a super admin account.

- **Effort:** advanced

- **Changelog:**

    - 14/01/2025 - minor - Adding format field to improve rules mapping
    - 08/08/2024 - minor - Group-by values were changed to avoid having too much alerts.

</details>
            
<details>
<summary>Successful Brute Force Login From Internet</summary>


Detects a spike of failed login followed by a success one from Internet for a given source and target

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Systancia Cleanroom Brute Force</summary>


Detects a successful brute force attempt to access systancia cleanroom web portal.

- **Effort:** master

</details>
    
**Multi-Factor Authentication Interception**

<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (CEPHAS 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit CEPHAS 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Gabagool)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Gabagool. The `filter_password_spraying` exclusion corresponds to a password spraying tool which is already detected by the rule `Entra ID Password Compromised By Known Credential Testing Tool`.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Greatness)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Greatness.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (HoneySecurity / HoneyStorm)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit HoneySecurity / HoneyStorm.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.

- **Effort:** elementary

- **Changelog:**

    - 09/08/2024 - major - Update the indicator.
    - 25/09/2024 - major - Rename the rule, update the indicators.
    - 23/12/2024 - major - Update the indicators.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Rockstar 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Rockstar 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Sneaky 2FA)</summary>


Detects a sign-in attempt with an impossible device shift characteristic of the adversary-in-the-middle phishing kit Sneaky 2FA.

- **Effort:** elementary

- **Changelog:**

    - 25/02/2025 - major - Update the indicator.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.

- **Effort:** elementary

- **Changelog:**

    - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
    - 31/12/2025 - major - Change the similarity strategy to user.id instead of user.email.

</details>
            
<details>
<summary>EvilProxy Phishing Domain</summary>


Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 Sign-in With No User Agent</summary>


Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.

- **Effort:** elementary

- **Changelog:**

    - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
    - 10/04/2025 - minor - Exclude more error codes to reduce false positives
    - 01/06/2026 - minor - Adding filter on user_type code to reduce false positives

</details>
            
<details>
<summary>Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses</summary>


Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.

- **Effort:** intermediate

- **Changelog:**

    - 01/06/2026 - minor - Adding more filter and review group-by clause to reduce false positives

</details>
            
<details>
<summary>Okta MFA Bypass Attempt</summary>


A bypass of MFA may have been attempted.

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential Azure AD Phishing Page (Adversary-in-the-Middle)</summary>


Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.

- **Effort:** intermediate

- **Changelog:**

    - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
    - 13/08/2025 - minor - Exclude additional legitimate domains and common benign positives.

</details>
            
<details>
<summary>Sign-In Via Known AiTM Phishing Kit</summary>


Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.

- **Effort:** elementary

- **Changelog:**

    - 12/12/2024 - minor - Update the selections to use a more appropriate ECS field. The rule now matches on more intakes. The name of the rule has been modified as well.

</details>
            
**Forced Authentication**

<details>
<summary>Correlation Suspicious Authentication Coercer Behavior</summary>


Detect a possible NTLM Relay attack combine with authent coerce

- **Effort:** intermediate

</details>
    
**Exploitation for Credential Access**

<details>
<summary>Abusing Azure Browser SSO</summary>


Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 

- **Effort:** master

</details>
    
<details>
<summary>Audit CVE Event</summary>


Detects events generated by Windows to indicate the exploitation of a known vulnerability.

- **Effort:** elementary

- **Changelog:**

    - 15/07/2024 - major - review filter and improve similarity

</details>
            
**Steal Application Access Token**

<details>
<summary>Abusing Azure Browser SSO</summary>


Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 

- **Effort:** master

</details>
    
**Steal Web Session Cookie**

<details>
<summary>Copying Browser Files With Credentials</summary>


Detects copy of sensitive data (passwords, cookies, credit cards) included in web browsers files.

- **Effort:** elementary

</details>
    
**Unsecured Credentials**

<details>
<summary>Adexplorer Usage</summary>


Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.

- **Effort:** advanced

- **Changelog:**

    - 27/03/2023 - minor - Modify pattern to avoid false positive and detect usage of either / or - character for snapshot parameter

</details>
            
<details>
<summary>Container Credential Access</summary>


Adversaries could abuse containers tools to obtain credential like Kubernetes secret or Kubernetes service account access token

- **Effort:** intermediate

</details>
    
<details>
<summary>Credentials Extraction</summary>


This rule aims to detect the use of a specific command to access some credentials without using mimikatz or another tool.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Cloud Audit Logs 2FA Disabled</summary>


Detects when Google Cloud Audit Logs notify the 2FA deactivation for a user account.

- **Effort:** intermediate

</details>
    
<details>
<summary>Linux Suspicious Search</summary>


Adversaries may search for private key on compromised systems

- **Effort:** intermediate

</details>
    
<details>
<summary>Opening Of a Password File</summary>


Command line detection of common office software opening some password related file. It could be a security breach if an unauthorized user access it.

- **Effort:** master

- **Changelog:**

    - 07/10/2024 - minor - Modified similarity strategy.
    - 21/03/2024 - minor - Adding similarity strategy to reduce alerts creation.
    - 22/01/2024 - minor - Removing a file extension to allow broader detection.
    - 16/11/2023 - minor - Changing effort level and adding filter to reduce false positives.
    - 03/07/2023 - minor - Added french words for the command lines.
    - 22/08/2023 - major - adding similarity strategy in order to avoid multiple alerts creation

</details>
            
<details>
<summary>Outlook Registry Access</summary>


Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.

- **Effort:** master

- **Changelog:**

    - 02/04/2024 - major - Updating the pattern and adding filter selection
    - 19/02/2024 - minor - Effort level was adapted according to the observed hits for the rule

</details>
            
<details>
<summary>Remote Registry Management Using Reg Utility</summary>


Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>XCopy Suspicious Usage</summary>


Detects the usage of xcopy with suspicious command line options (used by Judgment Panda APT in the past). The rule is based on command line only in case xcopy is renamed.

- **Effort:** advanced

</details>
    
**Credentials from Password Stores**

<details>
<summary>1Password EPM Grant Access Vault</summary>


Detects when a group is granted access to a 1Password vault.

- **Effort:** master

</details>
    
<details>
<summary>Anomaly Secret Store Access</summary>


The rule detects abnormally high access to secrets store folder

- **Effort:** master

- **Changelog:**

    - 08/04/2024 - minor - change field name on query
    - 12/06/2024 - minor - Adding new fields to be displayed in alerts.

</details>
            
<details>
<summary>Credential Harvesting Via Vaultcmd.exe</summary>


Detects when the process vaultcmd is used for credential harvesting.

- **Effort:** advanced

</details>
    
<details>
<summary>Credentials Extraction</summary>


This rule aims to detect the use of a specific command to access some credentials without using mimikatz or another tool.

- **Effort:** advanced

</details>
    
<details>
<summary>Flare Events Stealer Log Malware Infection</summary>


Detects a Flare stealer log event with an identified malware family, indicating credentials or host data were likely collected by infostealer malware.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Suspicious Forum Post</summary>


Detects a Flare forum post event, indicating credentials or host data were likely collected by infostealer malware.

- **Effort:** master

</details>
    
<details>
<summary>Generic Password Discovery</summary>


Detects when the security utility is used to access passwords in a keychain.

- **Effort:** advanced

</details>
    
<details>
<summary>Information Stealer Downloading Legitimate Third-Party DLLs</summary>


Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.

- **Effort:** intermediate

</details>
    
<details>
<summary>PasswordDump SecurityXploded Tool</summary>


Detects the execution of the PasswordDump SecurityXploded Tool

- **Effort:** elementary

</details>
    
**Modify Authentication Process**

<details>
<summary>1Password EPM MFA Disable</summary>


Detects when the MFA for 1Password is disabled.

- **Effort:** master

</details>
    
<details>
<summary>Active Directory Shadow Credentials</summary>


Detects alternative credentials material adding. Attackers can abuse msDS-KeyCredentialLink and create a key pair to obtain a persistent and stealthy access to the target user or computer.

- **Effort:** elementary

</details>
    
<details>
<summary>Google Workspace MFA changed</summary>


Detects when the settings for the MFA are modified.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace Password Change</summary>


Detects when a password is changed. An attacker can perform this action to impact the availability of the account.

- **Effort:** master

- **Changelog:**

    - 20/06/2024 - minor - Adding new element to increase detection.

</details>
            
<details>
<summary>KeePass Config XML In Command-Line</summary>


Detects a command-line interaction with the KeePass Config XML file. It could be used to retrieve informations or to be abused for persistence.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Entra ID (Azure AD) MFA Method Change</summary>


This rule detects when an user makes a change to the multifactor authentication methods for their account. In environments where this rule is too noisy, alert filters should be applied, e.g. to focus on privileged accounts, or unusual source network locations.

- **Effort:** master

</details>
    
**Adversary-in-the-Middle**

<details>
<summary>Correlation Suspicious Authentication Coercer Behavior</summary>


Detect a possible NTLM Relay attack combine with authent coerce

- **Effort:** intermediate

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (CEPHAS 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit CEPHAS 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Gabagool)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Gabagool. The `filter_password_spraying` exclusion corresponds to a password spraying tool which is already detected by the rule `Entra ID Password Compromised By Known Credential Testing Tool`.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Greatness)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Greatness.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (HoneySecurity / HoneyStorm)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit HoneySecurity / HoneyStorm.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.

- **Effort:** elementary

- **Changelog:**

    - 09/08/2024 - major - Update the indicator.
    - 25/09/2024 - major - Rename the rule, update the indicators.
    - 23/12/2024 - major - Update the indicators.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Rockstar 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Rockstar 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Sneaky 2FA)</summary>


Detects a sign-in attempt with an impossible device shift characteristic of the adversary-in-the-middle phishing kit Sneaky 2FA.

- **Effort:** elementary

- **Changelog:**

    - 25/02/2025 - major - Update the indicator.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.

- **Effort:** elementary

- **Changelog:**

    - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
    - 31/12/2025 - major - Change the similarity strategy to user.id instead of user.email.

</details>
            
<details>
<summary>EvilProxy Phishing Domain</summary>


Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 Sign-in With No User Agent</summary>


Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.

- **Effort:** elementary

- **Changelog:**

    - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
    - 10/04/2025 - minor - Exclude more error codes to reduce false positives
    - 01/06/2026 - minor - Adding filter on user_type code to reduce false positives

</details>
            
<details>
<summary>Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses</summary>


Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.

- **Effort:** intermediate

- **Changelog:**

    - 01/06/2026 - minor - Adding more filter and review group-by clause to reduce false positives

</details>
            
<details>
<summary>Possible RottenPotato Attack</summary>


Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Potential Azure AD Phishing Page (Adversary-in-the-Middle)</summary>


Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.

- **Effort:** intermediate

- **Changelog:**

    - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
    - 13/08/2025 - minor - Exclude additional legitimate domains and common benign positives.

</details>
            
<details>
<summary>Sign-In Via Known AiTM Phishing Kit</summary>


Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.

- **Effort:** elementary

- **Changelog:**

    - 12/12/2024 - minor - Update the selections to use a more appropriate ECS field. The rule now matches on more intakes. The name of the rule has been modified as well.

</details>
            
**Steal or Forge Kerberos Tickets**

<details>
<summary>Kerberos Pre-Auth Disabled in UAC</summary>


The rule identify a change performed on a domain user object that disables Kerberos Pre-Authentication

- **Effort:** elementary

</details>
    
<details>
<summary>Possible Replay Attack</summary>


This event can be a sign of Kerberos replay attack or, among other things, network device configuration or routing problems.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Rubeus Register New Logon Process</summary>


Detects potential use of Rubeus through registering a new logon process. This rule needs the EventID 4611, which can be configured through Group Policies (Audit Security System Extension)

- **Effort:** master

</details>
    
<details>
<summary>Rubeus Tool Command-line</summary>


Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious Kerberos Ticket</summary>


Detect suspicious Kerberos ticket based on on their parameters which suggest that it could be forged.

- **Effort:** intermediate

- **Changelog:**

    - 03/07/2024 - major - Add filter to cover a second case to improve rule coverage

</details>
            
<details>
<summary>Suspicious Outbound Kerberos Connection</summary>


Detects suspicious outbound network activity via kerberos default port indicating possible lateral movement or first stage PrivEsc via delegation.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed
    - 05/08/2024 - major - Rule reworked to match more intakes and have less false positives (filters were added).

</details>
            
<details>
<summary>Suspicious TGS requests (Kerberoasting)</summary>


The rule aims at detecting the Kerberoasting technique, when an attacker requests TGS in order to crack them offline. Toease its task, the attacker requests tickets with weak encryption (such as RC4_HMAC_MD5). The rule therefore detects when an user is requesting 5 TGS for different users in 5 minutes.

- **Effort:** advanced

</details>
    
<details>
<summary>User Couldn't Call A Privileged Service LsaRegisterLogonProcess</summary>


The LsaRegisterLogonProcess function verifies that the application making the function call is a logon process by checking that it has the SeTcbPrivilege privilege set. Possible Rubeus tries to get a handle to LSA. This rule requires to log the Event ID 4673, which can be done by updating the Audit Policy.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Steal or Forge Authentication Certificates**

<details>
<summary>Suspicious Certificate Request-adcs Abuse</summary>


Detects when a new certificate is requested or granted against Active Directory Certificate Services (AD CS) using a Subject Alternative Name (SAN)

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious Kerberos Ticket</summary>


Detect suspicious Kerberos ticket based on on their parameters which suggest that it could be forged.

- **Effort:** intermediate

- **Changelog:**

    - 03/07/2024 - major - Add filter to cover a second case to improve rule coverage

</details>
            
## Discovery
**System Service Discovery**

<details>
<summary>Anomaly Internal RDP</summary>


Detects uncompleted attempts to connect to a Remote Desktop Protocol (RDP) session.

- **Effort:** master

</details>
    
<details>
<summary>PowerView commandlets 1</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** advanced

- **Changelog:**

    - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.

</details>
            
<details>
<summary>PowerView commandlets 2</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** master

- **Changelog:**

    - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 07/04/2025 - minor - Changed similarity strategy and effort level.

</details>
            
<details>
<summary>SCM Database Handle Failure</summary>


Detects non-system users failing to get a handle of the SCM database.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>SCM Database Privileged Operation</summary>


Detects non-system users performing privileged operation on the SCM database

- **Effort:** master

</details>
    
**Query Registry**

<details>
<summary>Putty Sessions Listing</summary>


Detects attempts to list Putty sessions through registry. To fully work, this rule requires to log registry accesses, which can be done with the Windows Event ID 4656 or 4663 but for that specific configuration is needed.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Remote Registry Management Using Reg Utility</summary>


Remote registry management using REG utility from non-admin workstation. This requires Windows Security events logging.

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Taskkill Command</summary>


Detects rare taskkill command being used. It could be related to Baby Shark malware.

- **Effort:** intermediate

</details>
    
<details>
<summary>SysKey Registry Keys Access</summary>


Detects handle requests and access operations to specific registry keys to calculate the SysKey. The SysKey allows to decrypt Security Account Mannager (SAM) database entries (from registry or hive) and get NTLM, and sometimes LM hashes of local accounts passwords. Adversaries can calculate the Syskey by using RegOpenKeyEx/RegQueryInfoKey API calls to query the appropriate class info and values from the HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\JD, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Skew1, HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\GBG, and HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Data keys.

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**System Network Configuration Discovery**

<details>
<summary>Discovery Commands Correlation</summary>


Detects some frequent discovery commands used by some ransomware operators.

- **Effort:** intermediate

- **Changelog:**

    - 16/04/2024 - minor - Adding new elements to increase detection.

</details>
            
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Headless Web Browser Execution To Download File</summary>


Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.

- **Effort:** elementary

</details>
    
**Remote System Discovery**

<details>
<summary>Anomaly Internal Ping</summary>


Detects internal ping with uncomplete connection on internal network.

- **Effort:** master

</details>
    
<details>
<summary>Network Scanning and Discovery</summary>


Tools and command lines used for network discovery from current system

- **Effort:** advanced

</details>
    
<details>
<summary>Openfiles Usage</summary>


Detects when the command openfiles, to get information on files opened remotely, is used.

- **Effort:** advanced

</details>
    
<details>
<summary>PowerView commandlets 1</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** advanced

- **Changelog:**

    - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.

</details>
            
<details>
<summary>PowerView commandlets 2</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** master

- **Changelog:**

    - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 07/04/2025 - minor - Changed similarity strategy and effort level.

</details>
            
<details>
<summary>Shell PID Injection</summary>


Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.

- **Effort:** intermediate

</details>
    
**System Owner/User Discovery**

<details>
<summary>RDP Session Discovery</summary>


Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.

- **Effort:** advanced

</details>
    
**Network Sniffing**

<details>
<summary>Capture a network trace with netsh.exe</summary>


Detects capture a network trace via netsh.exe trace functionality

- **Effort:** advanced

- **Changelog:**

    - 24/04/2025 - minor - Adding similarity strategy and filters to reduce false positives and changing effort level.

</details>
            
<details>
<summary>Network Sniffing</summary>


List of common tools used for network packages sniffing

- **Effort:** advanced

</details>
    
<details>
<summary>Network Sniffing Windows</summary>


Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

- **Effort:** intermediate

</details>
    
<details>
<summary>WiFi Credentials Harvesting Using Netsh</summary>


Detects the harvesting of WiFi credentials using netsh.exe.

- **Effort:** advanced

- **Changelog:**

    - 21/11/2023 - minor - Rule's effort level has been changed to advanced as it was highly dependent on the environment.

</details>
            
**Network Service Discovery**

<details>
<summary>Advanced IP Scanner</summary>


Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.

- **Effort:** master

- **Changelog:**

    - 18/09/2025 - minor - Similarity strategy updated.
    - 01/06/2025 - minor - Added a condition for process executable.

</details>
            
<details>
<summary>Anomaly Internal Port Connection</summary>


Detects multiple scan of different ports on internal network.

- **Effort:** master

- **Changelog:**

    - 12/06/2024 - minor - Adding field to be displayed in the alerts and changing the query.
    - 04/07/2024 - minor - Reviewing query.

</details>
            
<details>
<summary>Anomaly Multiple Host Port Scan</summary>


Detects multiple port scan from/to a private address, excluding DNS.

- **Effort:** master

- **Changelog:**

    - 11/06/2024 - minor - Adding fields to be displayed in the alert and changing effort level.

</details>
            
**System Network Connections Discovery**

<details>
<summary>Broadcom Edge Secure Web Gateway Anomaly TCP Denied</summary>


Detects a high number of connection TCP denied.

- **Effort:** master

</details>
    
<details>
<summary>Cmd.exe Used To Run Reconnaissance Commands</summary>


Detects command lines with suspicious args

- **Effort:** advanced

</details>
    
<details>
<summary>Discovery Commands Correlation</summary>


Detects some frequent discovery commands used by some ransomware operators.

- **Effort:** intermediate

- **Changelog:**

    - 16/04/2024 - minor - Adding new elements to increase detection.

</details>
            
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
**Permission Groups Discovery**

<details>
<summary>Bloodhound and Sharphound Tools Usage</summary>


Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.

- **Effort:** intermediate

- **Changelog:**

    - 29/08/2025 - minor - Filtering some command line false positives.
    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    - 26/03/2024 - minor - Adapted the rule to remove false positives.

</details>
            
<details>
<summary>Domain Group And Permission Enumeration</summary>


Detects adversaries attempts to find domain-level groups and permission settings. Commands such as net group /domain of the Net utility can list domain-level groups The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators. Wizard Spider, FIN6, and other groups used net in their campaigns.

- **Effort:** advanced

</details>
    
<details>
<summary>Gpresult Usage</summary>


Detects when an account uses gpresult to get information on gpo.

- **Effort:** advanced

</details>
    
<details>
<summary>Permission Discovery Via Wmic</summary>


Detects discovery of permission on local groups via the tool wmic.

- **Effort:** advanced

</details>
    
**System Information Discovery**

<details>
<summary>Discovery Commands Correlation</summary>


Detects some frequent discovery commands used by some ransomware operators.

- **Effort:** intermediate

- **Changelog:**

    - 16/04/2024 - minor - Adding new elements to increase detection.

</details>
            
<details>
<summary>Listing Systemd Environment</summary>


Detects a listing of systemd environment variables. This command could be used to do reconnaissance on a compromised host.

- **Effort:** advanced

- **Changelog:**

    - 06/03/2024 - minor - Effort level was adapted according to the observed hits for the rule

</details>
            
<details>
<summary>Shadow Copies</summary>


Detects command line used to create and list shadow copies. An adversary may attempt to get information on shadow volumes to perform deletion or extract password hashes from the ntds.dit file. This rule requires command line logging or Windows PowerShell events (4104).

- **Effort:** master

- **Changelog:**

    - 11/07/2024 - minor - Adding new elements to detect and adding filter to reduce false positives.

</details>
            
<details>
<summary>Suspicious Headless Web Browser Execution To Download File</summary>


Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.

- **Effort:** elementary

</details>
    
<details>
<summary>System Info Discovery</summary>


System info discovery, attempt to detects basic command use to fingerprint a host.

- **Effort:** master

</details>
    
<details>
<summary>WMI Fingerprint Commands</summary>


Detects attacker fingerprint activities based on the correlation of specific WMIC commands. This has been observed with Aurora malware.

- **Effort:** advanced

- **Changelog:**

    - 19/08/2025 - major - Changing effort level.

</details>
            
**File and Directory Discovery**

<details>
<summary>Netskope DLP Alert</summary>


Detects DLP alerts which are not allowed.  

- **Effort:** master

- **Changelog:**

    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration
    - 29/06/2026 - minor - Update rule similarity

</details>
            
**Account Discovery**

<details>
<summary>AD Privileged Users Or Groups Reconnaissance</summary>


Detect privileged users or groups reconnaissance based on 4661 Event ID and known privileged users or groups SIDs. If the user account name is not a known admin it is suspicious.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>AD User Enumeration</summary>


Detects access to a domain user from a non-machine account. This requires Windows Security Event ID 4662 and could be triggered by some administrators configuring new users.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Active Directory Data Export Using Csvde</summary>


Detects the use of Csvde, a command-line tool from Windows Server that can be used to export Active Directory data to CSV files. This export doesn't include password hashes, but can be used as a discovery tool to enumerate users, machines and group memberships.

- **Effort:** elementary

</details>
    
<details>
<summary>Bloodhound and Sharphound Tools Usage</summary>


Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.

- **Effort:** intermediate

- **Changelog:**

    - 29/08/2025 - minor - Filtering some command line false positives.
    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    - 26/03/2024 - minor - Adapted the rule to remove false positives.

</details>
            
<details>
<summary>Discovery Commands Correlation</summary>


Detects some frequent discovery commands used by some ransomware operators.

- **Effort:** intermediate

- **Changelog:**

    - 16/04/2024 - minor - Adding new elements to increase detection.

</details>
            
<details>
<summary>Phosphorus (APT35) Exchange Discovery</summary>


According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about its the environment of compromised Microsoft Exchange servers. The command is the following: Get-Recipient | Select Name -ExpandProperty EmailAddresses -first 1 | Select SmtpAddress |  ft -hidetableheaders

- **Effort:** elementary

</details>
    
<details>
<summary>PowerView commandlets 1</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** advanced

- **Changelog:**

    - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.

</details>
            
<details>
<summary>PowerView commandlets 2</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** master

- **Changelog:**

    - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 07/04/2025 - minor - Changed similarity strategy and effort level.

</details>
            
<details>
<summary>Reconnaissance Commands Activities</summary>


Based on Cynet, Microsoft and Kaspersky analysis of Qakbot, this rule tries to detect some discovery TTPs.

- **Effort:** intermediate

</details>
    
<details>
<summary>Remote Enumeration Of Lateral Movement Groups</summary>


Detects remote sessions that list the members of four local groups relevant to lateral movement. This behavior is common in Active Directory mapping tools such as SharpHound. Legitimate Active Directory auditing and monitoring tools (e.g. Varonis, Netwrix) will also be detected, and can by excluded by applying an alert filter on the SID of the service account (user.id).

- **Effort:** intermediate

- **Changelog:**

    - 02/04/2025 - minor - Use chained correlation to group alerts by source account.

</details>
            
<details>
<summary>Remote Privileged Group Enumeration</summary>


Detects remote listing of local privileged group. Potential false positives, which should justify alert filters, are service accounts and administrators doing maintenance.

- **Effort:** advanced

- **Changelog:**

    - 18/04/2023 - minor - Exclude events from the Local System session that cause false positives.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Shell PID Injection</summary>


Detects when shells PID are listed and injected in another process. It can be performed to reuse sudo token related to shell in order to elevate privilege and maintain persistence.

- **Effort:** intermediate

</details>
    
**Network Share Discovery**

<details>
<summary>Correlation Admin Files Checked On Network Share</summary>


Detects requests to multiple admin files on a network share. This could be an attacker performing reconnaissance steps on the system.

- **Effort:** advanced

</details>
    
<details>
<summary>Netscan Share Access Artefact</summary>


Detects netscan artefact on windows network share - indicate network share discovery.

- **Effort:** intermediate

</details>
    
<details>
<summary>Network Share Discovery</summary>


Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. File sharing over a Windows network occurs over the SMB protocol. This technique is frequently leveraged by threat actors such as APT32, APT41, Wizard Spider. But also, through the use of some malware such as Cobalt Strike, Empire, PlugX and Ramsay.

- **Effort:** master

</details>
    
<details>
<summary>PowerView commandlets 1</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** advanced

- **Changelog:**

    - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.

</details>
            
<details>
<summary>PowerView commandlets 2</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** master

- **Changelog:**

    - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 07/04/2025 - minor - Changed similarity strategy and effort level.

</details>
            
**Domain Trust Discovery**

<details>
<summary>AdFind Usage</summary>


Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 

- **Effort:** elementary

- **Changelog:**

    - 12/10/2023 - minor - Slight change to a condition in order to reduce false positives.
    - 23/09/2025 - minor - Improving selection in order to reduce false positives.

</details>
            
<details>
<summary>Bloodhound and Sharphound Tools Usage</summary>


Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.

- **Effort:** intermediate

- **Changelog:**

    - 29/08/2025 - minor - Filtering some command line false positives.
    - 11/12/2024 - minor - Added a default similarity based on host name and user name to avoid too many alerts.
    - 26/03/2024 - minor - Adapted the rule to remove false positives.

</details>
            
<details>
<summary>Domain Trust Discovery Through LDAP</summary>


Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. "trustedDomain" which is detected here is a Microsoft Active Directory ObjectClass Type that represents a domain that is trusted by, or trusting, the local AD DOMAIN. Several tools are using LDAP queries in the end to get the information (DSQuery, sometimes ADFind as well, etc.)

- **Effort:** elementary

- **Changelog:**

    - 19/10/2023 - minor - improve filter to reduce false positives

</details>
            
<details>
<summary>NlTest Usage</summary>


Detects attempts to gather information on domain trust relationships that may be used to identify lateral movement opportunities. These command lines were observed in numerous attacks, but also sometimes from legitimate administrators for debugging purposes. The rule does not cover very basics commands but rather the ones that are interesting for attackers to gather information on a domain.

- **Effort:** advanced

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 10/10/2024 - minor - Adding new elements and filters to increase detection and reduce false positives.

</details>
            
<details>
<summary>Phosphorus Domain Controller Discovery</summary>


According to the Miscosoft's report, the group Phosphorus (part of APT35) uses a specific PowerShell command to collect information about the Domain Controller. The command is the following: "powershell.exe" /c Get-WMIObject Win32_NTDomain | findstr DomainController

- **Effort:** intermediate

</details>
    
<details>
<summary>PowerView commandlets 1</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** advanced

- **Changelog:**

    - 07/04/2025 - minor - Removed a keyword to reduce false positives and changed similarity strategy.

</details>
            
<details>
<summary>PowerView commandlets 2</summary>


Detects PowerView commandlets which perform network and Windows domain enumeration and exploitation. It provides replaces for almost all Windows net commands, letting you query users, machines, domain controllers, user descriptions, share, sessions, and more.

- **Effort:** master

- **Changelog:**

    - 04/10/2023 - major - Removed an option from the ScriptBlockText selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed
    - 07/04/2025 - minor - Changed similarity strategy and effort level.

</details>
            
<details>
<summary>Trickbot Malware Activity</summary>


Detects Trickbot malware process tree pattern in which rundll32.exe is parent of wermgr.exe.

- **Effort:** intermediate

</details>
    
**Software Discovery**

<details>
<summary>WMIC Command To Determine The Antivirus</summary>


Detects WMIC command to determine the antivirus on a system, characteristic of the ZLoader malware (and possibly others)

- **Effort:** advanced

- **Changelog:**

    - 28/02/2024 - minor - Adding a new usage of wmic.

</details>
            
**Cloud Service Discovery**

<details>
<summary>AWS Suspicious Discovery Commands</summary>


Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.

- **Effort:** master

</details>
    
<details>
<summary>AzureEdge in Command Line</summary>


Detects use of azureedge in the command line.

- **Effort:** advanced

</details>
    
**Cloud Infrastructure Discovery**

<details>
<summary>AWS Suspicious Discovery Commands</summary>


Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.

- **Effort:** master

</details>
    
**System Location Discovery**

<details>
<summary>Language Discovery</summary>


Detects when a user makes a query on the language of the system.

- **Effort:** advanced

</details>
    
**Cloud Storage Object Discovery**

<details>
<summary>AWS Suspicious Discovery Commands</summary>


Attackers often use discovery commands such as DescribeInstances or DescribeSecurityGroups, and many others, to find how an AWS tenant is configured.

- **Effort:** master

</details>
    
## Lateral Movement
**Remote Services**

<details>
<summary>AWS CloudTrail EC2 CreateKeyPair</summary>


Detects when a key pair is created. Usually, SendSSHPublicKey is used afterwards to push the created key to an EC2 instance in order to be able to establish a connection to that instance.

- **Effort:** advanced

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID.

</details>
            
<details>
<summary>AWS CloudTrail EC2 DeleteKeyPair</summary>


Detects when a specific key pair is deleted. This means the public key was removed from EC2.

- **Effort:** advanced

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>AWS CloudTrail EC2 Enable Serial Console Access</summary>


Detects when the EC2 serial console access feature is enabled. This could abused by some attackers to avoid network detection when accessing to EC2 instances.

- **Effort:** intermediate

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>AWS CloudTrail EC2 Instance Connect SendSSHPublicKey</summary>


Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a connection to the console using SSH.

- **Effort:** advanced

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>AWS CloudTrail EC2 Instance Connect SendSerialConsoleSSHPublicKey</summary>


Detects when an attacker is pushing an SSH Public Key to an EC2 instance. Then he can establish a serial connection to the console using SSH.

- **Effort:** advanced

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>Admin Share Access</summary>


Detects access to $ADMIN share. The advanced audit policy setting "Object Access > Audit File Share" must be configured for Success/Failure. Also be very cautious to previously check if this is not commonly used by your administrators as to remotely manage your computers.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Akamai Guardicore Medium On-Prem Severity Security Incident</summary>


Akamai Guardicore has detected a medium severity security incident, indicating suspicious activity that warrants analyst review. This may include unusual lateral movement patterns, policy violations, or communication with suspicious but unconfirmed malicious endpoints.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem High Severity Security Incident</summary>


Akamai Guardicore has detected a high severity security incident, indicating a likely confirmed threat such as communication with a known malicious IP, active malware beaconing, or exploitation of a vulnerable asset. Immediate triage is required.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem Low Severity Security Incident</summary>


Akamai Guardicore has detected a low severity security incident, such as a connection attempt to an IP address with a bad reputation identified by the Guardicore Reputation Service.

- **Effort:** master

</details>
    
<details>
<summary>Cobalt Strike Default Service Creation Usage</summary>


Detects Cobalt Strike usage from an existing beacon when attacker tries to elevate or move laterally through a service creation.

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Corelight Lateral Movement Notice</summary>


Detects a Zeek notice raised by a Corelight sensor that is related to lateral movement activity (e.g. ATTACK::Lateral_Movement), often indicating an adversary moving across internal hosts.

- **Effort:** master

</details>
    
<details>
<summary>Correlation Impacket Smbexec</summary>


This rule detects the execution of smbexec via the relevant share pattern name 

- **Effort:** elementary

</details>
    
<details>
<summary>Denied Access To Remote Desktop</summary>


Detects when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop. This event can be generated by attackers when searching for available windows servers in the network. This rule detects only users from external network.

- **Effort:** intermediate

- **Changelog:**

    - 19/10/2023 - minor - Minor change in selection to reduce false positives.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Lateral Movement Remote Named Pipe</summary>


Detects lateral movement and remote exec using named pipe over network. This requires Windows Security event logging with the File Share enable policy.

- **Effort:** advanced

- **Changelog:**

    - 12/06/2024 - minor - Fix filter selection
    - 03/04/2024 - major - Rule's pattern field changed
    - 26/03/2024 - minor - Filter was improved to reduce false positives

</details>
            
<details>
<summary>Lsass Access Through WinRM</summary>


Detects the access of LSASS.exe process through Windows Remote Management (WinRM) protocol. This is often done using Invoke-Mimikatz -ComputerName command, which uses PSRemoting and therefore WinRM. However, this is not limited to the Mimikatz threat and can be done by other tools as well. This rule needs Process Access monitoring, which can be done using Sysmon's event ID 10.

- **Effort:** intermediate

</details>
    
<details>
<summary>MMC Spawning Windows Shell</summary>


Detects a Windows command line executable started from MMC process

- **Effort:** master

- **Changelog:**

    - 26/03/2025 - minor - Adding similarity and changing effort level.

</details>
            
<details>
<summary>MMC20 Lateral Movement</summary>


Detects MMC20.Application Lateral Movement; specifically looks for the spawning of the parent MMC.exe with a command line of "-Embedding" as a child of svchost.exe.

- **Effort:** intermediate

</details>
    
<details>
<summary>Protected Storage Service Access</summary>


Detects access to a protected_storage service over the network. It could identify potential abuse of DPAPI to extract domain backup keys from Domain Controllers.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 09/05/2025 - minor - Adding similarity to regroup alerts.

</details>
            
<details>
<summary>RDP Login From Localhost</summary>


Detects RDP login from localhost source address, which may be a tunnelled login to bypass network restrictions.

- **Effort:** advanced

- **Changelog:**

    - 24/11/2023 - minor - Effort level changed to advanced.
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>RDP Port Change Using Powershell</summary>


Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 

- **Effort:** intermediate

</details>
    
<details>
<summary>Remote Service Activity Via SVCCTL Named Pipe</summary>


Detects remote service activity via remote access to the svcctl named pipe

- **Effort:** master

- **Changelog:**

    - 21/03/2024 - minor - change filter to ACL hex value and adapt effort
    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Smbexec.py Service Installation</summary>


Detects the use of smbexec.py tool by detecting a specific service installation

- **Effort:** elementary

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
**Replication Through Removable Media**

<details>
<summary>External Disk Drive Or USB Storage Device</summary>


Detects external diskdrives or plugged in USB device.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Exploitation of Remote Services**

<details>
<summary>Audit CVE Event</summary>


Detects events generated by Windows to indicate the exploitation of a known vulnerability.

- **Effort:** elementary

- **Changelog:**

    - 15/07/2024 - major - review filter and improve similarity

</details>
            
<details>
<summary>CVE-2019-0708 Scan</summary>


Detects the use of a scanner that discovers targets vulnerable to CVE-2019-0708 RDP RCE aka BlueKeep.

- **Effort:** elementary

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>ESET Protect Remote Action</summary>


Detects when different remote commands are performed on the same hostname is a short amount of time.

- **Effort:** master

</details>
    
<details>
<summary>Registry Checked For Lanmanserver DisableCompression Parameter</summary>


Detects registry access for Lanmanserver\Parameters. The check of the value DisableCompression could be a sign of an attack trying to exploit SMBGhost vulnerability (CVE-2020-0796).

- **Effort:** master

</details>
    
**Use Alternate Authentication Material**

<details>
<summary>Abusing Azure Browser SSO</summary>


Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser. An attacker can use this to authenticate to Azure AD in a browser as that user. This technique leverages the COM object (CoCreateInstance), which loads the DLL "C:\Windows\System32\MicrosoftAccountTokenProvider.dll", to get an authentication token. Monitoring the load of this DLL can detect an attacker abusing this technique. More details on this technique are available in the article in the source section. The prerequisite is to log for Loaded DLLs, it can be done using the Sysmon Event ID 7 (DLL image loaded by process). 

- **Effort:** master

</details>
    
<details>
<summary>Potential RDP Connection To Non-Domain Host</summary>


Detects logons using NTLM to hosts that are potentially not part of the domain using RDP (TermSrv). Event ID 8001 corresponds to outgoing NTLM authentication traffic and TermSrv stands for RDP Terminal Services Server. Check if the contacted host is legitimate. To use this detection rule, enable logging of outbound NTLM authentications on all domain controllers, using the following Group Policy (GPO) - Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers -> Define this policy setting: Audit all.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Rubeus Tool Command-line</summary>


Detects command line parameters used by Rubeus, a toolset to interact with Kerberos and abuse it.

- **Effort:** advanced

</details>
    
<details>
<summary>Successful Overpass The Hash Attempt</summary>


Detects successful logon with logon type 9 (NewCredentials) which matches the Overpass the Hash behavior of e.g Mimikatz's sekurlsa::pth module.

- **Effort:** advanced

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed
    - 25/03/2025 - minor - Changing pattern, adding similarity and changing effort level.

</details>
            
**Remote Service Session Hijacking**

<details>
<summary>Potential macOS SSH Brute Force Detected</summary>


Detects a potential ssh bruteforce to gain access to accounts.

- **Effort:** advanced

</details>
    
## Collection
**Data from Local System**

<details>
<summary>AWS CloudTrail EC2 VM Export Failure</summary>


Detects attempt to export an AWS EC2 instance. A VM Export might indicate an attempt to extract information from an instance.

- **Effort:** intermediate

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>Flare Events Stealer Log Malware Infection</summary>


Detects a Flare stealer log event with an identified malware family, indicating credentials or host data were likely collected by infostealer malware.

- **Effort:** master

</details>
    
<details>
<summary>Flare Events Suspicious Forum Post</summary>


Detects a Flare forum post event, indicating credentials or host data were likely collected by infostealer malware.

- **Effort:** master

</details>
    
<details>
<summary>Formbook File Creation DB1</summary>


Detects specific file creation (Users\*\AppData\Local\Temp\DB1) to store data to exfiltrate (Formbook behavior). Logging for Sysmon event 11 is usually used for this detection. 

- **Effort:** intermediate

</details>
    
<details>
<summary>Information Stealer Downloading Legitimate Third-Party DLLs</summary>


Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft Exchange PowerShell Snap-Ins To Export Exchange Mailbox Data</summary>


Detects PowerShell SnapIn command line or PowerShell script, often used with Get-Mailbox to export Exchange mailbox data.

- **Effort:** intermediate

- **Changelog:**

    - 13/08/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Ntfsinfo Usage</summary>


Detects when the command ntfsinfo is used. An attacker can access to information on the volume from NTFS and have a directory dump of NTFS files.

- **Effort:** advanced

</details>
    
**Data from Network Shared Drive**

<details>
<summary>RDP Configuration File From Mail Process</summary>


Detects RDP configuration file being created or executed by a Mail-related process like Outlook. RDP configuration file will allow, when opened, an user to connect to the configured server easily. Attackers use this to trick victims in order to get a shared drive and potentially retrieve the data from that drive, but also drop a malicious file on the drive to establish persistence. Using RDP can also expose the victim's credential and clipboard data on some cases.

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious Access To Sensitive File Extensions</summary>


Detects known sensitive file extensions accessed on a network share. This activity could possibly correspond to a malicious one (removing backup, reading sensitive files, etc.).

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Email Attachment Received</summary>


Detects email containing a suspicious file as an attachment, based on its extension.

- **Effort:** advanced

- **Changelog:**

    - 27/03/2025 - minor - Adding new extension
    - 15/04/2024 - minor - Update email from field to latest parser format
    - 14/11/2024 - major - Adding new file extension and new condition to make the rule broader as it can now match on more intakes.

</details>
            
**Input Capture**

<details>
<summary>AppleScript Password Prompt</summary>


Detects when a prompt is displayed to gain credentials. This technique is used by MacOS malware to obtain the user's password.

- **Effort:** advanced

</details>
    
**Data Staged**

<details>
<summary>CVE-2021-20023 SonicWall Arbitrary File Read</summary>


Detects Arbitrary File Read, which can be used with other vulnerabilities as a mean to obtain outputs generated by attackers, or sensitive data.

- **Effort:** advanced

</details>
    
**Email Collection**

<details>
<summary>Entra ID Consent Attempt to Suspicious OAuth Application</summary>


Detects an attempt to authorize account access to an OAuth application commonly used in business email compromise (BEC) attacks. Investigate the source IP address: unusual countries, RDP hosts and VPN providers are likely indicators of malicious activity.

- **Effort:** elementary

</details>
    
<details>
<summary>Exchange Mailbox Export</summary>


Detection of a standard Exchange Mailbox export, which stores all mails from a user in a pst file, from command line or PowerShell script.

- **Effort:** intermediate

</details>
    
<details>
<summary>Google Cloud Audit Logs Custom Gmail Route</summary>


Detects when a custom Gmail route is added or modified. This could be abused by attackers to exfiltrate data.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Cloud Audit Logs Email Forwarding</summary>


Detects when an out of domain email forwarding is enabled on Google Cloud.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace Email Forwarding</summary>


Detects when a user enables email forwarding out of the domain

- **Effort:** advanced

</details>
    
<details>
<summary>Microsoft 365 Email Forwarding To Consumer Email Address</summary>


An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (most common consumer email services).

- **Effort:** intermediate

- **Changelog:**

    - 22/04/2024 - minor - Add zohomail.com

</details>
            
<details>
<summary>Microsoft 365 Email Forwarding To Email Address With Rare TLD</summary>


An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (less common top-level domain).

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 Email Forwarding To Privacy Email Address</summary>


An email forwarding rule was created, that automatically forwards incoming emails to an address outside of the organization (most common privacy email services).

- **Effort:** elementary

- **Changelog:**

    - 31/12/2025 - minor - Add a domain name to the pattern

</details>
            
<details>
<summary>Outlook Registry Access</summary>


Detection of accesses to Microsoft Outlook registry hive, which might contain sensitive information.

- **Effort:** master

- **Changelog:**

    - 02/04/2024 - major - Updating the pattern and adding filter selection
    - 19/02/2024 - minor - Effort level was adapted according to the observed hits for the rule

</details>
            
**Audio Capture**

<details>
<summary>Audio Capture via PowerShell</summary>


Detects audio capture via PowerShell Cmdlet

- **Effort:** intermediate

- **Changelog:**

    - 18/04/2023 - minor - Use more specific patterns to fix false positives.

</details>
            
**Data from Cloud Storage**

<details>
<summary>Netskope DLP Alert</summary>


Detects DLP alerts which are not allowed.  

- **Effort:** master

- **Changelog:**

    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration
    - 29/06/2026 - minor - Update rule similarity

</details>
            
**Adversary-in-the-Middle**

<details>
<summary>Correlation Suspicious Authentication Coercer Behavior</summary>


Detect a possible NTLM Relay attack combine with authent coerce

- **Effort:** intermediate

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (CEPHAS 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit CEPHAS 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Gabagool)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Gabagool. The `filter_password_spraying` exclusion corresponds to a password spraying tool which is already detected by the rule `Entra ID Password Compromised By Known Credential Testing Tool`.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Greatness)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Greatness.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (HoneySecurity / HoneyStorm)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit HoneySecurity / HoneyStorm.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Mamba 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit tracked by Sekoia.io as Mamba 2FA.

- **Effort:** elementary

- **Changelog:**

    - 09/08/2024 - major - Update the indicator.
    - 25/09/2024 - major - Rename the rule, update the indicators.
    - 23/12/2024 - major - Update the indicators.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Rockstar 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Rockstar 2FA.

- **Effort:** elementary

</details>
    
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Sneaky 2FA)</summary>


Detects a sign-in attempt with an impossible device shift characteristic of the adversary-in-the-middle phishing kit Sneaky 2FA.

- **Effort:** elementary

- **Changelog:**

    - 25/02/2025 - major - Update the indicator.

</details>
            
<details>
<summary>Entra ID Sign-In Via Known AiTM Phishing Kit (Tycoon 2FA)</summary>


Detects a sign-in attempt with known characteristics of the adversary-in-the-middle phishing kit Tycoon 2FA.

- **Effort:** elementary

- **Changelog:**

    - 01/10/2024 - major - Update the pattern following changes in the phishing kit.
    - 31/12/2025 - major - Change the similarity strategy to user.id instead of user.email.

</details>
            
<details>
<summary>EvilProxy Phishing Domain</summary>


Detects subdomains potentially generated by the EvilProxy adversary-in-the-middle phishing platform. Inspect the other subdomains of the domain to identify the landing page, and determine if the user submitted credentials. This rule has a small percentage of false positives on legitimate domains.

- **Effort:** intermediate

</details>
    
<details>
<summary>Microsoft 365 Sign-in With No User Agent</summary>


Detects a sign-in without any User-Agent header. This may indicate that the sign-in originated from an adversary-in-the-middle phishing page or a password spraying tool. Sign-ins happening through a regular web browser always have a User-Agent header. Investigate the source IP address. If it is unknown, assume that the account's password is compromised.

- **Effort:** elementary

- **Changelog:**

    - 04/12/2023 - major - Added `Login:login` request type with a filter for codes indicating failure
    - 10/04/2025 - minor - Exclude more error codes to reduce false positives
    - 01/06/2026 - minor - Adding filter on user_type code to reduce false positives

</details>
            
<details>
<summary>Multiple Authentication On Microsoft 365 (Office 365) Portal From Two IP Addresses</summary>


Detection of login events from two IP addresses within 3mn, as it could happen if someone got phished with a tool like Evilginx2.

- **Effort:** intermediate

- **Changelog:**

    - 01/06/2026 - minor - Adding more filter and review group-by clause to reduce false positives

</details>
            
<details>
<summary>Possible RottenPotato Attack</summary>


Detects logon events that have characteristics of events generated during an attack leveraging RottenPotato.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Potential Azure AD Phishing Page (Adversary-in-the-Middle)</summary>


Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.

- **Effort:** intermediate

- **Changelog:**

    - 02/08/2024 - minor - Exclude an additionnal legitimate domain.
    - 13/08/2025 - minor - Exclude additional legitimate domains and common benign positives.

</details>
            
<details>
<summary>Sign-In Via Known AiTM Phishing Kit</summary>


Detects a sign-in attempt from an IP address belonging to a known adversary-in-the-middle phishing kit.

- **Effort:** elementary

- **Changelog:**

    - 12/12/2024 - minor - Update the selections to use a more appropriate ECS field. The rule now matches on more intakes. The name of the rule has been modified as well.

</details>
            
**Archive Collected Data**

<details>
<summary>Compress Data for Exfiltration via Archiver</summary>


Detects data compressed by specific tools.

- **Effort:** master

- **Changelog:**

    - 09/07/2024 - major - Reviewing detection to reduce false positives.

</details>
            
<details>
<summary>Data Compressed With Rar</summary>


An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program.

- **Effort:** master

</details>
    
<details>
<summary>Data Compressed With Rar With Password</summary>


An adversary may compress data in order to make it portable and minimize the amount of data sent over the network, this could be done the popular rar command line program. This is a more specific one for rar where the arguments allow to encrypt both file data and headers with a given password.

- **Effort:** intermediate

</details>
    
<details>
<summary>PowerShell Data Compressed</summary>


Detects data compression through a PowerShell command (could be used by an adversary for exfiltration).

- **Effort:** advanced

</details>
    
## Command and Control
**Data Obfuscation**

<details>
<summary>Suspicious ADSI-Cache Usage By Unknown Tool</summary>


Detects the usage of ADSI (LDAP) operations by tools. This may also detect tools like LDAPFragger. It needs file monitoring capabilities (Sysmon Event ID 11 with .sch file creation logging).

- **Effort:** advanced

</details>
    
<details>
<summary>Suspicious LDAP-Attributes Used</summary>


Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies. Careful as the 5136 is only on domain controllers and needs to be activated through the Group Policy.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Application Layer Protocol**

<details>
<summary>Akamai Guardicore Medium On-Prem Severity Security Incident</summary>


Akamai Guardicore has detected a medium severity security incident, indicating suspicious activity that warrants analyst review. This may include unusual lateral movement patterns, policy violations, or communication with suspicious but unconfirmed malicious endpoints.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem High Severity Security Incident</summary>


Akamai Guardicore has detected a high severity security incident, indicating a likely confirmed threat such as communication with a known malicious IP, active malware beaconing, or exploitation of a vulnerable asset. Immediate triage is required.

- **Effort:** master

</details>
    
<details>
<summary>Akamai Guardicore On-Prem Low Severity Security Incident</summary>


Akamai Guardicore has detected a low severity security incident, such as a connection attempt to an IP address with a bad reputation identified by the Guardicore Reputation Service.

- **Effort:** master

</details>
    
<details>
<summary>Bazar Loader DGA (Domain Generation Algorithm)</summary>


Detects Bazar Loader domains based on the Bazar Loader DGA

- **Effort:** elementary

</details>
    
<details>
<summary>Cato Networks SASE High Risk Alert</summary>


Cato Networks SASE intrusion detection has detected a high risk alert.

- **Effort:** master

</details>
    
<details>
<summary>Chafer (APT 39) Activity</summary>


Detects previous Chafer (APT 39) activity attributed to OilRig as reported in Nyotron report in March 2018.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Cloudflare Gateway DNS Query Allowed to Malicious Domain</summary>


A DNS query to a domain categorized by Cloudflare Gateway as malicious was allowed because no blocking policy is configured.

- **Effort:** master

</details>
    
<details>
<summary>Cloudflare Gateway DNS Query Blocked to Malicious Domain</summary>


A DNS query to a domain categorized by Cloudflare Gateway as malicious was blocked by policy.

- **Effort:** master

</details>
    
<details>
<summary>Cloudflare Gateway HTTP File Blocked By Anti-Virus Scan</summary>


Cloudflare Gateway allows admins to enable Anti-Virus (AV) scanning of files that are uploaded or downloaded by users as the file passes through Gateway. AV scanning of files requires organizations to enable Proxy mode under Settings > Network > Layer 7 Firewall. TLS decryption is also recommended to enable inspection of HTTPS traffic.

- **Effort:** advanced

</details>
    
<details>
<summary>Cobalt Strike DNS Beaconing</summary>


Detects suspicious DNS queries known from Cobalt Strike beacons. The threshold is more than 50 suspicious DNS requests to avoid false positives.

- **Effort:** advanced

</details>
    
<details>
<summary>Cobalt Strike HTTP Default GET beaconing</summary>


Detects GET HTTP queries from known Cobalt Strike beacons (source code 4.3)

- **Effort:** advanced

</details>
    
<details>
<summary>Cobalt Strike HTTP Default POST Beaconing</summary>


Detects POST HTTP queries from known Cobalt Strike beacons (source code 4.3)

- **Effort:** advanced

</details>
    
<details>
<summary>Corelight DNS NULL Record Query (Possible Tunneling)</summary>


Detects DNS queries of type NULL observed by a Corelight sensor. NULL record queries are rarely used by legitimate clients and are a strong indicator of DNS tunneling used for command-and-control or data exfiltration.

- **Effort:** master

</details>
    
<details>
<summary>Corelight Suricata Trojan Activity Alert</summary>


Detects a Suricata IDS alert categorized as trojan activity (e.g. "A Network Trojan was detected") reported by a Corelight sensor. This category typically flags malware command-and-control or beaconing traffic.

- **Effort:** master

</details>
    
<details>
<summary>Corelight Threat Intelligence Indicator Match</summary>


Detects a match against the Zeek Intelligence Framework on a Corelight sensor (intel log), meaning observed network traffic matched a known threat intelligence indicator (domain, IP, hash, etc.).

- **Effort:** master

</details>
    
<details>
<summary>Correlation Potential DNS Tunnel</summary>


Detects domain name which is longer than 62 characters and requested at least 50 times in a 10 minutes range time. Long domain names are distinctive of DNS tunnels.

- **Effort:** advanced

- **Changelog:**

    - 19/07/2023 - major - New regex pattern and new filters.
    - 20/01/2025 - major - Update regex pattern to improve detection, decrease count number, and add more filters to avoid false positives

</details>
            
<details>
<summary>Covenant Default HTTP Beaconing</summary>


Detects potential Covenant communications through the user-agent and specific urls

- **Effort:** intermediate

</details>
    
<details>
<summary>CrowdStrike Falcon Mobile Detection Critical Severity</summary>


CrowdStrike Falcon for Mobile raised an alert with critical severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Mobile Detection High Severity</summary>


CrowdStrike Falcon for Mobile raised an alert with high severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Mobile Detection Informational Severity</summary>


CrowdStrike Falcon for Mobile raised an alert with informational severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Mobile Detection Low Severity</summary>


CrowdStrike Falcon for Mobile raised an alert with low severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>CrowdStrike Falcon Mobile Detection Medium Severity</summary>


CrowdStrike Falcon for Mobile raised an alert with medium severity

- **Effort:** master

- **Changelog:**

    - 10/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Cryptomining</summary>


Detection of domain names potentially related to cryptomining activities.

- **Effort:** master

</details>
    
<details>
<summary>DNS Exfiltration and Tunneling Tools Execution</summary>


Well-known DNS exfiltration tools execution

- **Effort:** intermediate

</details>
    
<details>
<summary>DNS Tunnel Technique From MuddyWater</summary>


Detecting DNS Tunnel Activity For Muddywater intrusion set. This is the loading of a specific DLL from an Excel macro which is detected.

- **Effort:** elementary

</details>
    
<details>
<summary>Detect requests to Konni C2 servers</summary>


This rule detects requests to Konni C2 servers. These patterns come from an analysis done in 2022, September.

- **Effort:** elementary

</details>
    
<details>
<summary>Download File On Cloud Storage Through Command Line</summary>


Detects commonly used commands like curl or wget used to download files on a Cloud Storage URL like a Google Drive URL.

- **Effort:** intermediate

</details>
    
<details>
<summary>Dynamic DNS Contacted</summary>


Detect communication with dynamic dns domain. This kind of domain is often used by attackers. This rule can trigger false positive in non-controlled environment because dynamic dns is not always malicious.

- **Effort:** master

</details>
    
<details>
<summary>Exfiltration And Tunneling Tools Execution</summary>


Execution of well known tools for data exfiltration and tunneling

- **Effort:** advanced

</details>
    
<details>
<summary>FoggyWeb HTTP Default GET/POST Requests</summary>


Detects GET or POST request pattern observed within the first FoggyWeb campaign detected by Microsoft.

- **Effort:** advanced

</details>
    
<details>
<summary>Google Workspace External Sharing</summary>


Detects a large number of external sharing.

- **Effort:** master

- **Changelog:**

    - 20/06/2024 - minor - Adding new elements to increase detection.
    - 18/12/2025 - major - Deleting elements to reduce false positives.

</details>
            
<details>
<summary>Koadic MSHTML Command</summary>


Detects Koadic payload using MSHTML module

- **Effort:** intermediate

</details>
    
<details>
<summary>LokiBot Default C2 URL</summary>


Detects default C2 URL for trojan LokiBot

- **Effort:** elementary

</details>
    
<details>
<summary>Many Downloads From Several Binaries</summary>


Threat Actors might use all the binaries to download the payload to make sure at least one is present on the target. The prerequisites are to enable monitoring of the connect syscall using Auditbeat.

- **Effort:** advanced

</details>
    
<details>
<summary>Nimbo-C2 User Agent</summary>


Nimbo-C2 Uses an unusual User-Agent format in its implants.

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential Bazar Loader User-Agents</summary>


Detects potential Bazar loader communications through the user-agent

- **Effort:** elementary

</details>
    
<details>
<summary>Potential Lemon Duck User-Agent</summary>


Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".

- **Effort:** elementary

</details>
    
<details>
<summary>Potential LokiBot User-Agent</summary>


Detects potential LokiBot communications through the user-agent

- **Effort:** intermediate

- **Changelog:**

    - 04/08/2023 - minor - Added a condition to only match on internal IP as source

</details>
            
<details>
<summary>Python HTTP Server</summary>


Detects command used to start a Simple HTTP server in Python. Threat actors could use it for data extraction, hosting a webshell or else.

- **Effort:** intermediate

</details>
    
<details>
<summary>Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL</summary>


Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.

- **Effort:** elementary

- **Changelog:**

    - 13/06/2023 - minor - Adding private IPs as sources

</details>
            
<details>
<summary>SEKOIA.IO Intelligence Feed</summary>


Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.

- **Effort:** elementary

</details>
    
<details>
<summary>Sigma Intelligence Arcane Stealer HTTP Communication</summary>


Detects potential Arcane Stealer communications through the User-Agent.

- **Effort:** elementary

</details>
    
<details>
<summary>Sliver DNS Beaconing</summary>


Detects suspicious DNS queries known from Sliver beaconing 

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious LDAP-Attributes Used</summary>


Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies. Careful as the 5136 is only on domain controllers and needs to be activated through the Group Policy.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious Windows DNS Queries</summary>


Detects a suspicious Windows command-line process making a DNS query via known abuse text paste web services. This is based on Microsoft Windows Sysmon events (Event ID 22).

- **Effort:** advanced

- **Changelog:**

    - 21/07/2025 - minor - Updating pattern with new field and new filter to avoid false positives.
    - 11/06/2025 - minor - Added filters to reduce false positives.
    - 02/08/2023 - minor - Added a new field and filters to reduce false positives.

</details>
            
<details>
<summary>Trellix Network Security Threat Blocked</summary>


Trellix Network Security has detected a malicious traffic and blocked it.

- **Effort:** master

</details>
    
<details>
<summary>Trellix Network Security Threat Notified</summary>


Trellix Network Security has detected a malicious traffic and raised an alert.

- **Effort:** master

</details>
    
<details>
<summary>TrevorC2 HTTP Communication</summary>


Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 

- **Effort:** elementary

</details>
    
**Proxy**

<details>
<summary>Microsoft 365 Authenticated Activity From Tor IP Address</summary>


Detects authenticated Microsoft 365 activity from an IP address associated with Tor.

- **Effort:** advanced

</details>
    
<details>
<summary>Netsh Port Forwarding</summary>


Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Suspicious Hostname</summary>


Detects suspicious hostnames such as ones with kali in it, to detect kali linux default hosts, but also other hostnames commonly used in attacks. List can be improved according to the environment.

- **Effort:** advanced

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Suspicious TOR Gateway</summary>


Detects suspicious TOR gateways. Gateways are often used by the victim to pay and decrypt the encrypted files without installing TOR. Tor intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.

- **Effort:** advanced

</details>
    
<details>
<summary>TOR Usage</summary>


Detects TOR usage, based on the IP address and the destination port (filtered on NTP). TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.

- **Effort:** master

</details>
    
<details>
<summary>TOR Usage Generic Rule</summary>


Detects TOR usage globally, whether the IP is a destination or source. TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.

- **Effort:** master

- **Changelog:**

    - 26/01/2024 - minor - Modifying filter to improve rule.
    - 22/11/2023 - minor - Adding filter to improve rule.
    - 02/08/2024 - minor - Small pattern to change to match only the real tags related to TOR.
    - 14/08/2025 - minor - Adding NTP filter to reduce false positives.

</details>
            
**Web Service**

<details>
<summary>Discord Suspicious Download</summary>


Discord is a messaging application. It allows users to create their own communities to share messages and attachments. Those attachments have little to no overview and can be downloaded by almost anyone, which has been abused by attackers to host malicious payloads.

- **Effort:** advanced

- **Changelog:**

    - 25/03/2025 - major - Change the rule effort and similarity strategy.
    - 05/08/2023 - minor - Added filters for commonly observed files extensions.

</details>
            
<details>
<summary>Telegram Bot API Request</summary>


Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind

- **Effort:** advanced

</details>
    
**Ingress Tool Transfer**

<details>
<summary>Cloudflare Gateway HTTP File Blocked By Anti-Virus Scan</summary>


Cloudflare Gateway allows admins to enable Anti-Virus (AV) scanning of files that are uploaded or downloaded by users as the file passes through Gateway. AV scanning of files requires organizations to enable Proxy mode under Settings > Network > Layer 7 Firewall. TLS decryption is also recommended to enable inspection of HTTPS traffic.

- **Effort:** advanced

</details>
    
<details>
<summary>Corelight Windows Executable Download</summary>


Detects the transfer of a Windows executable (PE / application/x-dosexec) observed by a Corelight sensor in the files log. Executable downloads are a common malware delivery vector and warrant investigation.

- **Effort:** master

</details>
    
<details>
<summary>Correlation Netcat Infection Chain</summary>


Detect netcat connection to download et execute payload via piped bash

- **Effort:** elementary

</details>
    
<details>
<summary>Information Stealer Downloading Legitimate Third-Party DLLs</summary>


Detects operations that involved legitimate third-party DLLs used by information-stealing malware for data collection on the infected host. This detection rule correlates at least 7 events including the following DLLs - freebl3.dll, vcruntime140.dll, msvcp140.dll, nss3.dll, sqlite3.dll, softokn3.dll, mozglue.dll and libcurl.dll. This behaviour matches activities of several widespread stealer like Vidar, Raccoon Stealer v2, Mars Stealer, etc.

- **Effort:** intermediate

</details>
    
<details>
<summary>Network Connection Via Certutil</summary>


Identifies certutil.exe making a network connection. Adversaries could abuse certutil.exe to download a certificate, or malware, from a remote URL.

- **Effort:** intermediate

- **Changelog:**

    - 21/03/2025 - major - Review rule to reduce false positives and increases detection scope.

</details>
            
<details>
<summary>Pandemic Windows Implant</summary>


Detects Pandemic Windows Implant through registry keys or specific command lines. Prerequisites: Logging for Registry events is needed, which can be done in the Sysmon configuration (events 12 and 13).

- **Effort:** master

- **Changelog:**

    - 20/03/2025 - major - Rule's effort level has been changed to master, similarity and filter added.

</details>
            
<details>
<summary>Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL</summary>


Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.

- **Effort:** elementary

- **Changelog:**

    - 13/06/2023 - minor - Adding private IPs as sources

</details>
            
<details>
<summary>Rclone Process</summary>


Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.

- **Effort:** advanced

- **Changelog:**

    - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 05/08/2024 - major - Edited pattern of the rule to reduce false positives.

</details>
            
<details>
<summary>Suspicious Desktopimgdownldr Execution</summary>


Detects a suspicious Desktopimgdownldr execution. Desktopimgdownldr.exe is a Windows binary used to configure lockscreen/desktop image and can be abused to download malicious file.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Finger Usage</summary>


Detects suspicious aged finger.exe tool execution often used in malware attacks nowadays. An attacker can use finger to silently retrieve a command, a script or a payload from a remote server. For example, the tool Darkfinger-C2 uses this technique to download files from the C2 channel.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Headless Web Browser Execution To Download File</summary>


Detects a suspicious command used to execute a Chromium-based web browser (Chrome or Edge) using the headless mode, meaning that the browser window wouldn't be visible, and the dump mode to download a file. This technique can be used to fingerprint the compromised host, in particular by the Ducktail infostealer.

- **Effort:** elementary

</details>
    
<details>
<summary>Suspicious URI Used In A Lazarus Campaign</summary>


Detects suspicious requests to a specific URI, usually on an .asp page. The website is often compromised.

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious certutil command</summary>


Detects suspicious certutil command which can be used by threat actors to download and/or decode payload. 

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2023 - minor - "encode" and "decode" were removed as it was causing too much false positives while not being the main usage of the certutil command by attackers.

</details>
            
**Data Encoding**

<details>
<summary>DNS Exfiltration and Tunneling Tools Execution</summary>


Well-known DNS exfiltration tools execution

- **Effort:** intermediate

</details>
    
**Traffic Signaling**

<details>
<summary>Binary List Tcp</summary>


A binary is trying to list TCP connections. The prerequisites are to enable monitoring of the open and openat syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
**Remote Access Tools**

<details>
<summary>Antivirus Exploitation Framework Detection</summary>


Detects a highly relevant Antivirus alert that reports an exploitation framework. This is based on Windows Defender logs (Event ID 1116 and 1117). 

- **Effort:** elementary

- **Changelog:**

    - 16/02/2026 - minor - Filtering out Event ID 1011 which caused false positives. The rule fired at the deletion of a quarantined file by Defender which was not the wanted behaviour.

</details>
            
<details>
<summary>Antivirus Password Dumper Detection</summary>


Detects a highly relevant Antivirus alert that reports a password dumper. This detection relies on Windows Defender events logs. This is based on Windows Defender logs (Event ID 1116 and 1117).

- **Effort:** elementary

</details>
    
<details>
<summary>Antivirus Relevant File Paths Alerts</summary>


Detects an Antivirus alert in a highly relevant file path or with a relevant file name. This is only based on Windows Defender events.

- **Effort:** master

- **Changelog:**

    - 15/02/2024 - minor - Effort level was adapted according to the observed hits for the rule.
    - 26/03/2024 - major - Rule's pattern field changed
    - 22/04/2025 - major - Change effort level and similarity strategy

</details>
            
<details>
<summary>Remote Access Tool Domain</summary>


Detects traffic toward a domain flagged as a Remote Administration Tool (RAT).

- **Effort:** master

</details>
    
<details>
<summary>Remote Monitoring and Management Software - AnyDesk</summary>


Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool AnyDesk.

- **Effort:** master

</details>
    
<details>
<summary>Remote Monitoring and Management Software - Atera</summary>


Detect artifacts related to the installation or execution of the Remote Monitoring and Management tool Atera.

- **Effort:** master

</details>
    
<details>
<summary>Suspicious Activity Using Quick Assist</summary>


Detects when a chat is created (abusing Quick Assist feature) with a user external to the domain, which has been observed as a some phishing attemp by ransomware groups.

- **Effort:** elementary

</details>
    
**Dynamic Resolution**

<details>
<summary>Gatewatcher AionIQ V103 Dga Detect High</summary>


Detects when an event related to dga is raised by gatewatcher with a high severity. An attacker can use this to generate a new domain for C2.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Dga Detect Low</summary>


Detects when an event related to dga is raised by gatewatcher with a low severity. An attacker can use this to generate a new domain for C2.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Dga Detect Medium</summary>


Detects when an event related to dga is raised by gatewatcher with a medium severity. An attacker can use this to generate a new domain for C2.

- **Effort:** master

</details>
    
**Non-Standard Port**

<details>
<summary>RDP Port Change Using Powershell</summary>


Detects RDP port configuration change using a PowerShell command such as 'Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name PortNumber -Value XXX Restart-Service termservice -force'. Threat actors can change RDP to another port to bypass protections, avoid detection based on the port, or to take full control of the system. 

- **Effort:** intermediate

</details>
    
<details>
<summary>Suspicious Network Args In Command Line</summary>


Detection on some commonly observed suspicious processes command lines using HTTP schema with port 443.

- **Effort:** intermediate

- **Changelog:**

    - 10/08/2023 - major - Added a list of suspicious processes to drastically reduce false positives.

</details>
            
**Protocol Tunneling**

<details>
<summary>Exfiltration And Tunneling Tools Execution</summary>


Execution of well known tools for data exfiltration and tunneling

- **Effort:** advanced

</details>
    
<details>
<summary>Netsh Port Forwarding</summary>


Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Ngrok Process Execution</summary>


Detects possible Ngrok execution, which can be used by attacker for RDP tunneling.

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential DNS Tunnel</summary>


Detects domain name which is longer than 62 characters. Long domain names are distinctive of DNS tunnels.

- **Effort:** advanced

- **Changelog:**

    - 22/06/2023 - minor - Filter some domains to reduce false positives.
    - 19/07/2023 - major - New regex pattern and new filters.
    - 20/01/2025 - major - Update regex pattern to improve detection, and add more filters to avoid false positives

</details>
            
<details>
<summary>SOCKS Tunneling Tool</summary>


Detects the usage of a SOCKS tunneling tool, often used by threat actors. These tools often use the socks5 commandline argument, however socks4 can sometimes be used as well. Unfortunately, socks alone (without any number) triggered too many false positives. 

- **Effort:** intermediate

- **Changelog:**

    - 20/06/2024 - minor - Added filter to reduce false positives
    - 30/01/2025 - minor - Similarity strategy was modified to have more relevant alerts.

</details>
            
<details>
<summary>SSH Port Binding</summary>


When a user uses SSH tunneling in Linux, the sshd process binds sockets to communicate with the client machine via a ssh tunnel. With SSH tunneling, the SSH server can be used as a getaway to access internal systems. The traffic will seem to be coming from the SSH server whereas it only acts as a relay for an attacker. By using this technique, an attacker can successfully bypass external firewall rules. This rule is the most basic one (compared to the other one - SSH Tunnel), however it can detect the -D option in the ssh command if the machine is the client. This rule will detect the port binding (port 6010) when X11 forwarding is used. It will detect -R (server side), -D (client side) -X (server side), -Y (server side) and -L (client side) port binding.

- **Effort:** advanced

</details>
    
<details>
<summary>SSH Reverse Socks</summary>


Detects the usage of the -R option combined with StrictHostKeyChecking, which is an indication of using SSH for reverse socks.

- **Effort:** intermediate

</details>
    
<details>
<summary>SSH Tunnel Traffic</summary>


When a user creates and uses a SSH tunnel in Linux, the sshd process opens sockets to communicate with other machines or ports. With SSH tunneling, the SSH server can be used as a getaway to access internal systems. The traffic will seem to be coming from the SSH server whereas it only acts as a relay for an attacker. By using this technique, an attacker can successfully bypass external firewall rules and gain foothold to your network, allowing him to scan,hunt and attack your internal systems. This rule includes a filter on port 22, this filter is created to avoid false positive when a user is connecting via ssh. If you do not use port 22 for your machines, please create an alert filter.

- **Effort:** advanced

</details>
    
<details>
<summary>SSH X11 Forwarding</summary>


When a user creates and uses SSH X11 Forwarding in Linux, the sshd process opens sockets to communicate with the client machine via a ssh tunnel. X11 forwarding is used to deport graphic programs on the client side.

- **Effort:** advanced

</details>
    
<details>
<summary>Socat Relaying Socket</summary>


Socat is a linux tool used to relay local socket or internal network connection, this technics is often used by attacker to bypass security equipment such as firewall

- **Effort:** advanced

- **Changelog:**

    - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 17/01/2025 - major - Significant rewrite of the rule to reduce false positives.

</details>
            
<details>
<summary>Socat Reverse Shell Detection</summary>


Socat is a linux tool used to relay or open reverse shell that is often used by attacker to bypass security equipment.

- **Effort:** elementary

- **Changelog:**

    - 14/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 17/01/2025 - major - Complete rewrite of the rule to reduce false positives.

</details>
            
<details>
<summary>Venom Multi-hop Proxy agent detection</summary>


Detects Venom Multi-hop Proxy agent.

- **Effort:** intermediate

</details>
    
**Encrypted Channel**

<details>
<summary>Corelight TLS Certificate Validation Failure</summary>


Detects a TLS session observed by a Corelight sensor whose certificate failed validation (e.g. self signed certificate, unable to get local issuer certificate). Invalid certificates are frequently associated with malware command-and-control channels and interception.

- **Effort:** master

</details>
    
## Exfiltration
**Exfiltration Over Other Network Medium**

<details>
<summary>Zscaler Internet Access Data Exfiltration</summary>


Detects request of 100000000 bytes or more from Zscaler Internet Access monitored hosts.

- **Effort:** master

- **Changelog:**

    - 16/10/2026 - major - The initial query was fixed to have the correct one.

</details>
            
**Automated Exfiltration**

<details>
<summary>AWS CloudTrail RDS Change Master Password</summary>


Detects the change of database master password. It may be a part of data exfiltration.

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail RDS Public DB Restore</summary>


Detects the recovery of a new public database instance from a snapshot. It may be a part of data exfiltration.

- **Effort:** intermediate

</details>
    
<details>
<summary>Python Exfiltration Tools</summary>


Python has some built-in modules or library that could be installed and later be used as exflitration tool by an attacker

- **Effort:** advanced

</details>
    
**Scheduled Transfer**

<details>
<summary>Gatewatcher AionIQ V103 Malicious Powershell Detect High</summary>


Detects malicious powershell by Gatewatcher V103 with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Malicious Powershell Detect Low</summary>


Detects malicious powershell by Gatewatcher V103 with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Malicious Powershell Detect Medium</summary>


Detects malicious powershell by Gatewatcher V103 with a medium severity.

- **Effort:** master

</details>
    
**Exfiltration Over C2 Channel**

<details>
<summary>Claroty xDome Network Threat Detection Alert</summary>


Claroty xDome has raised an network threat detection alert.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Exfiltration And Tunneling Tools Execution</summary>


Execution of well known tools for data exfiltration and tunneling

- **Effort:** advanced

</details>
    
<details>
<summary>Forcepoint Secure Web Gateway Compromised Websites</summary>


Forcepoint Secure Web Gateway has detected an access to an IP/domain tagged as compromised. Even if it has been blocked, it could be interesting to investigate the source asset.

- **Effort:** master

</details>
    
<details>
<summary>Forcepoint Secure Web Gateway Malicious Websites</summary>


Forcepoint Secure Web Gateway has detected an access to an IP/domain tagged as malicious. Even if it has been blocked, it could be interesting to investigate the source asset.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ Malware Alert</summary>


Forward malware information reported by Gatewatcher AionIQ  

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Gatewatcher AionIQ Network Alert High</summary>


Forward network alerts reported by Gatewatcher AionIQ with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 06/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ Network Alert Low</summary>


Forward network alerts reported by Gatewatcher AionIQ with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ Network Alert Medium</summary>


Forward network alerts reported by Gatewatcher AionIQ with a medium severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Beacon Detect High</summary>


Detects a suspicious beacon with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 07/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Beacon Detect Low</summary>


Detects a suspicious beacon with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Beacon Detect Medium</summary>


Detects a suspicious beacon with a medium severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Sigflow Alert</summary>


Detects a sigflow alert by Gatewatcher AionIQ V103.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Netsh Port Forwarding</summary>


Detects netsh commands that enable a port forwarding between to hosts. This can be used by attackers to tunnel RDP or SMB shares for example.

- **Effort:** intermediate

- **Changelog:**

    - 15/02/2024 - minor - Added filter to reduce false positives

</details>
            
<details>
<summary>Netskope Alerts Compliance</summary>


Forward alerts reported by Netskope related to compliance issues.

- **Effort:** master

- **Changelog:**

    - 29/01/2024 - minor - Rework detection pattern to focus on compliance issues
    - 28/03/2024 - minor - Rule effort was updated to master
    - 27/02/2026 - minor - Update rule type to integration

</details>
            
<details>
<summary>Remote File Copy</summary>


Detects the use of remote tools that copy files from or to remote systems

- **Effort:** master

</details>
    
<details>
<summary>SEKOIA.IO Intelligence Feed</summary>


Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.

- **Effort:** elementary

</details>
    
**Exfiltration Over Alternative Protocol**

<details>
<summary>1Password EPM Share Externally</summary>


Detects when an item from 1Password is shared externally.

- **Effort:** master

</details>
    
<details>
<summary>DNS Exfiltration and Tunneling Tools Execution</summary>


Well-known DNS exfiltration tools execution

- **Effort:** intermediate

</details>
    
<details>
<summary>Exfiltration Domain</summary>


Detects traffic toward a domain flagged as a possible exfiltration vector.

- **Effort:** master

- **Changelog:**

    - 29/02/2024 - minor - enforce detection by adding tag

</details>
            
<details>
<summary>Exfiltration Domain In Command Line</summary>


Detects commands containing a domain linked to http exfiltration.

- **Effort:** intermediate

</details>
    
<details>
<summary>Potential DNS Tunnel</summary>


Detects domain name which is longer than 62 characters. Long domain names are distinctive of DNS tunnels.

- **Effort:** advanced

- **Changelog:**

    - 22/06/2023 - minor - Filter some domains to reduce false positives.
    - 19/07/2023 - major - New regex pattern and new filters.
    - 20/01/2025 - major - Update regex pattern to improve detection, and add more filters to avoid false positives

</details>
            
<details>
<summary>Powershell UploadString Function</summary>


Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host.

- **Effort:** advanced

- **Changelog:**

    - 20/03/2025 - major - Change effort level and add filter to reduce false positives

</details>
            
<details>
<summary>TUN/TAP Driver Installation</summary>


Detects the installation of the TUN or TAP driver service, this activity could be related to data exfiltration using tunneling techniques. The TUN/TAP Windows Adapter is a network driver that enables some VPN providers to facilitate a VPN connection to their server. TUN/TAP driver is only used by specific VPNs (e.g. OpenVPN, Wireguard), not by thoses based on IKE protocols (e.g. IPsec).

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Transfer Data to Cloud Account**

<details>
<summary>AWS CloudTrail EC2 VM Export Failure</summary>


Detects attempt to export an AWS EC2 instance. A VM Export might indicate an attempt to extract information from an instance.

- **Effort:** intermediate

- **Changelog:**

    - 14/08/2025 - minor - Similarity strategy modified to group alerts by user ID and instance ID

</details>
            
<details>
<summary>Google Cloud Audit Logs Drive Ownership Transferred</summary>


Detects when Drive/Docs user files ownership is transferred. The legit use case is when a user is being removed, but this could also be abused by an attacker for exfiltration.

- **Effort:** advanced

</details>
    
**Exfiltration Over Web Service**

<details>
<summary>Exfiltration Domain</summary>


Detects traffic toward a domain flagged as a possible exfiltration vector.

- **Effort:** master

- **Changelog:**

    - 29/02/2024 - minor - enforce detection by adding tag

</details>
            
<details>
<summary>Exfiltration Domain In Command Line</summary>


Detects commands containing a domain linked to http exfiltration.

- **Effort:** intermediate

</details>
    
<details>
<summary>Outgoing Bytes Peak</summary>


Spots outgoing bytes traffic peak to detect a data exfiltration.

- **Effort:** advanced

- **Changelog:**

    - 28/05/2024 - major - On Fortinet Fortigate intakes, events other than 0000000013 are now ignored.

</details>
            
<details>
<summary>Powershell UploadString Function</summary>


Powershell's `uploadXXX` functions are a category of methods which can be used to exfiltrate data through native means on a Windows host.

- **Effort:** advanced

- **Changelog:**

    - 20/03/2025 - major - Change effort level and add filter to reduce false positives

</details>
            
<details>
<summary>Rclone Process</summary>


Detects Rclone executable or Rclone execution by using the process name, the execution through a command obfuscated or not.

- **Effort:** advanced

- **Changelog:**

    - 28/06/2023 - minor - Added filter to the rule to reduce false positives.
    - 05/08/2024 - major - Edited pattern of the rule to reduce false positives.

</details>
            
## Impact
**Data Destruction**

<details>
<summary>AWS CloudTrail ECS Cluster Deleted</summary>


Detects when an attacker is destroying an AWS ECS Cluster

- **Effort:** intermediate

</details>
    
<details>
<summary>AWS CloudTrail RDS DB Cluster/Instance Deleted</summary>


Detects when an attacker is destroying a RDS Cluster or Instance

- **Effort:** advanced

</details>
    
<details>
<summary>Backup Catalog Deleted</summary>


The rule detects when the Backup Catalog has been deleted. It means the administrators will not be able to access any backups that were created earlier to perform recoveries. This is often being done using the wbadmin.exe tool.

- **Effort:** intermediate

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Commonly Used Commands To Stop Services And Remove Backups</summary>


Detects specific commands used regularly by ransomwares to stop services or remove backups

- **Effort:** master

- **Changelog:**

    - 14/04/2025 - major - Reviewing pattern and condition to reduce false positives, adding similarity strategy and changing effort level.

</details>
            
<details>
<summary>Secure Deletion With SDelete</summary>


Detects renaming of file while deletion with SDelete tool. SDelete is a tool that permits to securely delete files by overwriting them (no recovery possible). Few threat actors are using it to delete traces of their malware.

- **Effort:** intermediate

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Data Encrypted for Impact**

<details>
<summary>Flare Events Ransom Leaks Publication</summary>


Detects a Flare document event from a ransomware and/or extortion leak site, indicating a named victim organization has had data published as proof of compromise or extortion leverage.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Ransomware Detect High</summary>


Detects when a ransomware is detected by gatewatcherV103 with a high severity.

- **Effort:** master

- **Changelog:**

    - 05/03/2026 - minor - Update rule type to integration
    - 08/10/2026 - major - Update rule to add severity.

</details>
            
<details>
<summary>Gatewatcher AionIQ V103 Ransomware Detect Low</summary>


Detects when a ransomware is detected by gatewatcherV103 with a low severity.

- **Effort:** master

</details>
    
<details>
<summary>Gatewatcher AionIQ V103 Ransomware Detect Medium</summary>


Detects when a ransomware is detected by gatewatcherV103 with a medium severity.

- **Effort:** master

</details>
    
<details>
<summary>Suncrypt Parameters</summary>


Detects SunCrypt ransomware's parameters, most of which are unique.

- **Effort:** elementary

</details>
    
<details>
<summary>Varonis Many File Created and Deleted</summary>


This rule identifies a high number of file created and deleted on the same host. It is a typical ransomware behavior.

- **Effort:** master

</details>
    
<details>
<summary>Varonis Massive Dowloads By A Single User</summary>


This rule identifies a high number of File dowloaded by a single user.

- **Effort:** master

</details>
    
**Service Stop**

<details>
<summary>Commonly Used Commands To Stop Services And Remove Backups</summary>


Detects specific commands used regularly by ransomwares to stop services or remove backups

- **Effort:** master

- **Changelog:**

    - 14/04/2025 - major - Reviewing pattern and condition to reduce false positives, adding similarity strategy and changing effort level.

</details>
            
<details>
<summary>Correlation Multi Service Disable</summary>


The rule detects a high number of services stopped or de-activated in a short period of time.

- **Effort:** master

- **Changelog:**

    - 21/08/2024 - minor - Adding a space to reduce false positives.

</details>
            
<details>
<summary>Disabled Service</summary>


Service disabling can be abused by attacker to deny security mecanisms (eg: firewall, EDR, ect) and it is also often used by cryptominer to exploit as much RAM & CPU as possible on infected host. The prerequisites are to enable monitoring of the truncate, rename and unlink syscalls using Auditbeat.

- **Effort:** advanced

</details>
    
**Inhibit System Recovery**

<details>
<summary>Commonly Used Commands To Stop Services And Remove Backups</summary>


Detects specific commands used regularly by ransomwares to stop services or remove backups

- **Effort:** master

- **Changelog:**

    - 14/04/2025 - major - Reviewing pattern and condition to reduce false positives, adding similarity strategy and changing effort level.

</details>
            
<details>
<summary>Inhibit System Recovery Deleting Backups</summary>


Detects adversaries attempts to delete backups or inhibit system recovery. This rule relies on differents known techniques using Windows events logs from Sysmon (ID 1), and PowerShell (ID 4103, 4104).

- **Effort:** intermediate

- **Changelog:**

    - 31/01/2024 - minor - Improve selection filter
    - 04/09/2025 - minor - Adding similarity strategy.

</details>
            
<details>
<summary>Stop Backup Services</summary>


Detects adversaries attempts to stop backups services or disable Windows previous files versions feature. This could be related to ransomware operators or legit administrators. This rule relies Windows command line logging and registry logging, and PowerShell (ID 4103, 4104).

- **Effort:** master

- **Changelog:**

    - 02/04/2026 - minor - Adding regex to reduce false positives.
    - 21/06/2024 - major - Update detection pattern for ECS fields/value compliance
    - 16/05/2024 - minor - add pattern to extend and improve detection

</details>
            
<details>
<summary>Suncrypt Parameters</summary>


Detects SunCrypt ransomware's parameters, most of which are unique.

- **Effort:** elementary

</details>
    
<details>
<summary>Tmutil Delete Backups</summary>


Detects when the utility tmutil is used to delete backups. The Time Machine utility is used to restore data from backups, add or remove exclusions, and compare backups.

- **Effort:** elementary

</details>
    
<details>
<summary>Tmutil Disabled</summary>


Detects when the utility tmutil is disabled. The Time Machine utility is used to restore data from backups, add or remove exclusions, and compare backups.

- **Effort:** elementary

</details>
    
<details>
<summary>Tmutil Exclude File From Backups</summary>


Detects when the utility tmutil is used to exclude paths from backups.

- **Effort:** master

</details>
    
**Network Denial of Service**

<details>
<summary>Anomaly CloudFlare DDoS</summary>


Detects anomaly on volume of DNS events from CloudFlare logs.

- **Effort:** master

</details>
    
**Endpoint Denial of Service**

<details>
<summary>Audit CVE Event</summary>


Detects events generated by Windows to indicate the exploitation of a known vulnerability.

- **Effort:** elementary

- **Changelog:**

    - 15/07/2024 - major - review filter and improve similarity

</details>
            
**System Shutdown/Reboot**

<details>
<summary>Rebooting</summary>


Detects when forcing a computer to shutdown.

- **Effort:** master

</details>
    
**Account Access Removal**

<details>
<summary>Computer Account Deleted</summary>


Detects computer account deletion.

- **Effort:** master

- **Changelog:**

    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>Google Workspace Admin Deletion</summary>


Detects when an admin is deleted or when his role is unassigned.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace User Deletion</summary>


Detects when an user is deleted.

- **Effort:** master

</details>
    
<details>
<summary>Google Workspace User Suspended</summary>


Detects when an user is suspended. An attacker can use this to remove an account used during the intrusion.

- **Effort:** master

</details>
    
<details>
<summary>Jumpcloud Account Locked</summary>


A user has been locked on Jumpcloud portal.

- **Effort:** intermediate

</details>
    
<details>
<summary>Mass User And Computer Account Deleted</summary>


Detects when mutiple user and computer accounts are deleted in a short time.

- **Effort:** master

</details>
    
<details>
<summary>Okta User Account Locked</summary>


An user has been locked in Okta.

- **Effort:** intermediate

</details>
    
<details>
<summary>Privileged AD Builtin Group Modified</summary>


Detects changes to privileged AD builtin groups in Active Directory that could indicate malicious or unexpected administrative activity. This detection rule detects changes on specific groups that are Administrators (S-1-5-*-500), Domain Admins (S-1-5-*-512), Enterprise Admins (S-1-5-*-519), Schema Admins (S-1-5-*-518), Account Operators (S-1-5-32-548) and Backup Operators (S-1-5-32-551).

- **Effort:** master

- **Changelog:**

    - 10/07/2023 - minor - Added AD groups and change to effort master.
    - 26/03/2024 - major - Rule's pattern field changed

</details>
            
<details>
<summary>User Account Deleted</summary>


Detects local user deletion

- **Effort:** master

- **Changelog:**

    - 04/04/2024 - major - Rule's pattern field changed

</details>
            
**Financial Theft**

<details>
<summary>Flare Events Ransom Leaks Publication</summary>


Detects a Flare document event from a ransomware and/or extortion leak site, indicating a named victim organization has had data published as proof of compromise or extortion leverage.

- **Effort:** master

</details>
    
<!-- endinclude:_shared_content/operations_center/detection/generated/built_in_rules_do_not_edit_manually.md -->
