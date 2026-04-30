# Getting Started with the Sekoia.io API

The Sekoia.io REST API lets you access platform data, trigger actions, and build integrations or automations on top of Sekoia.io. The GUI itself is built on this API, so anything you can do in the interface, you can do via the API.

## Step 1 — Find your base URL

The base URL depends on the region where your Sekoia.io subscription is hosted.

| Region | Base URL |
| --- | --- |
| FRA1 (default) | `https://api.sekoia.io` |
| FRA2 | `https://app.fra2.sekoia.io/api` |
| MCO1 | `https://app.mco1.sekoia.io/api` |
| UAE1 | `https://app.uae1.sekoia.io/api` |
| USA1 | `https://app.usa1.sekoia.io/api` |

If you are unsure of your region, look at the URL you use to access the Sekoia.io application. For example, if you log in via `https://app.mco1.sekoia.io/`, your API base URL is `https://app.mco1.sekoia.io/api`.

## Step 2 — Create an API key

All API requests are authenticated with an API key. To create one:

1. In Sekoia.io, go to **Settings > Workspace > API Keys**.
2. Click **+ API key**.
3. Give your key a name and a description.
4. Set an expiration date (30 days, 180 days, 365 days, or custom up to 1 year).
5. Select the permissions your key needs.
6. Click **Save** and copy the key immediately — it will only be shown once.

!!! tip
    Start with read-only permissions. You can always create a second key with write permissions when you need to perform write operations.

!!! note
    Only users with admin roles can create API keys.

## Step 3 — Make your first API call

To verify that your key works, retrieve your user profile. This endpoint requires no special permissions beyond a valid key.

```bash
export SEKOIA_API_KEY="your_api_key_here"

curl -X GET https://api.sekoia.io/v1/me \
  -H "Authorization: Bearer $SEKOIA_API_KEY"
```

A successful response looks like this:

```json
{
  "uuid": "2a4b6c8d-...",
  "email": "you@example.com",
  "firstname": "Jane",
  "lastname": "Doe"
}
```

If you can see your email and UUID, your setup is working.

## Troubleshooting

| Status code | Meaning | What to do |
| --- | --- | --- |
| `401 Unauthorized` | The API key is missing, expired, or invalid. | Check that the key is correctly copied and has not expired. |
| `403 Forbidden` | The key does not have the required permission for this endpoint. | Edit the key and add the missing permission, or create a new key with the right permissions. |
| `429 Too Many Requests` | You have exceeded the rate limit. | Wait before retrying. Add a delay between requests in your scripts. |

## Next steps

- [Search for rules](tutorials/search_rules.md) — filter and retrieve detection rules from your catalog
- [Create a SIGMA rule](tutorials/create_sigma_rule.md) — create a detection rule programmatically
- [Search events](tutorials/search_events.md) — run an asynchronous event search and retrieve results
