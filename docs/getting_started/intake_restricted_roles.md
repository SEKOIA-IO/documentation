# Intake Restricted roles

Intake restricted roles allow organizations to segregate user access by datasources.

Not all teams need access to the same data. For example, a network infrastructure team may only require access to network logs, whereas a security team needs broader access across all logs to monitor for threats.

Intake restricted roles enable organizations to compartmentalize data streams so that only users with the appropriate permissions can access specific subsets of data, efficiently manage responsibilities and ensure data confidentiality.

## Creating an intake restricted role

To create an `intake restricted role`, follow these steps:

1. Go to Settings > Workspace > Roles
2. Click on the Add New Role button
3. Provide role details:
    - Role name: Enter a name for the new role
    - Description: Write a description between 10 and 1000 characters to explain the purpose and responsibilities associated with this role
4. Click on the `specific intakes` label to restrict access to a specific list of intakes

    ![specific intakes](/assets/user_center/specific_intakes.png)

5. Select the intakes to authorize for this role and click on the `Next` button

    ![intake list](/assets/user_center/restricted_intake_list.png)

4. Choose the specific permissions you want to assign to this role. These permissions will define what actions users with this role can perform
5. Click `Save` to create the role. The new role will now appear in the roles listing.

## Assigning the intake restricted role to users

Once the `intake restricted role` is created, you can assign it to existing users:

1. Navigate to the Workspace users page in the settings menu
2. Select the user you want to assign the role to
3. Attribute the new custom role to the user and save your changes

## Important considerations

### Limited permissions

With Intake restricted roles, permissions selection is limited to `alerts`, `queries` and `events` due to the nature of this role.

### Disabling built-in roles

When you assign a custom role to a user, any built-in roles previously assigned to that user will be disabled. Ensure that the custom role includes all necessary permissions for the user’s responsibilities.

### Exclusive Intake restricted roles

You can assign only one intake restricted role per user. Intake restricted cannot be combined with built-in or custom roles.