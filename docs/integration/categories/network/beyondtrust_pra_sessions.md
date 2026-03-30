# beyondtrust\_pra\_sessions

uuid: f6cfddb4-543a-41fe-9802-c66b7c90366d name: BeyondTrust PRA Sessions type: intake

### Overview

BeyondTrust Privileged Remote Access enables secure, controlled remote access to critical systems for employees and vendors, focusing on protecting privileged credentials and sessions.

This integration allows you to ingest BeyondTrust Privileged Remote Access session logs into Sekoia.io, enabling you to monitor and analyze privileged access activities.

* **Vendor**: BeyondTrust
* **Supported environment**: SaaS
* **Detection based on**: Telemetry
* **Supported application or feature**:
  * Authentication logs:
    * Session Start
    * Session End
  * Application logs
    * Chat Message
    * Conference Member Added
    * Conference Member Departed
    * Conference Member State Changed
    * Conference Member State Changed
    * Conference Owner Changed
    * Directory Created
    * File Deleted
    * File Download
    * File Upload
    * Session Foreground Window Changed
    * Session Mouse Left Clicked
    * Session Mouse Left Clicked
    * Session Window Closed
    * Special Action Executed

### Configure

#### How to create an API token

1. Log in the BeyondTrust Privileged Remote Access console
2.  On the left panel, click `Management`

    {: style="max-width:100%"}
3.  Click `API Configuration`

    {: style="max-width:100%"}
4.  Check `Enable XML API` and click `+ Add`

    {: style="max-width:100%"}
5. Check `Enable`
6. Type a name for the API Account and add a comment (optional)
7. Check `Reporting > Allow Access to Access Session Reports and Recordings`
8. Copy the OAuth client ID and the OAuth client Secret
9.  Click `Save`

    {: style="max-width:100%"}

#### Instruction on Sekoia

{!\_shared\_content/operations\_center/integrations/generated/f6cfddb4-543a-41fe-9802-c66b7c90366d\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_f6cfddb4-543a-41fe-9802-c66b7c90366d\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/f6cfddb4-543a-41fe-9802-c66b7c90366d.md!}

### Further readings

* [BeyondTrust Integrations](https://docs.beyondtrust.com/bt-docs/docs/integrations)
