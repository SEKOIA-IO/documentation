import argparse
import re
from pathlib import Path


def update_doc(build_log: str):
    missing_file_re = re.compile(r"Warning: could not find file (.*). Ignoring include statement.")
    missing_includes: list[str] = []

    invalid_links_re = re.compile(
        r"WARNING -  Doc file '(.*)' contains a link '(.*)', "
        r"but the target '(.*)' is not found among documentation files."
    )
    invalid_links: list[str] = []

    with Path(build_log).open() as f:
        for raw_line in f.readlines():
            line = raw_line.strip()

            if find := missing_file_re.match(line):
                missing_includes.append(find.group(1))

            if find := invalid_links_re.match(line):
                source = find.group(1)
                target = find.group(3)
                invalid_links.append(f"`{target}` in `{source}`")

    if len(missing_includes):
        print()
        print("The following included file is missing from the repository:")
        for missing_include in missing_includes:
            print(f"- `{missing_include}`")

    if len(invalid_links):
        print()
        print("The following included file is missing from the repository:")
        for invalid_link in invalid_links:
            print(f"- {invalid_link}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse MkDocs build errors")
    parser.add_argument("build_log", help="Path to the build log")
    args = parser.parse_args()

    update_doc(build_log=args.build_log)
