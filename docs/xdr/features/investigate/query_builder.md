# The Query Builder

Start exploring your data with the Query Builder. Hunt for threats, obtain analytics, and create insightful dashboards and reports. The Query Builder is a simple tool that allows you to build queries to explore your data effectively.

## Overview

With this form, you can aggregate data to extract new insights, helping you make informed decisions. Additionally, the Query Builder enables the visualization of data through various types of charts, enriching your reporting capabilities. 

![query builder](/assets/operation_center/events/qb-run.gif){: style="max-width:100%"}

Currently, the following data sources are available:

* **Alerts**: Monitor and analyze security alerts.
* **Events**: Query raw telemetry and logs.
* **Cases**: Analyze investigation workflows and case management metrics.

Future updates will introduce more sources to expand your investigation capabilities.

## Query modes

The Query Builder provides two distinct ways to interact with your data:

* **Form mode**: A wizard-like interface using dropdowns and buttons. It is ideal for quick explorations and users unfamiliar with query languages.
* **Code mode (Default)**: A powerful editor using **SOL (Sekoia.io Query Language)**. This mode allows for maximum precision, complex filtering, and advanced logic that the wizard might not cover.

## Key use cases

* **Threat hunting**: Search for specific indicators of compromise across your telemetry.
* **Security analytics**: Aggregate logs to identify patterns or anomalies in user behavior.
* **Operational reporting**: Power your dashboards with real-time queries to track SOC performance.

!!! warning

    Due to the important amount of logs ingested, the Query Builder has **rate limits** to protect the platform's health.

    There are 3 **rate limits**:

    1. **Maximum number of processed rows:** At the moment the maximum value is 10 000.
    2. **Maximum number of query:** 10 query executions are allowed per minute.
    3. **Query timeout:** A query will timeout automatically after 10 minutes.

    About the **maximum number of processed rows** limit, the Query Builder will display partial results in case this limit is reached.