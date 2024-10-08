from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

from extractor import *

from block import markdown_to_blocks

def main():
    # bold_node = TextNode("This text is in bold", text_type_bold)
    # link_node = TextNode("Click the link!", text_type_link, "https://www.bbc.co.uk")
    # img_node = TextNode("What a nice picture", text_type_image, "https://pictures.org/nice_pic.jpg")

    # print(bold_node)
    # print(link_node)
    # print(img_node)

    # print(text_node_to_html_node(bold_node))
    # print(text_node_to_html_node(link_node))
    # print(text_node_to_html_node(img_node))

    # print(text_node_to_html_node(bold_node).to_html())
    # print(text_node_to_html_node(link_node).to_html())
    # print(text_node_to_html_node(img_node).to_html())

    # html_node = HTMLNode("p", "This is an HTML node", props = {"v1":"one", "v2":"two"})

    # print(html_node)
    # print(html_node.props_to_html())

    # paragraph = LeafNode("p", "This is a paragraph of text.")
    # anchor = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    # print(paragraph)
    # print(anchor)

    # print(paragraph.to_html())
    # print(anchor.to_html())

    # pn = ParentNode("span", [paragraph, anchor])
    # print(pn.to_html())

    # print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    # print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))

    # node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
    # print(split_nodes_link([node]))

    # node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    # print(split_nodes_image([node]))

    text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

For some reason, this block is followed by two blank lines


And now a block followed by 3 blank lines



And then four:




The end."""

    print(text)

    blocks = markdown_to_blocks(text)

    print(blocks)

main()
