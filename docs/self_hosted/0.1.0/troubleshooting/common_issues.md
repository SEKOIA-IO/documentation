# Common issues

This article documents known issues that can occur during or after installation of Sekoia Self-Hosted 0.1.0, along with their resolution procedure. All commands are run from the **administration node**.

---

## Correlation rules never raise alerts

**Affects:** v0.1.0
**Fix scheduled:** Next release

### Symptom

Detection rules that match a single event raise alerts as expected, but correlation rules (`event_count`, `value_count`, `temporal`, and chained correlations) never raise an alert, even when their conditions are met.

The logs of the `sigma-workflow-sighting-creator` deployment show repeated connection failures to Elasticsearch, followed by retries:

```bash
kubectl logs -n sic deploy/sigma-workflow-sighting-creator --since=1h | grep -i "connection refused"
```

The failing requests target `siceventsindex-es-http.support`.

### Cause

After a correlation rule matches, the `sigma-workflow-sighting-creator` worker fetches the matched events to build the alert. In this release, the worker reads them from the default Elasticsearch cluster, which is not deployed on Sekoia Self-Hosted: events are stored in Quickwit. Every request fails with `Connection refused`, and the worker gives up after its retries, so no alert is created.

### Resolution

### Workaround

Configure the sighting creator to look up each community's storage (Quickwit) instead of the default Elasticsearch, by setting two environment variables on the deployment:

```bash
kubectl -n sic set env deployment/sigma-workflow-sighting-creator \
  MULTI_STORAGE_ENABLED="true" \
  QUICKWIT_BASE_URL="http://quickwit-metastore.quickwit:7280"
```

This triggers a rolling restart of the pods. Wait for it to complete:

```bash
kubectl -n sic rollout status deployment/sigma-workflow-sighting-creator
```

Check that the variables are applied:

```bash
kubectl -n sic set env deployment/sigma-workflow-sighting-creator --list | grep -E "MULTI_STORAGE_ENABLED|QUICKWIT_BASE_URL"
```

Correlation rules raise alerts again for new matches. Matches that occurred before the workaround are not replayed.


!!! warning "Re-apply after a synchronization"
    The ConfigMap is managed by ArgoCD. A synchronization of the `sigma-workflow-on-self-hosted` application, or a re-run of the `Install` execution plan, restores the original configuration.
    It is part of the platform configuration in the next release, so redeploying with a fixed version keeps the correct behavior.

---

## Related links

- [Debug your deployment](./debug_tool.md): Full SHC debug command reference.
- [Run platform diagnostics](../monitoring/run_diagnostics.md): Rule-based diagnostics for the alerts pipeline.
- [Release notes v0.1.0](../release_notes.md): Known issues and limitations for this version.
