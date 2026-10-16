# Scope auto-analysis with filters

By default, when auto-analysis is enabled, the Elevate agent analyzes every new alert. Filters limit auto-analysis to the alerts that matter to you, by detection rule, rule effort level, alert severity or alert urgency, so your runs are not spent on alerts your playbooks already handle.

## Prerequisites

- Elevate is activated on your workspace. See [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md).
- You have administrator-level access to the workspace.

## How filters work

Every filter is optional. When no filter is set, the agent analyzes all new alerts. When you add one or more filters, the agent analyzes an alert only if it matches **all** of them.

Filters are evaluated when an alert is raised, before any run is consumed. Alerts that do not match keep an empty verdict. To have Elevate analyze one of them anyway, assign the alert to Roy. See [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md).

!!! note "Workspace defaults and community settings"
    Filters set on the workspace apply to every community, unless a community uses custom settings. A community with custom settings has its own filters. See [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md).

## Available filters

| Filter | Values | Effect |
|---|---|---|
| **Rule effort level** | **Elementary**, **Intermediate**, **Advanced**, **Master** (one or more) | Analyzes only alerts raised by rules of the selected effort levels. |
| **Alert severity** | **more than** or **less than**, and a score | Analyzes only alerts whose severity is at or above (**more than**) or at or below (**less than**) the score. |
| **Alert urgency** | **more than** or **less than**, and a score from 1 to 100 | Analyzes only alerts whose urgency is at or above (**more than**) or at or below (**less than**) the score. See [Alert urgency](/xdr/features/investigate/alerts.md#alert-urgency). |
| **Include rules** | A list of detection rules | Analyzes only alerts raised by the selected rules. |
| **Exclude rules** | A list of detection rules | Analyzes alerts from every rule except the selected ones, including rules published later. |

!!! tip "Choose between Include rules and Exclude rules"
    Use **Include rules** when Elevate should focus on a short list of detections. Use **Exclude rules** when Elevate should cover everything except a few rules, for example rules whose alerts a playbook already closes.

## Add filters

1. Navigate to **Settings > AI agents**.
2. Select the workspace, or the community you want to configure.
3. Select the **Alert/Case investigation** agent.
4. Select the **Settings** tab.
5. Click **Filters**.
6. Select each filter you want to add.

Each selected filter appears as a row below the **Filters** button.

![Filters menu listing Rule effort level, Alert severity, Alert urgency, Include rules and Exclude rules](/assets/elevate/auto-analyze-filters-menu.png){: style="max-width:100%"}

!!! note "Changes are saved automatically"
    There is no save button. Each filter applies as soon as you set it.

### Filter by rule effort level

1. In the **Rule effort level** row, click **Select an option...**.
2. Select each effort level you want the agent to analyze.

The row lists the selected levels, for example **Elementary, Intermediate**.

### Filter by alert severity or urgency

1. In the **Alert severity** or **Alert urgency** row, select **more than** or **less than**.
2. Enter the score.

![Alert severity row with the more than and less than options](/assets/elevate/auto-analyze-filters-threshold.png){: style="max-width:100%"}

!!! warning "Less than excludes your most urgent alerts"
    Selecting **less than** on **Alert urgency** stops auto-analysis of every alert above the score, including your highest-risk alerts. Use **more than** to keep Elevate on the alerts that matter most.

### Include or exclude detection rules

**Include rules** and **Exclude rules** open the same **Select rules** modal. The row you start from decides whether the selected rules are included or excluded.

1. In the **Include rules** or **Exclude rules** row, click **Select rules**.
2. In **Search for rules...**, enter part of a rule name.
3. Select each rule.
4. Click **Save**.

![Select rules modal with a search field and a paginated list of detection rules](/assets/elevate/auto-analyze-filters-select-rules.png){: style="max-width:100%"}

The settings card lists every filter in force, one per row.

![Auto-analyze alerts settings with five filters configured](/assets/elevate/auto-analyze-filters-configured.png){: style="max-width:100%"}

## Remove a filter

To remove a filter, use either of these options:

- Click **Filters**, then clear the checkbox of the filter.
- On the row of the filter you want to remove, such as **Alert urgency**, click the delete icon.

Once every filter is removed, the agent analyzes all new alerts again.

??? example "Analyze urgent alerts but skip rules handled by playbooks"
    A SOC wants Elevate on high-risk alerts only, away from its noisiest detections and away from five rules a playbook already closes. The administrator sets these filters:

    | Filter | Setting |
    |---|---|
    | **Alert urgency** | **more than** 60 |
    | **Rule effort level** | **Elementary**, **Intermediate**, **Advanced** |
    | **Exclude rules** | The five rules handled by the playbook |

    Elevate analyzes an alert only when its urgency is 60 or above, its rule is not a **Master** effort rule and its rule is not one of the five excluded. Rules published later are analyzed as long as they match the other filters.

## Result

The agent automatically analyzes only the alerts that match every filter you set. Other alerts are not analyzed and consume no run. To have Elevate analyze any other alert, assign it to Roy.

## Related articles

- [Activate Elevate on a workspace](/xdr/features/modules/elevate_activate.md): How to enable the Elevate agent on your workspace.
- [Override Elevate settings for a community](/xdr/features/modules/elevate_community_override.md): How to give a community its own Elevate settings, including its own filters.
- [Trigger a manual Elevate analysis](/xdr/features/modules/elevate_manual_analysis.md): How to have Elevate analyze an alert that your filters exclude by assigning it to Roy.
- [Manage your Elevate runs](/xdr/features/modules/elevate_quota.md): How to monitor and optimize your monthly run pack.
