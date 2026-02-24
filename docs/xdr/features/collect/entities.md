# Entities
An entity is an organizational unit mostly used for configuration and reporting easiness.
Entities allow a logical grouping of your data sources and the associated alerts. It can be a company site, network zone, or any other grouping that you think is relevant.

An entity is denoted by a number of fields:

- a name
- an entity ID
- a description
- a default alert generation mode

All fields of entities are editable and mandatory.

### Alert generation mode
The **Alert generation mode** affects the alert processing workflow. There are two generation modes:

- `automatic`: for which the alerts proceed to the status `Ongoing` immediately after their creation
- `manual`: for which the alerts remain in the status `Pending` until a manual action.

## Entities listing

On the listing page of entities, you can find:

- Name of all your entities
- A description for each entity
- The number of intakes linked to each entity

Under the entity details, you will find the associated data sources.

!!! Note
    To activate a new intake for your entity, please refer to the [intakes](intakes.md) documentation.

## Create an entity
To create a new entity:

1. Go the the Entities page in the menu
2. Click on the `+ New Entity` button
3. Give your entity a name, an entity ID and a description. All these fields are mandatory
4. Choose your Alert generation mode (A default value for alert generation mode is defined for each entity but can be overridden in each detection rule)
5. Save your settings

## Entity details
On the details view of an entity, you can find:

- The name of the entity
- A description of the entity
- A table that lists all intakes related to this entity

This detailed view allows you to edit the entity or delete it if needed.
You can also add [intakes](intakes.md) to it by clicking on the `+ Add Intake` button on the upper right side of the table.

!!! Note
    One entity can have as many intakes in different formats as it requires.
