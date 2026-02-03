# Sekoia.io NetFlow Concentrator

## Overview

Sekoia.io offers a preconfigured NetFlow collector based on Docker to collect NetFlow data from network devices and forward it to the platform.

This method simplifies as much as possible the configuration needed to set up a concentrator in order to collect NetFlow data and send them to the relevant Intake.

The NetFlow Concentrator acts as a collector that:

- Listens for NetFlow data from network devices (routers, switches, firewalls)
- Processes and forwards the collected data to Sekoia.io

## Prerequisites

* Last version of Docker Engine with Docker Compose support. Please follow [this section](#docker-engine-installation) to install it if needed
* INBOUND UDP flow opened on the concentrator for NetFlow data reception (default port: 2055)
* OUTBOUND TCP flow opened towards:
    * **FRA1** intake.sekoia.io on port 10514
    * **FRA2** app.fra2.sekoia.io on port 10514
    * **MCO1** app.mco1.sekoia.io on port 10514
    * **UAE1** app.uae1.sekoia.io on port 10514
    * **USA1** app.usa1.sekoia.io on port 10514
* A Sekoia.io intake key for NetFlow data
* Network devices configured to send NetFlow data

## Configure your concentrator

Two files are needed to run the concentrator: `docker-compose.yml` and `configuration.ini`.

1. Create a folder where the configuration and data of the concentrator will be stored

    ```bash
    mkdir sekoiaio-netflow-concentrator && cd sekoiaio-netflow-concentrator
    ```

2. Create the two files

    ```bash
    touch docker-compose.yml && touch configuration.ini
    ```

### Configure configuration.ini file

The `configuration.ini` file is used to configure the NetFlow listener and the forwarder to Sekoia.io.

Edit the `configuration.ini` file with the following content:

```ini
[listener]
# IP address to bind the NetFlow listener (0.0.0.0 for all interfaces)
bind=0.0.0.0
# Port to listen for NetFlow data (default: 2055)
port=2055

[forwarder]
# SEKOIA.IO intake host (see Regional Hosts section below)
host=intake.sekoia.io
# SEKOIA.IO intake port
port=10514
# Your SEKOIA.IO intake key (REQUIRED)
intake_key=<intake_key>
```

!!! Important
    Replace `<intake_key>` with your actual Sekoia.io intake key and set the `host` according to your Sekoia.io region.

#### Regional Hosts

Select the appropriate host address based on your Sekoia.io region:

| Region | Host Address              | Port  |
|--------|---------------------------|-------|
| FRA1   | `intake.sekoia.io`        | 10514 |
| FRA2   | `app.fra2.sekoia.io`      | 10514 |
| MCO1   | `app.mco1.sekoia.io`      | 10514 |
| UAE1   | `app.uae1.sekoia.io`      | 10514 |
| USA1   | `app.usa1.sekoia.io`      | 10514 |

#### Configuration Parameters

**Listener Section:**

* `bind`: The IP address on which the NetFlow collector listens. Use `0.0.0.0` to listen on all network interfaces.
* `port`: The UDP port for receiving NetFlow data. Standard NetFlow ports are 2055 or 9995.

**Forwarder Section:**

* `host`: The Sekoia.io intake hostname (varies by region - see Regional Hosts section above)
* `port`: The Sekoia.io intake port (default: `10514`)
* `intake_key`: Your unique Sekoia.io intake key for authentication

### Configure docker-compose.yml file

Please find below a template of the `docker-compose.yml` file.

```yaml
services:
  netflow-concentrator:
    image: ghcr.io/sekoia-io/sekoiaio-netflow-forwarder:latest
    container_name: netflow-concentrator
    environment:
      - NETFLOW_COLLECTOR_DEBUG=false
    ports:
      - "2055:2055/udp"
    volumes:
      - ./configuration.ini:/app/configuration.ini:ro
    restart: always
    pull_policy: always
```

!!! Note
    Feel free to copy paste it and adapt it to your needs.

The following sections will describe each element of this file above.

#### Environment variables

```yaml
environment:
    - NETFLOW_COLLECTOR_DEBUG=false
```

The `NETFLOW_COLLECTOR_DEBUG` environment variable is used to enable or disable debug logging:

* `NETFLOW_COLLECTOR_DEBUG=false`: Normal operation mode (default)
* `NETFLOW_COLLECTOR_DEBUG=true`: Enable debug logs for troubleshooting

#### Ports

```yaml
ports:
    - "2055:2055/udp"
```

As specified in the Overview section, the concentrator will be run in an isolated environment. That means, by default, no flow is open between the host and the concentrator.

`2055:2055/udp` means that every UDP packets coming through port `2055` to the host will be forwarded to the concentrator container on port `2055`.

!!! Important
    The port must match the port specified in the `configuration.ini` file. If you change the port in the configuration file, you must also update it in the docker-compose.yml file.

#### Volumes

```yaml
volumes:
    - ./configuration.ini:/app/configuration.ini:ro
```

Volumes are used to share files and folders between the host and the container:

* `./configuration.ini:/app/configuration.ini:ro`: is used to tell the concentrator how to listen for NetFlow data and where to forward it. The `:ro` flag means the file is mounted as read-only.

#### Additional options

```yaml
restart: always
pull_policy: always
```

* `restart: always`: this line indicates to restart the concentrator everytime it stops. That means if it crashes, if you restart Docker or if you restart the host, the concentrator will start automatically.
* `pull_policy: always`: docker compose will always try to pull the image from the registry and check if a new version is available for the tag specified.

## Deploy your concentrator

### Starting the Service

1. Navigate to your concentrator directory:

    ```bash
    cd sekoiaio-netflow-concentrator
    ```

2. Start the NetFlow concentrator:

    ```bash
    docker compose up -d
    ```

3. Verify the container is running:

    ```bash
    docker compose ps
    ```

### Stopping the Service

```bash
docker compose down
```

### Viewing Logs

To view the logs in real-time:

```bash
docker compose logs -f netflow-concentrator
```

To enable debug logging, edit `docker-compose.yml` and set:

```yaml
environment:
  - NETFLOW_COLLECTOR_DEBUG=true
```

Then restart the service:

```bash
docker compose restart
```

## Network Configuration

### Firewall Rules

Ensure that the UDP port specified in `configuration.ini` (default: 2055) is open and accessible from your network devices:

=== "Debian, Ubuntu"

    ```bash
    sudo ufw allow 2055/udp
    ```

=== "Fedora, Red Hat, CentOS (firewalld)"

    ```bash
    sudo firewall-cmd --permanent --add-port=2055/udp
    sudo firewall-cmd --reload
    ```

### Configure Network Devices

Configure your network devices (routers, switches, firewalls) to export NetFlow data to:

* **IP Address**: The host running this Docker container
* **Port**: The port specified in `configuration.ini` (default: 2055)
* **Protocol**: UDP

Example configurations vary by vendor:

* **Cisco IOS**: Use `ip flow-export destination <host> 2055`
* **Juniper**: Configure `flow-export destination <host> port 2055`
* Consult your device documentation for specific NetFlow export configuration

!!! Note
    The NetFlow concentrator supports multiple NetFlow versions. Ensure your network devices are configured to export NetFlow v5, v9, or IPFIX (NetFlow v10).

## Troubleshooting

### Check Container Status

```bash
docker compose ps
docker compose logs netflow-concentrator
```

### Enable Debug Mode

Set `NETFLOW_COLLECTOR_DEBUG=true` in the `docker-compose.yml` file to get detailed logs:

```yaml
environment:
  - NETFLOW_COLLECTOR_DEBUG=true
```

Then restart the service:

```bash
docker compose restart
```

### Common Issues

1. **No data received**: 
    - Verify network devices are configured correctly
    - Check firewall rules allow UDP traffic on the listener port
    - Ensure the container is running and listening
    - Verify the bind address and port in `configuration.ini`

2. **Cannot connect to Sekoia.io**:
    - Verify your intake key is correct
    - Check that you're using the correct regional host address
    - Check network connectivity to your regional host on port 10514
    - Ensure outbound TCP traffic is allowed

3. **Container fails to start**:
    - Check that the configuration file exists and is properly formatted
    - Verify the intake key is set in `configuration.ini`
    - Review container logs for specific error messages: `docker compose logs netflow-concentrator`

4. **High CPU or memory usage**:
    - Monitor the volume of NetFlow data being received
    - Consider increasing host resources if needed
    - Check for network loops or misconfigured devices sending excessive data

## Updates

The container is configured with `pull_policy: always`, which means it will check for and pull the latest image version on startup. To manually update:

```bash
docker compose pull
docker compose up -d
```

## Docker Engine installation

To install the latest version of Docker Engine on your Linux host, please follow the official Docker documentation:

=== "Debian"

    [Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)

=== "Ubuntu"

    [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

=== "Fedora"

    [Install Docker Engine on Fedora](https://docs.docker.com/engine/install/fedora/)

=== "Red Hat Enterprise Linux (RHEL)"

    [Install Docker Engine on RHEL](https://docs.docker.com/engine/install/rhel/)

=== "CentOS"

    [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)

After installation, ensure Docker Compose is available (it's included with Docker Engine v2.0+):

```bash
docker compose version
```

## Support

For issues or questions:

* Sekoia.io Support: Contact your Sekoia.io support team
* GitHub Repository: [SEKOIA-IO/sekoiaio-netflow-concentrator](https://github.com/SEKOIA-IO/sekoiaio-netflow-concentrator)
