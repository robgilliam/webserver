import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "Some value")
        node2 = HTMLNode("tag", "Some value")
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = HTMLNode("tag", "Some value")
        node2 = HTMLNode("tug", "Some value")
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = HTMLNode("tag", "Some value")
        node2 = HTMLNode("tag", "Some other value")
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        node = HTMLNode("tag", "Some value", [ HTMLNode("subtag", "another value") ])
        node2 = HTMLNode("tag", "Some value", [ HTMLNode("subtag", "another value") ])
        self.assertEqual(node, node2)

    def test_not_eq_children(self):
        node = HTMLNode("tag", "Some value", [ HTMLNode("subtag", "another value") ])
        node2 = HTMLNode("tag", "Some value", [ HTMLNode("undertag", "another value") ])
        self.assertNotEqual(node, node2)

    def test_child_order_matters(self):
        node = HTMLNode("tag", "Some value", [ HTMLNode("subtag", "another value"), HTMLNode("subtag", "another 'nother value") ])
        node2 = HTMLNode("tag", "Some value", [ HTMLNode("subtag", "another 'nother value"), HTMLNode("subtag", "another value") ])
        self.assertNotEqual(node, node2)

    def test_eq_props(self):
        node = HTMLNode("tag", "Some value", None, {"fiirst": "one", "second": "two"})
        node2 = HTMLNode("tag", "Some value", None, {"fiirst": "one", "second": "two"})
        self.assertEqual(node, node2)

    def test_not_eq_props(self):
        node = HTMLNode("tag", "Some value", None, {"fiirst": "one", "second": "two"})
        node2 = HTMLNode("tag", "Some value", None, {"fiirst": "one", "second": "2"})
        self.assertNotEqual(node, node2)

    def test_props_order_doesnt_matter(self):
        node = HTMLNode("tag", "Some value", None, {"fiirst": "one", "second": "two"})
        node2 = HTMLNode("tag", "Some value", None, {"second": "two", "fiirst": "one"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props = { "p1":"one", "p2":"two", "p3":"three"})
        html = node.props_to_html()
        self.assertEqual(html, " p1=\"one\" p2=\"two\" p3=\"three\"")

    def test_empty_props_to_html(self):
        node = HTMLNode(props = {})
        html = node.props_to_html()
        self.assertEqual(html, "")

    def test_missing_props_to_html(self):
        node = HTMLNode()
        html = node.props_to_html()
        self.assertEqual(html, "")


if __name__ == "__main__":
    unittest.main()
