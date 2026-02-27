## Overview

- **Vendor**: Silverfort
- **Product**: Universal-MFA
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication Logs, DailyAuthStatistics
## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder
- **Network**:
    - Outbound traffic allowed
- **Permissions**:
    - Admin access to Silverfort Universal MFA Console
    - Root access to the Linux server with the syslog forwarder
## Step-by-Step Quick Configuration Procedure

1) Log into the Silverfort Universal MFA console and head to:

```
SYSTEM SETTINGS -> Notifications -> Syslog
```

2) Add a Syslog Server and configure the Server Name, Host and Protocol (TCP recommended)

3) Configure the intakes.yaml file to send the Silverfort logs towards the console 
