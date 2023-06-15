# Enrichers

An Enricher is a module that allows you to enrich Observables via external services.

In Sekoia.io, you have access to either free or paid services to perform enrichment tasks.

| Name | Type |
| --- | --- |
| DNS | Free |
| Whois | Free |
| VirusTotal | Paid |
| Censys | Paid |
| Shodan | Paid |
| BinaryEdge | Paid |

## Setup enricher services

In order to be able to use the paid enricher services they must be configured.

To do so once on the enrichers page click on the button "Enricher's Settings" as the top right of the page.

At the left of the page choose the service to configure and at the right you will see the settings to fill. 
The settings with a red star are required while the others are optional. 
Once the settings have been filled click on the "Save" button to persist them.

The enrichers from this service can now be used to enrich observables.


## Enrich an observable

On the details page of an observable, if enrichers are available click on the "Enrich" button at the top right of the page.

A list of available enrichers opens in a sidebar. Click on the enricher you would like to run to start the enrichment. 

Once the enrichment finished, it appears with a green tick and the result appears in the "Enrichers" tab of the observable. 

The enrichment can be expanded by clicking on the line to display the relationships that have been extracted from the result. 
The "See Code" button allows to see the raw result of the enrichment.


## Enrichers listing

The Enrichers home page lists the status and results of observable enrichment tasks performed from the Observables page or from a Content Proposal. Filters allow you to sort by observable type, enricher or task status.

An enrichment task can be:

- pending
- in progress
- completed
- failed

You can filter your enrichment tasks either by Observable type, Enricher type or task status.
