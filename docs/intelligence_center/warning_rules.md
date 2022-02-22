# Warning Rules

**This feature is only available with SEKOIA.IO TIP**

Warning Rules are designed to assist analysts when generating new intelligence in Content Proposals. In particular, they help avoid adding false positives to the CTI base or provide context to an investigation. 

For example, native Warning Rules indicate in a Content Proposal if an Indicator object has no relationship with another object present in the Content Proposal or if the Kill Chain step has not been defined.

In another case, the Warning Rules are based on the observables and the enrichment available via tags. For example, if in a report imported in a Content Proposal, some IP addresses observables automatically recognized belong to CloudFlare or are local addresses (RFC1918), a warning icon will indicate these elements to the analysts.

<img width="1286" alt="image" src="https://user-images.githubusercontent.com/17184467/155106305-12385153-1a9b-452c-bf32-9a962cec0671.png">

## Create a new Warning Rule

The "Add warning rule" button allows you to create new rules and offers you to define several elements that configure its triggering:
* Write the explicit warning message that will inform the analyst of the context around this observable
* Define which type of observable can trigger this Warning Rule
* Define which type of relation can trigger this Warning Rule
* Define a tag associated to the observable that will trigger this Warning Rule
* Indicate if the validity date of the tag must be valid or not to trigger this Warning Rule
* Set exclusions via Regexes (faculative)

<img width="634" alt="image" src="https://user-images.githubusercontent.com/17184467/155107814-fb187034-f15b-409d-afbe-4555db6a1d4c.png">

