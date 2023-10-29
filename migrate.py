import os
import shutil

# Delete and recreate the src/content/docs folder
if os.path.exists("src/content/docs"):
    shutil.rmtree("src/content/docs")
os.makedirs("src/content/docs")

# Find recursively all markdown files following symlinks in the docs and _shared_content folders
for root, dirs, files in os.walk(".", followlinks=True):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            if "docs" in filepath or "_shared_content" in filepath:
                # Duplicate the file to the src/content folder with the first line as the frontmatter title property and the parent folder as a category frontmatter property
                with open(filepath, "r") as f:
                    title = f.readline().strip("#").strip()
                category = os.path.basename(os.path.dirname(filepath))
                new_filepath = os.path.join("src/content/docs", category, file)
                os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
                with open(new_filepath, "w") as f:
                    f.write("---\n")
                    f.write(f"title: {title}\n")
                    f.write(f"category: {category}\n")
                    f.write("---\n")
                    with open(filepath, "r") as f2:
                        f.write(f2.read())
