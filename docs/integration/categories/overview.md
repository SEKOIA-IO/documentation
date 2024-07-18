# Intake Categories Overview

Welcome to the Intake Categories section of our documentation! This section provides an organized view of different intake categories used for log collection and processing purposes. Here, you'll find comprehensive guides and detailed information about various types of data sources, how to configure them, and best practices for ensuring seamless data ingestion.

## Structure of the Intake Categories Section

The Intake Categories section is organized into several sub-categories as explained in the [Best Practices for Using Sekoia SOC Platform page](getting_started/best_practices/), each representing a different type of data source. Below is the structure of the folder:

- **Applicative**: This category includes documentation on various application-level technologies  like Apache HTTP Server, Salesforce, JumpCloud.
- **Email**: Documentation related to email data sources can be found here.
- **Endpoint**: This category covers endpoint security solutions like EDR and host/system logs for Workstations and/or Servers.
- **Generic**: General and versatile data sources are documented in this category, like CEF format.
- **IAM / SASE**: Identity and Access Management (IAM) and Secure Access Service Edge (SASE) related technologies like MicroSoft EntraID, Okta, Wallix Bastion, OpenLDAP...
- **Network**: Documentation for network technologies like Squid, F5 BIG-IP, HAProxy or data sources such as Flow logs, HTTP requests, DHCP, DNS...
- **Network Security**: This category includes network security-specific data sources like WAF, Firewall, IDS, IPS, NDR...

Each category contains detailed pages for individual integrations.

## Standardized Page Structure for Integrations

!!! Note
    The standardisation is still in Work In Progress. Feel free to contribute to the effort by communicating inconstancies to the Support with your detailed written suggestions or the pull request link.

To ensure consistency and ease of use, each detailed page of an integration follows a standardized structure. This includes:

1. **Overview**: This section provides a high-level confirmation of what the technology does and whether it meets the customer's needs.
2. **High-Level Architecture Diagram**: When possible, a diagram is included to illustrate the architecture of the integration.
3. **Specifications**: Contains prerequisites, supported transport protocols/methods, and other technical details.
4. **Logs Details**: Information about the logs collected from the integration, including a sample of supported raw events.
5. **Step-by-Step Configuration Procedure**: Detailed instructions on how to set up and configure the integration.
6. **Detection**: Information on detection capabilities related to the integration with a list of built-in rules, and the list of extracted fields that can be used for creating your own custom rules or hunting activites.
7. **Further Readings**: Additional resources and links for further information.

## Coverage Score

To help assess the importance and extent of the integration within an enterprise, we introduce the concept of a Coverage Score:

| Coverage Score | Description |
| -------------- | ----------- |
| 1              | Technology installed on a few machines only. It has limited scope and is not used extensively in the enterprise. |
| 2              | Technology used in several parts of the enterprise, but not universally. It may cover specific departments or services. |
| 3              | Technology widely deployed and used across a significant portion of the enterprise. It covers many users or systems within the IT infrastructure. |
| 4              | Technology utilized by the majority of the IT infrastructure of the enterprise. It is essential and generally used by most employees and systems within the company. |

## Valuable Resources

To enhance your experience and keep you informed about our latest developments, we recommend exploring the following resources:

- **Integration Roadmap**: Stay updated on upcoming integrations and features by visiting our [Integration Roadmap](https://roadmap-integrations.sekoia.io/tabs/18-coming-next/tabs/5-under-consideration). Here, you can see what’s coming next.
- **Integrations Changelog**: Keep track of new integrations, improvements, and bug fixes with our [Integrations Changelog](https://changelog.sekoia.io/?type=t650d50f380b21).
- **Intake Catalog GitHub Repository**: Access our intake formats (Parser, Smart description, metadata, tests) and contribute to the project on GitHub. Check out the repository [here](https://github.com/SEKOIA-IO/intake-formats).