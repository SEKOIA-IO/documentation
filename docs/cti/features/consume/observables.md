# Observables

## What is interesting about the Observables page?

An observable is a technical information that can detect a potential threat.
They are derived from all data contained in the Intelligence Center but are not always contextualized.
If an observable cleary represents a malicious activity, then it is considered as an IoC.

This page provides a quick and efficient search engine for all the technical information available within the Intelligence Center, observables and IoC.

## Use Case

A classic use case is when you are looking for any information regarding an IP address, domain name, url or file hash. It will give you an answer with the potential related threat or/and associated tag.

## Tag

Tag information has a time validity and provides some technical enrichment depending of the type of the observable: geolocation, internet provider, reputation (e.g. scanner)

## How are the observables produced?

Technical information is automatically extracted from various sources: public, subscriptions, partners, SEKOIA internal analysis.

Depending of the source, a tag name could be associated with a `valid_from` and `valid_until` timestamp, providing an up-to-date technical information directly integrated to the Intelligence Center database: an IP address could be enriched with the tag `scanner` once, then have the tag expired if that IP address scanning activity is no longer observed.

An observable also has relationships with other observables: an IP address could `belongs-to` an subnet object, and have a url `hosted-on`. It could become an indicator of compromise with its associated threat (e.g. malware, campaign).

## The main features of the observables page

### Type (examples)

* Autonomous system
* x509 Certificate
* Directory
* Domain name
* Email addr
* File
* Filename
* Ipv4 addr
* Ipv6 addr
* Mac addr
* Mutex
* Organization
* Text
* URL
* Windows registry key

### Source (examples)

* SEKOIA
* SEKOIA C2 Tracker
* SEKOIA Malware Watcher
* Tria.ge
* URLHaus
* PhishTank
* MalwareBazaar

### Tag (examples)

* amazon_aws (Amazon AWS IP Ranges)
* cloudflare (Cloudflare IPv4)
* country:*	(Country)
* crl or ocsp (CRL and OCSP Domain Names)
* cryptomining (Domain Names related to Cryptomining activity)
* disposable_email	(List of domain names providing disposable email services)
* domains_top_1_000_000 (Top 1M domain names)
* domains_top_100_000 (Top 100k domain names)
* domains_top_10_000 (Top 10k domain names)
* dynamic-dns (Top 5000 dynamic malicious domains)
* google (Domain Names used by Google products)
* googlebot	(IP Addresses used by Google Bot)
* iplookup (IP Lookup Services)
* multicast	(RFC 5771 multicast CIDR blocks)
* nod:1month (Newly Observed Domains discovered within the past month)
* nod:4months (Newly Observed Domains discovered within the past 4 months)
* nod:12months (Newly Observed Domains discovered within the past 12 months)
* office365	(Office 365 IP Ranges and Domains)
* ovh_webhosting (Addresses IP OVH Web Hosting - Shared)
* rfc1918 (RFC1918 - Private Addresses)
* rfc5735 (RFC5735 - Special Use Addresses)
* rfc6598 (RFC6598 - Shared Address Space)
* rfc6761 (RFC6761 - Special Use Domain Names)
* scanner:*	(Hosts involved in mass scanning and/or exploitation attempts)
* security_vendor (Security Vendor Blogs)
* sinkhole (Brakmic Sinkholes)
* tor (Tor Exit Nodes)
* university (University Domain Names and Websites)
* url_shortener (URL Shorteners)

### Searches

You could proceed with bulk research, one observable on each line.
![!Intelligence Center Observable research](/assets/intelligence_center/observables_search.png){: style="width: 100%; max-width: 100%"}

The result page will give you two tabs, one for the known the other for the unknown with the potential associated tags, threats related.

When clicking on an Observable, a dedicated page will display information, raw object and sometimes relationships as shown bellow:
![!Intelligence Center Observable result](/assets/intelligence_center/observables_results_relationships.png){: style="width: 100%; max-width: 100%"}

## Example Use Case

You found some domain names during an investigation and you want to know if those observables are known in the Intelligence Center and if there is more context to it.

Simply paste the domain names into the search fields and hit enter.

In the `Known` tab you will find observables known in the Intelligence Center and some context over it if there is some. The `Unknown` tab will contain the observables never seen in the Intelligence Center.
