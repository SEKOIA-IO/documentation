# Syslog-ng

## Overview

Many technologies and agents allow the forwarding of their logs using the syslog protocol (RFC 5426).

We recommend you centralize them on a dedicated server: syslog-ng.

Before processing, you have to:

- Connect to [Sekoia.io SOC Platform with a Defend Plan](https://app.sekoia.io/intakes)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

## Syslog-ng installation prerequisites

The following prerequisites are needed in order to setup an efficient syslog-ng:

- Administrator privileges of the server: `root`
- Inbound traffic from the equipment to the syslog-ng must be open on `TCP 514` (or `UDP 514`)
- Outbound traffic from the syslog-ng to the Sekoia.io platform must be open on `TCP 10514` (IP for `intake.sekoia.io` is `213.32.5.228`)

## Syslog-ng installation procedure

After receiving the IDs to connect to the Linux server, the main activities are to be followed.

1. Connect to the syslog-ng node using SSH

2. Install the relevant packages using your package manager

    === "Debian, Ubuntu"

        ```bash
        sudo apt update
        sudo apt install -y syslog-ng syslog-ng-mod-tls openssl wget
        ```

    === "Fedora, Red Hat, CentOS (yum)"

        ```bash
        sudo yum update
        sudo yum install -y syslog-ng openssl wget
        ```

    === "Fedora, Red Hat, CentOS (dnf)"

        ```bash
        sudo dnf update
        sudo dnf install -y syslog-ng openssl wget
        ```

3. Add the Sekoia.io certification authority (CA) to the trusted store used by syslog-ng

    Certificates must be named by their hash values, which is done with the `openssl rehash` command.

    ```bash
    sudo mkdir -p /etc/syslog-ng/ca.d

    # Retrieve Certificate Authority (Let's Encrypt)
    sudo wget -O /etc/syslog-ng/ca.d/isrgrootx1.pem https://letsencrypt.org/certs/isrgrootx1.pem

    # Ask OpenSSL to create a hash for each PEM file
    sudo openssl rehash /etc/syslog-ng/ca.d
    ```

4. Modify the `/etc/syslog-ng/syslog-ng.conf` main configuration file

    This is an example of standard configuration file.
    In this file:

    * We allow syslog messages from `UDP 514` and `TCP 514` so that our syslog-ng acts as a concentrator
    * We define a destination `d_sekoia_io` that pushes events to Sekoia.io over TLS on `TCP 10514`
    * We include all `*.conf` files from `/etc/syslog-ng/conf.d/` to keep per-technology configuration in dedicated files

    !!!note
        It is recommended to keep distribution defaults for local logging rules in `/etc/syslog-ng/syslog-ng.conf`.
        Be sure a logrotate is applied to the files defined in the local logging rules!

    !!!note
        The `@version` directive must match the major version of syslog-ng installed on your server. Run `syslog-ng --version` to find it (for example `3.38` on Debian 12, `4.x` on Ubuntu 24.04). The example below uses `3.38`; replace it with your version if needed.

    ```
    @version: 3.38
    @include "scl.conf"

    options {
        chain_hostnames(off);
        use_dns(no);
        use_fqdn(no);
        keep_hostname(yes);
        owner("root");
        group("adm");
        perm(0640);
    };

    # Local sources
    source s_local {
        system();
        internal();
    };

    # Network sources (concentrator) — accept BSD (RFC3164) and RFC5424
    source s_network {
        network(
            transport("tcp")
            port(514)
        );
        network(
            transport("udp")
            port(514)
        );
    };

    # Sekoia.io destination over TLS
    destination d_sekoia_io {
        syslog("intake.sekoia.io"
            port(10514)
            transport("tls")
            frac_digits(6)
            ts_format(iso)
            tls(
                peer-verify(required-trusted)
                ca-dir("/etc/syslog-ng/ca.d")
            )
        );
    };

    # Local logging
    destination d_local {
        file("/var/log/syslog");
    };

    log {
        source(s_local);
        destination(d_local);
    };

    @include "/etc/syslog-ng/conf.d/*.conf"
    ```

5. Verify your configuration file is correct

    ```bash
    syslog-ng --syntax-only
    ```

    !!!note
        You may also use `syslog-ng -s` as a shorter equivalent.

6. Restart the syslog-ng service and check its status

    ```bash
    sudo systemctl restart syslog-ng
    sudo systemctl status syslog-ng
    ```

## Configure Syslog-ng server to receive and process logs

### Use case: process each incoming source on a specific port

In this use case, each source will send their events to a specific port to syslog-ng in order to identify the sources easily.
In this section, let's suppose that Windows event logs are sent to syslog-ng on port `TCP 20516`.

1. Modify the `/etc/syslog-ng/syslog-ng.conf` main configuration file

    Since Windows logs are sent to `TCP 20516`, logs should not be accepted on default port `514` in `TCP` or `UDP`.
    Comment the corresponding `network(...)` lines in the `source s_network { ... };` block.

2. Create a configuration file for each technology you want to forward to Sekoia.io

    Create a dedicated file in `/etc/syslog-ng/conf.d/` for each technology to be collected.

    In this example one file is created for Windows events.

    ```bash
    sudo touch /etc/syslog-ng/conf.d/15-windows.conf
    ```

3. Edit each configuration file as needed

    ```bash
    sudo vim /etc/syslog-ng/conf.d/15-windows.conf
    ```

    In this file, a source is specified for the port `20516` in `TCP`. A rewrite rule injects the **Intake key** into the structured-data section of the syslog message, and a `log` block ties the source to the Sekoia.io destination.

    Replace `YOUR_INTAKE_KEY` accordingly.

    ```
    source s_windows {
        network(
            transport("tcp")
            port(20516)
        );
    };

    rewrite r_windows {
        set("YOUR_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));
    };

    log {
        source(s_windows);
        rewrite(r_windows);
        destination(d_sekoia_io);
    };
    ```

4. Restart the syslog-ng service and make sure it is correctly set up

    ```bash
    sudo systemctl restart syslog-ng.service
    ```

### Use case: pattern matching for incoming Windows logs

#### Identify the pattern

To receive and process Windows logs, you have to follow these steps:

1. Verify that traffic is incoming from your log source

    ```bash
    sudo tcpdump -i <change_with_interface_name> -c10 -nn src <IP_OF_THE_SOURCE> -vv
    ```

    !!!tip
        Use `ip addr` command to find the relevant information to replace `<change_with_interface_name>`.

2. Ensure syslog events are correctly handled by the syslog-ng server

    For example, in Windows event logs, the field `hostname` is often used.

    ```bash
    sudo tail -f /var/log/syslog | grep -i "Hostname"
    ```

    !!!note
        Depending on the rules set in `/etc/syslog-ng/syslog-ng.conf`, adapt the path `/var/log/syslog` with the path where the syslog messages are stored - For instance `/var/log/messages`.

3. Identify syslog headers that will be used later

    **Method 1**: By watching messages in `/var/log/syslog`

    Messages in `/var/log/syslog` - or `/var/log/messages` depending on your `/etc/syslog-ng/syslog-ng.conf` configuration - contain information from the syslog header such as the `hostname` or the `program` (a.k.a. `app-name`) which can be used to identify your events.

    1. Search for Windows events in the file

        ```bash
        sudo tail -f /var/log/syslog | grep -i "Hostname"
        ```

    2. Identify the pattern. Similar log lines should be displayed within seconds:

        ```text
        Sep 16 12:39:18 windows-vm-0 Microsoft-Windows-Sysmon[3524] {"EventTime":"2022-09-16 12:39:18", [...] }
        ```

        In this example:

        * `windows-vm-0` corresponds to the `hostname` (`${HOST}` in syslog-ng)
        * `Microsoft-Windows-Sysmon` corresponds to the `program` (`${PROGRAM}` in syslog-ng)

        We can use this information to catch our events.

        !!!important
            If `Microsoft-Windows-Sysmon` is used, only Sysmon events will be caught. To get the other Windows event logs, only `Microsoft-Windows` should be used.

    **Method 2**: Create a configuration file to view raw syslog messages

    This method helps find key information located in the syslog headers to split technologies into separate pipelines and to forward them to the right Intakes on Sekoia.io.

    Log all the raw events received by the syslog-ng server to a **temporary file** named `00-testing.conf`.

    To identify syslog headers that will be used later, follow these steps:

    1. Create a dedicated configuration file

        ```bash
        sudo touch /etc/syslog-ng/conf.d/00-testing.conf
        ```

    2. Edit the configuration file

        ```bash
        sudo vim /etc/syslog-ng/conf.d/00-testing.conf
        ```

    3. Make sure the file contains the following information only:

        ```
        template t_sekoia_testing {
            template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] ${MSG}\n");
        };

        destination d_testing {
            file("/var/log/testing.log" template(t_sekoia_testing));
        };

        log {
            source(s_network);
            destination(d_testing);
        };
        ```

    4. Restart the syslog-ng service and verify its status

        ```bash
        sudo systemctl restart syslog-ng.service && sudo systemctl status syslog-ng.service
        ```

    5. Search for Windows events that now contain the syslog headers

        ```bash
        sudo tail -f /var/log/testing.log | grep -i "Hostname"
        ```

        Similar log lines should be displayed within seconds:

        ```text
        <14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"] {"EventTime":"2022-03-24 14:33:36","Hostname":"DESKTOP-XXXXXXX","Keywords":-922337203685XXXXXXX,"EventType":"INFO","SeverityValue":2,"Severity":"INFO","EventID":3,"SourceName":"Microsoft-Windows-Sysmon" [...]}
        ```

        In this example, the syslog header is:
        ```text
        <14>1 2022-03-24T14:33:36.738171+01:00 DESKTOP-XXXXXXX Microsoft-Windows-Sysmon 5504 LOG [SEKOIA@53288 intake_key="DO_NOT_CHANGE"]
        ```

        It corresponds to what was requested in the template `t_sekoia_testing`:
        ```text
        <${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"]
        ```

        !!!note
            More information about syslog-ng macros can be found in the [syslog-ng macros reference](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.38/administration-guide/macros).

    6. Find unique information to isolate this particular technology

        In this example, `DESKTOP-XXXXXXX` or `Microsoft-Windows` information is precious.

        The `${HOST}`, `${PROGRAM}` or `${MSGHDR}` macros in the syslog headers are often used to determine which intake the log should be forwarded to.

        Comparison done in `filter` blocks usually relies on `match()` (regex), `program()`, `host()` or `message()`. These match the corresponding macro values in the syslog header. Indeed, depending on your network, the `${HOST}` can be an FQDN, an IP address (with or without NAT) or the real hostname of the source machine.

    7. Comment the lines of the file `/etc/syslog-ng/conf.d/00-testing.conf`

        ```
        # template t_sekoia_testing {
        #     template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] ${MSG}\n");
        # };
        # destination d_testing { file("/var/log/testing.log" template(t_sekoia_testing)); };
        # log { source(s_network); destination(d_testing); };
        ```

    8. Restart the syslog-ng service and check its status

        ```bash
        sudo systemctl restart syslog-ng.service && sudo systemctl status syslog-ng.service
        ```

    9. Remove the `/var/log/testing.log` file

        ```bash
        sudo rm /var/log/testing.log
        ```

#### Forward logs to Sekoia.io

1. Create configuration files for each technology you want to forward to Sekoia.io

    Create a dedicated file in `/etc/syslog-ng/conf.d/` for each technology to be collected.

    Example for the Windows log collection:

    ```bash
    sudo touch /etc/syslog-ng/conf.d/15-windows.conf
    ```

2. Edit each configuration file as needed

    ```bash
    sudo vim /etc/syslog-ng/conf.d/15-windows.conf
    ```

    The **Intake key** is needed in this step. Ensure to replace `YOUR_INTAKE_KEY` by your Windows Intake Key.

    You should also adapt the filter name `f_windows` and its match pattern with appropriate content as explained in the previous section.

    Following the same example for Windows log collection:

    ```
    # Filter Windows events using the program (app-name) field
    filter f_windows {
        match("Microsoft-Windows" value("PROGRAM"));
    };

    # Inject the Intake key into the structured-data section of the syslog message
    rewrite r_windows {
        set("YOUR_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));
    };

    # Pipe matching events from the network source to the Sekoia.io destination
    log {
        source(s_network);
        filter(f_windows);
        rewrite(r_windows);
        destination(d_sekoia_io);
    };
    ```

3. Restart the syslog-ng service and make sure it is correctly set up

    ```bash
    sudo systemctl restart syslog-ng.service
    ```

## See your events on Sekoia.io XDR

Once you're done with all the actions above, you should see your events displayed in real-time on Sekoia.io.

To verify that everything works well, connect to [Sekoia.io Events' page](https://app.sekoia.io/operations/events) and wait for events to come.

If you would like to filter on specific intakes:

- Go to [Sekoia.io Intakes page](https://app.sekoia.io/operations/intakes)
- Copy your Intake Key. In this example, it can be: `88EYbSaG55YbVaTne8Gu93wKQbLE4axZ`
- Come back to [Sekoia.io Events' page](https://app.sekoia.io/operations/events)
- Query the following in the search bar: `sekoiaio.intake.key:"88EYbSaG55YbVaTne8Gu93wKQbLE4axZ"` and press `Enter`

## How to forward logs reliably using disk-buffer

Syslog-ng can be configured to push logs reliably by combining a TLS transport with the `disk-buffer()` option. When this is enabled, syslog-ng persists messages on disk if the connection to Sekoia.io is interrupted, and replays them once the connection is restored. With `reliable(yes)`, every message is written to disk before being sent — guaranteeing no loss even after a crash.

Before processing, you have to:

- Connect to [Sekoia.io SOC Platform with a Defend Plan](https://app.sekoia.io/intakes)
- Add an Intake to the relevant Entity
- Keep trace of the automatically generated Intake key

Follow these steps to forward logs reliably to Sekoia.io:

1. Make sure the disk-buffer directory exists and is writable by syslog-ng

    ```bash
    sudo mkdir -p /var/lib/syslog-ng
    sudo chown root:root /var/lib/syslog-ng
    sudo chmod 0700 /var/lib/syslog-ng
    ```

2. Update the Sekoia.io destination in `/etc/syslog-ng/syslog-ng.conf` to enable `disk-buffer()`:

    ```
    destination d_sekoia_io {
        syslog("intake.sekoia.io"
            port(10514)
            transport("tls")
            frac_digits(6)
            ts_format(iso)
            tls(
                peer-verify(required-trusted)
                ca-dir("/etc/syslog-ng/ca.d")
            )
            disk-buffer(
                mem-buf-size(10000)            # in-memory queue size (number of messages)
                disk-buf-size(2000000000)      # max disk buffer size in bytes (2 GB)
                reliable(yes)                  # write every message to disk before sending
                dir("/var/lib/syslog-ng")      # where the buffer is persisted
            )
        );
    };
    ```

3. Restart syslog-ng to apply the new configuration

    ```bash
    sudo systemctl restart syslog-ng.service
    ```

!!!note
    With `reliable(yes)`, throughput is lower than with `reliable(no)` because every message hits the disk before being acknowledged. If your throughput requirements are very high and a small amount of in-memory loss is acceptable on a hard crash, set `reliable(no)`.

## syslog-ng and Red Hat Enterprise Linux

If you can't see your events on Sekoia.io, you might encounter an issue with your syslog-ng and its capability dropping feature. This problem was faced by some of our customers with Red Hat Enterprise Linux for example.

As explained in syslog-ng's article "[Working around Linux capabilities problems for syslog-ng](https://www.syslog-ng.com/community/b/blog/posts/working-around-linux-capabilities-problems-for-syslog-ng)", you can execute the following commands to solve this issue:

```
# cat >> /etc/sysconfig/syslog-ng << EOF
SYSLOGNG_OPTS="--caps cap_sys_admin,cap_chown,cap_dac_override,cap_net_bind_service,cap_fowner=eip"
EOF
# systemctl restart syslog-ng
```

## How to Debug syslog-ng?

To check if syslog-ng is forwarding events to Sekoia.io, you can start it with the `-d` (to enable debug mode) and `-e` (to ensure that all logs are displayed to the standard output) flags:

```
/usr/sbin/syslog-ng -F --no-caps -d -e
```

The following output should be displayed:

```
[2022-03-31T11:46:55.939706] Syslog connection established; fd='12', server='AF_INET(51.159.9.95:10514)', local='AF_INET(0.0.0.0:0)'
…
[2022-03-31T11:46:59.319748] Certificate validation progress; subject='CN=ISRG Root X1, O=Internet Security Research Group, C=US', issuer='CN=ISRG Root X1, O=Internet Security Research Group, C=US'
[2022-03-31T11:46:59.319967] Certificate validation progress; subject='CN=R3, O=Let\'s Encrypt, C=US', issuer='CN=ISRG Root X1, O=Internet Security Research Group, C=US'
[2022-03-31T11:46:59.320050] Certificate validation progress; subject='CN=intake.sekoia.io', issuer='CN=R3, O=Let\'s Encrypt, C=US'
[2022-03-31T11:46:59.341597] Outgoing message; message='<13>1 2022-03-31T11:46:55.924744+00:00 942b0f2f58fb - 1049 - [SEKOIA@53288 intake_key="XXXX"][meta sequenceId="1"] XXXXX'
```

## Troubleshooting

After setting up your syslog-ng, you may encounter errors due to the contextual environment or omissions while copying and pasting information.

Useful troubleshooting resources are:

- The [syslog-ng documentation](https://www.syslog-ng.com/technical-documents/list/syslog-ng-open-source-edition)
- The syslog-ng [GitHub issue tracker](https://github.com/syslog-ng/syslog-ng/issues)

Here's a non-exhaustive list of known errors:

### 1- syslog-ng daemon error

Ensure the syslog-ng service is currently running on the server.

```bash
sudo systemctl status syslog-ng.service
```

If the service is down, try to restart syslog-ng:

```bash
sudo systemctl restart syslog-ng.service
```

### 2- Checking logs sent to syslog-ng

In your configuration files, there will be a section that looks like the following example:

```
template t_sekoia_unbound {
    template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} LOG [SEKOIA@53288 intake_key=\"<intake_key>\"] ${MSG}\n");
};

filter f_unbound { program("unbound"); };

log {
    source(s_network);
    filter(f_unbound);
    destination(d_sekoia_io);
};
```

If you want to retrieve the raw data that is forwarded to Sekoia.io, you can add an extra `log` block to dump matching events to a local file:

```
destination d_unbound_local {
    file("/tmp/unbound-output.log" template(t_sekoia_unbound));
};

log {
    source(s_network);
    filter(f_unbound);
    destination(d_unbound_local);
};
```

This way, you will be able to identify exactly what data is sent to Sekoia.io and to fix it if needed.

```
# tail -n 1 /tmp/unbound-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="<intake_key>"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```

### 3- Local messages not seen on the syslog-ng server

If you can't see local messages on the syslog-ng server, you have to make sure the logs are received on the syslog-ng server. This means that:

- Configurations are correctly undertaken on the remote equipment
- Internal network flows are open on `TCP or UDP 514`

To fix this:

1. Run the following command:

    ```bash
    tail -n 15 /var/log/syslog
    ```

2. Make sure a network source is defined - and not commented - in the main configuration file `/etc/syslog-ng/syslog-ng.conf` or in specific files in `/etc/syslog-ng/conf.d`. For instance:

    ```
    source s_network {
        network(transport("tcp") port(514));
        network(transport("udp") port(514));
    };
    ```

3. Verify that traffic is incoming from your log source

    ```bash
    sudo tcpdump -i <change_with_interface_name> -c10 -nn src 1.1.1.1 -vv
    ```

### 4- A `/etc/syslog-ng/conf.d/xx-<technology>.conf` file is misconfigured

If the syslog-ng service is failing to start, a typo may have been introduced in one of the `/etc/syslog-ng/conf.d/xx-<technology>.conf` files.

Run the following command to confirm it and get information about the error:

```bash
syslog-ng --syntax-only
```

If the syslog-ng service starts, the logs are correctly received and the `/etc/syslog-ng/syslog-ng.conf` file is correctly configured, but **no logs are received** on Sekoia.io, then it is highly possible that the `filter` is **not correct**.

In this case:

1. Ensure the relevant `Intake Key` is provided in the rewrite rule: `set("YOUR_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));`
2. Uncomment the lines in `/etc/syslog-ng/conf.d/00-testing.conf`
3. Restart the syslog-ng service
4. Use the `grep` function to filter on the relevant data from `/var/log/testing.log` file
5. Identify the right information on the syslog header and adapt the `filter` accordingly

It is possible to test your specific filter. To do so:

1. Add the following lines in the `/etc/syslog-ng/conf.d/00-testing.conf` and use your filter instead of `TO_BE_ADAPTED`.

    ```
    template t_sekoia_troubleshoot {
        template("<${PRI}>1 ${ISODATE} ${HOST} ${PROGRAM} ${PID} LOG [SEKOIA@53288 intake_key=\"DO_NOT_CHANGE\"] ${MSG}\n");
    };

    filter f_troubleshoot { TO_BE_ADAPTED; };

    destination d_troubleshoot {
        file("/var/log/troubleshoot.log" template(t_sekoia_troubleshoot));
    };

    log {
        source(s_network);
        filter(f_troubleshoot);
        destination(d_troubleshoot);
    };
    ```

2. Restart the syslog-ng service and check whether the new file `/var/log/troubleshoot.log` is created and populated with logs using `grep` command.
3. Comment the lines in the `/etc/syslog-ng/conf.d/00-testing.conf`
4. Restart the syslog-ng service
5. Remove the `/var/log/testing.log` file and `/var/log/troubleshoot.log` file if necessary

### 5- TLS error: syslog-ng cannot authenticate the Sekoia.io syslog endpoint

The Sekoia.io syslog endpoint is secured with a [Let's Encrypt](https://letsencrypt.org) certificate.

According to your installation, it may be necessary to install the `ISRG ROOT X1` certificate in the syslog-ng CA directory:

1. Download the `ISRG ROOT X1` certificate: <https://letsencrypt.org/certs/isrgrootx1.pem>

    ```bash
    sudo wget -O /etc/syslog-ng/ca.d/isrgrootx1.pem https://letsencrypt.org/certs/isrgrootx1.pem
    ```

2. Re-hash the CA directory so syslog-ng can find the certificate

    ```bash
    sudo openssl rehash /etc/syslog-ng/ca.d
    ```

3. Restart syslog-ng

    ```bash
    sudo systemctl restart syslog-ng.service
    ```

## Example of auto-setup configuration

In order to help users setting up this concentrator, the following bash script working for Ubuntu or Debian server is recommended.

It will automatically configure your syslog-ng server to collect and forward Windows Event logs.

!!!note
    `sudo` must be installed and set up for the current user.

1. From the Sekoia.io SOC Platform with a Defend Plan, add a Windows Intake to the relevant Entity and copy the `Intake Key`.
    It is possible to copy and paste this configuration locally then upload it with SCP command, or simply copy and paste it from the web to your remote server.

    ```bash
    #!/bin/bash
    ##### This file is used to automate the syslog-ng setup

    # Install service and dependencies
    sudo apt update
    sudo apt install -y syslog-ng syslog-ng-mod-tls openssl wget

    # Create the CA directory and install the Let's Encrypt root certificate
    sudo mkdir -p /etc/syslog-ng/ca.d
    sudo wget -O /etc/syslog-ng/ca.d/isrgrootx1.pem https://letsencrypt.org/certs/isrgrootx1.pem
    sudo openssl rehash /etc/syslog-ng/ca.d

    # Create the disk-buffer directory
    sudo mkdir -p /var/lib/syslog-ng
    sudo chown root:root /var/lib/syslog-ng
    sudo chmod 0700 /var/lib/syslog-ng

    ### Create a dedicated syslog-ng configuration file
    SyslogNgConfFile="/etc/syslog-ng/syslog-ng.conf"

    # Detect installed syslog-ng version to write a matching @version directive
    SYSLOGNG_VERSION=$(syslog-ng --version | awk '/Config version/{print $NF; exit}')

    sudo /bin/cat <<EOM >$SyslogNgConfFile
    @version: ${SYSLOGNG_VERSION}
    @include "scl.conf"

    options {
        chain_hostnames(off);
        use_dns(no);
        use_fqdn(no);
        keep_hostname(yes);
        owner("root");
        group("adm");
        perm(0640);
    };

    source s_local {
        system();
        internal();
    };

    source s_network {
        network(transport("tcp") port(514));
        network(transport("udp") port(514));
    };

    destination d_local {
        file("/var/log/syslog");
    };

    destination d_sekoia_io {
        syslog("intake.sekoia.io"
            port(10514)
            transport("tls")
            frac_digits(6)
            ts_format(iso)
            tls(
                peer-verify(required-trusted)
                ca-dir("/etc/syslog-ng/ca.d")
            )
            disk-buffer(
                mem-buf-size(10000)
                disk-buf-size(2000000000)
                reliable(yes)
                dir("/var/lib/syslog-ng")
            )
        );
    };

    log {
        source(s_local);
        destination(d_local);
    };

    @include "/etc/syslog-ng/conf.d/*.conf"
    EOM

    ### Create a dedicated Windows configuration file
    WindowsFile="/etc/syslog-ng/conf.d/15-windows.conf"

    sudo /bin/cat <<\EOM >$WindowsFile
    filter f_windows {
        match("Microsoft-Windows" value("PROGRAM"));
    };

    rewrite r_windows {
        set("YOUR_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));
    };

    log {
        source(s_network);
        filter(f_windows);
        rewrite(r_windows);
        destination(d_sekoia_io);
    };
    EOM
    ```

2. Once the file is created on the syslog-ng server, make it executable with the command `chmod +x <filename.sh>`.

3. Run it using this command:

    ```bash
    ./<filename.sh>
    ```

4. Change the intake key value in the `/etc/syslog-ng/conf.d/15-windows.conf` file
5. Restart the syslog-ng service:

    ```bash
    sudo systemctl restart syslog-ng.service
    ```
