# Indicators vs. Observables

This is one of the most common points of confusion in Threat Intelligence. The distinction is not just semantic. It has direct consequences on **how data is used, shared, and acted upon in the platform.**

### Start with the observable <a href="#start-with-the-observable" id="start-with-the-observable"></a>

An observable is a **fact**. It describes something that exists or has been observed in the digital world: an IP address, a domain name, a file hash, a URL. By itself, it carries no judgment.

> `198.51.100.42` is an IP address. That's all we know.

An observable can be:

* **Benign** — `google.com` is an observable. It is not a threat.
* **Suspicious** — an IP tagged `scanner:*` is worth watching, but is not confirmed malicious.
* **Unknown** — no context, no tags, no associations yet.

Observables are enriched over time with **tags** that provide context (geolocation, reputation, infrastructure type), but tags alone do not make an observable a threat.

### What makes an indicator different <a href="#what-makes-an-indicator-different" id="what-makes-an-indicator-different"></a>

An indicator is a **judgment**. It asserts that a specific observable pattern is malicious and is associated with a known threat. An indicator is never standalone. It always answers three questions:

1. **What is it?** The observable pattern (e.g. this exact IP, this file hash)
2. **What threat is it linked to?** A malware, campaign, intrusion set, threat actor, or vulnerability
3. **How certain are we, and for how long?** A confidence score and a validity period

> `198.51.100.42` has been observed communicating with Cobalt Strike C2 infrastructure attributed to APT28, with high confidence, valid until 2026-06-01. **That is an indicator.**

### The transformation path <a href="#the-transformation-path" id="the-transformation-path"></a>

An observable does not become an indicator automatically. It requires an **analytical decision**:

```
Observable (SCO)
    ↓
  + confirmed malicious activity
  + linked to a specific threat (malware, campaign, intrusion set...)
  + confidence score assigned
  + validity period defined
  + kill chain phase mapped
    ↓
Indicator (SDO) = IoC
```

This transformation is explicit and intentional. It is the work of an analyst, not an automated tag.

### Practical consequences <a href="#practical-consequences" id="practical-consequences"></a>

|                                 | Observable (SCO)             | Indicator (SDO)             |
| ------------------------------- | ---------------------------- | --------------------------- |
| **Inherently malicious?**       | No                           | Yes, by definition          |
| **Requires threat context?**    | No                           | Yes, always                 |
| **Has confidence score?**       | No                           | Yes                         |
| **Has validity period?**        | No                           | Yes                         |
| **Exported in CTI feed?**       | ❌                            | ✅ API, TAXII, MISP          |
| **Triggers alerts in XDR?**     | ❌ (tag-based rules possible) | ✅ Real-time + retro hunting |
| **Can be enriched with tags?**  | ✅                            | No                          |
| **Linked to kill chain phase?** | No                           | Yes                         |

### One-line rule <a href="#one-line-rule" id="one-line-rule"></a>

> If you can say _"this is malicious because of X threat"_, it is an indicator. If you can only say _"this exists"_, it is an observable.
