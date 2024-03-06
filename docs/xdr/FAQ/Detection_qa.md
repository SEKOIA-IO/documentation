## Documentation

**A [Sekoia.io](http://Sekoia.io) rule was changed, where could I get the information of any change in the rules catalog?**
    
We created a rules changelog page where you can get this information: https://docs.sekoia.io/xdr/features/detect/rules_changelog/. For the new rules added to the catalog, you can active a notification in our platform directly.

**I want to map the EventIDs with the rules from [Sekoia.io](http://Sekoia.io) to know which ones I need to collect or not, where can I find this information?**
    
This information can be found here: https://docs.sekoia.io/xdr/features/detect/built_in_detection_rules_eventids/. Please read the page carefully, note that the page is generated **automatically**.

**In the documentation I can see rules mapped to intakes which make no sense, and sometimes rules are not mapped, could you fix that please?**
    
These pages are generated automatically from the fields present in the rules and the fields present in the intakes. 

Furthermore there’s still some work in progress to include rules with Sekoia tags and Correlation rules.

## Detection strategy

**Which Detection perimeter?**
    
In 2024 the ideal detection perimeter should monitor at least the following areas: 
- Endpoint for workstations and servers
- Network outbound/inbound connections
- Cloud office applications
- Identity management

**Have you created rules for the last CVE-XXXXXX? Why not?**
    
We don’t create rules for CVEs because they often depends on the customer’s environment (so it’s not really generic) and it would be highly time consuming, especially since they are not the most useful rules in our opinion. Most of the time when an attacker exploits a vulnerability, he would still need to perform the actions he usually does: lateral movement, persistence, etc.
    
For that reason, we would rather focus instead of the common TTPs to detect actions perform by attackers whether there’s a vulnerability exploited or not.
    
That said, if a new vulnerability like ZeroLogon (allows directly from user to domain admin in an AD environment) is published, we will look if there’s a way to detect it. In that case, it directly impacts most of our customers and also allows the attacker to bypass most of the commonly used TTPs.
    
**Can you change the similarity strategy for the rule X? (grouping of events into Alerts)**
    
We always try to find the best similarity strategy that enables efficiency and productivity for the SOC analysts handling alerts.

That being said, not all SOC teams have the same workflow and needs on how to group events into Alerts. So if the existing similarity strategy is not well suited for your context, we recommend you to duplicate the detection rule, via copy/pasting the detection pattern and the different rule parameters, and applying the similarity strategy you like.
    
**Could you create a rule for "this detection use case"?**
    
Thank you for the suggestion. Please note that you can create your own rules in Sekoia.io.

That said if you want the rule to be managed by Sekoia.io, we will ask our detection engineering team which will come back to you in two weeks to assess whether they will perform the rule or not, and when will they deliver the rule.
    
**Why did this phishing email go undetected by your cybersecurity product?**
    
It's important to understand that our product is not primarily an anti-phishing tool. While we do incorporate IOCs related to phishing during our investigations and from reports, our main focus is not on phishing detection but rather on what's happening afterwards. Therefore, our database is not exhaustive in terms of phishing threats. We recommend using a dedicated anti-phishing tool in conjunction with our product for comprehensive protection against phishing attempts.
    
**Why doesn't the Sekoia Intelligence feed rule detect all the scanner IPs that appear on my firewalls? (Why my firewall linked to internet doesn't raise any alerts)**
    
The Sekoia Intelligence Feed rule is designed to identify threats based on a specific set of Indicators of Compromise (IOCs) collected by Sekoia's Threat and Detection Research team . Our approach is to focus on the most significant threats, and as such, we have chosen not to classify scanner IPs as IOCs. Indeed, we consider these scanning activities as reconnaissance, which do not inherently pose a direct threat on their own and risk to generate a lot of alert noise. However, information about these scanner IPs can be valuable in certain contexts, such as correlation with other alerts or during threat hunting activities.
    
To facilitate this, we categorize scanner IPs as observables and tag them with scanner rather than treating them as IOCs. This approach allows you to search for these scanner IPs on the events page easily. Additionally, we offer two master rules, named `Internet Scanner`and `Internet Scanner Target`, which utilize these tags. 

**Be careful with those rules tough**, as they are master rules, they might raise a lot of alerts.

## How [Sekoia.io](http://Sekoia.io) builds rules / does detection engineering

**What is your processus for creating rules? Are they tested?**
    
Please check our blogpost on that matter: https://blog.sekoia.io/xdr-detection-rules-at-scale/
