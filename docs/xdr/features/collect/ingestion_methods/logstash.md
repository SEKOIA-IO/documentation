# Forward logs to Sekoia.io from Logstash

If you are using Logstash as a log collector and/or parser, you can configure it to push your logs to Sekoia.io. This operation is done by using the “[Http output plugin][logstash-http-output-plugin]”, which is bundled into the default version of Logstash.

To push logs, you have to configure some filters in Logstash that will add the proper `intake key` considering your logs.

## Example

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

[logstash-http-output-plugin]: https://www.elastic.co/guide/en/logstash/current/plugins-outputs-http.html
