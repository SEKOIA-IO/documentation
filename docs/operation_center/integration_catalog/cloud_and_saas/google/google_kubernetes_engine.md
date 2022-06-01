uuid: 00bbde4f-cb17-4c3f-9f5e-a585fc7c8fc0
name: Google Kubernetes Engine (GKE)
type: intake

{!operation_center/integration_catalog/cloud_and_saas/google/google_cloud.md!}


## Google Kubernetes Engine (GKE) configuration

To start working with GKE, you should create a [Logs Router Sinks](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=en#creating_sink) according to your needs.

There's multiple kind of logs produced by GKE:

**Auditd logs**: Most import logs from a security point of view. We recommend that you use [Auditbeat](../../../endpoint/auditbeat_linux/) to collect Auditd logs.

**Activity logs**:

  - operations done on GCP cluster resources (create a cluster, etc.) `resource.type: gke_cluster` (*Intake type: Google Cloud Audit log*)
  - operations done on Kubernetes objects “inside” clusters (Kubernetes Audit Policy) `resource.type: k8s_cluster` (*Intake type: Google Cloud Audit log*)

**Event logs**: Kubernetes events are objects that provide insight into what is happening inside a cluster, such as what decisions were made by scheduler or why some pods were evicted from the node `log_id("events")`

**Node logs**: Services running on GKE nodes (kubelet, node problem detector, container runtime, etc.) emit their own logs `resource.type: k8s_node`

**Container logs**: Container stdout and stderr streams `log_id("stdout") log_id("stderr")`

**Instance logs**: Serial console output `log_id("serialconsole.googleapis.com/serial_port_1_output")`

To go further, consult the following resources:

- [Cloud Forensics 101 (Cloud Next '18)](https://youtu.be/OkjTqlETgMA)
- [A quick GKE logs primer](https://medium.com/google-cloud/a-quick-gke-logs-primer-a978f60daa7)


{!operation_center/integration_catalog/generated/google-kubernetes-engine_do_not_edit_manually.md!}
