# Prepare the load balancer

Users, API clients and log sources reach the platform through a load balancer. The load balancer forwards TCP connections to the Kubernetes nodes. Traefik, on every node, receives them.

## Rules

- The load balancer **MUST** work at the **TCP level (layer 4)**. It **MUST NOT** decrypt TLS: Traefik decrypts TLS with the platform certificate.
- The load balancer **MUST** forward these TCP ports to the Kubernetes nodes, on the same port numbers:

    | Port | Usage |
    | :---: | :--- |
    | 80 | HTTP, redirected to HTTPS |
    | 443 | Platform web interface, API, administrator portal, HTTPS log intake |
    | 10514 | Syslog over TLS log intake |
    | 11514 | RELP over TLS log intake |

- The load balancer **MUST NOT** send the PROXY protocol header.
- The load balancer **SHOULD** forward to the **3 manager nodes**. This is the validated setup. Traefik runs on every node, so worker nodes also work as backends.
- The load balancer **MAY** also forward TCP port **6443** (Kubernetes API) to the 3 manager nodes. This gives a highly available Kubernetes API.
- The DNS records of `global.host`, `global.delivery_host` and `global.alternative_hosts` **MUST** point to the IP address of the load balancer. See [DNS](./dns_time_certificates.md#dns).

### Impact on `config.yml`

| Your choice | `global.kube_manager_host` in `config.yml` |
| :--- | :--- |
| The load balancer forwards port 6443 | The DNS name (or IP address) of the load balancer, for example `kubernetes.<DOMAIN>`. |
| The load balancer does not forward port 6443 | The IP address of the first manager node, `<MANAGER_1_IP>`. This is the setup of the Sekoia lab. |

The SHC does not configure and does not test the load balancer. No other field of `config.yml` describes it.

## Install the load balancer

=== "nginx"

    **Validation status:** validated in the Sekoia lab (Debian 13, nginx from the Debian repository).

    The lab load balancer is a dedicated virtual machine. It forwards ports 80, 443, 10514, 11514 and 6443 to the 3 manager nodes.

    1. Install nginx and its TCP module:

        ```bash
        sudo apt-get update
        ```

        ```bash
        sudo apt-get install -y nginx libnginx-mod-stream
        ```

    2. Create the system user that runs nginx in this configuration:

        ```bash
        sudo useradd --system --shell /bin/false nginx
        ```

    3. Replace the main configuration file. The new file loads the TCP module and contains **no web site**: the default Debian web site would use port 80.

        ```bash
        sudo tee /etc/nginx/nginx.conf > /dev/null <<'EOF'
        load_module /usr/lib/nginx/modules/ngx_stream_module.so;

        user nginx;
        worker_processes auto;
        worker_rlimit_nofile 300000;
        error_log  /var/log/nginx/error.log  notice;
        pid        /var/run/nginx.pid;

        events {
            worker_connections 4096;
        }

        stream {
          log_format basic_stream '$remote_addr [$time_local] $protocol $status $bytes_sent $bytes_received $session_time "$upstream_addr" "$upstream_bytes_sent" "$upstream_bytes_received" "$upstream_connect_time"';

          include /etc/nginx/stream.d/*.conf;
        }
        EOF
        ```

    4. Create the directory of the forwarding rules:

        ```bash
        sudo mkdir -p /etc/nginx/stream.d
        ```

    5. Create the forwarding rules. Replace the three IP addresses with the IP addresses of your manager nodes. Remove the `6443` block if you do not forward the Kubernetes API.

        ```bash
        sudo tee /etc/nginx/stream.d/rproxy.conf > /dev/null <<'EOF'
        upstream backend_80 {
          server <MANAGER_1_IP>:80;
          server <MANAGER_2_IP>:80;
          server <MANAGER_3_IP>:80;
        }
        server {
          listen 80;
          proxy_pass backend_80;
          access_log /var/log/nginx/rproxy-80.log basic_stream;
        }

        upstream backend_443 {
          server <MANAGER_1_IP>:443;
          server <MANAGER_2_IP>:443;
          server <MANAGER_3_IP>:443;
        }
        server {
          listen 443;
          proxy_pass backend_443;
          access_log /var/log/nginx/rproxy-443.log basic_stream;
        }

        upstream backend_10514 {
          server <MANAGER_1_IP>:10514;
          server <MANAGER_2_IP>:10514;
          server <MANAGER_3_IP>:10514;
        }
        server {
          listen 10514;
          proxy_pass backend_10514;
          access_log /var/log/nginx/rproxy-10514.log basic_stream;
        }

        upstream backend_11514 {
          server <MANAGER_1_IP>:11514;
          server <MANAGER_2_IP>:11514;
          server <MANAGER_3_IP>:11514;
        }
        server {
          listen 11514;
          proxy_pass backend_11514;
          access_log /var/log/nginx/rproxy-11514.log basic_stream;
        }

        upstream backend_6443 {
          server <MANAGER_1_IP>:6443;
          server <MANAGER_2_IP>:6443;
          server <MANAGER_3_IP>:6443;
        }
        server {
          listen 6443;
          proxy_pass backend_6443;
          access_log /var/log/nginx/rproxy-6443.log basic_stream;
        }
        EOF
        ```

    6. Check the configuration:

        ```bash
        sudo nginx -t
        ```

        **Expected result:** `syntax is ok` and `test is successful`.

    7. Restart nginx and start it at every boot:

        ```bash
        sudo systemctl restart nginx
        ```

        ```bash
        sudo systemctl enable nginx
        ```

    8. Check that nginx listens on every port:

        ```bash
        sudo ss -tlnp | grep nginx
        ```

        **Expected result:** one line for each port: `80`, `443`, `10514`, `11514`, and `6443` if you kept it.

    !!! note "Before the installation"
        The backends answer only after the platform is installed. Until then, a connection to the load balancer is accepted and then closed: this is normal.

    !!! note "Health checks"
        This nginx configuration has no active health check. When a manager node is stopped, some connections fail before nginx stops using that node.

## Checklist

- [ ] The load balancer forwards TCP 80, 443, 10514 and 11514 to the nodes, without TLS decryption and without PROXY protocol.
- [ ] You chose the value of `global.kube_manager_host` (load balancer or first manager).
- [ ] `sudo ss -tlnp` on the load balancer shows every forwarded port.
