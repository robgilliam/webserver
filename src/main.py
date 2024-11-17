from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

from extractor import *

from block import *

from os import *

from  shutil import *

from pathlib import Path

from extractor import extract_title

def main():
    init_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")


def init_files(src_path, dst_path):
    # Start with empty dst_path
    if path.exists(dst_path):
        rmtree(dst_path)

    mkdir(dst_path)

    for p in listdir(src_path):
        sub_path = path.join(src_path, p)
        if (path.isfile(sub_path)):
            print(f"Copying file {sub_path}")
            copy(sub_path, dst_path)

        if (path.isdir(sub_path)):
            print(f"Copying folder {sub_path}")
            init_files(sub_path, path.join(dst_path, p))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #  Read markdown
    markdown = Path(from_path).read_text()

    template = Path(template_path).read_text()

    top_node = markdown_to_html_node(markdown)

    title = extract_title(markdown)

    makedirs(path.dirname(dest_path), exist_ok = True)

    Path(dest_path).write_text(template.replace("{{ Title }}", title).replace("{{ Content }}", top_node.to_html()))

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for p in listdir(dir_path_content):
        content_path = path.join(dir_path_content, p)

        if (path.isfile(content_path)):
            dest_path = Path(path.join(dest_dir_path, p)).with_suffix(".html")
            generate_page(content_path, template_path, dest_path)

        if (path.isdir(content_path)):
            dest_path = path.join(dest_dir_path, p)
            generate_pages_recursive(content_path, template_path, dest_path)


main()
