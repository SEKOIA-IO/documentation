# Retrieved logs from a Cloud provider or a SaaS platform

In addition to the previously documented push modes (HTTPS, Syslog, Relp), Sekoia.io also possesses the capability to ingest data using a pulling mode.

Indeed, many tools and equipment have APIs to enable direct data consumption. However, using these endpoints can be a bit tricky. Therefore, Sekoia.io has developed numerous integrations that include out-of-the-box connectors, known as triggers, responsible for collecting data. You can easily configure them in [Sekoia.io playbooks](/xdr/features/automate/index.md) with just a few clicks. Make sure to follow the documentation associated with your integration to verify the complete procedure.

Sekoia.io can also retrieve logs and data from cloud platforms, including Microsoft Azure, Amazon Web Services, or Google Cloud. To consume this type of data, as a prerequisites you need to define a location to centralize data coming from your managed services on your cloud provider:

- [AWS S3](aws.md)
- [Azure Event Hub](azure.md)
- [Google Pub/Sub](gcp.md)

Finally, you have to configure the associated out-of-the-box trigger as explained in the previous section. You can find a end to end documentation for each integration in his specific page covering the configuration of these prerequisites
