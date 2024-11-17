from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

from extractor import *

from block import *

from os import *

from  shutil import *

def main():
    init_files("static", "public")

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

main()
