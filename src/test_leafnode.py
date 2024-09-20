import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("tag", "Some value")
        node2 = LeafNode("tag", "Some value")
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        node = LeafNode("tag", "Some value")
        node2 = LeafNode("tug", "Some value")
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = LeafNode("tag", "Some value")
        node2 = LeafNode("tag", "Some other value")
        self.assertNotEqual(node, node2)

    def test_eq_props(self):
        node = LeafNode("tag", "Some value", {"fiirst": "one", "second": "two"})
        node2 = LeafNode("tag", "Some value", {"fiirst": "one", "second": "two"})
        self.assertEqual(node, node2)

    def test_not_eq_props(self):
        node = LeafNode("tag", "Some value", {"fiirst": "one", "second": "two"})
        node2 = LeafNode("tag", "Some value", {"fiirst": "one", "second": "2"})
        self.assertNotEqual(node, node2)

    def test_props_order_doesnt_matter(self):
        node = LeafNode("tag", "Some value", {"fiirst": "one", "second": "two"})
        node2 = LeafNode("tag", "Some value", {"second": "two", "fiirst": "one"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("tag", "Some value")
        html = node.to_html()
        self.assertEqual(html, "<tag>Some value</tag>")

    def test_to_html_with_props(self):
        node = LeafNode("tag", "Some value", {"first" : "one", "second": "two"})
        html = node.to_html()
        self.assertEqual(html, "<tag first=\"one\" second=\"two\">Some value</tag>")

    def test_value_missing(self):
        node = LeafNode("tag", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "LeafNode requires a value")

if __name__ == "__main__":
    unittest.main()
