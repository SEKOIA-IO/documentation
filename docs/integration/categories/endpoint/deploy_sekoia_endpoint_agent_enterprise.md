# Deploy the Sekoia Endpoint Agent at scale

This article explains how to deploy the Sekoia Endpoint Agent across a fleet of endpoints using Microsoft Intune on macOS and either Microsoft Intune or Group Policy Objects (GPOs) on Windows. It is intended for IT administrators managing enterprise or large-scale environments.

## Prerequisites

Before deploying at scale:

1. Create a dedicated intake in Sekoia. See [Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md#step-1-create-an-intake).
2. Retrieve your intake key from the intake configuration page.
3. Verify that the required network streams are open on your endpoints. See [Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md#prerequisites).

## Deploy on macOS via Microsoft Intune

On macOS, the agent is distributed as a `.app` bundle inside a `.zip` archive. The Intune deployment involves three steps:

1. Repackage the agent as a flat `.pkg` installer.
2. Push a Privacy Preferences Policy Control (PPPC) profile to grant Full Disk Access silently.
3. Deploy a shell script via Intune to install the agent with the correct intake key.

### Step 1: Create the .pkg installer

Repackage the `.app` bundle into a flat `.pkg` using `pkgbuild` on any macOS machine:

```shell
# Unzip the downloaded archive
unzip SekoiaEndpointAgent.zip -d /tmp/SekoiaAgent/

# Create a staging directory that mirrors the install root
mkdir -p /tmp/SekoiaAgentPkg/Applications
cp -R /tmp/SekoiaAgent/SekoiaEndpointAgent.app \
      /tmp/SekoiaAgentPkg/Applications/

# Build the flat .pkg
pkgbuild \
  --root /tmp/SekoiaAgentPkg \
  --identifier io.sekoia.endpointagent \
  --version "1.0" \
  --install-location "/" \
  SekoiaEndpointAgent.pkg
```

Upload the resulting `SekoiaEndpointAgent.pkg` to Intune under **Apps > macOS > Add > Line-of-business app**.

### Step 2: Push the Full Disk Access profile

The agent requires Full Disk Access to collect security events from the OS. Create a Device Configuration Profile in Intune under **Devices > macOS > Configuration profiles > Create > New policy > Templates > Custom**, using the following mobileconfig payload:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>PayloadContent</key>
    <array>
      <dict>
        <key>PayloadType</key>
        <string>com.apple.TCC.configuration-profile-policy</string>
        <key>PayloadIdentifier</key>
        <string>io.sekoia.pppc.endpointagent</string>
        <key>PayloadUUID</key>
        <string>A1B2C3D4-E5F6-7890-ABCD-EF1234567890</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>Services</key>
        <dict>
          <key>SystemPolicyAllFiles</key>
          <array>
            <dict>
              <key>Allowed</key>
              <true/>
              <key>CodeRequirement</key>
              <string>identifier "io.sekoia.SekoiaEndpointAgent" and anchor apple generic</string>
              <key>Comment</key>
              <string>Allow Full Disk Access for Sekoia Endpoint Agent</string>
              <key>Identifier</key>
              <string>io.sekoia.SekoiaEndpointAgent</string>
              <key>IdentifierType</key>
              <string>bundleID</string>
            </dict>
          </array>
        </dict>
      </dict>
    </array>
    <key>PayloadDescription</key>
    <string>Grants Full Disk Access to Sekoia Endpoint Agent</string>
    <key>PayloadDisplayName</key>
    <string>Sekoia Endpoint Agent - Full Disk Access</string>
    <key>PayloadIdentifier</key>
    <string>io.sekoia.pppc.profile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>B2C3D4E5-F6A7-8901-BCDE-F12345678901</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
  </dict>
</plist>
```

!!! note "Verify the bundle ID and UUIDs before deploying"
    Replace `io.sekoia.SekoiaEndpointAgent` with the actual bundle ID if it differs. To verify it, run:

    ```bash
    codesign -dv --verbose=4 SekoiaEndpointAgent.app 2>&1 | grep Identifier
    ```

    The `PayloadUUID` values in the payload above are examples. Generate unique UUIDs for your own deployment to avoid conflicts with other profiles in your Intune tenant.

Assign this profile to the target device group in Intune **before** deploying the application package.

### Step 3: Deploy the installation script

In Intune, go to **Devices > macOS > Shell scripts > Add** and upload the following script:

```bash
#!/bin/bash
set -e

INTAKE_KEY="<YOUR_INTAKE_KEY>"
REGION="fra1"   # Adjust to your region: fra1, fra2, mco1, uae1, usa1, sgp1
AGENT_BIN="/Applications/SekoiaEndpointAgent.app/Contents/MacOs/SekoiaEndpointAgent"

sudo "$AGENT_BIN" install \
  --intake-key "$INTAKE_KEY" \
  --region "$REGION"

sudo launchctl print system/SEKOIAEndpointAgent
```

Configure the script in Intune with the following settings:

| Setting | Value |
|---|---|
| Run script as signed-in user | No (runs as root) |
| Hide script notifications on devices | Yes |
| Script frequency | Not configured (run once) |
| Max number of times to retry if script fails | 3 |

!!! warning "Execution order"
    The PPPC profile must be applied on target devices before this script runs. Without Full Disk Access, the agent installs but cannot collect events.

## Deploy on Windows via Microsoft Intune

The agent ships as a self-contained `.exe` installer that supports silent, unattended installation. Intune requires `.exe` installers to be wrapped as `.intunewin` packages using the [Microsoft Win32 Content Prep Tool](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool).

### Step 1: Prepare the package folder

Create a folder named `SekoiaAgentPackage` containing `agent-latest.exe` and the two following scripts.

`install.ps1`:

```powershell
param()
$AgentPath = Join-Path $PSScriptRoot "agent-latest.exe"
$IntakeKey = "<YOUR_INTAKE_KEY>"
$Region    = "fra1"

Start-Process -FilePath $AgentPath `
  -ArgumentList "install --intake-key $IntakeKey --region $Region" `
  -Wait -NoNewWindow
```

`uninstall.ps1`:

```powershell
param()
$AgentPath = Join-Path $PSScriptRoot "agent-latest.exe"
Start-Process -FilePath $AgentPath `
  -ArgumentList "uninstall" `
  -Wait -NoNewWindow
```

### Step 2: Convert to .intunewin

```shell
IntuneWinAppUtil.exe -c .\SekoiaAgentPackage -s agent-latest.exe -o .\output
```

### Step 3: Add the app in Intune

In **Intune > Apps > Windows > Add > Windows app (Win32)**, configure the app with the following settings:

| Setting | Value |
|---|---|
| App package file | `SekoiaEndpointAgent.intunewin` |
| Install command | `powershell.exe -ExecutionPolicy Bypass -File install.ps1` |
| Uninstall command | `powershell.exe -ExecutionPolicy Bypass -File uninstall.ps1` |
| Install behavior | System |
| Device restart behavior | No specific action |
| Detection rule type | Registry |
| Key path | `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SEKOIAEndpointAgent` |
| Value name | `Start` |
| Detection method | Key exists |

### Step 4: Verify deployment

After the Intune policy applies, confirm the service is running on target machines:

```powershell
Get-Service SEKOIAEndpointAgent | Select-Object Status, StartType
```

The service should show `Running` with `StartType` set to `Automatic`.

## Deploy on Windows via Group Policy Object

GPO is suitable for on-premises or hybrid environments where computers are domain-joined. Two methods are available.

### Option A: GPO startup script

1. Open Group Policy Management Console (GPMC) and create or edit a GPO linked to the target OU.
2. Go to **Computer Configuration > Policies > Windows Settings > Scripts (Startup/Shutdown) > Startup**.
3. Add a PowerShell script with the following content:

```powershell
$AgentPath = "\\<fileserver>\NETLOGON\SekoiaAgent\agent-latest.exe"
$IntakeKey = "<YOUR_INTAKE_KEY>"
$Region    = "fra1"

$svc = Get-Service -Name "SEKOIAEndpointAgent" -ErrorAction SilentlyContinue
if (-not $svc) {
    Start-Process -FilePath $AgentPath `
      -ArgumentList "install --intake-key $IntakeKey --region $Region" `
      -Wait -NoNewWindow
}
```

!!! tip "Network share permissions"
    Store `agent-latest.exe` on a network share accessible to all target machines (for example, `\\<fileserver>\NETLOGON\SekoiaAgent`). Grant Read access to **computer accounts**, not just user accounts, because startup scripts run before logon.

### Option B: GPO scheduled task (recommended)

Scheduled tasks are more reliable than startup scripts because they execute after network connectivity is established.

1. In the GPO, go to **Computer Configuration > Preferences > Control Panel Settings > Scheduled Tasks > New > Scheduled Task (At least Windows 7)**.
2. Configure the task with the following settings:

| Setting | Value |
|---|---|
| Action | Create |
| Task name | `Sekoia Endpoint Agent Install` |
| Run as | `NT AUTHORITY\SYSTEM` |
| Trigger | At startup, with a 2-minute delay |
| Action (program) | `powershell.exe` |
| Action (arguments) | `-ExecutionPolicy Bypass -File "\\<fileserver>\NETLOGON\SekoiaAgent\install.ps1"` |
| Run only if network available | Yes |

### Verify deployment

After the GPO applies, confirm the service is running on target machines:

```powershell
Get-Service SEKOIAEndpointAgent | Select-Object Status, StartType
```

The service should show `Running` with `StartType` set to `Automatic`.

## Enable optional features during deployment

### Enable Host Hygiene collection

!!! note "Reveal module required"
    Host Hygiene telemetry collection is a feature of the Sekoia Reveal module. Contact your Sekoia account team to enable it.

To enable Host Hygiene collection at install time, append `--compliance-collector` to the installation command in the relevant script.

=== "Windows"

    ```powershell
    .\agent-latest.exe install `
      --intake-key "<YOUR_INTAKE_KEY>" `
      --region "fra1" `
      --compliance-collector
    ```

=== "macOS"

    ```bash
    sudo "$AGENT_BIN" install \
      --intake-key "$INTAKE_KEY" \
      --region "$REGION" \
      --compliance-collector
    ```

## Troubleshoot enterprise deployment

### macOS: agent not collecting events after Intune deployment

- Confirm the PPPC profile is applied: check **System Settings > Privacy & Security > Full Disk Access** for `SekoiaEndpointAgent`.
- Inspect the launchd service status: `sudo launchctl print system/SEKOIAEndpointAgent`.
- Review the agent log at `/var/log/endpoint-agent/agent.log`.
- Test connectivity to the intake endpoint: `curl -v https://intake.sekoia.io/`.

### Windows: service not installed after Intune or GPO deployment

- Check **Event Viewer > Windows Logs > Application** for PowerShell execution errors.
- Verify the service exists: `Get-Service SEKOIAEndpointAgent`.
- Run the installer interactively as SYSTEM using [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec): `psexec -s -i powershell.exe`.
- Confirm outbound HTTPS (TCP 443) is allowed to the intake and API endpoints for your region. See [Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md#prerequisites).

For general agent log paths and CLI reference, see [Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md).

## Related articles

[Install the Sekoia Endpoint Agent](/integration/categories/endpoint/install_sekoia_endpoint_agent.md): How to create an intake, download, and install the agent on a single host.

[Configure the Sekoia Endpoint Agent](/integration/categories/endpoint/configure_sekoia_endpoint_agent.md): How to set up log file collection, proxy, retention, and optional features.

[Sekoia Endpoint Agent](/integration/categories/endpoint/sekoia_endpoint_agent.md): Overview of the agent, supported OS versions, prerequisites, and resource footprint.

[Troubleshoot the Sekoia Endpoint Agent](/integration/categories/endpoint/troubleshoot_sekoia_endpoint_agent.md): How to read agent logs and resolve common errors.
