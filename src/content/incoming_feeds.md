---
title: # Incoming feeds
---

# Incoming feeds

Incoming feeds allow to ingest data from other sources in the TIP.

## Creating a feed

The first step consists in creating a new incoming feed. To do so, click on `Settings` at the top right and `+ Feed`.

When creating a new incoming feed, it is possible to choose between:

- A Sekoia.io TIP feed
- A TAXII 2.1 server

Depending on the feed type chosen, different options will be offered to contact the remote server. It is possible to choose:

- To activate the feed or not once it is created
- If the content proposals from the feed should be merged automatically or not. If set, it is also possible to choose to ignore the warnings during the merge. In this case all the [warning rules](./warning_rules.md) will be ignored.
- To skip expired objects (TIP only): Objects that are expired on the remote TIP instance will not be synchronized in this TIP.
- To start the synchroniztion from a specific point in time (TIP only): It allows to only retreive fresh data and avoid having the intial synchronization taking too much time.

## Enabling/disabling a feed

To enable or disable an incoming feed: 

1. Go to `Incoming feeds`listing
2. Click on the `Settings` button on top of the table 
3. In the `Settings` table, all incoming feeds are listed
4. Click on the toggle in the last column of the table to enable or disable a feed 

## Tracking synchronization results

### Synchronization tasks list

On the main page of the incoming feeds are listed synchronization tasks that ran or are still running.

Each line in the table allows to see:

- To which feed this synchronization task belongs to
- When it started
- Its duration
- The number of bundles this task created and how many of them have been processed
- The number of bundles in error
- The status of this synchronization task. Possible statuses are:

| Status | Description |
| --- | --- |
| Fetching bundles | The synchronization is fetching bundles from the remote source |
| Ingesting bundles | All the bundles have been retrieved and they are being ingested |
| Finished | The synchronization is done |
| Canceled | A synchronization task is already running for this feed so this one has been canceled |
| Error | Something wrong happened during the synchronization. More information are available in the details of this synchronization task |

You can filter results either by `Feed` or by `Status`.  

### Synchronization task details

When clicking on a specific line in the synchronization task details, it is possible to get the details of the synchronization task. 

For all tasks, there are common information like the URL that was contacted, when it started, the output... 

Tasks in error have a stack trace allowing to troubleshoot what went wrong.

There are also details about the bundles that have been ingested:

- The ingestion status of the bundle. Possible statuses are:

| Status | Description |
| --- | --- |
| Pending | The bundle is waiting to be processed by a worker |
| Running | The bundle is being processed |
| Success | The bundle has been processed successfully |
| Retrying | An error occurred when processing the bundle but it will be retried later |
| Failed | It was not possible to process the bundle, even after many tries |
    
- When the bundle is not in `Success`, it is possible to download the JSON bundle. 
- When the bundle is not in `Pending`, it is possible to see the created content proposal. 
