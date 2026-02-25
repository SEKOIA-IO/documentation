# FAQ

## IP

### Is the IP behind `intake.sekoia.io` static?

**IP for `intake.sekoia.io` is currently `213.32.5.228`.**

`intake.sekoia.io` is the domain name used to send your logs to Sekoia.io, either via Syslog or HTTP protocols. The IP address behind that service is mostly static but may change at any time. Please refrain from doing IP filtering to avoid future issues. If you absolutely need to perform IP filtering, please manage your own DNS configuration and keep up with upstream changes. Old IPs will continue working for up to a month after the official DNS modification.

### Outgoing IP addresses for playbooks runs and connectors


For all the actions available in the Playbooks section of Sekoia.io (include connectors used to retrieve logs from external sources), we use a number of outbound IP addresses. The full list is publicly accessible and can be retrieved at the following URL: [https://api.sekoia.io/outgoing-ips](https://api.sekoia.io/outgoing-ips). This will be useful to setup filtering options if needed, and even automate any future update.

We try to make this list as stable as possible, but events out of our control may result in modifications. If any changes occur, we are committed to providing our customers with advance notice of at least two weeks, either via a dedicated communication, or via our [status page](https://status.sekoia.io/).


### How to debug Rsyslog’s forward configuration to Sekoia.io?

If you use Rsyslog to forward your logs to Sekoia.io, you will probably have a section like this in your configuration files:

```
template(name="SEKOIAIOUnboundTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5\"] %msg%\n")
if $programname startswith 'unbound' then @@(o)intake.sekoia.io:10514;SEKOIAIOUnboundTemplate

```

If you want to retrieve the raw data that is forwarded to Sekoia.io, you can duplicate the last line and make Rsyslog dump logs to a local file:

```
if $programname startswith 'unbound' then /tmp/nginx-output.log;SEKOIAIOUnboundTemplate
```

This way, you will be able to exactly identify what data is sent to Sekoia.io.


```
# tail -n 1 /tmp/nginx-output.log
<30>1 2021-01-13T14:52:06.934860+01:00 ote unbound - LOG [SEKOIA@53288 intake_key="jOK5bMVXz5Iz7gfogQDbCcC7l7S2IrOs5"]  [596451:0] info: 127.0.0.1 intake.sekoia.io. A IN
```


## Logs

### Can I access logs older than my hot storage period?
Yes. If your subscription includes cold storage (**Archiving**, you can request the temporary restoration of archived events. 

To understand how tiers work, see our article on [Data storage and retention](docs/xdr/FAQ/data_storage_retention.md). 

To start a restoration, follow the procedure to [restore data from cold storage](docs/xdr/FAQ/restore_data_cold_storage.md).

**Restoration flow**

<img style="max-width:100%" alt="Archiving diagram" src="/xdr/FAQ/archiving_process.png">


## Best Practices for Development and Interaction with Our Product to Avoid Being Blocked by Our WAF

Web Application Firewalls (WAF) are crucial components for the security of web applications. They protect against various threats by filtering and monitoring HTTP traffic between a web application and the Internet. Our AI-based WAF uses a credibility score to determine the reliability of users and their interactions with our product. This article explores why we use a WAF, the specifics of our AI WAF, the main types of anomalies clients may encounter, and provides recommendations and best practices for interacting with our product without getting blocked.

### 1. Why Use a WAF?

A WAF is an indispensable security tool for protecting web applications against common attacks such as SQL injections, cross-site scripting (XSS), DDoS attacks, and other web-based threats. By using a WAF, we can:

- Prevent attacks by filtering malicious requests before they reach the application.
- Monitor traffic in real-time to detect and quickly respond to suspicious behavior.
- Protect sensitive data by preventing unauthorized access.
- Ensure application availability by minimizing interruptions due to attacks.

### 2. Specifics of an AI-Based WAF

Our AI-based WAF goes beyond traditional security rules by using machine learning algorithms to evaluate user credibility. The credibility score is calculated based on various behaviors and interactions. Here are some specifics:

- **Credibility Score Calculation**: The AI analyzes user behavior over periods of about ten seconds. Repeated anomalies lower the user's credibility.
- **Reputation Update Cycles**: The user's reputation is updated in cycles, averaging every 30 seconds. If suspicious behaviors persist, the user will be blocked.
- **Types of Anomalies**: The WAF detects security anomalies (scans, SSRF, injections, exploits, protocol manipulations), and behaviors exceeding fixed and dynamic (AI based) thresholds.

### 3. Main Types of Anomalies Clients May Encounter

Anomalies are evaluated in real-time and can impact the user's credibility. Here are the main types of anomalies:

- **Security Anomalies**:

    - Security scans, SSRF, injections, exploitation of vulnerabilities, protocol manipulations.

- **Anomalies Relative to Fixed Thresholds**:

    - **Response Time**: Requests taking more than 10 seconds of CPU/memory processing.
    - **Request Frequency**: More than 100 requests per second.
    - **Authentication**: Strengthened mechanisms on authentication management pages.

- **Anomalies Relative to Smart Thresholds**:

    - **Response Time**: Limit requests to less than 100 ms per second over a 10-second period.
    - **Error Requests**: Do not exceed 8 errors/s (4XX or 5XX codes) per 5-second period.

!!! Note
    **Error Code 429**: Indicates rate limiting when too many requests are received in a short time.

### 4. Recommendations and Best Practices

To avoid being blocked by our WAF, it is important to follow these best practices when interacting with our API and the product UI in general:

- **Optimize Requests**: Avoid requests that consume too many resources (no more than 100 ms per request).
- **Limit Request Frequency**: Do not exceed 5 requests per second.
- **Handle Errors**: Pause scripts if the return code is 4XX or 5XX for 2 requests within a 10-second period.
- **Impact Duration**: In case of blocking, the user will be impacted for between 30 seconds and 10 minutes (randomized duration).

!!! Note
    Users sharing the same VPN exit point will be considered as a single user. Ensure that multiple users accessing the service through the same VPN do not collectively exceed the recommended limits.

By following these recommendations, you can improve the user experience and ensure smooth interaction with our product while respecting the security measures implemented by our WAF.
