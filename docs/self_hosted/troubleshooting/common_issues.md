# Common issues

This article documents known issues that can occur during or after installation, along with their resolution procedure.

---

## ArangoDB provisioning failure during `PlatformInstallation`

**Affects:** v0.0.1  
**Fix scheduled:** Next release

### Symptom

The `PlatformInstallation` command fails with the following error sequence in the logs:

```json
{"module":"PlatformInstallation","job_provisioner":"ArangoDB","event":"Creating users","level":"info"}
{"module":"PlatformInstallation","job_provisioner":"KubernetesClient","event":"STDERR [kubectl ... exec -i arangodb-crdn-... -c server -- arangosh]: command terminated with exit code 1","level":"info"}
{"module":"PlatformInstallation","job_provisioner":"ArangoDB","event":"arangosh command returned an error","level":"info"}
{"module":"PlatformInstallation","job_provisioner":"ArangoDB","event":"Failed to execute arangosh command on coordinator","level":"info"}
{"module":"PlatformInstallation","job_provisioner":"Installer","event":"Exception was raised in step ArangoDB","level":"info"}
{"module":"PlatformInstallation","job_provisioner":"Installer","event":"One or more step failed, can't go further","level":"info"}
{"component":"platform-installer","exit_code":42,"event":"Job container exited with non-zero code","level":"error"}
```

The command exits with:

```
╭─────────────────────────────────── Error ────────────────────────────────────╮
│ install failed after 1 attempt(s)                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Cause

The ArangoDB operator occasionally fails to fully initialize before the platform installer attempts to provision users. This is a timing issue that occurs intermittently on first installation.

### Resolution

**Step 1: Wait for the operator to self-recover.**

The ArangoDB operator recovers automatically in most cases. Wait 1 hour, then check pod status:

```bash
kubectl get pods -A | grep arango
```

If all ArangoDB pods show `Running`, proceed to [retry the installation](#step-3-retry-the-installation). If one or more pods are still not running after 1 hour, continue with step 2.

**Step 2: Manually clean up the ArangoDB state.**

Run the debug platform installer to open an interactive shell:

```bash
./run-shc.sh exec DebugPlatformInstallation
kubectl exec -it -n sekoia-system jobs/shpi-debug-pause-platform-installer-job -- bash
```

Inside the shell, run the teardown command. This command is expected to fail after a moment:

```bash
./platform-installer exec ArangoDB -m teardown
```

Exit the shell (`exit` or `Ctrl+D`), then delete the ArangoDB operator resources:

```bash
kubectl delete deployments.apps -n support arangodb-exporter
kubectl delete deployments.apps -n support arango-deployment-operator
kubectl delete secret -n support arangodb-operator-api-jwt arangodb-operator-api-jwt-key arangodb-operator-dashboard
kubectl delete cm -n support arangodb-operator-feature-config-map
```

**Step 3: Retry the installation.**

```bash
./run-shc.sh exec PlatformInstallation
```

If the installation fails again at the same `ArangoDB` step, repeat step 2 and step 3.

---

## Related links

- [Debug your deployment](./debug_tool.md): Full SHC debug command reference.
- [Deploy the platform](../deployment/deployment_guide.md): Installation steps and post-deployment validation.
- [Release notes v0.0.1](../release_notes/0.0.1.md): Known issues and limitations for this version.
