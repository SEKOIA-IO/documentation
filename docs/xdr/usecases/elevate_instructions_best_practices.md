# Write effective instructions for Elevate

Elevate produces better verdicts when it understands your environment. Without context, the agent investigates every alert against generic assumptions: it does not know which IP ranges are internal, which accounts are privileged, or which behaviors are routine in your organization. Custom instructions fill that gap.

This article explains what to include in your instructions and provides examples you can adapt.

## What the agent does with your instructions

The agent reads your instructions before analyzing each alert. It uses them to distinguish expected activity from suspicious activity in your specific environment. An IP address that looks external to the agent may be a known VPN exit node. A service account running scripts at 3 AM may be a scheduled task, not an intrusion. Instructions give the agent the local knowledge it cannot infer from telemetry alone.

The more precise and factual your instructions are, the more relevant the agent's findings become.

## What to include

### Network context

Describe your internal address space, VPN ranges, and any external IP addresses or CIDR blocks that are legitimate in your environment. This helps the agent avoid flagging internal traffic as suspicious lateral movement or treating known infrastructure as a threat.

??? example "Network context instructions"
    Internal network ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
    Corporate VPN exit nodes: 185.220.10.0/24.
    Cloud infrastructure (AWS eu-west-1): 52.18.0.0/16.
    DNS and NTP servers: 10.0.0.1, 10.0.0.2. These generate high query volumes and should not be flagged for DNS anomalies.

### User and account context

Identify privileged accounts, service accounts, and administrative users whose activity differs significantly from standard user behavior. Specify what those accounts are expected to do so the agent does not treat routine privileged operations as indicators of compromise.

??? example "User and account context instructions"
    svc-backup@corp.com is a service account that runs nightly backup jobs between 01:00 and 04:00 UTC. Mass file access during this window is expected.
    admin-deploy@corp.com performs software deployments every Tuesday between 08:00 and 12:00 UTC and regularly executes PowerShell scripts on production servers.
    The domain admins group (DA-CORP) legitimately accesses all servers. Lateral movement from these accounts should be investigated but not automatically classified as a true positive.

### Business hours and operational calendar

Define your organization's normal operating hours and any recurring maintenance windows. This helps the agent calibrate the significance of activity that occurs outside business hours, which is a common indicator used in many detection rules.

??? example "Business hours instructions"
    Standard operating hours: Monday to Friday, 08:00 to 19:00 CET.
    Maintenance windows: every Sunday between 02:00 and 06:00 UTC. High system activity, remote connections, and configuration changes during this window are expected.
    The organization operates across three time zones (CET, EST, SGT). After-hours activity from Singapore-based users is normal.

### Known third-party tools and integrations

List security tools, monitoring agents, SaaS connectors, and other third-party software that generate telemetry patterns that could resemble malicious activity, such as vulnerability scanners, endpoint agents, or cloud sync services.

??? example "Third-party tools instructions"
    Qualys vulnerability scanner runs from 10.0.5.10 every weekday at 22:00 UTC and performs port scans across all internal subnets. This activity is authorized and should not be treated as reconnaissance.
    CrowdStrike Falcon agent is deployed on all endpoints and regularly injects into processes for monitoring purposes. Process injection from the Falcon sensor is expected behavior.
    Microsoft Intune performs MDM enrollment and policy pushes from the Azure IP range 40.74.0.0/15.

### Environment-specific false positive patterns

Document recurring false positive patterns specific to your environment that the agent should weigh carefully. These are situations where your infrastructure reliably produces alerts that are benign.

??? example "False positive pattern instructions"
    The development environment (dev.corp.com) regularly triggers impossible travel alerts because developers use shared VPN accounts from multiple locations simultaneously.
    PowerShell execution from the IT helpdesk workstations (OU=Helpdesk,DC=corp,DC=com) is routine. These machines run remote support scripts daily.

## What to avoid

**Vague statements** reduce instruction effectiveness. "We have many servers" gives the agent nothing to work with. Prefer specific ranges, account names, and time windows.

**Contradictory instructions** confuse the agent. If you state that an account is a service account but also describe it as a user who logs in interactively, the agent cannot resolve the conflict reliably.

**Listing every possible false positive** is counterproductive. Instructions are not a suppression list. Use them to describe your environment, not to tell the agent to ignore entire alert categories.

## Instructions at workspace vs. community level

If your workspace serves multiple customers or business units with different environments, write separate instructions per community rather than combining all context into a single workspace-level instruction block. Community-level instructions are more precise and prevent context from one tenant influencing the analysis of another.

See [Add custom instructions for Elevate agents](/xdr/features/modules/elevate_custom_instructions.md) for the configuration steps.

## Related links

- [Add custom instructions for Elevate agents](/xdr/features/modules/elevate_custom_instructions.md): Step-by-step instructions for adding contextual instructions and customizing runbook reasoning questions.
- [Elevate](/xdr/features/modules/elevate_overview.md): Concept overview of how Elevate works and its key concepts.
- [Investigate an alert with Elevate](/xdr/features/modules/elevate_investigate_alert.md): How to read an AI investigation report and assess whether instructions are influencing findings as expected.
