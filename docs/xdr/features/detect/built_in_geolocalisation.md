## IP geolocation and ASN enrichment

Sekoia.io automatically enriches events with geographical and network information for every detected IP address. This feature allows security analysts to quickly identify the origin of traffic and the Autonomous System Number (ASN) associated with an event.

# How it works
The Sekoia.io platform integrates IP geolocation data to provide context for your security events. This enrichment occurs automatically during the ingestion process and includes:

Country identification: Displays the country name and the corresponding flag.

ASN details: Identifies the network provider and the ASN code.

Data source and updates
Sekoia.io uses ipinfo.io as the primary data provider for these enrichments.

!!! note "Synchronization delay" The platform updates its local database from ipinfo.io every three days. You might observe temporary discrepancies between the latest ipinfo.io data and the information displayed in the Sekoia.io interface during these intervals.

Use cases
Threat Hunting: Filter events by specific geographic regions to identify anomalous traffic patterns.

Alert Investigation: Quickly determine if an IP address belongs to a known cloud provider or a specific ISP using the ASN enrichment.

Dashboarding: Create visualizations that represent the geographical distribution of your logs.