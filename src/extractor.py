import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    tuples = map(lambda match: (match[0], match[1]), matches)
    return list(tuples)

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    tuples = map(lambda match: (match[0], match[1]), matches)
    return list(tuples)