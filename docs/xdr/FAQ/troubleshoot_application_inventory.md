# Troubleshoot application inventory

_**[Reveal module](/xdr/features/modules/reveal_index.md)**. The Asset application tab is a feature of the Reveal add-on module._

Use this guide when the Asset Applications tab is unavailable, the application list is empty, or an expected application is missing from an asset.

## The Applications tab is unavailable

Check the following:

- You have access to Reveal.
- The selected asset supports the current Applications capability.
- A connected source can provide application data.
- The source has synchronized successfully.
- The Applications capability is enabled for your community.

If you use the Sekoia Endpoint Agent, confirm that the `software-collector` role is enabled on the agent. It is the only role the Applications tab needs, and it requires an intake key.

The `event-collector` and `compliance-collector` roles collect events and host hygiene data. They are useful, but the Applications tab does not depend on them: without `software-collector`, the tab can remain empty even when Hygiene data is available.

If the tab remains unavailable, contact a community administrator or Sekoia support.

## The Applications tab is empty

An empty application list does not always mean that the asset has no applications.

1. Confirm that you selected the correct asset.
2. Check that an endpoint or asset source is connected.
3. Check the source's last synchronization status.
4. Confirm that the source contains application inventory for the asset.
5. Clear the search term and filters.
6. Check whether the application type and operating system are supported.

## An expected application is missing

Application inventory depends on the source's supported inventory path.

Check the following:

- The application is present in the source inventory.
- The source synchronized after the application was installed or executed.
- The asset identity in the source matches the asset identity in Reveal.
- The application type is supported.
- The application is not containerized or running only inside Docker.

Containerized or Docker applications may not appear in the Applications tab.

## Application and vulnerability counts do not match

The **Vulnerable Applications** count represents applications with associated vulnerability findings. The **CVE Count** value represents findings associated with an individual application.

Counts can differ when:

- The asset or application data comes from different sources.
- An application has multiple CVE findings.
- The source has changed since the application summary was calculated.
- Product or version matching is incomplete.

Open the asset's vulnerability list with this path:

> **Asset context panel > Vulnerabilities**

For vulnerability-specific information, see [Vulnerability enrichment](/xdr/features/modules/reveal_vulnerabilities.md).

## Application details are empty

A dash indicates that the source did not provide a value or that the value could not be matched.

Check the source coverage for:

- Installation details.
- Observation dates.
- User information.
- Hashes.
- CPE and PURL identifiers.

## The application data appears stale

Check:

- The source's last successful synchronization time.
- Whether the source platform contains newer data.
- Whether the asset is still active in the source platform.
- Whether the application was recently installed, removed, or updated.

Application data may not change until the source synchronizes again.

## The Asset Risk Score does not change as expected

The Asset Risk Score is not based on the application count alone. Only open, confirmed vulnerabilities can contribute to the Exposure Score, and the contribution is based on CVSS severity.

The Asset Risk Score also includes recent activity and configured asset criticality. See [Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md) for the calculation rules.

## Information to provide to support

Include the following information when reporting an issue:

- Community identifier.
- Asset identifier and hostname.
- Application name and version, if available.
- Source connector.
- Source synchronization time.
- Asset Risk Score and last updated value, if relevant.
- The panel, tab, or filter where the issue appears.
- A screenshot that does not expose sensitive information.
- The expected result and the result displayed by Reveal.

## Related articles

[Application inventory](/xdr/features/modules/reveal_applications.md): Overview of the Applications tab, its coverage, and its relationship with vulnerability enrichment.

[Review applications](/xdr/features/modules/reveal_applications.md): How to use the Applications tab and inspect application records.

[Vulnerability enrichment](/xdr/features/modules/reveal_vulnerabilities.md): How Reveal collects and displays vulnerability findings.

[Asset risk scoring](/xdr/features/modules/asset_risk_scoring.md): Reference for the Asset Risk Score model and vulnerability contribution.
