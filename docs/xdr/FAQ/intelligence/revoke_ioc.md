### **What is a False Positive IoC?**

A false positive IoC is an [object](https://www.sekoia.io/en/glossary/stix/) linked to legitimate activity that is mistakenly identified as a threat or attack. These false positives can sometimes occur due to the sensitivity of detection rules or the complex nature of certain network activities. You can report what you suspect to be a false positive within a Sekoia feed.

### **Why is it important to request the revocation of a legitimate IoC?**

Reporting a false positive helps Sekoia.io improve the accuracy of its detection systems. By flagging these occurrences, you contribute to refining the collections that detect threats, reducing future false alerts, and allowing your security team to focus on real threats.

### **How to Request the Revocation of an IoC?**

You can do this directly by following these [steps in the documentation](/xdr/features/detect/ioccollections.md#revoke-an-indicator).

### **What Happens After Requesting the Revocation of an IoC?**

After a thorough review, several actions may be taken regarding your request:

- **Revocation of the indicator:** This action will be taken if the indicator was not meant to be on the platform initially (e.g., IoCs triggering false positives like [google.com](http://google.com/)).
- **Modification of the indicator's validity date:** This may occur in cases where the indicator is no longer valid or associated with an intrusion group. Conversely, if the indicator remains relevant for the intrusion group, its validity date may be extended.
- **No action:** If no changes are deemed necessary after the review, the indicator will remain unchanged, as it is still considered relevant.

### **Can I Cancel a False Positive Report?**

If you reported a false positive by mistake, you can contact Sekoia.io technical support via the [customer portal](https://support.sekoia.io/hc/en-gb) to request the cancellation of the report. It is important to provide details of the incorrect report (IoC UUID) to facilitate the correction process.

### **Who Should I Contact If I Encounter Issues Reporting a False Positive?**

If you face challenges in reporting a false positive or have additional questions, you can contact Sekoia.io customer support via the [customer portal](https://support.sekoia.io/hc/en-gb). The team is available to assist and address your concerns.

---
