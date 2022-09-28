## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **Palo Alto - Next Generation Firewall** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x Palo Alto - Next Generation Firewall on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_903ec1b8-f206-4ba5-8563-db21da09cafd_do_not_edit_manually.json){ .md-button }
??? abstract "Fortinet Firewall Login In Failure"
    
    Detects failed login attemps on firewall administration rule. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master

??? abstract "Fortinet Firewall Successful External Login"
    
    Detects succesfull access to administration console of firewall from another IP address than 127.0.0.1. Prerequisites, check that the firewall logs format corresponds to the rule
    
    - **Effort:** master

??? abstract "Internet Scanner"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP.
    
    - **Effort:** master

??? abstract "Internet Scanner Target"
    
    Detects known scanner IP addresses. Alert is only raised when the scan hits an opened port, on TCP or UDP and group by target address.
    
    - **Effort:** master

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO CTI"
    
    
    
    - **Effort:** elementary

??? abstract "TOR Usage"
    
    Detects TOR usage, based on the IP address and the destination port (filtered on NTP). TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master
