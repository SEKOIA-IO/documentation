import re
import sys
from pathlib import Path

import click

from constants import PREFIXES
from helpers import GitBookClient

REPOSITORY = Path(__file__).resolve().parents[2]
DOCS_DIR = REPOSITORY / "docs" / "integration"

# metadata are expected in the first lines of the page, either one key per line
# (mkdocs format) or flattened on a single line by GitBook
METADATA_LINES = 10
METADATA_RE = re.compile(r"(uuid|name|type):\s*(.*?)(?=\s+(?:uuid|name|type):|$)")
UUID_RE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")


def read_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    with path.open() as f:
        for _, line in zip(range(METADATA_LINES), f):
            line = line.strip()
            if not re.match(r"(uuid|name|type):", line):
                continue
            for key, value in METADATA_RE.findall(line):
                metadata.setdefault(key, value.strip())
    return metadata


def collect_uuids(docs_dir: Path) -> dict[str, tuple[str, str]]:
    """
    Return {source path: (repository file path, type)}
    """
    redirects: dict[str, tuple[str, str]] = {}

    for path in sorted(docs_dir.rglob("*.md", recurse_symlinks=True)):
        metadata = read_metadata(path)
        if "uuid" not in metadata:
            continue

        kind = metadata.get("type", "").lower().partition(" ")[0]
        relative = path.relative_to(docs_dir)
        if kind == "playbook" and relative.parts[0] != "action_library":
            continue
        if kind not in PREFIXES:
            continue

        git_path = path.relative_to(REPOSITORY).as_posix()
        for uuid in UUID_RE.findall(metadata["uuid"]):
            source = PREFIXES[kind] + uuid.lower()
            # several pages can share a format: as the mkdocs plugin, the last one wins
            if source in redirects:
                print(f"! {uuid} shared by {redirects[source][0]} and {git_path}, keeping the latter")
            redirects[source] = (git_path, kind)

    return redirects


@click.command()
@click.option("--token", envvar="GITBOOK_TOKEN", required=True, help="GitBook personal access token")
@click.option("--org", envvar="GITBOOK_ORG", required=True, help="organization id")
@click.option("--site", envvar="GITBOOK_SITE", required=True, help="site id (site_...)")
@click.option("--space", envvar="GITBOOK_SPACE", required=True, help="id of the space synchronized with docs/integration")
@click.option("--site-space", envvar="GITBOOK_SITE_SPACE", required=True, help="id of this space in the site (sitesp_...)")
@click.option("--apply", is_flag=True, help="push the changes as draft redirects")
@click.option("--no-delete", is_flag=True, help="keep the draft redirects not matching any page")
def main(token: str, org: str, site: str, space: str, site_space: str, apply: bool, no_delete: bool):
    """
    Synchronize GitBook site redirects from the `uuid` metadata of the documentation pages.

    It replaces the mkdocs plugin `plugins/integration_by_uuid.py`: every page holding an
    `uuid` metadata gets a redirect `/<prefix>/uuid/<uuid>` pointing to the GitBook page.

    Redirects are only pushed as drafts: they have to be enabled from the GitBook UI
    (Site > Settings > Redirects > Draft).

    \b
    Usage (from scripts/gitbook):
        uv run sync_gitbook_redirects.py            # dry-run, print the changes
        uv run sync_gitbook_redirects.py --apply    # push the changes as drafts
    """
    gitbook = GitBookClient(token)

    wanted = collect_uuids(DOCS_DIR)
    pages = gitbook.list_pages(space)
    existing = gitbook.list_draft_redirects(org, site)

    operations: list[dict] = []
    missing_pages: list[str] = []
    created = updated = unchanged = 0

    for source, (git_path, _) in sorted(wanted.items()):
        page_id = pages.get(git_path)
        if page_id is None:
            missing_pages.append(f"{source} -> {git_path}")
            continue

        destination = {"kind": "site-page", "siteSpaceId": site_space, "pageId": page_id}
        current = existing.get(source)
        if current is None:
            created += 1
            print(f"+ {source} -> {git_path}")
        elif current.get("kind") == "site-page" and current.get("pageId") == page_id:
            unchanged += 1
            continue
        else:
            updated += 1
            print(f"~ {source} -> {git_path}")
        operations.append({"source": source, "destination": destination})

    deleted = 0
    if not no_delete:
        for source in sorted(set(existing) - set(wanted)):
            deleted += 1
            print(f"- {source}")
            operations.append({"source": source, "destination": None})

    if missing_pages:
        print(f"\n{len(missing_pages)} uuid(s) without GitBook page (skipped):")
        for line in missing_pages:
            print(f"  {line}")

    print(
        f"\n{len(wanted)} uuids: {created} to create, {updated} to update, "
        f"{deleted} to delete, {unchanged} unchanged"
    )

    if not apply:
        print("Dry-run: nothing pushed (use --apply to push the drafts)")
        return

    if not operations:
        return

    errors = gitbook.push_draft_redirects(org, site, operations)
    if errors:
        print(f"\n{len(errors)} error(s):")
        for error in errors:
            print(f"  {error.get('source')}: {error.get('error')}")
        sys.exit(1)

    print(f"{len(operations)} draft redirect(s) pushed")


if __name__ == "__main__":
    main()
