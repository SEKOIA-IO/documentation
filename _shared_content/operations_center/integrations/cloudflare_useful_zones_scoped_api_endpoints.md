##### Useful Cloudflare API endpoints
On their documentation, Cloudflare provides a [list API endpoints](https://developers.cloudflare.com/logs/get-started/api-configuration/){:target="_blank"} you can use. Find below some useful endpoints:

- `https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/logpush/jobs/<JOB_ID>` to verify the job you previously created is correct (you need to specify the `JOB_ID`)
- `https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/logpush/datasets/<DATASET>/jobs` to get all the jobs for a specific dataset (`dns_log`, `firewalls_events` or `http_requests` in our case)
- `https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/logpush/jobs/<JOB_ID>` to update a job if you noticed a mistake after the creation of the job (wrong fields, wrong SEKOIA API Key...)
