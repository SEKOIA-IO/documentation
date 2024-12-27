# Notebooks (coming soon)

## Table of Contents
1. [Overview](#overview)
2. [Feature Benefits](#feature-benefits)
3. [Getting Started with Notebooks](#getting-started-with-notebooks)
4. [Creating and Managing Notebooks](#creating-and-managing-notebooks)
5. [Notebook Templates](#notebook-templates)
6. [Command Menu and Formatting](#command-menu-and-formatting)
7. [Sharing and Multi-tenant Support](#sharing-and-multi-tenant-support)
8. [Notebook Management](#notebook-management)

## Overview
Notebooks is a powerful documentation and investigation feature that allows SOC analysts to centralize their investigation queries, automation actions, and reporting in a single document. With support for markdown syntax and rich media, Notebooks streamlines the incident response process and facilitates team collaboration.

![notebook](/assets/operation_center/notebook.gif){: style="max-width:100%"}

## Feature Benefits
* Centralized incident response
* Rich text formatting with markdown support
* Embedded queries and automations
* Customizable templates for different threat types
* Standardized response processes
* Multi-tenant sharing capabilities
* PDF export

## Getting Started with Notebooks

### Types of Notebooks
**Standalone Notebooks**

* Independent notebooks for general use (threat hunting, reporting, KPI)
* Accessible from the Notebooks menu

**Context-linked Notebooks**

* Attached to specific alerts or cases for incident response use
* Provides centralized investigation context

## Creating and Managing Notebooks

### Creating a New Notebook
1. Navigate to the Notebooks menu
2. Click "New Notebook"
3. Edit the blank notebook or use an existing template

![notebook_blank](/assets/operation_center/notebook_case.png){: style="max-width:100%"}

### Basic Features
* Markdown syntax support
* Image attachment for evidence collection
* Multi datasources querying
* Investigation findings documentation
* Automations execution
* Real-time modifications saving

### Tracking Changes
* Last modification date displayed
* Author displayed

## Notebook Templates

### Template Management
Create templates for different threat types:

* Phishing investigations
* Malware analysis
* Intrusion detection
* Any custom threat responses

### Template Features
* Pre-defined investigation steps
* Suggested remediation actions
* Query templates
* Guidance for analysts

### Setting Default Templates
1. Navigate to Notebook templates
2. Select desired template
3. Set as default for alerts and cases

![notebook_template](/assets/operation_center/notebook_template.gif){: style="max-width:100%"}

### Template Creation Methods
* Create from scratch
* Convert existing notebook to template
* Modify existing template

## Command Menu and Formatting

### Accessing the Command Menu
* Press the slash key (/) to open
* Access notebook capabilities

![notebook_command](/assets/operation_center/notebook_command.gif){: style="max-width:100%"}

### Available Commands
* Text formatting options
* Query builder insertion
* Automation addition

### Query Builder Editor
* Display data in tables
* Create data visualizations: pie chart, line chart, bar chart, column chart, number

![notebook_viz](/assets/operation_center/notebook_viz.png){: style="max-width:100%"}

## Sharing and Multi-tenant Support

### Sharing Options
* Share notebooks or notebook templates with child tenants
* Export notebook as PDF

![notebook_share](/assets/operation_center/notebook_share.gif){: style="max-width:100%"}

### MSSP Features
* Individual notebook sharing
* Customer-specific reporting
* Secure information distribution

## Notebook Management

### Organization
* Search notebooks by title

### Deletion and Recovery
* Soft delete notebooks to trash
* 30-day recovery period
* Permanent deletion after 30 days
* Restore option available

## Best Practices
1. Use templates for standardized investigations
2. Document all investigation steps
3. Include relevant screenshots and evidence
4. Utilize data visualization for complex data
5. Maintain consistent formatting
6. Regular template updates
7. Proper sharing permissions management
