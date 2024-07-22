uuid: e8ca856f-8a58-490b-bea4-247b12b3d74b
name: OpenVPN
type: intake

## Overview
- **Vendor**:
- **Plan**: Core + Prime
- **Supported environment**:
- **Version compatibility**:
- **Detection based on**: Telemetry
- **Supported application or feature**:

OpenVPN is an open-source virtual private network (VPN) software, offering robust encryption, secure connectivity, flexible and reliable remote access to networks for individuals and businesses globally.



## Configure

This setup guide will show you how to forward your OpenVPN logs to Sekoia.io by means of a syslog transport channel.

### Prerequisites

- Have an internal log concentrator (Rsyslog)

### Enable Syslog forwarding

1. Open the OpenVPN server configuration file (commonly found in `/etc/openvpn/server.conf`) using your preferred text editor.
    
    Add or modify the following lines:

    ```bash
    verb 3        # Adjust verbosity level if needed
    log-append /var/log/openvpn.log   # Specify the log file path
    log /dev/null  # Disable OpenVPN's built-in logging to file
    ```

    Here, `verb 3` sets the logging verbosity level, `log-append` specifies the log file path where OpenVPN logs will be written, and `log /dev/null` ensures that OpenVPN doesn't log to its internal log file.

2. Ensure that the syslog daemon (e.g., rsyslog or syslog-ng) is properly set up and configured on your system.

    These daemons are responsible for receiving and managing log messages from various services.

    OpenVPN will log its messages to the specified log file (`/var/log/openvpn.log` in the above example).

    Syslog will be responsible for picking up these messages and handling them according to its configuration.

3. Syslog Configuration

    Configure the syslog server to send the event to our log concentrator.

    If you are using rsyslog, you might need to create a specific configuration file for OpenVPN to tell the syslog daemon where to send the logs.
    
    Create a new file, for instance, `/etc/rsyslog.d/openvpn.conf`, and add the following line:
    
    ```bash
    :programname, isequal, "openvpn" @<ip of the log concentrator>
    
    ```

4. Restart Services

    Restart the OpenVPN service to apply the changes to the configuration file:
    
    ```bash
    sudo systemctl restart openvpn
    sudo systemctl restart rsyslog    # Use appropriate command for your syslog daemon
    ```

### Forward logs to Sekoia.io

Please consult the [Syslog Forwarding](../../../ingestion_methods/sekoiaio_forwarder/) documentation to forward these logs to Sekoia.io.

### Create the intake

Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `OpenVPN`.

{!_shared_content/operations_center/integrations/generated/e8ca856f-8a58-490b-bea4-247b12b3d74b_sample.md!}


{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_e8ca856f-8a58-490b-bea4-247b12b3d74b_do_not_edit_manually.md!}
{!_shared_content/operations_center/integrations/generated/e8ca856f-8a58-490b-bea4-247b12b3d74b.md!}

