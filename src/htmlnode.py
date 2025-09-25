
from typing import Optional


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
            formatted_str = f"{k}='{v}'"
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


# if __name__ == "__main__":
    # main()