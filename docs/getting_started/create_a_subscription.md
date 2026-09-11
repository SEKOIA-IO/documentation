# Create a subscription

You can create a subscription from the **Subscriptions** page when Self-Service is enabled for your partner. The wizard guides you through the module, plan, commercial terms, usage settings, and final confirmation.

## Prerequisites

- You can access the target community.
- You have permission to manage community subscriptions.
- **Create a subscription** is available from **Add subscription**.
- You know the module, plan, start date, and capacity that you want to configure.

!!! note "Creation is unavailable"
    If **Add subscription** only opens **Assign a subscription**, creation is not enabled for your partner or user. Contact Sekoia if you need to create a new subscription.

## Create the subscription

### Open the wizard

1. Open **Subscriptions**.
2. Click **Add subscription**.
3. Click **Create a subscription**.

### Select the module

1. Select the module that you want to activate.
2. Click **Continue**.

The available modules depend on the catalog enabled for your partner. The current flow can display **Defend**, **Intelligence**, and **Reveal**.

![Module step of the subscription creation wizard](/assets/self_service/04_create_subscription_module.png)

### Select the plan

1. Select the plan that matches your requirements.
2. To review plan differences, click **Compare plans**.
3. Click **Continue**.

![Plan step of the subscription creation wizard](/assets/self_service/05_create_subscription_plan.png)

### Choose the commercial terms

1. Select **On-Demand** or **Fixed-Term**.
2. If you select **Fixed-Term**, enter the duration displayed by the form.
3. Select the available payment method.
4. Click **Continue**.

The current interface displays a fixed-term duration between 12 and 36 months. Available durations and payment methods depend on the selected configuration.

![Terms step with the commitment and payment options](/assets/self_service/06_create_subscription_terms.png)

### Configure usage

1. Enter the **Start date**.
2. Select the **Billing model** when the module provides more than one model.
3. Enter the capacity values requested by the form.
4. Select additional retention when the option is available.
5. Click **Continue**.

For the Defend **Asset-based** model, configure the number of assets and the available fair-use allocation per asset. The form calculates the included monthly capacity from these values.

For the **Volume-based** model, configure the data volume supported by the selected offer. The displayed fields and limits depend on the module and plan.

!!! warning "Check the capacity"
    Verify the asset count or data volume before continuing. These values define the included capacity and can affect usage billing or overage charges.

![Usage step with Defend asset-based capacity settings](/assets/self_service/07_create_subscription_usage.png)

![Usage step before capacity values are entered](/assets/self_service/08_create_subscription_usage_empty.png)

### Review and confirm

1. Review the module and plan.
2. Review the commitment, payment method, and dates.
3. Review the billing model and calculated capacity.
4. Select every required confirmation.
5. Click **Create subscription**.

The confirmation button remains disabled until the required confirmations are selected.

![Review step with the configuration summary and required confirmations](/assets/self_service/09_create_subscription_review.png)

## Result

After confirmation, Sekoia attaches the subscription to the target community. The subscription appears on the **Subscriptions** page with the available module, plan, period, region, and capacity information.

If you selected **Save as template**, the configuration can be reused for another subscription. Check the dates and community-specific capacity for every new subscription.

## Related articles

- [Subscriptions](/getting_started/subscriptions.md): Overview of the Subscriptions page and its available workflows.
- [Assign a subscription](/getting_started/assign_a_subscription.md): How to attach an existing subscription instead of creating one.
