# checkpoint\_harmony\_email\_collaboration

uuid: 71bd28dc-163d-4262-9d50-84ec4a9cef65 name: Checkpoint Harmony Email and Collaboration type: intake

### Overview

Check Point Harmony Email & Collaboration Suite Security delivers unified protection for email, cloud storage and collaboration apps (Office 365, Google Workspace, Teams, Slack). Advanced anti-phishing, zero-day malware sandboxing, URL defense and data loss prevention stop BEC, ransomware and data leaks. Centrally managed with granular policies, threat intelligence and real-time insights for seamless workspace security.

!!! Warning Important note - This format is currently in beta. We highly value your feedback to improve its performance.

* **Vendor**: Check Point
* **Supported environment**: SaaS
* **Detection based on**: Telemetry, Alert
* **Supported application or feature**: Email gateway, Cloud security

#### Supported events

This integration supports the following event types:

* `phishing`
* `malware`
* `suspicious malware`
* `dlp`
* `anomaly`
* `shadow_it`
* `malicious_url_click`
* `malicious_url`
* `alert`

### Configure

**How To Set Up The Forwarding**

1. Log in to the Checkpoint Harmony portal
2. Go to the Checkpoint Harmony Email & Collaboration interface
3. On the left panel, navigate to `Security Settings` > `Security Engines`
4. Scroll down to the `SIEM Integration` section
5. Click `Configure`
6. Select `HTTP Collector` as **Transport**
7. Type `https://intake.sekoia.io/plain` as **HTTP Collector URL**

!!! warning The previous URL works for the FRA1 region. For any other region, replace the domain “intake.sekoia.io” with your region’s HTTP-intake domain—for example:

```
https://app.usa1.sekoia.io/api/v1/intake-http

You can find your region’s domain here: [https://docs.sekoia.io/getting_started/regions/](https://docs.sekoia.io/getting_started/regions/)
```

8\. Select `JSON` as **Format**

9. Enable `Add custom header`
10. Type `X-SEKOIAIO-INTAKE-KEY` as the **Custom header name**
11. Type your intake key as the **Custom header value**
12. Click `Save`

!!! info Events can take up to 15 minutes to be sent by Checkpoint Harmony after being generated.

**Create an intake**

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Checkpoint Harmony Email & Collaboration`.
2. Copy the intake key that was generated.
3. Use this intake key in the Checkpoint Harmony configuration as described above.

{!\_shared\_content/operations\_center/integrations/generated/71bd28dc-163d-4262-9d50-84ec4a9cef65\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_71bd28dc-163d-4262-9d50-84ec4a9cef65\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/71bd28dc-163d-4262-9d50-84ec4a9cef65.md!}
