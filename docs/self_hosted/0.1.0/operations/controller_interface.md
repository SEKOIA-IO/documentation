# Use the controller interface

The Self-Hosted Controller (SHC) ships with an interactive terminal interface that runs the same commands as the one-shot CLI and adds live views of your nodes, your cluster, your storage, and your platform diagnostics. This article explains how to open it, how to navigate it, and what each tab reports.

## Prerequisites

- You have access to the orchestration node.
- The SHC Docker image is loaded and the `run-shc.sh` execution script is in place. See [Deploy the platform](../deployment/deployment_guide.md).
- Your terminal is attached to a TTY. The `run-shc.sh` script in [Deploy the platform](../deployment/deployment_guide.md) allocates one automatically when it runs in a terminal.
- For the Kubernetes, Storage, and Diagnostics tabs, the cluster is installed and the SHC holds a valid kubeconfig. Run `GetKubeconfig` if it does not.

!!! note "Same commands, two front-ends"
    The interface and the one-shot CLI share one command implementation. Anything you run as `./run-shc.sh exec <Module>` behaves identically when typed in the interface, and the reverse is also true. Use the one-shot CLI for scripted or unattended runs.

## Open the interface

To open the interface, run the execution script with no command:

```bash
./run-shc.sh
```

The interface opens on the **Controller** tab. Passing a command instead, such as `exec`, `list`, `help`, or `config`, keeps the SHC in one-shot mode and returns to your shell when the command completes.

> 📸 [SCREENSHOT SUGGESTION: The controller interface on the Controller tab, showing the log panel, the command input docked at the bottom, the log file path, and the tab bar with Controller, Machines, Kubernetes, Storage, and Diagnostics. | ALT TEXT: The SHC interactive interface on the Controller tab.]

## Navigate the interface

| Key | Action |
| :--- | :--- |
| `Shift+Tab` | Move to the next tab. |
| `Ctrl+C` | Cancel the command in progress, then quit the interface and restore the terminal. |
| `Escape` | Return to the target list from a diagnostic result view. |
| `Shift+Down` | Move to the next diagnostic result panel. |
| `Shift+Up` | Move to the previous diagnostic result panel. |

Every run writes a timestamped log file, whose path is displayed at the bottom of the interface. Attach that file when you escalate an issue to Sekoia support.

## Run a command from the Controller tab

The Controller tab pairs a log panel with a command input. It accepts the same commands as the one-shot CLI:

| Command | Description |
| :--- | :--- |
| `exec <Module>` | Execute a module. |
| `exec <Module> --set KEY=VALUE` | Execute a module with runtime configuration overrides. |
| `list` | List the available modules. |
| `help <Module>` | Show the runtime overrides a module accepts. |
| `config help [prefix]` | Show the configuration reference. |
| `config show [prefix]` | Show the computed configuration. |
| `quit` | Close the interface. |

To run a command, enter it in the input and press `Enter`. Module output and log lines are interleaved in the log panel, in real time.

While you type, the input suggests a matching command. Press `Tab` to accept the suggestion, and press `Tab` again to cycle through the other matches. Press `Up` and `Down` to browse the commands you already ran.

The interface runs one command at a time. A command submitted while another is still running is rejected rather than queued, and the interface tells you to wait for the first one to finish.

To copy the visible output, right-click the log panel. The interface copies the lines currently in the viewport to your clipboard and confirms with a notification.

### Follow the platform installation

While `PlatformInstallation` runs, a progress bar replaces the command input and reports the completion percentage, the current step, the active provisioner, and the number of completed steps out of the total. The bar disappears when the module completes, and the command input returns.

## Read the Machines tab

The Machines tab shows one card per host in `utils.ansible.inventory`, titled with the host address. Each card reports the live CPU, RAM, and disk usage of the host as a progress bar, alongside the core count and the device paths, plus the load average.

Bar colors indicate how close a metric is to saturation: green below 70%, yellow from 70%, and red from 90%. A host that cannot be reached is reported as such on its own card.

The cards are laid out on a responsive grid, recomputed when you resize the terminal, and refreshed every 60 seconds. The data comes from the read-only `GetServerStatus` module, which changes nothing on the hosts.

## Read the Kubernetes tab

The Kubernetes tab renders three `kubectl` views of the cluster:

| Panel | Command |
| :--- | :--- |
| Nodes | `kubectl get nodes` |
| Pods update | `kubectl get pods -A -w`, streamed continuously |
| Pods not running | Every pod that is neither `Running` nor `Completed` |

Use the Pods not running panel first when the platform misbehaves: an empty panel means no pod is stuck.

## Read the Storage tab

The Storage tab reports the state of the Ceph cluster through three stacked panels, each refreshed every 30 seconds:

| Panel | What it reports |
| :--- | :--- |
| Ceph status | Overall cluster health, monitors, managers, OSDs, and current activity (`ceph -s`). |
| OSD usage | Per-OSD capacity and utilization (`ceph osd df`). |
| OSD tree | The OSD topology per host (`ceph osd tree`). |

The panels run against the `rook-ceph-tools` deployment in the `rook-ceph` namespace, so they need a healthy cluster and a valid kubeconfig.

## Run a diagnostic from the Diagnostics tab

The Diagnostics tab lists the diagnostic targets available on the SHC, one per rule file.

To run a target:

1. Select the tab with `Shift+Tab` until **Diagnostics** is active.
2. Select a target in the **Available diagnostics** list and press `Enter`.

The interface opens a result view with one collapsible panel per rule of that target, in file order. Each panel starts as `NOT_STARTED`, switches to `RUNNING` while its rule is evaluated, and ends on `OK`, `WARN`, or `CRIT`. Rules are evaluated one at a time, and the first panel to reach a result is focused automatically so you can navigate from the keyboard.

A completed panel holds a results table with the measured values and their labels, and a **Likely causes & remediation** section. Sort the table by selecting a column header. To copy the full report of the current run to your clipboard, right-click the result view or the table.

To return to the target list, press `Escape`.

!!! note "No diagnostics listed"
    When the tab reports that no diagnostics were found, the rule files are missing from the SHC image. Verify the image reference you set in `DOCKER_IMAGE`, then contact Sekoia support with the path shown in the warning.

## Result

You can drive the SHC, follow an installation, inspect your nodes, your cluster and your storage, and run platform diagnostics from a single interface, without leaving the orchestration node.

## Related links

- [The deployment process](../deployment/deployment_process.md): The modules the SHC exposes and the installation execution plan.
- [Run platform diagnostics](../monitoring/run_diagnostics.md): The diagnostic targets and how to read a result.
- [Debug your deployment](../troubleshooting/debug_tool.md): Full SHC debug command reference with remediation steps.
- [Monitor your platform](../monitoring/monitoring_guide.md): Observability stack and daily monitoring workflows.
