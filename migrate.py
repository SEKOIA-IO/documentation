import os
import shutil

src_dir = "/Users/mathieubellon/Projects/sekoia_official_doc/docs"
dst_dir = "/Users/mathieubellon/Projects/sekoia_official_doc/src/content"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(".md"):
            src_file = os.path.join(root, file)
            with open(src_file, "r") as f:
                title = f.readline().strip()
            dst_file = os.path.join(dst_dir, file)
            with open(dst_file, "w") as f:
                f.write("---\n")
                f.write(f"title: {title}\n")
                f.write("---\n\n")
                with open(src_file, "r") as f2:
                    f.write(f2.read())
            os.remove(src_file)
