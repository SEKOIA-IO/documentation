import sys

import requests

from constants import API_URL, BULK_SIZE, PREFIXES


class GitBookClient:
    """GitBook API client for managing pages and redirects."""

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"

    def request(self, method: str, path: str, params: dict | None = None, body: dict | None = None) -> dict:
        # API_URL ends with /v1: concatenate rather than urljoin, which would drop it
        response = self.session.request(method, f"{API_URL}{path}", params=params, json=body)
        if not response.ok:
            sys.exit(f"{method} {path} failed ({response.status_code}): {response.text}")
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

    def list_draft_redirects(self, org: str, site: str) -> dict[str, dict]:
        """
        Return {source: destination} of the draft redirects managed by this script
        """
        redirects: dict[str, dict] = {}
        params: dict = {"limit": 100, "draft": "true"}
        while True:
            response = self.request("GET", f"/orgs/{org}/sites/{site}/redirects", params=params)
            for item in response.get("items", []):
                if item.get("draft") and item["source"].startswith(tuple(PREFIXES.values())):
                    redirects[item["source"]] = item["destination"]
            next_page = (response.get("next") or {}).get("page")
            if not next_page:
                return redirects
            params["page"] = next_page

    def push_draft_redirects(self, org: str, site: str, operations: list[dict]) -> list[dict]:
        errors = []
        for i in range(0, len(operations), BULK_SIZE):
            batch = [{"intent": "draft", **operation} for operation in operations[i : i + BULK_SIZE]]
            response = self.request("PUT", f"/orgs/{org}/sites/{site}/redirects", body={"redirects": batch})
            errors += [result for result in response.get("results", []) if result.get("status") == "error"]
        return errors
