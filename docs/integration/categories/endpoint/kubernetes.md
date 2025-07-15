---
uuid: 4a3bb630-951a-40d9-be5e-5c712b37248e
name: Kubernetes Audit Log
type: intake
---

## Overview

Kubernetes is an open-source container orchestration system for automating software deployment, scaling and managment.

In this documentation, you will learn how to configure, collect and send Kubernetes Audit logs to SEKOIA.IO.

- **Supported environment**: On Premise / SaaS

## Configuration of Kubernetes

Enable the audit logs in kubernetes:

- Audit logs are disabled by default. To enable them, you need to specify an audit file path in your API server configuration :

```
 kube-apiserver
  [...]
  --audit-log-path=/var/log/kubernetes/apiserver/audit.log
  --audit-policy-file=/etc/kubernetes/audit-policies/policy.yaml
```

- Create the policy file at /etc/kubernetes/audit-policies/policy.yaml to specify the types of API requests you want to log in your audit logs file. The kubernetes audit policy has different levels:

    - `None` - don't log events that match this rule.
    - `Metadata` - log events with metadata (requesting user, timestamp, resource, verb, etc.) but not request or response body.
    - `Request` - log events with request metadata and body but not response body. This does not apply for non-resource requests.
    - `RequestResponse` - log events with request metadata, request body and response body. This does not apply for non-resource requests.

- You can use this minimal audit policy file to log all requests at the `Metadata` level:

```yaml
# Log all requests at the Metadata level.
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
```

For more information about Kubernetes audit logs, please visit [kubernetes website](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/).

## Collect Configuration

- Enable the log collection in your DaemonSet, there are disabled by default:

```yaml
env:
    # (...)
    - name: DD_LOGS_ENABLED
      value: 'true'
```

- Mount the audit log directory in a path where the Sekoia Agent collect the log file. For that you need to update your daemonset: 

```yaml
 # (...)
    volumeMounts:
      # (...)
      - name: auditdir
        mountPath: /var/log/kubernetes/apiserver
  # (...)
  volumes:
    # (...)
    - hostPath:
        path: /var/log/kubernetes/apiserver
      name: auditdir
  # (...)

```

### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Kubernetes`.

2. Update the Agent configuration:

```yaml
logfiles:
    - filepath: /var/log/kubernetes/apiserver/audit.log  # Path to the file to watch
      intakekey: {intake key}  # Intake key to use to send the events
```

3. Once the configuration file is modified, restart the agent:Once the configuration file is modified, restart the agent.

{!_shared_content/operations_center/integrations/generated/4a3bb630-951a-40d9-be5e-5c712b37248e_sample.md!}

{!_shared_content/operations_center/integrations/generated/4a3bb630-951a-40d9-be5e-5c712b37248e.md!}

## Support

If you need assistance with this integration, please contact our support team at www.support.sekoia.io. 