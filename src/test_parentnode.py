import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2])
        node2 = ParentNode("box", [child1, child2])
        self.assertEqual(node, node2)

    def test_not_eq_tag(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2])
        node2 = ParentNode("bux", [child1, child2])
        self.assertNotEqual(node, node2)

    def test_not_eq_children(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1])
        node2 = ParentNode("bux", [child2])
        self.assertNotEqual(node, node2)

    def test_child_order_matters(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2])
        node2 = ParentNode("box", [child2, child1])
        self.assertNotEqual(node, node2)

    def test_eq_props(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2], {"fiirst": "one", "second": "two"})
        node2 = ParentNode("box", [child1, child2], {"fiirst": "one", "second": "two"})
        self.assertEqual(node, node2)

    def test_not_eq_props(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2], {"fiirst": "one", "second": "two"})
        node2 = ParentNode("box", [child1, child2], {"fiirst": "one", "second": "2"})
        self.assertNotEqual(node, node2)

    def test_props_order_doesnt_matter(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2], {"fiirst": "one", "second": "two"})
        node2 = ParentNode("box", [child1, child2], {"second": "two", "fiirst": "one"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2])
        html = node.to_html()
        self.assertEqual(html, "<box><tag>Some value</tag><tag>Some other value</tag></box>")

    def test_to_html_with_props(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode("box", [child1, child2], {"first" : "one", "second": "two"})
        html = node.to_html()
        self.assertEqual(html, "<box first=\"one\" second=\"two\"><tag>Some value</tag><tag>Some other value</tag></box>")

    def test_tag_missing(self):
        child1 = LeafNode("tag", "Some value")
        child2 = LeafNode("tag", "Some other value")
        node = ParentNode(None, [child1, child2])
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "ParentNode requires a tag")

    def test_children_missing(self):
        node = ParentNode("box", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "ParentNode has no children")

    def test_children_empty(self):
        node = ParentNode("box", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "ParentNode has no children")

if __name__ == "__main__":
    unittest.main()
