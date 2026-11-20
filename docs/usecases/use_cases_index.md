# Use cases

Sekoia use cases show how security teams solve concrete operational problems with the platform. Each tutorial starts with a situation you may recognize, shows how to achieve the outcome in Sekoia, and links to the detailed product documentation for configuration and reference information.

## Use your data and intelligence

Bring your own telemetry, indicators, and export workflows into the security operations process.

- [Export large volumes of events for investigation or compliance](massive_export.md): Extract a completed event search and send the result to local storage or your own data lake.
- [Detect threats with your own CTI](use_your_own_cti.md): Import indicators into an IOC Collection and use them in detection rules.
- [Implement a blocklist in Sekoia](implement_blocklist.md): Publish observable values to a firewall or proxy through an IOC Collection feed.

## Connect Sekoia to your workflow

Use playbooks to send information to external tools, keep asset data consistent, and notify the people who need to act.

- [Synchronize alerts with an external tool](synchronize_alerts.md): Send alert metadata to an external security or workflow platform.
- [Synchronize assets with Active Directory](synchronize_asset_with_ad.md): Consolidate asset identities with data from Active Directory.
- [Send notifications to a webhook using a playbook](notifications_using_playbooks.md): Forward alert information to Slack, Microsoft Teams, or another webhook endpoint.

## Operate and optimize

Use these tutorials when you need to understand or reduce the volume entering the platform.

- [Investigate fair use overusage](investigate_overusage.md): Identify the community, intake, dialect, or event source responsible for a usage increase.
- [Reduce log volume without losing the signal you need](log_volume_reduction_strategies.md): Choose the right filtering level for noisy event sources.

## Find product details

Use cases explain how to reach an outcome. The product sections contain the configuration steps, field references, permissions, and troubleshooting information behind each workflow.

- [Investigate](https://docs.sekoia.com/sekoia-solutions/defend/investigate/investigate): Investigate alerts, events, and cases.
- [Automate](https://docs.sekoia.com/sekoia-solutions/defend/automate/automate): Build and run playbooks.
- [IOC Collections](https://docs.sekoia.com/sekoia-solutions/cti/consume/ioccollections): Create collections, import indicators, and expose feeds.
- [Sekoia Elevate](https://docs.sekoia.com/sekoia-solutions/elevate/elevate_overview): Understand Elevate investigations, runbooks, findings, and verdicts.

Self-Hosted deployment scenarios are documented in [Sekoia Self-Hosted](https://docs.sekoia.com/self-hosted), alongside the version-specific deployment and operations guides.
