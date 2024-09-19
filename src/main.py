from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(text_node)

    html_node = HTMLNode("p", "This is an HTML node", props = {"v1":"one", "v2":"two"})

    print(html_node)
    print(html_node.props_to_html())

main()
