---
title: "Troubleshoot common issues"
description: "First-level solutions for the most common login, connectivity, and data ingestion issues in Sekoia."
keywords: [troubleshooting, login, websocket, intake, no events, connectivity, 2fa, password, network]
audience: all
module: all
type: task
---

# Troubleshoot common issues

This article covers the most common issues you may encounter when using Sekoia and provides first steps to resolve them. If a solution does not resolve your problem, contact support at [support.sekoia.com](https://support.sekoia.com).

## Login and account issues

### You cannot reach the login page

**Possible cause:** You are using the wrong URL for your workspace region.

**What to do:**

1. Verify your region URL with your administrator. Each Sekoia region has a different app URL (see [Log in for the first time](/getting_started/log_in_for_the_first_time.md) for the full table).
2. Try accessing the URL directly in your browser instead of using a saved bookmark.
3. Check that your network does not block access to `*.sekoia.io`.

### Your password does not work

**What to do:**

1. Click **Forgot password** on the login page.
2. Enter your email address.
3. Check your inbox (including spam) for the password reset email.
4. Follow the link in the email to set a new password. The link is valid for 24 hours.

### Your two-factor authentication code is not accepted

**Possible cause:** The time on your device is out of sync, or you are using an expired code.

**What to do:**

1. Verify that your device's time and date are set automatically (check your operating system clock settings).
2. Wait for your authenticator app to generate a new code before trying again.
3. If the problem persists, contact your workspace administrator and ask them to reset your 2FA.

See: [Secure your account](/getting_started/secure_your_account.md) for the administrator reset procedure.

### Your account has been deactivated

**What to do:**

Contact your workspace administrator. They can reactivate your account from **Settings > Users**. After reactivation, you must log in at least once before midnight on the same day, or the account will be deactivated again.

## Connectivity issues

### The platform does not refresh automatically (WebSocket error)

**Symptom:** A network connectivity error banner appears at the top of the page, and data in the interface does not update without a manual page refresh.

**Cause:** Your browser cannot maintain a WebSocket connection to `app.sekoia.com/live`.

**What to do:**

!!! tips "HAR archive step"
   If the net-export log file does not provide enough detail, generate a HAR (HTTP Archive) file to capture the full request and response trace:

   1. Open Chrome DevTools (F12) and select the **Network** tab.
   2. Check **Preserve log**.
   3. Reproduce the connectivity issue in the Sekoia tab.
   4. Right-click on any request in the Network tab and select **Save all as HAR with content**.
   5. Attach the `.har` file to your support ticket.

!!! note "Other browsers"
    If you are not using Chrome, contact [support.sekoia.com](https://support.sekoia.com) and describe your browser. The support team will guide you through the equivalent steps.

1. Contact your network administrator and ask them to verify that WebSocket connections are permitted to `wss://app.sekoia.io/live`.
2. If the problem persists, collect network logs for investigation:
    1. Open Google Chrome and navigate to `chrome://net-export/`.
    2. Click **Start Logging to Disk** and save the file.
    3. In a new tab, open your Sekoia workspace and reproduce the issue.
    4. Return to `chrome://net-export/` and click **Stop Logging**.
    5. Attach the log file when opening a support ticket at [support.sekoia.com](https://support.sekoia.com).

### API requests are blocked or return a 429 error

**Cause:** Your requests are hitting Sekoia's Web Application Firewall (WAF) rate limits.

**What to do:**

- Reduce your request frequency to fewer than 5 requests per second.
- If your script encounters two 4XX or 5XX errors within 10 seconds, add a pause before retrying.
- If multiple users share a VPN exit point, coordinate API usage to stay within collective limits.

## Intake and event ingestion issues

### Your intake shows zero events after setup

**What to do:**

| Intake type | Check |
|---|---|
| **Push** | Verify the intake key is correctly deployed in your data source configuration. Confirm your firewall permits outbound connections to the Sekoia intake endpoint for your region. |
| **Pull** | Open the intake detail page and check the **Connector log** tab for error messages. Look for authentication failures or API connectivity errors. Verify the credentials you entered during intake setup are correct. |

Allow up to 30 minutes after configuration before concluding that no events are arriving.

See: [Verify event reception](/getting_started/defend_step2_verify_event_reception.md) for the full verification procedure.

### Your intake shows a high rate of warning or invalid events

**What to do:**

1. Open the intake detail page.
2. In the **Events** section, filter by **Warning** or **Invalid** to view the parsing error messages.
3. Cross-reference the error with the technology-specific setup guide in the [integration catalog](https://docs.sekoia.com/integration/).
4. If the issue is not covered in the guide, open a support ticket.

## Still need help?

If none of the steps above resolve your issue, contact the Sekoia support team:

- Open a ticket at [support.sekoia.com](https://support.sekoia.com).
- Include your workspace name, the region, the affected feature, and a description of the steps you already tried.

## Related links

- [Support and resources](/getting_started/support_and_resources.md) — Full list of support and learning resources.
- [Log in for the first time](/getting_started/log_in_for_the_first_time.md) — Region URL reference and invitation troubleshooting.
- [Secure your account](/getting_started/secure_your_account.md) — 2FA reset procedure for administrators.
- [Verify event reception](/getting_started/defend_step2_verify_event_reception.md) — Intake health checks and monitoring setup.
