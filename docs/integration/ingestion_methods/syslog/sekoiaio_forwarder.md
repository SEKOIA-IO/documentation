# Sekoia.io Forwarder

The Sekoia.io Forwarder is a preconfigured collector and concentrator based on Docker. It collects events from multiple sources and forwards them to the correct intakes on the Sekoia.io platform. Each technology sends its logs to a dedicated port on the concentrator, which maps that port to the corresponding intake key.

!!! warning "Port isolation required"
    Each technology must send its logs to a distinct port on the concentrator. The forwarder uses port numbers to route events to the correct intake key.

Find the English tutorial video below. A French version is also available [here](https://youtu.be/CSEG2flmffE){:target="_blank"}.

[![Sekoia.io Forwarder tutorial](https://img.youtube.com/vi/BwydQiWMlv0/0.jpg)](https://youtu.be/BwydQiWMlv0){:target="_blank"}

## Prerequisites

Before deploying the forwarder, verify the following:

- A x86-64 Linux host matching one of the templates below
- Last version of Docker Engine installed (see [Docker Engine installation](#docker-engine-installation))
- Inbound TCP or UDP flows open between your log sources and the concentrator on the ports you choose
- Outbound TCP flow open toward the relevant [regional host](#regional-hosts) on port `10514`

**Host sizing recommendations**

| Number of assets | vCPUs | RAM (GB) | Disk size (GB) | MEMORY_MESSAGES | DISK_SPACE |
|------------------|:-----:|:--------:|:--------------:|:---------------:|:----------:|
| 1,000 | 2 | 4 | 200 | 2,000,000 | 180g |
| 10,000 | 4 | 8 | 1,000 | 5,000,000 | 980g |
| 50,000 | 6 | 16 | 5,000 | 12,000,000 | 4,980g |

!!! note "Sizing context"
    These values are based on observed averages on Sekoia.io and may vary depending on your use case. Disk type (SSD or HDD) does not affect forwarder performance, though SSD improves recovery speed when catchup is needed.

## Regional hosts

Select the host address that matches your Sekoia.io region:

| Region | Host address | Port |
|--------|-------------|------|
| FRA1 | `intake.sekoia.io` | `10514` |
| FRA2 | `intake.fra2.sekoia.io` | `10514` |
| MCO1 | `intake.mco1.sekoia.io` | `10514` |
| UAE1 | `intake.uae1.sekoia.io` | `10514` |
| USA1 | `intake.usa1.sekoia.io` | `10514` |

## Configure the concentrator

The concentrator requires two configuration files: `docker-compose.yml` and `intakes.yaml`.

### Step 1 - Create the working directory

```bash
mkdir sekoiaio-concentrator && cd sekoiaio-concentrator
```

### Step 2 - Create the configuration files

```bash
touch docker-compose.yml && touch intakes.yaml
```

### Step 3 - Configure intakes.yaml

The `intakes.yaml` file maps each listening port to an intake key and its associated technology. For each entry, define:

| Field | Description |
|-------|-------------|
| `name` | A label of your choice. Not used by Sekoia.io. |
| `protocol` | `tcp`, `udp`, or `tls` |
| `port` | The port on which the concentrator listens for this technology |
| `intake_key` | The intake key retrieved from the **Intakes** page of your community |

??? example "intakes.yaml with three technologies"

    ```yaml
    ---
    intakes:
    - name: Techno1
      protocol: tcp
      port: 20516
      intake_key: INTAKE_KEY_FOR_TECHNO_1
    - name: Techno2
      protocol: udp
      port: 20517
      intake_key: INTAKE_KEY_FOR_TECHNO_2
    - name: Techno3
      protocol: tcp
      port: 20518
      intake_key: INTAKE_KEY_FOR_TECHNO_3
    ```

#### Enable per-intake debug logging

To print raw received events and output messages to STDOUT for a specific intake, add `debug: True` to its entry. Each log line is tagged with `[Input INTAKE_KEY]` or `[Output INTAKE_KEY]`.

??? example "intakes.yaml with debug enabled on Techno2"

    ```yaml
    ---
    intakes:
    - name: Techno1
      protocol: tcp
      port: 20516
      intake_key: INTAKE_KEY_FOR_TECHNO_1
    - name: Techno2
      protocol: tcp
      port: 20517
      intake_key: INTAKE_KEY_FOR_TECHNO_2
      debug: True
    - name: Techno3
      protocol: tcp
      port: 20518
      intake_key: INTAKE_KEY_FOR_TECHNO_3
    ```

#### Set a custom queue size per intake

By default, the memory queue is distributed across all intakes (`MEMORY_MESSAGES` divided by the number of intakes). For example, if 10 intakes are configured, each queue has a retention capacity of `MEMORY_MESSAGES / 10` messages. To override this for a specific intake, add `queue_size`:

```yaml
- name: Techno1
  protocol: tcp
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
  queue_size: 100000
```

!!! note "Effect on other intakes"
    Intakes without an explicit `queue_size` retain the default value calculated from `MEMORY_MESSAGES`.

### Step 4 - Configure docker-compose.yml

??? example "docker-compose.yml template"

    ```yaml
    services:
      rsyslog:
        image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:2.7.2
        environment:
          - MEMORY_MESSAGES=2000000
          - DISK_SPACE=180g
          - REGION=FRA1
        ports:
          - "20516-20566:20516-20566"
          - "20516-20566:20516-20566/udp"
        volumes:
          - ./intakes.yaml:/intakes.yaml
          - ./disk_queue:/var/spool/rsyslog
        restart: always
        pull_policy: always
    ```

#### Environment variables

| Variable | Status | Description |
|----------|--------|-------------|
| `MEMORY_MESSAGES` | Recommended | Maximum number of messages stored in memory across all queues. Example: `2,000,000 × 1.2 KB = 2.4 GB` of RAM. |
| `DISK_SPACE` | Recommended | Total disk space allocated to on-disk queues across all intakes. |
| `REGION` | Required | Target region. Accepted values: `FRA1`, `FRA2`, `MCO1`, `UAE1`, `USA1`. |
| `RELP_OUTPUT` | Optional | Set to `True` to send logs via RELP instead of the default TCP syslog mode. |

#### Ports

The `ports` section exposes the concentrator's listening ports to the host network. Each entry follows the format `HOST_PORT:CONTAINER_PORT`. Add `/udp` for UDP flows.

!!! warning "Keep ports in sync"
    The port ranges declared here must match exactly the ports defined in `intakes.yaml`. Mismatches will silently drop traffic.

#### Volumes

| Mount | Purpose |
|-------|---------|
| `./intakes.yaml:/intakes.yaml` | Injects your intake configuration into the container |
| `./disk_queue:/var/spool/rsyslog` | Persists on-disk queues to the host, preventing data loss if the container is recreated |
| `./certs:/certs` | Required when using TLS (see [Configure TLS for an intake](#configure-tls-for-an-intake)) |
| `./extended_conf:/extended_conf` | Mounts custom rsyslog configuration files (see [Import a custom rsyslog configuration](#import-a-custom-rsyslog-configuration)) |

#### Restart and pull policy

| Option | Value | Effect |
|--------|-------|--------|
| `restart` | `always` | Automatically restarts the concentrator after a crash, a Docker restart, or a host reboot |
| `pull_policy` | `always` | Checks for a newer image at every `docker compose up` |

### Step 5 - Start the concentrator

Run the following command from the directory containing `docker-compose.yml` and `intakes.yaml`:

```bash
sudo docker compose up -d
```

To verify the concentrator is running:

```bash
sudo docker compose ps
```

!!! note "First startup"
    On first run, Docker downloads the image from `ghcr.io/sekoia-io/sekoiaio-docker-concentrator`. This requires an outbound internet connection.

## Import a custom rsyslog configuration

You can extend the concentrator with additional rsyslog configuration files to handle use cases not natively supported, such as custom input modules or advanced parsing.

To do so, create an `extended_conf` directory and place `.conf` files inside it:

```bash
mkdir extended_conf
```

Then mount it in `docker-compose.yml`:

```yaml
volumes:
    - ./intakes.yaml:/intakes.yaml
    - ./extended_conf:/extended_conf
    - ./disk_queue:/var/spool/rsyslog
```

!!! warning "Do not declare the same port twice"
    If a port or input is defined in a `.conf` file inside `extended_conf`, do not declare it again in `intakes.yaml`. Duplicate bindings will prevent the concentrator from starting.

When writing custom configurations, forward events to Sekoia.io using the following template structure, replacing `MY-APP-NAME` and `MY-INTAKE-KEY` with your values:

```
input(type="imtcp" port="20521" ruleset="remote20521")

template(name="SEKOIAIO_Template" type="string"
    string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% MY-APP-NAME - LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY\"] %msg%\n")

ruleset(name="remote20521"){
    action(
        name="action"
        type="omfwd"
        protocol="tcp"
        target="intake.sekoia.io"
        port="10514"
        TCP_Framing="octet-counted"
        StreamDriver="gtls"
        StreamDriverMode="1"
        StreamDriverAuthMode="x509/name"
        StreamDriverPermittedPeers="intake.sekoia.io"
        Template="SEKOIAIO_Template"
    )
}
```

## Route multiple technologies on a single port

Some network appliances cannot be reconfigured to send syslog to a custom port. When several technologies are hardcoded to the same destination port (for example, the standard port `514`), the one-port-per-intake approach in `intakes.yaml` is not applicable.

The solution is to write a custom rsyslog configuration that inspects each incoming message's properties and routes it to the correct intake.

!!! warning "Do not declare the shared port in intakes.yaml"
    If port `514` is handled by a custom `.conf` file, it must not appear in `intakes.yaml`. Declaring it in both places will cause a startup failure.

### Step 1 - Update docker-compose.yml

Add the shared port mapping and the `extended_conf` volume mount:

```yaml
services:
  rsyslog:
    image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:2.7.2
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
```

Create the `extended_conf` directory if it does not exist:

```bash
mkdir -p extended_conf
```

### Step 2 - Identify a discriminating property

Before writing routing rules, inspect the raw syslog messages arriving on the shared port to identify a property that uniquely identifies each technology.

To capture live traffic on the forwarder host:

```bash
sudo tcpdump -i any -c 100 -nn -A 'port 514' | grep "LOG"
```

The following rsyslog properties are available for routing decisions:

| Property | Description | Typical use |
|----------|-------------|-------------|
| `$fromhost-ip` | Source IP as seen by the forwarder | Most reliable for network appliances |
| `$hostname` | Hostname declared in the syslog header | Identify a device by its declared name |
| `$syslogtag` | Application or program name | Identify a specific product (e.g., `%ASA-`) |
| `$app-name` | RFC 5424 application name field | Similar to `$syslogtag` for RFC 5424 senders |
| `$msg` | The log message body | Last resort when no header property is distinctive |

??? example "Reading a syslog header: Windows Sysmon example"

    Consider the following raw syslog message:

    ```
    <13>1 2026-05-07T09:49:31.308+00:00 windows-vm-0 Microsoft-Windows-Sysmon[3524] - LOG {"EventTime":"2022-09-16 12:39:18", [...] }
    ```

    The syslog header fields map to rsyslog properties as follows:

    | Value in the message | rsyslog property | Notes |
    |----------------------|-----------------|-------|
    | `windows-vm-0` | `$hostname` | The hostname declared by the sender in the syslog header |
    | `Microsoft-Windows-Sysmon` | `$app-name` | The RFC 5424 application name field |
    | `3524` | `$procid` | The process ID reported by the sender |

    To route all logs from this host to a Windows Sysmon intake, you could use either:

    ```
    if ($hostname isequal "windows-vm-0") then { ... }
    ```

    or, to match all Sysmon sources regardless of hostname:

    ```
    if ($app-name isequal "Microsoft-Windows-Sysmon") then { ... }
    ```

For a complete property reference, see the [rsyslog properties documentation](https://docs.rsyslog.com/doc/configuration/properties.html).

!!! tip "Finding the right discriminant"
    Use `tcpdump` from the forwarder host to inspect raw syslog frames. Because Docker exposes the port on the host network interface, the capture works without entering the container. Typical choices: a firewall sending from a known IP uses `$fromhost-ip`; a VPN concentrator announcing a specific app name uses `$syslogtag`; a switch always sending with a hostname convention uses `$hostname`.

Rsyslog `if` conditions support the following string comparison operators:

| Operator | Behavior |
|----------|----------|
| `isequal` | Exact match (case-sensitive) |
| `contains` | Substring match (case-sensitive) |
| `contains_i` | Substring match (case-insensitive) |
| `startswith` | Prefix match (case-sensitive) |

### Step 3 - Create the routing configuration file

Create `extended_conf/port514.conf`. The file must define one template per technology, one `input()` per protocol, one ruleset per protocol, and a fallback action for unmatched logs.

!!! warning "Do not load imtcp or imudp in this file"
    These modules are already loaded by the concentrator. Adding `module(load="imtcp")` or `module(load="imudp")` will cause a startup error.

!!! warning "Action names must be unique"
    Use suffixes such as `_tcp` and `_udp` to avoid name collisions with other rulesets.

??? example "port514.conf routing Palo Alto, Cisco ASA, and Cisco Switch"

    ```
    # --- Templates: one per technology ---
    template(name="Tmpl_PaloAlto" type="string"
        string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-PALOALTO\"] %msg%\n")

    template(name="Tmpl_CiscoASA" type="string"
        string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CISCO-ASA\"] %msg%\n")

    template(name="Tmpl_CiscoSwitch" type="string"
        string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CISCO-SWITCH\"] %msg%\n")

    template(name="Tmpl_CatchAll" type="string"
        string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY-CATCHALL\"] %msg%\n")

    # --- TCP listener ---
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

    # --- UDP listener ---
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
    ```

!!! note "Why stop is required"
    The `stop` directive prevents a matched log from being evaluated by subsequent rules. Without it, a single message could be forwarded to multiple intakes simultaneously.

!!! note "TCP and UDP require separate rulesets"
    An rsyslog `input()` can only be bound to one ruleset. The routing logic is intentionally duplicated between `remote514tcp` and `remote514udp`.

!!! note "Regional host"
    The examples above use `intake.sekoia.io` (FRA1). Adapt the `target` and `StreamDriverPermittedPeers` values to match your region.

### Step 4 - Reload the forwarder

Apply the new configuration:

```bash
sudo docker compose up -d
```

Verify the container started without errors:

```bash
sudo docker compose logs | head -50
```

A syntax error in the `.conf` file will appear here and may prevent the container from starting.

### Troubleshoot routing issues

**Logs are not routed to the expected intake**

Re-run the `tcpdump` capture and compare the actual syslog header values with the conditions in your `.conf` file. A common cause is a case mismatch. Use `contains_i` for case-insensitive matching while debugging.

Verify that `stop` is present after each matched action.

**Temporarily verify routing with a file output**

Add a file output action before the forwarding action to confirm a rule is matching:

```
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
```

To read the file from the host:

```bash
sudo docker compose exec rsyslog tail -f /tmp/debug-paloalto.log
```

!!! warning "Remove debug actions before going to production"
    File output inside the container is not persistent and will consume disk space indefinitely.

**The container fails to start after adding the .conf file**

Check the rsyslog error output:

```bash
sudo docker compose logs rsyslog | head -100
```

Common causes:

| Cause | Fix |
|-------|-----|
| Syntax error in the `.conf` file | Check for missing parentheses or unknown directives |
| Shared port also declared in `intakes.yaml` | Remove it from `intakes.yaml` |
| `module(load="imtcp")` or `module(load="imudp")` present in `.conf` | Remove those lines |
| Two actions share the same `name=` value | Rename one of them |

## Configure TLS for an intake

By default, logs between your devices and the forwarder are not encrypted, even when using `tcp` or `udp`. This section shows how to enable TLS on a specific intake.

Logs between the forwarder and Sekoia.io are always encrypted with TLS regardless of this setting.

### Step 1 - Generate a key and certificate

Create the `certs` directory and navigate to it:

```bash
mkdir certs && cd certs
```

Install OpenSSL if it is not already present:

=== "Debian, Ubuntu"

    ```bash
    sudo apt update && sudo apt install -y openssl
    ```

=== "Fedora, Red Hat, CentOS (yum)"

    ```bash
    sudo yum update && sudo yum install -y openssl
    ```

=== "Fedora, Red Hat, CentOS (dnf)"

    ```bash
    sudo dnf update && sudo dnf install -y openssl
    ```

Generate a self-signed certificate valid for 5 years:

```bash
openssl req -x509 \
    -sha256 -days 1825 \
    -nodes \
    -newkey rsa:4096 \
    -keyout server.key -out server.crt
```

Set restrictive permissions on the generated files:

```bash
chmod 600 server.key server.crt
```

### Step 2 - Mount the certs volume

Add the following line to the `volumes` section of `docker-compose.yml`:

```yaml
volumes:
    - ./certs:/certs
    - ./intakes.yaml:/intakes.yaml
    - ./disk_queue:/var/spool/rsyslog
```

### Step 3 - Update intakes.yaml

Set the protocol to `tls` for the relevant intake:

```yaml
- name: Techno1
  protocol: tls
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
```

By default, the forwarder reads the key and certificate from `/certs/server.key` and `/certs/server.crt`. To use different filenames, specify them explicitly:

```yaml
- name: Techno1
  protocol: tls
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
  tls_key_name: server
  tls_cert_name: server
  tls_ca_name: server
```

## Monitor the concentrator

The forwarder transmits health metrics to Sekoia.io, allowing you to create detection rules for conditions such as queue saturation or service interruptions.

### Step 1 - Create the forwarder logs intake

Create a dedicated intake on the Sekoia.io platform. Refer to the [Sekoia.io Forwarder Logs integration documentation](/integration/categories/applicative/sekoiaio_forwarder_logs.md) for detailed instructions. Save the associated intake key.

### Step 2 - Enable monitoring in intakes.yaml

Add a monitoring entry with `stats: True`:

```yaml
---
intakes:
- name: Monitoring
  stats: True
  intake_key: INTAKE_KEY_FOR_FORWARDER_LOGS
```

!!! note "No port required"
    This intake is auto-generated by the forwarder. You do not need to define a port or protocol.

### Understanding concentrator metrics

The concentrator uses the rsyslog [impstats module](https://www.rsyslog.com/doc/configuration/modules/impstats.html) to generate internal metrics. One set of metrics is produced per configured intake, identified by a dedicated name.

> 📸 [SCREENSHOT SUGGESTION: The forwarder monitoring metrics diagram showing per-intake metric names. | ALT TEXT: Diagram showing rsyslog metric names per intake in the Sekoia.io forwarder.]

The following detection rule pattern identifies full queues, which may lead to log loss:

```yaml
detection:
  selection:
    - sekoiaio.forwarder.queue.discarded.full|gt: 0
    - sekoiaio.forwarder.queue.discarded.nf|gt: 0
    - sekoiaio.forwarder.queue.full|gt: 0
  condition: selection
```

For the full list of available counters, refer to the [rsyslog statistic counter documentation](https://www.rsyslog.com/doc/configuration/rsyslog_statistic_counter.html).

### Retrieve local metrics during an outage

When the forwarder cannot send metrics to Sekoia.io (for example, due to a full queue), a raw copy of the metrics is retained locally inside the container. To extract it to the host:

```bash
sudo docker compose cp rsyslog:/var/log/rsyslog-stats.log rsyslog-stats.log
```

## Useful commands

| Action | Command |
|--------|---------|
| Start the concentrator | `sudo docker compose up -d` |
| Check running status | `sudo docker compose ps` |
| View all logs | `sudo docker compose logs` |
| Stream logs in real time | `sudo docker compose logs -f` |
| Filter logs by intake key | `sudo docker compose logs \| grep "YOUR_INTAKE_KEY"` |
| Stop the concentrator | `sudo docker compose stop` |
| Delete the concentrator | `sudo docker compose rm` |

## Troubleshoot the concentrator

### Step 1 - Verify the forwarder version

Sekoia regularly releases new versions of the forwarder. Check that you are running the latest version before investigating further.

### Step 2 - Check that events are received

Enable debug mode on the relevant intake in `intakes.yaml`:

```yaml
- name: Techno2
  protocol: tcp
  port: 20517
  intake_key: INTAKE_KEY_FOR_TECHNO_2
  debug: True
```

Rebuild and restart the container:

```bash
docker compose down && docker compose up -d
```

Stream the logs and filter by intake key:

```bash
sudo docker compose logs -f | grep "YOUR_INTAKE_KEY"
```

If no events appear, verify the following:

1. The `intakes.yaml` file declares the correct protocol and port for the expected source.
2. The declared ports are reflected in the `ports` section of `docker-compose.yml`. For example, if you configured ports `25020` to `25023`, the ports line must include at least `"25020-25023:25020-25023"`.
3. No firewall is blocking traffic from the log source:

    ```bash
    sudo tcpdump -c10 -nn src <remote_ip> -vv
    ```

4. The log source is configured to send to the correct IP address and port using the correct protocol.

### Step 3 - Verify connectivity to Sekoia.io

1. Confirm the intake key in `intakes.yaml` is correct.
2. Test the outbound network flow to Sekoia.io:

    ```bash
    sudo apt install telnet && telnet intake.sekoia.io 10514
    ```

    A successful connection returns:

    ```
    Connected to intake.sekoia.io.
    Escape character is '^]'.
    ```

    Remove `telnet` after testing:

    ```bash
    sudo apt remove telnet
    ```

3. Check the platform status at [https://status.sekoia.io](https://status.sekoia.io).

## Update the concentrator

The image version is defined in the `image` line of `docker-compose.yml`:

```
image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:2.7.2
```

To update, change the version tag and recreate the container:

```bash
sudo docker compose up -d
```

All available versions are listed on the [GitHub container registry](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator/pkgs/container/sekoiaio-docker-concentrator/versions?filters%5Bversion_type%5D=tagged).

!!! tip "Using the latest tag"
    The `latest` tag always resolves to the most recent version. With `pull_policy: always`, the image is updated on every `docker compose up`.

!!! warning "Use latest with caution in production"
    A major version change could break your current configuration. Pin to a specific version in production environments.

!!! note "Weekly security patches"
    Each image version is rebuilt weekly with the latest OS security patches. You are responsible for recreating the container periodically to apply them.

## Add a new intake

1. Edit `intakes.yaml` and add the new entry:

    ```yaml
    - name: NewIntake
      protocol: tcp
      port: 20519
      intake_key: INTAKE_KEY_FOR_NEW_INTAKE
    ```

2. Verify that the new port falls within the range already declared in `docker-compose.yml`. If not, expand the range:

    ```yaml
    ports:
      - "20516-20566:20516-20566"
      - "20516-20566:20516-20566/udp"
    ```

3. Recreate the concentrator:

    ```bash
    sudo docker compose up -d
    ```

4. Confirm the new intake appears in the startup logs:

    ```bash
    sudo docker compose logs | more
    ```

## Docker Engine installation

This section covers Docker Engine installation on Debian 64-bit (Bullseye 11 or Buster 10). For other Linux distributions, refer to the [official Docker documentation](https://docs.docker.com/engine/install/).

### Uninstall previous versions

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### Set up the apt repository

1. Update the package index and install HTTPS transport dependencies:

    ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release
    ```

2. Add Docker's official GPG key:

    ```bash
    sudo mkdir -m 0755 -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```

3. Add the Docker repository:

    ```bash
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

### Install Docker Engine

1. Update the package index:

    ```bash
    sudo apt-get update
    ```

2. Install Docker Engine and its components:

    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

3. Verify the installation:

    ```bash
    sudo docker run hello-world
    ```

## 5-minute setup on Debian

This script automates all the steps on this page for a Debian host.

!!! warning "Read before running"
    Review the full content of this page before executing the script. The script applies all default settings without prompting for confirmation.

**Step 1** - Download and run the setup script:

```bash
wget https://raw.githubusercontent.com/SEKOIA-IO/documentation/main/docs/assets/operation_center/ingestion_methods/sekoiaio_forwarder/sekoiaio_docker_concentrator_autosetup.sh
chmod +x sekoiaio_docker_concentrator_autosetup.sh
./sekoiaio_docker_concentrator_autosetup.sh
rm sekoiaio_docker_concentrator_autosetup.sh
```

**Step 2** - Edit the generated configuration files:

- In `sekoiaio-concentrator/intakes.yaml`, replace the `name`, `protocol`, `port`, and `intake_key` values for each intake.
- In `sekoiaio-concentrator/docker-compose.yml`, update the port range to match your `intakes.yaml`.

**Step 3** - Start the concentrator:

```bash
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs -f
```

## Additional resources

The forwarder image is maintained on the [sekoiaio-docker-concentrator GitHub repository](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator). Contributions and pull requests are welcome.
