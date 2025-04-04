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
                "USA1"
            ],
            urls: [
                "https://app.sekoia.io/api/v1/dashboard/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/telemetry/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/events/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/notebooks/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/sic/conf/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/ingest/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/sic/swagger.json?context=public",
                "https://app.sekoia.io/api/v1/symphony/swagger.json?context=public",
                "https://app.sekoia.io/api/v2/asset-management/openapi.json?context=public",
                "https://app.sekoia.io/api/v1/edl-gateway/openapi.json",
                "https://app.sekoia.io/api/v2/inthreat/swagger.json?context=public",
            ],
            tag_mappings:{
                "mfa": "MFA",
                "me": "User profile",
                "automations": "Automation",
                "Observables relationships": "Observable relationships",
                "Object relationships": "Relationships"
            },
            intro: [
                "Quickstart",
                "Authentication",
                "Organization",
                "Code examples",
            ],
            menu:[
                {
                    name: "User",
                    tags: [
                        "User Authentication",
                        "User profile",
                        "MFA",
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
                        "users", // TODO set this tag on all user administration endpoints
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
                        "Intakes",
                        "Assets",
                        "Atoms",
                        "Intakes by status",
                        "Intakes errors and warnings",
                        "Intakes lag and processing lag",
                        "formats",
                        "Intake Optimization Rules",
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
                    name: "Detection",
                    tags: [
                        "Rules",
                            "compilation-reports", // TODO sicconf => Rules
                            "rules-catalog-multi-tenant", // TODO sicconf => Rules
                            "rules-catalog", // TODO sicconf => Rules
                        "Alerts",
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
                        "UEBA",
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
                    name: "Automation",
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
                        "dashboards",
                        "Intelligence",
                            "Intelligence statistics", // => Intelligence
                        "Events",
                        "Rules",
                        "Alert filters",
                        "Assets",
                        "Playbooks",
                            "Automation statistics", // => Playbooks
                        "AI assistant",
                        "Statistics", // ?
                    ]
                }
            ]
        })
    };
</script>
