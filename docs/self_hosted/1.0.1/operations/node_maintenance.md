# Patch and restart the nodes

Node maintenance restarts the cluster nodes to apply OS patches, kernel updates, or to recover the whole cluster after a crash. To keep the platform running, restart the nodes one at a time. Keep the self-hosted-controller (SHC) commands `RebootNodes` and `KubeCrashRecovery` for a planned cold restart during a maintenance window.

## Prerequisites

- You run the commands from the orchestration node, with `kubectl` access to the cluster.
- The platform is healthy before you start: every node is `Ready` and the Ceph cluster reports all placement groups `active+clean`.
- You can open an SSH session with `sudo` rights on every node.

## Patch the nodes one at a time

The Ceph storage keeps two copies of the data on two different nodes. While one node is down, the data stays available from the other copy. The three manager nodes hold the Kubernetes database (etcd), which stays available as long as two managers are running.

!!! warning "Restart one node at a time"
    If two nodes holding the same data are down at the same time, the platform can no longer read or write that data. Never restart a node before the previous one is back and the storage has recovered.

1. To prevent Ceph from moving data while a node is down, set the `noout` flag:

    ```bash
    kubectl exec -n rook-ceph deploy/rook-ceph-tools -- ceph osd set noout
    ```

2. Repeat the following steps for each node, one node at a time:

    1. Find the node name in the output of `kubectl get nodes`.
    2. Move the pods of the node to the other nodes:

        !!! warning "Do not force the eviction"
            If the command stops on a pod disruption budget, do not force the eviction.

        ```bash
        kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data --timeout=10m
        ```

    3. Apply your patches on the node.
    4. Restart the node, for example with `sudo systemctl reboot`.
    5. Wait until `kubectl get nodes` lists the node as `Ready` again.
    6. Allow pods to run on the node again:

        ```bash
        kubectl uncordon <node-name>
        ```

    7. Wait until the Ceph cluster reports every placement group `active+clean` before you move to the next node:

        !!! note "Expected Ceph warnings"
            While `noout` is set, the health status stays at `HEALTH_WARN` with the message `noout flag(s) set`. While the node is down and until the storage has recovered, placement groups also report `undersized` or `degraded`. Both states are expected and clear on their own.

        ```bash
        kubectl exec -n rook-ceph deploy/rook-ceph-tools -- ceph status
        ```

3. Once every node is patched, remove the `noout` flag:

    ```bash
    kubectl exec -n rook-ceph deploy/rook-ceph-tools -- ceph osd unset noout
    ```

4. To check the platform health, run `exec Diagnostic`. See [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

### Result

Every node runs the patched OS, the Ceph cluster reports `HEALTH_OK`, and the platform stayed available during the whole procedure.

## Run a cold restart of the whole cluster

A cold restart reboots every node, then restarts every pod in dependency order. Use it when the whole cluster must be restarted or after an unexpected crash of several nodes that left pods stuck in a failed state.

!!! warning "Full platform outage"
    `RebootNodes` and `KubeCrashRecovery` make the whole platform unavailable: ingestion, detection, and the web interface stop until every pod is running again. Run them only during a maintenance window. To patch the nodes without an outage, use the [rolling procedure](#patch-the-nodes-one-at-a-time) instead.

1. To reboot the nodes, run:

    ```bash
    exec RebootNodes
    ```

    The command reboots every node of `utils.ansible.inventory` in parallel, up to five nodes at a time, without draining them. It waits up to five minutes for each node to accept SSH connections again.

2. Wait until `kubectl get nodes` lists every node as `Ready`.

    !!! note "Kubernetes API required"
        `KubeCrashRecovery` stops immediately if it cannot reach the Kubernetes API. Do not run it while `kubectl get nodes` fails or a node is `NotReady`.

3. To restart the pods in dependency order, run:

    ```bash
    exec KubeCrashRecovery
    ```

    The command deletes every pod of the cluster, namespace group by namespace group, and waits for each group to be ready before it moves to the next. See [KubeCrashRecovery](/self_hosted/1.0.1/troubleshooting/debug_tool.md#kubecrashrecovery).

4. Check that Vault is unsealed. Vault unseals itself when its pod starts, so the output must show `Sealed false`:

    ```bash
    kubectl exec -n vault vault-0 -- vault status
    ```

    If Vault is still sealed, delete the `vault-0` pod so that the unsealing runs again.

5. Check that the ArangoDB pods of the `support` namespace are running and ready. `KubeCrashRecovery` does not wait for them:

    ```bash
    kubectl get pods -n support | grep arango
    ```

6. To check the platform health, run `exec Diagnostic`. See [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md).

### Result

Every node is `Ready`, every pod is running, Vault is unsealed, and the platform accepts events and logins again.

## Related links

- [Debug your deployment](/self_hosted/1.0.1/troubleshooting/debug_tool.md): Reference of the `RebootNodes` and `KubeCrashRecovery` commands.
- [Use the SHC interface](/self_hosted/1.0.1/operations/controller_interface.md): The Storage tab shows the Ceph status.
- [Run platform diagnostics](/self_hosted/1.0.1/monitoring/run_diagnostics.md): Health checks per platform area.
