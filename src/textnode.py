
from enum import Enum


class TextType(Enum):
	normal_text = "normal text"
	bold_text = "bold_text"
	italic_text = "italic_text"
	code_text = "code_text"
	links = "LINKS"
	images = "images"


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

# print(TextType.normal_text.value)
