import re

from functools import reduce

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
