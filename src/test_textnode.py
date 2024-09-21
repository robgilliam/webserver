import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://bbc.co.uk/")
        node2 = TextNode("This is a text node", "bold", "https://bbc.co.uk/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://bbc.co.uk/")
        node2 = TextNode("This is a text node", "bold", "https://bbc.com/")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("This is some text", text_type_text)
        expected_node = LeafNode(None, "This is some text")
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This text is in bold", text_type_bold)
        expected_node = LeafNode("b", "This text is in bold")
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This text is in italics", text_type_italic)
        expected_node = LeafNode("i", "This text is in italics")
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This text is a code block", text_type_code)
        expected_node = LeafNode("code", "This text is a code block")
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("This is a link", text_type_link, "http://www.google.com")
        expected_node = LeafNode("a", "This is a link", {"href": "http://www.google.com"})
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("A picture of a poodle", text_type_image, "http://dogpics.org/poodle.jpg")
        expected_node = LeafNode("img", "", {"src": "http://dogpics.org/poodle.jpg", "alt": "A picture of a poodle"})
        self.assertEqual(text_node_to_html_node(text_node), expected_node)

    def test_split_nodes_delimiter_bold(self):
        nodes = [TextNode("This node has **bold text** in it")]
        new_nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This node has ", text_type_text, None),
            TextNode("bold text", text_type_bold, None),
            TextNode(" in it", text_type_text, None)
        ])

    def test_split_nodes_delimiter_italic(self):
        nodes = [TextNode("This node has *italicised text* in it")]
        new_nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This node has ", text_type_text, None),
            TextNode("italicised text", text_type_italic, None),
            TextNode(" in it", text_type_text, None)
        ])

    def test_split_nodes_delimiter_code(self):
        nodes = [TextNode("This node has `embedded code` in it")]
        new_nodes = split_nodes_delimiter(nodes, "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("This node has ", text_type_text, None),
            TextNode("embedded code", text_type_code, None),
            TextNode(" in it", text_type_text, None)
        ])


    def test_split_nodes_image(self):
        nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text, None),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text, None),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_split_nodes_link(self):
        nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link ", text_type_text, None),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text, None),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")
        ])

    def test_text_to_text_nodes(self):
        text = """This is some text
This is some *italic text*
This is some **bold text**
This is some `embedded code`
This is some more text
This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
Here are some pictures: ![rick roll](https://i.imgur.com/aKaOqIh.gif)![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
Goodbye!
"""
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is some text\nThis is some ", text_type_text),
            TextNode("italic text", text_type_italic),
            TextNode("\nThis is some ", text_type_text),
            TextNode("bold text", text_type_bold),
            TextNode("\nThis is some ", text_type_text),
            TextNode("embedded code", text_type_code),
            TextNode("\nThis is some more text\nThis is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
            TextNode("\nHere are some pictures: ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("\nGoodbye!\n", text_type_text),
        ]

        self.assertEqual(nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
