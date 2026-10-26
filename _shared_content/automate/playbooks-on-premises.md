# Local runners

Local runners are hosts in your environment where the Sekoia Endpoint Agent executes eligible playbook actions and asset connector jobs. The runner polls Sekoia for jobs and initiates every connection itself, so Sekoia Cloud does not need inbound access to the host where the local runner is installed.

Local runners were previously called **Playbook runners**. Only the name changed. Existing runners keep their identifier and configuration, appear on the **Local runners** page, and do not need to be reinstalled. The installation command still uses the `--playbook-runner` option.

!!! warning "Asset connector requirements"

    To execute an asset connector job, the local runner and the asset connector must belong to the same community, and that community must have a Reveal subscription.

    Asset connectors cannot be created in a workspace, which is the parent community an MSSP uses to manage customer communities. Assets are inventoried per customer community. To collect assets for a customer, create the asset connector and install the local runner in that customer's community.

    
## Prerequisites

### Host requirements

Install the local runner on a host that meets these minimum requirements:

- 16 GB RAM.
- 150 GB of disk space.
- 2 CPUs, with 4 CPUs recommended.

### Supported operating systems

Local runners support Linux distributions based on kernel version 3.10 or later. The following distributions are supported:

- Ubuntu 14.04 and later.
- Debian 8 and later.
- CentOS 7 and later.
- Red Hat Enterprise Linux 7 and later.

### Docker

Local runners use Docker to execute actions. Install the Docker client and Docker engine on the host before you install the local runner. See the [Docker installation documentation](https://docs.docker.com/engine/install/).

#### Podman compatibility

Some Linux distributions include Podman, which can prevent Docker from working correctly. The `podman-docker` package can also intercept Docker commands.

The local runner requires both the Docker client and the Docker engine. If Podman is installed on the host, remove it and any conflicting packages before you continue.

!!! warning "Removing container packages"
    The following commands remove container packages and local container data. Confirm that the host does not run containers that you need to keep before you execute them.

    ```bash
    sudo yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
    sudo rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
    cd ~ && rm -rf /.local/share/containers/
    ```

### Network access

The Sekoia Endpoint Agent must be able to connect to the domains required by your region. The host needs access to the following domains in the FRA1 region:

- `ghcr.io` and `githubusercontent.com` to download module images.
- `sekoia.io`, `app.sekoia.io`, `api.sekoia.io`, and `minio-symphony.prod.sekoia.io` to send execution results and store files.

Other regions use region-specific endpoints. The local runner installation instructions display the required domains for the selected region.

### Test the host

Run the following command to check Docker access and connectivity with Sekoia:

```bash
docker run ghcr.io/sekoia-io/hello-sekoia:latest
```

The command downloads a test image and checks whether the host can connect to the Docker registry and Sekoia services.

To specify a region or proxy, pass the corresponding environment variables to Docker:

```bash
docker run \
  -e region=<region> \
  -e https_proxy=<proxy_url> \
  ghcr.io/sekoia-io/hello-sekoia:latest
```

For more information, see [Regions](/getting_started/regions.md).

## Create a local runner

1. Open the **Local runners** page with the **Local runners** button at the top of the **Playbooks** page or of the **Configure > Assets** page.
2. Select **+ Local runner**.
3. In **Name of the local runner**, enter a name.
4. If the **Account’s community** field is displayed, select the customer community where you will install the runner. This field is displayed only from a parent community used by an MSSP.
5. Select **Continue**.
6. Follow the installation instructions displayed by Sekoia.

    ![Installation instructions for a new local runner](img/local_runner_setup.png)

After installation, return to **Local runners**. The new runner appears in the list with its community, last activity, hostname, and version.

![Local runners page with the + Local runner button and a runner card](img/local_runners_list.png)


### Select the right community

The community selected during local runner creation determines which capabilities are available.

| Selected community | Available capability |
| --- | --- |
| A community with a Reveal subscription | Playbook actions and eligible asset connector jobs |
| A community without a Reveal subscription | Playbook actions only |
| A workspace or parent community used by an MSSP | Playbook actions only; asset inventory is not available |

If the selected community does not have Reveal, the local runner displays a warning that it can execute playbooks but cannot execute asset connectors. Enable Reveal for the customer community before you use the local runner for asset collection.

> 📸 [SCREENSHOT SUGGESTION: Create a new local runner dialog showing the Community field and the warning about Reveal and workspace communities. | ALT TEXT: Local runner creation dialog with a community selector and an asset inventory warning.]

## Execute a playbook action with a local runner

!!! note "Playbook execution"

    Local runners execute playbook actions, not playbook triggers.

A local runner executes actions, not triggers. The action must also support on-premises execution.

1. Open the playbook that contains the action.
2. Add a new action or select an existing action.
3. Set **How to execute this action** to **On-premise**.
4. Select the local runner that should execute the action.
5. Complete the remaining action configuration.
6. Save the playbook.

The action runs on the host where the selected local runner is installed.

> 📸 [SCREENSHOT SUGGESTION: Playbook action configuration showing On-premise execution and the local runner selector. | ALT TEXT: Playbook action configuration with On-premise execution selected and a local runner chosen.]

## Execute asset connector jobs with a local runner

Local runners can execute jobs for eligible asset connectors from inside your environment. This allows the connector to reach internal systems without requiring inbound access from Sekoia Cloud.

- The asset connector supports local execution. Only some integrations support it, and custom integrations do not.
- The community of the asset connector has a Reveal subscription.
- The local runner belongs to the same community as the asset connector.
- The local runner is installed in an environment that can reach the source system.

### Select a local runner for an asset connector

You select the local runner in the asset connector configuration, when you create the connector or when you edit it. The runner is assigned per asset connector: different connectors of the same community can use different runners.

1. Create or edit the asset connector.
2. In **How do you want to execute this action**, select **On premise**. This option is displayed only for asset connectors that support local execution.
3. In **Using which local runner?**, select the local runner. The list contains the local runners of the connector's community.
4. Complete the remaining configuration and save the connector.

> 📸 [SCREENSHOT SUGGESTION: Asset connector configuration with On premise selected and the local runner selector. | ALT TEXT: Asset connector configuration dialog with On premise execution and a local runner chosen.]

The test connection button is not available for connectors executed on premise.

You can change the selected local runner at any time. To switch a connector between **Cloud** and **On premise**, stop the connector first.

### Synchronization

A connector executed on premise synchronizes once a day, and once right after it is started. If a synchronization cannot start, for example because the local runner is offline, Sekoia retries it once one hour later. A synchronization that has not finished two hours after it started is marked as failed.

Connector logs work the same way whether the connector runs in the cloud or on a local runner: the messages that the connector logs during a synchronization appear in the connector logs panel. When a synchronization fails, Sekoia also adds an error log with the message `The sync failed:` followed by the error. See [Check asset connector health](/xdr/features/collect/asset_connector_health.md).

The **Local runners** page displays a card for each runner, with the following information:

| Field | Description |
| --- | --- |
| Last activity | The last time the runner contacted Sekoia |
| Hostname | The hostname of the host where the runner is installed |
| Version | The version of the Sekoia Endpoint Agent |

A runner becomes **Offline** when it has not contacted Sekoia for one hour. The card then displays an **Offline** badge, and the runner details page displays **Your local runner is unable to reach us**. When the runner is online, the details page displays **Up & running**.

A runner usually becomes offline when the host is stopped, the Endpoint Agent service is stopped, or the host can no longer reach Sekoia, for example because of a proxy or firewall change.

### Troubleshoot a local runner

1. Check that the Endpoint Agent service is running:

    ```bash
    sudo systemctl status SEKOIAEndpointAgent.service
    ```

2. Check that Docker is running and that the host can reach Sekoia with the test command in [Test the host](#test-the-host).
3. Review the Endpoint Agent logs in `/var/log/endpoint-agent/agent.log`.

When you contact Support, provide the following information:

- The Endpoint Agent logs, in `/var/log/endpoint-agent/`.
- The configuration file `/etc/endpoint-agent/config.yaml`. Remove the `Token` value and any proxy password before you share it.
- The output of `/opt/endpoint-agent/agent --version`, which displays the agent version and identifier.

For more diagnostic steps, see [Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md).

## Permissions

Local runners belong to one community. From a parent community, an MSSP can create and list the local runners of its customer communities.

| Action | Required permissions |
| --- | --- |
| View local runners | Read playbooks and read the list of playbook runners |
| Create a local runner | Read playbooks and enroll new playbook runners |
| Assign a local runner to an asset connector | Edit asset connectors |

By default, only the **Admin** role can view and create local runners.

Local runners cannot be renamed or deleted from Sekoia. To rename a runner, change `AgentName` in `/etc/endpoint-agent/config.yaml` on the runner host and restart the Endpoint Agent: the new name appears after its next contact with Sekoia. A runner that you uninstall from its host stays in the list and is displayed as **Offline**.

## Configure proxy support

Configure a proxy when the runner host must use a proxy to reach Sekoia or services used by local actions.

1. Edit `/etc/endpoint-agent/config.yaml`.
2. Add the `HTTPProxyURL` setting.

```yaml
HTTPProxyURL: "<PROXY_URL>"
```

Use the following format for the proxy URL:

```text
http://user:pass@host:port
```

To exclude domains from proxy use, add `NoProxyDomains`:

```yaml
NoProxyDomains:
  - 127.0.0.1
  - localhost
```

Restart the Endpoint Agent after you change the configuration:

```bash
sudo systemctl restart SEKOIAEndpointAgent.service
```

If these settings are not defined, the agent checks the `http_proxy`, `https_proxy`, `all_proxy`, and `no_proxy` environment variables on the host and passes them to running actions.

## Configure a custom CA bundle

If a proxy or internal service uses a TLS certificate signed by a custom Certification Authority, configure a CA bundle so the Endpoint Agent can validate the certificate.

1. Edit `/etc/endpoint-agent/config.yaml`.
2. Add the `CABundlePath` setting.

```yaml
CABundlePath: "path/to/bundle/cacert.pem"
```

The bundle must contain the trusted CA certificates required to communicate with Sekoia.

## Related articles

- [Assets](/xdr/features/collect/assets.md): Overview of asset inventory and asset discovery methods.
- [Create an asset connector](/xdr/features/modules/reveal_asset_connectors_create.md): How to configure an asset connector from the integration catalog.
- [Check asset connector health](/xdr/features/collect/asset_connector_health.md): How to review asset connector status and logs.
- [Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to collect logs and diagnose Endpoint Agent issues.
- [Regions](/getting_started/regions.md): Reference for Sekoia regions and region-specific endpoints.
