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
                // "FRA2",
                // "MCO1",
                // "UAE1",
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
                "https://app.sekoia.io/api/v2/asset-management/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/edl-gateway/openapi.json",
                "https://app.sekoia.io/api/v2/inthreat/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/events/openapi.json",
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
                        "counters", // TODO => +Avatars
                    ],
                },
                {
                    name: "Configuration",
                    tags: [
                        "Entities",
                        "Enrichers",
                        "Callbacks",
                        "Services",
                        "Archives",
                        "Views", // TODO => + Archives
                    ]
                },
                {
                    name: "Intelligence",
                    tags: [
                        "Objects",
                        "CTI Objects", // TODO fix telemetry => Objects
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
                        "Graphs",
                        "Relationships",
                        "Reports",
                        "Support",
                        "Sources",
                        "Vulnerabilities",
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
                        "Intake Optimization Rules",
                    ],
                },
                {
                    name: "Detection",
                    tags: [
                        "Rules",
                            "compilation-reports", // TODO sicconf => Rules
                            "rules-catalog-multi-tenant", // TODO sicconf => Rules
                            "rules-catalog", // TODO sicconf => Rules
                        "datasources",
                        "generation-modes", // TODO sicconf => Generation modes
                        "Alert filters",
                        "IOC Collections",
                        "Alerts",
                            "Alert", // TODO sicalert => Detection+Alerts
                            "Alert Entities", // TODO sicalert => Detection+Alerts
                            "Alert Rules", // TODO sicalert => Detection+Alerts
                            "Alert Sources and Targets", // TODO sicalert => Detection+Alerts
                            "Stats", // TODO sicalert => Detection+Alerts+Alert stats
                            "Alert Status", // TODO sicalert => Detection+Alerts
                            "Alert Type", // TODO sicalert => Detection+Alerts
                        "Countermeasures",
                        "Cyber Kill Chain",
                    ],
                },
                {
                    name: "Investigation",
                    tags: [
                        "Cases",
                            "Case", // TODO => Cases
                            "Comments", // TODO => + Cases
                        "Notebooks",
                        "Events",
                        "Tasks",
                    ],
                },
                {
                    name: "Automations",
                    tags: [
                        "Playbooks",
                        "Playbook actions telemetry",
                        "modules",
                        "Playbook runs",
                            "Playbooks runs", // TODO: Fix symphony => Playbook runs
                        "Node runs",
                        "Action Runs",
                        "Actions",
                        "Connector Configurations",
                        "Connectors",
                        "Module Configurations",
                        "Modules",
                        "Runs",
                        "Trigger Configurations",
                        "Triggers",
                        "SSH Keys",
                    ],
                },
                {
                    name:"Reporting",
                    tags: [
                        "Intelligence statistics",
                        "Automation statistics",
                        "Statistics",
                        "dashboards",
                        "Roy tokens use telemetry",
                        "Alert filters telemetry",
                    ]
                }
            ]
        })
    };
</script>
