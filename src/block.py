import re

from functools import reduce

from htmlnode import *
from textnode import *
from parentnode import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered"
block_type_ordered_list = "ordered"


def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        block = block.strip()
        if len(block) > 0:
            blocks.append(block)

    return blocks

def block_to_blocktype(block):
    if re.match(r"^#{1,6} ", block) is not None:
        return block_type_heading

    if re.match(r"```[^`]", block[:4]) and re.match(r"[^`]```", block [-4:]):
        return block_type_code

    lines = block.split("\n")

    if all(map(lambda b: b[0] == ">", lines)):
        return block_type_quote

    if all(map(lambda b: b[:2] == "* ", lines)):
        return block_type_unordered_list

    if all(map(lambda b: b[:2] == "- ", lines)):
        return block_type_unordered_list

    for i in range(len(lines)):
        matches = re.findall(r"^(\d+)\. ", lines[i])
        if len(matches) != 1 or str(i+1) != matches[0]:
            return block_type_paragraph

    return block_type_ordered_list

def markdown_to_html_node(markdown):
    nodes = []

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        html_node = block_to_html_node(block)
        nodes.append(html_node)

    return ParentNode("div", nodes)

def block_to_html_node(block):
        block_type = block_to_blocktype(block)

        if block_type == block_type_paragraph:
            return paragraph_to_html_node(block)

        if block_type == block_type_heading:
            return heading_to_html_node(block)

        if block_type == block_type_code:
            return code_to_html_node(block)

        if block_type ==  block_type_ordered_list:
            return olist_to_html_node(block)

        if block_type == block_type_unordered_list:
            return ulist_to_html_node(block)

        if block_type == block_type_quote:
            return quote_to_html_node(block)


def text_to_children(text):
    children = []

    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")

    text = block [level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())

    content = " ".join(new_lines)
    children = text_to_children(content)

    return ParentNode("blockquote", children)