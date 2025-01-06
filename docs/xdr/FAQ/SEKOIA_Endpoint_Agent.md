## General Questions about the Sekoia.io Endpoint Agent

### 1. **Does the Sekoia.io Endpoint Agent require Internet access to function?**

Yes, the Sekoia.io Endpoint Agent requires Internet access to send events directly to Sekoia.io via HTTPS. If your information system uses an HTTP proxy that allows access to the [HTTP intake endpoint for your region](/getting_started/regions.md), you can configure the agent to use this proxy. In the absence of direct Internet access, alternatives like **NXLog** for Windows or **Auditbeat** for Linux may be considered.

### 2. **Can events be redirected to a log forwarder without Internet access?**

No, the Sekoia.io Endpoint Agent sends events directly to Sekoia.io via HTTPS, which requires Internet access. However, an HTTP proxy can be configured to facilitate this communication if direct access is unavailable.

### 3. **Can the Sekoia.io Endpoint Agent work in a Docker environment?**

The Sekoia.io Endpoint Agent is not specifically designed for Docker environments. Operations like installation and service status verification might not function correctly in Docker. Additionally, there is no version of the agent designed for use as a Kubernetes DaemonSet.

### 4. **What happens if the Internet connection is lost?**

If the Internet connection is lost, the agent stores logs locally on disk, up to 100 MB. Once this limit is reached, the oldest logs are overwritten. When the connection is restored, the oldest logs are sent to Sekoia.io first.

### 5. **Can the Sekoia.io Endpoint Agent be configured with an HTTP proxy?**

Yes, the agent supports HTTP proxy for its HTTPS requests. You can configure the proxy by modifying the `config.yaml` file. Refer to the documentation for more details on proxy configuration.

### 6. **How often are events sent to Sekoia.io?**

Events are sent to Sekoia.io when one of the following conditions is met:
- A batch contains 250 events.
- 5 seconds have elapsed since the first event was added to the batch.

### 7. **Which operating systems are supported by the Sekoia.io Endpoint Agent?**

The agent is compatible with the following 64-bit operating systems:
- **Windows**
- **Linux**
- **MacOS**

For a detailed list of supported versions, please refer to [this link](/integration/categories/endpoint/sekoiaio.md).

### 8. **Can the agent be uninstalled?**

Yes, the agent can be uninstalled. Refer to [this page](/integration/categories/endpoint/sekoiaio.md#uninstall) for the command corresponding to your operating system. For versions earlier than 0.3.0, you must stop and uninstall the service before deleting the agent’s directories. Detailed instructions are available in the [documentation](/integration/categories/endpoint/sekoiaio.md).

### 9. **How does the automatic update feature of the agent work?**

By default, the agent updates automatically. To disable this feature, use the `--disable-auto-update` option during installation. To update manually, execute the appropriate command for your operating system, available [here](/integration/categories/endpoint/sekoiaio.md#manual-update) .

### 10. **How to diagnose a problem with the agent installation?**

To diagnose issues, check the agent’s logs located at:
- **Windows** (default): `C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\logs\agent.log`
- **Linux/MacOS** (default): `/var/log/endpoint-agent/agent.log`

These logs provide valuable information for troubleshooting. If needed, contact Sekoia.io support for assistance.

---

## Specific Features and Use Cases

### 1. **Can the Sekoia.io Endpoint Agent (Windows) retrieve events linked to file accesses such as denied access or modifications?**

The agent tracks information on file creation and deletion but not for denied or modified access. However, an event might be linked to a process attempting to access a file.

### 2. **Is it possible to add a Windows Event ID to a file loaded by the Sekoia.io Agent?**

No, it is not possible to add an Event ID. Each Event ID is formatted to align with Sekoia.io’s Taxonomy (ECS norm). However, suggestions for additional Event IDs to collect are welcome.

### 3. **Can the agent retrieve events linked to blocked accounts in Active Directory (AD)?**

Not at this time. This capability has been identified as an area for improvement in the agent’s integration with AD.

### 4. **What are the new features in Sekoia.io Agent version 0.2.8?**

Version 0.2.8 introduces:
- Automatic agent updates
- Improved integration with rules produced by Sekoia.io analysts
- Support for new event types

### 5. **Does the Sekoia.io Endpoint Agent collect DNS logs?**

Yes, DNS logs are collected in the Windows version via system calls. This feature is not currently available in the Linux version.

### 6. **Will there be duplicate events when using the Sekoia.io Agent and Sysmon?**

For some events, the agent ignores Sysmon events as it already covers the same scope. Examples include:
- sysmonProcessCreation
- sysmonNetworkConnection
- sysmonProcessTerminated
- sysmonCreateRemoteThread
- sysmonFileCreate
- sysmonDNSEvent
- sysmonFileDelete
- sysmonFileDeleteDetected

### 7. **Does the agent comply with ANSSI recommendations without Sysmon?**

We aim to cover all ANSSI recommendations and SEKOIA rules comprehensively in future beta versions.

### 8. **Will the Sysmon option be removed?**

We plan to continue supporting Sysmon for users who wish to use it.

### 9. **Is the agent suitable for monitoring Docker or Kubernetes hosts?**

The agent, based on Auditd, effectively monitors system activities on Linux hosts, including those running Docker or Kubernetes. While it captures some container-related activities (e.g., DNS requests or file accesses on the host), it is not designed specifically for Docker or Kubernetes and may lack the granularity of specialized tools.

---

### **Useful Links:**
- [Sekoia.io Endpoint Agent Documentation](/integration/categories/endpoint/sekoiaio.md)

