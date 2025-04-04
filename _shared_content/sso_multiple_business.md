## Important Note on SSO Configuration for Multiple Business Entities

When configuring Single Sign-On (SSO) for organizations that have multiple business entities with the same email domain, it's essential to ensure that users from one entity do not have access to the other’s Sekoia communities. Here are specific recommendations to achieve this:

- **Disable Automatic User Creation**: While configuring SSO for both entities, ensure that the "automatically create user if missing" option is **NOT** enabled. This setting will prevent unintended account creation across different communities. Only manually created account in a community will have the possibility to login to it.
- **Allow Same Domain**: SSO can be configured to support the same email domain across two distinct communities without issues. This means entities can use the same domain for authentication while keeping their communities isolated.
- **Utilize Distinct Providers**: It’s advisable to set up unique providers for each business entity, which involves **creating separate policies**. This configuration will help restrict access to specific users and reduce the possibility of misconfiguration on Sekoia.io.