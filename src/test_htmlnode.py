import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode(self):
        node = HTMLNode("a", "something here", ['<a>'], {"href": "https://www.google.com", "target": "_blank",})
        self.assertIsInstance(node.props_to_html(), str)

    def test_HTMLNode_properties(self):
        node = HTMLNode()
        for attr, value in node.__dict__.items():
            self.assertEqual(value, None)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")
        
    def test_leaf_to_html_p(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_grandchild_nodes(self):
        first_grandchild_node = LeafNode("p", "grandchild")
        second_grandchild_node = LeafNode("p", "grandchild")
        parent_node = ParentNode("span", [first_grandchild_node, second_grandchild_node])
        self.assertEqual(parent_node.to_html(), "<span><p>grandchild</p><p>grandchild</p></span>")
    
    def test_no_child_nodes(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("span", [])  # Empty children list
            parent_node.to_html()
        self.assertEqual(str(context.exception), "List is empty")

class TestTextToLeafNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
