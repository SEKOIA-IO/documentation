## Related Built-in Rules

Benefit from SEKOIA.IO built-in rules and upgrade **McAfee Web Gateway / Skyhigh Secure Web Gateway** with the following detection capabilities out-of-the-box.

[SEKOIA.IO x McAfee Web Gateway / Skyhigh Secure Web Gateway on ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FSEKOIA-IO%2Fdocumentation%2Fmain%2F_shared_content%2Foperations_center%2Fdetection%2Fgenerated%2Fattack_40bac399-2d8e-40e3-af3b-f73a622c9687_do_not_edit_manually.json){ .md-button }
??? abstract "AdFind Usage"
    
    Detects the usage of the AdFind tool. AdFind.exe is a free tool that extracts information from Active Directory.  Wizard Spider (Bazar, TrickBot, Ryuk), FIN6 and MAZE operators have used AdFind.exe to collect information about Active Directory organizational units and trust objects 
    
    - **Effort:** elementary

??? abstract "Adexplorer Usage"
    
    Detects the usage of Adexplorer, a legitimate tool from the Sysinternals suite that could be abused by attackers as it can saves snapshots of the Active Directory Database.
    
    - **Effort:** advanced

??? abstract "Bazar Loader DGA (Domain Generation Algorithm)"
    
    Detects Bazar Loader domains based on the Bazar Loader DGA
    
    - **Effort:** elementary

??? abstract "Bloodhound and Sharphound Tools Usage"
    
    Detects default process names and default command line parameters used by Bloodhound and Sharphound tools.
    
    - **Effort:** intermediate

??? abstract "Burp Suite Tool Detected"
    
    Burp Suite is a cybersecurity tool. When used as a proxy service, its purpose is to intercept packets and modify them to send them to the server. Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities (vulnerabilities scanner)
    
    - **Effort:** intermediate

??? abstract "CMSTP Execution"
    
    Detects various indicators of Microsoft Connection Manager Profile Installer execution
    
    - **Effort:** intermediate

??? abstract "CVE-2018-11776 Apache Struts2"
    
    Apache Struts versions 2.3 to 2.3.34 and 2.5 to 2.5.16 suffer from possible Remote Code Execution when alwaysSelectFullNamespace is true (either by user or a plugin like Convention Plugin) and then: results are used with no namespace and in same time, its upper package have no or wildcard namespace and similar to results, same possibility when using url tag which doesn't have value and action set and in same time, its upper package have no or wildcard namespace. 
    
    - **Effort:** intermediate

??? abstract "CVE-2018-13379 Fortinet Exploit"
    
    Detects the successful exploitation of the Fortinet FortiOS CVE-2018-13379. This CVE is one of the most exploited CVEs since 2018. It is exploited by APT threat actors as well as cybercriminals. The exploitation of this CVE lead an unauthenticated user to get full access to FortiOS system file through SSL VPN via specially crafted HTTP resource requests. The exploit read /dev/cmdb/sslvpn_websession file, that contains login and passwords in (clear/text). An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects FortiOS 5.6.3 to 5.6.7 and FortiOS 6.0.0 to 6.0.4.
    
    - **Effort:** advanced

??? abstract "CVE-2019-0604 SharePoint"
    
    Detects the exploitation of the SharePoint vulnerability (CVE-2019-0604)
    
    - **Effort:** advanced

??? abstract "CVE-2019-11510 Pulse Secure Exploit"
    
    Detects the successful exploitation of the Pulse Secure vulnerability CVE-2019-11510. This CVE is one of the most exploited CVEs since 2019. It is exploited by diverse threat actors, leading sometimes in ransomware deployement. Among these groups: Maze, Conti, Egregor, DoppelPaymer, NetWalker and REvil. But also APT actors such as APT29. The exploitation of this CVE allows a remote, unauthenticated attacker to compromise a vulnerable VPN server. The attacker may be able to gain access to all active users and their plain-text credentials. It may also be possible for the attacker to execute arbitrary commands on each VPN client as it successfully connects to the VPN server. The exploit reads /etc/passwd file to get access to login and passwords in (clear/text). 	 An HTTP response status code = 200, means the file was successfully accessed. This vulnerability affects 8.1R15.1, 8.2 before 8.2R12.1, 8.3 before 8.3R7.1, and 9.0 before 9.0R3.4 products.
    
    - **Effort:** elementary

??? abstract "CVE-2019-19781 Citrix Netscaler"
    
    Detects CVE-2019-19781 exploitation attempt against Citrix Netscaler, Application Delivery Controller and Citrix Gateway Attack
    
    - **Effort:** elementary

??? abstract "CVE-2019-2725 Oracle Weblogic Exploit"
    
    Detects the successful exploitation of a deserialization vulnerability in Oracle Weblogic Server, CVE-2019-2725. This vulnerability affects versions 10.X and 12.1.3 of WebLogic that have the components wls9_async_response.war and wls-wsat.war enabled. It is a remote code execution which can be exploited without authentication via HTTP. An HTTP response status code = 202, means the target is vulnerable, the analyst then has to look in depth to check if a webshell has been uploaded or something else has been done.
    
    - **Effort:** elementary

??? abstract "CVE-2020-0688 Microsoft Exchange Server Exploit"
    
    Detects the exploitation of CVE-2020-0688. The POC exploit a .NET serialization vulnerability in the Exchange Control Panel (ECP) web page. The vulnerability is due to Microsoft Exchange Server not randomizing the keys on a per-installation basis resulting in them using the same validationKey and decryptionKey values. With knowledge of these, values an attacker can craft a special viewstate to use an OS command to be executed by NT_AUTHORITY\SYSTEM using .NET deserialization. To exploit this vulnerability, an attacker needs to leverage the credentials of an account it had already compromised to authenticate to OWA. 
    
    - **Effort:** elementary

??? abstract "CVE-2020-1147 SharePoint"
    
    Detection of SharePoint vulnerability CVE-2020-1147
    
    - **Effort:** advanced

??? abstract "CVE-2020-14882 Oracle WebLogic Server"
    
    Detects the exploitation of the Oracle WebLogic Server vulnerability (CVE-2020-16952)
    
    - **Effort:** advanced

??? abstract "CVE-2020-17530 Apache Struts RCE"
    
    Detects the exploitation of the Apache Struts vulnerability (CVE-2020-17530).
    
    - **Effort:** intermediate

??? abstract "CVE-2020-5902 F5 BIG-IP Exploitation Attempts"
    
    Detects the exploitation attempt of the vulnerability found in F5 BIG-IP and described in CVE-2020-5902
    
    - **Effort:** elementary

??? abstract "CVE-2021-20021 SonicWall Unauthenticated Administrator Access"
    
    Detects the exploitation of SonicWall Unauthenticated Admin Access.
    
    - **Effort:** advanced

??? abstract "CVE-2021-20023 SonicWall Arbitrary File Read"
    
    Detects Arbitrary File Read, which can be used with other vulnerabilities as a mean to obtain outputs generated by attackers, or sensitive data.
    
    - **Effort:** advanced

??? abstract "CVE-2021-21972 VMware vCenter"
    
    The vSphere Client (HTML5) contains a remote code execution vulnerability in a vCenter Server plugin. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.x before 7.0 U1c, 6.7 before 6.7 U3l and 6.5 before 6.5 U3n) and VMware Cloud Foundation (4.x before 4.2 and 3.x before 3.10.1.2). POST request on the following PATH "/ui/vropspluginui/rest/services/uploadova". If in response body (500) the words it has "uploadFile", that means the vCenter is available to accept files via POST without any restrictions.
    
    - **Effort:** intermediate

??? abstract "CVE-2021-21985 VMware vCenter"
    
    The vSphere Client (HTML5) contains a remote code execution vulnerability due to lack of input validation in the Virtual SAN Health Check plug-in which is enabled by default in vCenter Server. A malicious actor with network access to port 443 may exploit this issue to execute commands with unrestricted privileges on the underlying operating system that hosts vCenter Server. This affects VMware vCenter Server (7.0 before 7.0 U2b, 6.7 before 6.7 U3n and 6.5 before 6.5 U3p) and VMware Cloud Foundation (4.x before 4.2.1 and 3.x before 3.10.2.1).
    
    - **Effort:** intermediate

??? abstract "CVE-2021-22123 Fortinet FortiWeb OS Command Injection"
    
    Detects Fortinet FortiWeb OS Command Injection (August 2021) vulnerability exploitation attempt. A remote, authenticated attacker can execute arbitrary commands on the system hosting a vulnerable FortiWeb WAF by sending a POST request with the command in the name field. At the time of writing this rule, it would appear that the request would respond in code 500 for a successful exploitation attempt. 
    
    - **Effort:** advanced

??? abstract "CVE-2021-22893 Pulse Connect Secure RCE Vulnerability"
    
    Detects potential exploitation of the authentication by-pass vulnerability that can allow an unauthenticated user to perform remote arbitrary file execution on the Pulse Connect Secure gateway. It is highly recommended to apply the Pulse Secure mitigations and seach for indicators of compromise on affected servers if you are in doubt over the integrity of your Pulse Connect Secure product.
    
    - **Effort:** intermediate

??? abstract "CVE-2021-26855 Exchange SSRF"
    
    Detects the exploitation of ProyxLogon vulerability on Exchange servers.
    
    - **Effort:** advanced

??? abstract "CVE-2021-34473 ProxyShell Attempt"
    
    Detects CVE-2021-34473 ProxyShell attempt against Microsoft Exchange Server, Remote Code Execution Vulnerability.
    
    - **Effort:** advanced

??? abstract "CVE-2021-41773 Apache 2.4.49 Path Traversal"
    
    Detects successful exploitation of the Apache Path Traversal CVE-2021-41773.
    
    - **Effort:** advanced

??? abstract "CVE-2021-43798 Grafana Directory Traversal"
    
    Grafana version 8.x has a 0day arbitrary file read (with no fix yet) based on a directory traversal vulnerability
    
    - **Effort:** intermediate

??? abstract "Certificate Authority Modification"
    
    Installation of new certificate(s) in the Certificate Authority can be used to trick user when spoofing website or to add trusted destinations.
    
    - **Effort:** master

??? abstract "Cobalt Strike Default Beacons Names"
    
    Detects the default names of Cobalt Strike beacons / payloads.
    
    - **Effort:** elementary

??? abstract "Cobalt Strike HTTP Default GET beaconing"
    
    Detects GET HTTP queries from known Cobalt Strike beacons (source code 4.3)
    
    - **Effort:** advanced

??? abstract "Cobalt Strike HTTP Default POST Beaconing"
    
    Detects POST HTTP queries from known Cobalt Strike beacons (source code 4.3)
    
    - **Effort:** advanced

??? abstract "Download Files From Suspicious TLDs"
    
    Detects download of certain file types from hosts in suspicious TLDs
    
    - **Effort:** master

??? abstract "Exchange Server Creating Unusual Files"
    
    Look for Microsoft Exchange Server’s Unified Messaging service creating non-standard content on disk, which could indicate web shells or other malicious content, suggesting exploitation of CVE-2021-26858 vulnerability
    
    - **Effort:** intermediate

??? abstract "Exfiltration And Tunneling Tools Execution"
    
    Execution of well known tools for data exfiltration and tunneling
    
    - **Effort:** advanced

??? abstract "FoggyWeb HTTP Default GET/POST Requests"
    
    Detects GET or POST request pattern observed within the first FoggyWeb campaign detected by Microsoft.
    
    - **Effort:** advanced

??? abstract "GitLab CVE-2021-22205"
    
    Detects GitLab vulnerability CVE-2021-22205 exploitation success. It allows an attacker to do some remote code execution with user git. The HTTP return code 422 indicates a successfull exploitation.
    
    - **Effort:** intermediate

??? abstract "Kernel Module Alteration"
    
    Kernel module installation can be used to configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems.
    
    - **Effort:** advanced

??? abstract "Koadic MSHTML Command"
    
    Detects Koadic payload using MSHTML module
    
    - **Effort:** intermediate

??? abstract "LokiBot Default C2 URL"
    
    Detects default C2 URL for trojan LokiBot
    
    - **Effort:** elementary

??? abstract "Network Scanning and Discovery"
    
    Tools and command lines used for network discovery from current system
    
    - **Effort:** advanced

??? abstract "Network Sniffing"
    
    List of common tools used for network packages sniffing
    
    - **Effort:** advanced

??? abstract "Network Sniffing Windows"
    
    Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.
    
    - **Effort:** intermediate

??? abstract "Nimbo-C2 User Agent"
    
    Nimbo-C2 Uses an unusual User-Agent format in its implants.
    
    - **Effort:** intermediate

??? abstract "PasswordDump SecurityXploded Tool"
    
    Detects the execution of the PasswordDump SecurityXploded Tool
    
    - **Effort:** elementary

??? abstract "Possible Malicious File Double Extension"
    
    Detects request to potential malicious file with double extension
    
    - **Effort:** elementary

??? abstract "Potential Bazar Loader User-Agents"
    
    Detects potential Bazar loader communications through the user-agent
    
    - **Effort:** elementary

??? abstract "Potential Lemon Duck User-Agent"
    
    Detects LemonDuck user agent. The format used two sets of alphabetical characters separated by dashes, for example "User-Agent: Lemon-Duck-[A-Z]-[A-Z]".
    
    - **Effort:** elementary

??? abstract "Potential LokiBot User-Agent"
    
    Detects potential LokiBot communications through the user-agent
    
    - **Effort:** intermediate

??? abstract "Privilege Escalation Awesome Scripts (PEAS)"
    
    Detect PEAS privileges escalation scripts and binaries
    
    - **Effort:** elementary

??? abstract "ProxyShell Exchange Suspicious Paths"
    
    Detects suspicious calls to Exchange resources, in locations related to webshells observed in campaigns using this vulnerability.
    
    - **Effort:** elementary

??? abstract "PsExec Process"
    
    Detects PsExec execution, command line which contains pstools or installation of the PsExec service. PsExec is a SysInternals which can be used to execute a program on another computer. The tool is as much used by attackers as by administrators. 
    
    - **Effort:** advanced

??? abstract "RDP Session Discovery"
    
    Detects use of RDP session discovery via qwinsta or quser. Used by some threat actors to know if someone is working via RDP on a server.
    
    - **Effort:** advanced

??? abstract "RTLO Character"
    
    Detects RTLO (Right-To-Left character) in file and process names.
    
    - **Effort:** elementary

??? abstract "RYUK Ransomeware - martinstevens Username"
    
    Detects user name "martinstevens". Wizard Spider is used to add the user name "martinstevens" to the AD of its victims. It was observed in several campaigns; in 2019 and 2020.
    
    - **Effort:** elementary

??? abstract "Raccoon Stealer 2.0 Legitimate Third-Party DLL Download URL"
    
    Detects Raccoon Stealer 2.0 malware downloading legitimate third-party DLLs from its C2 server. These legitimate DLLs are used by the information stealer to collect data on the compromised hosts.
    
    - **Effort:** elementary

??? abstract "SEKOIA.IO Intelligence Feed"
    
    Detect threats based on indicators of compromise (IOCs) collected by SEKOIA's Threat and Detection Research team.
    
    - **Effort:** elementary

??? abstract "SharePoint Authenticated SSRF"
    
    Detects succesful SSRF from an authenticated SharePoint user.
    
    - **Effort:** elementary

??? abstract "SolarWinds Suspicious File Creation"
    
    Detects SolarWinds process creating a file with a suspicious extension. The process solarwinds.businesslayerhost.exe created an unexpected file whose extension is ".exe", ".ps1", ".jpg", ".png" or ".dll".
    
    - **Effort:** intermediate

??? abstract "Suspicious Double Extension"
    
    Detects suspicious use of an .exe extension after a non-executable file extension like .pdf.exe, a set of spaces or underlines to cloak the executable file in spearphishing campaigns
    
    - **Effort:** elementary

??? abstract "Suspicious Download Links From Legitimate Services"
    
    Detects users clicking on Google docs links to download suspicious files. This technique was used a lot by Bazar Loader in the past.
    
    - **Effort:** elementary

??? abstract "Suspicious URI Used In A Lazarus Campaign"
    
    Detects suspicious requests to a specific URI, usually on an .asp page. The website is often compromised.
    
    - **Effort:** intermediate

??? abstract "System Info Discovery"
    
    System info discovery, attempt to detects basic command use to fingerprint a host
    
    - **Effort:** master

??? abstract "Telegram Bot API Request"
    
    Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind
    
    - **Effort:** advanced

??? abstract "WCE wceaux.dll Creation"
    
    Detects wceaux.dll creation while Windows Credentials Editor (WCE) is executed.
    
    - **Effort:** intermediate
