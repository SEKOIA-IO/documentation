# Incoming feeds

Incoming feeds allow to ingest data from other sources in the TIP.

## Creating a feed

The first step consists in creating a new incoming feed. To do so click on "Settings" at the top right and "+ Feed".

When creating a new incoming feed it is possible to choose between:

* A SEKOIA.IO TIP feed
* A TAXII server

Depending on the feed type different options will be offered to contact the remote server. It is also possible to choose:

* To activate the feed or not once it is created
* If the content proposals from the feed should be merged automatically or not. If set, it is also possible to choose to ignore the warnings during the merge. In this case all the [warning rules](./warning_rules.md) will be ignored.
* To skip expired objects (TIP only): Objects that are expired on the remote TIP instance will not be synchronized in this TIP.
* To start the synchroniztion from a specific point in time (TIP only): It allows to only retreive fresh data and avoid having the intial synchronization taking too much time.

## Enabling/Disabling a feed

From the home screen of the outgoing feeds click on "Settings" at the top right. On this page we can see all the feeds that have been created and for each of them a slider allows to enable or disable it.

## Tracking synchronization results

### Sychronization tasks list

On the main page of the incoming feeds we can see all the synchronization tasks that ran or are still running.

Each line in the table allows to see:

* To which feed this synchronization task belongs to
* When it started
* The time it took
* The number of bundles this task created and how many of them have been processed
* The number of bundles in error
* The status of this synchronization task. Possible statuses are:
    * Fetching bundles: The synchronization is fetching bundles from the remote source
    * Ingesting bundles: All the bundles have been retrieved and they are being ingested
    * Finished: The synchronization is done
    * Canceled: A synchronization task is already running for this feed so this one has been canceled 
    * Error: Something wrong happened during the synchronization. More information are available in the details of this synchronization task


### Sychronization task details

When clicking on a specific line it is possible to get the details of the synchronization task. 

For all tasks we have common information like the URL that was contacted, when it started, the output, ... Tasks in error also have a stack trace allowing to troubleshoot what went wrong.

We also have details about the bundles that have been ingested:

* The ingestion status of the bundle. Possible statuses are:
    * Pending: The bundle is waiting to be processed by a worker
    * Running: The bundles is being processed
    * Success: The bundle has been processed successfully
    * Retrying: An error occured when processing the bundle but it will be retried later
    * Failed: It was not possible to process the bundle after many tries
* It is possible to download the JSON bundle if the status is not "Success"
* It is possible to see the created content proposal when the bundle is not in "Pending"
