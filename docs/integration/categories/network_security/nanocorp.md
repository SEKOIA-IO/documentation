uuid: 0ebb28ba-5748-4617-af1f-51b7ca31bf9a
name: Nanocorp
type: intake

## Overview
Nanocorp provides network observability and security events, offering centralized visibility and enhanced detection capabilities across the infrastructure.


- **Vendor**: Nanocorp
- **Supported environment**: Cloud/On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Network events


## Configure

### Prerequisites

Before starting, ensure you have:

- Access to the **Brain Machine**
- Sufficient permissions to create an external connector
- The **Intake Key** provided by the Sekoia platform


### Configuration Procedure

#### 1. Access the Panopticon Page

1. Log in to the **Brain Machine**.
2. Navigate to the **Panopticon** page.
3. Click the **"Add external connector"** button.

#### 2. Create a Sekoia Connector

1. From the list of available connectors, select **"Sekoia"**.
2. Fill in the required fields.

### 3. Mandatory Parameter

- **INTAKE KEY** : The ingestion key provided by the Sekoia platform. This key is used to authenticate and forward events to your Sekoia tenant.

### Validation

1. Review the configuration settings.
2. Save the connector.
3. Verify that events are successfully forwarded to Sekoia.
