# Configure SEKOIA.IO XDR in 5 minutes

## Introduction


Following the creation of a new community, there is a set of standard configurations on SEKOIA.IO Operations Center pages that needs to be completed. This executive note provides guidance on the primary steps to be taken in the first few minutes of setting up a community.

## Out of scope content 

The full guide on how to create and setup an account, create and invite users to a community, manage roles, permissions and notifications and much more, is available [here](https://docs.sekoia.io/getting_started/).

## Let's get started

### Create an entity

1. Go to the Entities page and create an Entity
2. Select the `Alert generation` mode of your choice. More details [here](https://docs.sekoia.io/xdr/features/collect/entities/)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0e0edb32-607d-4a0f-88aa-67687e9b3f5c/Untitled.png)

### Create intakes 

To create intakes associated to the technology you woud like to collect: 

1. Go to the Intakes page and create intakes one by one from the catalog
2. Make sure the logs are pushed to [SEKOIA.IO](http://SEKOIA.IO) using [syslog](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/rsyslog/) or [HTTPS](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/https/) protocols providing the Intake key accordingly, or pulled by API

!!! note
    Find more details on each integration [here](https://docs.sekoia.io/xdr/features/collect/integrations/). 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e802b9ae-29fd-4a58-bf8e-e255fc4a5974/Untitled.png)

### Activate detection rules 

1. Enable all detection rules of effort levels 1 or 2 by filtring on each effort level then clicking on the `Enable all` button
2. Automate the activation of future detection rule of the same effort levels following [this procedure](https://docs.sekoia.io/xdr/features/detect/rules_catalog/#enable-new-rules)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ca3b5de-d7e0-46c4-931d-fc1454632d64/Untitled.png)

**That’s it!**

Feel free to configure and customize your community to fit your needs, using other features as listed [here](https://docs.sekoia.io/xdr/).
