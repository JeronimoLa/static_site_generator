import unittest
import time

from htmlnode import HTMLNode, LeafNode

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