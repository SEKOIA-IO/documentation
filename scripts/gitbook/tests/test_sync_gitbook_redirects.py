import tempfile
import unittest
from pathlib import Path
from typing import ClassVar
from unittest import mock

import requests
from click.testing import CliRunner

import sync_gitbook_redirects
from constants import TIMEOUT
from helpers import GitBookClient, GitBookError
from sync_gitbook_redirects import collect_uuids, main, read_metadata

INTAKE_UUID = "591feb54-1d1f-4453-b780-b225c59e9f99"
INTAKE_UUID_2 = "f95fea50-533c-4897-9272-2f8361e63644"
ASSET_UUID = "b2e2e2c7-1a3e-4b7a-9c2d-8e4f3a6b7c9d"
PLAYBOOK_UUID = "5894985f-91eb-46db-9306-cc5ac6463d3d"

INTAKE_SOURCE = f"/operation_center/integration_catalog/uuid/{INTAKE_UUID}"
INTAKE_SOURCE_2 = f"/operation_center/integration_catalog/uuid/{INTAKE_UUID_2}"


class RepositoryTestCase(unittest.TestCase):
    """Build a fake repository with a docs/integration directory."""

    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.repository = Path(directory.name).resolve()
        self.docs_dir = self.repository / "docs" / "integration"
        self.docs_dir.mkdir(parents=True)

        patcher = mock.patch.object(sync_gitbook_redirects, "REPOSITORY", self.repository)
        patcher.start()
        self.addCleanup(patcher.stop)

    def write(self, relative: str, content: str) -> Path:
        path = self.docs_dir / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path


class ReadMetadataTests(RepositoryTestCase):
    def test_mkdocs_format(self):
        path = self.write("a.md", f"uuid: {INTAKE_UUID}\nname: Cisco NX-OS\ntype: intake\n\n## Overview\n")
        self.assertEqual(read_metadata(path), {"uuid": INTAKE_UUID, "name": "Cisco NX-OS", "type": "intake"})

    def test_flattened_by_gitbook(self):
        path = self.write("a.md", f"# cisco\\_nx\\_os\n\nuuid: {INTAKE_UUID} name: Cisco NX-OS type: intake\n")
        self.assertEqual(read_metadata(path), {"uuid": INTAKE_UUID, "name": "Cisco NX-OS", "type": "intake"})

    def test_metadata_after_first_lines_is_ignored(self):
        path = self.write("a.md", "\n" * 15 + f"uuid: {INTAKE_UUID}\ntype: intake\n")
        self.assertEqual(read_metadata(path), {})

    def test_late_uuid_is_detected(self):
        late = self.write("late.md", "\n" * 15 + f"uuid: {INTAKE_UUID}\n")
        mid_line = self.write("mid.md", "\n" * 15 + "Some text with uuid: in the middle\n")
        self.assertTrue(sync_gitbook_redirects.has_late_uuid(late))
        self.assertFalse(sync_gitbook_redirects.has_late_uuid(mid_line))

    def test_no_metadata(self):
        path = self.write("a.md", "# Title\n\nSome text with uuid: in the middle\n")
        self.assertEqual(read_metadata(path), {})


class CollectUuidsTests(RepositoryTestCase):
    def test_sources_by_type(self):
        self.write("categories/network/cisco.md", f"uuid: {INTAKE_UUID}\nname: Cisco\ntype: intake\n")
        self.write("assets_categories/user/okta.md", f"uuid: {ASSET_UUID}\nname: Okta\ntype: asset\n")
        self.write("action_library/http.md", f"uuid: {PLAYBOOK_UUID}\nname: HTTP\ntype: playbook\n")

        self.assertEqual(
            collect_uuids(self.docs_dir),
            {
                INTAKE_SOURCE: ("docs/integration/categories/network/cisco.md", "intake"),
                f"/integration/asset_connectors/uuid/{ASSET_UUID}": (
                    "docs/integration/assets_categories/user/okta.md",
                    "asset",
                ),
                f"/integration/action_library/uuid/{PLAYBOOK_UUID}": (
                    "docs/integration/action_library/http.md",
                    "playbook",
                ),
            },
        )

    def test_playbook_outside_action_library_is_ignored(self):
        self.write("categories/other/playbook.md", f"uuid: {PLAYBOOK_UUID}\ntype: playbook\n")
        self.assertEqual(collect_uuids(self.docs_dir), {})

    def test_unknown_type_and_missing_uuid_are_ignored(self):
        self.write("a.md", f"uuid: {INTAKE_UUID}\ntype: rule\n")
        self.write("b.md", "name: No uuid\ntype: intake\n")
        self.assertEqual(collect_uuids(self.docs_dir), {})

    def test_several_uuids_in_one_page(self):
        self.write("a.md", f"uuid: {INTAKE_UUID.upper()}, {INTAKE_UUID_2}\ntype: intake\n")
        # the original case is kept, as the mkdocs plugin did
        self.assertEqual(
            set(collect_uuids(self.docs_dir)),
            {f"/operation_center/integration_catalog/uuid/{INTAKE_UUID.upper()}", INTAKE_SOURCE_2},
        )

    def test_late_uuid_is_reported(self):
        self.write("a.md", "\n" * 15 + f"uuid: {INTAKE_UUID}\ntype: intake\n")

        with mock.patch("builtins.print") as printed:
            self.assertEqual(collect_uuids(self.docs_dir), {})

        self.assertIn("after the first 10 lines", printed.call_args.args[0])

    def test_shared_uuid_keeps_the_last_page(self):
        self.write("categories/network/opnsense.md", f"uuid: {INTAKE_UUID}\ntype: intake\n")
        self.write("categories/network/pfsense.md", f"uuid: {INTAKE_UUID}\ntype: intake\n")

        with mock.patch("builtins.print") as printed:
            redirects = collect_uuids(self.docs_dir)

        self.assertEqual(redirects[INTAKE_SOURCE][0], "docs/integration/categories/network/pfsense.md")
        printed.assert_called_once()

    def test_symlinked_directory_is_followed(self):
        library = self.repository / "_shared_content" / "library"
        library.mkdir(parents=True)
        (library / "http.md").write_text(f"uuid: {PLAYBOOK_UUID}\ntype: playbook\n")
        (self.docs_dir / "action_library").symlink_to(library)

        self.assertEqual(
            collect_uuids(self.docs_dir),
            {
                f"/integration/action_library/uuid/{PLAYBOOK_UUID}": (
                    "docs/integration/action_library/http.md",
                    "playbook",
                )
            },
        )


def response(payload: dict | None = None, status: int = 200) -> mock.Mock:
    return mock.Mock(ok=status < 400, status_code=status, content=b"{}", text="error", json=lambda: payload or {})


class GitBookClientTests(unittest.TestCase):
    def setUp(self):
        self.client = GitBookClient("secret")
        self.session_request = mock.patch.object(self.client.session, "request").start()
        self.addCleanup(mock.patch.stopall)

    def test_request_url_and_authentication(self):
        self.session_request.return_value = response({"ok": True})

        self.assertEqual(self.client.request("GET", "/spaces/abc/content/pages", params={"limit": 1}), {"ok": True})
        self.session_request.assert_called_once_with(
            "GET",
            "https://api.gitbook.com/v1/spaces/abc/content/pages",
            params={"limit": 1},
            json=None,
            timeout=TIMEOUT,
        )
        self.assertEqual(self.client.session.headers["Authorization"], "Bearer secret")

    def test_request_error_raises(self):
        self.session_request.return_value = response(status=404)
        with self.assertRaises(GitBookError):
            self.client.request("GET", "/spaces/abc/content/pages")

    def test_connection_error_raises(self):
        self.session_request.side_effect = requests.ConnectionError("timed out")
        with self.assertRaises(GitBookError):
            self.client.request("GET", "/spaces/abc/content/pages")

    def test_retries_are_configured(self):
        retry = self.client.session.get_adapter("https://api.gitbook.com").max_retries
        self.assertEqual(retry.total, 3)
        self.assertIn(429, retry.status_forcelist)
        self.assertIn("PUT", retry.allowed_methods)

    def test_list_pages_walks_the_tree(self):
        self.session_request.return_value = response(
            {
                "pages": [
                    {
                        "id": "group",
                        "path": "categories",
                        "pages": [
                            {"id": "page1", "git": {"path": "docs/integration/categories/a.md"}},
                            {"id": "page2", "git": {"path": "docs/integration/categories/b.md"}, "pages": []},
                        ],
                    }
                ]
            }
        )
        self.assertEqual(
            self.client.list_pages("abc"),
            {"docs/integration/categories/a.md": "page1", "docs/integration/categories/b.md": "page2"},
        )

    def test_list_draft_redirects_paginates_and_filters(self):
        destination = {"kind": "site-page", "pageId": "page1"}
        self.session_request.side_effect = [
            response(
                {
                    "items": [
                        {"source": INTAKE_SOURCE, "draft": True, "destination": destination},
                        {"source": "/other/redirect", "draft": True, "destination": destination},
                    ],
                    "next": {"page": "cursor"},
                }
            ),
            response({"items": [{"source": INTAKE_SOURCE_2, "draft": False, "destination": destination}]}),
        ]

        self.assertEqual(self.client.list_redirects("org", "site", draft=True), {INTAKE_SOURCE: destination})
        self.assertEqual(self.session_request.call_args.kwargs["params"]["page"], "cursor")
        self.assertEqual(self.session_request.call_args.kwargs["params"]["draft"], "true")

    def test_list_live_redirects(self):
        destination = {"kind": "site-page", "pageId": "page1"}
        self.session_request.return_value = response(
            {"items": [{"source": INTAKE_SOURCE, "draft": False, "destination": destination}]}
        )

        self.assertEqual(self.client.list_redirects("org", "site", draft=False), {INTAKE_SOURCE: destination})
        self.assertEqual(self.session_request.call_args.kwargs["params"]["draft"], "false")

    def test_push_draft_redirects_in_batches(self):
        self.session_request.return_value = response(
            {"results": [{"source": INTAKE_SOURCE, "status": "error", "error": "Page not found"}]}
        )
        operations = [{"source": f"/s/{i}", "destination": None} for i in range(501)]

        errors = self.client.push_draft_redirects("org", "site", operations)

        batches = [call.kwargs["json"]["redirects"] for call in self.session_request.call_args_list]
        self.assertEqual([len(batch) for batch in batches], [500, 1])
        self.assertTrue(all(operation["intent"] == "draft" for batch in batches for operation in batch))
        self.assertEqual(len(errors), 2)

    def test_failing_batch_does_not_stop_the_next_ones(self):
        self.session_request.side_effect = [response(status=500), response({"results": []})]
        operations = [{"source": f"/s/{i}", "destination": None} for i in range(501)]

        errors = self.client.push_draft_redirects("org", "site", operations)

        self.assertEqual(self.session_request.call_count, 2)
        self.assertEqual(len(errors), 500)


class MainTests(RepositoryTestCase):
    ENV: ClassVar[dict[str, str]] = {
        "GITBOOK_TOKEN": "secret",
        "GITBOOK_ORG": "org",
        "GITBOOK_SITE": "site",
        "GITBOOK_SPACE": "space",
        "GITBOOK_SITE_SPACE": "sitesp",
    }

    def setUp(self):
        super().setUp()
        mock.patch.object(sync_gitbook_redirects, "DOCS_DIR", self.docs_dir).start()
        # the guards have dedicated tests and would be triggered by this small fixture
        mock.patch.object(sync_gitbook_redirects, "MAX_MISSING_PAGES_RATIO", 1).start()
        mock.patch.object(sync_gitbook_redirects, "MAX_DELETE_RATIO", 1).start()
        self.client = mock.patch.object(sync_gitbook_redirects, "GitBookClient").start().return_value
        self.addCleanup(mock.patch.stopall)

        # new: to create / changed: page moved / missing: no GitBook page / orphan: page removed
        self.write("new.md", f"uuid: {INTAKE_UUID}\ntype: intake\n")
        self.write("changed.md", f"uuid: {INTAKE_UUID_2}\ntype: intake\n")
        self.write("missing.md", f"uuid: {ASSET_UUID}\ntype: asset\n")
        self.client.list_pages.return_value = {
            "docs/integration/new.md": "page-new",
            "docs/integration/changed.md": "page-changed",
        }
        self.orphan = "/operation_center/integration_catalog/uuid/00000000-0000-0000-0000-000000000000"
        self.drafts = {
            INTAKE_SOURCE_2: {"kind": "site-page", "pageId": "old-page"},
            self.orphan: {"kind": "site-page", "pageId": "removed"},
        }
        self.live: dict[str, dict] = {}
        self.client.list_redirects.side_effect = lambda org, site, draft: self.drafts if draft else self.live
        self.client.push_draft_redirects.return_value = []

    def run_main(self, *args: str):
        return CliRunner().invoke(main, list(args), env=self.ENV)

    def test_dry_run_pushes_nothing(self):
        result = self.run_main()

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("1 to create, 1 to update, 1 to delete, 0 unchanged", result.output)
        self.assertIn("1 uuid(s) without GitBook page", result.output)
        self.client.push_draft_redirects.assert_not_called()

    def test_apply_pushes_the_diff(self):
        result = self.run_main("--apply")

        self.assertEqual(result.exit_code, 0, result.output)
        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertEqual(
            operations,
            [
                {
                    "source": INTAKE_SOURCE,
                    "destination": {"kind": "site-page", "siteSpaceId": "sitesp", "pageId": "page-new"},
                },
                {
                    "source": INTAKE_SOURCE_2,
                    "destination": {"kind": "site-page", "siteSpaceId": "sitesp", "pageId": "page-changed"},
                },
                {"source": self.orphan, "destination": None},
            ],
        )

    def test_unchanged_redirects_are_not_pushed(self):
        self.drafts = {INTAKE_SOURCE: {"kind": "site-page", "siteSpaceId": "sitesp", "pageId": "page-new"}}

        self.run_main("--apply")

        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertNotIn(INTAKE_SOURCE, [operation["source"] for operation in operations])

    def test_redirect_to_another_site_space_is_updated(self):
        self.drafts = {INTAKE_SOURCE: {"kind": "site-page", "siteSpaceId": "other", "pageId": "page-new"}}

        result = self.run_main("--apply")

        self.assertIn("1 to update", result.output)
        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertIn(INTAKE_SOURCE, [operation["source"] for operation in operations])

    def test_no_delete_keeps_orphans(self):
        self.run_main("--apply", "--no-delete")

        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertNotIn(self.orphan, [operation["source"] for operation in operations])

    def test_api_errors_fail(self):
        self.client.push_draft_redirects.return_value = [{"source": INTAKE_SOURCE, "error": "Page not found"}]

        result = self.run_main("--apply")

        self.assertEqual(result.exit_code, 1)
        self.assertIn("Page not found", result.output)

    def test_live_redirect_is_taken_into_account(self):
        self.live = {INTAKE_SOURCE: {"kind": "site-page", "siteSpaceId": "sitesp", "pageId": "page-new"}}

        result = self.run_main("--apply")

        self.assertIn("0 to create, 1 to update, 1 to delete, 1 unchanged", result.output)
        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertNotIn(INTAKE_SOURCE, [operation["source"] for operation in operations])

    def test_outdated_live_redirect_gets_a_draft(self):
        self.live = {INTAKE_SOURCE: {"kind": "site-page", "siteSpaceId": "sitesp", "pageId": "old-page"}}

        result = self.run_main()

        self.assertIn("0 to create, 2 to update", result.output)

    def test_live_orphans_are_reported_not_deleted(self):
        self.live = {self.orphan.replace("0000-0000-0000", "1111-1111-1111"): {"kind": "site-page"}}

        result = self.run_main("--apply")

        self.assertIn("1 live redirect(s) without page", result.output)
        _, _, operations = self.client.push_draft_redirects.call_args.args
        self.assertEqual(
            [operation["source"] for operation in operations if operation["destination"] is None], [self.orphan]
        )

    def test_no_uuid_is_refused(self):
        for path in self.docs_dir.iterdir():
            path.unlink()

        result = self.run_main("--apply")

        self.assertEqual(result.exit_code, 1)
        self.assertIn("no uuid found", result.output)
        self.client.list_redirects.assert_not_called()
        self.client.push_draft_redirects.assert_not_called()

    def test_missing_pages_guard(self):
        mock.patch.object(sync_gitbook_redirects, "MAX_MISSING_PAGES_RATIO", 0.2).start()

        dry_run = self.run_main()
        self.assertEqual(dry_run.exit_code, 0, dry_run.output)
        self.assertIn("1/3 uuids have no GitBook page", dry_run.output)
        self.assertIn("Check the Git Sync root", dry_run.output)

        refused = self.run_main("--apply")
        self.assertEqual(refused.exit_code, 1)
        self.assertIn("safety guard triggered", refused.output)
        self.client.push_draft_redirects.assert_not_called()

        forced = self.run_main("--apply", "--force")
        self.assertEqual(forced.exit_code, 0, forced.output)
        self.client.push_draft_redirects.assert_called_once()

    def test_delete_guard(self):
        mock.patch.object(sync_gitbook_redirects, "MAX_DELETE_RATIO", 0.2).start()

        refused = self.run_main("--apply")
        self.assertEqual(refused.exit_code, 1)
        self.assertIn("1/2 managed redirects would be deleted", refused.output)
        self.client.push_draft_redirects.assert_not_called()

        self.assertEqual(self.run_main("--apply", "--no-delete").exit_code, 0)

    def test_api_failure_is_reported(self):
        self.client.list_pages.side_effect = GitBookError("GET /spaces/space/content/pages failed (401): denied")

        result = self.run_main()

        self.assertEqual(result.exit_code, 1)
        self.assertIn("failed (401)", result.output)

    def test_missing_token_fails(self):
        result = CliRunner().invoke(main, [], env={**self.ENV, "GITBOOK_TOKEN": None})

        self.assertEqual(result.exit_code, 1)
        self.assertIn("GITBOOK_TOKEN", result.output)
        self.client.list_pages.assert_not_called()

    def test_missing_option_fails(self):
        result = CliRunner().invoke(main, [], env=dict.fromkeys(self.ENV))
        self.assertNotEqual(result.exit_code, 0)
        self.client.list_pages.assert_not_called()


if __name__ == "__main__":
    unittest.main()
