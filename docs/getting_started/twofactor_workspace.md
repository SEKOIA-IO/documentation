# Enforce Two-Factor Authentication for all users

Two-Factor Authentication (2FA) adds an extra layer of security to user accounts by requiring a second form of verification during login. This ensures that even if a password is compromised, unauthorized access is prevented.

## Benefits of enabling 2FA to all users in a workspace

- **Enhanced security**: 2FA provides additional protection for user accounts, making it significantly harder for unauthorized users to gain access.
- **Compliance**: Many security standards and regulations recommend or require the use of 2FA for enhanced data protection.

## Enforcing 2FA for all users

To enforce 2FA for all users in a community, you need to have the necessary permissions. Follow these steps:

1. Navigate to the Settings page 
2. Go to the Workspace security section 
3. Locate the Two-Factor Authentication option 
4. Click on Enable and follow instructions
5. Confirm and save your changes to enforce the new security policy.

!!! note
    When deploying 2FA for all workspace users, they will be forced to [configure their second authenticator factor](account_security.md) on their next login. 


## Impact of enabling 2FA

**New users**: New users will be required to configure 2FA during the registration process. This ensures that every new account has 2FA enabled from the start.

**Existing users**: Users who are logged out and do not have 2FA configured will be redirected to the 2FA configuration page upon their next login attempt. They will need to complete the 2FA setup to gain access to their account.