
from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"  # Normal text
    BOLD = "bold"      # Bold text (**text**)
    ITALIC = "italic"  # Italic text (_text_)
    CODE = "code"      # Code text (`text`)
    LINK = "link"      # Links ([anchor text](url))
    IMAGE = "image"    # Images (![alt text](url))

class TextNode:
	def __init__(self, text:str, text_type:TextType, url=None):
		if not isinstance(text_type, TextType):
			raise TypeError(f"text_type must be of TextType, got {type(text_type)}")

		self.text = text
		self.text_type = text_type
		self.url = url 

	def __eq__(self, other):
		if self.text_type == other.text_type:
			return True

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode(None, text_node.text)
            return node
        case TextType.BOLD:
            node = LeafNode("b", text_node.text)
            return node
        case TextType.ITALIC:
            node = LeafNode("i", text_node.text)
            return node
        case TextType.CODE:
            node = LeafNode("code", text_node.text)
            return node
        case TextType.LINK:
            node = LeafNode("a", text_node.text, {"href": "https://www.google.com"})
            return node
        case TextType.IMAGE:
            node = LeafNode("img", "", {"src": "https://www.google.com/image", "alt": "alt text"})
            return node
