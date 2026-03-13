# Deploy the platform

This guide describes how to install the Sekoia Self-Hosted platform using the orchestration CLI.

## Prerequisites
* An orchestration node running Debian 12 with Python 3.11.
* A completed `customer.yml` manifest.
* Access to the digitally signed Sekoia installer archive.

## Procedure

### 1. Extract the installer
To begin, set up the deployment environment on your orchestration node.

1.  Navigate to your installation directory.
2.  Extract the signed archive.
3.  Initialize the deployment CLI.

### 2. Run preflight checks
You must validate the environment before proceeding with the installation.

1.  Execute the CLI `check` command.
2.  Review the output to confirm all hardware and network requirements are met.
3.  Resolve any reported failures.

!!! warning "Preflight block"
    The installation will not proceed if critical validation checks fail.

### 3. Launch orchestration
Trigger the deployment to configure the platform components.

1.  Load the `customer.yml` manifest.
2.  Run the `deploy` command.
3.  Wait for the final convergence report.

## Results
The Sekoia platform is now operational. You can access the interface via the load balancer URL provided in your configuration.