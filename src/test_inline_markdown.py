
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

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ], 
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
        
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)       
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
