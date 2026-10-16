# Reset or destroy the platform

The self-hosted-controller (SHC) can remove the Sekoia platform from a dedicated cluster while it verifies that no node still uses a storage volume. Use `PlatformScaleDown` to delete the platform workloads and keep the Kubernetes cluster, or `PlatformDestroy` to also uninstall K3s and wipe the Ceph storage disks before a reinstallation from scratch.

!!! warning "Irreversible operations"
    Both commands permanently delete the platform data stored in the cluster. They do not delete the data stored in your S3-compatible platform storage. Use them only on a dedicated cluster that you intend to reset or decommission.

## Prerequisites

- You run the SHC from the orchestration node. Both commands refuse to run from a pod inside the cluster.
- The Kubernetes cluster is running and the SHC can retrieve its kubeconfig. Both commands start with `GetKubeconfig`, so they cannot run once K3s is uninstalled.
- Every node of `utils.ansible.inventory` is reachable over SSH and provides `python3`, `findmnt`, and `lsblk`.
- For `PlatformDestroy`, the release files are extracted on the orchestration node. The Cilium cleanup tool is extracted from the Cilium image of the release.
- For `PlatformDestroy`, every node also provides `pvs`, `vgchange`, `dmsetup`, `strings`, `wipefs`, `sgdisk`, and `dd`.

## What the commands remove

`PlatformScaleDown` deletes every namespace of the cluster except the following ones, which hold the Kubernetes system services and the storage operators:

| Preserved namespace | Content |
| :--- | :--- |
| `default`, `kube-system`, `kube-public`, `kube-node-lease` | Kubernetes system namespaces. |
| `rook-ceph` | Ceph storage operator. |
| `cnpg-system` | CloudNativePG database operator. |

The ArgoCD namespace is deleted with the platform. Before deleting anything, the command stops the ArgoCD controllers so that they cannot recreate the deleted resources. ArgoCD is not restarted afterwards.

`PlatformDestroy` runs the following phases in order, and stops at the first failure:

1. `CleanupCilium` preparation: stages the Cilium cleanup tool on every node.
2. `PlatformScaleDown`: deletes the platform namespaces and verifies the volume release.
3. `K3SUninstall`: uninstalls K3s from the worker nodes, then from the manager nodes, and removes the Cilium networking from every node.
4. `WipeStorageDisks`: wipes the disks used by Ceph and removes the Rook host state.

## Delete the platform workloads

`PlatformScaleDown` is disabled by default. To enable it for one run, pass `modules.platform_scale_down.enabled=true` as a runtime override.

To delete the platform namespaces, run:

```bash
exec PlatformScaleDown --set modules.platform_scale_down.enabled=true
```

The command proceeds as follows:

- Before deleting anything, it checks that it can delete every resource safely. It stops without deleting anything when a pod of a preserved namespace uses a Ceph volume, when a pod uses a storage driver other than Ceph, or when an API group of the cluster does not respond.
- It deletes the namespaces, then waits until every node has released its client volumes. On each node, it checks that no Ceph or CSI volume is still mounted, that no RBD device is still mapped, and that no NBD device is still active.
- If resources are still blocking after the grace period, it deletes them and removes their blocking finalizers. It removes the finalizers of a persistent volume claim only once its storage is released, and it never modifies volume attachments or persistent volumes.

The command adjusts its timing with the following keys, which it also accepts as `--set` overrides:

| Field | Description | Default |
| :--- | :--- | :--- |
| `modules.platform_scale_down.enabled` | Allows the deletion of the platform namespaces. | `false` |
| `modules.platform_scale_down.grace_period` | Seconds of graceful cleanup before the command removes blocking finalizers. Must be lower than `timeout`. | `120` |
| `modules.platform_scale_down.timeout` | Overall deadline in seconds for the cleanup and the volume release. | `600` |
| `modules.platform_scale_down.poll_interval` | Seconds between two checks. | `5` |

### Result

The log reports `Platform namespaces removed; client volumes released on every inventory host`. The Kubernetes cluster, the Ceph storage operator, and the database operator are still running.

## Destroy the platform and wipe the storage disks

`PlatformDestroy` requires two safety flags: `modules.platform_scale_down.enabled` for the namespace deletion and `modules.wipe_storage.enabled` for the disk wiping. Without both flags set to `true`, the command stops before changing anything.

To destroy the platform, run:

```bash
exec PlatformDestroy --set modules.platform_scale_down.enabled=true --set modules.wipe_storage.enabled=true
```

The command runs its four phases. In the last one, `WipeStorageDisks` selects the whole disks that carry a Ceph LVM volume group, a partition labeled `ceph`, or a Ceph signature in their first 10 MB. It deactivates their Ceph volume groups, then erases the disks with `wipefs`, `sgdisk --zap-all`, and `dd`. It refuses a disk that is mounted, still in use, or shared with a volume group that is not a Ceph volume group. Finally, it removes `/var/lib/rook` on every node, after checking that no K3s or Ceph process is running and that nothing is mounted under that directory.

### Result

The nodes no longer run K3s, their Cilium networking is removed, their storage disks are blank, and their Rook host state is removed. To reinstall the platform, run `Install` again. See [Deploy the platform](../deployment/deployment_guide.md).

## Recover from a failure

Every failure names the phase that stopped, the phases already completed, the phases not attempted, and the next safe step. Do not stop `kubelet`, Ceph, or the CSI drivers to bypass a blocked volume release, and do not unmount or wipe a volume manually.

| Phase that failed | What to do |
| :--- | :--- |
| `CleanupCilium` preparation | Nothing was deleted. Confirm that the release files are extracted on the orchestration node and that every node is reachable, then run the command again. |
| `PlatformScaleDown` | K3s uninstall and disk wiping were not started. Resolve the blockers listed in the error, for example with `findmnt`, `lsblk`, the logs of the CSI node plugin, and `journalctl -u k3s -u k3s-agent` on the reported node, then run `PlatformScaleDown` again to verify the release. |
| `K3SUninstall` | The uninstall may be partially complete. Inspect the failed node and its `k3s` or `k3s-agent` journal. Do not run `PlatformDestroy` again. If K3s was removed but the Cilium networking cleanup failed, run `CleanupCilium`. |
| `WipeStorageDisks` | K3s is already removed. Inspect the failed node and device, then run `WipeStorageDisks` on its own, as described below. Do not run `PlatformDestroy` again. |

!!! warning "Run WipeStorageDisks on its own"
    `WipeStorageDisks` does not accept `--set` overrides. To run it on its own, set `modules.wipe_storage.enabled: true` in your `config.yml`. With the flag unset, the command logs a warning and completes without wiping any disk. Remove the flag from `config.yml` once the disks are wiped.

### Clean up the Cilium networking

`CleanupCilium` removes the Cilium networking left on dedicated nodes after a K3s uninstall: network interfaces, BPF programs, and `CILIUM_` firewall rules for IPv4 and IPv6. Run it when `K3SUninstall` reports an incomplete networking cleanup, or when `CheckNodePortReachability` reports dropped connections on nodes where K3s is stopped.

```bash
exec CleanupCilium
```

The command first checks every node, and changes nothing until all nodes pass. It refuses to run while K3s, containerd, or a Cilium agent is still running on a node, and it refuses any interface, BPF program, mount, or firewall rule that it cannot attribute to Cilium. The output of the cleanup tool is kept on each node in `/var/lib/sekoia-controller/cilium-cleanup/native-output.log`.

## Related links

- [Debug your deployment](../troubleshooting/debug_tool.md): Reference of the SHC commands, including `WipeStorageDisks` and `K3SUninstall`.
- [The deployment process](../deployment/deployment_process.md): Lifecycle operations of the SHC.
- [Deploy the platform](../deployment/deployment_guide.md): Reinstall the platform after a reset.
- [Network requirements](../deployment/network_requirements.md): Ports checked by `CheckNodePortReachability` before a reinstallation.
