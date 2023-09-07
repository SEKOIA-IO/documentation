# Definition of the taxomony

The taxonomy of [structured events](structured_event.md) is based on the [ECS](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) specifications. This taxonomy defines a set of fields available for values in [parsers](parser.md).

## Best Practices

- When a raw event encompasses a datetime, parse this information with a stage date and set the result in the field `@timestamp`
- Define `event.category`, `event.type` and `event.kind` according to the [event categorization fields](https://www.elastic.co/guide/en/ecs/current/ecs-category-field-values-reference.html)
- Define `event.category` and `event.type` as arrays
- If possible, define [`event.dataset`](https://www.elastic.co/guide/en/ecs/current/ecs-event.html#field-event-dataset)
- If possible, define observer information in [`observer.*`](https://www.elastic.co/guide/en/ecs/current/ecs-observer.html)
- For events collected from cloud services, provide cloud information in [`cloud.*`](https://www.elastic.co/guide/en/ecs/current/ecs-cloud.html) (The cloud account id must land in `cloud.account.id`)
- The name of an action must be hosted in `event.action`
- The reason of the event must be hosted in `event.reason`
- Error code and error message must land in `error.code` and `error.message`
- `email.to.address`, `email.from.address` and `email.cc.address` are arrays
- As documented in the ECS specification, [`host.hostname`](https://www.elastic.co/guide/en/ecs/current/ecs-host.html#field-host-hostname) must contain the hostname as return by the command **hostname** on the host. [`host.name`](https://www.elastic.co/guide/en/ecs/current/ecs-host.html#field-host-name) is more permissive

## Custom Taxomony

When a valuable information is present in the raw event, and no ECS fields is suitable to host the information, a custom field may be defined.

The custom taxonomy is defined in the directory `_meta/fields.yml` in the format. The document is written in [JSON](https://json.org) dialect.

### Custom field

!!! warning
	Please ensure that no field from the ECS taxonomy is suitable before creating a new field.

A custom field consists of three elements:

- name: The name of the field. It corresponds to the path (dot-notation) of the field in the [structured event](structured_event.md).

!!! note
    We recommend prefixing the field with the vendor and the name of the product (e.g for AWS cloud trail, custom taxonomy is prefixing with `aws.cloudtrail`).

- type: The type of the field.

	Available types are:

	- `keyword` for textual values
	- `boolean` for boolean values
	- `long` for integer and long values
	- `float` for float values
	- `array` for list
	- `dict` for dictionaries

- description: a short description to understand the value of the field

### Example

See [AWS CloudTrail](https://github.com/SEKOIA-IO/intake-formats/blob/main/AWS/aws-cloudtrail/_meta/fields.yml). 

