# How to forward logs to Sekoia.io from a third-party application using HTTPS

Many third-party applications have the ability to centralize events and forward them using HTTPS. Below, you can find some examples of usage. Please note that these solutions are not the official methods for sending logs to Sekoia.io.


## Logstash

If you are using Logstash as a log collector and/or parser, you can configure it to push your logs to Sekoia.io. This operation is done by using the “[Http output plugin][logstash-http-output-plugin]”, which is bundled into the default version of Logstash.

To push logs, you have to configure some filters in Logstash that will add the proper `intake key` considering your logs.

### Example

In the following example, we have multiple inputs to handle logs collected via Syslog (Apache HTTP Server and NGINX logs) and via [Beats (Winlogbeat)](../integrations/endpoint/winlogbeat.md) and forward them to Sekoia.io. 

In order to filter events effectively, Logstash uses tags as a key component. To ensure proper functionality, make sure to update the intake key value by editing the placeholder `CHANGE_ME_INTAKE_KEY` mentioned below. Additionally, you have the flexibility to incorporate multiple filters within the `filter` section as per your requirements.

!!! tip 
    By adding additional filters, you can enhance the filtering capabilities of Logstash and customize the processing of events to suit your requirements.

!!! note    
    Beats agents require a specific output configuration as you need to forward the complete JSON event to Sekoia.io.

```
input {
  beats {
    port => 5044
  }
  tcp {
    port => 514
  }
}

filter {
    # Edit this filter to adapt to your own needs.
    if "apache2" in [tags] {
        mutate {
            add_field => { "[@metadata][intake_key]" => "CHANGE_ME_INTAKE_KEY" }
        }
    }
    else if "nginx" in [tags] {
        mutate {
            add_field => { "[@metadata][intake_key]" => "CHANGE_ME_INTAKE_KEY" }
        }
    }
}

output {
    if "" in [@metadata][intake_key] {
        http {
            format => "json"
            http_method => "post"
            url => "https://intake.sekoia.io"
            mapping => {
                "@timestamp" => "%{@timestamp}"
                "json" => "%{message}"
                "intake_key" => "%{[@metadata][intake_key]}"
            }
        }
    }
    else if "winlogbeat" in [agent][type] {
        http {
            format => "json"
            http_method => "post"
            url => "https://intake.sekoia.io/plain"
            codec => "json_lines"
            headers => {
                "X-SEKOIAIO-INTAKE-KEY" => "CHANGE_ME_INTAKE_KEY"
                "X-SEKOIAIO-EVENT-TIMESTAMP" => "%{@timestamp}"
            }
        }
    }
}
```

### Advanced configuration

!!! warning
    This advanced configuration is provided as-is by Sekoia.io for experienced Logstash administrators. Sekoia.io will provide best effort support on this configuration.

The above configuration will send your logs one at a time (one HTTP request per log), this configuration will work for single pipeline / low log throughput.

For more advanced use cases, where you want to send logs to Sekoia.io and to an Elasticsearch instance for example, a more advanced Logstash configuration is recommended to achieve higher throughput. This configuration uses multiple pipelines and pipeline-to-pipeline communications to duplicate events and format them to the expected payload format required by Sekoia.io. Events will be sent in batch mode, providing better performance.

!!! note    
    Beats events do not need to be duplicated into a second pipeline as the complete JSON event is sent to Sekoia.io.

*pipelines.yml*
```
- pipeline.id: my-pipeline_1
  path.config: "/etc/path/to/p1.cfg"

- pipeline.id: my-other-pipeline
  path.config: "/etc/different/path/p2.cfg"

- pipeline.id: sekoiaio-apache2
  path.config: "/etc/path/to/sekoiaio-apache2.cfg"

- pipeline.id: sekoiaio-nginx
  path.config: "/etc/path/to/sekoiaio-nginx.cfg"
```

*p1.cfg*
```
input {
    beats {
        port => 5044
    }
}

output {
    elasticsearch {
        #Your elasticsearch configuration
    }

    if "winlogbeat" in [agent][type] {
        http {
            format => "json_batch"
            http_method => "post"
            url => "https://intake.sekoia.io/jsons"
            codec => "json_lines"
            headers => {
                "X-SEKOIAIO-INTAKE-KEY" => "CHANGE_ME_INTAKE_KEY"
            }
        }
    }
}
```

*p2.cfg*
```
input {
    tcp {
        port => 514
    }
}
output {
    if "apache2" in [tags] {
        elasticsearch {
            #Your elasticsearch configuration
        }
        pipeline {
            send_to => [sekoiaio-apache2]
        }
    }
    else if "nginx" in [tags] {
        elasticsearch {
            #Your elasticsearch configuration
        }
        pipeline {
            send_to => [sekoiaio-nginx]
        }
    }
}
```

*sekoiaio-apache2.cfg*
```
input {
    pipeline {
        address => sekoia-apache2
    }
}

filter {
    # When sending events in batch mode, we cannot choose in the output configuration which fields to send. We need to keep only the message field.
    prune {
      whitelist_names => ["^message$"]
    }
    # Rename the message field to json (expected field name by the HTTP endpoint) and add the intake key
    mutate {
      rename => { "message" => "json" }
      add_field => { "intake_key" => "CHANGE_ME_INTAKE_KEY_APACHE2" }
    }
}

output {
    http {
        format => "json_batch"
        http_method => "post"
        url => "https://intake.sekoia.io/array"
        codec => "json_lines"
    }
}
```

*sekoiaio-nginx.cfg*
```
input {
    pipeline {
        address => sekoia-nginx
    }
}

filter {
    # When sending events in batch mode, we cannot choose in the output configuration which fields to send. We need to keep only the message field.
    prune {
      whitelist_names => ["^message$"]
    }
    # Rename the message field to json (expected field name by the HTTP endpoint) and add the intake key
    mutate {
      rename => { "message" => "json" }
      add_field => { "intake_key" => "CHANGE_ME_INTAKE_KEY_NGINX" }
    }
}

output {
    http {
        format => "json_batch"
        http_method => "post"
        url => "https://intake.sekoia.io/array"
        codec => "json_lines"
    }
}
```

### External references

- [Logstash HTTP output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-http.html)
- [Logstash Multiple Pipelines](https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html)
- [Logstash Pipeline-to-pipeline communication](https://www.elastic.co/guide/en/logstash/current/pipeline-to-pipeline.html)



## Graylog

If you are using Graylog as a log collector, you can configure it to push your logs to Sekoia.io. This operation is done by using the “[HttpOutput Plugin for Graylog][graylog-http-plugin]”.

Prerequisites:

- Access to Sekoia.io
- Intake key(s) created
- Priviledge account on the Graylog server

### Installation procedure
1. Download the JAR file [here](https://github.com/SekoiaLab/graylog-http-plugin/releases/).
2. Copy the JAR file in your Graylog plugin directory.
3. Restart `graylog-server` and you are done.

If you want to generate yourself the JAR file :

1. Clone this repository “[HttpOutput Plugin for Graylog][graylog-http-plugin]”
2. Run `mvn package` to build a JAR file.
3. Copy generated JAR file in target directory to your Graylog plugin directory.
4. Restart `graylog-server` and you are done.

> The plugin directory is the `plugins/` folder relative from your `graylog-server` directory by default and can be configured in your `graylog.conf` file.

### Configuration of the log forwarding
#### Create a Stream for each Intake
For each of your Intake, you need to create a dedicated Stream.

1. Click on `Streams`
2. `Create Stream`
3. Give a title and a description for your stream, for instance : "Apache logs"


#### Rule and Pipeline creation
##### Create a rule
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

##### Create a pipeline
Now that you have one or more rules, you need to create a pipeline to apply them to your logs.

1. Go to `System/Pipelines`
2. Click on `Manage pipelines` > `Add new pipeline` and give it a name and a description
3. Click on `Edit connections` and select your logs input (by default `All messages`)
4. Click on `Add new stage`
	* Select `At least one of the rules on this stage matches the message`
	* Select your rule(s)
	* Click on `Save`

Your logs should now appear in your dedicated Stream.

#### Create a HTTP output for your events.

Now that you have your logs in your stream, you need to configure an Output to send your events to Sekoia.io

1. Go to `Streams`
2. Identify your stream and click on `More Actions` > `Manage Outputs`
3. Declare the output mode associated to the Sekoia.io stream with the type `com.plugin.HttpOutput` with the unique parameter `https://intake.sekoia.io` and your API key.

![image](/assets/operation_center/data_collection/ingestion_methods/graylog/graylog_output_declaration.png)

[graylog-http-plugin]: https://github.com/SekoiaLab/graylog-http-plugin
