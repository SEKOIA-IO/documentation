## What happens when you add events to an alert? 
When you attach events to an alert, there are two mechanisms that are executed in parallel: alert generation and events externalisation.
Some latency might happen between alert generation and attaching events to an alert.

## Event search request on IP range
You can easily request an event search on IP range. For instance, with an IP address starting with 145, you can search by range as follow: `source.ip:[145.0.0.0 TO 145.255.255.255]`. 

## timestamp, event.created, event.start, event.end meaning

**timestamp** and **event.created** are the same (reception of logs and beginning of processing in Sekoia.io).

**event.created** is parsed and can be selected. The timezone is defined with UTC.
**event.start**   contains the date when the event started or when the activity was first observed.
**event.end**   contains the date when the event ended or when the activity was last observed.

**event.start** & **event.end** are activity and monitoring of the event (Pre-Sekoia.io if not producedd by Sekoia.io)

`event.start` <= `event.end` <= `event.created`

## What is the timestamp based on?
The event timestamp is based on the event timestamp (when it's created in the machine), not on the ingestion timestamp in Sekoia.io. 
