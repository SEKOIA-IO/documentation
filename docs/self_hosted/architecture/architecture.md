# Reference Architecture

The Sekoia Self-Hosted architecture is built for resilience and scalability within a customer-managed perimeter.

## Core components
The platform is delivered as a single digitally signed archive containing all necessary applications:

* **Deployer**: Handles the Kubernetes installation and support services.
* **Microservices**: Includes the core platform logic and Sekoia applications.
* **Databases**: Integrated data persistence layers.
* **Rules Catalog**: The collection of Sekoia detection rules.

## High availability logic
The architecture is designed for production-grade reliability:

* **Redundancy**: Built-in component redundancy to prevent single points of failure.
* **Self-healing**: Automated recovery mechanisms for continuous operations.
* **Scalability**: Support for multi-node compute clusters to handle high-volume ingestion.

## Data Workflow

* **Ingestion**: Event logs are sent to forwarders which point to a unique domain/port redirected to your Load Balancer.
* **Processing**: Microservices are decoupled to prevent cascading failures.
* **Storage**: Data is written to an S3-compatible storage managed by the customer.