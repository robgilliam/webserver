from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(text_node)

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
