## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Cloudflare HTTP requests** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Cloudflare HTTP requests on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_0ba58f32-7dba-4084-ab17-90c0be6b1f10_do_not_edit_manually.json){ .md-button }
??? abstract "Covenant Default HTTP Beaconing"
    
    Detects potential Covenant communications through the user-agent and specific urls
    
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

??? abstract "SEKOIA.IO CTI"
    
    
    
    - **Effort:** elementary

??? abstract "TrevorC2 HTTP Communication"
    
    Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 
    
    - **Effort:** elementary
