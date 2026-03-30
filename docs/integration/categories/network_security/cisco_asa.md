# cisco\_asa

uuid: 466aeca2-e112-4ccc-a109-c6d85b91bbcf name: Cisco Secure Firewall type: intake

### Overview

The Cisco Secure Firewall (formerly Next-Generation Firewall) is a security product designed to protect your network, from physical ones to those hosted in the cloud.

* **Vendor**: Cisco
* **Supported environment**: On Premise
* **Version compatibility, if applicable**:
* **Detection based on**: Security Alerts, Telemetry, Admin
* **Supported application or feature**:
  * **Adaptive Security Appliance (ASA)**: Combines firewall, antivirus, intrusion prevention, and virtual private network (VPN) capabilities.
  * **Firepower Threat Defense (FTD)**: A unified software image that includes the Cisco ASA features and FirePOWER Services. This unified software offers both ASA and FirePOWER functionalities on one platform, in terms of both hardware and software features.
  * **Next Generation IPS (NGIPS)**: Detects and stops intrusions in your internal network or public cloud. NGIPS helps you to mitigate vulnerabilities and manage patch applications.

### High-Level Architecture Diagram

* **Type of integration**: Outbound (PUSH to Sekoia.io)
* **Schema**

{: style="max-width:100%"}

### Specification

#### Prerequisites

* **Resource**:
  * Self-managed syslog forwarder
* **Network**:
  * Outbound traffic allowed
* **Permissions**:
  * Administrator or Root access to the Cisco Secure Firewall appliance
  * Root access to the Linux server with the syslog forwarder

#### Transport Protocol/Method

* **Indirect Syslog**

#### Logs details

* **Supported functionalities**: See section [Overview](cisco_asa.md#overview)
* **Supported type(s) of structure**: Plain text
* **Supported verbosity level**: Alert, Warning, Informational

!!! Note Log levels are based on the taxonomy of [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424). Adapt according to the terminology used by the editor.

### Step-by-Step Configuration Procedure

#### Instructions on the 3rd Party Solution

**Configure Cisco Secure Firewall Logs**

*   On Cisco appliances, most of the important hardware and software activities that are relevant for security detection and analysis can be enabled by one simple command:

    ```bash
    hostname(config)# logging enable
    hostname(config)# logging timestamp
    hostname(config)# logging trap informational
    ```

**Configure the Cisco Appliance for Log Forwarding**

*   To forward logs to a syslog concentrator:

    ```bash
    hostname(config)# show interface
    hostname(config)# show hostname
    hostname(config)# logging host interface_name syslog_ip [ tcp[/ port ] udp [/ port ] ]
    ```
*   Example:

    ```bash
    hostname(config)# logging host interface_1 127.0.0.1 udp
    ```
* Explanation:
  * The `interface_name` specifies the interface through which you access the syslog server.
  * The `syslog_ip` specifies the IP address of the syslog server.
  * The `tcp[/ port ]` or `udp[/ port ]` keyword specifies whether TCP or UDP is used to send syslog messages. The default is UDP on port 514.

!!! Note If you specify TCP, the ASA discovers when the syslog server fails and as a security protection, new connections through the ASA are blocked. If you specify UDP, the ASA continues to allow new connections whether or not the syslog server is operational. Valid port values for either protocol range from 1025 through 65535. The default UDP port is 514, and the default TCP port is 1470. For more information about Cisco ASA logging, please refer to your [Cisco documentation](https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S.html).

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

{!\_shared\_content/integration/forwarder\_configuration.md!}

{!\_shared\_content/operations\_center/integrations/generated/466aeca2-e112-4ccc-a109-c6d85b91bbcf\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_466aeca2-e112-4ccc-a109-c6d85b91bbcf\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/466aeca2-e112-4ccc-a109-c6d85b91bbcf.md!}

### Further readings

* [Cisco ASA Command Reference](https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/S/asa-command-ref-S.html).
