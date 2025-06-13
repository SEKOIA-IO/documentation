# Integrations Catalog 

This page provides a centralized overview of all available integrations that connect your essential tools and services to Sekoia.io. Explore a range of integrations, including intake formats, connectors, and playbook triggers and actions, designed to streamline your operations and extend platform capabilities.

## Explore Integrations

Looking for something specific? Use the search bar to quickly find the integration you need.

### Categories

Easily discover the integrations you need with our intuitive categorization:

- **Recent Integrations:** Stay up-to-date with the latest additions to our growing catalog.
- **Popular Integrations:** See what other users are finding most valuable, ranked by the number of installs.
- **All Integrations:** Browse our complete list of integrations, which can be sorted by:
    - Name (A-Z)
    - Most popular
    - Most recent

### Filters

Refine your search and find the perfect integration using our filters:

- **Featured:** Filter by Built-in and custom integrations
- **Categories:** Narrow down integrations by their primary domain or purpose (Cloud Providers, Email, Network, Threat Intelligence, etc…)
- **Content Types:** Identify integrations based on the type of content (Intake formats, connectors, triggers, actions)

### Quick Access

Quickly access our **[Integrations roadmap](https://roadmap-integrations.sekoia.io)** from the header to stay up-to-date on what's coming next for integrations. You can also easily jump to your **connected accounts** to manage all the external accounts you've logged into for your integrations.

## Integration detailed page

Each integration has its own detailed page, providing comprehensive information. On this page, you'll find:

- A description of the integration
- Information on where it is used, allowing you to directly pivot to the playbooks or intakes where the integration is active
- An overview of its content (Event collection, playbook actions and triggers) 
- A changelog to track latest updates

From this detailed listing, you can also create intakes or try playbook triggers and actions related to the integration.

## Create Your Own Integration

Can't find an integration that perfectly fits your unique needs? No problem! Unlock unlimited potential and effortlessly create custom integrations tailored specifically for you. With this capability, your integration possibilities are now boundless. Build your own playbook actions, triggers, connectors, intake formats, and more.

### Pre-requisites

To create a custom integration in Sekoia.io, you will need:

- Python version 3.11 or newer
- Your favorite IDE

### Steps to create your custom integration

1. **Install Sekoia.io Automation SDK**: Open your terminal or command prompt and run the following command `pip install sekoia-automation-sdk`
2. **Initialize the integration**: Create an empty integration code folder using this command line. The `modules` path should be the directory where you want to store your integration: `sekoia-automation new-module modules`
3. **Develop your integration**: From here, dive into our comprehensive developer documentation to build out the functionalities of your integration.

Once your development is complete, proceed to import your integration. Your custom integration will then be ready to use!

### How to import your integration

Connect and sync your GitHub or GitLab repository to import your integration once your code is ready.

- **If your repository is private:** You will need to allow Sekoia.io repository access by adding our public SSH key to your Git provider's settings.
    - **For GitHub:** Navigate to `Settings` > `Deploy keys`.
    - **For GitLab:** Go to `Settings` > `Repository` > `Deploy keys`.
- **Connect your repository:** Enter your repository URL in the designated field and click `Connect` to test the connection.

Once you've connected your repository and initiated the import, the platform automatically performs a series of checks on your integration's code. If all pre-requisites and development steps are successfully accomplished, indicated by a "green check" status, your custom integration will be officially created within Sekoia.io. At this point, it will become accessible from the main Integrations Catalog listing and can be used just like any other pre-built integration.
