# seckiot\_citadelle

uuid: ec7fd978-5526-42c8-acd5-e1b4aa752a73 name: Seckiot Citadelle type: intake

### Overview

Seckiot Citadelle is an integrated cybersecurity platform designed for industrial control systems (ICS) and operational technology (OT) environments, providing comprehensive threat detection, asset discovery, and vulnerability management to safeguard critical infrastructure.

* **Vendor**: Seckiot
* **Supported environment**: On Premise & Cloud
* **Version compatibility, if applicable**: 25.5 and more
* **Detection based on**: Alerts, Telemetry
* **Supported application or feature**: Network protocol analysis

### Specification

#### Prerequisites

* **Network**:
  * Outbound traffic allowed
* **Permissions**:
  * Administrator or Root access to the Seckiot Citadelle appliance

#### Transport Protocol/Method

* **Direct HTTPS**

#### Logs details

* **Supported functionalities**: See section [Overview](seckiot_citadelle.md#overview)
* **Supported type(s) of structure**: JSON
* **Supported verbosity level**: Alert

### Step-by-Step Configuration Procedure

#### Instruction on Sekoia

{!\_shared\_content/integration/intake\_configuration.md!}

**Configure Seckiot Alert Forwarding**

1. Log in to the Seckiot platform.
2. In the left panel, click on `Capture architecture`.
3.  Click on `Add -> Add a forwarder`

    {: style="max-width:100%"}
4. Select the forwarder type `Sekoia.io`
5.  Enter a `Name` to identify the forwarder, then go back to the intake you created earlier in step `Configure Your Intake` in the Sekoia platform. Finally, copy your intake key into the `Intake Key` field.

    {: style="max-width:100%"}
6. Click `Add Forwarder`

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/integrations/generated/ec7fd978-5526-42c8-acd5-e1b4aa752a73.md!} {!\_shared\_content/integration/detection\_section.md!} {!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_ec7fd978-5526-42c8-acd5-e1b4aa752a73\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/ec7fd978-5526-42c8-acd5-e1b4aa752a73.md!}
