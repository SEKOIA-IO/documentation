uuid: 8f472113-ba5b-45b9-9a2c-944834396333
name: Security Scorecard Vunerability Assessment Scanner 
type: intake

## Overview

SecurityScorecard's Vulnerability Assessment Scanner is a tool designed to identify and assess vulnerabilities in an 
organization's digital infrastructure, offering real-time insights and prioritized recommendations to strengthen 
security measures and reduce cyber risk.

!!! warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

{!_shared_content/operations_center/detection/generated/suggested_rules_8f472113-ba5b-45b9-9a2c-944834396333_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/8f472113-ba5b-45b9-9a2c-944834396333.md!}

## Configure

This setup guide will show you how to provide an integration between Security Scorecard Vunerability Assessment Scanner 
events and Sekoia.io.

### Create an intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Security Scorecard VAS.
Copy the intake key.

### Configure Security Scorecard

* Login to admin panel and go to `Rule Builder` tab.

    ![Rule Builder](/assets/instructions/securityscorecard_vas/securityscorecard_vas_1.png)

* Click `Create Rule` button.

    ![Create Rule](/assets/instructions/securityscorecard_vas/securityscorecard_vas_2.png)

* In the forms that you see please feel all the fields with correct values and use `Send web request to` as action.
Set the destination url to `https://intake.sekoia.io/plain?intake_key=<intake_key>` with value from previous steps.

    ![Create Rule](/assets/instructions/securityscorecard_vas/securityscorecard_vas_3.png)

* Save the configuration and enjoy your events

## Further Readings

- [Build apps with SecurityScorecard](https://securityscorecard.readme.io/docs/build-an-app)
