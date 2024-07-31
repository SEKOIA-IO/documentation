# Structured event

Parsers transform raw events into structured ones.

A structured event is a [JSON](https://json.org) document. The root of the document is a dictionary containing a set of objects.

The schema of this document is defined according to the [taxonomy](taxonomy.md) of the format. This taxonomy is based on the [ECS](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) specification and can be extended with the [custom taxonomy](taxonomy.md#custom-taxomony) of the format.
