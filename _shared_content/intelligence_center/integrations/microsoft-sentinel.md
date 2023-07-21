# External Integrations: Microsoft Sentinel

Microsoft Sentinel is a cloud-native, security information and event management (SIEM) and security orchestration, automation, and response (SOAR) solution.

Microsoft Sentinel enables you to use Sekoia.io produced threat intelligence by using SEKOIA.IO’s TAXII feed.

## Configure Sekoia.io

The first thing to do is to configure Sekoia.io to create a new CTI feed dedicated to Microsoft Sentinel and an API key so that you can access the CTI objects from Microsoft Sentinel.

### Create a new API Key

You should create a new API Key in Sekoia.io’s “User Center”:

1. Go to [Sekoia.io’s User Center](https://app.sekoia.io/user/profile).
2. On the left menu, click on “Managed Communities”.
3. Then click on the “API keys” tab title
4. Create a new API key and give a title and a description.
5. Finally, give the “Intelligence Center Read-Only” role to the API Key and click on the “Save” button.<br/>
![](/assets/intelligence_center/apikey_create.png)
6. Copy the API Key (which is only displayed once).

Please keep the resulting API Key carefully as it will be required later.

### Create a New Feed

In order to bring Sekoia.io threat intelligence in Microsoft Sentinel, the first step consists in creating a new CTI feed within SEKOIA.IO.

1. On Sekoia.io’s Intelligence Center, connect to the “Feeds” section
2. Create a new CTI feed by clicking on the “+ Feed” button:
3. Fill the feed creation form with the following information. Set an arbitrary title for you feed, choose to only export CTI “indicators” and choose the “JSON” format.<br/>
![](/assets/intelligence_center/create_feeds_form.png)
4. Click on “Save”:
5. After saving, the feed list is displayed. You can click next to the feed title to copy its unique identifier.<br/>
![](/assets/intelligence_center/create_feeds_copy-id.png)

Please keep the feed title unique identifier carefully as it will be used later.

## Configure CTI Feed in Microsoft Sentinel

1. Go to the Microsoft Sentinel interface in Microsoft Azure.
2. In the “Configuration” menu, click on “Data connectors”.
3. Search for “TAXII” and select “Threat intelligence - TAXII” connector.
4. Click on the “Open connector page” button.

In the “Threat intelligence - TAXII” connector page, fill the form with the following information:

- Friendly name (for server): `Sekoia.io`
- API Root URL: `https://app.sekoia.io/api/v2/inthreat/taxii-server`
- Collection ID: paste here your feed identifier.
- Username: `username`
- Password: paste here the API key that was created in the first step.
- Import indicators: “All available”.
- Polling Frequency: “Once an hour”.

![](/assets/intelligence_center/sentinel-configure-cti-feed.png)

Finally, click on “Add”.

After a short delay, Sekoia.io CTI will be pushed to Microsoft Sentinel and will be available in the “Threat Intelligence” section.
