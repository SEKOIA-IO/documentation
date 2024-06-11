# Manage API keys

## Overview

API keys are a crucial component of the Sekoia.io platform, enabling users to automate actions and provide technical access without needing to navigate through the UI.

An API key serves as both a unique identifier and a secret token for authentication. It allows for specific access tailored to the identity associated with it, ensuring secure and controlled interactions with the platform.

### Uses of API Keys

- **Automation**: Automate various tasks and workflows within the platform, enhancing efficiency and productivity
- **Technical access**: Provide technical access for integrations and interactions without relying on the UI
- **Specific access control**: Grant precise permissions and access levels specific to the API key’s associated identity, ensuring that only authorized actions are performed

### Required for certain features

Some features within the app require the creation of an API key, including:

- CTI interconnection: Connect with third-party tools for Cyber Threat Intelligence (CTI) sharing and integration
- Playbooks: Utilize API keys within playbooks to execute automated responses and processes.

By using API keys, users can seamlessly integrate with Sekoia.io and leverage its capabilities to their full extent, ensuring secure and efficient operations.


## API keys listing

To access the list of generated API keys in your community, you have to go to Settings > Workspace > API Keys.

On this view, you can:

- Search for an API key by using the search bar on top of the table
- Filter your API keys by status: `Active`, `Revoked`, `All`
- Add a new API Key by clicking on the button `+ API key`

!!! note 
    Only users with admin roles and permissions have the right to create API keys. 

## Create an API key

To create a new API key, you’ll have to:

1. Click on the `+ API key` button
2. Give a name and a description to your key (description should be more than 10 characters and less than 100 characters)
3. Select one or more roles to associate with your key. For instance, if you want to use your key to retrieve information from the Intelligence Center, please select the role `ic_viewer - Intelligence Center Read-Only`
4. Click on `Save`

!!! note
    The key will only be displayed once. We recommend you to save it into a vault.

## Revoke an API Key

Revoking an API key will make it unusable. It’s rather easy to do but keep in mind that it’s an action that cannot be reversed.

To revoke an API key, please proceed with the following steps:

1. Go to Settings > Workspace > API Keys 
2. Click on the `Edit` button next to your API Key 
3. Revoke the API key by clicking on the button `Revoke`
