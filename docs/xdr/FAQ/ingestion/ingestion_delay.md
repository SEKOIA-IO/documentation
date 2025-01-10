# Event Ingestion and Alert Delays on Sekoia.io

When using the Sekoia.io platform, you might occasionally notice delays in event ingestion or alert generation. Below are some frequently asked questions to help you understand and address these issues.


### **1. Why was the event ingested with a delay?**

The platform uses various fields to determine event timestamps, depending on the intake (connector) used. For instance:

- **Syslog events**: The timestamp may be extracted from the Syslog header.
- **Default behavior**: If no specific timestamp is defined in the parser, the platform uses the `event.created` field, which indicates when the event was received on Sekoia.io.

**Common causes of delays:**

- **Source-side delays**: Events might be generated or made available late from the source.
- **Connectivity issues**: Network problems, such as a loss of internet connectivity, can delay event transmission.
- **Platform incidents**: Rare incidents on the platform can slow down ingestion. Check the [SEKOIA Status](https://status.sekoia.io/) page for updates.


### **2. Why was the alert generated with a delay relative to the event?**

Several factors may cause this:

- **Recently added IoC**: If the alert is based on an Indicator of Compromise (IoC), it might have been added after the event was received. Retro-hunting can trigger alerts for past events, as indicated in the alert's `Detection Type` field.
- **Platform incidents**: Issues on the platform can occasionally delay alert processing. Refer to the [SEKOIA Status](https://status.sekoia.io/) page for updates.
- **Delayed event transmission**: If the event was sent late, the `event.created` field (when the event was received on Sekoia.io) may provide a more accurate timeline than the event's original timestamp.


### **3. What should I do if I suspect a delay in ingestion or alert generation?**

To investigate and address delays:

1. **Check the timestamp fields**:
   - Review the parser code for the intake to determine which field is used for the event timestamp.
   - If no specific timestamp is defined, refer to the `event.created` field.

2. **Consult the `event.created` field**:
   - This field indicates when the platform received the event and is crucial for understanding delays caused by late event transmission.

3. **Verify platform status**:
   - Check for ongoing incidents on the [SEKOIA Status](https://status.sekoia.io/) page.

4. **Contact support**:
   - If the issue persists and no clear cause is identified, contact our technical support team with details of the affected event.


For any additional questions or concerns, feel free to reach out to our team for assistance.
