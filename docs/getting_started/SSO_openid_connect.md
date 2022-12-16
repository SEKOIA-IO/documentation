# Single Sign On With openID Connect

To make it easier for employees to access SEKOIA.IO, you can enable SSO on SEKOIA.IO. 

## Prerequisites for Open ID connect
- Your Identity Provider (IdP) must support the OpenID connect standard
- Only admin user with the following permission "COMMUNITY_WRITE_ROLE" can configure the SSO

## Configure SSO on SEKOIA.IO

To set up SSO, follow these instructions :

1. Log in to SEKOIA.IO platform
2. Click on your profile picture and select `Account settings` to access the User center
3. Under Manage community > Authicafication, click on the button `Configure` 
5. Fill in identidy provider details
6. Save the configuration

Once SSO is set up and your IdP is configure to accept requests, users can log in via the Single Sign-on URL available on this page.
Share it with your users.
![SSO_URL](/assets/getting_started/SSO_URL.png)


## Just in time provisioning (JIT)
You can choose to enable automatic creation of your users. When your user logs in for the first time, his account will be automatically created. You can set the default role for new JIT users. You can choose the default rôle among all the roles available in your community.
![SSO_JIT](/assets/getting_started/SSO_JIT.png)

If you don't enable it, you will have to manually create user accounts. You can find all the details on how to "Invite users to join your community" [Here](https://docs.sekoia.io/getting_started/invite_users/).


## Login method
Once you have completed your configuration of SAML SSO, users will be able to log in via SSO.
Users who create their account via SSO, can only log in via this method. 
Only users who create their account via invitation and set up username/password can use both methods to log in : SSO and username/password. 
When Two-factor authentication is enabled or enforced to your account, if you log in via single sign-on, you will not be subject to this.


## Diseable account
To prevent a user from retrieving your organization's data, deactivate the user from your community and your identity provider.




