# Graylog

If you are using Graylog as a log collector, you can configure it to push your logs to Sekoia.io. This operation is done by using the “[HttpOutput Plugin for Graylog][graylog-http-plugin]”.

Prerequisites:

- Access to Sekoia.io
- Intake key(s) created
- Priviledge account on the Graylog server

## Installation procedure
1. Download the JAR file [here](https://github.com/SekoiaLab/graylog-http-plugin/releases/).
2. Copy the JAR file in your Graylog plugin directory.
3. Restart `graylog-server` and you are done.

If you want to generate yourself the JAR file :

1. Clone this repository “[HttpOutput Plugin for Graylog][graylog-http-plugin]”
2. Run `mvn package` to build a JAR file.
3. Copy generated JAR file in target directory to your Graylog plugin directory.
4. Restart `graylog-server` and you are done.

> The plugin directory is the `plugins/` folder relative from your `graylog-server` directory by default and can be configured in your `graylog.conf` file.

## Configuration of the log forwarding
### Create a Stream for each Intake
For each of your Intake, you need to create a dedicated Stream.

1. Click on `Streams`
2. `Create Stream`
3. Give a title and a description for your stream, for instance : "Apache logs"


### Rule and Pipeline creation
#### Create a rule
To route your logs to the stream you created, your need to create a Rule and a Pipeline.

1. Go to `System/Pipelines`
2. Click on `Manage Rules`, then `Create Rule`

Identify the source of logs to be routed to your stream
```
rule "route traffic to apache stream"
when
	has_field("source") AND
    to_string($message.source) == "<Hostname_Or_IP_Of_Your_Apache_Server>"
then
	route_to_stream("Apache logs");
end

```

> `$message.source` corresponds to the value of the field `Source` of your events you want to catch.
> You can find this value by looking an event you want in the `All messages` Stream and look at the `source` field.

#### Create a pipeline
Now that you have one or more rules, you need to create a pipeline to apply them to your logs.

1. Go to `System/Pipelines`
2. Click on `Manage pipelines` > `Add new pipeline` and give it a name and a description
3. Click on `Edit connections` and select your logs input (by default `All messages`)
4. Click on `Add new stage`
	* Select `At least one of the rules on this stage matches the message`
	* Select your rule(s)
	* Click on `Save`

Your logs should now appear in your dedicated Stream.

### Create a HTTP output for your events.

Now that you have your logs in your stream, you need to configure an Output to send your events to Sekoia.io

1. Go to `Streams`
2. Identify your stream and click on `More Actions` > `Manage Outputs`
3. Declare the output mode associated to the Sekoia.io stream with the type `com.plugin.HttpOutput` with the unique parameter `https://intake.sekoia.io/batch` and your intake key.

![image](/assets/operation_center/data_collection/ingestion_methods/graylog/graylog_output_declaration.png)

[graylog-http-plugin]: https://github.com/SekoiaLab/graylog-http-plugin
