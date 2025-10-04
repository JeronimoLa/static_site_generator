
from block_to_html import *
import unittest

class TestMDToHTML(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        
    def test_heading(self):
        md = """
# This is heading one

## This is heading two

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is heading one</h1><h2>This is heading two</h2></div>"
        )
        
    def test_quote(self):
        md = """
> This is the first line of the quote.
> This is the second line of the quote.
> This is the third line of the quote.

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is the first line of the quote.</br>This is the second line of the quote.</br>This is the third line of the quote.</p></blockquote></div>"

        )
        
#     def test_unorderedlist(self):
#         md = """
# - This is the first list item in a list block
# - This is a list item
# - This is another list item

# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"
#         )
        
#     def test_orderedlist(self):
#         md = """
# 1. First item
# 2. Second item
# 3. Third item

# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
#         )
    
        


