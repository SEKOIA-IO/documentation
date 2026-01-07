# Usage overview

The Usage page provides users with a comprehensive overview of their data consumption and performance metrics associated with their communities. This feature is essential for understanding resource allocation and ensuring compliance with the usage policy. 

From this page, users can access detailed analytics regarding their analyzed bytes by community, as well as all executed playbook actions. 

## How it works

### Single-tenant communities

The Usage page is accessible from the `Settings` section. On this page, users are presented with a dashboard containing the following widgets: 

- **Analyzed bytes**: An overview of the analyzed bytes for this community. The progress bar shows the following:
    - Current: Actual data usage for this community for the current month. 
    - Projected: An estimate of the data volume that is anticipated to be transmitted over a month. It is calculated based on analyzing past data usage trends. 
- **Executed Playbook actions**: Total number of playbook actions taken based on playbooks in this community. 
- **Date selector**: In the top right corner of the page, it allows users to browse and analyze consumption data by month.

For communities with the `Intelligence plan` only, there are no widgets yet, but new ones should be implemented soon. 

### Multi-tenant communities 

As members of a workspace, users can quickly review consumption metrics across all of their communities. In addition to the previously described widgets, a summary table lists the following information: 

- **Community name**
- **Number of subscribed assets**: Total subscribed assets in each community (based on what has been defined in your contract with Sekoia). 
- **Type of subscription**: The subscription plan type.
- **Analyzed bytes**: The amount of data analyzed by month, applicable to your plan.






