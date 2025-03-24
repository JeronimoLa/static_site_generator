import unittest

from enum import Enum
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.bold_text)
		node2 = TextNode("This is a text node", TextType.bold_text)
		self.assertEqual(node, node2)
	
	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.links)
		node2 = TextNode("This is a text node", TextType.bold_text)
		self.assertNotEqual(node, node2)
		
	def test_url_property(self):
		node = TextNode("This is a text node", TextType.links)
		self.assertIsNone(node.url)

	def test_text_types_is_str(self):
		""" Test that all values are of type str """
		for item in TextType:
			self.assertIsInstance(item.value, str)
		
	def test_enum_class_used(self):
		class OtherTextTypeEnum(Enum):
			normal_text = "normal text"

		with self.assertRaises(TypeError):
			TextNode("This is a text node", OtherTextTypeEnum.normal_text)


if __name__ == "__main__":
	unittest.main()	
