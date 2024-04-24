## Related Built-in Rules

The following Sekoia.io built-in rules match the intake **Github Audit logs**. This documentation is updated automatically and is based solely on the fields used by the intake which are checked against our rules. This means that some rules will be listed but might not be relevant with the intake.

[SEKOIA.IO x Github Audit logs on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_80de6ccb-7246-40de-bcbb-bc830118c1f9_do_not_edit_manually.json){ .md-button }
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

??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary
