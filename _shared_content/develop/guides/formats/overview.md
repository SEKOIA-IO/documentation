# Intake format

A format defines the steps to extract and transform useful information from events into structured and normalized events and make them understable to decision-making-process.

## Overview

Formats are grouped by module (a module usually correlates to a vendor).

### Module

A module contains:

- meta-information in the `_meta` directory
- as many sub-directories as there are formats

The `_meta` directory of a module hosts two files:

- the logo of the vendor
- a `manifest.yml` file with the UUID of the module, its name, a slug and a short description (cf [AWS](https://github.com/SEKOIA-IO/intake-formats/blob/main/AWS/_meta/manifest.yml) manifest)

### Formats

A format corresponds to a product.

Each format will have the same tree structure:

- meta-information in the `_meta` directory
- a parser (see [SkyHigh Secure WG](https://github.com/SEKOIA-IO/intake-formats/blob/main/SkyhighSecurity/skyhigh_secure_web_gateway/ingest/parser.yml))
- a set of testing files (see [SkyHigh Secure WG](https://github.com/SEKOIA-IO/intake-formats/tree/main/SkyhighSecurity/skyhigh_secure_web_gateway/tests))

The `_meta` directory consists of 4 files:

- a logo that represents the product
- a `manifest.yml` file with the UUID of the format, its name, a slug, a short description and data sources (see [Trend Micro Deep Security](https://github.com/SEKOIA-IO/intake-formats/blob/main/Trend%20Micro/deep-security/_meta/manifest.yml) manifest)
- a [taxonomy](taxonomy.md) file (e.g.: [Windows taxonomy](https://github.com/SEKOIA-IO/intake-formats/blob/main/Windows/windows/_meta/fields.yml))
- some smart-descriptions (e.g.: [Windows smart-descriptions](https://github.com/SEKOIA-IO/intake-formats/blob/main/Windows/windows/_meta/smart-descriptions.json))

## Definition of a parser

The parser is a set of instructions that schedules how information will be extracted from the raw event.

The parser is written in YAML format.

Refer to the [How to write a parser documentation](parser.md) to develop your own parser.

## Definition of smart descriptions

A smart description transforms a structured event into a readable description.

It may contain placeholders (`{<fieldname>}`) to display relevant information from the event (e.g. an IP address, a hostname, ….)

A smart description consists of:

- The description with placeholders
- A list of conditions when the smart description should be applied
    
    A condition is composed of a mandatory field name (property `field`) and a value (property `value`).
    With the presence of the value, the condition will test the content of the field against the value (like an `equal` operation). 
    
    The absence of the `value` property will test the existence of the field in the event.
    
- A list of relationships to link relevant information in the graph exploration
    
    A relationship relies on a `source`, a `target` and a word (`type`) to describe the relationship
    
Take a look at the [How to write smart-descriptions guide](smartdescriptions.md) for more details.
