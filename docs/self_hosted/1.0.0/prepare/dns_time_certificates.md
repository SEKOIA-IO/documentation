# Prepare DNS, time, email and certificates

## DNS

The platform answers on three names. You choose them, and you write them in `config.yml`:

| Field of `config.yml` | Role | Example |
| :--- | :--- | :--- |
| `global.host` | Main address: web interface, API, log intake. | `app.<DOMAIN>` |
| `global.alternative_hosts` | A second address of the platform. | `api.<DOMAIN>` |
| `global.delivery_host` | Administrator portal and Grafana. | `admin.<DOMAIN>` |

### Rules

- `global.host`, `global.alternative_hosts` and `global.delivery_host` **MUST** resolve to the IP address of the [load balancer](./load_balancer.md), for users, API clients and log sources.
- If `global.kube_manager_host` is a name (not an IP address), this name **MUST** resolve before the installation.
- `global.forward_dns` **MUST** be the IP address of a DNS server that the Kubernetes nodes reach on port 53. The platform services use this server for every name outside the cluster.
- Every name that the platform uses (Git server, OCI registry, S3 storage, SMTP server) **MUST** resolve with the `global.forward_dns` server, **or** be written as an IP address in the configuration. The platform services do not read the `/etc/hosts` file of the nodes.
- `global.alternative_hosts` **SHOULD** be set to a name of your domain. Its default value, `api.sekoia.local`, is an example.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What happens |
| :--- | :--- |
| `global.alternative_hosts` not set | The platform also answers on `api.sekoia.local`. Nothing breaks, but your certificate must then also cover `api.sekoia.local`, or users see a certificate warning on this name. |

=== "DNS server"

    **Validation status:** reference procedure.

    Ask your DNS administrator to create these records **before** the installation:

    | Name | Type | Value |
    | :--- | :---: | :--- |
    | `app.<DOMAIN>` (`global.host`) | A | `<LB_IP>` |
    | `api.<DOMAIN>` (`global.alternative_hosts`) | A | `<LB_IP>` |
    | `admin.<DOMAIN>` (`global.delivery_host`) | A | `<LB_IP>` |
    | `kubernetes.<DOMAIN>` (only if `global.kube_manager_host` is this name) | A | `<LB_IP>` |

    Check from the orchestration node and from one Kubernetes node:

    ```bash
    getent hosts app.<DOMAIN> api.<DOMAIN> admin.<DOMAIN>
    ```

    **Expected result:** three lines, each with `<LB_IP>`.

=== "/etc/hosts (no DNS server)"

    **Validation status:** validated in the Sekoia lab.

    The lab has no DNS server for the platform names. Every server of the lab (orchestration node, load balancer, Kubernetes nodes) has these lines in `/etc/hosts`. The Git server, the registry and the storage are written as IP addresses in `config.yml`.

    1. On **each server**, add the lines. Replace `<LB_IP>` and the names:

        ```bash
        printf '<LB_IP> app.<DOMAIN>\n<LB_IP> api.<DOMAIN>\n<LB_IP> admin.<DOMAIN>\n<LB_IP> kubernetes.<DOMAIN>\n' | sudo tee -a /etc/hosts
        ```

    2. On each computer that opens the web interface, add the same lines to its `hosts` file (on Windows: `C:\Windows\System32\drivers\etc\hosts`, edited as administrator).

    3. Set `global.forward_dns` to a DNS server that the nodes reach, for example the DNS server of your network.

## Time (NTP)

### Rules

- Every server (Kubernetes nodes and orchestration node) **MUST** synchronize its clock with NTP.
- The clocks of the Kubernetes nodes **MUST** differ by less than 1 second.
- The nodes **SHOULD** use your company NTP servers. The default Debian configuration uses public NTP servers on the internet: on a site without internet access, the clock is never synchronized and `CheckServerSpec` fails.

=== "chrony"

    **Validation status:** validated in the Sekoia lab (the lab uses public NTP servers).

    Run these commands on each server.

    1. Install chrony:

        ```bash
        sudo apt-get install -y chrony
        ```

    2. Declare your NTP server. Replace `<NTP_SERVER>` with its name or IP address. Run the command once for each NTP server, with a different file name:

        ```bash
        echo "server <NTP_SERVER> iburst" | sudo tee /etc/chrony/sources.d/company-ntp-1.sources
        ```

    3. Restart chrony:

        ```bash
        sudo systemctl restart chrony
        ```

    4. Enable NTP synchronization:

        ```bash
        sudo timedatectl set-ntp true
        ```

    5. Wait one minute, then check:

        ```bash
        timedatectl show -p NTP -p NTPSynchronized
        ```

        **Expected result:** `NTP=yes` and `NTPSynchronized=yes`. If you see `NTPSynchronized=no`, run `chronyc sources`: the line of your server must start with `^*`.

=== "systemd-timesyncd"

    **Validation status:** reference procedure. `systemd-timesyncd` is the default time service of Debian when chrony is not installed.

    Run these commands on each server.

    1. Open the configuration file:

        ```bash
        sudo nano /etc/systemd/timesyncd.conf
        ```

    2. In the `[Time]` section, write this line (remove the `#` at the start if it is there). Replace the names with your NTP servers, separated by a space:

        ```ini
        NTP=<NTP_SERVER_1> <NTP_SERVER_2>
        ```

    3. Restart the service and enable NTP:

        ```bash
        sudo systemctl restart systemd-timesyncd
        ```

        ```bash
        sudo timedatectl set-ntp true
        ```

    4. Wait one minute, then check:

        ```bash
        timedatectl show -p NTP -p NTPSynchronized
        ```

        **Expected result:** `NTP=yes` and `NTPSynchronized=yes`.

## Email (SMTP)

### Rules

- The platform **SHOULD** send email through your SMTP server. It sends user invitations and notifications.
- The Kubernetes nodes **MUST** reach the SMTP server on its port, **without a proxy**: email does not use the platform proxy.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What happens |
| :--- | :--- |
| No SMTP server configured | The installation works, but the platform sends no email: no invitation, no notification. You can configure SMTP later and run `exec PlatformInstallation` again. |

### Configuration

Write these fields in `config.yml`. The full reference is in [Email notifications](../deployment/deployment_configuration.md#email-notifications).

```yaml
modules:
  platform_configuration:
    config:
      email:
        email_sender: "noreply@<DOMAIN>"
        smtp:
          host: "<SMTP_SERVER>"
          port: "587"
          user: "<SMTP_USER>"
          password: "${env.SMTP_PASSWORD}"
          tls: "False"
          starttls: "True"
```

Because the password is an environment variable:

1. In `env.rc`, add `export SMTP_PASSWORD='<SMTP_PASSWORD>'`.
2. In `run-shc.sh`, add the line `-e SMTP_PASSWORD="$SMTP_PASSWORD" \` after the other `-e` lines.

| Your SMTP server | `port` | `tls` | `starttls` |
| :--- | :---: | :---: | :---: |
| STARTTLS (most common) | `"587"` | `"False"` | `"True"` |
| Implicit TLS | `"465"` | `"True"` | `"False"` |
| No encryption (internal relay) | `"25"` | `"False"` | `"False"` |

Write `"True"` and `"False"` with an uppercase first letter, between quotes.

## Platform certificate

Traefik serves the platform over HTTPS (port 443) and receives the logs over TLS (ports 10514 and 11514). It uses one certificate for all of them.

### Rules

- The platform **SHOULD** use a certificate issued by your certificate authority.
- The certificate **MUST** be valid for `global.host`, `global.alternative_hosts` and `global.delivery_host`: these three names **MUST** be in the *Subject Alternative Name* of the certificate. A wildcard certificate (`*.<DOMAIN>`) covers them if they are all in `<DOMAIN>`.
- The certificate and its key **MUST** be in PEM format (text that starts with `-----BEGIN`). The key **MUST NOT** have a password.
- The certificate file **SHOULD** contain the full chain: the certificate first, then the intermediate certificates, then the root certificate.

### If you do not follow a SHOULD rule

| SHOULD rule not followed | What happens and what you must change |
| :--- | :--- |
| No certificate | Do not set `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY`. Traefik then uses a self-signed certificate: browsers show a warning, and API clients and log forwarders must accept an untrusted certificate. |
| Self-signed certificate (lab) | Users, API clients and log forwarders must accept or trust this certificate. Use the tab "Self-signed certificate". |
| Chain incomplete | Some clients reject the certificate. Add the intermediate certificates to `tls.crt`. |

### Install the certificate

=== "Certificate from your authority"

    **Validation status:** reference procedure.

    1. Copy the certificate (full chain) to `~/shc/tls.crt` and the private key to `~/shc/tls.key` on the orchestration node.

    2. Protect the key:

        ```bash
        chmod 600 ~/shc/tls.key
        ```

    3. Check the names in the certificate:

        ```bash
        openssl x509 -in ~/shc/tls.crt -noout -ext subjectAltName
        ```

        **Expected result:** the three names of the platform, or a wildcard that covers them.

    4. Check that the key matches the certificate. The two commands must print the same value:

        ```bash
        openssl x509 -in ~/shc/tls.crt -noout -pubkey | sha256sum
        ```

        ```bash
        openssl pkey -in ~/shc/tls.key -pubout | sha256sum
        ```

    5. Load the environment file again. `env.rc` reads the two files into `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY`:

        ```bash
        source ~/env.rc
        ```

=== "Self-signed certificate"

    **Validation status:** validated in the Sekoia lab.

    1. Create the certificate and its key on the orchestration node. Replace the three names with the values of `global.host`, `global.alternative_hosts` and `global.delivery_host`:

        ```bash
        mkdir -p ~/shc && chmod 777 ~/shc
        ```

        ```bash
        openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 365 -keyout ~/shc/tls.key -out ~/shc/tls.crt -subj "/CN=app.<DOMAIN>" -addext "subjectAltName=DNS:app.<DOMAIN>,DNS:api.<DOMAIN>,DNS:admin.<DOMAIN>"
        ```

    2. Protect the key:

        ```bash
        chmod 600 ~/shc/tls.key
        ```

    3. Load the environment file again. `env.rc` reads the two files into `TRAEFIK_PUBKEY` and `TRAEFIK_PRIVKEY`:

        ```bash
        source ~/env.rc
        ```

    This certificate is valid for 365 days.

## Checklist

- [ ] `getent hosts` resolves the three platform names to the load balancer, on the orchestration node and on the Kubernetes nodes.
- [ ] `global.forward_dns` is a DNS server that the nodes reach.
- [ ] `timedatectl show -p NTPSynchronized` prints `NTPSynchronized=yes` on every server.
- [ ] The SMTP fields are in `config.yml` (or you accept that the platform sends no email).
- [ ] `~/shc/tls.crt` and `~/shc/tls.key` exist (or you accept the default self-signed certificate), and `env.rc` is loaded again.
