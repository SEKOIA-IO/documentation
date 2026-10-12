# Known Issues

This page lists known issues affecting Sekoia Self-Hosted releases, along with the workaround to apply until a fixed version is deployed.

## Correlation rules never raise alerts

**Affected versions**: 0.1.0

### Symptoms

* Correlation rules match events but no alert is ever raised.
* Standard (non-correlation) rules raise alerts normally.
* The logs of the `sigma-workflow-sighting-creator` pods show repeated `Connection refused` errors towards `siceventsindex-es-http.support`, until the worker gives up.

To confirm, run:

```bash
kubectl -n sic logs deployment/sigma-workflow-sighting-creator --tail=200 | grep -i "connection refused"
```

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

!!! note
    This change is applied directly to the running deployment. It is part of the platform configuration in the next release, so redeploying with a fixed version keeps the correct behavior.
