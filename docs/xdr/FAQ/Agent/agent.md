# Questions about the agent

### 1. **Does the Sekoia.io agent require Internet access to operate?**

Yes, the Sekoia.io agent requires Internet access to send events directly to Sekoia.io via HTTPS. If your information system uses an HTTP proxy that allows access to the [HTTP intake endpoint for your region](https://docs.sekoia.io/getting_started/regions/), you can configure the agent to route through this proxy. In cases where direct Internet access is unavailable, alternatives like **NXLog** for Windows or **Auditbeat** for Linux can be considered.

### 2. **Can events be redirected to a log forwarder without Internet access?**

No, the Sekoia.io agent sends events directly to Sekoia.io via HTTPS and therefore requires Internet access. However, as mentioned above, an HTTP proxy can be used if properly configured.

### 3. **Can the Sekoia.io agent operate in a Docker environment?**

The Sekoia.io agent is not specifically designed to operate in a Docker environment. Installation and service status checks might not function correctly in Docker. Additionally, there is no version of the agent optimized for use as a Kubernetes DaemonSet.

### 4. **What happens if Internet connectivity is lost?**

If Internet connectivity is lost, the agent stores logs locally on disk with a maximum space allocation of 100 MB. Once this limit is reached, the oldest logs are overwritten by newer ones. When the connection is restored, the oldest logs are sent first to Sekoia.io.

### 5. **Can the Sekoia agent be configured to use an HTTP proxy?**

Yes, the Sekoia.io agent supports HTTP proxy for its HTTPS requests. You can configure the agent to use a proxy by modifying the `config.yaml` file. Refer to the documentation for more details on proxy configuration.

### 6. **How often are events sent to Sekoia.io?**

Events are sent to Sekoia.io when either of the following conditions is met:

- The batch contains 250 events.
- 5 seconds have elapsed since the first events were added to the batch.

### 7. **What operating systems are supported by the Sekoia.io agent?**

The Sekoia.io agent is compatible with the following 64-bit operating systems:

- **Windows**
- **Linux**
- **macOS**

For a complete list of supported versions, consult this link.

### 8. **Can the agent be uninstalled?**

Yes, it is possible to uninstall the agent.

To uninstall the agent, refer to [this page](/integration/categories/endpoint/sekoiaio.md#uninstall) to find the appropriate command for your operating system.

For versions prior to 0.3.0, it is necessary to stop and uninstall the service before deleting the directories created by the agent. Detailed instructions can be found in our [documentation](https://docs.sekoia.io/integration/categories/endpoint/sekoiaio/).

### 9. **How does the Sekoia.io agent's auto-update feature work?**

By default, the Sekoia.io agent updates automatically. If you want to disable this feature, use the `--disable-auto-update` option during installation.

To manually update the agent, run the command specific to your operating system available at the following [page](/integration/categories/endpoint/sekoiaio.md#manual-update) 

This command will update the agent to the latest version.

### 10. **What are the first steps for diagnosing an issue with the Sekoia.io agent installation?**

To diagnose an issue, start by checking the agent logs. These logs can be found at the following locations depending on your operating system:

- **Windows** (default): `C:\Windows\System32\config\systemprofile\AppData\Local\SEKOIA.IO\EndpointAgent\logs\agent.log`
- **Linux/macOS** (default): `/var/log/endpoint-agent/agent.log`

If you cannot locate the log file, check your configuration.

These logs provide valuable information for identifying and resolving issues. If necessary, contact Sekoia.io technical support for additional assistance.

---

### **Useful Link:**

- [Sekoia.io Endpoint Agent Documentation](/integration/categories/endpoint/sekoiaio.md)