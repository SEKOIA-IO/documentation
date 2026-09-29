# Route multiple technologies through one port

The Sekoia.io Forwarder normally maps one input port to one intake key. Use a custom rsyslog configuration when multiple technologies must send syslog events to the same port, such as the standard port `514`.

This procedure adds a shared listener, identifies each source from its syslog properties, and forwards matching events to the appropriate intake.

## Prerequisites

Before you start, make sure that:

- The Sekoia.io Forwarder is deployed. See [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md).
- You have an intake key for each technology.
- You can inspect the syslog messages sent by each source.
- You have access to the forwarder host with `sudo` privileges.

!!! warning "Do not declare the shared port twice"

    If a custom `.conf` file handles port `514`, do not declare port `514` in `intakes.yaml`. Declaring the same listener in both places prevents the container from starting.

## Add the shared port

1. Create the custom configuration directory:

    ````bash
    mkdir -p extended_conf
    ````

2. Add the shared TCP and UDP ports and the configuration volume to `docker-compose.yml`:

    ````yaml
    services:
      rsyslog:
        image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:latest
        environment:
          - MEMORY_MESSAGES=2000000
          - DISK_SPACE=180g
          - REGION=FRA1
        ports:
          - "20516-20566:20516-20566"
          - "20516-20566:20516-20566/udp"
          - "514:514"
          - "514:514/udp"
        volumes:
          - ./intakes.yaml:/intakes.yaml
          - ./extended_conf:/extended_conf
          - ./disk_queue:/var/spool/rsyslog
        restart: always
        pull_policy: always
    ````

3. Remove port `514` from `intakes.yaml` if it is present there.

## Identify a routing property

Inspect the raw messages arriving on the shared port before you write the routing rules.

````bash
sudo tcpdump -i any -c 100 -nn -A 'port 514' | grep "LOG"
````

Choose a property that uniquely identifies each technology.

| Property | Description | Typical use |
| --- | --- | --- |
| `$fromhost-ip` | Source IP as seen by the forwarder. | Network appliances with fixed source addresses. |
| `$hostname` | Hostname declared in the syslog header. | Devices that use a stable hostname pattern. |
| `$syslogtag` | Application or program name. | Products that use a distinctive tag, such as `%ASA-`. |
| `$app-name` | RFC 5424 application name. | RFC 5424 senders with a distinctive application name. |
| `$msg` | Log message body. | A fallback when no header property identifies the source. |

For example, this message contains the hostname `windows-vm-0` and the application name `Microsoft-Windows-Sysmon`:

````text
<13>1 2026-05-07T09:49:31.308+00:00 windows-vm-0 Microsoft-Windows-Sysmon[3524] - LOG {"EventTime":"2022-09-16 12:39:18", [...] }
````

The corresponding rsyslog properties are:

| Value | Rsyslog property | Description |
| --- | --- | --- |
| `windows-vm-0` | `$hostname` | Hostname declared in the syslog header. |
| `Microsoft-Windows-Sysmon` | `$app-name` | RFC 5424 application name. |
| `3524` | `$procid` | Process ID reported by the sender. |

Use an exact match when possible:

````text
if ($hostname isequal "windows-vm-0") then { ... }
````

Use `$app-name` when you want to match all sources that use the same application name:

````text
if ($app-name isequal "Microsoft-Windows-Sysmon") then { ... }
````

For the complete property list, see the [rsyslog properties documentation](https://docs.rsyslog.com/doc/configuration/properties.html).

The supported string comparison operators are:

| Operator | Behavior |
| --- | --- |
| `isequal` | Exact, case-sensitive match. |
| `contains` | Case-sensitive substring match. |
| `contains_i` | Case-insensitive substring match. |
| `startswith` | Case-sensitive prefix match. |

## Create the routing configuration

Create `extended_conf/port514.conf`. Define a template for each intake, an input and ruleset for each protocol, and a fallback action for unmatched messages.

!!! warning "Do not load the input modules"

    The forwarder already loads `imtcp` and `imudp`. Do not add `module(load="imtcp")` or `module(load="imudp")` to this file.

!!! note "Use unique action names"

    Add a protocol suffix such as `_tcp` or `_udp` to every action name. This prevents name collisions between rulesets.

The following example routes Palo Alto, Cisco ASA, and Cisco switch events. Replace the example intake keys and source conditions with values from your environment.

````text
# Templates
 template(name="Tmpl_PaloAlto" type="string"
     string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-PALOALTO\"] %msg%\n")

 template(name="Tmpl_CiscoASA" type="string"
     string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CISCO-ASA\"] %msg%\n")

 template(name="Tmpl_CiscoSwitch" type="string"
     string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CISCO-SWITCH\"] %msg%\n")

 template(name="Tmpl_CatchAll" type="string"
     string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CATCHALL\"] %msg%\n")

# TCP listener
 input(type="imtcp" port="514" ruleset="remote514tcp")

 ruleset(name="remote514tcp") {
     if ($fromhost-ip isequal "192.168.10.5") then {
         action(
             name="fwd_paloalto_tcp"
             type="omfwd" protocol="tcp"
             target="intake.sekoia.io" port="10514"
             TCP_Framing="octet-counted"
             StreamDriver="gtls" StreamDriverMode="1"
             StreamDriverAuthMode="x509/name"
             StreamDriverPermittedPeers="intake.sekoia.io"
             Template="Tmpl_PaloAlto"
         )
         stop
     }
     if ($syslogtag startswith "%ASA-") then {
         action(
             name="fwd_ciscoasa_tcp"
             type="omfwd" protocol="tcp"
             target="intake.sekoia.io" port="10514"
             TCP_Framing="octet-counted"
             StreamDriver="gtls" StreamDriverMode="1"
             StreamDriverAuthMode="x509/name"
             StreamDriverPermittedPeers="intake.sekoia.io"
             Template="Tmpl_CiscoASA"
         )
         stop
     }
     action(
         name="fwd_catchall_tcp"
         type="omfwd" protocol="tcp"
         target="intake.sekoia.io" port="10514"
         TCP_Framing="octet-counted"
         StreamDriver="gtls" StreamDriverMode="1"
         StreamDriverAuthMode="x509/name"
         StreamDriverPermittedPeers="intake.sekoia.io"
         Template="Tmpl_CatchAll"
     )
 }

# UDP listener
 input(type="imudp" port="514" ruleset="remote514udp")

 ruleset(name="remote514udp") {
     if ($hostname startswith "sw-") then {
         action(
             name="fwd_ciscoswitch_udp"
             type="omfwd" protocol="tcp"
             target="intake.sekoia.io" port="10514"
             TCP_Framing="octet-counted"
             StreamDriver="gtls" StreamDriverMode="1"
             StreamDriverAuthMode="x509/name"
             StreamDriverPermittedPeers="intake.sekoia.io"
             Template="Tmpl_CiscoSwitch"
         )
         stop
     }
     action(
         name="fwd_catchall_udp"
         type="omfwd" protocol="tcp"
         target="intake.sekoia.io" port="10514"
         TCP_Framing="octet-counted"
         StreamDriver="gtls" StreamDriverMode="1"
         StreamDriverAuthMode="x509/name"
         StreamDriverPermittedPeers="intake.sekoia.io"
         Template="Tmpl_CatchAll"
     )
 }
````

The example uses the FRA1 endpoint. Replace both `target` and `StreamDriverPermittedPeers` with the host for your region.

The `stop` directive prevents a matched message from being evaluated by later rules. Without it, one message can be sent to more than one intake.

TCP and UDP use separate rulesets because an rsyslog `input()` can be bound to only one ruleset.

## Apply and verify the configuration

1. Recreate the forwarder:

    ````bash
    sudo docker compose up -d
    ````

2. Check the container logs:

    ````bash
    sudo docker compose logs rsyslog | head -100
    ````

3. Send a test event from each source and confirm that it reaches the expected intake.

## Troubleshoot routing

### Events reach the wrong intake

Capture the raw message again and compare its actual properties with the conditions in `port514.conf`. Check the capitalization of each value. Use `contains_i` while testing if the source changes capitalization.

Confirm that every matched action is followed by `stop`.

### Verify a rule with a temporary file output

Add a temporary `omfile` action before the forwarding action:

````text
module(load="omfile")

if ($fromhost-ip isequal "192.168.10.5") then {
    action(
        name="debug_paloalto_tcp"
        type="omfile"
        file="/tmp/debug-paloalto.log"
    )
    action(
        name="fwd_paloalto_tcp"
        ...
    )
    stop
}
````

Read the file from the host:

````bash
sudo docker compose exec rsyslog tail -f /tmp/debug-paloalto.log
````

!!! warning "Remove temporary file outputs"

    The file is stored inside the container, is not persistent, and continues to consume disk space until you remove the action.

### The container does not start

Check the rsyslog output:

````bash
sudo docker compose logs rsyslog | head -100
````

| Cause | Fix |
| --- | --- |
| Syntax error in the `.conf` file. | Check parentheses and directive names. |
| Shared port also declared in `intakes.yaml`. | Remove the shared port from `intakes.yaml`. |
| `imtcp` or `imudp` loaded in the custom file. | Remove the module declarations. |
| Duplicate action name. | Give each action a unique name. |

## Related articles

- [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md): How to deploy the standard port-to-intake configuration.
- [Secure forwarder inputs with TLS](/integration/ingestion_methods/syslog/secure_forwarder_inputs_with_tls.md): How to encrypt traffic between sources and the forwarder.
- [Troubleshoot the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/troubleshoot_the_sekoiaio_forwarder.md): How to investigate missing events and connection failures.
