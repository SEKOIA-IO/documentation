# Notebooks (coming soon)

## Table of Contents
1. [Overview](#overview)
2. [Feature Benefits](#feature-benefits)
3. [Getting Started with Notebooks](#getting-started-with-notebooks)
4. [Creating and Managing Notebooks](#creating-and-managing-notebooks)
5. [Notebook Templates](#notebook-templates)
6. [Command Menu and Formatting](#command-menu-and-formatting)
7. [Sharing Notebooks](#sharing-notebooks)
8. [Notebook Management](#notebook-management)
9. [Notebook Practices](#best-practices)

## Overview
Notebooks is a powerful incident response feature that allows SOC analysts to centralize their `investigation queries`, `automation actions`, and `reporting` in a single document. With support for markdown syntax and rich media, Notebooks streamlines the incident response process and facilitates team collaboration.

![notebook](/assets/operation_center/notebook.gif){: style="max-width:100%"}

## Feature Benefits
* Centralized incident response
* Embedded queries and automations
* Customizable templates for different threat types
* Rich text formatting with markdown support
* Standardized response processes
* PDF export
* Multi-tenant sharing capabilities

## Getting Started with Notebooks

### Types of Notebooks
**Standalone Notebooks**

* Independent notebooks for general use (threat hunting, custom reporting)
* Accessible from the `Notebooks menu`

**Context-linked Notebooks**

* Attached to specific `cases` or `alerts` for incident response
* Directly accessible from the `Notebooks tab` within cases or alerts
* Provides centralized investigation context

## Creating and Managing Notebooks

### Creating a New Notebook
1. Navigate to the `Notebooks tab` within a case or an alert
2. Click `New Notebook`
3. Edit blank notebook or use an existing template

![notebook_blank](/assets/operation_center/notebook_case.png){: style="max-width:100%"}

!!! Warning
    In a **multi-tenant** environment, notebooks are created in the **parent** workspace by default. They are not visible to child tenants unless you explicitly share the notebook with them.

### Basic Features
* Markdown syntax support
* Image attachment for evidence collection
* Multi datasources querying
* Investigation findings documentation
* Automations execution
* Real-time modifications saving

!!! Info
    Currently, Markdown table syntax is not supported.

### Tracking Changes
* Last modification date
* Last modification author

![notebook_changes](/assets/operation_center/notebook_changes.png){: style="max-width:100%"}

## Notebook Templates

### Template Management
Enhance incident response capabilities by creating template notebooks tailored to different threat types:

* Phishing investigations
* Malware analysis
* Intrusion containment
* Any custom threat responses

### Template Features
* Pre-defined investigation steps
* Threat tailored query templates
* Suggested remediation actions
* Guidance for analysts

### Setting Default Notebook Template For Cases/Alerts
1. Navigate to Notebook templates
2. Select desired template
3. Set as `default` for cases and alerts

The `default` notebook template will be suggested for use in cases and alerts, enabling the SOC team to standardize their response processes.

![notebook_template](/assets/operation_center/notebook_template.gif){: style="max-width:100%"}

### Template Creation Methods
* Create notebook template from scratch
* Convert existing notebook to template

![notebook_convert_template](/assets/operation_center/notebook_convert_template.gif){: style="max-width:100%"}

## Command Menu and Formatting

### Accessing the Command Menu
* Press the slash key (/) to open the Command menu
* Access notebook capabilities

![notebook_command](/assets/operation_center/notebook_command.gif){: style="max-width:100%"}

!!! Tip
    When the command menu is open, quickly search for an integration by typing its name.

### Available Commands
* Text formatting options
* Query builder insertion
* Automation insertion

![notebook_menu](/assets/operation_center/notebook_menu.png){: style="max-width:100%"}

### Query Builder Editor
* Display data in tables
* Create various data visualizations, including pie charts, line charts, bar charts, column charts, and numeric displays

![notebook_viz](/assets/operation_center/notebook_viz.png){: style="max-width:100%"}

## Sharing Notebooks

### Export notebook as PDF

Convert notebooks into PDF files to efficiently share incident, threat hunting, and KPI reports.

![notebook_share](/assets/operation_center/notebook_pdf.gif){: style="max-width:100%"}

### Multi-tenant support
* Individual notebook sharing
* Customer-specific reporting
* Secure information distribution

Share notebooks and templates directly with child tenants to ensure secure information distribution, provide incident reports, and share best practices with customers.

![notebook_share](/assets/operation_center/notebook_share.gif){: style="max-width:100%"}

## Notebook Management

### Organization
* Use the search bar to find notebooks by their titles

### Deletion and Recovery
* Soft delete notebooks to trash
* 30-day recovery period
* Permanent deletion after 30 days
* Restore option available

![notebook_share](/assets/operation_center/notebook_delete.gif){: style="max-width:100%"}

## Best Practices
1. Use templates for standardized investigations
2. Document all investigation steps
3. Include relevant screenshots and evidence
4. Utilize data visualization for complex data
5. Maintain consistent formatting
6. Regular template updates
7. Proper sharing permissions management
