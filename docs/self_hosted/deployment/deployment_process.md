# The Deployment process

The Sekoia Self-Hosted platform uses an idempotent, agentless CLI to manage the platform lifecycle. This process unifies installation, configuration, and drift reconciliation.

## Core principles
The deployment engine operates on three main pillars:

* **Preflight validation**: The CLI verifies OS versions, network connectivity, and credentials before any change is applied.
* **Declarative configuration**: You define the desired state of your infrastructure in a `customer.yml` manifest.
* **Orchestration**: A core engine computes the difference between the actual and desired state to execute only necessary tasks.

## Artifact delivery
Each release is delivered as a single digitally signed archive that guarantees tamper evidence and verifiability. This archive contains the core platform and Sekoia applications, including the deployer, Kubernetes stack, and microservices.