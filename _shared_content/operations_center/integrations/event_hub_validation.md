Follow these steps to check that the events flow from the Microsoft product to Sekoia.io:

1. **The Microsoft product sends events to the Event Hub**: in the Azure portal, open your **Event Hub** and look at the **Incoming Messages** metric in the **Overview** tab. It must be greater than zero. Otherwise, review the streaming configuration of the Microsoft product. The first events can take several minutes to arrive.
2. **Sekoia.io reads the Event Hub**: on the same page, the **Outgoing Messages** metric must follow the **Incoming Messages** metric. Otherwise, check the Event Hub name, the connection string and the consumer group set in the intake configuration.
3. **Checkpoints are written**: in your **Storage Account**, open the **Blob Container** of the intake. It must contain a folder tree named after your Event Hub Namespace, Event Hub and Consumer Group, ending with a `checkpoint` folder that holds one blob per partition of the Event Hub. Otherwise, check the storage connection string and the container name set in the intake configuration.
4. **Events reach Sekoia.io**: on the [Events page](https://app.sekoia.io/operations/events), filter on your intake and check that recent events are displayed and parsed.

!!! note
    Only the events received by the Event Hub after the creation of the intake are collected. Generate some activity (a sign-in for instance) if no event shows up.
