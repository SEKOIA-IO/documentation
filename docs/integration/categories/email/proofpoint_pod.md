# proofpoint\_pod

uuid: e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e name: Proofpoint On Demand type: intake

### Overview

ProofPoint On Demand (PoD) offers a real-time email processing feed to detect, classify and mitigate threats.

* **Vendor**: Proofpoint
* **Supported environment**: Cloud
* **Detection based on**: Telemetry
* **Supported application or feature**: Email gateway

### Configure

#### Proofpoint On Demand

As a prerequisite, you need to create an APIKey and to get your cluster id:

To create an APIKey, from [admin.proofpoint.com](https://admin.proofpoint.com):

* Open the menu, unfold the `Settings` section and go to `API Key Management`.
* Select the `PoD Logging` tab
* Click on the button `Create New` to display the `Create New API Key` dialog box.
* Type a name
* Copy the Cluster ID
* Click `Generate Key`
* Select `View Details` from the ellipsis menu on the fresh API Key and copy the key.

#### Create the intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the format `Proofpoint PoD`.
2. Set up the intake configuration with the api key and the cluster id.

Start the playbook and enjoy your events.

{!\_shared\_content/operations\_center/integrations/generated/e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e\_do\_not\_edit\_manually.md!}

{!\_shared\_content/operations\_center/integrations/generated/e0eaf2f1-02d0-4d1a-be89-f2b8be4baf4e.md!}

### Further Readings

* [ProofPoint APIKey Management](https://help.proofpoint.com/Admin_Portal/Settings/API_Key_Management)
