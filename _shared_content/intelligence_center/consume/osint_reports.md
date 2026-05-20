# OSINT Reports

OSINT reports are publications from external sources, collected and made available directly in the platform. They cover ongoing campaigns, intrusion sets, attack techniques, and threat activity across sectors and geographies.

They complement the TDR-produced [FLINT reports](./flints.md) by bringing in third-party intelligence to broaden situational awareness.

## Overview

The Reports page lets you browse and explore external threat intelligence collected from curated sources. Sources are selected for their reliability and cover a wide range of industries, threat types, and languages.

Each report renders the original web publication directly in the platform. A text summary is available for most reports. Where available, reports are also linked to STIX objects and observables in the platform, allowing you to pivot from a report into your investigation workflows.

Sources are curated by the Sekoia team and include government CERTs, national cybersecurity agencies, security vendors, and independent research organizations. They publish in multiple languages and cover a broad spectrum of industries, threat actors, and attack techniques. <!-- TODO: add a representative list of sources -->

## How to access

Navigate to **Reports** in the left-hand menu. OSINT reports are listed alongside FLINTs and can be filtered independently using the filter bar.

## What you can do

### Read a report

Reports open in **PDF view** by default, rendering the original source article. You can:

- Zoom in and out to adjust readability.
- Switch to **text view** using the toggle at the top of the report to read a summary of the publication.
- Resize the report list panel on the left to give more space to the reading area.

!!! note
    The text view sometimes displays a summary, not a full transcription of the original article. Not all reports have a text version available.

### Filter reports using Feeds

You can scope the reports list to a specific feed to focus on the threat intelligence most relevant to your environment or use case. Select a feed from the filter bar at the top of the reports list to apply it.

Feeds can be configured to filter by source, sector, geography, and more. See [Feeds](../feeds.md) <!-- TODO: confirm path --> for instructions on how to create and configure a feed.

### Explore linked intelligence

Where applicable, reports are linked to STIX objects in the platform. From a report, you can:

- Click any **object or observable** in the report body to open its detail page.
- Click the **report title** to open the full Report detail page, listing all STIX objects and observables associated with that report.
- Open the **graph exploration** view to visualize relationships between the report's objects.
