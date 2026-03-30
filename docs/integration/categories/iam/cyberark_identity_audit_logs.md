---
uuid: e129243d-0eeb-4b4c-a0f6-f15051b04a7e
name: CyberArk Identity Audit Logs
type: intake
---

# cyberark\_identity\_audit\_logs

### Overview

* **Supported environment**: SaaS
* **Detection based on**: Audit
* **Supported application or feature**:
  * Audit Events

### Configure

#### How to create credentials

1. Log in the CyberArk Administration Console
2.  On the left panel, click on the application switcher and click `Audit`

    {: style="max-width:100%"}
3.  On the left panel, Click `SIEM integrations`

    {: style="max-width:100%"}
4.  Click `Create SIEM integration`

    {: style="max-width:100%"} {: style="max-width:100%"}
5. Click on the link on the first link to go on the CyberArk Identity Administration console
6. On the left panel, go to `Apps & Widgets` > `Web Apps`
7.  Click `Add Web Apps`

    {: style="max-width:100%"}
8. In the popup, click on the tab `Custom`
9.  Look for `OAuth2 Server` and click `Add`

    {: style="max-width:100%"}
10. Click `Yes` in the new popup

    {: style="max-width:100%"}
11. Type an `Application ID`, a `Name`, and a `Category`

    {: style="max-width:100%"}
12. Go to the section `Scope`
13. Click the `Add` button and type `isp.audit.events:read` in the new entry

    {: style="max-width:100%"}
14. Go to the section `Token`
15. Select `jwtRS256` as token type
16. Check `Client creds` as authentication method and uncheck other options

    {: style="max-width:100%"}
17. Go to the section `Advanced`
18. Paste the following script

    ```
        setClaim('tenant_id', TenantData.Get("CybrTenantID"));
        setClaim('aud', 'cyberark.isp.audit');
    ```

    {: style="max-width:100%"}
19. Click `Save`
20. On the left panel, go to `Core Services` > `Users`
21. On the right panel, Select `CyberArk Cloud Directory Users` then click `Add User`

    {: style="max-width:100%"}
22. In the section `Status`, check `Is service user` and `Is OAuth confidential client`
23. Type a login name, a display name, and a password
24. Click `Create User`

    {: style="max-width:100%"}
25. Click on the user and go to the section `Application Settings`
26. Click `Add`

    {: style="max-width:100%"}
27. Select the Web application previous created

    {: style="max-width:100%"}
28. On the left panel, go to `Apps & Widgets` > `Web Apps`
29. Click on the application previously created
30. Go to the section `Permissions`
31. Click `Add`

    {: style="max-width:100%"}
32. Look for the user previously created
33. Check it and click `Add`

    {: style="max-width:100%"}
34. Check `Grant`, `View`, `Manage`, and `Delete` for the user
35. Click `Save`

    {: style="max-width:100%"}
36. On the `Create SIEM Page`, type the name and the description of the integration and click `Apply`

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/e129243d-0eeb-4b4c-a0f6-f15051b04a7e\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_e129243d-0eeb-4b4c-a0f6-f15051b04a7e\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/e129243d-0eeb-4b4c-a0f6-f15051b04a7e.md!}

### Further readings

* [Integrate Audit with third-party SIEM applications](https://docs.cyberark.com/audit/latest/en/content/audit/isp_siem-integration.htm)
* [Add Service Users](https://docs.cyberark.com/identity-administration/latest/en/content/ispss/ispss-add-service-user.htm)
* [API token authentication for CyberArk Identity Security Platform Shared Services](https://api-docs.cyberark.com/docs/ispss-api-auth/2c297daca8a97-api-token-authentication-for-cyber-ark-identity-security-platform-shared-services)
