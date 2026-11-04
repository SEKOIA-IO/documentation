# Run the Sekoia Endpoint Agent alongside other software

The Sekoia Endpoint Agent runs next to other software on your hosts: antivirus and EDR products, backup tools, browsers and their extensions. This article explains what you can expect from the agent, how to allow it in your security tools, and the interactions we know of.

## What to expect

| Situation | Example | What to do |
| --- | --- | --- |
| The agent prevents another program from working | A backup or an update fails because the agent keeps a file open | Apply the workaround in [A program cannot rename or delete a file](#a-program-cannot-rename-or-delete-a-file-windows). If the issue persists, contact the support: this is an issue with the agent. |
| Another program, or a limit of the operating system, prevents the agent from collecting | An EDR blocks the agent, Windows refuses one of its trace sessions, or `auditd` holds the Linux audit framework | Allow the agent in that program, or follow the matching entry in [Known interactions](#known-interactions). |
| The agent reads events from a third-party tool | Sysmon events forwarded by the agent | The third-party tool itself is not supported by Sekoia. |

The agent is designed not to interfere with other programs. It cannot, however, be compatible with every configuration of every security product: when another product blocks or restricts it, that product must be configured to allow the agent.

## Allow the agent in your security tools

If an antivirus or EDR product runs on the host, add the agent to its allow list so that it is not blocked, quarantined or slowed down.

=== "Windows"

    | Item | Path |
    | --- | --- |
    | Executable | `C:\Program Files\EndpointAgent\agent.exe` |
    | Data, configuration and logs | `C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent` |
    | Configuration backup | `C:\ProgramData\SEKOIA.IO\EndpointAgent` |

=== "Linux"

    | Item | Path |
    | --- | --- |
    | Executable | `/opt/endpoint-agent/agent` |
    | Configuration | `/etc/endpoint-agent` |
    | Data | `/var/lib/endpoint-agent` |
    | Logs | `/var/log/endpoint-agent` |

=== "macOS"

    | Item | Path |
    | --- | --- |
    | Application | `/Applications/SekoiaEndpointAgent.app` |
    | Configuration | `/etc/endpoint-agent` |
    | Data | `/var/lib/endpoint-agent` |
    | Logs | `/var/log/endpoint-agent` |

The agent also connects to Sekoia over HTTPS: see the [network prerequisites](/integration/categories/endpoint/sekoiaio.md#prerequisites).

## Known interactions

### A program cannot rename or delete a file (Windows)

**Symptoms:** a backup, an update or an installation fails because a file cannot be moved or deleted; temporary files pile up and fill the disk; a browser cannot install an extension.

**Cause:** the agent computes the hashes of new files. It reads them in a way that lets other programs rename or delete them at the same time, so it should not block them. Older agent versions did block them while they computed the hash: [update the agent](/integration/categories/endpoint/update_uninstall_sekoia_endpoint_agent.md) first.

**If the issue persists:** some programs move a whole directory at once, which Windows can still refuse while a file inside it is open. Exclude the directory where the program writes its temporary files from hash computation, with the `HashesExcludedPaths` option. See [Exclude directories from hash computation](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md#exclude-directories-from-hash-computation). Keep the exclusion as narrow as possible, for example a dedicated directory or a file extension, since files under an excluded path get no hashes.

### Process creation and termination events are missing (Windows)

**Symptoms:** a host no longer sends process creation and termination events, while its other events still arrive.

**Cause:** the agent collects these events through a kernel trace session (ETW). Windows only allows a limited number of kernel trace sessions at the same time, and other security products use them too. When none is left, the agent logs the following error and tries again every 5 minutes:

```
{"level":"error","error":"StartTraceW failed; Insufficient system resources exist to complete the requested service.","session_name":"Generic.Kernel.Tracing.Session","retry_in":300000,"time":"...","message":"Could not create ETW trace"}
```

**What to do:**

1. Look for this error in the [agent logs](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md#check-the-agent-logs). Since the agent sends its logs to Sekoia, you can also be alerted when it appears.
2. List the trace sessions running on the host with `logman query -ets`, in a command prompt run as administrator.
3. Check with the vendors of the other products whether some of their sessions can be disabled. Once a session slot is free, the agent creates its session within 5 minutes and process events come back, without restarting the agent.

### The agent does not start (Linux)

**Symptoms:** the agent does not start, or the host sends no events.

**Cause:** the agent collects events through the Linux audit framework. It cannot work while `auditd` is running, or while another service, such as `journald`, listens to the audit socket.

**What to do:** stop and disable the conflicting services, then restart the agent, as described in [The agent does not start on Linux](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md#the-agent-does-not-start-on-linux).

### Alerts raised on the actions of an EDR

If the host runs an EDR, its own detection and response actions generate events that the agent collects, and some detection rules may raise false positive alerts. See the warning in [Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md).

### Sysmon

The agent forwards Sysmon events when Sysmon is installed, and ignores the Sysmon events it already produces itself. Sysmon is a Microsoft tool and is not supported by Sekoia. See [Install Sysmon](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md#install-sysmon-windows-only) and the [agent FAQ](/xdr/FAQ/SEKOIA_Endpoint_Agent.md).

## Report an issue

When you contact the support about an interaction with another program, send:

- the agent version (`agent --version`, or `agent.exe --version` on Windows);
- the [agent logs](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md#check-the-agent-logs) covering the time of the issue;
- the list of security products running on the host (antivirus, EDR, backup), with their versions;
- for missing process events on Windows, the output of `logman query -ets`.

## Related articles

[Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): How to set up log file collection, proxy, retention, and optional features.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to check the logs, use the CLI, and identify common errors.
