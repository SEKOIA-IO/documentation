uuid: 59498b29-5cfb-46e6-aaf1-9c0c3afeb00c
name: Stormshield
type: playbook

# Stormshield

![Stormshield](/assets/playbooks/library/stormshield.png){ align=right width=150 }

Stormshield Network Security is a range of network security appliances.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | Base URL of the Stormshield SNS API |
| `api_token` | `string` | Authentication token for the API |

## Actions

### Block IP address

Block an IPv4 or IPv6 address on Stormshield SNS.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `ip_address` | `string` | IPv4 or IPv6 address to block |
| `duration_s` | `integer` | Duration in seconds for which the IP should be blocked |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `status` | `string` |  |
| `ip_address` | `string` |  |
| `duration_s` | `integer` |  |
| `message` | `string` |  |
| `response` | `object` |  |

## Set up

## Configuration

### Create a Stormshield REST API key

1. **Access the administration interface:**

      - Open your web browser and go to the firewall administration URL (e.g., `https://api.stormshield.lab`).

      - Enter your username and password to log in.

2. **Navigate to the REST API menu:**

      - In the left navigation column, expand the **SYSTEM** menu.

      - Click on **REST API**.

3. **Initiate the key creation:**

      - On the REST API page, navigate to the **API KEY** tab.

      - Click the **Create** button.

4. **Configure key privileges:**

      - In the creation pop-up window, configure the following:

         - **Comment**: Add a description if necessary (optional).
         - **Lifespan**: Modify the validity duration according to your needs (optional).
         - **Access rights**: You must select the **Blacklist management - Read/Write** option.
         
      - Validate the generation.

5. **Save the generated key and secret:**

      - A confirmation window titled "THE API KEY HAS BEEN CREATED" appears.

      - Copy the long alphanumeric character string generated in the bottom text field.

    !!! warning
        Make sure to store this API key and the associated secret in a secure location (like a password manager). The system explicitly states that it will be impossible to recover this secret once this window is closed.

6. **Finish the operation:**

      - Only after ensuring you have safely saved the secret, click the **CLOSE** button to close the window.


## Extra

Module **`Stormshield` v1.0.3**