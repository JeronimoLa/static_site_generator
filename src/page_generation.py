import os, time
from block_to_html import markdown_to_html_node
from jinja2 import Template

import shutil

def extract_title(md):
    for line in md.splitlines():
        if line.startswith("# "):
            return line.split()[1]

def generate_page(dir_path_content, template_path, dest_dir_path, base_path):
    # print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
    template_content = open(template_path).read()
    
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for content in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, content)

        if os.path.isfile(path):
            with open(path, "r") as f:
                data = f.read()
                html_node = markdown_to_html_node(data)
                html_str = html_node.to_html()
                title = extract_title(data)
                template = Template(template_content)
                html_text = template.render(Title=title, Content=html_str)
                html_text = html_text.replace("href='/'", f'href="{base_path}"')
                html_text = html_text.replace("src='/'", f'src="{base_path}"')

                with open(dest_dir_path+"/index.html", "w") as fi:
                    fi.write(html_text)

        if os.path.isdir(path):
            dest_dir = os.path.join(dest_dir_path, content)
            generate_page(path, template_path, dest_dir, base_path)
    

if __name__ == "__main__": pass

