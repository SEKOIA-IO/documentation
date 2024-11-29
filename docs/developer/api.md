---
template: overrides/openapi.html
---

# Sekoia.io API documentation

{!docs/developer/quickstart.md!}


<script>
    window.onload = ()=> {
        OpenAPIViewer.init({
            title:"Sekoia.io API Documentation",
            regions: [
                "FRA1",
                "FRA2",
                "MCO1",
                "UAE1",
            ],
            urls: [
                "https://app.sekoia.io/api/v1/dashboard/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/telemetry/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/notebooks/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/sic/conf/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/ingest/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/sic/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/symphony/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/enricher/swagger.json?context=tip",
                "https://app.sekoia.io/api/v2/asset-management/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/edl-gateway/openapi.json",
                "https://app.sekoia.io/api/v2/inthreat/swagger.json?context=public",
            ],
            menu:[
                {
                    name: "User",
                    tags: [
                        "User Authentication",
                        "me",
                        "mfa", // TODO: split 'mfa' into administration and self
                        "permissions",
                    ],
                },
                {
                    name: "Workspace",
                    tags: [
                        "customers", // TODO deprecated, get rid of it
                        "communities",
                        "api-keys",
                        "licenses",
                        "invitations",
                        "plans",
                        "sub-communities",
                        "avatars",
                        "users", // TODO set this tag on all user administration stuff
                        "roles",
                    ],
                },
                {
                    name: "Intelligence",
                    tags: [
                        "Observables",
                        "CTI Objects",
                        "Bundles",
                        "Collections",
                        "Exports",
                        "Outgoing Feeds",
                        "Graphs",
                        "MISP",
                        "Objects",
                        "Observable relationships",
                        "Indicators",
                        "Images",
                        "support",
                        "Labels",
                        "Kill Chains",
                    ],
                },
                {
                    name: "Collect",
                    tags: [
                        "Intakes",
                        "Assets",
                        "Atoms",
                        "Intakes by status",
                        "Intakes errors and warnings",
                        "Intakes lag and processing lag",
                        "formats",
                        "IOC Collections",
                    ],
                },

                {
                    name: "Detection rules",
                    tags: [
                        "Rules",
                        "datasources",
                        "generation-modes",
                        "rules-catalog",
                        "alert-filter", // TODO: to create, this tag doesn't exist yet
                    ],
                },
                {
                    name: "Alerts",
                    tags: [
                        "Alert",
                        "Alert Entities",
                        "Alert Rules",
                        "Alert Sources and Targets",
                        "Countermeasures",
                        "Cyber Kill Chain",
                        "Stats",
                        "Alert Status",
                        "Alert Type",
                    ],
                },
                {
                    name: "Cases",
                    tags: [
                        "Case",
                        "Comments",
                        "Statistics",
                        "Enrichers",
                        "Callbacks",
                        "Services",
                        "Tasks",
                    ],
                },
                {
                    name: "Playbooks",
                    tags: [
                        "Playbook actions telemetry",
                        "modules",
                        "Action Runs",
                        "Actions",
                        "Changes",
                        "Connector Configurations",
                        "Connectors",
                        "Module Configurations",
                        "Modules",
                        "Node Runs",
                        "Playbooks Runs",
                        "Playbooks",
                        "Trigger Configurations",
                        "Triggers",
                    ],
                },
                {
                    name: "AI assistant", // TODO: Make that private
                    tags: [
                        "Roy tokens use telemetry",
                    ],
                },
            ]
        })
    };
</script>
