# github\_audit\_logs

uuid: 80de6ccb-7246-40de-bcbb-bc830118c1f9 name: Github Audit Logs type: intake

### Overview

* **Vendor**: Microsoft
* **Supported environment**: SaaS
* **Detection based on**: Audit
* **Supported application or feature**: Application Logs

Github audit logs represents activities on your Github organization.

This setup guide describes how to forward audit logs from Github to Sekoia.io.

### Configure

#### Prerequisites

* Your organization must use GitHub Enterprise Cloud to [get access to audit log API](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#using-the-audit-log-api)
* You must be Administrator of the organization. There are two options on how to configure connector:
  * [With Github API Key](github_audit_logs.md#creating-the-github-api-key)
  * [With Github PEM file](github_audit_logs.md#create-the-github-pem-file)

#### Creating the Github API key

To create an API key on [Github](https://github.com/):

1. On the top right corner, click on your profile picture then on `Settings`.
2. On the Developer Settings, create a Personal access token (classic) with read access to the audit\_logs.
3. Validate the configuration and save the token for the configuration of the connector.

#### Create the Github PEM file

1. On the top right corner, click on your profile picture then on `Your organizations`.
2. Select organization you want to create PEM file for:
3. Scroll to `Developer settings` and select `Github apps`:
4. Click on edit `Github app`:
   * Make sure you have all necessary rights (#1)
   * After that click on edit (#2)
5. Go to `General` section:
6. Scroll to `Private keys` section and click on `Generate a private key`:
7. Follow all necessary instructions and save PEM file for the configuration of the connector.
8. Scroll up and copy `App ID` for the configuration of the connector.
9. As a result you should have `App ID` and `PEM file` for the configuration of the connector.

#### Create the intake in Sekoia.io

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Github audit logs`.
2. Edit the intake configuration with the Github organization and the APIkey.

{!\_shared\_content/operations\_center/integrations/generated/80de6ccb-7246-40de-bcbb-bc830118c1f9\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_80de6ccb-7246-40de-bcbb-bc830118c1f9\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/80de6ccb-7246-40de-bcbb-bc830118c1f9.md!}
