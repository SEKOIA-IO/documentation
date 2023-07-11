## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Salesforce Events** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Salesforce Events on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_d2725f97-0c7b-4942-a847-983f38efb8ff_do_not_edit_manually.json){ .md-button }
??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "Potential Azure AD Phishing Page (Adversary-in-the-Middle)"
    
    Detects an HTTP request to an URL typical of the Azure AD authentication flow, but towards a domain that is not one the legitimate Microsoft domains used for Azure AD authentication.
    
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

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary
