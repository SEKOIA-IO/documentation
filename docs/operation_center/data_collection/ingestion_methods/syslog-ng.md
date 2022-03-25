# Forward Logs to SEKOIA.IO From syslog-ng

If you are using syslog-ng as a log collector, you can configure it to push your logs to SEKOIA.IO. This operation is done by using Syslog protocol.

To push logs, you have to configure some filters and rewrite rules in syslog-ng that will add the proper “intake key” considering your logs.

## Destination Configuration

The first thing to do is to add the SEKOIA.IO certification authority (CA) file in the `/etc/syslog-ng/ca.d` directory. To proceed, you can execute the following commands in your favorite shell:
```
sudo mkdir -p /etc/syslog-ng/ca.d && sudo wget -O /etc/syslog-ng/ca.d/SEKOIA-IO-intake.pem https://app.sekoia.io/assets/files/SEKOIA-IO-intake.pem
```

Then, you have to define syslog-ng’s destination module to push Syslog events to SEKOIA.IO in `/etc/syslog-ng/syslog-ng.conf`:

```
destination d_sekoia_io {
    syslog("intake.sekoia.io"
            port(10514)
            transport("tls")
            frac_digits(6)
            ts_format(iso)
            tls(peer-verify(required-trusted) ca-dir("/etc/syslog-ng/ca.d"))
    );
};
```

## Dispatching Events

In the following example, we are pushing Apache HTTP Server and NGINX logs to SEKOIA.IO. To filter in events, we are relying on process names. Make sure you update your intake key value by changing `CHANGE_ME_INTAKE_KEY` below.

You have to add the following configuration snippet in your main syslog-ng configuration file, `/etc/syslog-ng/syslog-ng.conf`:

```
filter f_apache2 {
    program(apache2);
};

rewrite r_apache2 {
    set("CHANGE_ME_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));
};

log {
    source(s_network);
    filter(f_apache2);
    rewrite(r_apache2);
    destination(d_sekoia_io);
};

filter f_nginx {
    program(nginx);
};

rewrite r_nginx {
    set("CHANGE_ME_INTAKE_KEY" value(".SDATA.SEKOIA@53288.intake_key"));
};

log {
    source(s_network);
    filter(f_nginx);
    rewrite(r_nginx);
    destination(d_sekoia_io);
};
```
