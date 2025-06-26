# Sekoia.io Detection Strategy

## A Sekoia.io rule was changed, how can I be notified when there is any change in the Rules Catalog?

You can easily stay informed about changes in the Rules Catalog. We provide a [dedicated Rules changelog page](https://docs.sekoia.io/xdr/features/detect/rules_changelog/) where you can find details about what changes were made to existing rules.

For new rules, you can directly enable notifications within the Sekoia.io platform to receive alerts. Go to the Notifications tool, create a new notification and select `A new rule is added to the Rules Catalog by Sekoia.io` as the trigger. 


## I want to map the EventIDs with the rules from Sekoia.io to know which ones I need to collect or not, where can I find this information?

Easily find the mapping between EventIDs, rules, and EventProviders in our comprehensive guide: [Built-in detection rules, EventIDs and EventProviders relations](https://docs.sekoia.io/xdr/features/detect/built_in_detection_rules_eventids/). This page provides a clear overview of which EventIDs are associated with specific rules and their corresponding sources.

Please note that this information is automatically generated, so double-check for any discrepancies.
    
## In the documentation, I see incorrect rule-to-intake mappings, and some rules are missing. Could you fix this please?

We understand your concerns. The rule-to-intake mappings and rule listings you see in the documentation are automatically generated based on the fields present both in the rules and the intakes. This means any inconsistencies in this data can be reflected in the documentation.

We are actively working on improving the documentation by:

- Adding support for **Sekoia tags**: This will allow for more accurate rule categorization and mapping.
- Including **Correlation rules**: These rules will be displayed alongside other detection rules for a complete picture.

## What is the focus of your detection perimeter?
    
In 2024, the ideal detection perimeter should monitor at least the following areas: 

- Endpoint for workstations and servers
- Network outbound/inbound connections
- Cloud office applications
- Identity management

## Have you created rules for specific vulnerabilities (CVEs)? Why not? 

We prioritize detection based on common Tactics, Techniques, and Procedures (TTPs) employed by attackers, rather than focusing solely on individual vulnerabilities (CVEs). Here's why:

- CVEs often depend heavily on a customer's specific environment, making detection rules based solely on them less broadly applicable.
- Continuously creating and maintaining rules for every new CVE is resource-intensive and inefficient.
- Attackers, regardless of the specific vulnerability exploited, often exhibit similar behaviors during lateral movement, persistence, and other stages of an attack. By focusing on these common TTPs, we can achieve broader and more efficient threat detection.

**Exceptions for High-Impact Vulnerabilities**

We do make exceptions for highly impactful vulnerabilities that pose a significant threat and potentially bypass standard security controls. In such cases, we prioritize developing specific detection rules to address risks associated with these vulnerabilities. For instance, if a vulnerability like [ZeroLogon](https://app.sekoia.io/intelligence/objects/vulnerability--f0cce579-8483-4839-9da2-14bb266928a8) is published, we will look if there’s a way to detect it since it directly impacts most of our customers. 


## Can you change the similarity strategy for a rule? (Grouping events into alerts)

While we strive to define optimal similarity strategies that promote efficiency and productivity for security analysts, we recognize that different SOCs have unique workflows and needs for grouping events into alerts.

If the existing similarity strategy doesn't align perfectly with your context, you can create a **custom rule**: 

- Select the rule you want to edit 
- Copy the detection pattern and the different rule parameters 
- Create a new custom rule using the previously copied settings 

This lets you create a new rule where you can freely adjust the similarity strategy to match your specific requirements.

Please note that we have received a lot of requests for improvements concerning this part of the product and we will be working on enhancing this feature in the coming year. 

## Could you create a rule for a specific detection use case?

We appreciate all your suggestions! Sekoia.io empowers you to create your own custom rules to address your unique detection needs.

If you want the rule to be managed by Sekoia.io, you can submit a request to the support. The Threat Detection and Research team will then have around two weeks to evaluate your request and provide a timeline for potential rule development and delivery. 


## Why did this phishing email go undetected by Sekoia.io?

It's important to understand that our product is not primarily an anti-phishing tool. While we do incorporate IOCs related to phishing during our investigations and from reports, our main focus is not on phishing detection but rather on what's happening afterwards. 

As a result, our database of known phishing threats is not exhaustive.

For comprehensive protection against phishing attempts, we strongly recommend using a dedicated anti-phishing tool alongside Sekoia.io.

## Why doesn't the Sekoia Intelligence Feed rule detect all the scanner IPs showing up on my firewall? (Why my firewall linked to internet doesn't raise any alerts)

The Sekoia Intelligence Feed rule focuses on identifying high-risk threats based on specific IOCs compiled by our Threat and Detection Research team. Since scanner activity is considered reconnaissance and not inherently indicative of a direct threat, we have opted not to classify scanner IPs as IOCs to avoid generating excessive alerts (often referred to as "alert noise").

However, we recognize the potential value of scanner IPs in specific contexts, such as correlation with other alerts or threat hunting activities. Therefore, we:

- Categorize scanner IPs as observables and tags them with "scanner" instead of treating them as IOCs. This allows you to easily search for them on the events page.
- Offer two master rules: `Internet Scanner` and `Internet Scanner Target`, which leverage these tags.

!!! note
    Be careful with these rules as they are master rules and might raise a significant number of alerts. 

## What is your processus for creating detection rules? Are they tested?
    
Sekoia.io follows a specific process to build detection rules. This process is designed to ensure that the rules are high quality and do not cause false positives.

Here are the main steps involved in crafting Sekoia.io's verified detection rules:

- **Field normalization:** This is the first step in the process, and it involves converting all of the logs from different sources into a common format (ECS). This is important because it allows Sekoia.io to create rules that can be applied to all of the logs in its system, regardless of the source.
- **Rule creation and review**: Once the logs have been normalized, Sekoia.io analysts create detection rules using Sigma. These rules are then reviewed by other analysts to ensure that they are correct and effective.
- **Testing**: Once a rule has been reviewed, it is tested using test samples. These test samples are events (logs) that have already been classified as malicious or benign. The rule is considered to be successful if it correctly identifies the malicious events and does not generate any false positives on the benign events.
- **Staging**: Once a rule has been successfully tested, it is moved to a staging environment. This is a production-like environment where the rule can be monitored for false positives before it is deployed to production.
- **Approval**: If a rule performs well in staging, it is then approved for production deployment.

## Detection Engineering references
For more insights on how we create rules and how we test them, check our blogposts on that matter:
* [XDR detection engineering at scale: crafting detection rules for SecOps efficiency](https://blog.sekoia.io/xdr-detection-rules-at-scale/).
* [Detection engineering at scale: one step closer (part one)](https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-one/).
* [Detection engineering at scale: one step closer (part two)](https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-two/).
* [Detection engineering at scale: one step closer (part three)](https://blog.sekoia.io/detection-engineering-at-scale-one-step-closer-part-three/).

A [full PDF version](/assets/detection_engineering_at_scale_one_step_closer.pdf) of our three parts blogpost above is also available.
