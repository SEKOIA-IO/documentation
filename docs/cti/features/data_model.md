# Data Model


The Intelligence Center uses the industry standard STIX ([version 2.1](https://oasis-open.github.io/cti-documentation/stix/intro.html)) to represent information.

## Objects

STIX uses JSON objects with pre-defined schemas to represent Cyber Threat Intelligence data. The knowledge graph is based on nodes (STIX Domain Objects or SDO) and relationships (STIX Relationship Objects or SRO).

The Intelligence Center supports the following STIX Domain Objects:

![objects-types](/assets/intelligence_center/data-model-objects.png){: style="max-width:100%"}

## Observables

An observable is a technical information that can detect a potential threat. They are derived from all data contained in the Intelligence Center but are not always contextualized.

!!! note
    If an observable clearly represent a malicious activity then it is an IoC (Indicator of Compromise).

Observables are automatically extracted from various sources : public, subscriptions, partners, SEKOIA internal analysis.

The Intelligence Center supports the following observables:

![observables-types](/assets/intelligence_center/data-model-observables.png){: style="max-width:100%"}

### What is the difference between an indicator and an observable?
To understand the difference between an indicator (an object type) and an observable, we have to dig deeper into the definition of each one of these.

**Observables**

- These are different kinds of technical artifacts
- They are not necessary malicious (example: `google.com`)
- They can be enriched with tags to contextualize the (non)-threat
    - These tags allow you to enrich logs/events in Sekoia.io XDR
- They are not provided in the CTI feed (API / TAXII / MISP, etc.)
- They don’t directly raise alerts in Sekoia.io XDR but tag-based detection rules can be created to allow that
- They can be manually enriched through the web application and can have dedicated relations (for example : `resolves-to`, `belongs-to`, etc.)
- They are usable (thanks to the tags system) within Sekoia.io XDR to create warning rules that provide context to the analysts who are in charge of producing Intelligence or to avoid false positives creation.

**Indicators**

- These are Indicators of Compromise (IoC)
- They are always related to a threat (malware, campaign, intrusion set, threat actor, vulnerability, etc.) and they are always contextualized with a confidence rating, a validity date and a Kill chain phase
- They are based on observables
- They are exported in the CTI feed (API / TAXII / MISP, etc.) to allow a contextualized detection
- They raise real-time alerts in Sekoia.io XDR but also in the past through retro hunting which depends on the validity period of the indicator and the log retention duration

## External Sources

One of the founding principle of the Intelligence Center is the consolidation of information coming from several sources.

Sources are represented in STIX by `Identity` objects.

Our consolidation strategy means that the `created_by_ref` field of the STIX objects will always be set to the SEKOIA identity. The sources that contributed to one of our STIX object are available, as references, in the `x_inthreat_sources_refs` custom field.

As an example, here are parts of a `Spearphishing Link` object:

```json
{
  "type": "attack-pattern",
  "name": "Spearphishing Link",
  "id": "attack-pattern--6cd1a813-ccdf-4ba0-9b54-cb808f1059cc",

  "created_by_ref": "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",  # SEKOIA

  "x_inthreat_sources_refs": [
    "identity--357447d7-9229-4ce1-b7fa-f1b83587048e",  # SEKOIA
    "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5"   # The MITRE Corporation
  ],

  [...]
}
```

## Confidence

STIX 2.1 adds an optional `confidence` field for an object creator to express how confident we are about the information.

When specified, this confidence level on objects should be read with the [Admiralty Credibility](https://docs.google.com/document/d/1Cqi89CU6FwEdLjGFqMnxpl3T4iSWE_gbImBq2WXEXYk/edit#heading=h.1v6elyto0uqg) scale.

| Number | Meaning | Details |
| --- | --- | --- |
| 1 | Confirmed by other sources | Confirmed by other independent sources; logical in itself; Consistent with other information on the subject |
| 2 | Probably true | Not confirmed; logical in itself; consistent with other information on the subject |
| 3 | Possibly true | Not confirmed; reasonably logical in itself; agrees with some other information on the subject |
| 4 | Doubtful | Not confirmed; possible but not logical; no other information on the subject |
| 5 | Improbable | Not confirmed; not logical in itself; contradicted by other information on the subject |
| 6 | Truth cannot be judged | No basis exists for evaluating the validity of the information |

## Reliability

Next to the source (object type: `Identity`), the `confidence` score may be specified to express the source's reliability. When specified, this reliability level should be read with the [Admiralty Reliability](https://docs.google.com/document/d/1Cqi89CU6FwEdLjGFqMnxpl3T4iSWE_gbImBq2WXEXYk/edit#heading=h.1v6elyto0uqg) scale.

| Letter | Meaning | Details |
| --- | --- | --- |
| A | Completely reliable | No doubt of authenticity, trustworthiness, or competency; has a history of complete reliability |
| B | Usually reliable | Minor doubt about authenticity, trustworthiness, or competency; has a history of valid information most of the time |
| C | Fairly reliable | Doubt of authenticity, trustworthiness, or competency but has provided valid information in the past |
| D | Not usually reliable | Significant doubt about authenticity, trustworthiness, or competency but has provided valid information in the past |
| E | Unreliable | Lacking in authenticity, trustworthiness, and competency; history of invalid information |
| F | Reliability cannot be judged | No basis exists for evaluating the reliability of the source |
