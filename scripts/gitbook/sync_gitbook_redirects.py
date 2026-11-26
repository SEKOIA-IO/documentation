import os
import re
import sys
from pathlib import Path

import click

from constants import MAX_DELETE_RATIO, MAX_MISSING_PAGES_RATIO, PREFIXES
from helpers import GitBookClient, GitBookError

REPOSITORY = Path(__file__).resolve().parents[2]
DOCS_DIR = REPOSITORY / "docs" / "integration"

# metadata are expected in the first lines of the page, either one key per line
# (mkdocs format) or flattened on a single line by GitBook
METADATA_LINES = 10
METADATA_RE = re.compile(r"(uuid|name|type):\s*(.*?)(?=\s+(?:uuid|name|type):|$)")
UUID_RE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
LATE_UUID_RE = re.compile(rf"^\s*uuid:.*{UUID_RE.pattern}", re.MULTILINE)


def read_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        for _, line in zip(range(METADATA_LINES), f):
            line = line.strip()
            if not re.match(r"(uuid|name|type):", line):
                continue
            for key, value in METADATA_RE.findall(line):
                metadata.setdefault(key, value.strip())
    return metadata


def has_late_uuid(path: Path) -> bool:
    """
    Return True when an `uuid:` line holding a uuid exists after the lines read by `read_metadata`
    """
    with path.open(encoding="utf-8", errors="replace") as f:
        lines = f.readlines()[METADATA_LINES:]
    return LATE_UUID_RE.search("".join(lines)) is not None


def collect_uuids(docs_dir: Path, issues: list[str] | None = None) -> dict[str, tuple[str, str]]:
    """
    Return {source path: (repository file path, type)}

    Pages whose uuid cannot be read (metadata after the first lines, malformed uuid) are
    skipped and reported in `issues`, as they would otherwise lose their redirect silently.
    """
    redirects: dict[str, tuple[str, str]] = {}
    issues = issues if issues is not None else []

    for path in sorted(docs_dir.rglob("*.md", recurse_symlinks=True)):
        metadata = read_metadata(path)
        git_path = path.relative_to(REPOSITORY).as_posix()
        if "uuid" not in metadata:
            if has_late_uuid(path):
                issues.append(f"{git_path}: `uuid:` found after the first {METADATA_LINES} lines")
            continue

        kind = metadata.get("type", "").lower().partition(" ")[0]
        relative = path.relative_to(docs_dir)
        if kind == "playbook" and relative.parts[0] != "action_library":
            continue
        if kind not in PREFIXES:
            continue

        uuids = UUID_RE.findall(metadata["uuid"])
        if not uuids:
            issues.append(f"{git_path}: no valid uuid in `uuid: {metadata['uuid']}`")
            continue

        for uuid in uuids:
            # keep the original case, as the mkdocs plugin did
            source = PREFIXES[kind] + uuid
            # several pages can share a format: as the mkdocs plugin, the last one wins
            if source in redirects:
                print(f"! {uuid} shared by {redirects[source][0]} and {git_path}, keeping the latter")
            redirects[source] = (git_path, kind)

    return redirects


def same_destination(current: dict | None, destination: dict) -> bool:
    return current is not None and all(current.get(key) == value for key, value in destination.items())


@click.command()
@click.option("--org", envvar="GITBOOK_ORG", required=True, help="organization id")
@click.option("--site", envvar="GITBOOK_SITE", required=True, help="site id (site_...)")
@click.option(
    "--space",
    envvar="GITBOOK_SPACE",
    required=True,
    help="id of the space Git-synced with this repository",
)
@click.option(
    "--site-space", envvar="GITBOOK_SITE_SPACE", required=True, help="id of this space in the site (sitesp_...)"
)
@click.option("--apply", is_flag=True, help="push the changes as draft redirects")
@click.option("--no-delete", is_flag=True, help="keep the draft redirects not matching any page")
@click.option("--force", is_flag=True, help="apply even when the safety guards are triggered")
def main(org: str, site: str, space: str, site_space: str, apply: bool, no_delete: bool, force: bool):
    """
    Synchronize GitBook site redirects from the `uuid` metadata of the documentation pages.

    It replaces the mkdocs plugin `plugins/integration_by_uuid.py`: every page holding an
    `uuid` metadata gets a redirect `/<prefix>/uuid/<uuid>` pointing to the GitBook page.

    Pages are matched to GitBook pages by their path in the repository, so the script must
    run from a checkout of the branch the space is Git-synced with.

    Redirects are only pushed as drafts: they have to be enabled from the GitBook UI
    (Site > Settings > Redirects > Draft). Live redirects are read to avoid duplicates,
    but never modified.

    The GitBook personal access token is read from the GITBOOK_TOKEN environment variable.

    \b
    Usage (from scripts/gitbook):
        uv run sync_gitbook_redirects.py            # dry-run, print the changes
        uv run sync_gitbook_redirects.py --apply    # push the changes as drafts
    """
    token = os.environ.get("GITBOOK_TOKEN")
    if not token:
        raise click.ClickException("the GITBOOK_TOKEN environment variable is not set")

    try:
        sync(GitBookClient(token), org, site, space, site_space, apply, no_delete, force)
    except GitBookError as error:
        raise click.ClickException(str(error)) from error


def sync(
    gitbook: GitBookClient,
    org: str,
    site: str,
    space: str,
    site_space: str,
    apply: bool,
    no_delete: bool,
    force: bool,
):
    issues: list[str] = []
    wanted = collect_uuids(DOCS_DIR, issues)
    if not wanted:
        # protects the existing redirects from a wrong DOCS_DIR or an incomplete checkout
        raise click.ClickException(f"no uuid found in {DOCS_DIR}, refusing to synchronize")

    pages = gitbook.list_pages(space)
    drafts = gitbook.list_redirects(org, site, draft=True)
    live = gitbook.list_redirects(org, site, draft=False)

    operations: list[dict] = []
    missing_pages: list[str] = []
    created = updated = unchanged = 0

    for source, (git_path, _) in sorted(wanted.items()):
        page_id = pages.get(git_path)
        if page_id is None:
            missing_pages.append(f"{source} -> {git_path}")
            continue

        destination = {"kind": "site-page", "siteSpaceId": site_space, "pageId": page_id}
        # a pending draft takes precedence over the live redirect it will replace
        current = drafts.get(source, live.get(source))
        if current is None:
            created += 1
            print(f"+ {source} -> {git_path}")
        elif same_destination(current, destination):
            unchanged += 1
            continue
        else:
            updated += 1
            print(f"~ {source} -> {git_path}")
        operations.append({"source": source, "destination": destination})

    deleted = 0
    if not no_delete:
        for source in sorted(set(drafts) - set(wanted)):
            deleted += 1
            print(f"- {source}")
            operations.append({"source": source, "destination": None})

    if issues:
        print(f"\n{len(issues)} page(s) with unreadable uuid (skipped):")
        for line in issues:
            print(f"  {line}")

    if missing_pages:
        print(f"\n{len(missing_pages)} uuid(s) without GitBook page (skipped):")
        for line in missing_pages:
            print(f"  {line}")

    live_orphans = sorted(set(live) - set(wanted))
    if live_orphans:
        print(f"\n{len(live_orphans)} live redirect(s) without page (to remove from the GitBook UI):")
        for source in live_orphans:
            print(f"  {source}")

    print(
        f"\n{len(wanted)} uuids: {created} to create, {updated} to update, {deleted} to delete, {unchanged} unchanged"
    )

    warnings = check_guards(wanted, pages, missing_pages, deleted, issues)
    for warning in warnings:
        print(f"\n! {warning}")

    if not apply:
        print("Dry-run: nothing pushed (use --apply to push the drafts)")
        return

    if warnings and not force:
        raise click.ClickException("safety guard triggered, nothing pushed (use --force to bypass)")

    if not operations:
        return

    errors = gitbook.push_draft_redirects(org, site, operations)
    if errors:
        print(f"\n{len(errors)} error(s):")
        for error in errors:
            print(f"  {error.get('source')}: {error.get('error')}")
        sys.exit(1)

    print(f"{len(operations)} draft redirect(s) pushed")


def check_guards(
    wanted: dict[str, tuple[str, str]],
    pages: dict[str, str],
    missing_pages: list[str],
    deleted: int,
    issues: list[str],
) -> list[str]:
    """
    Return the reasons to refuse pushing the changes
    """
    warnings = []

    if issues:
        warnings.append(f"{len(issues)} page(s) have an unreadable uuid: their redirects would be deleted.")

    if len(missing_pages) > MAX_MISSING_PAGES_RATIO * len(wanted):
        expected = next(iter(wanted.values()))[0]
        example = next(iter(sorted(pages)), "no page with a git path")
        warnings.append(
            f"{len(missing_pages)}/{len(wanted)} uuids have no GitBook page: the repository paths "
            f"(e.g. {expected}) probably do not match the GitBook git paths (e.g. {example}). "
            "Check that this checkout is the branch the space is synced with."
        )

    # compared to the pages of this checkout: a partial checkout makes many drafts orphans
    if deleted > MAX_DELETE_RATIO * len(wanted):
        warnings.append(f"{deleted} draft redirect(s) would be deleted for {len(wanted)} uuids.")

    return warnings


if __name__ == "__main__":
    main()
