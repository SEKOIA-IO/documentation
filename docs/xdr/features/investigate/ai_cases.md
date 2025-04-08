# AI Cases

## Table of Contents
1. [Overview](#overview)
2. [Feature Benefits](#feature-benefits)
3. [How AI Cases Work](#how-ai-cases-work)
4. [AI Case Creation and Alert Correlation](#ai-case-creation-and-alert-correlation)
5. [AI Case Priority System](#ai-case-priority-system)
6. [AI Case Updates](#ai-case-updates)

## Overview
AI Cases is an intelligent case management feature that automatically creates and manages security incidents by correlating related alerts. This feature streamlines the incident response process by providing SOC analysts with automated case creation, alert correlation, and contextual information.

![ai_case](/assets/operation_center/ai-case.gif){: style="max-width:100%"}

## Feature Benefits
* Automated case creation and alert correlation
* Intelligent incident summarization
* Dynamic case updates and priority management
* Comprehensive threat context
* Streamlined incident response workflow
* Reduced manual correlation effort
* AI-generated descriptions for individual alerts

## How AI Cases Work
AI Cases automatically processes security alerts and creates cases based on related incidents. Each case includes:

* Auto-generated title summarizing the incident
* Detailed description with threat context
* Correlated alerts from the same incident (up to 1000 alerts per case)
* AI-generated descriptions for individual alerts
* Dynamic priority rating
* Continuous updates over a 7-day period

## AI Case Creation and Alert Correlation
### Alert Correlation Criteria
AI Cases correlates alerts based on two main criteria:

**Asset-based Correlation:**

* Alerts targeting the same asset (account or host)
* Related infrastructure impacts

!!! Warning
    For the moment, `unverified` assets are excluded from the Correlation criteria. We are working to remove this limitation.

**Threat-based Correlation:**

* Same malware
* Same tool
* Same intrusion-set
* Same threat actor
* Same campaign
* Same vulnerability

### AI Case Description Generation
The case description is automatically generated using:

* Sekoia Cyber Threat Intelligence (CTI)
* Detection rule information
* Affected asset details
* Related alert context

## AI Case Priority System
Cases are automatically assigned priority levels based on the highest alert urgency value in the case. The case priority is recalculated whenever a new alert is added:

| Highest Alert Urgency | Case Priority |
|------------------------|---------------|
| 71-100                 | High          |
| 36-70                  | Medium        |
| 0-35                   | Low           |

## AI Case Updates
### Content Updates
* AI Cases remain active for 7 days from creation
* New related alerts are automatically added to existing cases (up to 1000 alerts maximum)
* Case descriptions are updated with new alert information
* Priority levels are adjusted based on alert criticality
* Each new alert receives its own AI-generated description
* After 7 days, the case becomes inactive and no more alerts are added

### Update Frequency
* Real-time alert correlation
* Immediate case priority updates
* Dynamic case description updates with new alerts
* Instant AI-generated descriptions for new alerts
