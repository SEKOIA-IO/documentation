---
uuid: 1ef7f586-5354-4171-9266-f9f049c3253a
name: PingFederate
type: intake
---

## Overview

PingFederate is an enterprise federation server from Ping Identity that provides secure single sign-on (SSO), API security, and identity bridging. It generates audit and operational logs (authentication events, token lifecycle actions, administrative changes) that can be forwarded via Syslog for centralized monitoring and detection.

In this documentation, you will learn how to collect and send PingFederate logs to Sekoia.io.

- **Vendor**: Ping Identity
- **Supported environment**: On Premise
- **Detection based on**: Telemetry
- **Supported application or feature**: Authentication, Authorization, Token lifecycle, Administrative audit logs

!!! Warning
    This format is currently in beta. We highly value your feedback to improve its performance.

## High-Level Architecture Diagram

- **Type of integration**: Outbound (PUSH to Sekoia.io)
- **Schema**

## Specification

### Prerequisites

- **Resource**:
    - Self-managed syslog forwarder (e.g. rsyslog, syslog-ng)
- **Network**:
    - Outbound TCP allowed from the PingFederate appliance to the forwarder on your chosen port
- **Permissions**:
    - Root (or equivalent) access on the PingFederate appliance
    - Root (or equivalent) access on the Linux server hosting the syslog forwarder

### Transport Protocol/Method

- **Indirect Syslog (RFC5424)**

### Logs details

- **Supported functionalities**: See section [Overview](#overview)
- **Supported type(s) of structure**: Syslog messages (RFC5424)
- **Supported verbosity level**: Informational / Audit

!!! Note
    Log levels follow the RFC5424 taxonomy. Adapt your forwarder's parsing rules accordingly.

## Step-by-Step Configuration Procedure

### Instructions on the 3rd Party Solution

#### Forward PingFederate Logs to a syslog forwarder

This setup guide will lead you into forwarding PingFederate's logs to Sekoia.io by means of a syslog transport channel.

#### Detailed Procedure:

1. **Prerequisites:**
   - An internal syslog concentrator is required to collect and forward events to Sekoia.io.

2. **Create the Intake in Sekoia.io:**
   - Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `PingFederate`. Copy the intake key.

3. **Configure Log4j2 for Syslog Forwarding:**

   On the system hosting PingFederate:

   1. SSH into your PingFederate server and open the Log4j2 configuration file:

      ```bash
      vi /opt/pingfederate/server/default/conf/log4j2.xml
      ```

   2. **Enable tracking ID correlation** (recommended for event correlation):

      Tracking IDs (`tid`) allow you to correlate events across multiple log entries for the same transaction. Ensure the `TrackingIdSupport` is enabled in your PingFederate configuration.

   3. Add or modify the Syslog appender to forward logs with the proper format. The pattern **must match** the format expected by Sekoia.io's parser:

      ```xml
      <Configuration>
        <Appenders>
          <!-- Existing appenders ... -->

          <!-- Syslog appender for Sekoia.io -->
          <Syslog name="SekoiaSyslog"
                  format="RFC5424"
                  host="<concentrator-ip-address>"
                  port="<concentrator-port>"
                  protocol="TCP"
                  facility="LOCAL0"
                  appName="pingfederate">
            <!-- CRITICAL: Use this exact pattern for proper parsing -->
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss,SSS} tid:%X{trackingid} %-5level [%c] %msg%n"/>
          </Syslog>

          <!-- Optional: HTTP access logs appender (if using embedded Jetty logging) -->
          <Syslog name="SekoiaHttpAccess"
                  format="RFC5424"
                  host="<concentrator-ip-address>"
                  port="<concentrator-port>"
                  protocol="TCP"
                  facility="LOCAL1"
                  appName="pingfederate-http">
            <PatternLayout pattern="%msg%n"/>
          </Syslog>
        </Appenders>

        <Loggers>
          <!-- Application logs: audit, authentication, token lifecycle -->
          <Root level="info">
            <AppenderRef ref="SekoiaSyslog"/>
          </Root>

          <!-- Capture detailed authentication events -->
          <Logger name="org.sourceid.saml20.domain.mgmt.impl" level="info" additivity="false">
            <AppenderRef ref="SekoiaSyslog"/>
          </Logger>

          <!-- Capture OAuth/OIDC token events -->
          <Logger name="org.sourceid.oauth20" level="info" additivity="false">
            <AppenderRef ref="SekoiaSyslog"/>
          </Logger>

          <!-- Capture session and SSO events -->
          <Logger name="org.sourceid.websso" level="info" additivity="false">
            <AppenderRef ref="SekoiaSyslog"/>
          </Logger>

          <!-- Capture administrative audit events -->
          <Logger name="com.pingidentity.console.audit" level="info" additivity="false">
            <AppenderRef ref="SekoiaSyslog"/>
          </Logger>

          <!-- Optional: Capture DEBUG level for troubleshooting (generates more logs) -->
          <!-- Uncomment if needed for detailed debugging -->
          <!--
          <Logger name="org.sourceid" level="debug" additivity="false">
            <AppenderRef ref="SekoiaSyslog"/>
          </Logger>
          -->
        </Loggers>
      </Configuration>
      ```

      **Key Configuration Notes:**

      - **Pattern Layout**: The pattern `%d{yyyy-MM-dd HH:mm:ss,SSS} tid:%X{trackingid} %-5level [%c] %msg%n` ensures compatibility with Sekoia.io's parser
      - **Tracking ID**: `%X{trackingid}` includes the correlation ID in every log entry (appears as `tid:` in logs)
      - **Timestamp format**: `yyyy-MM-dd HH:mm:ss,SSS` matches the expected ISO8601-like format with milliseconds
      - **Logger name**: `[%c]` includes the full Java class name for better event categorization

   4. **Configure HTTP access logs** (optional but recommended):

      If you want to capture HTTP access logs separately, edit the Jetty configuration:

      ```bash
      vi /opt/pingfederate/server/default/conf/jetty-runtime.xml
      ```

      Enable request logging with the Common Log Format (CLF):

      ```xml
      <Set name="RequestLog">
        <New class="org.eclipse.jetty.server.NCSARequestLog">
          <Arg>
            <SystemProperty name="pf.log.dir" default="<pf_install>/pingfederate/log"/>
            /pf-http-access.log
          </Arg>
          <Set name="extended">false</Set>
          <Set name="append">true</Set>
          <Set name="LogTimeZone">GMT</Set>
        </New>
      </Set>
      ```

      Then configure rsyslog on the PingFederate host to forward these logs to your concentrator (see step 5).

   5. **Forward HTTP access logs via rsyslog** (if using file-based HTTP logs):

      On the PingFederate host, configure rsyslog to monitor the HTTP access log file:

      ```bash
      vi /etc/rsyslog.d/10-pingfederate-http.conf
      ```

      Add:

      ```bash
      # Monitor PingFederate HTTP access logs
      module(load="imfile" PollingInterval="10")

      input(type="imfile"
            File="/opt/pingfederate/log/pf-http-access.log"
            Tag="pingfederate-http:"
            Severity="info"
            Facility="local1")

      # Forward to concentrator
      local1.* @@<concentrator-ip-address>:<concentrator-port>
      ```

      Restart rsyslog:

      ```bash
      systemctl restart rsyslog
      ```

   6. Save `log4j2.xml` and restart PingFederate:

      ```bash
      systemctl restart pingfederate
      ```

   7. **Verify log format** by checking the syslog output:

      ```bash
      tail -f /var/log/messages | grep pingfederate
      ```

      You should see logs in this format:

      ```
      2025-09-02 11:02:32,869 tid:Z8I1vdotGu084PB7b2HrQ0A1kKU INFO [org.sourceid.saml20.service.impl.AuthnRequestProcessorImpl] Processing authentication request
      ```

!!! Note
    **Important Pattern Requirements:**

    - The timestamp **must** use the format `yyyy-MM-dd HH:mm:ss,SSS` (comma before milliseconds)
    - The tracking ID **must** appear as `tid:XXXXX` (with the colon)
    - The log level **must** be 5 characters wide with left padding (`%-5level`)
    - The logger name **must** be enclosed in brackets `[%c]`

    Any deviation from this pattern will cause parsing failures in Sekoia.io.


### Instruction on Sekoia
{!_shared_content/integration/intake_configuration.md!}

{!_shared_content/integration/forwarder_configuration.md!}

{!_shared_content/operations_center/integrations/generated/1ef7f586-5354-4171-9266-f9f049c3253a_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_1ef7f586-5354-4171-9266-f9f049c3253a_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/1ef7f586-5354-4171-9266-f9f049c3253a.md!}

## Further Readings

- [PingFederate documentation - Logging Configuration](https://docs.pingidentity.com/r/en-us/pingfederate-latest/pf_logging_configuration)
- [PingFederate documentation - Correlating log events using attributes](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_correlating_log_events_attributes.html)
- [RFC5424 - The Syslog Protocol](https://datatracker.ietf.org/doc/html/rfc5424)