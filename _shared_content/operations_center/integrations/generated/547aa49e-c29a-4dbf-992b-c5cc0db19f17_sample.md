
### Raw Events Samples { data-search-exclude }

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_alert_agent_error_rate"

    ```
	More than 5% of support-agent.example.com spans ended in error over the last 15 minutes.
    ```



=== "test_alert_high_severity_agent_only_without_base_url"

    ```
	research-agent.example.com used more than its 150k-token budget over the last 15 minutes.
    ```



=== "test_alert_pii_in_tool_response"

    ```
	A response from get_customer_kyc (agent: support-agent.example.com) contained sensitive data flagged as PERSON. This may mean personally identifiable or otherwise sensitive information was exposed through a tool's output -- review the trace to confirm whether this was expected.
    ```



=== "test_alert_seed_demo_guardrail_without_base_url"

    ```
	The injection_scan guardrail flagged the input to read_calendar as a prompt-injection attempt and blocked the call.
    ```



=== "test_alert_url_in_tool_response"

    ```
	A call to get_recent_transactions by support-agent.example.com returned a link to evil.example.com. This may indicate the agent is exposing, following, or being redirected to an unexpected external destination -- worth checking whether this domain is expected for this tool.
    ```



=== "test_alert_url_in_tool_response_no_data"

    ```
	URL in tool response received no data since 2026-10-01 09:45:03
    ```



=== "test_alert_url_in_tool_response_no_data_resolved"

    ```
	URL in tool response receives data again
    ```



=== "test_alert_url_in_tool_response_resolved"

    ```
	A call to get_recent_transactions by support-agent.example.com returned a link to evil.example.com. This may indicate the agent is exposing, following, or being redirected to an unexpected external destination -- worth checking whether this domain is expected for this tool.
    ```



=== "test_alert_url_in_tool_response_warning_without_base_url"

    ```
	A call to fetch_invoice by billing-agent.example.com returned a link to cdn.example.net. This may indicate the agent is exposing, following, or being redirected to an unexpected external destination -- worth checking whether this domain is expected for this tool.
    ```



=== "test_audit_dashboard_created_ipv6_client"

    ```
	alice@example.com (11111111-1111-1111-1111-111111111111) created dashboard (0199e3e1-6b2d-7f35-a9c4-8e1b0d7f2a63)
    ```



=== "test_audit_failed_sign_in"

    ```
	alice@example.com failed to create session
    ```



=== "test_audit_rule_updated"

    ```
	alice@example.com (11111111-1111-1111-1111-111111111111) updated rule (0199e3c4-5b7a-7d21-9f4e-2a6c8b1d3e57)
    ```



=== "test_audit_rule_updated_without_client"

    ```
	alice@example.com (11111111-1111-1111-1111-111111111111) updated rule (0199e3c9-12f0-7a44-b3d8-6e0f9c27a1b4)
    ```



=== "test_audit_system_actor"

    ```
	updated rule (0199e3d2-8c41-7e09-a5b6-3f7d1e48c920)
    ```



=== "test_audit_trace_export"

    ```
	alice@example.com (11111111-1111-1111-1111-111111111111) read traces
    ```



