uuid: 049b3dfd-8f67-40b6-a22d-b86ba3b42a05
name: Delinea Platform Audit Logs
type: intake

## Overview

Delinea Platform is a secure session‐broker solution that lets organizations grant, monitor and audit elevated RDP, SSH and SFTP connections to critical systems without exposing underlying credentials to end users. PRA integrates with your vault, identity providers and SIEMs to enforce just-in-time, least-privilege access policies, record every keystroke and file transfer, and stream real-time audit events for compliance and threat detection. By isolating sessions, injecting credentials on the fly and capturing detailed forensic logs, Delinea Platform reduces risk from shared accounts, lateral movement and credential theft while delivering complete visibility into who accessed what, when and how.

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

- **Vendor**: Delinea
- **Supported environment**: SaaS
- **Detection based on**: Audit events
- **Supported application or feature**:
    - Remote Access logs
    - Vault Secret logs

## Configure

This setup guide will show you how to forward your Delinea logs to Sekoia.io.

### Create a Role

1. Log in the Delinea Plaftorm Admin Portal.
2. Go to `Access` > `Roles`.

    ![Step 01](/assets/integration/iam/delinea_audit_logs/Step 01.webp){: style="max-width:100%"}

3. Click `Add Role`

    ![Step 02](/assets/integration/iam/delinea_audit_logs/Step 02.webp){: style="max-width:100%"}

4. Select `Add New Custom Role` as `Role Type`
5. Name the Role (e.g., `API Service Audit Role`).
6. Describe the Role (optional).
7. Click `Save`

    ![Step 03](/assets/integration/iam/delinea_audit_logs/Step 03.webp){: style="max-width:100%"}

8. Click the `Permissions` tab.

    ![Step 04](/assets/integration/iam/delinea_audit_logs/Step 04.webp){: style="max-width:100%"}

9. Select `Read Audit events` in the list of permissions.
10. Click `Assign`

    ![Step 05](/assets/integration/iam/delinea_audit_logs/Step 05.webp){: style="max-width:100%"}

### Create a Group

1. In the Delinea PRA Admin Portal, go to `Access` > `Groups`.

    ![Step 06](/assets/integration/iam/delinea_audit_logs/Step 06.webp){: style="max-width:100%"}

2. Click `Add Group`

    ![Step 07](/assets/integration/iam/delinea_audit_logs/Step 07.webp){: style="max-width:100%"}

3. Name the Group (e.g., `API Service Audit Group`).
4. Describe the Group (optional).
5. Click `Save`

    ![Step 08](/assets/integration/iam/delinea_audit_logs/Step 08.webp){: style="max-width:100%"}

6. Click on the new group

    ![Step 09](/assets/integration/iam/delinea_audit_logs/Step 09.webp){: style="max-width:100%"}

7. Go to the `Roles` tab.

    ![Step 10](/assets/integration/iam/delinea_audit_logs/Step 10.webp){: style="max-width:100%"}

8. Click `Assign Role`

    ![Step 11](/assets/integration/iam/delinea_audit_logs/Step 11.webp){: style="max-width:100%"}

9. Select the previously created Role (e.g., `API Service Audit Role`).
10. Click `Assign`.

    ![Step 12](/assets/integration/iam/delinea_audit_logs/Step 12.webp){: style="max-width:100%"}

### Create a user

1. In the Delinea PRA Admin Portal, go to `Access` > `Users`.

    ![Step 13](/assets/integration/iam/delinea_audit_logs/Step 13.webp){: style="max-width:100%"}

2. Click `More` > `Add service user`.

    ![Step 14](/assets/integration/iam/delinea_audit_logs/Step 14.webp){: style="max-width:100%"}

3. Name the user (e.g., `API Service Audit User`).
4. Type an email address.
5. Type a display name.
6. Select `Generated` or type a password.
7. Save the password somewhere safe.
8. Click `Next`.

    ![Step 15](/assets/integration/iam/delinea_audit_logs/Step 15.webp){: style="max-width:100%"}

9. Select the previously created Group (e.g., `API Service Audit Group`).
10. Click `Add`.

    ![Step 16](/assets/integration/iam/delinea_audit_logs/Step 16.webp){: style="max-width:100%"}

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Delinea PRA`.
2. Set up the intake configuration with the base url, the username as `client id` and the password as `client_secret` of the previously created service user.

{!_shared_content/operations_center/integrations/generated/049b3dfd-8f67-40b6-a22d-b86ba3b42a05.md!}

{!_shared_content/integration/detection_section.md!}


{!_shared_content/operations_center/detection/generated/suggested_rules_049b3dfd-8f67-40b6-a22d-b86ba3b42a05_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/049b3dfd-8f67-40b6-a22d-b86ba3b42a05.md!}

## Further readings

- [Authenticating with Platform API | Delinea](https://docs.delinea.com/online-help/delinea-platform/api/platform-apis.htm#Creating3)
- [Adding Users | Delinea](https://docs.delinea.com/online-help/delinea-platform/users/add-users.htm#ServiceUsers)
