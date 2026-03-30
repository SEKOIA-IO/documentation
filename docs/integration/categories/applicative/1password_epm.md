# 1password\_epm

uuid: 09754cc4-e247-4712-9a76-25529ba11b8b name: 1Password EPM type: intake

### Overview

1Password's Enterprise Password Manager offers robust security features for businesses, enabling secure sharing and management of passwords and sensitive data across teams, with advanced admin controls and seamless integration into existing workflows.

* **Supported environment**: SaaS
* **Detection based on**: Telemetry, Audit
* **Supported application or feature**:
  * Audit Events
  * Item Usages
  * Sign-in Attempts

### Configure

#### How to create an API token

1. Log in the 1Password console
2. On the right panel, click `Integrations`
3. In the Events Reporting, Click the `Other`
4. Type a name for the Integration and click `Add Integration`
5. Type a name for the token, select the expiration period
6. Select `Audit events`, `Item usage events` and `Sign-in attempts` as events to report
7. Click `Issue token`

#### Create your intake

Go to your Sekoia.io [Intakes page](https://app.sekoia.io/operations/intakes), and follow these steps:

1. Click on **+ Intake** button to create a new one
2. Choose **1Password EPM**, give it a name and choose the relevant Entity
3. Click on **Create** button

* API token from `How to create an API token` step.
*   Base URL depending by the server that hosts your 1Password account:

    | If your account is on: | Your base URL is:                                                                                                   |
    | ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
    | 1Password.com          | <p>https://events.1password.com (1Password Business)<br>https://events.ent.1password.com (1Password Enterprise)</p> |
    | 1Password.ca           | https://events.1password.ca                                                                                         |
    | 1Password.eu           | https://events.1password.eu                                                                                         |

**Enjoy your events on the** [**Events page**](https://app.sekoia.io/operations/events)

{!\_shared\_content/operations\_center/integrations/generated/09754cc4-e247-4712-9a76-25529ba11b8b\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_09754cc4-e247-4712-9a76-25529ba11b8b\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/09754cc4-e247-4712-9a76-25529ba11b8b.md!}
