# Forward Logs to SEKOIA.IO From Logstash

If you are using Logstash as a log collector and/or parser, you can configure it to push your logs to Sekoia.io. This operation is done by using the “[Http output plugin][logstash-http-output-plugin]”, which is bundled into the default version of Logstash.

To push logs, you have to configure some filters in Logstash that will add the proper “intake key” considering your logs.

In the following example, we have multiple inputs to handle logs collected via Syslog (Apache HTTP Server and NGINX logs) and via Beats (Winlogbeat) and forward them to Sekoia.io. To filter in events, we are relying on Logstash tags. Make sure you update your intake key value by changing `CHANGE_ME_INTAKE_KEY` below. You can add as many “filters“ you want in the `filter` section.
Beats agents require a specific output configuration as we need to forward the complete JSON event to Sekoia.io.

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
