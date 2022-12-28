uuid: 22f2afd2-c858-443d-8e06-7b335e439c29
name: CrowdStrike Falcon
type: intake

## Overview

CrowdStrike Falcon is an Endpoint Detection and Response solution.
This setup guide explains how to forward and collect the detections and activity logs of your CrowdStrike EDR to SEKOIA.IO.

{!_shared_content/operations_center/detection/generated/suggested_rules_22f2afd2-c858-443d-8e06-7b335e439c29_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/crowdstrike-falcon_do_not_edit_manually.md!}

## Configure

To retrieve the events produced by your Falcon instance, a playbook must be configured with the dedicated trigger "Trigger on Falcon Events". This trigger requires the following API information to connect on the Event Stream of CrowdStrike:

* the base URL of the API (e.g. https://api.eu-1.crowdstrike.com)
* a client identifier
* a client secret

!!!important
    Use the "API Client & Keys" CrowdStrike configuration panel to create an OAuth2 API client with the `Read` permission on scope `Event Stream` and `Detection`. For Threat Graph, please contact Crowdstrike Support to activate it and create the ID of the legacy Threat Graph API.
