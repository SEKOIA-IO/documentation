# Sekoia.io Forwarder

## Overview

[Docker](https://docs.docker.com/get-started/overview/) is a tool that can be used to run packaged applications in an isolated environment on a host.
Packaged applications are stored in an object called an image, which includes an OS, the dependencies and the configuration. With that, the application will have the same behaviour whatever the OS used on the host as long as it's a x86-64 Linux host.

Sekoia.io offers a preconfigured collector / concentrator based on Docker to forward events on the platform.

This method simplifies as much as possible the configuration needed to set up a concentrator in order to collect logs and send them on each relevant Intakes.

!!! Warning
    In this method, each technology MUST send their logs on different ports (of your choice) of the concentrator in order to make it work. The main principle of this method is to discriminate each technology by port to link them with the right Intake key.

Please find our English tutorial video below to see how to configure the forwarder ! French version is also available [here](https://youtu.be/CSEG2flmffE){:target="_blank"}.
[![French tutorial](https://img.youtube.com/vi/CSEG2flmffE/0.jpg)](https://youtu.be/BwydQiWMlv0){:target="_blank"}

## Prerequisites

* A x86-64 Linux host using one of these templates:

  | Number of assets |  vCPUs |  RAM (Go) | Disk size (Go) | Sekoia concentrator settings                |
  |------------------|:------:|:---------:|:--------------:|:-------------------------------------------:|
  | 1000             |    2   |   4       |      200       |  MEMORY_MESSAGES=2000000 / DISK_SPACE=180g  |
  | 10 000           |    4   |   8       |      1000      |  MEMORY_MESSAGES=5000000 / DISK_SPACE=980g  |
  | 50 000           |    6   |   16      |      5000      |  MEMORY_MESSAGES=12000000 / DISK_SPACE=4980g |

  !!! info
      These data are recommendations based on standards and observed averages on Sekoia.io, so they may change depending on use cases.

* Last version of Docker Engine. Please follow [this section](#docker-engine-installation) to install it if needed
* INBOUND TCP or UDP flows opened between the systems/applications and the concentrator on the ports of your choice
* OUTBOUND TCP flow opened towards:
  * **FRA1** intake.sekoia.io on port 10514
  * **FRA2** intake.fra2.sekoia.io on port 10514
  * **MCO1** intake.mco1.sekoia.io on port 10514
  * **UAE1** intake.uae1.sekoia.io on port 10514
  * **USA1** intake.usa1.sekoia.io on port 10514

  !!! note
      The disk choice (SSD or HDD type) has no impact on the performance of Sekoia.io Forwarder.
      However, SSD type would be useful when an issue arise for recovery or catchup.
      Please choose accordingly to your usage and cost.

## Configure your concentrator

Two files are needed to run the concentrator: `docker-compose.yml` and `intakes.yaml`.

1. Create a folder where the configuration and data of the concentrator will be stored

    ```bash
    mkdir sekoiaio-concentrator && cd sekoiaio-concentrator
    ```

2. Create the two files

    ```bash
    touch docker-compose.yml && touch intakes.yaml
    ```

### Configure intakes.yaml file

The `intakes.yaml` file is used to tell the concentrator how to bind a port where logs are received to its technology represented by the Intake key.
For each technology, specify:

* a name: it has nothing to do with Sekoia.io, feel free to use the explicite value of your choice
* the protocol: `tcp`, `udp` or `tls`
* a port: to process incoming events
* the Intake key: can be retreived from the Intakes page of your community

Here is an example of the file with 3 technologies sending their events to the concentrator on ports `20516`, `20517` and `20518`. Feel free to copy paste it and adapt it to your need:

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

!!! Tip
    You are not limited to 3 entries. Feel free to adapt it to your needs.

#### Debug
A debug variable is available in order to debug a specific intake, for example
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

When debug is set to true, the raw event received and the output message will be printed in STDOUT. Each one will be respectively identified using tags: : [Input $INTAKE_KEY] & [Output $INTAKE_KEY]

### Configure docker-compose.yml file

Please find below a template of the `docker-compose.yml` file.

```yaml
# Version is deprecated with latest versions of Docker Engine
# version: "3.9"
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

!!! Note
    Feel free to copy paste it and adapt it to your needs.

The following sections will describe each element of this file above.

#### Environment variables

```yaml
environment:
    - MEMORY_MESSAGES=2000000
    - DISK_SPACE=180g
    - REGION=FRA1
    - RELP_OUTPUT=True
```

Two environment variables are used to customize the container. These variables are used to define a queue for incoming logs in case there is a temporarily issue in transmitting events to Sekoia.io. The queue stores messages in memory up to a certain number of events and then store them on disk. When the issue is fixed, events stored are retrieved from the queue and forward to the plateform.

* `MEMORY_MESSAGES=2000000` means queues are allowed to store up to 2,000,000 messages in memory. If we consider a message size is 1.2KB, then you will use 2,4GB of RAM memory (2000000 * 1.2KB = 2.4GB). Note that this value is distributed among the configured intakes. For example, if 10 intakes are configured, each queue will have a retention capacity of 200,000 messages.
* `DISK_SPACE=180g` means that the total of all queues is allowed to store up to 180 gigabytes of messages on disk.
* `REGION=FRA1` is the region where to send the logs. Currently 5 options are available: `FRA1`, `FRA2`, `MCO1`, `UAE1` and `USA1`
* `RELP_OUTPUT=True` it is an optional environment variable. If the value is set to true, it allows sending all logs to Sekoia via the relp protocol instead of the default tcp syslog mode.

[Here](#prerequisites) you will find recommendations to set these variables based on the number of assets. You can also define your own values, which should be chosen according to your virtual machine's template.

!!! Info
    In case you want to set a specific retention size in memory for a particular intake, you can define it using this type of configuration:
    ```yaml
    - name: Techno1
      protocol: tcp
      port: 20516
      intake_key: INTAKE_KEY_FOR_TECHNO_1
      queue_size: 100000
    ```
    Note that other intakes will retain their default values, which is MEMORY_MESSAGES divided by the total number of intakes.

#### Ports

```yaml
ports:
    - "20516-20566:20516-20566"
    - "20516-20566:20516-20566/udp"
```

As specified in the Overview section, the concentrator will be run in an isolated environment. That means, by default, no flow is open between the host and the concentrator.
`20516-20518:20516-20566` means that every packets coming through the TCP port form `20516` to  `20566` to the host will be forwarded to the concentrator container from port `20516` to `20566`.

If you want to open a UDP flow, please add a line with `/udp` at the end.

!!! Important
    Please adapt these values according to the intakes.yaml file.

#### Volumes

```yaml
volumes:
    - ./intakes.yaml:/intakes.yaml
    - ./rsyslog:/var/spool/rsyslog
```

Volumes are used to share files and folders between the host and the container:

* `./intakes.yaml:/intakes.yaml` is used to tell the concentrator what protocol, ports and intake keys to use.
* `./conf:/etc/rsyslog.d` is mapped if you want to customize some rsyslog configuration (ADVANCED)
* `./disk_queue:/var/spool/rsyslog` is used when the concentrator queue stores data on disk. The mapping avoids data loss if logs are stored on disk and the container is deleted.

#### Import a custom rsyslog configuration

You can add your own additional rsyslog configuration. This can be useful to handle specific use cases that are not natively supported by the Sekoia.io concentrator. To enable it, simply create a new folder called `extended_conf` and place your additional rsyslog configuration file(s) inside (your file must have the `.conf` extension).

!!! warning
    If you configure a port or input in your custom `.conf` file within the `extended_conf` directory, **do not declare this intake again in the `intake.yaml` file**. Using both for the same input or port will cause conflicts and may prevent the concentrator from starting correctly.
    Your custom configuration will be added in addition to the existing intake definitions and will not overwrite them. Just make sure each port or source is configured *either* in `intake.yaml` *or* in your `.conf` file, not both.


You can define your own method for obtaining logs using rsyslog modules, but you still need to forward events to Sekoia.io by providing a syslog-valid message with your intake key as a header, as follows:

```bash
input(type="imtcp" port="20521" ruleset="remote20521")
template(name="SEKOIAIO_Template" type="string" string="<%pri%>1 %timegenerated:::date-rfc3339% %hostname% MY-APP-NAME - LOG [SEKOIA@53288 intake_key=\"MY-INTAKE-KEY\"] %msg%\n")
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

Once additional configuration has been added, you simply have to mount them in the docker as following:

```yaml
volumes:
    - ./intakes.yaml:/intakes.yaml
    - ./extended_conf:/extended_conf
    - ./disk_queue:/var/spool/rsyslog
```

#### Additional options

```yaml
restart: always
pull_policy: always
```

* `restart: always`: this line indicates to restart the concentrator everytime it stops. That means if it crashes, if you restart Docker or if you restart the host, the concentrator will start automatically.
* `pull_policy: always`: docker compose will always try to pull the image from the registry and check if a new version is available for the tag specified.

## Configure TLS for an Intake

Sending logs between the forwarder and Sekoia is always encrypted with TLS. However, by default, if you use the `tcp` or `udp` protocol option in your intake configuration, the logs between your devices and the forwarder will not be encrypted. This section shows you how to configure TLS between a source and the forwarder.

### Configuration of the docker-compose.yml

Activating TLS requires setting up an encryption key, a certificate, and a CA certificate. These should be placed in the `./certs` directory within the forwarder's directory.
Therefore it is necessary to mount this volume. Add the following line to the configuration:

```yaml
volumes:
    - ./certs:/certs
    [...]
```

### Creating the Key and Certificate

We will now create the key and certificate that will be used for encryption. In this case, we will create a self-signed certificate, meaning that the server certificate and the CA (Certificate Authority) certificate will be the same. If you have expertise in managing certificates, you can create a certificate signed by a real CA.

**Step one**: Create the directory and navigate to it:

```
mkdir certs && cd certs
```

**Step two**: Install OpenSSL

=== "Debian, Ubuntu"

    ```bash
    sudo apt update
    sudo apt install -y openssl
    ```

=== "Fedora, Red Hat, CentOS (yum)"

    ```bash
    sudo yum update
    sudo yum install -y openssl
    ```

=== "Fedora, Red Hat, CentOS (dnf)"

    ```bash
    sudo dnf update
    sudo dnf install -y openssl
    ```

Step three: Create the key and certificate

```
openssl req -x509 \
            -sha256 -days 1825 \
            -nodes \
            -newkey rsa:4096 \
            -keyout server.key -out server.crt
```

- `openssl req`: Launches the process to create a Certificate Signing Request (CSR) or a self-signed certificate.
- `-x509`: This option tells OpenSSL to generate a self-signed certificate rather than a CSR.
- `-sha256`: Specifies that the SHA-256 hashing algorithm should be used for the certificate's signature.
- `-days 1825`: Sets the certificate's validity period to 1825 days, which corresponds 5 years.
- `-nodes`: This stands for "no DES" and indicates that the private key should not be encrypted, meaning no password will be required to use the private key.
- `-newkey rsa:4096`: Generates a new RSA key pair of 4096 bits in length, and simultaneously creates a certificate request using this key pair.
- `-keyout server.key`: Specifies the file where the generated private key should be saved. In this case, it will be saved to `server.key`.
- `-out server.crt`: Specifies the file where the generated self-signed certificate should be saved. In this case, it will be saved to `server.crt`.

**Step four**: Change permissions on the files

```
chmod 600 server.key server.crt
```

### Configuration of the intakes.yaml File

To use TLS, you need to specify `tls` in the protocol definition:

```
protocol: tls
```

By default, as soon as you specify the tls protocol, the forwarder will attempt to read the private key and certificate at /certs/server.key and /certs/server.crt.
If you wish to specify other filenames, you can do so in the intake configuration:

```
[...]
protocol: tls
tls_key_name: server
tls_cert_name: server
tls_ca_name: server
```

## Monitor your concentrator

The forwarder is a critical component in the architecture between your information system and the Sekoia platform. A prolonged service interruption could lead to data loss, potentially causing missed detection of an attack within your environment.

In this context, please find below the instructions to enable monitoring of your forwarder.
This will allow health status information of the component to be transmitted to Sekoia, enabling you to set up alerts based on the values of the transmitted metrics.

### Create the forwarder logs intake

The first step is to create the intake on the Sekoia platform and save the associated intake key

For detailed information on this process, please refer to the following [documentation](/integration/categories/applicative/sekoiaio_forwarder_logs.md)

### Configuration of the intake.yml file

To activate the monitoring mode, simply defined a new intake and add `stats: True` in the `intakes.yaml` file with the associated `intake_key` coming from the right format:

```yaml
---
intakes:
- name: Monitoring
  stats: True
  intake_key: INTAKE_KEY_FOR_FORWARDER_LOGS
```

!!! Note
    This intake is special because logs are auto-generated by the forwarder. As a consequency, you don't need to define an input port neither the protocol.

### Understanding concentrator metrics

The concentrator is based on a rsyslog instance so to monitor the forwarder, we decided against developing our own metrics. Instead, we opted for leveraging a standard implementation provided by rsyslog direclty: the [impstats module](https://www.rsyslog.com/doc/configuration/modules/impstats.html)

By enabling this internal module, rsyslog generates numerous low-level metrics, which are essential for us to comprehend in order to understand the forwarder metrics. Therefore, it is crucial to grasp the operational workflow of rsyslog. [Here](https://www.rsyslog.com/doc/configuration/basic_structure.html) you can find more details about rsyslog principles.

The forwarder is configured with one input module per intake, as specified in the `intake.yaml` file. Each input module is paired with a corresponding ruleset, action, and specific queue. When monitoring is enabled, dedicated metrics for each module will be transferred to Sekoia, identified by a specific name, as shown below:

![image](/assets/operation_center/ingestion_methods/sekoiaio_forwarder/forwarder_monitoring_2.png){: style="max-width:100%"}

By leveraging these metrics, you can easily define custom rules to detect specific behaviors such as service interruptions, full queues, discarded events, and more. This monitoring capability is crucial for maintaining optimal performance and ensuring the reliability of the forwarder in your system.

Below is an example of a rule pattern designed to identify if queues are full on the forwarder, which may lead to log loss. The cause of a full queue can be attributed to several factors, such as an under-provisioned machine unable to handle the load, a sudden increase in events per second (EPS), or infrastructure issues. In any case, this type of alert indicates the need for further investigation into the behavior of the forwarder to understand the root cause of the problem.

```yaml
detection:
  selection:
    - sekoiaio.forwarder.queue.discarded.full|gt: 0
    - sekoiaio.forwarder.queue.discarded.nf|gt: 0
    - sekoiaio.forwarder.queue.full|gt: 0
  condition: selection
```

!!! Note
    To understand the detailed meaning of each counter, please refer to the [associated rsyslog documentation](https://www.rsyslog.com/doc/configuration/rsyslog_statistic_counter.html) and be free to implement your own rules based on these metrics.

### Extract concentrator metrics in case of outage

In extreme cases, the forwarder may cease to function entirely, and as a result, it will also stop sending its metrics to Sekoia (e.g., a full queue). While an alert from Sekoia will notify you of this issue, you will still need to investigate and understand the root cause to resolve the problem.

In addition to continuously sending its metrics to Sekoia, the forwarder also retains a raw copy of its metrics locally. To retrieve these logs on your host for debugging purpose, you can use the following command:


```bash
 sudo docker compose cp rsyslog:/var/log/rsyslog-stats.log  rsyslog-stats.log
```

## Start the concentrator

To start the concentrator, run the following command in the folder where `docker-compose.yml` and `intakes.yaml` are stored:

```bash
sudo docker compose up -d
```

You should have an answer like this:

```bash
[+] Running 1/1
 ⠿ Container docker-compose-rsyslog-1  Started
```

!!! Note
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

If you are using the Debug variable, everytime a log is received by the Forwarder, it's visible using `docker compose logs`.

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

You can't find the logs in your community? No worries this section will give you an advice to identify what is happening.

### Step 1: Verify you are running the latest version of the forwarder
Sekoia regularly pushes new versions of the forwarder. Be sure you are running the latest version to ensure you have the latest updates.

### Step 2: Check if the events are received by the forwarder

To check if the events are received by the forwarder, you can activate the debug mode for a specific Intake. The debug mode will display all logs that are received and sent by the forwarder associated with a specific Intake, in the standard output of the container (`docker logs`).
To activate the debug mode, simply add `debug: True` in the definition of the Intake you want, in the `intakes.yaml` file.

Example:
```yaml
- name: Techno2
  protocol: tcp
  port: 20517
  intake_key: INTAKE_KEY_FOR_TECHNO_2
  debug: True
```

Then rebuild the container and start it:
```yaml
docker compose down && docker compose up -d
```

Now, you can run the following command and display all the last logs received for the Intakes with the mode debug activated:

```bash
sudo docker compose logs
```

To view container logs for a specific intake when using the debug variable:

```bash
sudo docker compose logs | grep "YOUR_INTAKE_KEY"
```

Finally, if you want to check events coming in real time for Intakes with the debug variable:

```bash
sudo docker compose logs -f
```

**You don't see your events with these commands?**

1. Check that the forwarder is correctly configured

    * Check the `intakes.yaml` file to see if you have declared the protocols and ports you wanted.

    * Verify if this information is taken into account by the concentrator. At start-up, the concentrator always shows the list of Intakes with the protocols and ports.
        ```bash
        sudo docker compose logs | more
        ```

    * Check that you correctly declared the `ports` section in the `docker-compose.yml` file. They MUST be the same as the ports declared in the `intakes.yaml` file. For instance, if you declared 4 technologies on ports `25020`, `25021`, `25022` and `25023`, the ports line the `docker-compose.yml` has to be at least `"25020-25023:25020-25023"` for TCP and `"25020-25023:25020-25023/udp"` if using UDP.

2. Verify that traffic is incoming from your log source, **meaning no firewall is blocking the events**.
    ```bash
    sudo tcpdump -c10 -nn src <remote_ip> -vv
    ```

    `remote_ip`is the IP from which the logs should be incoming.

3. If you are sure that no firewall blocks the events but you still don't see any logs, verify on the source that you are forwarding the logs to the right IP and port using the correct protocol.

    **Example**

    You want to forward your firewall logs to Sekoia. You decided to use the `TCP/20524` port.

    * Check in the settings of the firewall that you have activated the log forwarding to the IP of the forwarder and the `TCP/20524` port.
    * Verify in the `docker-compose.ym`l` file of the forwarder that there is a range including the TCP/20524 port like `"25020-25030:25020-25030"`.
    * Check in the file `intakes.yaml` that there is an entry for this port:
        ```
        - name: Firewall_techno
        protocol: tcp
        port: 20524
        intake_key: INTAKE_KEY_FOR_THE_FIREWALL
        debug: True
        ```

### Step 3: Verify everything is correctly configured to forward events to Sekoia.io

1. Check the Intake key you wrote in `intakes.yaml` is correct.

2. Check the network flow between the Forwarder host and Sekoia is opened to the destination `intake.sekoia.io` through the protocol `TCP` and port `10514`. You can easily check it with `telnet`:
    ```bash
    sudo apt install telnet && telnet intake.sekoia.io 10514
    ```

    This command should return the following answer, meaning the network flow is opened:

    ```bash
    Connected to intake.sekoia.io.
    Escape character is '^]'.
    ```

    Remove `telnet` if don't need it anymore

    ```bash
    sudo apt remove telnet
    ```

3. Finally check the status of the Sekoia.io plateform on [https://status.sekoia.io](https://status.sekoia.io).

## Additional information

The image used to run the concentrator is maintained on [this github repository](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator). Feel free to contribute and make a pull request to improve the concentrator!

## How to update the concentrator
Docker uses the notion of tag to identify the version of an image. The tag is always referenced in line starting with `image` in `docker-compose.yml`:

```
image: ghcr.io/sekoia-io/sekoiaio-docker-concentrator:2.6.0
```

`2.6.0` means the version used by `docker compose` is 2.6.0. You can find all the versions available on the GitHub repository [here](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator/pkgs/container/sekoiaio-docker-concentrator/versions?filters%5Bversion_type%5D=tagged)

To update the concentrator, just change the tag in `docker-compose.yml`, then recreate the concentrator with the command:
```bash
sudo docker compose up -d
```

There is a special tag called `latest` which always refers to the latest version. If you use this tag, every time the concentrator will be recreated, the image will be updated to the latest version.

!!! Important
    Be very careful if you use the tag `latest` in production! If a major change is present in a new version, it could break your current concentrator with the settings in place.

!!! Important
    Each image version is also updated every week in order to update the OS contained in the image with the latest security patches. You are responsible for recreating the concentrator periodically to initiate the image update.


## How do I add a new Intake later?
To add a new Intake, it's very simple ! Follow these steps:

1. Edit the `intakes.yaml` file and add the new intake
    ```yaml
    - name: NewIntake
      protocol: tcp
      port: 20519
      intake_key: INTAKE_KEY_FOR_NEW_INTAKE
    ```
2. Edit the `docker-compose.yml` file if needed and modify the `ports` section according to the `intakes.yaml` file. It shouldn't be necessary from port `20516` to `20566`
    ```yaml
    ports:
    - "20516-20566:20516-20566"
    - "20516-20566:20516-20566/udp"
    ```
3. Recreate the concentrator by running the command:
    ```bash
    sudo docker compose up -d
    ```
4. Check in the concentrator logs that the new Intake is taken into account
    ```bash
    sudo docker compose logs | more
    ```

## Docker Engine installation

This section describes how to install Docker using the `apt` repository on one of those Debian 64-bit versions:

* Debian Bullseye 11 (stable)
* Debian Buster 10 (oldstable)

All of the installation steps come from the [official Docker Engine installation for Debian](https://docs.docker.com/engine/install/debian/). Feel free to consult the official installation page for more information.
To install Docker on another Linux OS, please consult the [official Docker documentation](https://docs.docker.com/engine/install/)

### Uninstall old versions (if applicable)

Run the following command to uninstall old Docker versions:

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### Set up the repository

1. Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS

    ```bash
    sudo apt-get update
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    ```

2. Add Docker's official GPG key

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

1. Update the `apt` package index

    ```bash
    sudo apt-get update
    ```

2. Install Docker Engine, containerd, and Docker compose

    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

3. Verify that the Docker Engine installation is successful by running the hello-world image

    ```bash
    sudo docker run hello-world
    ```

## 5 minutes setup on Debian

!!! Warning
    This script will automate all the steps detailed on this page **for a Debian host**. Please read  the content of this page carefully before executing it.

Connect to the remote server where you would like to install the Sekoia.io Forwarder, then follow those steps:

1. Execute a script to setup the docker

    ```bash
    wget https://raw.githubusercontent.com/SEKOIA-IO/documentation/main/docs/assets/operation_center/ingestion_methods/sekoiaio_forwarder/sekoiaio_docker_concentrator_autosetup.sh
    chmod +x sekoiaio_docker_concentrator_autosetup.sh
    ./sekoiaio_docker_concentrator_autosetup.sh
    rm sekoiaio_docker_concentrator_autosetup.sh
    ```

2. Edit the configuration files

    - `sekoiaio-concentrator/intakes.yaml` by replacing the `name`, `protocol`, `port` and `intake_key` for each intake you would like to collect
    - `sekoiaio-concentrator/docker-compose.yml` by replacing the value `"20516-20518:20516-20518"` by a relevant content according to the `sekoiaio-concentrator/intakes.yaml` previously edited

3. Start the docker

    Follow the process you can find on the section [Start the concentrator](#start-the-concentrator) of this page.
    ```bash
    sudo docker compose up -d
    sudo docker compose ps
    sudo docker compose logs -f
    ```

Enjoy your docker!
