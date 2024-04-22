# Manage users

## Overview

A role has attached permissions allowing a user to access, view pages and use its features.

In the following sections, you will learn how to manage your users.

## Needed role and permissions

To manage users in a community, you need to be an Administrator of the community.

## Detailed page of a user

To access the detailed page of a user:

1. Go to the page `Managed communities` that’s accessible by clicking on your avatar in the upper right of the screen 
2. In the tab `Users`, click on the name of a user

From this page, you can: 

- Add new roles to the user
- See attached permissions to each role attributed
- Access the list of assigned roles
- Delete assigned roles
- Delete user from the community

<img width="787" alt="image" src="https://user-images.githubusercontent.com/101662967/186946653-164d6b71-b075-402c-8013-61046da65931.png">


## In MSSP communities

In an MSSP community, role management can be a bit tricky. 

When a user is invited to the main MSSP community, the roles assign to this person are applied to all managed communities.
Same behavior when a user is added on Main MSSP community.

In addition to that, external roles can be added in any managed community to the user role set previously in the main MSSP community.
Roles assigned to a user in a managed community are independent from their roles in other subcommunities.

For example, 

1) A user has been added with the role `IC_viewer` set in the main MSSP community.
This user will have this role applied in all other managed communities.

2) Then the admin adds the role `IC_writer` to this user in a specific managed community.
The user will have the role `IC_writer` in this specific managed community in addition to the role `IC_writer` set in the main MSSP community.

To learn more about how to invite users to MSSP communities, please refer to [this documentation](https://docs.sekoia.io/getting_started/invite_users/#in-an-mssp-community). 

## Create custom roles

As an admin of your community, you can control what kind of actions your guests are allowed to do. Our roles’ system is based on permissions already defined by us and we keep them up to date following our latest features.

For example, some users in your community will only be able to view data but cannot interact with it. Others can change the status of an alert, write a content proposal or simply duplicate a dashboard, without being able to access other parts of the app.

To create custom roles for your guests, you’ll have to:

1. Access your `Managed Communities` by clicking on your avatar on the upper right of the screen
2. Click on the `Roles` tab then on the `+Role` button
3. Provide a `name` and a `description` to your new role
4. Select `permissions` you want to give to your users
5. Save your changes

!!! note
    You can edit or delete roles by clicking on the icons on the right side of the table that lists all the roles.

## Add permissions

Permissions can be different depending on your job position at your company.
There are three main categories to all of these permissions: `Admin`, `Manage` or `View`.
