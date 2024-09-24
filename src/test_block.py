import unittest

from block import *

class TestBlock(unittest.TestCase):
    def test_empty_text(self):
        test_text = ""
        blocks = markdown_to_blocks(test_text)
        self.assertListEqual(blocks, [])

    def test_blank_line(self):
        test_text = "\n"
        blocks = markdown_to_blocks(test_text)
        self.assertListEqual(blocks, [])

    def test_two_blank_lines(self):
        test_text = "\n\n"
        blocks = markdown_to_blocks(test_text)
        self.assertListEqual(blocks, [])

    def test_three_blank_lines(self):
        test_text = "\n\n\n"
        blocks = markdown_to_blocks(test_text)
        self.assertListEqual(blocks, [])

    def test_unterminated_block(self):
        test_text = "No newlines in this block"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["No newlines in this block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_one_block(self):
        test_text = "This is the first block\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_one_block_one_blank_line(self):
        test_text = "This is the first block\n\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_one_block_two_blank_lines(self):
        test_text = "This is the first block\n\n\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_two_blocks_with_one_blank_line(self):
        test_text = "This is the first block\n\nThis is the second block\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block", "This is the second block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_two_blocks_with_two_blank_lines(self):
        test_text = "This is the first block\n\n\nThis is the second block\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block", "This is the second block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_two_blocks_with_three_blank_lines(self):
        test_text = "This is the first block\n\n\n\nThis is the second block\n"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block", "This is the second block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_three_blocks(self):
        test_text = "This is the first block\n\nThis is the second block\n\nThis is the third block"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block", "This is the second block", "This is the third block"]

        self.assertListEqual(blocks, expected_blocks)

    def test_newline_in_the_block(self):
        test_text = "This is the first block\nThis is still the first block"
        blocks = markdown_to_blocks(test_text)

        expected_blocks = ["This is the first block\nThis is still the first block"]

        self.assertListEqual(blocks, expected_blocks)
