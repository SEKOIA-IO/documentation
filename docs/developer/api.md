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
                "../../javascript/schema.json",
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
                        "Objects",
                        "Indicators",
                        "Observables",
                        "Observable relationships",
                        "Exports",
                        "Kill Chains",
                        "Outgoing Feeds",
                        "Collections",
                        "MISP",
                        "TAXII",
                        "Bundles",
                        "Images",
                        "Labels",
                    ],
                },
                {
                    name: "Configuration",
                    tags: [
                        "Intakes",
                        "Assets",
                        "Intakes by status",
                        "Intakes errors and warnings",
                        "Intakes lag and processing lag",
                        "formats",
                    ],
                },
                {
                    name: "Detection",
                    tags: [
                        "Rules",
                        "datasources",
                        "generation-modes",
                        "rules-catalog",
                        "alert-filter", // TODO: to create, this tag doesn't exist yet
                        "IOC Collections",
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
                        "Enrichers",
                        "Callbacks",
                        "Services",
                        "Tasks",
                    ],
                },
                {
                    name: "Automations",
                    tags: [
                        "Playbooks",
                        "Playbook actions telemetry",
                        "modules",
                        "Action Runs",
                        "Actions",
                        "Connector Configurations",
                        "Connectors",
                        "Module Configurations",
                        "Modules",
                        "Runs",
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
                {
                    name:"Reporting",
                    tags: [
                        "Intelligence statistics",
                        "Automation statistics",
                        "Statistics",
                    ]
                }
            ]
        })
    };
</script>
