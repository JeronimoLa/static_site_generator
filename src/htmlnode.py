
from typing import Optional
from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, 
                tag: Optional[str] = None,
                value: Optional[str] = None,
                children: Optional[list] = None,
                props: Optional[dict] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attributes = ""
        for k, v in self.props.items():
	        formatted_str = f'{k}="{v}" '
	        attributes += formatted_str
        return attributes

    def __repr__(self):
        print(f"\nTAG: {self.tag},\nVALUE: {self.value},\nCHILDREN: {self.children},\nPROPS: {self.props},\n")


class LeafNode(HTMLNode):
    def __init__(self, tag:Optional[str] = None, value:str = None, props:dict = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Value parameter is empty")
        if self.tag == None:
            return self.value
        
        if self.props:
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:Optional[str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag does not exist")
        if self.children == None or self.children == []:
            raise ValueError("List is empty")

        format_str = ''
        for child in self.children:
            html_str = child.to_html()
            format_str += html_str

        return f"<{self.tag}>{format_str}</{self.tag}>"

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

if __name__ == "__main__":
    main()