# Configure the Sekoia.io Forwarder

The Sekoia.io Forwarder is a Docker-based collector that receives events from multiple sources and forwards them to the matching Sekoia intake. It maps each listening port to an intake key, so each technology normally requires its own port.

!!! warning "Use a distinct port for each intake"

    Configure every technology to send its logs to a distinct forwarder port. The forwarder uses the port-to-intake mapping to route events correctly. If several technologies must use the same port, follow [Route multiple technologies through one port](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md).

## Prerequisites

Before you deploy the forwarder, prepare the following:

- An x86-64 Linux host.
- Docker Engine with Docker Compose support.
- An intake key for each technology that you want to collect.
- Inbound TCP or UDP traffic from your log sources to the ports exposed by the forwarder.
- Outbound TCP traffic from the forwarder host to the Sekoia regional endpoint on port `10514`.

### Select the host size

Use the following recommendations as a starting point. Actual resource requirements depend on your event volume and message size.

| Number of assets | vCPUs | RAM (GB) | Disk size (GB) | `MEMORY_MESSAGES` | `DISK_SPACE` |
| --- | ---: | ---: | ---: | ---: | --- |
| 1,000 | 2 | 4 | 200 | 2,000,000 | 180g |
| 10,000 | 4 | 8 | 1,000 | 5,000,000 | 980g |
| 50,000 | 6 | 16 | 5,000 | 12,000,000 | 4,980g |

Disk type does not affect forwarder throughput. An SSD can reduce recovery time when the forwarder catches up with messages stored in the disk queue.

### Select the regional endpoint

Set the `REGION` environment variable to the region that hosts your Sekoia environment.

| Region | Host address | Port |
| --- | --- | --- |
| FRA1 | `intake.sekoia.io` | `10514` |
| FRA2 | `intake.fra2.sekoia.io` | `10514` |
| MCO1 | `intake.mco1.sekoia.io` | `10514` |
| UAE1 | `intake.uae1.sekoia.io` | `10514` |
| USA1 | `intake.usa1.sekoia.io` | `10514` |
| SGP1 | `intake.sgp1.sekoia.io` | `10514` |

## Install Docker Engine

The following commands install Docker Engine from Docker's official Debian repository. For another Linux distribution, follow the [official Docker Engine installation instructions](https://docs.docker.com/engine/install/).

1. Remove conflicting packages:

    ````bash
    sudo apt-get remove docker docker-engine docker.io containerd runc
    ````

2. Update the package index and install the repository dependencies:

    ````bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release
    ````

3. Add Docker's GPG key:

    ````bash
    sudo mkdir -m 0755 -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ````

4. Add the Docker repository:

    ````bash
    echo \
         "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/$(lsb_release -is) \
         $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ````

5. Install Docker Engine and Docker Compose:

    ````bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ````

6. Verify the installation:

    ````bash
    sudo docker run hello-world
    ````

## Deploy the forwarder

### Create the working directory

Create a directory for the forwarder configuration and move into it.

````bash
mkdir sekoiaio-concentrator && cd sekoiaio-concentrator
````

Create the two configuration files used by the deployment.

````bash
touch docker-compose.yml intakes.yaml
````

### Configure `intakes.yaml`

The `intakes.yaml` file maps a listening port to an intake key. Add one entry for each technology.

| Field | Description |
| --- | --- |
| `name` | A label for the intake. Sekoia does not use this value for routing. |
| `protocol` | `tcp`, `udp`, or `tls`. |
| `port` | The port on which the forwarder listens for this technology. |
| `intake_key` | The key associated with the Sekoia intake. |
| `debug` | Optional. Set to `True` to print received and forwarded messages for this intake. |
| `queue_size` | Optional. Sets a custom in-memory queue size for this intake. |

The following example configures three technologies:

````yaml
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
````

By default, the forwarder divides `MEMORY_MESSAGES` between all configured intakes. To reserve a specific queue size for an intake, add `queue_size`:

````yaml
- name: Techno1
  protocol: tcp
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
  queue_size: 100000
````

Intakes without an explicit `queue_size` keep the default calculated from `MEMORY_MESSAGES`.

!!! note "Enable debug logging only while investigating"

    Add `debug: True` to the relevant intake when you need to confirm that the forwarder receives and forwards events. Disable it after testing because the output can be large.

### Configure `docker-compose.yml`

Create a Compose file similar to the following example:

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
    volumes:
      - ./intakes.yaml:/intakes.yaml
      - ./disk_queue:/var/spool/rsyslog
    restart: always
    pull_policy: always
````

Adjust the port ranges to match the ports in `intakes.yaml`.

#### Configure the environment variables

| Variable | Status | Description |
| --- | --- | --- |
| `MEMORY_MESSAGES` | Recommended | Maximum number of messages kept in memory across all queues. For example, `2,000,000 × 1.2 KB` uses about `2.4 GB` of RAM. |
| `DISK_SPACE` | Recommended | Disk space allocated to on-disk queues across all intakes. |
| `REGION` | Required | Sekoia region. Accepted values are `FRA1`, `FRA2`, `MCO1`, `UAE1`, `USA1`, and `SGP1`. |
| `RELP_OUTPUT` | Optional | Set to `True` to send events with RELP instead of the default TCP syslog mode. |

#### Expose the input ports

Each entry in the `ports` section follows the `HOST_PORT:CONTAINER_PORT` format. Add `/udp` for UDP traffic.

!!! warning "Keep the port mappings synchronized"

    Every port in `intakes.yaml` must be exposed by the matching `ports` entry in `docker-compose.yml`. A mismatch prevents the forwarder from receiving traffic on that port.

#### Persist the queues

The `./disk_queue:/var/spool/rsyslog` volume stores on-disk queues on the host. Keep this directory on persistent storage so that queued messages survive container recreation.

Use the following additional mounts for advanced configurations:

| Mount | Use |
| --- | --- |
| `./certs:/certs` | Certificates for [TLS input](/integration/ingestion_methods/syslog/secure_forwarder_inputs_with_tls.md). |
| `./extended_conf:/extended_conf` | Custom rsyslog configuration for [shared-port routing](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md). |

The `restart: always` option restarts the container after a failure, Docker restart, or host reboot. The `pull_policy: always` option checks for a newer image each time you run `docker compose up`.

### Start the forwarder

Start the container from the directory that contains `docker-compose.yml` and `intakes.yaml`.

````bash
sudo docker compose up -d
````

Check the container status.

````bash
sudo docker compose ps
````

On the first startup, Docker downloads the image from `ghcr.io/sekoia-io/sekoiaio-docker-concentrator`. The host must have outbound internet access for this download.

## Add an intake

1. Open `intakes.yaml`.
2. Add an entry with a unique `name`, `protocol`, `port`, and `intake_key`.

    ````yaml
    - name: NewIntake
      protocol: tcp
      port: 20519
      intake_key: INTAKE_KEY_FOR_NEW_INTAKE
    ````

3. Confirm that the new port is included in the `ports` section of `docker-compose.yml`.
4. Recreate the container:

    ````bash
    sudo docker compose up -d
    ````

5. Check the startup logs:

    ````bash
    sudo docker compose logs
    ````

## Update the forwarder

The image version is defined in the `image` field of `docker-compose.yml`.

````yaml
image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:latest
````

To update the image, replace `latest` with the required version tag and recreate the container:

````bash
sudo docker compose up -d
````

The available image versions are listed in the [GitHub Container Registry](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator/pkgs/container/sekoiaio-docker-concentrator/versions?filters%5Bversion_type%5D=tagged).

!!! warning "Pin the image version in production"

    The `latest` tag resolves to the newest image. A major version change can affect an existing configuration. Pin a tested version in production and recreate the container regularly to receive the security updates included in that version.

## Use the Debian setup script

The setup script creates a default Debian deployment. Review this page before running it because the script applies its default settings without prompting for confirmation.

1. Download and run the script:

    ````bash
    wget https://raw.githubusercontent.com/SEKOIA-IO/documentation/main/docs/assets/operation_center/ingestion_methods/sekoiaio_forwarder/sekoiaio_docker_concentrator_autosetup.sh
    chmod +x sekoiaio_docker_concentrator_autosetup.sh
    ./sekoiaio_docker_concentrator_autosetup.sh
    rm sekoiaio_docker_concentrator_autosetup.sh
    ````

2. Edit `sekoiaio-concentrator/intakes.yaml` and replace the `name`, `protocol`, `port`, and `intake_key` values.
3. Edit `sekoiaio-concentrator/docker-compose.yml` and update the port ranges to match `intakes.yaml`.
4. Start and verify the container:

    ````bash
    sudo docker compose up -d
    sudo docker compose ps
    sudo docker compose logs -f
    ````

## Useful commands

| Action | Command |
| --- | --- |
| Start the forwarder | `sudo docker compose up -d` |
| Check the status | `sudo docker compose ps` |
| View logs | `sudo docker compose logs` |
| Stream logs | `sudo docker compose logs -f` |
| Filter logs by intake key | `sudo docker compose logs \| grep "YOUR_INTAKE_KEY"` |
| Stop the forwarder | `sudo docker compose stop` |
| Remove the container | `sudo docker compose rm` |

## Result

The forwarder is running as a Docker container, accepts events on the configured ports, and sends them to the Sekoia regional endpoint associated with `REGION`.

## Related articles

- [Route multiple technologies through one port](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md): How to route several technologies that use the same input port.
- [Secure forwarder inputs with TLS](/integration/ingestion_methods/syslog/secure_forwarder_inputs_with_tls.md): How to encrypt traffic between log sources and the forwarder.
- [Monitor the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/monitor_the_sekoiaio_forwarder.md): How to send forwarder health metrics to Sekoia.
- [Troubleshoot the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/troubleshoot_the_sekoiaio_forwarder.md): How to investigate missing events and connectivity issues.
- [Sekoia.io forwarder logs](/integration/categories/applicative/sekoiaio_forwarder_logs.md): Overview of the forwarder health intake.
