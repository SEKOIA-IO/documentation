# Update a custom integration

A custom integration runs code hosted in your own Git repository, and exposes connectors that collect events and triggers that start playbooks. This article explains how to bring a new version of that code into Sekoia, what the platform restarts on its own, and what you have to do yourself.

Two actions on the integration page bring a change into the platform:

- **Check for updates** looks at the integration's Git repository and lists the new commits available since the last update. This action only checks, it changes nothing.
- **Update** pulls the latest code, validates it, rebuilds the integration's Docker image with its new version, and applies the change to the integration's connectors and triggers.

Running **Update** is enough to make the new code available. What you do next depends on whether you update a connector or a trigger, and on whether it was already running.

## Before you update

!!! warning "Bump the version before pushing"
    If you push a code change without changing the version, the platform has no way to tell that anything changed, and does not know to restart what is currently running. Update the `version` field in both `manifest.json` and `CHANGELOG.md` before pushing. See [Deploy your module](/integration/develop_integration/automation/create_a_module.md#deploy-your-module).

Prepare the update:

- Push your code change with a new version to the repository connected to the integration.
- Read your own changelog. If the update changes required configuration fields, authentication, or the shape of the data the integration produces, plan to check the configuration after updating.
- Note which connector configurations and which playbooks use this integration, and whether they are currently running or activated, so you know what to check afterwards.

## Check for updates

To see what a new update would bring:

1. Navigate to **Integrations** and open your custom integration.
2. Click **Check for updates**.
3. Review the list of new commits available since the last update.

This step is read-only. Nothing is applied to your connectors or triggers until you run **Update**.

## Update the integration

To apply the new code:

1. Click **Update** on the integration page.
2. Wait for the update to complete.

The platform pulls the latest code, validates it, rebuilds the integration's Docker image with its new version, and applies the change to the integration's connectors and triggers.

## Update a connector

Run **Check for updates**, then **Update**, on the integration.

- Every connector configuration of this integration that is currently running is restarted automatically with the new version. You have nothing else to do for those.
- Every connector configuration that is currently stopped keeps the update but is not started. Start it manually from the connector configuration once you are ready to use the new version.

To verify the update applied, check that the connector configuration's status and last restart reflect a recent restart, and that data flows again as expected.

!!! tip "A running connector did not restart"
    Do not wait and do not run the update again. Click **Stop**, then **Start** on the connector configuration. A manual restart always applies the integration's current version, whatever prevented the automatic restart.

## Update a trigger

Run **Check for updates**, then **Update**, on the integration, exactly as for a connector.

A trigger configuration is tied to a playbook. It runs while its playbook is activated, and stops when the playbook is deactivated.

- Every trigger configuration currently running, meaning its playbook is activated, is restarted automatically with the new version, the same way connectors are.
- A trigger configuration whose playbook is deactivated is not running, so nothing is restarted. It uses the new version the next time you activate the playbook.

To verify the update applied, send a test event or wait for a real one, then confirm the playbook runs with the expected new behavior.

!!! tip "A running trigger did not pick up the update"
    Deactivate the playbook, then activate it again. This is the equivalent of **Stop** and **Start** for a connector, and always applies the integration's current version.

## Restart instead of deleting and recreating

!!! warning "Deleting a configuration is never required to apply an update"
    A new configuration gets a new identifier and a new authentication token. For a connector, anything that references the configuration externally, in particular the intake it feeds, does not follow the new one. For a trigger, you have to re-attach the playbook to the new configuration manually.

A restart keeps everything in place and only replaces the running instance with the new version.

| | Restart | Delete and recreate |
| --- | --- | --- |
| **How** | **Stop** then **Start** for a connector, deactivate then activate the playbook for a trigger | Delete the configuration, then create a new one |
| **Identifier** | Kept | New |
| **Authentication token** | Kept | New |
| **Intake link (connector)** | Kept | Lost, not reassigned automatically |
| **Playbook attachment (trigger)** | Kept | The playbook must be re-attached manually |

Always try a restart before you consider recreating anything.

## Troubleshooting

Nothing seems to have changed after you ran **Update**:

- **Check that the version was bumped in your latest push.** If the version did not change, the platform detects nothing to restart. Bump the version and update again, or restart the configuration manually to apply the current version now.
- **Check that the configuration was running when you ran the update.** If the connector was stopped or the playbook deactivated, no restart is expected. Start the connector, or activate the playbook, now that the update is saved.
- **Read the connector or trigger logs.** Look for authentication errors and for parsing or schema errors, especially if the update changed required configuration fields or the data the integration produces.
- **Roll back a broken version.** Revert your change in the Git repository and run the update again, then investigate.

Consider deleting and recreating a configuration only if, after all of the above, it is genuinely broken beyond a restart. It is never a way to force a version change.

## Related articles

* [Integrations catalog](/xdr/features/collect/integrations_hub.md): Overview of the catalog and how to create and import a custom integration.
* [Create a module](/integration/develop_integration/automation/create_a_module.md): How to develop a module, version it, and push it to GitHub or GitLab.
* [Module](/integration/develop_integration/automation/module.md): Reference for the module structure and its manifest, including the `version` field.
* [Intakes](/xdr/features/collect/intakes.md): How pull intakes and their connectors are started, stopped and monitored.
* [Navigate through playbooks](/xdr/features/automate/navigate-playbooks.md): How to activate and deactivate a playbook and read its status.
