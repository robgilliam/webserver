from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
    bold_node = TextNode("This text is in bold", text_type_bold)
    link_node = TextNode("Click the link!", text_type_link, "https://www.bbc.co.uk")
    img_node = TextNode("What a nice picture", text_type_image, "https://pictures.org/nice_pic.jpg")

    print(bold_node)
    print(link_node)
    print(img_node)

    print(text_node_to_html_node(bold_node))
    print(text_node_to_html_node(link_node))
    print(text_node_to_html_node(img_node))

    print(text_node_to_html_node(bold_node).to_html())
    print(text_node_to_html_node(link_node).to_html())
    print(text_node_to_html_node(img_node).to_html())

    html_node = HTMLNode("p", "This is an HTML node", props = {"v1":"one", "v2":"two"})

    print(html_node)
    print(html_node.props_to_html())

    paragraph = LeafNode("p", "This is a paragraph of text.")
    anchor = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(paragraph)
    print(anchor)

    print(paragraph.to_html())
    print(anchor.to_html())

    pn = ParentNode("span", [paragraph, anchor])
    print(pn.to_html())

main()
