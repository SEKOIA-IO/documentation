# The Hive

## Overview

[TheHive](https://thehive-project.org/) is a scalable, open source and free Security Incident Response Platform. This integration allows you to forward SEKOIA.IO alerts in an instance of The Hive.

## Configure

First of all, you will have to retrieve your organisation name from your The Hive instance or create an organisation (see [The Hive documentation](https://docs.thehive-project.org/thehive/user-guides/quick-start/#create-an-organisation) to learn how to create an organisation).

Next, you will need a [user apikey](https://docs.thehive-project.org/thehive/user-guides/organisation-managers/users-management/) in this organisation with `manageAlert` permission (for example with the `analyst` profile [profile](https://docs.thehive-project.org/thehive/user-guides/administrators/profiles/). 

You now have all informations to configure The Hive module and its `Create Alert` action in SEKOIA.IO.

To start your playbook with an example template, go to : "Create a new playbook" > "Use a template" > Search for TheHive.

You can also create your own on the same basis. A typical playbook to send alerts to a TheHive instance will use this kind of chain :

- a trigger based on alerts (for example `Alert Webhook` one or `Alert Created`) ;
- a first action `Get Alert` to query the alert details ;
- a second action `Get events` to query the alert events, the query is `alert_short_ids:"{{ the alert short id variable }}"`, from `-1d` to `now` ;
- the hive `Create alert` action that will send the alert and its events to your instance of the hive