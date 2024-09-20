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

if __name__ == "__main__":
    unittest.main()
