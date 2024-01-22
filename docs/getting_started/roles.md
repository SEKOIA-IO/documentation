# Overview

Role-based access systems are designed to enhance security and improve the user experience by defining user permissions based on their specific roles. These systems typically include built-in roles that are pre-defined and cannot be modified and Custom roles, providing additional options for user access control.

## Built-In roles

Built-in roles are a fundamental part of Sekoia's user management system. They are the default roles that each community possesses and cannot be modified. **The built-in roles, carefully designed with specific permissions, enhance the user experience and system security, making it reliable and trustworthy for all users.**

### Functionality of Built-In Roles

Three main built-in roles exist by default now in every community: the Guest, the Analyst, and the Admin role.

-   **Guest Role**: This role is read-only and is ideal for clients or anyone who needs to view the information but not interact with it.
-   **Analyst Role**: This role is designed for platform usage and can include your entire team. This allows for read and write access, enabling users to participate actively.
-   **Admin Role**: The Admin role is a special role that allows for community management tasks, such as adding or removing users and updating roles. Unlike the other roles, the admin role has the most access and control over the platform's settings.

### Future Progress

Based on user feedback, we plan to introduce more built-in roles to accommodate various roles in our clients' operational workflows. This means there will be more tailored options to suit your team's specific needs.

## Custom Roles

In addition to built-in roles, each admin may create Custom roles. These will work in conjunction with built-in roles, providing even more flexibility for user access control.

## Legacy roles

To create your own roles, please refer to this [section](https://docs.sekoia.io/getting_started/manage_users/#create-custom-roles).

| Name              | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| admin             | Community administrator                                                     |
| symphony_operator | Playbook usage                                                              |
| ic_viewer         | Intelligence Center Read Only                                               |
| oc_viewer         | Allow a user to ONLY view OC related data as a OC operator                  |
| oc_contributor    | Allow a user to view OC related data as a OC operator and to comment alerts |
| oc_operator       | Allow a user to manage alerts and incidents                                 |
| oc_administrator  | Allow a user to manage rules, templates, entities, countermeasures...       |
| manage_api_keys   | Allow a user to manage API keys of the community                            |
| manage_community  | Allow a user to do any actions on community settings                        |
| manage_roles      | Allow a user to create, update, delete and attribute role(s)                |
| manage_members    | Allow a user to add and delete users in the community                       |
