# Best Practices for Using Sekoia SOC Platform (Defend plan)

In the current cybersecurity landscape, organizations face significant challenges, including a scarcity of skilled professionals and the complexity of traditional security solutions. At Sekoia, we strive to ensure our customers get the most out of our product by following best practices. These practices help maximize the effectiveness of our solutions while maintaining optimal security and operational efficiency. Below, we outline the key best practices and configuration guidelines that we recommend for all our users.

### Rules Configuration

Our extensive catalog of over 900 rules, each [associated with a TTP from the MITRE ATT&CK framework](https://docs.sekoia.io/xdr/features/detect/built_in_detection_rules/), is categorized by four levels of effort. This enables targeted and effective defense against threats. The normalization of events via [intake formats](https://github.com/SEKOIA-IO/intake-formats/blob/main/doc/structured_event.md) and the use of [ECS taxonomy](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) allows for technology-agnostic integration, facilitating the production of detection rules based on the [SIGMA models](https://docs.sekoia.io/xdr/features/detect/sigma/), our specific [anomaly detection engine](https://docs.sekoia.io/xdr/features/detect/anomaly/) and even the [IOC Detection](https://docs.sekoia.io/xdr/features/detect/iocdetection/) & [Collections](https://docs.sekoia.io/xdr/features/detect/ioccollections/).

**Recommendations:**

- **Activate all [effort level](https://docs.sekoia.io/xdr/features/detect/rules_catalog/#effort-level) 1 and 2 rules** during the initial setup of your community.

- **Configure the Rules Settings** to [enable new rules](https://docs.sekoia.io/xdr/features/detect/rules_catalog/#automatically) up to the Intermediate level.

- **Fine-tune detection rules** after each false positive alert through the [available options](https://docs.sekoia.io/xdr/features/detect/rules_catalog/#limiting-the-scope-of-a-rule), primarily using alert filters.

- **Activate a new wave of higher effort level rules** after the initial RUN period, representing:

    - 20% of level 3 / "Advanced" rules,
    - 10% of level 4 / "Master" rules.

- **Aim for continuous improvement**, reaching an average of:

    -  10% tuning for level 3 rules with at least 1 alert-filter,
    -  20% tuning for level 4 rules with at least 1 alert-filter.

### Intakes Configuration

To ensure comprehensive and effective coverage, it is crucial to configure your intakes correctly. Our recommendations are to activate and configure log collection for at least:

- **1 company wide Endpoint Based Intake** (e.g., EDR, Windows, Sekoia.io for Endpoint). This allows for threat detection directly on workstations and servers, covering a wide range of threats such as malware and suspicious user behaviors. This means we recommend to install the Sekoia.io for Endpoint agent only when no active or passive agent is already installed on the host to avoid side effects on log collection and alerting.
- **1 company wide Security Network Based Intake** (e.g., Firewall, NDR, WAF) **with security options enabled**. These intakes are essential for monitoring network attacks, intrusion attempts, and malicious activities from outside.
- **2 company wide Network Based Intake** (e.g., Loadbalancer/Reverse-Proxy, Proxy, DNS). They help monitor internal network traffic and detect anomalies such as lateral movements by attackers and suspicious communications.
- **1 company wide Email Security Based Intake** (e.g., Office, ProofPoint, Vade) **with security options enabled**. This helps identify phishing attacks, malware transmitted via email, and other email-related threats.
- **1 Identity and Access Management Based Intake** for **on-premise** environments (e.g., Active Directory, Okta, Wallix) **and 1 for cloud** environments if applicable (e.g., Azure Entra ID, Cloudflare Access Requests, Google Workspace). This helps detect suspicious activities related to user access, such as unauthorized login attempts and privilege changes, and ensures security oversight across both on-premise and cloud environments.
- **Activity Logs**: Ensure that [Sekoia.io activity logs](https://docs.sekoia.io/integration/integrations/application/sekoiaio_activity_logs/) are activated. This allows monitoring actions and changes within the Sekoia.io platform itself, ensuring complete transparency and traceability.
- **No intake should have zero events received** in the past 7 days. An intake without events can indicate a configuration or data collection issue, compromising threat detection capability. Ensure that notifications are configured to alert in the case of [an event drop for an intake](https://docs.sekoia.io/getting_started/notifications-Examples/#intakes).

- **Use the [Sekoia.io Forwarder](https://docs.sekoia.io/integration/ingestion_methods/syslog/sekoiaio_forwarder/)** each time you need to forward On Premise events via syslog protocol to Sekoia.io SOC Platform to ease discriminate logs before adding them the relevant Intake Key. It also is the only log forwarder that our Support team will be able to provide you with assistance.


### Events Quality

The quality of events is crucial for accurate and effective detection. Here are the best practices to follow:

- **Ensure less than 3% of events per intake are warnings**. Warnings can indicate potential issues with data collection or interpretation, and a high percentage can lead to miss detections.
- **Ensure less than 1% of events per intake are invalid**. Invalid events cannot be used for detection and may indicate formatting or data integrity issues.

### Alerts

Our product is designed to focus on high-priority threats, enabling expert resources to conduct a manageable number of quality investigations each day. By creating alert filters, you can ensure that alerts are raised for the right reasons, enhancing the efficiency and effectiveness of your security operations.

- **Monitor the average number of Alerts per Intake** to identify intakes generating too many or too few alerts.
- **Limit the number of Daily New Alerts** at a manageable level for your team (by experience, around 6 to 8 per day per analyst, or 60 per day) and prioritise the [tuning of a rule](https://docs.sekoia.io/xdr/features/investigate/alerts/#create-an-alert-filter) over automating its status change if no defensive action is to be taken.
- **Track the Weekly and Monthly volume of New Alerts** to evaluate the evolution of threats and the performance of detection rules.
- **Assess the number of Daily New Cases** to understand workload and the effectiveness of response processes. In general, the number of case(s) per day does not exceed 1, as it is cconsidered as a very important incident.
- **Ensure no sleeping alert is older than 1 week** without status "Closed" or "Rejected".

![alert_workflow](/assets/operation_center/alerts/alert_workflow.png){: style="max-width:100%"}

### Playbooks

Playbooks complement operational optimization by automating various types of manual tasks mastered by the analyst team. They allow, for example, to automate certain steps in the alert analysis workflow, enrich certain types of alerts with specific external sources (like VirusTotal), or retrieve additional contextual information on an endpoint when an active agent is installed before deciding to quarantine it or take other actions.

**Recommendations:**

- **Keep the number of playbook executions per day low**: Aim for less than 60 executions per playbook per day, aligning with the number of raised alerts. Each playbook should have a specific objective to meet a particular need.
- **Design playbooks with simplicity in mind**: On average, each playbook should be composed of less than 15 modules, including:
    - **1 [Trigger](https://docs.sekoia.io/xdr/features/automate/triggers/)** such as the “Manual trigger” or “Alert created” trigger **with a filter condition** to start the playbook only for relevant cases.
    - **Some [Operator](https://docs.sekoia.io/xdr/features/automate/operators/) modules** like "[Condition](https://docs.sekoia.io/xdr/features/automate/operators/#condition)" and "[Foreach](https://docs.sekoia.io/xdr/features/automate/operators/#foreach)" to halt the playbook execution if new information gathered during the process indicates that the playbook is unnecessary in the current context.
    - **A majority of [Action](https://docs.sekoia.io/xdr/features/automate/actions/) modules** making it easily understandable for new team members and maintainable over time. To give you more details on the top 10 most used playbook Actions, here is a list:

        1. [Read JSON File](https://docs.sekoia.io/xdr/features/automate/library/fileutils/#read-json-file)
        2. [Comment Alert](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#comment-alert)
        3. [Get Alert](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#get-alert)
        4. [Request URL](https://docs.sekoia.io/xdr/features/automate/library/http/#request-url)
        5. [Update Alert Status](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#update-alert-status)
        6. [Get Events](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#get-events)
        7. [VirusTotal Scan URL](https://docs.sekoia.io/xdr/features/automate/library/virustotal/#scan-url)
        8. [Get Event Field Common Values](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#get-event-field-common-values)
        9. [Edit Alert](https://docs.sekoia.io/xdr/features/automate/library/sekoia-io/#edit-alert)
        10. [VirusTotal Scan Hash](https://docs.sekoia.io/xdr/features/automate/library/virustotal/#scan-hash)

For instance, the following [playbook template](https://docs.sekoia.io/xdr/features/automate/build-playbooks/#templates) composed of 9 modules (1 Trigger, 1 Operator, 7 Actions) answers the need of adding a domain in a blocklist (IOC Collection).

![playbook_example](/assets/getting_started/playbook_example.png){: style="max-width:100%"}

- **Ensure the duration of each Action** within playbooks is less than 10 seconds to reduce the chance of a timeout with most third-party tools you interact with.
- **Track the overall [duration of playbook executions](https://docs.sekoia.io/xdr/features/automate/navigate-playbooks/#playbook-runs)** for each playbook to complete its execution in less than 1 minute.
- **Ensure no playbook is having an issue** that is visible with the status "Trigger crashed" and "Configuration issues".
- **Keep a low number of "Ready to start" playbooks**, for instance less than 2, to avoid activation issue after a long period of configuration due to confict with recent evolutions of your community.

By adhering to these best practices, you can maximize the efficiency of Sekoia’s solutions, ensuring optimal security and operational performance for your organization.
