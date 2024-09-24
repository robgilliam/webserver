def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        block = block.strip()
        if len(block) > 0:
            blocks.append(block)

    return blocks
