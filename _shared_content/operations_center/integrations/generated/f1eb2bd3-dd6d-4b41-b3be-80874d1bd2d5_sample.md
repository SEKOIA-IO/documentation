
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "test_audit1"

    ```
	New audit log entry reported by the Guardicore Security Suite;;Username: admin;IP Address: 192.0.2.1;;Title: Run Data Exporter Integration Test Connections;;Description: None
    ```



=== "test_audit2"

    ```
	New Audit log entry reported by the Guardicore Security Suite;;Username: admin;IP Address: 192.0.2.1;; Title: Adding new Syslog integration configuration; Description: Created label group Role: App (id: 7de50df5-f530-4752-9450-553cce25ebd2)
    ```



=== "test_audit3"

    ```
	New audit log entry reported by the Guardicore Security Suite;;Username: None;IP Address: 192.0.2.1;;Title: Access to unknown resource;;Description: Access to resource: /api/login with status code: 404
    ```



=== "test_audit4"

    ```
	New audit log entry reported by the Guardicore Security Suite;;Username: jdoe;IP Address: 192.0.2.1;;Title: Authentication success;;Description: User jdoe authenticated successfully
    ```



=== "test_connection"

    ```
	New test connection entry reported by the Guardicore Security Suite;;Username: None;IP Address: 192.0.2.10;;Title: Run Data Exporter Integration Test Connections;;Description: Test successful
    ```



=== "test_incident"

    ```
	New low severity security incident reported by the Guardicore Security Suite;;ID: 00000000-0000-0000-0000-000000000000;URL: https://lab.example.com/overview/incidents/00000000-0000-0000-0000-000000000000;;Description: A request was made to an IP address with a bad reputation;;Severity: low;Start Time: 2026-04-07T08:47Z;End Time: 2026-04-07T08:47Z;;Rule ID: No rule;Affected Assets:;192.0.2.1 (source);destination.test.org (destination);;Destination labels: Role: FE;Terraform: True;Worksite: Default;App: CRM;Environment: Development;os_name: Ubuntu 24.04.4 LTS;os_type: Linux;;Tags: Known Phishing, Known Malware;;Summary: ;1. IP address 198.51.100.50:22, communicating with asset destination.test.org (192.0.2.2), was identified as Known Malware and Known Phishing by Guardicore Reputation Service.;Direction: Inbound;
    ```



=== "test_network_failure"

    ```
	New network connection reported by the Guardicore Security Suite;ID: eac74b0a;Connection type: FAILED; Action: Blocked;Count: 1;Time: 2024-04-03T02:05:40.611Z;Source IP: 192.0.2.1;Source process name: Unknown Client;Source application name: Unknown Client;Destination IP: 192.0.2.2;Destination port: 22;Destination asset name: hostname.local;Destination user name: root;Destination process name: sshd;Destination process path: /usr/sbin/sshd;Destination process name: sshd;Protocol: TCP;Connection verdict: blocked_by_destination;Policy rule: 11234vs-4573-7432-7543-2342gsdf436; Incidents: 11124vs-2342-1231-6543-2342gsdf424
    ```



=== "test_network_success"

    ```
	New network connection reported by the Guardicore Security Suite;ID: eac74b0a;Connection type: SUCCESSFUL; Action: Allowed;Count: 1;Time: 2024-04-03T02:05:40.611Z;Source IP: 192.0.2.5;Source process name: Unknown Client;Source application name: Unknown Client;Destination IP: 192.0.2.6;Destination port: 67;Destination asset name: hostname.local;Destination user name: root;Destination process name: sshd;Destination process path: /usr/sbin/dnsmasq;Destination process name: sshd;Protocol: UDP;Connection verdict: allowed;Policy rule: default; Incidents: 11124vs-2342-1231-6543-2342gsdf424
    ```



