# How to write smart descriptions

An event can be hard to read as a raw data. To make the visualization and the understanding of events easier, smart descriptions help displaying important information to the user.

## Organization

Smart descriptions are defined in the directory `_meta/smart-descriptions.json` in the format. The document is written in [JSON](https://json.org) dialect.

The root element of the document is a JSON-array. This array contains a set of smart descriptions.

## Smart description components

A smart description consists of:

- The value (mandatory):

	A sentence that will display information from the [structured event](structured_event.md).

	This sentence contains placeholders (delimited with curly-braces). Each placeholder encompasses a path (dot-notation); the path indicates the location of the value in the structured event that is used to replace the placeholder in the description.

	e.g:
	With a structured event containing:

	```json
	{
	    "source": {
	        "ip": "1.2.3.4"
	    }
	}
	```

	The description `Connection from {source.ip}` will result in `Connection from 1.2.3.4`.

- A list of conditions (optional):

	These conditions define when the description should be displayed. For a same event, the description, with the largest number of matching conditions, will succeed.

	A condition is a compound of a path (dot-notation) to the field to test, and the expected value of the field (equal operation).

	e.g:
	With a structured event containing:

	```json
	{
	    "event": {
	      "kind": "alert"
	    }
	}
	```

	This condition will match

	```json
	{
	    "field": "event.kind",
	    "value": "alert"
	}
	```

	while the condition will not match

	```json
	{
	    "field": "event.kind",
	    "value": "event"
	}
	```


	To test the existence of a field in the structured event, define the field in the condition only.

	e.g:

	This condition 	will test the existence of `event.kind`:

	```json
	{
	    "field": "event.kind"
	}
	```


- A list of relationships (optional): The relationships help connect information from the structured event.

	A relationship is a compound of:

	- the source: the path to the field, in the structured data, to consider as the source of the relationship
	- the target: the path to the field, in the structured data, to consider as the target of the relationship
	- the type: a sentence that describes the nature of the relationship

	e.g:

	With a structured event containing:

	```json
	{
	    "source": {
	      "ip": "1.2.3.4"
	    },
	    "destination": {
	      "ip": "5.6.7.8"
	    }
	}
	```

	This relationship will connect `1.2.3.4` to `5.6.7.8` as a `was connected to` relation: 


	```json
	{
	    "source": "source.ip",
	    "target": "destination.ip",
	    "type": "was connected to"
	}
	```


## Example

See [Windows smart-descriptions](https://github.com/SEKOIA-IO/intake-formats/blob/main/Windows/windows/_meta/smart-descriptions.json).
