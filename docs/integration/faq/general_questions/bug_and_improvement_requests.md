# Difference Between a Bug and an Improvement Request

In this FAQ, we will clarify the distinction between a bug and an improvement request within the context of intakes and automations. Understanding this difference helps in categorizing and addressing issues effectively, ensuring smooth operation and timely enhancements.

## Glossary

- **Intake**: Refers to intake format, intake connector.
- **Automation**: Refers to trigger, action, playbook template, enricher.

## Bug Definition

In the context of an intake or automation, a bug is defined by the following categories and descriptions:

| Issue Category | Description |
| --- | --- |
| **Functional** | - Parsing produces an incorrect value<br>- Parsing fails unexpectedly and generates no error<br>- Automation execution does not fulfill its expected objective<br>- Incoming deprecation (with breaking change) of a feature currently supported by intake/automation |
| **Performance** | - The data ingestion lag exceeds **1h** on Sekoia’s side |
| **Standardization** | - Parsing is not compliant with the **ECS standard**<br>- Parsing is not aligned with other similar data sources which complicates detection rule patterns or query search |
| **Documentation** | - The documentation is missing information for the configuration of an intake/automation|

## Improvement Definition

In the context of an intake or automation, an improvement is defined by the following categories and descriptions:

| Issue Category | Description |
| --- | --- |
| **Functional** | - Request to add a new field to parse that is not in the ECS Required Fields <br>- Add a new trigger or action<br>- Expand the perimeter of existing intake/automation<br>- An integration has released a new version (with no breaking change) not supported by Sekoia<br>- An integration will be soon deprecated |
| **Performance** | - Improve intake consumption/cost, resilience, technical architecture |
| **Standardization** | - Implement new evolutions of ECS standard |
| **Documentation** | - Provide additional or complementary information on integration topics |

!!! Information
    Improvements are addressed at the discretion of our product strategy.

## Detailed Difference in Functional Category

In the functional category, distinguishing between a bug and an improvement request can sometimes be nuanced, particularly concerning the extraction of new fields in the context of an intake. Here is a more precise explanation:

- **Bug**: A new field extraction request will be considered a bug if the field is part of the list of ECS fields present in the sections "Required Fields" or "Required Fields depending on context" of the documentation pages found in the section "How to develop a new Integration" > "Formats" > "Best Practices". For instance:
    - For technologies of type Endpoints, see the [Required Fields](/integration/develop_integration/formats/best_practices/endpoints.md#required-fields).
    - For network technologies, see the [Required Fields](/integration/develop_integration/formats/best_practices/networks.md#required-fields).

- **Improvement**: A request to add a field that does not fall under the aforementioned mandatory ECS fields will be considered an improvement. This can include optional fields or new fields that enhance the functionality but are not strictly required by the ECS standard.
    - Clients have the flexibility to create custom formats to meet their specific needs. Additionally, they can be supported by our Professional Services team. Furthermore, clients can request the homologation of their custom format by following the process described in our documentation: [Homologate Your Custom Format in the SEKOIA Catalog](/integration/develop_integration/overview.md#step-3-homologate-your-custom-format-in-the-sekoia-catalog-optional)

Understanding whether an issue is a bug or an improvement request is crucial for effective problem resolution and enhancement planning. Should you encounter issues or have suggestions, please consult this guide and reach out to our support team if needed.
