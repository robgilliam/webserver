from extractor import *

from leafnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
	def __init__(self, text, text_type = text_type_text, url = None):
			self.text = text
			self.text_type = text_type
			self.url = url

	def __eq__(self, other):
		return (self.text == other.text
				and self.text_type == other.text_type
				and self.url == other.url)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
	if text_node.text_type == text_type_text:
		return LeafNode(None, text_node.text)
	if text_node.text_type == text_type_bold:
		return LeafNode("b", text_node.text)
	if text_node.text_type == text_type_italic:
		return LeafNode("i", text_node.text)
	if text_node.text_type == text_type_code:
		return LeafNode("code", text_node.text)
	if text_node.text_type == text_type_link:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	if text_node.text_type == text_type_image:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	raise ValueError(f"Invalid text type {text_node.text_type}")

def split_nodes_delimiter(nodes, delimiter, text_type):
	new_nodes = []

	for node in nodes:
		if node.text_type != text_type_text:
			new_nodes.append(node)
			continue

		sections = node.text.split(delimiter)
		if len(sections) % 2 == 0:
			raise ValueError("Invalid markdown, formatted section not closed")
		for i in range(len(sections)):
			if sections[i] == "":
				continue
			new_nodes.append(TextNode(sections[i], text_type_text if i % 2 == 0 else text_type))

	return new_nodes

def split_nodes_link(nodes):
	new_nodes = []

	for node in nodes:
		if node.text_type != text_type_text:
			new_nodes.append(node)
			continue

		text = node.text
		links = extract_markdown_links(node.text)
		if len(links) == 0:
			new_nodes.append(node)
			continue
		for (link_text, url) in links:
			sections = text.split(f"[{link_text}]({url})", 1)
			if len(sections) != 2:
				raise ValueError("Invalid markdown, link section not closed")
			if sections[0] != "":
				new_nodes.append(TextNode(sections[0], text_type_text))
			new_nodes.append(TextNode(link_text, text_type_link, url))
			text = sections[1]

		if text != "":
			new_nodes.append(TextNode(text, text_type_text))

	return new_nodes


def split_nodes_image(nodes):
	new_nodes = []

	for node in nodes:
		if node.text_type != text_type_text:
			new_nodes.append(node)
			continue

		text = node.text
		images = extract_markdown_images(node.text)
		if len(images) == 0:
			new_nodes.append(node)
			continue
		for (alt_text, src) in images:
			sections = text.split(f"![{alt_text}]({src})", 1)
			if len(sections) != 2:
				raise ValueError("Invalid markdown, image section not closed")
			if sections[0] != "":
				new_nodes.append(TextNode(sections[0], text_type_text))
			new_nodes.append(TextNode(alt_text, text_type_image, src))
			text = sections[1]

		if text != "":
			new_nodes.append(TextNode(text, text_type_text))

	return new_nodes

def text_to_textnodes(text):
	nodes = [TextNode(text, text_type_text)]

	nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
	nodes =	split_nodes_delimiter(nodes, "*", text_type_italic)
	nodes = split_nodes_delimiter(nodes, "`", text_type_code)
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)

	return nodes