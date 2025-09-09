# Syslog-ng

If you are using syslog-ng as a log collector, you can configure it to push your logs to Sekoia.io. This operation is done by using Syslog protocol.

To push logs, you have to configure some filters and rewrite rules in syslog-ng that will add the proper “intake key” considering your logs.

## Destination Configuration

The first thing to do is to add the Sekoia.io certification authority (CA) file in the `/etc/syslog-ng/ca.d` directory. Certificates should be in names by their hash values (that can be done via the `openssl rehash` command).

To proceed, you can execute the following commands in your favorite shell:

```
sudo mkdir -p /etc/syslog-ng/ca.d

# Retrieve Certificate Authority (Let’s Encrypt)
sudo wget -O /etc/syslog-ng/ca.d/isrgrootx1.pem https://letsencrypt.org/certs/isrgrootx1.pem

# Ask OpenSSL to create a hash for each PEM file.
sudo openssl rehash /etc/syslog-ng/ca.d
```

Then, you have to define syslog-ng’s destination module to push Syslog events to Sekoia.io in `/etc/syslog-ng/syslog-ng.conf`:

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

In the following example, we are pushing Apache HTTP Server and NGINX logs to Sekoia.io. To filter in events, we are relying on process names. Make sure you update your intake key value by changing `CHANGE_ME_INTAKE_KEY` below.

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

## syslog-ng and Red Hat Enterprise Linux

If you can’t see your events on Sekoia.io, you might encounter an issue with your syslog-ng and its capability dropping feature. This problem was faced by some of our customers with Red Hat Enterprise Linux for example.

As explained in syslog-ng’s article “[Working around Linux capabilities problems for syslog-ng](https://www.syslog-ng.com/community/b/blog/posts/working-around-linux-capabilities-problems-for-syslog-ng)”, you can execute the following commands to solve this issue:

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
