# IOC Collections

Indicators Of Compromise (IOCs) are commonly shared between CERT and SOC teams and by Cyber Threat Intelligence providers. They are an important part of detection.

While IOCs produced by Sekoia’s own Threat & Detection Research team are directly available inside the application, IOC Collections allow you to import indicators from other sources.

You can then easily see telemetry on these collections and use them inside detection rules.

## Create an IOC Collection

You can open the IOC Collection creation modal by clicking on `+ Collection`. You will then have to fill out the form:

- Define the name of the collection
- (Optional) Add a description to the collection
- Choose if you want to automatically add IOCs from this collection into your detection by creating a dedicated detection rule. Note that you will be able to manually create a detection rule for this collection later if you want

![ioc_creation](/assets/operation_center/IOCscollections/ioc-create_updated.png){: style="max-width:100%"}

!!! Note
    Inside a MSSP community, you also have to choose the community in which the IOC Collection should be created. If you choose “All communities”, the collection will be readable by all subcommunities.

## Import IOCs inside a collection

You can add indicators to a collection by clicking on the `Import` button. You will then have to choose between File Import and Text Import.

Each indicator inside the collection can have the following properties:

| Field                 | Description                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| Observable <a id="observable-field"></a>           | This is the actual IOC value (can be an IP address (IPv4 or IPv6), a MAC address,  a domain name, a URL, a file hash (MD5, SHA-1, SHA-256, SHA-512) or an email address) |
| Related Threats       | A list of threats that are related to this indicator. These threats have to exist inside the Intelligence Center        |
| Valid From            | The date from which this indicator should be considered valid                                                       |
| Valid Until           | The date from which this indicator should no longer be considered valid                                              |
| Kill Chain Phases     | Steps of the attack this indicator belongs to                                                                        |
| Description           | Any text that would add additional context. It is limited to **500 characters**                                      |


!!! warning
	If you select the kill chain phase '**Command and Control**' when importing IP addresses in an IOC collection, our detection engines will only look into `destination.ip`. This is meant to reduce false positives, such as network scans.

### Limitations 

We allow a maximum **limit of 500,000 IOCs** entries that can be imported. This limit applies to the total IOC imports across all collections in a community. 

### Text Import

Text Import can be used when you want to import a list of IOCs (typically one IOC per line) that all have the same properties.

Add all your IOCs in the text field, then click on `Next`. 

!!! note
    You can only use IOC types listed into the [Observable description](#observable-field). 

![collectiontypes](/assets/operation_center/IOCscollections/ioc-types.png){: style="max-width:100%"}

On the next screen, select the additional properties to add intelligence context to your indicators. All fields are optional here:

![collectionform](/assets/operation_center/IOCscollections/ioc_import.png){: style="max-width:100%"}

Finally, click on `Import` to add indicators to your collection. Depending on the number of indicators your are importing at once, this can take some time.

### File Import

IOCs are commonly shared in tabular files where each indicator has its own row and additional context appears in different columns. File Import can be used with CSV, XLS and XLSX files to directly import indicators from these files.

!!! note
    You can only use IOC types listed into the [Observable description](#observable-field).

1. Upload the file you would like to process
2. The application will display the first 10 lines of the file, which a suggestion on how each column should be mapped to an indicator’s properties
    ![collectiontable](/assets/operation_center/IOCscollections/ioc_table.png){: style="max-width:100%"}

3. Make sure the suggestions are correct and adjust if necessary by clicking on the chevron next to the column mapping. Use special value “Ignore” if the column should not be mapped to a property. In that case, the content of the column will be discarded.
4. Click on `Next`. If some indicator properties are not mapped by any column, you will have the opportunity to define values that will apply to all indicators.
    ![collectionthreats](/assets/operation_center/IOCscollections/ioc_relatedthreats.png){: style="max-width:100%"}

5. Finally, click on `Import` and wait for indicators to be created. Depending on the numbers of indicators in your file, this can take some time.

## Indicator Actions

When inside a collection, buttons are available at the end of each line to update or revoke an indicator. If you are looking for a specific indicator within the collection, you can use the search bar above the table.

### Edit an indicator

1. Click on the `Edit` button
2. Modify the properties you would like to change inside the modal
3. Click on `Save`

!!! Warning 
    The observable value cannot be changed.

### Revoke an indicator

If you realize that an indicator is bad and produces false positive detections, you can use the revoke button to remove it from detection.

#### How to Request the Revocation of an IoC

- Go to the **Intelligence** section in the left menu.
- Search for and select the object you believe is a false positive.
- Before reporting a false positive, make sure to carefully review the details associated with the object, including:
    - The **pattern**
    - The **source**
    - The **threat context**
    - Linked **observables**
- Click the **Request revocation** button available at the top right.

!!! warning
    Revoking an indicator cannot be undone.

## Export an IOC Collection with a custom format

You can retrieve an IOC Collection through the collections API and customize each output line for an external tool, such as a firewall or proxy. This changes the response for that request only; it does not modify the collection.

Use the collection's Feed ID in the `/api/v2/inthreat/collections/{feed_id}/objects` endpoint and add both query parameters:

| Parameter | Value |
| --- | --- |
| `format` | `custom` |
| `template` | A single-line template using supported `$variable` names |

For example, `$observables # $description` exports the observable values followed by the indicator's description. URL-encode the template, including `$`, spaces, and `#`:

```text
https://app.sekoia.io/api/v2/inthreat/collections/YOUR-IOC-COLLECTION-FEED-ID/objects?format=custom&template=%24observables%20%23%20%24description&limit=10000&skip_expired=true&include_revoked=false
```

Authenticate using an API key with the **View IOC collections** permission. See the [blocklist integration guide](/xdr/usecases/playbook/implement_blocklist.md#connect-your-firewall-or-proxy) for equipment authentication and configuration.

Example response:

```text
192.0.2.10 # Indicator added after investigating a phishing alert
192.0.2.11 #
```

### Template behavior and limits

- `$observables` contains the observable values extracted from the indicator's pattern. Use this variable, rather than `$value`.
- `$description` contains the **indicator's description**, not the collection's description. If it is missing or empty, the variable produces an empty string. Line breaks in descriptions are replaced with spaces.
- Other supported variables include `$id`, `$name`, `$type`, `$observable_types`, `$pattern`, `$confidence`, `$tlp`, `$created`, `$modified`, `$valid_from`, and `$valid_until`.
- `${observables}` is equivalent to `$observables`. Use `$$` to output a literal dollar sign.
- A template must contain at least one supported variable and must fit on a single line. Invalid syntax or unsupported variables return HTTP 400.
- Each indicator produces one output line. When an indicator contains multiple observable values, such as several file hashes, `$observables` groups them on the same line, separated by commas. The standard `format=text` export emits these values on separate lines.
- Custom IOC Collection exports support up to **10,000 indicators per request**. This is a per-request limit, not a limit on the collection's size. Use API pagination when retrieving larger collections; a single request does not return the entire collection beyond that limit.

Choose a template and observable types that your receiving tool accepts. See [Implement a blocklist](/xdr/usecases/playbook/implement_blocklist.md) for the complete setup.
