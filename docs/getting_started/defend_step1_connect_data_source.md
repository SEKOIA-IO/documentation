---
title: "Step 1: Connect a data source"
description: "Create your first intake in Sekoia Defend to start collecting logs from a data source in your environment."
keywords: [intake, data source, connect, log collection, integration catalog, intake key, entity, push, pull]
audience: analyst
module: defend
type: task
---

# Step 1: Connect a data source

An intake is the connection between one of your data sources (a firewall, an EDR, a cloud service, etc.) and Sekoia Defend. Creating an intake tells Sekoia which technology is sending logs, how to parse them, and where to store them. This is the first step to getting events into the platform so that detection rules can start working.

## Before you begin

- You need the **Admin** role or a custom role with intake management permissions to create an intake.
- Identify at least one data source you want to connect. If you are unsure where to start, refer to the [best practices for intake configuration](docs/getting_started/best_practices.md) for recommendations on which sources to prioritize.

!!! note "No admin access?"
    If you do not have permission to create intakes, share this article with your administrator and ask them to create the intake. Once it is created, you can continue from [Step 2: Verify event reception](/getting_started/defend_step2_verify_event_reception.md).

## Understand intake types

Sekoia supports two types of intakes:

| Type | How it works | Example sources |
|---|---|---|
| **Push** | You configure your data source to forward logs to Sekoia using the intake key | Firewall via Syslog, Windows Event Forwarding |
| **Pull** | Sekoia connects to a source API and retrieves logs automatically | Microsoft 365, Okta, CrowdStrike |

For pull intakes, you start and stop collection using an On/Off toggle. For push intakes, you configure forwarding on your source side using the intake key.

## Create an intake

1. In the navigation menu, select **Configure > Intakes**.
2. On the top right corner, click **+ New Intake**.
3. In the integration catalog, search for your data source technology or browse by category.
4. Click **Create** on the matching integration card.
5. Enter a descriptive ***Name** for the intake (for example, `Windows Workstations - Paris Office`).
6. Select the **Entity** this intake belongs to. Entities help organize your data sources by infrastructure group or business unit.
7. Click **Create**.

For pull intakes, an additional configuration step appears. Enter the credentials or API parameters required to connect to the source.

> 📸 [SCREENSHOT SUGGESTION: The intake creation modal showing the name field, entity selector, and Create button. | ALT TEXT: Intake creation modal with fields for name and entity selection.]

## Copy and deploy the intake key

After creating the intake, Sekoia generates a unique **intake key** for this data source.

!!! warning "Copy the intake key now"
    The intake key is used to route incoming logs to this specific intake. You will need it to configure forwarding on your data source. Copy it before leaving this page.

To copy the intake key:

1. Click **...** on the intake card.
2. Select **Copy intake key**.

Deploy the intake key on your data source following the technology-specific setup guide available in the [integration catalog](https://docs.sekoia.io/integration/).

## What to expect after creating an intake

For **push intakes**, Sekoia starts receiving logs as soon as your data source begins forwarding them to the intake endpoint. No action is required in Sekoia after deploying the intake key.

For **pull intakes**, the intake is inactive by default. To start data collection, toggle the **On/Off** switch on the intake card to **On**.

## Related links

- [Step 2: Verify event reception](/getting_started/defend_step2_verify_event_reception.md) — Confirm that logs are arriving and being parsed correctly.
- [Integration catalog](https://docs.sekoia.io/integration/) — Technology-specific setup guides for each supported data source.
- [Notification system overview](/getting_started/notification_system_overview.md) — How to set up alerts when an intake stops receiving data.
