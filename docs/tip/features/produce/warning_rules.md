# Warning Rules

Warning Rules are designed to help analysts when producing intelligence in Content Proposals. They make it possible to avoid adding false positives to the CTI database and they also provide more context during an investigation.

In a Content Proposal, SEKOIA.IO’s default Warning Rules let you know if an Indicator has no relationship with another object present in the Content Proposal. They also warn you if the Kill Chain step has not been defined.

## Create a warning rule

You can create Warning Rules via the Warning Rules’ listing page. 

The `Add warning rule` button allows you to create new rules and define several elements to configure its triggering. 

To create a Warning Rule, you’ll have to: 

- Write the explicit warning message that will inform the analyst of the context around the observable
- Define what type of Observable can trigger this Warning Rule
- Define what type of relationship can trigger this Warning Rule
- Define a tag associated with the observable that will trigger this Warning Rule
- Indicate whether the tag validity date must be valid or not to trigger this Warning Rule
- Add exclusions regexes (optional): they will be applied on the pattern of the indicator and, if they match, they can prevent the warning from being created.

### Examples of Warning Rules with tag values

- This indicator contains a domain name used by a University
- This indicator contains a domain-name that is used by Google Services
- This indicator contains an IP address used by Cloudflare. It’s probably a false positive.
