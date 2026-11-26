# Common issues

This article documents known issues that you can encounter during or after the installation of Sekoia Self-Hosted 1.0. It describes how to identify each issue, apply its workaround, and verify recovery.

## ExaLog Kafka controller registration remains blocked after deployment

This issue was observed with Strimzi 0.51.0 and Kafka 4.1.1, on a deployment with a single controller in the `kafka-quickwit` namespace.

### Symptoms

The `KafkaQuickwit` installation step does not reach a healthy state. The `kafka-quickwit-on-self-hosted` ArgoCD application stays `Synced` and `Degraded`, even though every Kafka pod reports `1/1 Running` and the latest synchronization succeeded.

To inspect the Kafka conditions, run from a host with `kubectl` access to the affected cluster:

```bash
kubectl -n kafka-quickwit get kafka kafka-quickwit-cluster \
  -o jsonpath='{range .status.conditions[*]}{.type}{"="}{.status}{" | "}{.reason}{" | "}{.message}{"\n"}{end}'
```

The affected resource reports:

```text
NotReady=True | UnforceableProblem | An error while trying to determine the active controller
```

The Strimzi operator logs contain:

```text
Timed out waiting for a node assignment. Call: describeMetadataQuorum
```

To identify the controller pod, run:

```bash
kubectl -n kafka-quickwit get pods -l strimzi.io/controller-role=true
```

Replace `<controller-pod>` in the following commands with its name. To inspect its registration, run:

```bash
kubectl -n kafka-quickwit logs <controller-pod> -c kafka
```

The controller becomes leader, then logs the following messages, with no later successful registration:

```text
RegistrationResponseHandler: channel manager timed out before sending the request.
maybeSendControllerRegistration: waiting for the previous RPC to complete.
```

### Cause

The logs indicate that the controller registration remains pending after its initial request times out. The controller continues to process events, but the operator cannot determine the active controller through the Kafka administration API and leaves the Kafka resource `NotReady`.

The startup trigger is not confirmed. A similar registration failure is reported in [Strimzi issue #12760](https://github.com/strimzi/strimzi-kafka-operator/issues/12760), where a transient DNS failure preceded the timeout. Successful DNS resolution and TCP connectivity after startup do not rule out this registration failure.

### Workaround

Restarting the single controller pod recovered the affected deployment. Apply this workaround only when the symptoms above match and the operator can resolve the controller DNS name and reach its TCP port 9090.

!!! warning "Temporary Kafka control plane interruption"
    The single controller is unavailable while its pod restarts. Plan a maintenance window if the platform is already in use. Delete only the controller pod; keep its persistent volume claim and the Kafka resource. If your deployment has several controllers, contact Sekoia support for a recovery procedure adapted to that topology.

1. To restart the blocked controller, run:

    ```bash
    kubectl -n kafka-quickwit delete pod <controller-pod>
    ```

    Strimzi recreates the pod and reuses its persistent volume.

2. To wait for Kafka recovery, run:

    ```bash
    kubectl -n kafka-quickwit wait kafka/kafka-quickwit-cluster \
      --for=condition=Ready --timeout=600s
    ```

    If the command times out, collect the new controller and operator logs and contact Sekoia support before repeating the restart.

3. To check the ArgoCD application, run:

    ```bash
    kubectl -n argocd get application kafka-quickwit-on-self-hosted \
      -o jsonpath='{.status.sync.status}{" | "}{.status.health.status}{"\n"}'
    ```

    After ArgoCD refreshes the application health, the expected output is `Synced | Healthy`. A new synchronization is not required to restart the controller pod.

## PostgreSQL replica creation blocks installation

### Identify the issue

During installation, the self-hosted-controller (SHC) module `PlatformInstallation` fails because the platform installer cannot complete the `CNPGClusters` step. The logs contain:

```text
[critical ] Provisioners failed: CNPGClusters; can't go further
[error    ] Platform installer container failed; inspect the pod logs for the failing step
```

An affected PostgreSQL cluster stays in `Creating a new replica` with one ready primary. Its replica initialization job repeatedly reports `role "streaming_replica" does not exist`. The primary logs report `Unable to update PostgreSQL roles and permissions` with `permission denied to create role`.

### Resolve the issue

From a host with `kubectl` access, recreate the missing role and its `pg_rewind` permissions on the primary. This example targets `sic-pg-cluster` in `support`; adapt the cluster name and namespace if needed.

```bash
CNPG_PRIMARY=$(kubectl -n support get cluster sic-pg-cluster -o jsonpath='{.status.currentPrimary}')
kubectl -n support exec -i "$CNPG_PRIMARY" -c postgres -- \
  psql -X -v ON_ERROR_STOP=1 -U postgres -d postgres <<'SQL'
BEGIN;
CREATE ROLE streaming_replica WITH LOGIN REPLICATION;
GRANT EXECUTE ON FUNCTION
  pg_catalog.pg_ls_dir(text, boolean, boolean),
  pg_catalog.pg_stat_file(text, boolean),
  pg_catalog.pg_read_binary_file(text),
  pg_catalog.pg_read_binary_file(text, bigint, bigint, boolean)
TO streaming_replica;
COMMIT;
SQL
```

The replica initialization job retries automatically. No pod restart or volume deletion is needed. To verify recovery, run:

```bash
kubectl -n support wait cluster/sic-pg-cluster --for=condition=Ready --timeout=600s
```

Once the cluster is ready, run `exec Install` again in the SHC. If recovery times out, inspect the replica initialization job logs and contact Sekoia support.

### Why it happens

This issue was observed with CNPG 1.25.4. The likely cause is a shared monitoring connection retaining `SET ROLE pg_monitor`. When initialization reuses that connection, it lacks permission to create the replication role. CNPG logs the failure without retrying the permission setup during the same server run, leaving the primary operational and replica creation blocked.

## Related links

- [Strimzi issue #12760](https://github.com/strimzi/strimzi-kafka-operator/issues/12760): Upstream report of a controller registration failure after startup.
- [Argo CD resource health](https://argo-cd.readthedocs.io/en/stable/operator-manual/health/): How ArgoCD evaluates application health.
