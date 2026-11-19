uuid: 7b92dd21-ceab-4450-a3bc-99d1669f2e18
name: urlscan.io
type: playbook

# urlscan.io

![urlscan.io](../../../../assets/playbooks/library/urlscan-io.png)

urlscan.io is a sandbox for the web. It visits submitted URLs in an automated browser, records the domains, IPs, requests and files involved, takes a screenshot, gives a verdict and indexes every scan for search.

## Configuration

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `api_key` | `string` | urlscan.io API key. A team API key is recommended: scans submitted with it are visible to every team member |
| `base_url` | `string` | Base URL of the urlscan.io API |

## Actions

### Download scan screenshot

Download the PNG screenshot of a finished urlscan.io scan as a file of the playbook run. The file can be downloaded from the playbook run and may show victim data. Fails when urlscan.io did not store the screenshot.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `scan_id` | `string` | UUID of a finished scan (urlscan.io scanId) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `screenshot_path` | `string` | Path of the PNG, relative to the playbook run storage: urlscan/<uuid>.png |
| `screenshot_url` | `string` | Link to the PNG on urlscan.io, opens without an account even for a private scan |
| `size` | `integer` | Size of the PNG in bytes |

### Get scan result

Return the summary of an existing urlscan.io scan: verdict, final page, contacted infrastructure, links and a ready-to-post Markdown comment.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `scan_id` | `string` | UUID of a finished scan (urlscan.io scanId) |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `['string', 'null']` | Scan UUID |
| `status` | `string` | Scan status, done for a finished scan |
| `submitted_url` | `['string', 'null']` | URL scanned, normalised by urlscan.io |
| `visibility` | `['string', 'null']` | public, unlisted or private |
| `scan_time` | `['string', 'null']` | Scan time, ISO 8601 |
| `tags` | `array` | User tags |
| `verdict` | `object` | Verdict of the scan |
| `page` | `object` | Final page of the scan |
| `brand` | `['string', 'null']` | Detected brand |
| `contacted` | `object` | Infrastructure contacted by the page |
| `stats` | `object` | Request statistics |
| `downloaded_files` | `array` | Files downloaded by the page |
| `report_url` | `['string', 'null']` | urlscan.io report, opens without an account |
| `result_api_url` | `['string', 'null']` | Raw JSON result |
| `screenshot_available` | `['boolean', 'null']` | True when urlscan.io stores the screenshot, false when it does not, null when not checked |
| `screenshot_url` | `['string', 'null']` | Screenshot URL, opens without an account; null when the screenshot is not stored |
| `dom_available` | `['boolean', 'null']` | True when urlscan.io stores the DOM, false when it does not, null when not checked |
| `dom_url` | `['string', 'null']` | DOM URL, null when the DOM is not stored; opens only for urlscan.io team members |
| `comment` | `['string', 'null']` | Ready-to-post Markdown comment for Comment Alert / Comment case; embeds the screenshot when urlscan.io stores it (the image stays hosted by urlscan.io) |

### Scan URL

Submit a URL to urlscan.io, wait for the scan and return the verdict, the final page, the contacted infrastructure, the report / screenshot / DOM links and a ready-to-post Markdown comment. Internal addresses are refused before submission.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `url` | `string` | The URL to scan |
| `customagent` | `string` | Override the HTTP User-Agent used by urlscan.io |
| `visibility` | `string` | Visibility of the scan: public, unlisted or private. A public scan is visible to everyone |
| `tags` | `array` | User tags, for example phishing (at most 10, 30 characters each) |
| `country` | `string` | Two-letter ISO 3166-1 alpha-2 code of the country to scan from, for example fr. urlscan.io detects it when empty |
| `fail_on_blacklisted_url` | `boolean` | When false, a URL blacklisted by urlscan.io returns the status blacklisted instead of failing |
| `wait_for_result` | `boolean` | When false, return right after the submission with the status submitted; use Get scan result later |
| `timeout` | `integer` | Maximum time to wait for the scan, in seconds |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `uuid` | `['string', 'null']` | Scan UUID |
| `status` | `string` | Scan status: done, submitted (wait_for_result false) or blacklisted (fail_on_blacklisted_url false) |
| `submitted_url` | `['string', 'null']` | URL scanned, normalised by urlscan.io |
| `visibility` | `['string', 'null']` | public, unlisted or private |
| `scan_time` | `['string', 'null']` | Scan time, ISO 8601 |
| `tags` | `array` | User tags |
| `verdict` | `object` | Verdict of the scan |
| `page` | `object` | Final page of the scan |
| `brand` | `['string', 'null']` | Detected brand |
| `contacted` | `object` | Infrastructure contacted by the page |
| `stats` | `object` | Request statistics |
| `downloaded_files` | `array` | Files downloaded by the page |
| `report_url` | `['string', 'null']` | urlscan.io report, opens without an account |
| `result_api_url` | `['string', 'null']` | Raw JSON result |
| `screenshot_available` | `['boolean', 'null']` | True when urlscan.io stores the screenshot, false when it does not, null when not checked |
| `screenshot_url` | `['string', 'null']` | Screenshot URL, opens without an account; null when the screenshot is not stored |
| `dom_available` | `['boolean', 'null']` | True when urlscan.io stores the DOM, false when it does not, null when not checked |
| `dom_url` | `['string', 'null']` | DOM URL, null when the DOM is not stored; opens only for urlscan.io team members |
| `comment` | `['string', 'null']` | Ready-to-post Markdown comment for Comment Alert / Comment case; embeds the screenshot when urlscan.io stores it (the image stays hosted by urlscan.io) |

### Search

Search existing urlscan.io scans from an indicator (URL, domain, IP or SHA256) or an Elasticsearch Query String query, without spending a scan. Returns one page; paginate with next_search_after.

**Arguments**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `indicator` | `string` | IP address, domain, URL or SHA256 to search for; provide this or query |
| `query` | `string` | Elasticsearch Query String query, sent as the q parameter, for example task.tags:"phishing" AND date:>now-7d; values with colons, slashes or spaces must be double-quoted; provide this or indicator |
| `size` | `integer` | Number of results in the page |
| `search_after` | `string` | next_search_after of the previous call (comma-separated sort values of its last result), to get the next page |


**Outputs**

| Name      |  Type   |  Description  |
| --------- | ------- | --------------------------- |
| `query` | `string` | Query sent to urlscan.io, the query argument or the one built from the indicator |
| `total` | `integer` | Number of matching scans, exact up to 10000 |
| `has_more` | `boolean` | True when more than 10000 scans match |
| `took` | `integer` | Search time in milliseconds |
| `search_date_limit_days` | `['integer', 'null']` | History limit in days, set on free plans only |
| `next_search_after` | `['string', 'null']` | Value to pass as search_after for the next page, null on the last page |
| `results` | `array` | Scans of the page |

## Set up

## Create a team API key

A team key is recommended: it uses the team quotas and features, is not tied to a user, and every team member sees it. Scans submitted with it are visible to all team members.

1. Log in to [urlscan.io](https://urlscan.io) and open the [`User`](https://urlscan.io/user/) tab.
2. Go to `Manage Team` > `<your team>` > `Team API Keys`.
3. Click `➕ New Team API key`, set a comment (e.g. `Sekoia.io playbooks`) and validate.

## Retrieve the key

The API has no endpoint to list or retrieve keys, and no login endpoint. Only the user who created the key can copy it: in `Team API Keys`, reveal the masked key in the `Key Details` column and paste it in the `API key` field of the module configuration.

## Check the key

```bash
curl -s -H "API-Key: $API_KEY" https://urlscan.io/user/username   # must reference your team
curl -s -H "API-Key: $API_KEY" https://urlscan.io/api/v1/quotas    # "scope": "team"
```

`401` means the key is invalid or disabled. Key activity: `Last Activity` column, or `GET https://urlscan.io/api/v1/activity/user` / `activity/team`.

## Confidentiality

- The `screenshot_url` and `report_url` of a `private` scan open **without a urlscan.io account**. Once posted in an alert or case comment, they are visible to every user who can read it. Treat them as sensitive.
- The `comment` result embeds the screenshot: the reader's browser loads it from urlscan.io. The image disappears when urlscan.io deletes the scan.
- *Download scan screenshot* writes the PNG to the playbook run. Users who can view playbook runs can download it until the run is deleted (8 days on FRA1, 7 days on the other regions). A phishing screenshot may show victim data.


## Extra

Module **`urlscan.io` v1.0.0**