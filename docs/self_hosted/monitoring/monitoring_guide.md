# Monitor cluster health

Sekoia Self-Hosted includes integrated tools to provide real-time visibility into cluster health and performance.

## Built-in dashboards
You can access monitoring dashboards within the platform to view:
* Cluster resource usage (CPU, RAM, Storage).
* Microservices status and logs.
* Event ingestion rates and processing latency.

## Diagnostic collection
To troubleshoot performance issues, you can generate a diagnostic bundle using the deployment CLI.

1.  Connect to the orchestration node.
2.  Run the CLI `diagnose` command.
3.  Export the resulting log bundle for analysis.