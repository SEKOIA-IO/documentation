---
uuid: e129243d-0eeb-4b4c-a0f6-f15051b04a7e
name: CyberArk Identity Audit Logs
type: intake
---

## Overview

- **Supported environment**: SaaS
- **Detection based on**: Audit
- **Supported application or feature**:
    - Audit Events

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Configure

### How to create credentials

1. Log in the CyberArk Administration Console
2. On the left panel, click on the application switcher and click `Audit`


    ![step2](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step02.png){: style="max-width:100%"}


3. On the left panel, Click `SIEM integrations`


    ![step3](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step03.png){: style="max-width:100%"}


4. Click `Create SIEM integration`


    ![step4](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step04.png){: style="max-width:100%"}
    ![step5](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05.png){: style="max-width:100%"}

5. Click on the link on the first link to go on the CyberArk Identity Administration console
6. On the left panel, go to `Apps & Widgets` > `Web Apps`
7. Click `Add Web Apps`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05c.png){: style="max-width:100%"}

8. In the popup, click on the tab `Custom`
9. Look for `OAuth2 Server` and click `Add`

    ![step5d](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05d.png){: style="max-width:100%"}
   
10. Click `Yes` in the new popup

    ![step5e](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05e.png){: style="max-width:100%"}
   
11. Type an `Application ID`, a `Name`, and a `Category`

    ![step5f](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05f.png){: style="max-width:100%"}
   
12. Go to the section `Scope`
13. Click the `Add` button and type `isp.audit.events:read` in the new entry

    ![step5g](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05g.png){: style="max-width:100%"}
   
14. Go to the section `Token`
15. Select `jwtRS256` as token type
16. Check `Client creds` as authentication method and uncheck other options

    ![step5h](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05h.png){: style="max-width:100%"}
   
17. Go to the section `Advanced`
18. Paste the following script
    ```
        setClaim('tenant_id', TenantData.Get("CybrTenantID"));
        setClaim('aud', 'cyberark.isp.audit');
    ```

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05i.png){: style="max-width:100%"}
   
19. Click `Save`
20. On the left panel, go to `Core Services` > `Users`
21. On the right panel, Select `CyberArk Cloud Directory Users` then click `Add User`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05j.png){: style="max-width:100%"}
   
22. In the section `Status`, check `Is service user` and `Is OAuth confidential client`
23. Type a login name, a display name, and a password
24. Click `Create User`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05k.png){: style="max-width:100%"}
   
25. Click on the user and go to the section `Application Settings`
26. Click `Add`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step5l.png){: style="max-width:100%"}
   
27. Select the Web application previous created

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05m.png){: style="max-width:100%"}
   
28. On the left panel, go to `Apps & Widgets` > `Web Apps`
29. Click on the application previously created
30. Go to the section `Permissions`
31. Click `Add`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05n.png){: style="max-width:100%"}
   
32. Look for the user previously created
33. Check it and click `Add`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05p.png){: style="max-width:100%"}
   
34. Check `Grant`, `View`, `Manage`, and `Delete` for the user
35. Click `Save`

    ![step5c](/assets/operation_center/integration_catalog/cloud_and_saas/cyberark_audit/Step05o.png){: style="max-width:100%"}
   
36. On the `Create SIEM Page`, type the name and the description of the integration and click `Apply`

### Instruction on Sekoia

{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/operations_center/integrations/generated/e129243d-0eeb-4b4c-a0f6-f15051b04a7e_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e129243d-0eeb-4b4c-a0f6-f15051b04a7e_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/e129243d-0eeb-4b4c-a0f6-f15051b04a7e.md!}

## Further readings

- https://docs.cyberark.com/audit/latest/en/content/audit/isp_siem-integration.htm
- [Add Service Users](https://docs.cyberark.com/identity-administration/latest/en/content/ispss/ispss-add-service-user.htm)
- https://api-docs.cyberark.com/docs/ispss-api-auth/2c297daca8a97-api-token-authentication-for-cyber-ark-identity-security-platform-shared-services