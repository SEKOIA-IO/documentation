# thinkst\_canary

uuid: 89346697-b64b-45d4-a456-72fd8a2be5d8 name: Thinkst Canary type: intake

### Overview

Thinkst Canary is a deceptive honeypot device that mimics various systems to lure and detect cyber threats, providing early and accurate breach alerts. Canarytokens are easy-to-deploy digital traps that notify users of unauthorized access to sensitive information.

* **Vendor**: Thinkst Applied Research
* **Supported environment**: SaaS
* **Detection based on**: Alert
* **Supported application or feature**: events associated to the incidents

### Step-by-Step Configuration Procedure

#### How to create an API Key

1. Log in the Thinkst Canary console
2. On the top panel, click the toothed wheel and got to **Global Settings**
3. In the **Global Settings**, Click the **API** section
4. Turn on the **Enabled** toggle and Click **+** button. Write down `Domain hash`
5. Select **Analyst** as the API Key type
6. Type a name for the API Key
7. Click **Create**

#### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Thinkst Canary`.
2. Set the intake configuration with the following parameters:
   * `Base URL`, which should be `https://DOMAINHASH.canary.tools`, where `DOMAINHASH` is your domain hash from the `How to create an API Key` step
   * `Auth token` from the same step

#### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!\_shared\_content/operations\_center/integrations/generated/89346697-b64b-45d4-a456-72fd8a2be5d8\_sample.md!}

{!\_shared\_content/integration/detection\_section.md!}

{!\_shared\_content/operations\_center/detection/generated/suggested\_rules\_89346697-b64b-45d4-a456-72fd8a2be5d8\_do\_not\_edit\_manually.md!} {!\_shared\_content/operations\_center/integrations/generated/89346697-b64b-45d4-a456-72fd8a2be5d8.md!}
