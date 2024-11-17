import unittest

from extractor import *

class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(test_text)
        self.assertEqual(images, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_markdown_links(self):
        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(test_text)
        self.assertEqual(links, [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_extract_title_happy_path(self):
        test_markdown = "# Richard III"

        title = extract_title(test_markdown)
        self.assertEqual(title, "Richard III")

    def test_extract_title_other_lines(self):
        test_markdown = "# Richard III\nNow is the winter of our discontent"

        title = extract_title(test_markdown)
        self.assertEqual(title, "Richard III")

    def test_extract_title_not_first_line(self):
        test_markdown = "By William Shakespeare\n# Richard III"

        title = extract_title(test_markdown)
        self.assertEqual(title, "Richard III")

    def test_extract_title_no_title(self):
        test_markdown = "Now is the winter of our discontent"

        with self.assertRaises(ValueError) as context:
            extract_title(test_markdown)

        self.assertEqual(str(context.exception), "No title found")

    def test_extract_title_no_space(self):
        test_markdown = "#Richard III"

        with self.assertRaises(ValueError) as context:
            extract_title(test_markdown)

        self.assertEqual(str(context.exception), "No title found")

    def test_extract_title_bad_level(self):
        test_markdown = "##Richard III"

        with self.assertRaises(ValueError) as context:
            extract_title(test_markdown)

        self.assertEqual(str(context.exception), "No title found")
