# External Integrations: MISP Feed

The default feed is available as a MISP feed.

It can be added to an existing MISP instance by following [MISP's documentation](https://www.circl.lu/doc/misp/managing-feeds/).

To fetch Sekoia.io’s MISP feed, you’ll have to generate an API key with the `INTHREAT_READ_OBJECTS` permission. Please read the “[Generate API keys](../../../../getting_started/manage_api_keys)“ page to understand how to create a new API key with the proper permissions.

The following field values are required for the feed to work properly:

-   Input Source: Network
-   URL: `https://api.sekoia.io/api/v2/inthreat/misp`
-   Source Format: MISP Feed
-   Headers: `Authorization: Bearer <APIKEY>` (please replace `<APIKEY>` with the secret API key)
-   Enabled: `True`

![!Configuring Sekoia.io’s MISP feed in MISP](/assets/intelligence_center/misp_feed_configuration.png){width=400px}

You then need to make sure you have a scheduled task in place to regularly fetch the feed's content.

!!! note

    MISP adds automatically the suffix `/manifest.json` to the feed URL. If you want to try the connection to the feed outside MISP or make a custom script, you need to use the following URL: `https://api.sekoia.io/api/v2/inthreat/misp/manifest.json`

## Beta Version of Sekoia.io’s MISP Feed

!!! warning

    This feed is still considered as beta and should be used carefuly. If you find any regression or issue with this new feed, please contact your support.

The new MISP feed contains all non-expired Sekoia.io intelligence material and is constantly kept in sync with SEKOIA.IO’s intelligence feed. This way, when an indicator is updated in SEKOIA.IO, that latter will be also updated in the MISP feed. This will ensure that the indicator is not duplicated each time an indicator is updated.

The MISP feed is organized by data “source” per creation date of the indicator. Hence, if an indicator has several sources, it will be included in several MISP events.

You can configure your MISP instance to read Sekoia.io’s MISP feed by using this URL: `https://api.sekoia.io/v1/misp-gateway/misp`.
