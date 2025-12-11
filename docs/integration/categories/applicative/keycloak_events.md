uuid: cc1b212e-80c2-4dde-8446-2e194c6d4e80
name: Keycloak
type: intake

## Overview

Keycloak is an open-source identity and access management solution that enables Single Sign-On (SSO), social login and standard protocols like OAuth2, OpenID Connect and SAML. It supports user federation, fine-grained authorization policies and multi-factor authentication. Easy to deploy and integrate, it secures applications and services with minimal coding.

- **Vendor**: Keycloak
- **Supported environment**: On-premise, Cloud
- **Detection based on**: Telemetry
- **Supported application or feature**: User Events


!!! Warning
	Important note - This format is currently in beta. We highly value your feedback to improve its performance.


## Supported events

This integration supports the following event types:

- User Events

## Configure

### Prerequisites

- Administrator access to Keycloak Console
- Access to Sekoia.io Intakes page with write permissions
- A log concentrator to forward events to Sekoia.io

### Create an intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format Keycloak.
2. Copy the intake key for later use in the forwarder configuration.

### Enable User events in Keycloak

#### Step 1: Access Realm Settings

1. Log in to the Keycloak Console as an administrator
2. Go to `Realm settings`

    ![Step - 01.png](/assets/integration/applicative/keycloak_events/Step_01.png)

3. Click `Events` tab

    ![Step - 02.png](/assets/integration/applicative/keycloak_events/Step_02.png)

4. Select `jboss-logging` as `Event listeners`
5. Click `Save`

    ![Step - 03.png](/assets/integration/applicative/keycloak_events/Step_03.png)

6. Click `User events settings` Tab

    ![Step - 04.png](/assets/integration/applicative/keycloak_events/Step_04.png)

7. Enable `save events`
8. Click `Save`

    ![Step - 03.png](/assets/integration/applicative/keycloak_events/Step_03_1.png)

### Forward events to the concentrator

In the Keycloak configuration, set the following options to forward events to a log concentrator:

- `log` (env: `KC_LOG`): add `syslog` to the option
- `log-syslog-endpoint` (env: `KC_LOG_SYSLOG_ENDPOINT`): Set the IP address of the concentrator and the port dedicated for the intake
- `log-syslog-protocol` (env: `KC_LOG_SYSLOG_PROTOCOL`): Set to `tcp`
- `log-syslog-output` (env: `KC_LOG_SYSLOG_OUTPUT`): Set to `json`
- `log-syslog-json-format` (env: `KC_LOG_SYSLOG_JSON_FORMAT`): Set to `ecs`

**Using Environment Variables**

```bash
KC_LOG=syslog
KC_LOG_SYSLOG_ENDPOINT=<ip_concentrator>:<intake_port>
KC_LOG_SYSLOG_PROTOCOL=tcp
KC_LOG_SYSLOG_OUTPUT=json
KC_LOG_SYSLOG_JSON_FORMAT=ecs
```

**Using the `keycloak.conf` File**

```bash
log=syslog
log-syslog-endpoint=<ip_concentrator>:<intake_port>
log-syslog-protocol=tcp
log-syslog-output=json
log-syslog-json-format=ecs
```

### Forward events to Sekoia.io

Please consult the [Syslog Forwarding](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) documentation to forward these logs to Sekoia.io.

Create a new configuration file:

```bash
sudo vim ./extended_conf/12-keycloak.conf
```

with the following template:

```bash
input(type="imtcp" port="PORT" ruleset="remoteKeycloak")

template(name="SEKOIAIOTemplate" type="string" string="<%pri%>1 %timestamp:::date-rfc3339% %hostname% %app-name% %procid% LOG [SEKOIA@53288 intake_key=\"INTAKE_KEY\"] %msg%\n")
ruleset(name="remoteKeycloak"){
  if($msg contains "org.keycloak.events") then {
    action(
        type="omfwd"
        protocol="tcp"
        target="intake.sekoia.io"
        port="10514"
        TCP_Framing="octet-counted"
        StreamDriver="gtls"
        StreamDriverMode="1"
        StreamDriverAuthMode="x509/name"
        StreamDriverPermittedPeers="intake.sekoia.io"
        Template="SEKOIAIOTemplate"
    )
  }
}
```

!!! note
    Please change `INTAKE_KEY` with your actual intake key, as well as the `PORT` number.

Update the `docker-compose.yml` file of the Sekoia.io forwarder to mount the extended conf:

```yaml
volumes:
    - ./intakes.yaml:/intakes.yaml
...
    - ./extended_conf:/extended_conf
```

{!_shared_content/operations_center/integrations/generated/cc1b212e-80c2-4dde-8446-2e194c6d4e80_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_cc1b212e-80c2-4dde-8446-2e194c6d4e80_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/cc1b212e-80c2-4dde-8446-2e194c6d4e80.md!}
