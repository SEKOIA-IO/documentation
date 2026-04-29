# The Deployment Process

A central tool called the **Self-Hosted Controller** manages the platform lifecycle. This tool takes a configuration file as a parameter, with all settings described in the configuration section. 

All available commands can be listed by running the `list` command. Specific details for these commands are provided in the relevant sections below (Deployment, Debug, Check). Before proceeding, please consult the list of prerequisites for a Self-Hosted deployment.

## Core Principles
The deployment engine is designed around three fundamental pillars to ensure stability and predictability:

* **Preflight Validation**: The CLI performs comprehensive checks before any execution. It verifies OS versions, network connectivity, and file checksums, blocking execution until the environment meets all minimum requirements.
* **Declarative Configuration**: The platform state is defined by a `config.yml` manifest. This file acts as the single source of truth for infrastructure settings (IPs, load-balancers, DNS), service configurations (SMTP, feature toggles, AI modules), and scaling parameters (node counts, resource quotas).
* **Orchestration**: A core engine computes the difference between the actual and desired state to execute only necessary tasks.

## Workflow Execution
The CLI supports both online and air-gapped environments:

* **Online**: Fetches artifacts directly from authorized registries.
* **Air-gapped**: Operates in fully disconnected modes using pre-staged packages and locally cached manifests.

