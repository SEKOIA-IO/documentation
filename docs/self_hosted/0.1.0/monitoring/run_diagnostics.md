# Run platform diagnostics

The Diagnostic module runs targeted health checks against the platform's Prometheus metrics. It reports the health of features so you can narrow an incident to the affected service.

## Prerequisites

- You have access to the orchestration node.
- The platform and its Prometheus service are running.
- You completed the post-deployment validation in [Deploy the platform](../deployment/deployment_guide.md).

!!! warning "Run diagnostics before changing the platform"
    Use the reported likely causes and remediation steps to investigate a failed check. Do not restart or reconfigure services based only on a diagnostic result.

## Run all diagnostic targets

To run every bundled diagnostic target, run:

```bash
./run-shc.sh exec Diagnostic
```

The module runs these targets in alphabetical order:

- `alerts`: alert creation and processing.
- `asset_discovery`: asset discovery processing.
- `asset_management`: asset management processing.
- `telemetry`: telemetry processing.

By default, the terminal report hides successful checks. Failed or warning checks show the affected value and labels, an explanation, likely causes, and remediation actions.

## Run a diagnostic target

To investigate one platform area, set `modules.diagnostic.targets` to its target name:

```bash
./run-shc.sh exec Diagnostic --set modules.diagnostic.targets=alerts
```

To run more than one target, separate their names with commas:

```bash
./run-shc.sh exec Diagnostic --set modules.diagnostic.targets=alerts,telemetry
```

The module continues with the remaining targets when one target cannot be loaded or queried. Review the terminal error for each target that does not produce results.

## Change diagnostic output

To display successful checks as well as warnings and critical checks, set `modules.diagnostic.hide_ok` to `false`:

```bash
./run-shc.sh exec Diagnostic --set modules.diagnostic.targets=alerts --set modules.diagnostic.hide_ok=false
```

To send the report to another tool, set `modules.diagnostic.format` to `text` or `json`:

```bash
./run-shc.sh exec Diagnostic --set modules.diagnostic.format=json --set modules.diagnostic.hide_ok=false
```

The `json` and `text` formats apply to the terminal output. API callers receive the complete result set, including successful checks, regardless of the `hide_ok` setting.

## Result

You have a diagnostic report for the selected platform areas. Use a `CRIT` result to prioritize investigation, and use a `WARN` result to identify degraded behavior before it interrupts service.

## Related links

- [Monitor your platform](monitoring_guide.md): Daily monitoring and incident-response workflows.
- [Debug your deployment](../troubleshooting/debug_tool.md): Additional SHC diagnostic commands and log collection guidance.
- [Deploy the platform](../deployment/deployment_guide.md): Post-deployment validation procedure.
