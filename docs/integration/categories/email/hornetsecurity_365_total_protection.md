uuid: 21bb5b9b-dc0e-4941-8932-262005a2789c
name: Hornetsecurity 365 TotalProtection
type: intake

## Overview

Hornetsecurity is a leading provider of cloud-based email security and data protection services. Our solutions are designed to protect businesses from spam, malware, phishing, and other email-borne threats. With a focus on simplicity and reliability, Hornetsecurity offers advanced threat protection, email archiving, encryption, and continuity services to ensure secure and uninterrupted communication for organizations of all sizes.

- **Vendor**: Hornetsecurity
- **Supported environment**: Control Panel
- **Detection based on**: Telemetry
- **Supported application or feature**: Email gateway, Anti-virus

!!! Warning
    Important note - This format is currently in beta. We highly value your feedback to improve its performance.


## Configure

### Create a Token in the Hornetsecurity Control Panel

1.	Go to the [Hornetsecurity Control Panel](https://cp.hornetsecurity.com/).
2.	Sign in with your credentials.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step1_login.png)

3.	In the top-right menu, click on **User settings**.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step3_usersettings_link.png)

4.	On the **User settings** page, go to the **API Token** tab.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step4_usersettings_apitoken.png)

5.	Click on the **Create token** button.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step5_createtoken.png)

6.	Enter a name for your token, then click **Create**.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step6_tokenname.png)

7.	Copy your token from the **Token details** section.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step7_gettoken.png)

8.	You can view your token(s), expiration date(s), and other details in the table on this page.

    ![Hornetsecurity Control Panel](/assets/integration/email/hornetsecurity/Step8_tokeninfo.png)



### Create your intake

1. Go to the [intake page](https://app.sekoia.io/operations/intakes) and create a new intake from the `Hornetsecurity 365 Total Protection`.
2. Set the intake account configuration with the `api_token` and the `base_url` from the previous step.

### Enjoy your events on the [Events page](https://app.sekoia.io/operations/events)

{!_shared_content/operations_center/integrations/generated/21bb5b9b-dc0e-4941-8932-262005a2789c_sample.md!}

{!_shared_content/integration/detection_section.md!}

{!_shared_content/operations_center/detection/generated/suggested_rules_21bb5b9b-dc0e-4941-8932-262005a2789c_do_not_edit_manually.md!}

{!_shared_content/operations_center/integrations/generated/21bb5b9b-dc0e-4941-8932-262005a2789c.md!}
