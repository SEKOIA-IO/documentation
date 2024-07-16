uuid: 00bbde4f-cb17-4c3f-9f5e-a585fc7c8fc0
name: Google Kubernetes Engine (GKE)
type: intake

{!_shared_content/operations_center/integrations/google_cloud.md!}

{!_shared_content/operations_center/integrations/generated/00bbde4f-cb17-4c3f-9f5e-a585fc7c8fc0.md!}


## Google Kubernetes Engine (GKE) configuration

There are different types of logs produced by GKE:

**Auditd logs**: Most important logs from a security point of view. We recommend that you use [Auditbeat](../../../endpoint/auditbeat_linux/) to collect Auditd logs.

**Flow Logs**: From [Google VPC FLow Logs documentation](https://cloud.google.com/vpc/docs/using-flow-logs):
> VPC Flow Logs records a sample of network flows sent from and received by VM instances, including instances used as GKE nodes. These logs can be used for network monitoring, forensics, real-time security analysis, and expense optimization.

Please read the [dedicated documentation](google_vpc_flow_logs.md).
(*Intake type: Google VPC Flow Logs*)

**Activity logs** (*Intake type: Google Cloud Audit log*):

  - operations done on GCP cluster resources (create a cluster, etc.) `resource.type: gke_cluster`
  - operations done on Kubernetes objects “inside” clusters (Kubernetes Audit Policy) `resource.type: k8s_cluster`

**Event logs**: Kubernetes events are objects that provide insight into what is happening inside a cluster, such as what decisions were made by the scheduler or why some pods were evicted from the node `log_id("events")` (*Intake type: Google Cloud Audit log*)

**Node logs**: Services running on GKE nodes (kubelet, node problem detector, container runtime, etc.) emit their own logs `resource.type: k8s_node`

**Container logs**: Container stdout and stderr streams `log_id("stdout") log_id("stderr")`

**Instance logs**: Serial console output `log_id("serialconsole.googleapis.com/serial_port_1_output")`

To learn more, consult the following resources:

- [Youtube video - Cloud Forensics 101 (Cloud Next '18)](https://youtu.be/OkjTqlETgMA)
- [Blog post - A quick GKE logs primer](https://medium.com/google-cloud/a-quick-gke-logs-primer-a978f60daa7)
