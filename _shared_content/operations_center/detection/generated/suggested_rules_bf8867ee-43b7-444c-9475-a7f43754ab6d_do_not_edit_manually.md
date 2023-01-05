## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Vectra Cognito Detect** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Vectra Cognito Detect on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_bf8867ee-43b7-444c-9475-a7f43754ab6d_do_not_edit_manually.json){ .md-button }
??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner)
    
    - **Effort:** intermediate

??? abstract "Intune Policy Change"
    
    Detects edits, deletions or creations made to an organization Intune policies.
    
    - **Effort:** intermediate

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "Suspicious TOR Gateway"
    
    Detects suspicious TOR gateways. Gateways are often used by the victim to pay and decrypt the encrypted files without installing TOR. Tor intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** advanced

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced

??? abstract "Vectra General Threat Detection"
    
    Vectra Cognito detected a potential threat. This is a very generic rule to raise as much alerts as possible from Vectra detections however RECONNAISSANCE and INFO categories have been removed to avoid spamming.
    
    - **Effort:** master
