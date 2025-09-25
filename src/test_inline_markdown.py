
import unittest

from inline_markdown import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("code block", TextType.CODE),
                                      TextNode(" word", TextType.TEXT),])

    def test_multiple_code_elements(self): 
        node = TextNode("This is text with a `code block` word and another `code in here as well` here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("code block", TextType.CODE),
                                      TextNode("word and another", TextType.TEXT),
                                      TextNode("code in here as well", TextType.CODE),
                                      TextNode("here", TextType.TEXT),])


    def test_multiple_code_nodes(self):
        node_1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node_2 = TextNode("This is text with a `code block` word and another `code in here as well` here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_1, node_2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("code block", TextType.CODE),
                                      TextNode(" word", TextType.TEXT),
                                      TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("code block", TextType.CODE),
                                      TextNode("word and another", TextType.TEXT),
                                      TextNode("code in here as well", TextType.CODE),
                                      TextNode("here", TextType.TEXT),])

    def test_bold(self): 
        node = TextNode("This is text with a **bolded phrase** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("bolded phrase", TextType.BOLD),
                                      TextNode(" word", TextType.TEXT),])


    def test_italic(self): 
        node = TextNode("This is text with a _italic phrase_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("italic phrase", TextType.ITALIC),
                                      TextNode(" word", TextType.TEXT),])

class ExtractLinksImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)