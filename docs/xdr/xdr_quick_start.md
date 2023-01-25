# Configure SEKOIA.IO XDR in 5 minutes

## Introduction

Right after the creation of a brand new community, a first set of standard configurations are to be completed on SEKOIA.IO Operations Center pages. This executive note guides you on the principal steps to follow on the fisrt minutes of a community setup. 

## Out of scope content 

The configuration of your User Center, available [here](https://docs.sekoia.io/getting_started/).

## Let's get started

1. Create an Entity

- Go to the Entities page and create an Entity
- Select the Alert generation mode of your choice. More details [here](https://docs.sekoia.io/xdr/features/collect/entities/)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0e0edb32-607d-4a0f-88aa-67687e9b3f5c/Untitled.png)

2. Create each Intake associated to the technology you would like to collect

- Go to the Intakes page and create the intakes one by one from the catalog
- Then ensure the logs are pushed to [SEKOIA.IO](http://SEKOIA.IO) using [syslog](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/rsyslog/) or [HTTPS](https://docs.sekoia.io/xdr/features/collect/ingestion_methods/https/) protocols providing the Intake key accordingly, or pulled by API find more details on each integration [here](https://docs.sekoia.io/xdr/features/collect/integrations/)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e802b9ae-29fd-4a58-bf8e-e255fc4a5974/Untitled.png)

3. Activate the detection rules with an effort levels of 1 and 2

- Enable all detection rules of effort levels 1 or 2, by filtring on each effort level before clicking on the “Enable all” button
- Automate the activation of future detection rule of the same effort levels following [this procedure](https://docs.sekoia.io/xdr/features/detect/rules_catalog/#enable-new-rules)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ca3b5de-d7e0-46c4-931d-fc1454632d64/Untitled.png)

**That’s it!**

Feel free to configure and customize your community to fit your needs, using other features as listed [here](https://docs.sekoia.io/xdr/).
