## Suggested Built-in Rules

This integration enables the following built-in detection rules. Use the Rules Catalog to customize and adapt these to your security posture.


??? tip "Bazar Loader DGA (Domain Generation Algorithm)"
    
    Detects Bazar Loader domains based on the Bazar Loader DGA
    
    - **Effort:** elementary

??? tip "Covenant Default HTTP Beaconing"
    
    Detects potential Covenant communications through the user-agent and specific urls
    
    - **Effort:** intermediate

??? tip "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? tip "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? tip "Potential LokiBot User-Agent"
    
    Detects potential LokiBot communications through the user-agent
    
    - **Effort:** intermediate

??? tip "Sliver DNS Beaconing"
    
    Detects suspicious DNS queries known from Sliver beaconing 
    
    - **Effort:** intermediate

??? warning "TOR Usage"
    
    Detects TOR usage, based on the IP address and the destination port (filtered on NTP). TOR is short for The Onion Router, and it gets its name from how it works. TOR intercepts the network traffic from one or more apps on user’s computer, usually the user web browser, and shuffles it through a number of randomly-chosen computers before passing it on to its destination. This disguises user location, and makes it harder for servers to pick him/her out on repeat visits, or to tie together separate visits to different sites, this making tracking and surveillance more difficult. Before a network packet starts its journey, user’s computer chooses a random list of relays and repeatedly encrypts the data in multiple layers, like an onion. Each relay knows only enough to strip off the outermost layer of encryption, before passing what’s left on to the next relay in the list.
    
    - **Effort:** master

??? tip "TrevorC2 HTTP Communication"
    
    Detects TrevorC2 HTTP communication based on the HTTP request URI and the user-agent. 
    
    - **Effort:** elementary

??? tip "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
