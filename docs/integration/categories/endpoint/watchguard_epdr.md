---
uuid: 4f9ea4fb-e8b8-4001-822a-4c7a547c31d6
title: WatchGuard EPDR
name: WatchGuard EPDR
type: intake
---

## Overview

WatchGuard EPDR (Endpoint Protection Detection and Response) is a robust cybersecurity solution designed to protect against advanced threats. 
It provides real-time monitoring and automated response capabilities, ensuring comprehensive endpoint security for organizations of all sizes. With its intuitive management interface, businesses can easily detect, investigate, and remediate potential security incidents.

- **Vendor**: WatchGuard
- **Supported environment**: SaaS
- **Detection based on**: Alert
- **Supported application or feature**: Security events

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

### Enable API Access ( Creation of credentials )

1. Log in to your WatchGuard Cloud account.
2. If you are a Service Provider, go to Subscriber view for your own account or a managed account.
3. Select **`Administration` > `Managed Access`**
4. Click **`Enable API Access`**.
5. Specify the **readwrite** and **readonly** passwords to use as your API access credentials. Passwords must be at least 12 characters long and include a lowercase letter, uppercase letter, number, and symbol. The password must not include <, >, emojis, or spaces.
6. Select the **`I agree to the terms and conditions in the WatchGuard APIs License Agreement`** check box.
7. Click **`Save`**.
8. Copy the Access ID (read-only), the API URL (base) and the API Key

## Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format WatchGuard EPDR.
2. Set up the intake with the following parameters:
    - **username**: The Access ID (read-only) you copied when you created the credentials.
    - **password**: The password of the  Access ID (read-only)
    - **base url**: The scheme and the domain name of the API URL (base) (without the path; for example, `https://api.<region>.cloud.watchguard.com`).
    - **application key**: The API Key you copied when you created the credentials.
    - **account id**: The account ID of your WatchGuard Cloud account ID. You can find it on the My Account page in WatchGuard Cloud.

{!_shared_content/operations_center/integrations/generated/4f9ea4fb-e8b8-4001-822a-4c7a547c31d6_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_4f9ea4fb-e8b8-4001-822a-4c7a547c31d6_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/4f9ea4fb-e8b8-4001-822a-4c7a547c31d6.md!}

## Further Readings
- [Get Started with WatchGuard APIs](https://www.watchguard.com/help/docs/API/Content/en-US/api_get_started/get_started.html)
- [WatchGuard EPDR API authentication](https://www.watchguard.com/help/docs/API/Content/en-US/api_get_started/authentication.html)
