# SEKOIA.IO Docker concentrator
## Overview
[Docker](https://docs.docker.com/get-started/overview/) is a tool that can be used to run packaged applications in an isolated environment on a host.
Packaged applications are stored in an object called an image, which includes an OS, the dependencies and the configuration. With that, the application will have the same behaviour whatever the OS used on the host as long as it's a x86-64 Linux host.

SEKOIA.IO offers a preconfigured concentrator based on Docker to forward events on the platform.

This method simplfies as much as possible the configuration needed to set up a concentrator.

For that, each technologies will send their logs to a specific port on the concentrator, to easily identify them and forward them to the right Intake.

## Prerequisites
* A x86-64 Linux host
* Last version of Docker Engine.
* INBOUND TCP or UDP flows between your systems/applications and the concentrator on the ports of your choice
* OUTBOUND TCP flow to intake.sekoia.io on port 10514

## Docker Engine installation
This section describe how to install Docker using the `apt` repository on one of those Debian 64-bit versions:

* Debian Bullseye 11 (stable)
* Debian Buster 10 (oldstable)

All of the installation steps come from the [official Docker Engine installation for Debian](https://docs.docker.com/engine/install/debian/). Feel free to consult the official installation page for more information.
To install Docker on another Linux OS, please consult the [official Docker documentation](https://docs.docker.com/engine/install/)

### Uninstall old verions
Run the following command to uninstall old Docker versions:
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### Set up the repository
1. Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS:

```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

2. Add Docker's official GPG key:

```bash
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

3. Use the following command to set up the repository

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker Engine
1. Update the `apt` package index:
```bash
sudo apt-get update
```

2. Install Docker Engine, containerd, and Docker compose.
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the hello-world image:
```
sudo docker run hello-world
```

## Configure your concentrator
Two files are needed to run the concentrator: `docker-compose.yml` and `intakes.yaml`.

1. Create a folder where the configuration and data of the concentrator will be stored:
```bash
mkdir sekoiaio-concentrator && cd sekoiaio-concentrator
```

2. Create the two files:
```bash
touch docker-compose.yml && touch intakes.yaml
```

### Configure intakes.yaml file
The `intakes.yaml` file is used to tell the concentrator what ports and intake keys to use depending of the technologies you want to forward.
For each technology, specify:

* a name (it has nothing to do with SEKOIA.IO, it can be a random value)
* the protocol, `tcp` or `udp`
* a port, to process incoming events
* the intake key

Here is an example of the file with 3 technologies sending their events to the concentrator on ports `20516`, `20517` & `20518`. Feel free to copy paste it and adapt it to your need:
```yml
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

### Configure docker-compose.yml file
Please find below a template of the `docker-compose.yml` file. Feel free to copy paste it and adapt it to your need. The next sections will describe each element of this file:
```yaml
version: "3.9"
services:
  sekoia_concentrator:
    logging:
      options:
        max-size: "1000m"
        max-file: "2"
    image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:latest
    environment:
      - MEMORY_MESSAGES=100000
      - DISK_SPACE=32g
    ports:
      - "20516-20518:20516-20518"
    volumes:
      - ./intakes.yaml:/intakes.yaml
      - ./conf:/etc/rsyslog.d
      - ./disk_queue:/var/spool/rsyslog
    restart: always
```

#### Logging
```yaml
logging:
    options:
    max-size: "1000m"
    max-file: "2"
```

Docker logging system offers the flexibility to view events received on the container in real time with the command `docker logs <container_name>`. These logs are stored by default in `/var/lib/docker/containers/<container_uuid>/<container_uuid>-json.log`. To avoid the overload of disk space on your host, some options are specified. `max-size` specifies the maximum size of one file and `max-file` specifies the total number of files allowed. When the maximum number of files is reached, a log rotation is performed and the oldest file is deleted.

!!!Note
  Docker logging system has nothing to do with SEKOIA.IO or the buffer you want to set up on your concentrator. It is only used to view the last events on your concentrator.

#### Environment variables
```yaml
environment:
    - MEMORY_MESSAGES=100000
    - DISK_SPACE=32g
```

Two environment variables are used to customize the container. These variables are used to define a queue for incoming logs in case there is a temporaly issue in transmitting events to SEKOIA.IO. The queue stores messages in memory up to a certain number of events and then store them on disk. When the issue is fixed, events stored are retrieved from the queue and forward to the plateform.

* `MEMORY_MESSAGES=1000000` means the queue is allowed to store up to 100000 messages in memory. Since in the image configuration, the maximum value of a message is 20k, 100000 means 100000 * 20000 = 2G
* `DISK_SPACE=32g` means the queue is allowed to store on disk up to 32 giga of messages.

#### Ports
```
ports:
    - "20516-20518:20516-20518"
```

As specified in the Overview section, the concentrator will be run in a isolated environment. That means, by default, no flow is open between the host and the concentrator. 
`20516-20518:20516-20518` means that every packets coming through the TCP port `20516`, `20517` or `20518` to the host will be forwarded to the concentrator container on the port 20516, 20517 or 20518. Please adapt these values accordingly to the intakes.yaml file.

#### Volumes
```
volumes:
    - ./intakes.yaml:/intakes.yaml
    - ./conf:/etc/rsyslog.d
    - ./rsyslog:/var/spool/rsyslog
```

Volumes are used to share files and folders between the host and the container:

* `./intakes.yaml:/intakes.yaml` is used to tell the concentrator what protocol, ports and intake keys to use.
* `./conf:/etc/rsyslog.d` is mapped if you want to customize some rsyslog configuration (ADVANCED)
* `./disk_queue:/var/spool/rsyslog` is used when the concentrator queue stores data on disk. The mapping avoids data loss if logs are stored on disk and the container is deleted.

#### Persistance
```
restart: always
```

This line indicates to restart the concentrator everytime it stops. That means if it crashes, if you restart Docker or if you restart the host, the concentrator will start automatically.

## Start the concentrator
To start the concentrator, run the following command in the folder where `docker-compose.yml` and `intakes.yaml` are stored:
```bash
sudo docker compose up -d
```

You should have have an answer like this:
```
[+] Running 1/1
 ⠿ Container docker-compose-rsyslog-1  Started
```

!!!note
  The first time you start the container, you will download the image stored on the GitHub repository - `ghcr.io/sekoia-io/sekoiaio-docker-concentrator`

To check the status of the concentrator, you can run:
```bash
sudo docker compose ps
```

## Useful commands
**To view all the concentrator logs:**
```bash
sudo docker compose logs
```

Everytime an event is sent to the concentrator, the event is shown in these logs.

**To view last logs in real time:**
```bash
sudo docker compose logs -f
```

**To stop the concentrator:**
```bash
sudo docker compose stop
```

**To delete the concentrator (the concentrator needs to be stopped):**
```bash
sudo docker compose rm
```

## Troubleshooting
You can't the logs in your community ? No worries this section will give you the advice to see what is happening.

### Step 1: check if the events are received by the concentrator
To check if the events are received by the concentrator, you can run the following command that will display all the last logs received:
```
sudo docker compose logs
```

If you are looking for specific logs, you can also run:
```
sudo docker compose logs | grep "YOUR_PATTERN"
```

Finally, if you want to check if events are coming in real time:
```
sudo docker compose logs -f
```

**You don't see your events with these commands ?** 

1. Check the `intakes.yaml` file to see if you have declared the protocols and ports you wanted. You can also verify these information are taken into account by the concentrator. At start-up the concentrator always shows the list of Intakes with the protocols and ports.
  ```bash
  sudo docker compose logs | more
  ```

2. Check that you correctly declared the `ports` section in the `docker-compose.yml` file accordingly with the ports declared in  the `intakes.yaml` file.
   For instance, if you declared 4 technologies on ports `25020`, `25021`, `25022` and `25023`, the ports line the `docker-compose.yml` has to be `"25020-25023"`. 

3. Verify that traffic is incoming from your log source, meaning no firewall is blocking the events:
```bash
sudo tcpdump -i <change_with_interface_name> -c10 -nn src <remote_ip> -vv
```

### Step 2: verify everything is correctly configured to forward events to SEKOIA.IO

1. Check the intake keys you wrote in `intakes.yaml` are correct.

2. Check the flow between the concentrator host and SEKOIA.IO is opened to `intake.sekoia.io` in `TCP 10514`. You can easily check it with `telnet`:
   ```
   sudo apt install telnet && telnet intake.sekoia.io 10514
   ```
   This command should return
   ```
   Connected to intake.sekoia.io.
   Escape character is '^]'.
   ```
   meaning the flow is opened.

3. Finally check the status of the SEKOIA.IO plateform on [https://status.sekoia.io](https://status.sekoia.io)

## Additional information
The image used to run the concentrator is maintained on [this github repository](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator). Feel free to contribute and make a pull request to improve the concentrator !