---
title: "Troubleshoot common issues"
description: "First-level solutions for the most common login, connectivity, and data ingestion issues in Sekoia."
keywords: [troubleshooting, login, websocket, intake, no events, connectivity, 2fa, password, network]
audience: all
module: all
type: task
---

# Troubleshoot common issues

This article covers the most common issues you may encounter when using Sekoia and provides first steps to resolve them. If a solution does not resolve your problem, contact support at [support.sekoia.io](https://support.sekoia.io).

## Login and account issues

### You cannot reach the login page

**Possible cause:** You are using the wrong URL for your workspace region.

**What to do:**

1. Verify your region URL with your administrator. Each Sekoia region has a different app URL (see [Log in for the first time](/getting_started/log_in_for_the_first_time.md) for the full table).
2. Try accessing the URL directly in your browser instead of using a saved bookmark.
3. Check that your network does not block access to `*.sekoia.io`.

!!! note "SSO workspaces"
    If your workspace uses Single Sign-On (SSO), your login URL may differ from the standard region URL. Contact your administrator for the correct SSO login link.

### Your password does not work

**What to do:**

1. Click **Forgot password** on the login page.
2. Enter your email address.
3. Check your inbox (including spam) for the password reset email.
4. Follow the link in the email to set a new password. The link is valid for 24 hours.

!!! note "First-time access and SSO"
    If you have never logged in before, password reset will not work. Use the invitation link from your welcome email to activate your account first.
    Password reset is not available for users who log in using Single Sign-On (SSO). Contact your IT administrator to reset your SSO credentials.

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

**Cause:** Your browser cannot maintain a WebSocket connection to `app.sekoia.io/live`.

**What to do:**

1. Contact your network administrator and ask them to verify that WebSocket connections are permitted to `wss://app.sekoia.io/live`.
2. If the problem persists, collect a network log (HAR file) for investigation and attach it to your support ticket:
    - For Google Chrome, follow the [Chrome HAR capture instructions](https://support.google.com/admanager/answer/10358597).
    - For Mozilla Firefox, use the Network Monitor in DevTools: open DevTools (F12), go to the **Network** tab, reproduce the issue, right-click any request, and select **Save All as HAR**.
    - For Microsoft Edge, follow the [Edge network log instructions](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network/reference).
    - For other browsers, refer to your browser vendor's documentation for capturing a HAR file.

    Open a support ticket at [support.sekoia.io](https://support.sekoia.io) and attach the log file.

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

!!! tip "Using the Sekoia Forwarder?"
    If you are using the Sekoia.io Forwarder to send events, consult the [Forwarder troubleshooting guide](/integration/ingestion_methods/syslog/sekoiaio_forwarder.md) for specific diagnostic steps.

See: [Verify event reception](/getting_started/defend_step2_verify_event_reception.md) for the full verification procedure.

### Your intake shows a high rate of warning or invalid events

**What to do:**

1. Open the intake detail page.
2. In the **Events** section, filter by **Warning** or **Invalid** to view the parsing error messages.
3. Check the **Raw event** tab for the affected events to verify that the log format matches what the intake expects. If the format is different from what Sekoia expects (for example, an unknown header or unexpected structure), the log is considered malformed.
4. If the format is malformed, review your entire ingestion chain and the configuration of the third-party application sending the log.
5. If the format is correct but Sekoia does not extract fields relevant to detection, cross-reference the issue with the technology-specific setup guide in the [integration catalog](/integration/categories/index.md) and open a support ticket with a copy of the raw event if the issue is not covered.

!!! tip "Checking log format"
    In the intake documentation for your technology, the **Raw event** section shows an example of the expected log format. Compare it with what your source is sending to identify formatting differences.

## Still need help?

If none of the steps above resolve your issue, contact the Sekoia support team:

- Open a ticket at [support.sekoia.io](https://support.sekoia.io).
- Include your workspace name, the region, the affected feature, and a description of the steps you already tried.

## Related links

- [Support and resources](/getting_started/support_and_resources.md): Full list of support and learning resources.
- [Log in for the first time](/getting_started/log_in_for_the_first_time.md): Region URL reference and invitation troubleshooting.
- [Secure your account](/getting_started/secure_your_account.md): 2FA reset procedure for administrators.
- [Verify event reception](/getting_started/defend_step2_verify_event_reception.md): Intake health checks and monitoring setup.
