# Troubleshoot the Sekoia.io Forwarder

Use this procedure when the Sekoia.io Forwarder is not receiving events, does not forward events, or fails to start. Check the local configuration and input traffic first, then verify the connection to the Sekoia regional endpoint.

## Prerequisites

Before you start, make sure that:

- You have access to the forwarder host with `sudo` privileges.
- You can read `docker-compose.yml` and `intakes.yaml`.
- You know the source IP address, destination port, and protocol used by the affected log source.

## Check the forwarder version

Sekoia releases new forwarder images regularly. Check the image tag in `docker-compose.yml` and compare it with the available versions in the [GitHub Container Registry](https://github.com/SEKOIA-IO/sekoiaio-docker-concentrator/pkgs/container/sekoiaio-docker-concentrator/versions?filters%5Bversion_type%5D=tagged).

## Check that the forwarder receives events

1. Enable debug logging for the affected intake in `intakes.yaml`:

    ````yaml
    - name: Techno2
      protocol: tcp
      port: 20517
      intake_key: INTAKE_KEY_FOR_TECHNO_2
      debug: True
    ````

2. Recreate the container:

    ````bash
    sudo docker compose down
    sudo docker compose up -d
    ````

3. Stream logs for the affected intake:

    ````bash
    sudo docker compose logs -f | grep "YOUR_INTAKE_KEY"
    ````

If no events appear, check the following:

- `intakes.yaml` declares the protocol and port used by the source.
- The same port is exposed in the `ports` section of `docker-compose.yml`. For example, a port range from `25020` to `25023` requires at least `"25020-25023:25020-25023"`.
- A firewall allows traffic from the log source to the forwarder.
- The source sends events to the correct forwarder IP address and port.

To check whether traffic reaches the host, run:

````bash
sudo tcpdump -c 10 -nn src <remote_ip> -vv
````

Disable debug logging after testing.

## Check connectivity to Sekoia

1. Confirm that the intake key in `intakes.yaml` is correct.
2. Test the outbound connection to the regional endpoint:

    ````bash
    sudo apt install telnet
    telnet intake.sekoia.io 10514
    ````

3. Confirm that a successful connection returns:

    ````text
    Connected to intake.sekoia.io.
    Escape character is '^]'.
    ````

4. Remove Telnet after testing:

    ````bash
    sudo apt remove telnet
    ````

5. Check the [Sekoia status page](https://status.sekoia.io/).

!!! note "Use the endpoint for your region"

    Replace `intake.sekoia.io` with the regional host configured by `REGION` when you test a non-FRA1 deployment.

## Check container logs

View all logs:

````bash
sudo docker compose logs
````

Stream logs while reproducing the issue:

````bash
sudo docker compose logs -f
````

Check the container status:

````bash
sudo docker compose ps
````

If the container fails after you add a custom rsyslog file, see [Route multiple technologies through one port](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md) for syntax and listener checks.

## Result

You have identified whether the problem is caused by the source configuration, the forwarder's port mapping, a firewall, an intake key, or the outbound connection to Sekoia.

## Related articles

- [Configure the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md): How to deploy and configure the forwarder.
- [Route multiple technologies through one port](/integration/ingestion_methods/syslog/route_multiple_technologies_through_one_port.md): How to troubleshoot custom shared-port routing.
- [Monitor the Sekoia.io Forwarder](/integration/ingestion_methods/syslog/monitor_the_sekoiaio_forwarder.md): How to send forwarder health metrics to Sekoia.
