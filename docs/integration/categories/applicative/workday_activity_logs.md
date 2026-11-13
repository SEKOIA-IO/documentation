uuid: abfabd65-f08d-4aee-bba1-c0b8cfdcdde6
name: Workday Activity Logs
type: intake

## Overview

Workday is a leading provider of enterprise cloud applications for finance, HR, and planning. This integration collects activity logs from Workday to provide visibility into user actions, data access, and system changes. The Activity Logging API enables security monitoring, compliance auditing, and threat detection by capturing detailed information about all user interactions with the Workday platform.

- **Vendor**: Workday
- **Supported environment**: SaaS
- **Detection based on**: Telemetry
- **Supported application or feature**: Application logs

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.

## Specification

### Prerequisites

- Access to Workday tenant with administrative privileges
- Ability to create API clients and integration system users
- OAuth 2.0 must be enabled in tenant security settings

### Transport Protocol/Method

- **Sekoia connector**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: JSON

## Step-by-Step Quick Configuration Procedure

1. Create an Integration System User (ISU)
    - Navigate to Create Security Group task
    - Create a new integration system security group
    - Navigate to Create Integration System User task
    - Create a new ISU account (e.g., Sekoia_ISU)
    - Assign the ISU to the integration security group
    - Set Session Timeout Minutes to 0 (no timeout)
    - Ensure the user has permissions to access Activity Logging API
    - Click OK to save

2. Register an API Client :
    - Navigate to Register API Client for Integrations task
    - Click OK to create a new API client
    - Enter a Client Name (e.g., "Sekoia Activity Logging Connector")
    - Select Scope: Choose System
    - Enable Non-Expiring Refresh Tokens
    - Important: Copy and save the Client ID and Client Secret immediately (they won't be shown again)
    

3. Generate a Refresh Token
    - Navigate to View API Clients task
    - Find your registered API client
    - Click on the API Client to open details
    - Click Manage Refresh Tokens for Integrations
    - Select the Integration System User created earlier
    - Click OK to generate
    - Important: Copy and save the Refresh Token immediately (it won't be shown again)

4. Configure the connector in Sekoia
    - Go to the [Sekoia.io](http://sekoia.io/) Operations Center
    - Navigate to Integrations > Intake catalog
    - Search for "Workday Activity Logging"
    - Click Create to add a new intake
    - Enter the following configuration :
        - Workday Host URL: Your Workday instance host (e.g., wd2-impl-services1.workday.com)
        - Tenant Name: Your Workday tenant name
        - Client ID: The Client ID from step 2
        - Client Secret: The Client Secret from step 2
        - Refresh Token: The Refresh Token from step 3
        - Token Endpoint URL: https://{workday_host}/ccx/oauth2/{tenant_name}/token
    - Click Save to start collecting logs

### **Troubleshooting section**

Add a troubleshooting section with common issues:

**Common Issues:**

1. **Authentication failures (401):**
    - Verify Client ID and Client Secret are correct
    - Check that the refresh token hasn't been revoked
    - Ensure OAuth 2.0 is enabled in tenant settings
    - Verify the ISU account is active and has necessary permissions
2. **No data collected:**
    - Check that the ISU has permissions to access Activity Logging API
    - Verify the time range in the configuration
    - Ensure the tenant has activity logs for the specified period
    - Check connector logs for errors
3. **Rate limit errors (429):**
    - The connector automatically handles rate limiting with backoff
    - If persistent, contact Workday support to request higher rate limits
4. **Duplicate events:**
    - The connector uses caching to prevent duplicates
    - If duplicates persist, check the checkpoint configuration

!!! Note
    If you encounter any issues during the configuration specified in this section "Instructions on the 3rd Party Solution," please do not hesitate to contact your editor. We also welcome any suggestions for improving our documentation to better serve your needs.

### Instruction on Sekoia

{!_shared_content/operations_center/integrations/generated/abfabd65-f08d-4aee-bba1-c0b8cfdcdde6_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/integrations/generated/abfabd65-f08d-4aee-bba1-c0b8cfdcdde6.md!}