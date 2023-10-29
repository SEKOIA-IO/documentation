import os
import shutil
import re

def get_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        frontmatter_dict = {}
        for line in frontmatter.split('\n'):
            if line.strip():
                key, value = line.split(':', 1)
                frontmatter_dict[key.strip()] = value.strip()
        return frontmatter_dict
    else:
        return {}

def process_file(file_path):
    frontmatter = get_frontmatter(file_path)
    title = frontmatter.get('title', os.path.splitext(os.path.basename(file_path))[0])
    category = os.path.basename(os.path.dirname(file_path))
    new_file_path = os.path.join('src', 'content', 'docs', category, os.path.basename(file_path))
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    with open(file_path, 'r') as f:
        content = f.read()
    with open(new_file_path, 'w') as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'category: "{category}"\n')
        for key, value in frontmatter.items():
            if key not in ['title']:
                f.write(f'{key}: {value}\n')
        f.write('---\n')
        f.write(content)

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, followlinks=True):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)



# Delete and recreate the src/content/docs folder
if os.path.exists("src/content/docs"):
    shutil.rmtree("src/content/docs")
os.makedirs("src/content/docs")

process_folder('docs')


docs_dir = "./docs"
src_dir = "./src/content/docs"

docs_files = os.listdir(docs_dir)
src_files = os.listdir(src_dir)

num_docs_files = len([f for f in docs_files if f.endswith(".md")])
num_src_files = len([f for f in src_files if f.endswith(".md")])

print(f"Number of markdown files in docs folder: {num_docs_files}")
print(f"Number of markdown files in src/content/docs folder: {num_src_files}")