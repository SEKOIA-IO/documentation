# Secure forwarder inputs with TLS

The Sekoia.io Forwarder encrypts traffic between the forwarder and Sekoia with TLS by default. You can also enable TLS between a log source and a specific forwarder input by configuring a certificate and setting the intake protocol to `tls`.

## Prerequisites

Before you start, make sure that:

- The Sekoia.io Forwarder is deployed. See [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md).
- You have access to the forwarder host with `sudo` privileges.
- The source can send syslog over TLS to the selected port.

!!! note "TLS scope"

    Setting `protocol: tls` encrypts the connection between the source and the forwarder. The forwarder-to-Sekoia connection remains encrypted with TLS regardless of the input protocol.

## Generate a certificate

1. Create the certificate directory:

    ````bash
    mkdir certs && cd certs
    ````

2. Install OpenSSL if needed. On Debian or Ubuntu, run:

    ````bash
    sudo apt update && sudo apt install -y openssl
    ````

    On Fedora, Red Hat, or CentOS with `yum`, run:

    ````bash
    sudo yum update && sudo yum install -y openssl
    ````

    On Fedora, Red Hat, or CentOS with `dnf`, run:

    ````bash
    sudo dnf update && sudo dnf install -y openssl
    ````

3. Generate a self-signed certificate valid for five years:

    ````bash
    openssl req -x509 \
        -sha256 -days 1825 \
        -nodes \
        -newkey rsa:4096 \
        -keyout server.key -out server.crt
    ````

4. Restrict access to the key and certificate:

    ````bash
    chmod 600 server.key server.crt
    ````

!!! warning "Use a certificate trusted by your sources"

    The example creates a self-signed certificate. Confirm that every log source trusts it before using this configuration in production.

## Mount the certificate directory

Add the certificate mount to the `volumes` section of `docker-compose.yml`:

````yaml
volumes:
  - ./certs:/certs
  - ./intakes.yaml:/intakes.yaml
  - ./disk_queue:/var/spool/rsyslog
````

## Enable TLS for an intake

Set `protocol: tls` for the selected intake in `intakes.yaml`:

````yaml
- name: Techno1
  protocol: tls
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
````

The forwarder reads the default files `/certs/server.key` and `/certs/server.crt`.

To use different filenames, set the TLS file names explicitly:

````yaml
- name: Techno1
  protocol: tls
  port: 20516
  intake_key: INTAKE_KEY_FOR_TECHNO_1
  tls_key_name: server
  tls_cert_name: server
  tls_ca_name: server
````

Restart the forwarder after changing the configuration:

````bash
sudo docker compose up -d
````

## Result

The selected input accepts syslog over TLS, and the forwarder continues to send events to Sekoia over its encrypted output connection.

## Related articles

- [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md): How to deploy and configure the forwarder.
- [Route multiple technologies through one port](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md): How to route shared-port syslog traffic with custom rsyslog rules.
