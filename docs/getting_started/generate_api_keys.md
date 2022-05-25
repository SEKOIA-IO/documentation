# Generate API keys

## Overview

API keys are an important part of the platform. They let our users automate actions and provide technical access without going through the UI.

An API key is not only a unique identifier and a secret token for authentication, but it can also work as a mean to give an access that is more specific to the identity that is associated with it. 

Some bricks within the app also require the creation of an API key such as our CTI interconnection with third-party tools and playbooks.

## API keys listing

To access the list of generated API keys in your community, you have to click on your avatar, go to Managed communities and click on the `API keys` tab.

On this view, you can:

- Search for an API key by using the search bar on top of the table
- Filter your API keys by status: `Active`, `Revoked`, `All`
- Add a new API Key by clicking on the button `+ API key`

The table that lists API keys has various columns where you can find the following:

- Name of the API key
- Description of the API key
- ID of the API key that can be copied with the button icon `copy`
- Creation date
- Roles linked to the API key
- Status:  `Active`, `Revoked`, `All`
- A button to edit the API key

## Create an API key

To create a new API key, you’ll have to:

1. Click on the `+ API key` button
2. Give a name and a description to your key
3. Select one or more roles associated to your key. For instance, if you want to use your key to retrieve information from the Intelligence Center, you can use the role `ic_viewer - Intelligence Center Read-Only`
4. Click on `Save`

!!! note
    The key will only be displayed once. We recommend you save it into a vault.

## Revoke an API Key

Revoking an API key make it useless. It’s rather easy to do but keep in mind that it’s an action that cannot be reversed. 

To revoke an API key, you’ll have to: 

- Access the `Managed communities` page
- On the API key tab, click on the `Edit` button
- From there, you can revoke the API key by clicking on the red button `Revoke`
