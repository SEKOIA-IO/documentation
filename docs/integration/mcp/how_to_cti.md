# Threat intelligence how-to guides

This page shows what the `sekoia-cti` plugin does in Claude Code. It follows the analyst's path: explore what Sekoia knows, write it up as a report, then check whether the threat touches your own telemetry. Each guide gives the permissions it needs, an example prompt, the result and the tools the skill calls.

!!! note "Early Access"
    This feature is currently in Early Access and is only available for Beta testers. Sekoia plans to roll out this functionality to all environments soon.

The guides assume the `sekoia-cti` plugin is installed. See [Install the Sekoia plugins in Claude Code](/integration/mcp/install_claude_code.md). The prompts are examples: write your own, Claude Code picks the matching skill.

| Step | Use case | Skill |
|---|---|---|
| 1 | [Explore Sekoia threat intelligence](#explore-sekoia-threat-intelligence) | `query` |
| 2 | [Produce intelligence reports](#produce-intelligence-reports) | `exposure-assessment`, `threat-horizon-assessment`, `intelligence-delta` |
| 3 | [Check whether you were exposed to a threat](#check-whether-you-were-exposed-to-a-threat) | `query` |
| 3 | [Hunt the behaviours of a FLINT report](#hunt-the-behaviours-of-a-flint-report) | `report-hunt` |

## Explore Sekoia threat intelligence

Ask about actors, malware, indicators, vulnerabilities, sectors, campaigns and reports in plain language. The `query` skill picks the tool sequence and answers in a few sentences with the evidence behind it:

- the object IDs and links to the platform;
- the relationship confidence, read relationship by relationship;
- the dates that matter: activity dates on indicators, and the date of the latest relationship for the freshness of an actor or a malware;
- the Sekoia source of the evidence: Sekoia itself, its C2 Tracker, Honeypot or Malware Watcher, or a third-party report;
- what was searched and not found.

Permissions: `View intelligence`.

### Profile a threat actor

=== "Prompt"

    ```
    What does Sekoia know about TeamTNT? List its aliases, its malware and tools, and the latest reports that cover it.
    ```

=== "Result"

    A short profile: aliases, activity window, goals, the malware and tools linked to the actor with the confidence of each relationship, and the reports by publication date, Sekoia FLINT reports flagged as such.

=== "Tools called"

    1. `search_cti` with `term = "TeamTNT"` returns candidates ranked by relevance; the skill picks the intrusion set.
    2. `get_cti_object_by_id` returns its profile.
    3. `get_cti_object_relationships_by_id` with `target_types = ["malware", "tool"]` returns the linked malware and tools.
    4. `get_cti_object_reports_by_id` returns the reports.

### Enrich an indicator

=== "Prompt"

    ```
    Is 203.0.113.42 known to Sekoia CTI? If it is, which threat is it linked to and since when?
    ```

=== "Result"

    For each value: known or not, its validity period, the threat it indicates and the Sekoia source that produced it. A match whose validity has expired is reported as historical context, not as a current finding. You can pass several values at once.

=== "Tools called"

    1. `search_observables` with `searches = ["203.0.113.42"]` returns the observable and the threats it indicates.
    2. `get_cti_object_by_id` on the indicated threat returns its profile.

### Find the actors targeting a sector

=== "Prompt"

    ```
    Which actors carry out sabotage against the energy sector? Give the confidence of each link and their latest campaign.
    ```

=== "Result"

    The actors related to the sector whose recorded goals include sabotage, with the relationship type and confidence, and the campaigns whose objective is sabotage. Free-text goals that do not match the vocabulary (espionage, lucrative, sabotage, disruption, influence, reconnaissance, pre-positioning) are listed apart rather than folded in. The answer also states that an actor's goal is not proof of what one campaign did.

=== "Tools called"

    1. `search_cti` with `term = "Energy"` returns the sector identity.
    2. `get_cti_object_relationships_by_id` on the sector with `target_types = ["intrusion-set"]` and then `["campaign"]`.

### Profile a malware family after an incident

=== "Prompt"

    ```
    What does Sekoia CTI know about the malware family found in case CA4mN8xQ2rTz? Which actors use it, what infrastructure is linked to it, and which reports cover it?
    ```

=== "Result"

    The malware profile, the actors, infrastructure and tools linked to it, and the reports, most recent first. Reading the case needs `View cases` in addition to `View intelligence`; without it, name the malware family in the prompt.

=== "Tools called"

    1. `get_case` with `case_short_id = "CA4mN8xQ2rTz"` returns the malware named in its alerts.
    2. `search_cti` and `get_cti_object_by_id` return the malware object.
    3. `get_cti_object_relationships_by_id` with `target_types = ["intrusion-set", "infrastructure", "tool"]`.
    4. `get_cti_object_reports_by_id` on the malware.

### Vet a third party's infrastructure

=== "Prompt"

    ```
    Check these domains and IPs for any association with malicious activity in Sekoia CTI: supplier.example, mail.supplier.example, 198.51.100.7.
    ```

=== "Result"

    Each value with its status: not known, known and current, or known with an expired validity. Matches come with the threat involved and the source of the evidence.

=== "Tools called"

    1. `search_observables` with all the values in `searches`.
    2. `get_cti_object_by_id` on each indicated threat.

## Produce intelligence reports

Turn Sekoia evidence into a document you can share. Three report skills each produce a markdown report, an evidence manifest, a self-contained HTML rendering in the Sekoia Intelligence design and a PDF printed from it.

Permissions: `View intelligence`.

| Skill | What it is for |
|---|---|
| `exposure-assessment` | How an actor or a campaign exposes a sector or an organisation, and sector technical RFIs |
| `threat-horizon-assessment` | How a threat theme will evolve over 3 to 12 months, and what to watch |
| `intelligence-delta` | What Sekoia adds that a generic feed does not, demonstrated on one finding |

All three apply the `evidence-protocol` skill. Every claim is typed (fact, calculated result, assessment, exposure model) and traced to a Sekoia object or relationship ID. Clusters are never merged, dates are never borrowed between objects, and the boundaries of the evidence are stated. The evidence manifest ships next to the report so that a reviewer can audit every claim.

=== "Exposure assessment"

    ```
    Produce a Sekoia Intelligence Exposure Assessment on TeamTNT and cloud cryptojacking for cloud-native SaaS providers.
    ```

=== "Sector RFI"

    ```
    Build a telecommunications technical RFI on Salt Typhoon edge-device exploitation and router persistence.
    ```

=== "Threat horizon"

    ```
    How will AI-enabled attacks evolve for the financial sector over the next 12 months?
    ```

=== "Intelligence delta"

    ```
    Prove the intelligence delta of Sekoia for an MSSP on one recent campaign.
    ```

The PDF is printed with a local Chrome or Chromium. Without one, the markdown, the manifest and the HTML are still produced.

## Check whether you were exposed to a threat

Turn "are we exposed to this actor?" into a check on your own community. The `query` skill takes the threat it retrieved and asks your telemetry two questions:

1. **Has Sekoia intelligence already fired here?** Sekoia [IOC detection](/xdr/features/detect/iocdetection.md) raises alerts that carry the ID of the threat behind the matched indicator. The skill counts those alerts for the actor and its infrastructure, malware and tools, by threat and status.
2. **Do its indicators appear in your events?** The skill sweeps the indicators over a bounded window, by host and log source.

Permissions: `View intelligence`, `View query builder data sources`, `Execute query`.

=== "Prompt"

    ```
    Has Sekoia CTI on APT28 or its infrastructure fired in our tenant over the last 30 days? Then check our events for its domains.
    ```

=== "Result"

    Three labelled parts: what Sekoia intelligence records about the threat, which IDs and indicators were checked, and what your community returned over which window, with the alert short IDs and the hosts found.

=== "Queries run"

    ```shell
    alerts
    | where created_at > ago(30d)
    | where threats.id in ['intrusion-set--…', 'infrastructure--…', 'malware--…']
    | aggregate count() by threats.name, status
    | limit 50
    ```

    ```shell
    events
    | where timestamp between (ago(30d) .. now())
    | where related.hosts in ['<domain>'] or related.hash in ['<sha256>']
    | aggregate count() by host.name, sekoiaio.intake.dialect
    | order by count desc
    | limit 50
    ```

!!! tip "Read the results as leads"
    A hit is a lead for the SOC, not an attribution of the activity to the actor. No rows means no alert and no event on the indicators checked in that window, never "not exposed": the indicators are a sample, telemetry coverage is partial and retention is finite.

## Hunt the behaviours of a FLINT report

Indicators are already covered by Sekoia IOC detection. What a FLINT report adds is behaviour: the techniques and procedures it describes. The `report-hunt` skill turns them into a hunt pack for your community:

- the alerts Sekoia intelligence already raised on the report's threats;
- each behaviour of the report, paired with the procedure it describes and the ATT&CK technique;
- which of your log sources can see it, and the gaps when none can;
- the built-in rules that already cover it, and whether they are enabled;
- for the rest, bounded SOL queries written from the report's exact strings, labelled as hunt hypotheses.

Permissions: `View intelligence`, `View query builder data sources`, `Execute query`.

=== "Prompt"

    ```
    Build a hunt pack from FLINT 2026-011 on EvilTokens: which behaviours can our telemetry see, which built-in rules cover them, and the SOL queries for the rest.
    ```

=== "Result"

    A hunt pack with a table of behaviours (source in the report, ATT&CK technique, telemetry here, built-in rule, query, result), the queries, the gaps and the boundaries of the exercise. The queries run only when you ask, a few at a time.

=== "Tools called"

    1. `search_cti` and `get_cti_object_by_id` on the report and its linked techniques and malware.
    2. `run_sol_query` on `alerts` for the threats already detected.
    3. `run_sol_query` on `events` for the log sources present.
    4. `run_sol_query` on the rules catalog for the built-in rules that cover each behaviour.

The hunt pack carries the strictest TLP marking of the material it uses. A hit is a lead for the SOC, and an empty result does not mean you are not affected.

## Related articles

* [Sekoia MCP Server](/integration/mcp/overview.md): Use cases, how the server works, access control and limits.
* [SOC how-to guides](/integration/mcp/how_to_soc.md): Alerts, cases and SOL queries in plain language.
* [Plugins and skills](/integration/mcp/plugins_skills.md): Every skill, what it is for and the permissions it needs.
* [MCP tools](/integration/mcp/tools_reference.md): Parameters, permissions and examples for every tool.
* [Getting started with the Sekoia MCP Server](/integration/mcp/getting_started.md): Investigate an alert end to end from Claude Code.
* [IOC detection](/xdr/features/detect/iocdetection.md): How Sekoia intelligence raises alerts on your events.
