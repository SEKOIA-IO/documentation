# Sekoia Endpoint Agent

_**[Reveal module](/xdr/features/modules/reveal_index.md)**. This feature requires the Reveal add-on module._

## Overview

The Sekoia Endpoint Agent can report the software installed on each host where it runs. Reveal adds this inventory to the host asset, in its **Applications** tab, and matches the applications against known vulnerabilities.

Unlike the other software connectors, there is no asset connector to create: the agent sends the inventory itself once its software collection role is enabled.

- **Vendor**: Sekoia.io
- **Product**: Sekoia Endpoint Agent
- **Supported environment**: Windows, Linux and macOS hosts

## Prerequisites

- The Reveal module on your community.
- The Sekoia Endpoint Agent, version 1.12.0 or later, installed with an intake key. See [Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md).

## Configure

Enable the `software-collector` role on the agent, either with the `--software-collector` option at installation or in the agent configuration file afterwards. See [Collect additional host asset context](/integration/categories/endpoint/install_sekoia_endpoint_agent.md#collect-additional-host-asset-context).

`software-collector` is the only role the Applications tab needs. The `event-collector` and `compliance-collector` roles are recommended for the other Reveal features.

## Collected data

For each installed application, the agent reports its name, version, vendor, install path and install date, when the operating system provides them. It reads:

| Operating system | Source |
| --- | --- |
| Windows | Programs registered as installed (the `Uninstall` registry keys) |
| Linux | Packages of the `dpkg`, `rpm` and `pacman` package managers |
| macOS | Installed applications, including the name of their executable |

## Refresh and limits

- The agent reads the inventory every 24 hours and sends it only when it changed, with a full send at least every 7 days. A newly installed application can therefore take up to a day to appear.
- An application the agent no longer reports for 14 days is considered uninstalled: it leaves the Applications tab, and its vulnerabilities are marked as remediated. An agent that stops reporting, for instance on a host that is turned off, keeps its last inventory.
- Only the sources above are read. Software installed another way, such as a portable executable, an archive extracted by hand, or a Snap or Flatpak package, is not reported.

## Further reading

- [Application inventory](/xdr/features/modules/reveal_applications.md): use the Applications tab of a host asset.
- [Troubleshoot application inventory](/xdr/FAQ/troubleshoot_application_inventory.md): the Applications tab is empty or unavailable.
