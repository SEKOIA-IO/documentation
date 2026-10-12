# Import the CTI database

The self-hosted-controller (SHC) imports the Sekoia CTI database into the ArangoDB database of your platform with the `ImportArangoCollection` command. It downloads the latest CTI export from the Sekoia release bucket and loads the STIX objects and relationships it contains.

## Prerequisites

- The platform is installed and the SHC can retrieve its kubeconfig.
- The `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables hold the Sekoia release bucket credentials provided by Sekoia, and `global.version.fetch` points to the Sekoia release bucket, as described in [Configure the deployment](../deployment/deployment_configuration.md#release-download-and-security-content).

## Import the CTI database

!!! tip "Safe to run again"
    The import updates the documents that already exist. If an import fails, run the command again.

1. To read the ArangoDB root password of the platform, run on the orchestration node:

    ```bash
    export ARANGO_ROOT_PASSWORD="$(kubectl -n support get secret arangodb-operator-dashboard -o jsonpath='{.data.password}' | base64 -d)"
    ```

2. Add `-e ARANGO_ROOT_PASSWORD="$ARANGO_ROOT_PASSWORD"` to the `docker run` command of the [execution script](../deployment/deployment_guide.md#step-4-create-the-execution-script).

3. To import the CTI database, run:

    ```bash
    exec ImportArangoCollection
    ```

## Select a CTI version

By default, the command imports the latest CTI export. To import another export, set `global.version.data.cti.version`:

| Value | Imported export |
| :--- | :--- |
| `latest` | The latest completed export. This is the default. |
| A day, for example `2026-09-03` | The most recent completed export of that day, for each collection. |

For example, to import the export of a given day for one run:

```bash
exec ImportArangoCollection --set global.version.data.cti.version=2026-09-03
```

## Result

The command logs an `Import progress` line for each part it loads, then a summary of the documents created and updated per collection. If a collection fails, the command still imports the other ones and lists every failure at the end.

## Related links

- [Use the SHC interface](./controller_interface.md): Run SHC commands and runtime overrides.
- [Configure the deployment](../deployment/deployment_configuration.md): Set the release bucket credentials and endpoint.
- [Deploy the platform](../deployment/deployment_guide.md): Prepare the SHC execution script.
