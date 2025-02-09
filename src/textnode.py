
from enum import Enum

class TextType(Enum):
	normal_text = "normal text"
	bold_text = "bold_text"
	italic_text = "italic_text"
	code_text = "code_text"
	links = "LINKS"
	images = "images"


class TextNode:
	def __init__(self, text, text_type, url):
		self.text = text
		self.text_type = text_type
		self.url = url 

	def __eq__(self, other):
		if self == other:
			return True

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

# print(TextType.normal_text.value)