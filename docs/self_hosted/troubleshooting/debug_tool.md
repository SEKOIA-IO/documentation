# Troubleshooting with the Debug Tool

The Sekoia Self-Hosted CLI includes specialized diagnostic tools to assist in troubleshooting deployment or operational issues.

## Debug capabilities
The debug tool can perform the following actions:

* **Connectivity checks**: Verify network paths between compute nodes and storage.
* **Integrity checks**: Confirm that all deployed artifacts match the expected signatures.
* **State reconciliation**: Identify configuration drift and force a synchronization.

## Running a debug session
To initiate a debug session:
1.  Access the orchestration node.
2.  Run the CLI with the `debug` flag.
3.  Review the automated report for any "failed" status indicators.