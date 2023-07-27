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

!!! Warning 
    In MSSP mode, an asset created in the parent community enriches only the events received in this parent community.

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

| Type of asset | Key characteristics | events ECS field |
| --- | --- | --- |
| **Brand** |  Domain | dns.question.name, dns.question.registered_domain, client.domain, client.registered_domain, destination.domain, destination.registered_domain, source.domain, source.registered_domain, server.domain, server.registered_domain, url.domain, url.registered_domain, x509.subject.common_name, x509.alternative_names, tls.client.x509.alternative_names |  
| **Person** | Email | client.user.email, destination.user.email, file.x509.alternative_names, x509.alternative_names, host.user.email, server.user.email, source.user.email, user.email, user.changes.email, user.effective.email, user.target.email, email.from.address, email.to.address, email.from, email.to, tls.client.x509.alternative_names |  
|  | Last name | user.full_name |  
|  | Name | user.name |  
| **Certificate** | x509 | x509.subject.common_name, x509.subject.distinguished_name |  
| **Computer** | fqdn | dns.question.name, dns.question.registered_domain, client.domain, client.registered_domain, destination.domain, destination.registered_domain, source.domain, source.registered_domain, server.domain, server.registered_domain, url.domain, url.registered_domain |  
|  | host | log.hostname, host.hostname, host.name |  
|  | ip-v4 | client.ip, destination.ip, host.ip, server.ip, source.ip |  
|  | ip-v6 | client.ip, destination.ip, host.ip, server.ip, source.ip |  
| **Network** | cidr-v4 | client.ip, destination.ip, host.ip, server.ip, source.ip |  
|  | cidr-v6 | client.ip, destination.ip, host.ip, server.ip, source.ip |  
| **Custom** |zone_name | customer.zone_name |  

!!! tip
    To edit an asset, you have to click on an asset in the list, change what needs to be changed and click on `Save`.
