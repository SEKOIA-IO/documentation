# Deployment configuration

The `customer.yml` file is the central manifest used to describe your specific environment and service requirements.

## Manifest parameters
The following sections must be defined in your configuration file:

### Infrastructure settings
* **Nodes**: List of IP addresses for compute and GPU servers.
* **DNS**: Domain names and resolution settings for the platform.
* **Load Balancer**: Target addresses for Web UI and ingestion flows.

### Service settings
* **SMTP**: Configuration for system notifications and alerts.
* **Feature Toggles**: Activation of specific modules, such as AI features.
* **Resource Quotas**: Scaling parameters and node counts based on your sizing requirements.

!!! note "Validating the Manifest"
    The deployment CLI validates the syntax and integrity of the `customer.yml` file during the preflight stage.