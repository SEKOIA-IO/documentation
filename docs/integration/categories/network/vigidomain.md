uuid: cc64de36-d998-4f9a-b354-bc1fa3f340b4
name: Vigidomain
type: intake

## Overview
 
**Vendor:** Vigidomain
 
Vigidomain monitors for typosquatting, brand impersonation, and malicious domains that target your organization. It surfaces contextualized, actionable threat indicators so you can catch phishing campaigns and other external threats early.
 
## Configure
 
This guide walks through connecting Vigidomain to Sekoia, so that Vigidomain alerts are automatically pushed into a Sekoia intake.
 
### Prerequisites
 
Before you start, confirm your Vigidomain account has:
 
- **API access enabled** — you should see an "API" link under **Settings > API** in the main sidebar.
- **The "External API" option enabled** — this is what allows Vigidomain to push alerts to external destinations like Sekoia.

If either is missing, contact Vigidomain support to have them enabled for your organization.
 
### Step 1 — Create the intake in Sekoia
 
1. In Sekoia, go to **Intakes**.
2. Click **Create intake** and search for "Vigidomain".
3. Copy the **intake key**. You'll need it in Step 2.

### Step 2 — Connect Vigidomain to the intake
 
1. In Vigidomain, go to **Settings > API**.
2. Under the "External API" section, click **Add** to create a new endpoint.
3. Name and describe the endpoint however you like.
   Example — Name: `Sekoia`, Description: `Push alerts to Sekoia intake`.
4. Choose the push method matching your Sekoia instance (usually **POST**), and enter the push URL.
5. Add a header:
   - **Header:** `X-SEKOIAIO-INTAKE-KEY`
   - **Value:** the intake key copied in Step 1.
6. Select which domains and assets should trigger alerts sent to Sekoia.
7. Click **Save**.

Once saved, new alerts matching your selected assets are pushed to Sekoia automatically. To confirm it's working, use the built-in **test** button to send an existing alert through the endpoint.
