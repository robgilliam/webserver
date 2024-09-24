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

    def test_block_type_paragraph(self):
        block = "This is just a paragraph of text"
        block_type = block_to_blocktype(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_heading(self):
        for h_num in range(1, 11):
            with self.subTest(f"Check heading level {h_num}", h_num = h_num):
                block = "#" * h_num + " heading level " + str(h_num)
                block_type = block_to_blocktype(block)

                if h_num <= 6:
                    self.assertEqual(block_type, block_type_heading)
                else:
                    self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_code(self):
        block = "```\nprint(\"Hello, world!\")\nexit(0)```"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_code)

    def test_block_type_bad_code_too_many_start_backticks(self):
        block = "````\nprint(\"Hello, world!\")\nexit(0)```"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_code_too_many_end_backticks(self):
        block = "```\nprint(\"Hello, world!\")\nexit(0)````"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_code_too_few_start_backticks(self):
        block = "``\nprint(\"Hello, world!\")\nexit(0)```"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_code_too_few_end_backticks(self):
        block = "```\nprint(\"Hello, world!\")\nexit(0)``"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_code_missing_start_backticks(self):
        block = "print(\"Hello, world!\")\nexit(0)```"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_code_missing_end_backticks(self):
        block = "````\nprint(\"Hello, world!\")\nexit(0)"
        block_type = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_quote(self):
        block = "> I wondered lonely as a cloud\n> That floats on high o'er dales and hills\n> When all at once I saw a crowd\n> That confiscated all my pills"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_quote)

    def test_block_type_bad_quote_missing_gt_at_start(self):
        block = "I wondered lonely as a cloud\n> That floats on high o'er dales and hills\n> When all at once I saw a crowd\n> That confiscated all my pills"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_quote_missing_gt(self):
        block = "> I wondered lonely as a cloud\n> That floats on high o'er dales and hills\nWhen all at once I saw a crowd\n> That confiscated all my pills"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_unordered_list_asterisk(self):
        block = "* Apples\n* Pears\n* Oranges\n* Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_unordered_list)

    def test_block_type_unordered_list_hyphen(self):
        block = "- Apples\n- Pears\n- Oranges\n- Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_unordered_list)

    def test_block_type_bad_unordered_list_mixed(self):
        block = "* Apples\n* Pears\n- Oranges\n- Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_unordered_list_missing_asterisk(self):
        block = "* Apples\n* Pears\n Oranges\n* Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_unordered_list_missing_hyphen(self):
        block = "- Apples\n Pears\n- Oranges\n- Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_unordered_list_missing_space_after_asterisk(self):
        block = "*Apples\n*Pears\n*Oranges\n*Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_type_bad_unordered_list_missing_space_after_hyphen(self):
        block = "-Apples\n-Pears\n-Oranges\n-Lemons"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_ordered_list(self):
        block = "1. Get bread from pack\n2. Put bread in toaster\n3. Wait for toaster to pop\n4. Spread butter on bread\n5. Enjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_ordered_list)

    def test_block_bad_ordered_list_jumbled_sequence(self):
        block = "1. Get bread from pack\n3. Put bread in toaster\n2. Wait for toaster to pop\n4. Spread butter on bread\n5. Enjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_bad_ordered_list_skipped_sequence(self):
        block = "1. Get bread from pack\n3. Put bread in toaster\n4. Wait for toaster to pop\n5. Spread butter on bread\n6. Enjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_bad_ordered_list_duplicate_number(self):
        block = "1. Get bread from pack\n2. Put bread in toaster\n2. Wait for toaster to pop\n3. Spread butter on bread\n4. Enjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_bad_ordered_list_missing_space(self):
        block = "1. Get bread from pack\n2. Put bread in toaster\n3. Wait for toaster to pop\n4. Spread butter on bread\n5.Enjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)

    def test_block_bad_ordered_list_missing_number(self):
        block = "1. Get bread from pack\n2. Put bread in toaster\n3. Wait for toaster to pop\n4. Spread butter on bread\nEnjoy!"
        block_type  = block_to_blocktype(block)

        self.assertEqual(block_type, block_type_paragraph)