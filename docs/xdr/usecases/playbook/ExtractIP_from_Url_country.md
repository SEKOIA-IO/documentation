# Extract IP from URL & Country  

This use case describes how to extract an IP address from a URL and a country.  


## Prerequisites

- A Sekoia.io XDR licence
- The user that configures the Playbook should have:
	* Be an Administrator or an Analyst of the community.
    * Have an API Key with a role that contains at least the permission "View alerts"

> To create your API Key, follow this [documentation](../../../getting_started/generate_api_keys.md).

## Playbook configuration

Here is the playbook configuration to set:

![Playbook ExtractIP](docs/assets/playbooks/library/UseCases/ExtractIP.png)

Alert created => set module & trigger configuration
Get Alert => **uuid** = `short_id` variables in **Alert created**


### Extract IP from URL

For example, we would like to extract the IP `65.74.70.888` from `url.original : /Service/Voice/SecuritySettings/111111/ManageIP/New/65.74.70.888`

Read JSON File module,  **Jsonpath** = `{{ value.split()[0].split("/ManageIP/New/")[1] }}`

```
This Jinja recipe consists in splitting the URL into 2 strings: the one preceding the string /ManageIP/New/ and the one succeeding it, which corresponds to the IP address. 
The value is set with the second string stored in the array, with the use of [1].
```

!!!note
   You can find the CODE Feature section in documentation page and in particular built-in filters existing in Jinja [here](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters). 
   (split is coming from Python)

### Extract IP from Country

For example, we would like to extract the IP `<ip>` from  `https://rdap.db.ripe.net/ip/<ip>`

Read JSON File,  **Jsonpath** = `{{ value.split()[0].split("/ip/")[1] }}`
