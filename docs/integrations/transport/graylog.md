# Forward Logs to SEKOIA.IO From Graylog

If you are using Graylog as a log collector, you can configure it to push your logs to SEKOIA.IO. This operation is done by using the “[Http output plugin][https://github.com/SekoiaLab/graylog-http-plugin]”.

Prerequisites:

- Access to SEKOIA.IO
- Intake key(s) created
- Priviledge account on the Graylog server

## Installation procedure

1. Downloard the plugin
2. Clone this repository
3. Run `mvn package` to build a JAR file.
4. Copy generated JAR file in target directory to your Graylog plugin directory.
5. Restart `graylog-server` and you are done.

> The plugin directory is the `plugins/` folder relative from your `graylog-server` directory by default and can be configured in your `graylog.conf` file.

## Configuration of the log forwarding

### Pipeline creation

Add the intake key to a dedicated stream of logs towards SEKOIA.IO.

```
rule "add-key"
when
	true
then
	set_field("intake_key", "INSERT_HERE_YOUR_INTAKE_KEY");
end

```

> Change the value `INSERT_HERE_YOUR_INTAKE_KEY` by the relevant intake key.

### Activation of the HTTP output

Declare the output mode associated to the SEKOIA.IO stream with the type `com.plugin.HttpOutput` with the unique parameter `https://intake.sekoia.io`

![image](/assets/graylog_output_declaration.png)
