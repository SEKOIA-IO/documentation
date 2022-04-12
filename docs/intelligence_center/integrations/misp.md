# Intelligence Center External Integrations: MISP Feed

The default feed is available as a MISP feed.

It can be added to an existing MISP instance by following [MISP's documentation](https://www.circl.lu/doc/misp/managing-feeds/).

The following field values are required for the feed to work properly:

-   Input Source: Network
-   URL: `https://api.sekoia.io/api/v2/inthreat/misp`
-   Source Format: MISP Feed
-   Headers: `Authorization: Bearer <APIKEY>`
-   Enabled: `True`

You then need to make sure you have a scheduled task in place to regularly fetch the feed's content.

> **Warning**: MISP adds automatically the suffix `/manifest.json` to the feed URL. If you want to try the connection to the feed outside MISP or make a custom script, you need to use the following URL: `https://api.sekoia.io/api/v2/inthreat/misp/manifest.json`
