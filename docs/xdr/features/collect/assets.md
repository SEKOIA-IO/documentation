# Assets

## What is an asset?

In SEKOIA.IO, assets participate to the security workflow of your community. When an incoming event matches with a defined asset, the event is enriched with assets information. Their criticality will be taken into account when calculating the urgency of an alert, together with the severity of the rule that triggered the alert. 

When more than one asset match with an event, the highest criticality is used for urgency calculation. 

Assets also permit the selective application of detection rules: rules can be applied to one, several or all entities, and to one, several or all assets.

## Types of assets

Assets in SEKOIA.IO can be of different types. There are three main categories: 

- **Branding** (banking, brand, project, social network)
- **People** (a person)
- **Technical** (certificate, computer, network, phone, product, custom)

The most commonly used by our users are:

- **Computers**: identified by an IP address or a hostname
- **Networks**: identified by CIDR
- **Users**: identified by an email address

## Assets’ homepage

The assets homepage lists all of your community’s assets, their type, creation date, events and alerts associated and the criticality score. 

The **numbers of events and alerts** shown in the table are calculated for the **past 7 days.**

**Criticality** of assets ranges from 0 to 100, 100 being the most critical.

## Create an asset

To create an asset from our UI, you have to: 

1. Click on `Asset` in the assets’ homepage
2. Select a category (`branding`, `people` or `technical`) 
3. Give it a name and a description 
4. Determine its `criticality` 
5. Choose your type of asset from the list
6. Add `key characteristics` depending on your asset’s type (see the list below)
7. Add `attributes` with values 
8. Save your settings

| Category | Type of asset | Key characteristics |
| --- | --- | --- |
| **Branding** | Banking | BIC, BIN |
|  | Brand | Brand, Domain |
|  | Project | Product, Project |
|  | Social Network | Facebook, Pinterest, Twitter, Instagram |
| **People** | Person | Email, Last name, Name |
| **Technical** | Certificate | x509 |
|  | Computer | fqdn, host, ip-v4, ip-v6 |
|  | Network | as, cidr-v4, cidr-v6 |
|  | Phone | Phone |
|  | Product | cpe-item, cpe-unknown |
|  | Custom | zone_name |

!!! tip
    To edit an asset, you have to click on an asset in the list, change what needs to be changed and click on `Save`.
