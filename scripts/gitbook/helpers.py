import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from constants import API_URL, BULK_SIZE, PREFIXES, RETRIES, RETRY_STATUSES, TIMEOUT


class GitBookError(Exception):
    """Raised when a GitBook API call fails."""


class GitBookClient:
    """GitBook API client for managing pages and redirects."""

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        # every call made here is idempotent (GET, bulk PUT), so they can be retried safely
        retry = Retry(
            total=RETRIES,
            backoff_factor=1,
            status_forcelist=RETRY_STATUSES,
            allowed_methods=frozenset({"GET", "PUT"}),
            respect_retry_after_header=True,
            raise_on_status=False,
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

    def request(self, method: str, path: str, params: dict | None = None, body: dict | None = None) -> dict:
        try:
            response = self.session.request(method, f"{API_URL}{path}", params=params, json=body, timeout=TIMEOUT)
        except requests.RequestException as error:
            raise GitBookError(f"{method} {path} failed: {error}") from error
        if not response.ok:
            raise GitBookError(f"{method} {path} failed ({response.status_code}): {response.text}")
        return response.json() if response.content else {}

    def list_pages(self, space: str) -> dict[str, str]:
        """
        Return {repository file path: page id}
        """
        pages: dict[str, str] = {}

        def walk(node):
            if isinstance(node, dict):
                git_path = (node.get("git") or {}).get("path")
                if git_path and node.get("id"):
                    pages[git_path] = node["id"]
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)

        walk(self.request("GET", f"/spaces/{space}/content/pages"))
        return pages

    def list_redirects(self, org: str, site: str, draft: bool) -> dict[str, dict]:
        """
        Return {source: destination} of the draft (or live) redirects managed by this script
        """
        redirects: dict[str, dict] = {}
        # the API lists either the live redirects (default) or the draft ones, never both
        params: dict = {"limit": 100, "draft": "true" if draft else "false"}
        while True:
            response = self.request("GET", f"/orgs/{org}/sites/{site}/redirects", params=params)
            for item in response.get("items", []):
                if bool(item.get("draft")) == draft and item["source"].startswith(tuple(PREFIXES.values())):
                    redirects[item["source"]] = item["destination"]
            next_page = (response.get("next") or {}).get("page")
            if not next_page:
                return redirects
            params["page"] = next_page

    def push_draft_redirects(self, org: str, site: str, operations: list[dict]) -> list[dict]:
        """
        Push the operations as draft redirects, in batches, and return the failed items.

        Batches are independent: a failing batch does not stop the next ones, its items are
        reported as errors. The synchronization is idempotent, so a rerun applies what is left.
        """
        errors = []
        for i in range(0, len(operations), BULK_SIZE):
            batch = [{"intent": "draft", **operation} for operation in operations[i : i + BULK_SIZE]]
            try:
                response = self.request("PUT", f"/orgs/{org}/sites/{site}/redirects", body={"redirects": batch})
            except GitBookError as error:
                errors += [{"source": operation["source"], "error": str(error)} for operation in batch]
                continue
            errors += [result for result in response.get("results", []) if result.get("status") == "error"]
        return errors
