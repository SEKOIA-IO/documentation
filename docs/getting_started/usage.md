# Usage overview

The Usage page provides users with a comprehensive overview of their data consumption and performance metrics associated with their communities. This feature is essential for understanding resource allocation and ensuring compliance with the usage policy. Users can access detailed analytics regarding their analyzed bytes by community, as well as all executed playbook actions, facilitating efficient monitoring of usage and prevention of service degradation.

## How it works

Upon accessing the Usage page, you are presented with a dashboard that displays current month data usage. The dashboard consists of key sections:

- **Analyzed Bytes**: Visualizes the total data analyzed by the community.
- **Executed Playbook Actions**: Summarizes automation actions taken based on user-defined playbooks. 

As a member of a workspace, you can quickly review consumption metrics across all your communities. The summary table includes:

- **Community name**
- **Number of subscribed assets**: Total subscribed assets in each community (based on what has been defined in your contract with Sekoia). 
- **Type of subscription**: The subscription plan type.
- **Analyzed bytes**: The amount of data analyzed, applicable to your plan.

You can also have a look at your previous consumption by clicking on the date selector in the upper right of the screen. 

## Sections

### Analyzed bytes

In the Analyzed bytes section, users can view a detailed breakdown of their monthly data usage in relation to their usage policy.

- **Current usage**: Displays the total bytes analyzed (e.g., 100 GB).
- **Fair use indicator**: A visual marker shows whether current consumption exceeds the fair use threshold.

### Fair use policy

The Fair Use Policy ensures equitable access to platform resources for all users. If a user exceeds their allocated usage, they may experience degraded performance or incur additional charges. 

Tracking consumption empowers users to proactively adjust their data usage and consider upgrading their plans if necessary.

!!! note
    If you are on an **Intelligence plan** only, please note that you will not see any analyzed bytes, as there are none associated with this plan.

### Playbook Actions

The Executed Playbook Actions section displays the total number of actions completed within the selected month. This is calculated by:

- **Number of actions**: Each playbook action initiated by the user within their playbooks is logged. The total actions executed by the user are aggregated and presented accordingly.
- **Usage patterns**: Users can identify trends in their automation efforts. 

### Definition of an asset

An asset refers to any equipment that produces logs, including user workstations, servers, and virtual machines. Customers subscribe based on the number of assets they wish to monitor, which directly influences their data usage and associated costs.

## Plans and usage

### Defend CORE and PRIME plans

Depending on the plan you are subscribed to, you may have different thresholds for data usage:

- **Defend CORE**: Fair use threshold is set at **3GB per asset per month**.
- **Defend PRIME**: Faire use threshold is set at **5GB per asset per month**.

Both plans implement a soft violation policy. If a user exceeds the set thresholds, they will be notified, but no immediate penalties will be enforced.

### Defend FLOW Plan

The FLOW plan establishes threshold metrics for data usage based on a predefined number of GB per month. 

