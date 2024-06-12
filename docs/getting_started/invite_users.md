# Invite users to join your workspace

To invite users to a workspace or a community, you need to send them an invitation to join you on Sekoia.io. You can invite as many users as needed as soon as you are an Administrator of the workspace/community. 

However, depending on the [type of community](concepts.md) you are in, the invitation process can differ. 

In this documentation, you will learn how to add news users to a workspace or a community. 

## Add new users to a workspace

To invite new users to a workspace, follow these steps: 

1. Navigate to the `Settings` page from the menu 
2. On the `Users` page, click the `Add new users` button
3. Enter the email addresses of the users you want to invite, separating each with a comma 
4. Select the communities you want to add them to
5. Assign roles to your guests. You can either select the default ones or create custom roles based on chosen permissions. Check this documentation to learn how to [create custom roles](docs/getting_started/roles.md). 

These steps are the same whether you want to invite new users to a workspace or to a community. 
In case it's a multi-tenant workspace, the invited user will only have access to the selected community, not the whole workspace. 

!!! note
     A welcome email with a password set link is sent only to new users on Sekoia.io (excluding existing members in other communities).

## Automatic creation of users with SSO Okta

As mentioned on [this page](sso/openid_connect.md): Workspace admins who have enabled SSO with Okta can configure an option to automatically create new users accounts in their workspace. When a user logs-in for the first time, their account will be automatically created. You can set the default role for newly created users, and you can choose the default role among all the roles available in your community.

 





